"""Kết nối trợ lý AI của Sổ Thu Chi với Nanobot qua API local."""

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_API_URL = "http://127.0.0.1:8900/v1/chat/completions"
SESSION_ID = "sothuchi-desktop"


def build_finance_context(transactions, budgets):
    """Tạo thông tin tổng hợp; không đưa ghi chú hay từng giao dịch vào AI."""
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
            category = item.get("category", "Khác")
            expense_by_category[category] = (
                expense_by_category.get(category, 0) + item.get("amount", 0)
            )

    lines = [
        "Dữ liệu tổng hợp từ Sổ Thu Chi (đơn vị: VND):",
        f"- Tổng thu: {income:,}",
        f"- Tổng chi: {expense:,}",
        f"- Số dư: {income - expense:,}",
    ]
    if expense_by_category:
        lines.append("- Chi theo danh mục:")
        for category, amount in sorted(
            expense_by_category.items(), key=lambda pair: pair[1], reverse=True
        ):
            lines.append(f"  + {category}: {amount:,}")
    if budgets:
        lines.append("- Ngân sách tháng:")
        for month, amount in sorted(budgets.items()):
            lines.append(f"  + {month}: {amount:,}")
    return "\n".join(lines)


def ask_nanobot(message, finance_context=None, timeout=120):
    """Gửi câu hỏi đến Nanobot đang chạy trên máy hiện tại."""
    message = str(message).strip()
    if not message:
        raise ValueError("Hãy nhập câu hỏi trước khi gửi.")

    api_url = os.environ.get("SOTHUCHI_NANOBOT_URL", DEFAULT_API_URL).strip()
    prompt = (
        "Bạn là trợ lý AI hỗ trợ ứng dụng Sổ Thu Chi. "
        "Trả lời bằng tiếng Việt dễ hiểu, rõ ràng và không phán xét. "
        "Chỉ dựa trên số liệu được cung cấp; nếu thiếu dữ liệu thì hãy nói rõ. "
        "Hãy đưa ra gợi ý tham khảo, không tự ý thay đổi dữ liệu tài chính.\n\n"
    )
    if finance_context:
        prompt += finance_context + "\n\n"
    prompt += "Câu hỏi của người dùng: " + message

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
        raise RuntimeError(f"Nanobot trả về lỗi HTTP {error.code}: {detail}") from error
    except URLError as error:
        raise RuntimeError(
            "Không kết nối được Nanobot. Hãy kiểm tra Nanobot đã được cấu hình "
            "và lệnh 'nanobot serve' đang chạy chưa."
        ) from error
    except (TimeoutError, OSError) as error:
        raise RuntimeError(f"Không thể gửi yêu cầu đến Nanobot: {error}") from error
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise RuntimeError("Phản hồi từ Nanobot không phải JSON hợp lệ.") from error

    try:
        answer = result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as error:
        raise RuntimeError("Nanobot trả về phản hồi không đúng định dạng.") from error
    if not isinstance(answer, str) or not answer.strip():
        raise RuntimeError("Nanobot không trả về nội dung.")
    return answer.strip()
