import pytest
from members.Quying2522.w1.translate  import selection_sort


def test_unsorted_list():
    a = [64, 25, 12, 22, 11]
    selection_sort(a)
    assert a == [11, 12, 22, 25, 64]


def test_random_order():
    a = [5, 3, 8, 1, 2]
    selection_sort(a)
    assert a == [1, 2, 3, 5, 8]


def test_already_sorted():
    a = [1, 2, 3, 4, 5]
    selection_sort(a)
    assert a == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    a = [5, 4, 3, 2, 1]
    selection_sort(a)
    assert a == [1, 2, 3, 4, 5]


def test_duplicate_elements():
    a = [4, 2, 4, 1, 2, 1]
    selection_sort(a)
    assert a == [1, 1, 2, 2, 4, 4]


def test_empty_list():
    a = []
    selection_sort(a)
    assert a == []


def test_single_element():
    a = [42]
    selection_sort(a)
    assert a == [42]


def test_negative_numbers_and_zero():
    a = [0, -5, 3, -1, 2]
    selection_sort(a)
    assert a == [-5, -1, 0, 2, 3]