import pytest

# Import các hàm từ thư mục bài làm W1 của hoaikhang53
from members.hoaikhang53.w1.grades import summary
from members.hoaikhang53.w1.rules import can_register_thesis, missing
from members.hoaikhang53.w1.text_tools import word_count, top_k
from members.hoaikhang53.w1.timetable import by_day
from members.hoaikhang53.w1.translate import two_sum


# 1. Tests cho grades.py (summary)
def test_summary_normal_even_length():
    scores = [7.5, 9.0, 6.0, 8.0]
    result = summary(scores)
    assert result == {
        "min": 6.0,
        "max": 9.0,
        "mean": 7.62,
        "median": 7.75
    }

def test_summary_normal_odd_length():
    scores = [5.0, 10.0, 8.0]
    result = summary(scores)
    assert result == {
        "min": 5.0,
        "max": 10.0,
        "mean": 7.67,
        "median": 8.0
    }

def test_summary_single_element():
    result = summary([8.5])
    assert result == {
        "min": 8.5,
        "max": 8.5,
        "mean": 8.5,
        "median": 8.5
    }

def test_summary_empty_list_raises_value_error():
    with pytest.raises(ValueError, match="scores cannot be empty"):
        summary([])


# 2. Tests cho rules.py (can_register_thesis & missing)
def test_can_register_thesis():
    assert can_register_thesis(120, 2.0) is True   # Biên đủ điều kiện
    assert can_register_thesis(130, 3.5) is True   # Đủ điều kiện
    assert can_register_thesis(119, 3.0) is False  # Thiếu tín chỉ
    assert can_register_thesis(125, 1.99) is False # Thiếu GPA
    assert can_register_thesis(100, 1.5) is False  # Thiếu cả hai

def test_missing_requirements():
    assert missing(120, 2.0) == []
    assert missing(118, 2.5) == ["need 2 more credits"]
    assert missing(125, 1.8) == ["GPA must be at least 2.0"]
    assert missing(115, 1.5) == ["need 5 more credits", "GPA must be at least 2.0"]


# 3. Tests cho text_tools.py (word_count & top_k)
def test_word_count_basic():
    text = "Git is fun. Git is fast!"
    expected = {"git": 2, "is": 2, "fun": 1, "fast": 1}
    assert word_count(text) == expected

def test_word_count_empty_text():
    assert word_count("") == {}

def test_top_k():
    text = "apple banana apple cherry banana apple"
    assert top_k(text, 2) == [("apple", 3), ("banana", 2)]

def test_top_k_alphabetical_tie_breaker():
    # Trường hợp biên: Cùng tần suất, sắp xếp theo bảng chữ cái
    text = "cat dog apple"
    assert top_k(text, 2) == [("apple", 1), ("cat", 1)]

def test_top_k_with_k_larger_than_unique_words():
    text = "hello world"
    assert len(top_k(text, 10)) == 2


# 4. Tests cho timetable.py (by_day)
def test_by_day_normal():
    courses = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon")
    ]
    expected = {
        "Mon": ["CSC10001", "CSC10014"],
        "Tue": ["MTH00003"]
    }
    assert by_day(courses) == expected

def test_by_day_empty_list():
    assert by_day([]) == {}


# 5. Tests cho translate.py (two_sum)
def test_two_sum_found():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_not_found():
    assert two_sum([1, 2, 3], 10) == []