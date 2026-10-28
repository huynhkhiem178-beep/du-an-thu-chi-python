"""Local CLI bridge for OpenClaw. Stores data beside this script."""
import argparse, json, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TX = ROOT / "transactions.json"
BUDGETS = ROOT / "monthly_budgets.json"

def read(path, expected):
    try:
        with path.open(encoding="utf-8") as f: data = json.load(f)
        if not isinstance(data, expected): raise ValueError(f"Invalid format: {path.name}")
        return data
    except FileNotFoundError: return expected()

def write(path, data):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(path)

def valid_month(s):
    try: date.fromisoformat(s + "-01"); return True
    except ValueError: return False

def main():
    p = argparse.ArgumentParser(description="Local Sổ Thu Chi bridge")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("summary")
    ls = sub.add_parser("list"); ls.add_argument("--month"); ls.add_argument("--category")
    add = sub.add_parser("add")
    add.add_argument("--kind", choices=["Thu", "Chi"], required=True)
    add.add_argument("--amount", type=int, required=True)
    add.add_argument("--category", required=True)
    add.add_argument("--day", default=date.today().isoformat())
    add.add_argument("--note", default="")
    bud = sub.add_parser("set-budget")
    bud.add_argument("--month", required=True); bud.add_argument("--amount", type=int, required=True)
    a = p.parse_args(); tx = read(TX, list); budgets = read(BUDGETS, dict)
    if a.cmd == "summary":
        m = date.today().strftime("%Y-%m")
        rows = [t for t in tx if str(t.get("day", "")).startswith(m)]
        income = sum(int(t.get("amount", 0)) for t in rows if t.get("kind") == "Thu")
        expense = sum(int(t.get("amount", 0)) for t in rows if t.get("kind") == "Chi")
        budget = int(budgets.get(m, 0))
        print(json.dumps({"month":m,"income":income,"expense":expense,"balance":income-expense,"budget":budget,"budget_remaining":budget-expense if budget else None,"transaction_count":len(rows)}, ensure_ascii=False))
    elif a.cmd == "list":
        if a.month and not valid_month(a.month): p.error("--month must be YYYY-MM")
        rows = tx
        if a.month: rows = [t for t in rows if str(t.get("day","")).startswith(a.month)]
        if a.category: rows = [t for t in rows if a.category.casefold() in str(t.get("category","")).casefold()]
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    elif a.cmd == "add":
        try: date.fromisoformat(a.day)
        except ValueError: p.error("--day must be YYYY-MM-DD")
        if a.amount <= 0 or not a.category.strip(): p.error("amount must be positive; category required")
        item = {"kind":a.kind,"amount":a.amount,"category":a.category.strip(),"day":a.day,"note":a.note.strip()}
        tx.append(item); write(TX, tx); print(json.dumps({"ok":True,"added":item}, ensure_ascii=False))
    elif a.cmd == "set-budget":
        if not valid_month(a.month) or a.amount < 0: p.error("month must be YYYY-MM and amount >= 0")
        if a.amount == 0: budgets.pop(a.month, None)
        else: budgets[a.month] = a.amount
        write(BUDGETS, budgets); print(json.dumps({"ok":True,"month":a.month,"budget":a.amount}, ensure_ascii=False))

if __name__ == "__main__":
    try: main()
    except (OSError, json.JSONDecodeError, ValueError) as e:
        print(json.dumps({"ok":False,"error":str(e)}, ensure_ascii=False), file=sys.stderr); raise SystemExit(1)
