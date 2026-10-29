"""Algorithm translated from C++ to Python."""


def binary_search(a: list[int], key: int) -> int:
    """Perform binary search on a sorted list of integers.

    Args:
        a: Sorted list of integers.
        key: The target value to find.

    Returns:
        Index of the key if found, or -1 otherwise.
    """
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    mang_da_sap_xep = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    gia_tri_tim = 23
    vi_tri = binary_search(mang_da_sap_xep, gia_tri_tim)

    print(f"Danh sách: {mang_da_sap_xep}")
    print(f"Tìm kiếm số {gia_tri_tim} ở vị trí index:", vi_tri)


# ------------------------------------
"""
code C++:
int binary_search(const std::vector<int>& a, int key) {
    int lo = 0, hi = (int)a.size() - 1; // 1. Khởi tạo 2 con trỏ đầu và cuối
    while (lo <= hi) {                  // 2. Chừng nào khoảng còn hợp lệ
        int mid = lo + (hi - lo) / 2;   // 3. Tìm vị trí ở giữa
        if (a[mid] == key) return mid;  // 4. Nếu trúng thì trả về vị trí
        if (a[mid] < key)
            lo = mid + 1;               // 5. Nếu giữa < key -> tìm nửa phải
        else
            hi = mid - 1;               // 6. Ngược lại -> tìm nửa trái
    }
    return -1;                          // 7. Duyệt hết mà không thấy thì trả về -1
}

khác biệt so với C++:
    - Không cần định nghĩa kiểu dữ liệu tường minh như int hay vector.
    - Sử dụng toán tử '//' thay vì phép chia '/' thông thường để đảm bảo kết quả
      tính vị trí 'mid' luôn là số nguyên (giống cơ chế chia số nguyên của C++).
"""
