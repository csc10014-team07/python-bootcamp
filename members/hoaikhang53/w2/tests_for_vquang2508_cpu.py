
from translate import binary_search


def test_binary_search_finds_middle_element() -> None:
    """binary_search returns the index of an element in the middle of the list."""
    assert binary_search([2, 5, 8, 12, 16, 23, 38], 12) == 3


def test_binary_search_finds_first_element() -> None:
    """binary_search returns 0 when the target is the first element."""
    assert binary_search([2, 5, 8, 12, 16], 2) == 0


def test_binary_search_finds_last_element() -> None:
    """binary_search returns the last index when the target is the last element."""
    assert binary_search([2, 5, 8, 12, 16], 16) == 4


def test_binary_search_returns_minus_one_when_not_found() -> None:
    """binary_search returns -1 when the target is not in the list."""
    assert binary_search([2, 5, 8, 12, 16], 10) == -1


def test_binary_search_empty_list() -> None:
    """binary_search returns -1 when searching an empty list."""
    # Edge case: searching an empty list must return -1.
    assert binary_search([], 10) == -1


def test_binary_search_single_element() -> None:
    """binary_search handles a single-element list for both hit and miss."""
    assert binary_search([7], 7) == 0
    assert binary_search([7], 3) == -1
