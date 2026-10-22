
import pytest

from test_tools import word_count, top_k
from grades import summary
from rules import can_register_thesis, missing
from timetable import by_day
from translate import insertion_sort



def test_word_count_basic():
    assert word_count("hello world hello") == {
        "hello": 2,
        "world": 1,
    }


def test_word_count_ignores_case():
    assert word_count("Hello HELLO hello") == {"hello": 3}


def test_word_count_removes_punctuation():
    assert word_count("hello, world! hello.") == {
        "hello": 2,
        "world": 1,
    }


def test_word_count_empty_string():
    assert word_count("") == {}


def test_word_count_multiple_spaces():
    assert word_count("cat   dog  cat") == {
        "cat": 2,
        "dog": 1,
    }

def test_top_k_orders_by_frequency():
    assert top_k("apple banana apple orange banana apple", 2) == [
        ("apple", 3),
        ("banana", 2),
    ]


def test_top_k_alphabetical_tiebreak():
    assert top_k("banana apple cherry", 3) == [
        ("apple", 1),
        ("banana", 1),
        ("cherry", 1),
    ]


def test_top_k_zero():
    assert top_k("apple banana", 0) == []


def test_top_k_negative_k():
    assert top_k("apple banana", -2) == []


def test_top_k_larger_than_word_count():
    assert top_k("cat dog cat", 10) == [
        ("cat", 2),
        ("dog", 1),
    ]


def test_summary_basic():
    assert summary([7.5, 9, 6, 8]) == {
        "min": 6,
        "max": 9,
        "mean": 7.62,
        "median": 7.75,
    }


def test_summary_single_score():
    assert summary([5.0]) == {
        "min": 5.0,
        "max": 5.0,
        "mean": 5.0,
        "median": 5.0,
    }


def test_summary_odd_number_of_scores():
    result = summary([1, 3, 5])
    assert result["median"] == 3


def test_summary_even_number_of_scores():
    result = summary([1, 2, 3, 4])
    assert result["median"] == 2.5


def test_summary_empty_scores():
    with pytest.raises(ValueError, match="scores must not be empty"):
        summary([])


def test_can_register_when_eligible():
    assert can_register_thesis(120, 2.0) is True


def test_cannot_register_insufficient_credits():
    assert can_register_thesis(119, 3.5) is False


def test_cannot_register_low_gpa():
    assert can_register_thesis(130, 1.9) is False


def test_cannot_register_when_both_requirements_fail():
    assert can_register_thesis(100, 1.5) is False


def test_missing_no_requirements():
    assert missing(120, 2.0) == []


def test_missing_both_requirements():
    assert missing(100, 1.5) == [
        "need 20 more credits",
        "need GPA 0.5 more",
    ]



def test_by_day_groups_courses():
    assert by_day([
        ("Math", "Monday"),
        ("Physics", "Tuesday"),
        ("English", "Monday"),
    ]) == {
        "Monday": ["English", "Math"],
        "Tuesday": ["Physics"],
    }


def test_by_day_sorts_courses():
    assert by_day([
        ("Zoology", "Friday"),
        ("Biology", "Friday"),
        ("Chemistry", "Friday"),
    ]) == {
        "Friday": ["Biology", "Chemistry", "Zoology"],
    }


def test_by_day_empty_schedule():
    assert by_day([]) == {}


def test_by_day_single_course():
    assert by_day([("Math", "Monday")]) == {
        "Monday": ["Math"],
    }


def test_by_day_preserves_multiple_courses_on_same_day():
    result = by_day([
        ("Math", "Monday"),
        ("Math", "Monday"),
    ])
    assert result == {"Monday": ["Math", "Math"]}


def test_insertion_sort_unsorted_list():
    assert insertion_sort([4, 2, 5, 1, 3]) == [1, 2, 3, 4, 5]


def test_insertion_sort_already_sorted():
    assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_insertion_sort_reverse_order():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_insertion_sort_empty_list():
    assert insertion_sort([]) == []


def test_insertion_sort_duplicates_and_negatives():
    assert insertion_sort([3, -1, 3, 0, -5]) == [-5, -1, 0, 3, 3]


def test_insertion_sort_returns_same_list_object():
    values = [3, 1, 2]
    result = insertion_sort(values)

    assert result is values
    assert values == [1, 2, 3]
