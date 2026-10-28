"""Automated tests for the Sổ Thu Chi data and storage helpers."""

import json

import app


def test_validate_month_accepts_real_month():
    assert app.validate_month("2026-09")
    assert app.validate_month("2024-02")


def test_validate_month_rejects_invalid_values():
    for value in ("2026-13", "2026-2", "26-09", "", None, 202609):
        assert not app.validate_month(value)


def test_validate_transaction_normalizes_valid_record():
    result = app.validate_transaction({
        "kind": "Chi",
        "amount": 50000,
        "category": "  Ăn uống  ",
        "day": "2026-09-28",
        "note": "  Bữa trưa  ",
    })
    assert result == {
        "kind": "Chi",
        "amount": 50000,
        "category": "Ăn uống",
        "day": "2026-09-28",
        "note": "Bữa trưa",
    }


def test_validate_transaction_rejects_bad_data():
    base = {
        "kind": "Thu",
        "amount": 100,
        "category": "Lương",
        "day": "2026-09-01",
        "note": "",
    }
    invalid_records = [
        None,
        [],
        {**base, "kind": "Other"},
        {**base, "amount": 0},
        {**base, "amount": -1},
        {**base, "amount": True},
        {**base, "amount": "100"},
        {**base, "category": "  "},
        {**base, "day": "2026-02-30"},
    ]
    for record in invalid_records:
        assert app.validate_transaction(record) is None


def test_load_transactions_skips_invalid_records_without_overwriting_file(tmp_path, monkeypatch):
    data_file = tmp_path / "transactions.json"
    original = [
        {"kind": "Thu", "amount": 1000, "category": "Lương", "day": "2026-09-01", "note": ""},
        {"kind": "Chi", "amount": "broken", "category": "Ăn uống", "day": "2026-09-02", "note": ""},
    ]
    data_file.write_text(json.dumps(original, ensure_ascii=False), encoding="utf-8")
    monkeypatch.setattr(app, "DATA_FILE", data_file)

    assert app.load_transactions() == [original[0]]
    assert json.loads(data_file.read_text(encoding="utf-8")) == original


def test_load_transactions_handles_malformed_json_without_overwriting(tmp_path, monkeypatch):
    data_file = tmp_path / "transactions.json"
    original = "{this is not json"
    data_file.write_text(original, encoding="utf-8")
    monkeypatch.setattr(app, "DATA_FILE", data_file)

    assert app.load_transactions() == []
    assert data_file.read_text(encoding="utf-8") == original


def test_save_transactions_writes_json_atomically(tmp_path, monkeypatch):
    data_file = tmp_path / "transactions.json"
    monkeypatch.setattr(app, "DATA_FILE", data_file)
    monkeypatch.setattr(app, "transactions", [
        {"kind": "Thu", "amount": 1000, "category": "Lương", "day": "2026-09-01", "note": ""}
    ])

    assert app.save_transactions() is True
    assert json.loads(data_file.read_text(encoding="utf-8")) == app.transactions
    assert list(tmp_path.glob("*.tmp")) == []


def test_load_budgets_keeps_only_valid_months_and_amounts(tmp_path, monkeypatch):
    budget_file = tmp_path / "monthly_budgets.json"
    budget_file.write_text(json.dumps({
        "2026-09": 250000,
        "2026-13": 300000,
        "2026-08": -1,
        "2026-07": True,
        "bad": 100,
    }), encoding="utf-8")
    monkeypatch.setattr(app, "BUDGETS_FILE", budget_file)

    assert app.load_budgets() == {"2026-09": 250000}


def test_save_budgets_writes_json(tmp_path, monkeypatch):
    budget_file = tmp_path / "monthly_budgets.json"
    monkeypatch.setattr(app, "BUDGETS_FILE", budget_file)
    monkeypatch.setattr(app, "monthly_budgets", {"2026-09": 250000})

    assert app.save_budgets() is True
    assert json.loads(budget_file.read_text(encoding="utf-8")) == {"2026-09": 250000}
