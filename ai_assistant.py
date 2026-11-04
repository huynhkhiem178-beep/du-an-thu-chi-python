"""Ket noi tro ly AI cua So Thu Chi voi Nanobot qua API local."""

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_API_URL = "http://127.0.0.1:8900/v1/chat/completions"
SESSION_ID = "sothuchi-desktop"


def build_finance_context(transactions, budgets):
    """Tao thong tin tong hop; khong dua ghi chu hay tung giao dich vao AI."""
    income = sum(
        item.get("amount", 0) for item in transactions
        if item.get("kind") == "Thu"
    )
    expense = sum(
        item.get("amount", 0) for item in transactions
        if item.get("kind") == "Chi"
    )
    expense_by_category = {}
    for item in transactions:
        if item.get("kind") == "Chi":
            category = item.get("category", "Khac")
            expense_by_category[category] = (
                expense_by_category.get(category, 0) + item.get("amount", 0)
            )

    lines = [
        "Du lieu tong hop tu So Thu Chi (don vi: VND):",
        f"- Tong thu: {income:,}",
        f"- Tong chi: {expense:,}",
        f"- So du: {income - expense:,}",
    ]
    if expense_by_category:
        lines.append("- Chi theo danh muc:")
        for category, amount in sorted(
            expense_by_category.items(), key=lambda pair: pair[1], reverse=True
        ):
            lines.append(f"  + {category}: {amount:,}")
    if budgets:
        lines.append("- Ngan sach thang:")
        for month, amount in sorted(budgets.items()):
            lines.append(f"  + {month}: {amount:,}")
    return "\n".join(lines)


def ask_nanobot(message, finance_context=None, timeout=120):
    """Gui mot cau hoi den Nanobot dang chay tren may hien tai."""
    message = str(message).strip()
    if not message:
        raise ValueError("Hay nhap cau hoi truoc khi gui.")

    api_url = os.environ.get("SOTHUCHI_NANOBOT_URL", DEFAULT_API_URL).strip()
    prompt = (
        "Ban la tro ly AI ho tro ung dung So Thu Chi. "
        "Tra loi bang tieng Viet de hieu, ro rang va khong phan xet. "
        "Chi dua tren so lieu duoc cung cap; neu thieu du lieu thi hay noi ro. "
        "Hay dua ra goi y tham khao, khong tu y thay doi du lieu tai chinh.\n\n"
    )
    if finance_context:
        prompt += finance_context + "\n\n"
    prompt += "Cau hoi cua nguoi dung: " + message

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "session_id": SESSION_ID,
    }
    request = Request(
        api_url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            result = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"Nanobot tra ve loi HTTP {error.code}: {detail}") from error
    except URLError as error:
        raise RuntimeError(
            "Khong ket noi duoc Nanobot. Hay kiem tra Nanobot da duoc cau hinh "
            "va lenh 'nanobot serve' dang chay chua."
        ) from error
    except (TimeoutError, OSError) as error:
        raise RuntimeError(f"Khong the gui yeu cau den Nanobot: {error}") from error
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise RuntimeError("Phan hoi tu Nanobot khong phai JSON hop le.") from error

    try:
        answer = result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as error:
        raise RuntimeError("Nanobot tra ve phan hoi khong dung dinh dang.") from error
    if not isinstance(answer, str) or not answer.strip():
        raise RuntimeError("Nanobot khong tra ve noi dung.")
    return answer.strip()
