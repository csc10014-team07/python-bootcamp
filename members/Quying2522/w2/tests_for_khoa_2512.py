import sys
from pathlib import Path

MEMBERS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(MEMBERS / "Khoa_2512" / "w1"))

from translate import primes_up_to_n


def test_known_values():
    assert primes_up_to_n(10) == [2, 3, 5, 7]
    assert primes_up_to_n(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_no_primes_for_small_n():
    assert primes_up_to_n(-5) == []
    assert primes_up_to_n(0) == []
    assert primes_up_to_n(1) == []
    assert primes_up_to_n(2) == []


def test_upper_bound_is_exclusive():
    assert primes_up_to_n(7) == [2, 3, 5]


def test_primes_up_to_100():
    result = primes_up_to_n(100)
    assert len(result) == 25
    assert result[-1] == 97


def test_returns_list_of_int():
    result = primes_up_to_n(30)
    assert isinstance(result, list)
    assert all(isinstance(p, int) for p in result)
