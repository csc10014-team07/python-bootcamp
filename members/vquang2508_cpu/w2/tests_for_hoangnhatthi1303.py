"""Tests for hoangnhatthi1303's transpose implementation."""

try:
    from members.hoangnhatthi1303.w1.translate import transpose
except ImportError:
    from translate import transpose


def test_transpose_standard_rectangular() -> None:
    """Case 1: Standard rectangular matrix (2 rows x 3 columns)."""
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert transpose(matrix) == expected


def test_transpose_square() -> None:
    """Case 2: Square matrix (2 rows x 2 columns)."""
    matrix = [[1, 2], [3, 4]]
    expected = [[1, 3], [2, 4]]
    assert transpose(matrix) == expected


def test_transpose_empty() -> None:
    """Case 3: Empty matrix edge case."""
    assert transpose([]) == []


def test_transpose_single_row() -> None:
    """Case 4: Single row matrix (1 row x 3 columns)."""
    matrix = [[1, 2, 3]]
    expected = [[1], [2], [3]]
    assert transpose(matrix) == expected


def test_transpose_ragged_matrix_creative() -> None:
    """Case 5: Ragged matrix with rows of uneven lengths.

    Due to zip(*matrix) behavior in Python, it stops at the length of the shortest
    row. This tests real-world edge cases when input is not rectangular.
    """
    matrix = [[1, 2, 3], [4, 5]]
    expected = [[1, 4], [2, 5]]
    assert transpose(matrix) == expected
