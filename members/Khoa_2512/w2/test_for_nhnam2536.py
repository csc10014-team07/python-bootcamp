import pytest

from members.nhnam2536.w1.translate import insertion_sort


def test_unsorted_list():
    assert insertion_sort([5, 3, 4, 1]) == [1, 3, 4, 5]


def test_already_sorted_list():
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted_list():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_empty_list():
    assert insertion_sort([]) == []


def test_single_element_list():
    assert insertion_sort([7]) == [7]


def test_duplicate_elements():
    assert insertion_sort([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]


def test_negative_numbers():
    assert insertion_sort([3, -1, -5, 2, 0]) == [-5, -1, 0, 2, 3]


def test_all_elements_equal():
    assert insertion_sort([3, 3, 3, 3]) == [3, 3, 3, 3]


def test_list_with_zero():
    assert insertion_sort([0, 5, -2, 0, 1]) == [-2, 0, 0, 1, 5]


def test_original_list_is_modified():
    numbers = [5, 3, 1, 4]
    result = insertion_sort(numbers)

    assert numbers == [1, 3, 4, 5]
    assert result is numbers
