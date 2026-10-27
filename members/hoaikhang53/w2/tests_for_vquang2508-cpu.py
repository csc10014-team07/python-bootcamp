import pytest

from translate import binary_search

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