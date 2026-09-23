# So thu chi ca nhan - phien ban terminal

transactions = []


def add_transaction():
    """Nhap mot khoan thu hoac chi va them vao danh sach."""
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
        print("So tien phai la mot so nguyen, vi du: 50000.")
        return

    if amount <= 0:
        print("So tien phai lon hon 0.")
        return

    category = input("Danh muc (vi du: an uong, luong): ").strip()
    if not category:
        print("Danh muc khong duoc de trong.")
        return

    note = input("Ghi chu (co the de trong): ").strip()

    transaction = {
        "kind": kind,
        "amount": amount,
        "category": category,
        "note": note,
    }
    transactions.append(transaction)
    print("Da them giao dich!")


def show_transactions():
    """In tat ca giao dich da nhap."""
    print("\n--- Danh sach giao dich ---")
    if not transactions:
        print("Chua co giao dich nao.")
        return

    for number, transaction in enumerate(transactions, start=1):
        sign = "+" if transaction["kind"] == "Thu" else "-"
        line = (
            f"{number}. {transaction['kind']} | "
            f"{transaction['category']} | "
            f"{sign}{transaction['amount']:,} VND"
        )
        if transaction["note"]:
            line += f" | {transaction['note']}"
        print(line)


def show_summary():
    """Tinh tong thu, tong chi va so du."""
    total_income = 0
    total_expense = 0

    for transaction in transactions:
        if transaction["kind"] == "Thu":
            total_income += transaction["amount"]
        else:
            total_expense += transaction["amount"]

    balance = total_income - total_expense
    print("\n--- Tong ket ---")
    print(f"Tong thu:  {total_income:,} VND")
    print(f"Tong chi:  {total_expense:,} VND")
    print(f"So du:     {balance:,} VND")


def main():
    """Hien menu va xu ly lua chon cho den khi nguoi dung thoat."""
    while True:
        print("\n===== SO THU CHI CA NHAN =====")
        print("1. Them giao dich")
        print("2. Xem danh sach giao dich")
        print("3. Xem tong ket thu chi")
        print("0. Thoat")

        choice = input("Nhap lua chon: ").strip()
        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_transactions()
        elif choice == "3":
            show_summary()
        elif choice == "0":
            print("Hen gap lai!")
            break
        else:
            print("Lua chon khong hop le. Hay chon 0, 1, 2 hoac 3.")


if __name__ == "__main__":
    main()
