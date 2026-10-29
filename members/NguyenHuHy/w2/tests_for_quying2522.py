import pytest

from members.Quying2522.w1.translate import fib


def test_known_values():
    assert fib(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fib(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_no_fibonacci_for_small_n():
    assert fib(-5) == []
    assert fib(0) == []


def test_upper_bound_is_exclusive():
    assert fib(8) == [0, 1, 1, 2, 3, 5]


def test_fib_up_to_20():
    result = fib(20)
    assert result == [0, 1, 1, 2, 3, 5, 8, 13]


def test_returns_list_of_int():
    result = fib(30)
    assert isinstance(result, list)
    assert all(isinstance(num, int) for num in result)


def test_smallest_boundary():
    assert fib(1) == [0]
    assert fib(2) == [0, 1]


def test_invalid_type():
    with pytest.raises(TypeError):
        fib("10")
