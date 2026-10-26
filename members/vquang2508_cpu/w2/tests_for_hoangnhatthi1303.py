from translate import transpose


def test_transpose_standard_rectangular():
    """Case 1: Ma trận chữ nhật thông thường (2 hàng x 3 cột)."""
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert transpose(matrix) == expected


def test_transpose_square():
    """Case 2: Ma trận vuông (2 hàng x 2 cột)."""
    matrix = [[1, 2], [3, 4]]
    expected = [[1, 3], [2, 4]]
    assert transpose(matrix) == expected


def test_transpose_empty():
    """Case 3: Ma trận rỗng (Edge case cơ bản xử lý điều kiện `if not matrix`)."""
    assert transpose([]) == []


def test_transpose_single_row():
    """Case 4: Ma trận chỉ có đúng 1 hàng (1 hàng x 3 cột)."""
    matrix = [[1, 2, 3]]
    expected = [[1], [2], [3]]
    assert transpose(matrix) == expected


def test_transpose_ragged_matrix_creative():
    """Case 5 (Case độc đáo - Giảng viên có thể chưa nghĩ tới):
    Test với ma trận dạng 'ragged matrix' (các hàng có số lượng phần tử không đồng đều,
    ví dụ hàng 1 có 3 phần tử nhưng hàng 2 chỉ có 2 phần tử).
    Do bản chất của hàm zip(*matrix) trong Python, nó sẽ dừng lại ở độ dài của
    iterable ngắn nhất. Case này giúp kiểm tra sự bất cẩn hoặc hành vi thực tế
    của code khi đầu vào không phải là ma trận chuẩn hợp lệ.
    """
    matrix = [[1, 2, 3], [4, 5]]
    expected = [[1, 4], [2, 5]]
    assert transpose(matrix) == expected
