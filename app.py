# So thu chi ca nhan - ung dung terminal bang Python
import json
import sys
from datetime import date
from pathlib import Path

transactions = []
# Khi chạy từ source, giữ dữ liệu cạnh app.py. Khi đóng gói thành .exe,
# lưu dữ liệu cạnh file thực thi để dữ liệu còn nguyên sau khi đóng app.
APP_DIR = Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else Path(__file__).resolve().parent
DATA_FILE = APP_DIR / "transactions.json"
BUDGETS_FILE = APP_DIR / "monthly_budgets.json"
monthly_budgets = {}


def load_transactions():
    """Doc giao dich tu file JSON neu file da ton tai."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            saved_transactions = json.load(file)
        if isinstance(saved_transactions, list):
            return [item for item in saved_transactions if isinstance(item, dict)]
        print("File du lieu khong dung dinh dang.")
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Khong doc duoc file JSON. Bat dau voi danh sach rong.")
    return []


def save_transactions():
    """Luu danh sach giao dich vao file JSON."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(transactions, file, ensure_ascii=False, indent=4)
    except OSError:
        print("Khong the ghi file. Giao dich chi duoc giu trong phien nay.")


def load_budgets():
    """Doc ngan sach theo thang tu file JSON."""
    try:
        with open(BUDGETS_FILE, "r", encoding="utf-8") as file:
            saved_budgets = json.load(file)
        if isinstance(saved_budgets, dict):
            return saved_budgets
        print("File ngan sach khong dung dinh dang.")
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Khong doc duoc file ngan sach JSON. Bat dau voi ngan sach rong.")
    return {}


def save_budgets():
    """Luu cac ngan sach theo thang vao file JSON."""
    try:
        with open(BUDGETS_FILE, "w", encoding="utf-8") as file:
            json.dump(monthly_budgets, file, ensure_ascii=False, indent=4)
    except OSError:
        print("Khong the ghi file ngan sach.")


def add_transaction():
    """Nhap mot khoan thu hoac chi."""
    print("\n--- Them giao dich ---")
    print("1. Khoan thu")
    print("2. Khoan chi")
    choice = input("Chon loai giao dich (1/2): ").strip()

    if choice == "1":
        kind = "Thu"
    elif choice == "2":
        kind = "Chi"
    else:
        print("Lua chon khong hop le.")
        return

    try:
        amount = int(input("So tien (VND): ").strip())
    except ValueError:
        print("So tien phai la so nguyen, vi du: 50000.")
        return
    if amount <= 0:
        print("So tien phai lon hon 0.")
        return

    category = input("Danh muc (vi du: an uong, luong): ").strip()
    if not category:
        print("Danh muc khong duoc de trong.")
        return

    transaction_day = input(
        f"Ngay (YYYY-MM-DD, Enter = {date.today().isoformat()}): "
    ).strip()
    if not transaction_day:
        transaction_day = date.today().isoformat()
    try:
        date.fromisoformat(transaction_day)
    except ValueError:
        print("Ngay khong hop le. Hay nhap theo dang YYYY-MM-DD.")
        return

    note = input("Ghi chu (co the de trong): ").strip()
    transaction = {
        "kind": kind,
        "amount": amount,
        "category": category,
        "day": transaction_day,
        "note": note,
    }
    transactions.append(transaction)
    save_transactions()
    print("Da them giao dich!")


def show_transactions(records=None):
    """In cac giao dich duoc truyen vao, hoac tat ca giao dich."""
    if records is None:
        records = transactions

    print("\n--- Danh sach giao dich ---")
    if not records:
        print("Khong tim thay giao dich nao.")
        return

    for number, transaction in enumerate(records, start=1):
        sign = "+" if transaction.get("kind") == "Thu" else "-"
        day = transaction.get("day", "Chua co ngay")
        line = (
            f"{number}. {day} | {transaction.get('kind', 'Khong ro')} | "
            f"{transaction.get('category', 'Khong ro')} | "
            f"{sign}{transaction.get('amount', 0):,} VND"
        )
        if transaction.get("note"):
            line += f" | {transaction['note']}"
        print(line)


def show_summary(records=None, month=None):
    """Tinh tong thu, tong chi va so du cho mot danh sach giao dich."""
    if records is None:
        records = transactions

    total_income = 0
    total_expense = 0
    for transaction in records:
        if transaction.get("kind") == "Thu":
            total_income += transaction.get("amount", 0)
        elif transaction.get("kind") == "Chi":
            total_expense += transaction.get("amount", 0)

    balance = total_income - total_expense
    print("\n--- Tong ket ---")
    print(f"Tong thu:  {total_income:,} VND")
    print(f"Tong chi:  {total_expense:,} VND")
    print(f"So du:     {balance:,} VND")

    if month is not None and month in monthly_budgets:
        budget = monthly_budgets[month]
        remaining = budget - total_expense
        print(f"Ngan sach: {budget:,} VND")
        if remaining < 0:
            print(f"Canh bao: Da vuot ngan sach {abs(remaining):,} VND.")
        elif remaining == 0:
            print("Ban da dung het ngan sach thang nay.")
        else:
            print(f"Con lai:   {remaining:,} VND")


def get_transactions_for_month():
    """Loc giao dich theo thang duoc nhap theo dang YYYY-MM."""
    month = input("Nhap thang can xem (YYYY-MM): ").strip()
    try:
        date.fromisoformat(month + "-01")
    except ValueError:
        print("Thang khong hop le. Hay nhap theo dang YYYY-MM.")
        return None

    month_transactions = [
        transaction for transaction in transactions
        if transaction.get("day", "").startswith(month)
    ]
    return month, month_transactions


def filter_by_month():
    """Hien cac giao dich trong thang duoc chon."""
    result = get_transactions_for_month()
    if result is not None:
        _, month_transactions = result
        show_transactions(month_transactions)


def show_month_summary():
    """Hien tong thu chi trong thang duoc chon."""
    result = get_transactions_for_month()
    if result is not None:
        month, month_transactions = result
        show_summary(month_transactions, month)


def set_monthly_budget():
    """Dat hoac tat ngan sach chi cho mot thang."""
    global monthly_budgets

    month = input("Nhap thang dat ngan sach (YYYY-MM): ").strip()
    try:
        date.fromisoformat(month + "-01")
    except ValueError:
        print("Thang khong hop le. Hay nhap theo dang YYYY-MM.")
        return

    try:
        amount = int(input("Han muc chi (VND, nhap 0 de tat): ").strip())
    except ValueError:
        print("Han muc phai la so nguyen.")
        return

    if amount < 0:
        print("Han muc khong duoc la so am.")
        return

    if amount == 0:
        monthly_budgets.pop(month, None)
        print(f"Da tat ngan sach cho thang {month}.")
    else:
        monthly_budgets[month] = amount
        print(f"Da dat ngan sach thang {month}: {amount:,} VND.")
    save_budgets()


def filter_by_category():
    """Tim giao dich theo ten danh muc."""
    keyword = input("Nhap danh muc can tim: ").strip().casefold()
    if not keyword:
        print("Danh muc khong duoc de trong.")
        return

    matching_transactions = [
        transaction
        for transaction in transactions
        if keyword in transaction.get("category", "").casefold()
    ]
    show_transactions(matching_transactions)


def delete_transaction():
    """Xoa mot giao dich theo so thu tu trong danh sach."""
    show_transactions()
    if not transactions:
        return

    try:
        number = int(input("Nhap so thu tu giao dich muon xoa: ").strip())
    except ValueError:
        print("Hay nhap so thu tu bang chu so.")
        return

    if number < 1 or number > len(transactions):
        print("So thu tu khong ton tai.")
        return

    deleted_transaction = transactions.pop(number - 1)
    save_transactions()
    print(
        f"Da xoa giao dich {deleted_transaction.get('category', 'Khong ro')} "
        f"{deleted_transaction.get('amount', 0):,} VND."
    )


def edit_transaction():
    """Sua thong tin mot giao dich theo so thu tu."""
    show_transactions()
    if not transactions:
        return

    try:
        number = int(input("Nhap so thu tu giao dich muon sua: ").strip())
    except ValueError:
        print("Hay nhap so thu tu bang chu so.")
        return
    if number < 1 or number > len(transactions):
        print("So thu tu khong ton tai.")
        return

    transaction = transactions[number - 1]
    print("Nhan Enter de giu thong tin cu.")

    kind_choice = input("Loai giao dich (1=Thu, 2=Chi): ").strip()
    if kind_choice == "1":
        kind = "Thu"
    elif kind_choice == "2":
        kind = "Chi"
    elif kind_choice == "":
        kind = transaction.get("kind", "Chi")
    else:
        print("Loai giao dich khong hop le. Chua luu thay doi.")
        return

    amount_text = input(f"So tien [{transaction.get('amount', 0)}]: ").strip()
    if amount_text:
        try:
            amount = int(amount_text)
        except ValueError:
            print("So tien phai la so nguyen. Chua luu thay doi.")
            return
        if amount <= 0:
            print("So tien phai lon hon 0. Chua luu thay doi.")
            return
    else:
        amount = transaction.get("amount", 0)

    category_input = input(f"Danh muc [{transaction.get('category', '')}]: ").strip()
    category = category_input or transaction.get("category", "")
    if not category:
        print("Danh muc khong duoc de trong. Chua luu thay doi.")
        return

    day_input = input(f"Ngay YYYY-MM-DD [{transaction.get('day', '')}]: ").strip()
    transaction_day = day_input or transaction.get("day", "")
    try:
        date.fromisoformat(transaction_day)
    except ValueError:
        print("Ngay khong hop le. Chua luu thay doi.")
        return

    note_input = input("Ghi chu (Enter giu nguyen, nhap - de xoa): ")
    if note_input.strip() == "-":
        note = ""
    elif note_input.strip():
        note = note_input.strip()
    else:
        note = transaction.get("note", "")

    transaction.update({
        "kind": kind,
        "amount": amount,
        "category": category,
        "day": transaction_day,
        "note": note,
    })
    save_transactions()
    print("Da cap nhat giao dich.")


def main():
    """Tai du lieu roi hien menu."""
    global transactions, monthly_budgets
    transactions = load_transactions()
    monthly_budgets = load_budgets()

    while True:
        print("\n===== SO THU CHI CA NHAN =====")
        print("1. Them giao dich")
        print("2. Xem tat ca giao dich")
        print("3. Xem tong ket")
        print("4. Loc giao dich theo thang")
        print("5. Loc giao dich theo danh muc")
        print("6. Xem tong ket theo thang")
        print("7. Xoa giao dich")
        print("8. Dat ngan sach cho thang")
        print("9. Sua giao dich")
        print("0. Thoat")
        choice = input("Nhap lua chon: ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_transactions()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            filter_by_month()
        elif choice == "5":
            filter_by_category()
        elif choice == "6":
            show_month_summary()
        elif choice == "7":
            delete_transaction()
        elif choice == "8":
            set_monthly_budget()
        elif choice == "9":
            edit_transaction()
        elif choice == "0":
            print("Hen gap lai!")
            break
        else:
            print("Lua chon khong hop le. Hay chon tu 0 den 9.")


if __name__ == "__main__":
    main()
