# Import các hàm từ thư mục bài làm W1 của hoaikhang53
from members.hoaikhang53.w1.translate import two_sum


# 5. Tests cho translate.py (two_sum)
def test_two_sum_found():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


def test_two_sum_not_found():
    assert two_sum([1, 2, 3], 10) == []
