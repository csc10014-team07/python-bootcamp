import pytest
from members.hoangnhatthi1303.w1.grades import summary
from members.hoangnhatthi1303.w1.rules import can_register_thesis, missing
from members.hoangnhatthi1303.w1.text_tools import word_count, top_k
from members.hoangnhatthi1303.w1.timetable import by_day
from members.hoangnhatthi1303.w1.translate import transpose

# --- TEST CHO GRADES.PY (W1-1) ---
def test_summary_normal():
    # Test trường hợp dữ liệu chuẩn
    result = summary([7.5, 9.0, 6.0, 8.0])
    assert result["min"] == 6.0
    assert result["max"] == 9.0
    assert result["mean"] == 7.62
    assert result["median"] == 7.75

def test_summary_empty_exception():
    # Test trường hợp biên: danh sách rỗng phải ném ra ValueError (edge case)
    with pytest.raises(ValueError, match="scores cannot be empty"):
        summary([])


# --- TEST CHO RULES.PY (W1-3) ---
def test_thesis_eligibility():
    # Test đủ điều kiện tốt nghiệp
    assert can_register_thesis(125, 2.5) == True
    assert missing(125, 2.5) == []

    # Test thiếu điều kiện (edge case: thiếu cả tín chỉ lẫn GPA)
    assert can_register_thesis(110, 1.8) == False
    assert len(missing(110, 1.8)) == 2


# --- TEST CHO TEXT_TOOLS.PY (W1-2) ---
def test_word_count_and_top_k():
    text = "Git is fun. Git is fast!"
    counts = word_count(text)
    assert counts["git"] == 2
    assert counts["is"] == 2

    top = top_k(text, 2)
    assert len(top) == 2
    assert top[0][0] in ["git", "is"]


# --- TEST CHO TIMETABLE.PY (W1-5) ---
def test_by_day():
    courses = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon")
    ]
    grouped = by_day(courses)
    # Kiểm tra xem danh sách các môn học trong ngày Mon đã được sắp xếp alphabet chưa
    assert grouped["Mon"] == ["CSC10001", "CSC10014"]
    assert grouped["Tue"] == ["MTH00003"]


# --- TEST CHO TRANSLATE.PY (W1-4) ---
def test_transpose_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    assert transpose(matrix) == expected

def test_transpose_empty():
    # Test trường hợp biên: ma trận rỗng (edge case)
    assert transpose([]) == []