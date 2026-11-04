"""Tests for the optional Nanobot assistant integration."""

import ai_assistant


def test_build_finance_context_summarizes_totals_and_categories():
    context = ai_assistant.build_finance_context(
        [
            {"kind": "Thu", "amount": 100000, "category": "Lương", "note": "private"},
            {"kind": "Chi", "amount": 20000, "category": "Ăn uống", "note": "private note"},
            {"kind": "Chi", "amount": 30000, "category": "Học tập", "note": ""},
        ],
        {"2026-11": 200000},
    )

    assert "Tổng thu: 100,000" in context
    assert "Tổng chi: 50,000" in context
    assert "Số dư: 50,000" in context
    assert "Ăn uống: 20,000" in context
    assert "Học tập: 30,000" in context
    assert "private" not in context


def test_build_finance_context_handles_empty_data():
    context = ai_assistant.build_finance_context([], {})
    assert "Tổng thu: 0" in context
    assert "Tổng chi: 0" in context
    assert "Số dư: 0" in context


def test_ask_nanobot_rejects_empty_question():
    try:
        ai_assistant.ask_nanobot("   ")
    except ValueError as error:
        assert "nhập câu hỏi" in str(error)
    else:
        raise AssertionError("Expected ValueError for an empty question")
