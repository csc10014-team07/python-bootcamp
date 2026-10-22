import pytest

from grades import summary
from rules import can_register_thesis, missing
from text_tools import word_count, top_k
from timetable import by_day
from translate import binary_search


def test_summary_even_number_of_scores():
    assert summary([7.5, 9, 6, 8]) == {
        "min": 6,
        "max": 9,
        "mean": 7.62,
        "median": 7.75,
    }


def test_summary_empty_scores_raises_value_error():
    with pytest.raises(ValueError, match="Danh sách điểm không được để trống."):
        summary([])


def test_can_register_thesis_at_exact_thresholds():
    assert can_register_thesis(120, 2.0) is True


def test_missing_reports_both_requirements_in_order():
    result = missing(115, 1.5)

    assert len(result) == 2

    assert any(
        "5" in reason and "credit" in reason.lower()
        for reason in result
    )

    assert any(
        "gpa" in reason.lower() and "2.0" in reason
        for reason in result
    )


def test_word_count_ignores_case_and_common_punctuation():
    assert word_count("Git is fun. git is fast!") == {
        "git": 2,
        "is": 2,
        "fun": 1,
        "fast": 1,
    }


def test_top_k_breaks_frequency_ties_alphabetically():
    assert top_k("banana apple cherry", 2) == [
        ("apple", 1),
        ("banana", 1),
    ]


def test_top_k_zero_returns_empty_list():
    assert top_k("git is fun", 0) == []


def test_by_day_sorts_courses_and_handles_empty_input():
    assert by_day([
        ("CSC10014", "Mon"),
        ("CSC10001", "Mon"),
        ("MTH00003", "Tue"),
    ]) == {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"],
    }
    assert by_day([]) == {}


def test_binary_search_finds_middle_element():
    assert binary_search([2, 5, 8, 12, 16, 23, 38], 12) == 3


def test_binary_search_finds_first_element():
    assert binary_search([2, 5, 8, 12, 16], 2) == 0


def test_binary_search_finds_last_element():
    assert binary_search([2, 5, 8, 12, 16], 16) == 4


def test_binary_search_returns_minus_one_when_not_found():
    assert binary_search([2, 5, 8, 12, 16], 10) == -1


def test_binary_search_empty_list():
    # Edge case: searching an empty list must return -1.
    assert binary_search([], 10) == -1


def test_binary_search_single_element():
    assert binary_search([7], 7) == 0
    assert binary_search([7], 3) == -1