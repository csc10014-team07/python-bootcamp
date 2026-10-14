def selection_sort(a: list[int]) -> None:
    """
    Sort a list in ascending order using selection sort.

    Code C++:

  void selection_sort(vector<int>& a) {
      int n = a.size();

      for (int i = 0; i < n - 1; i++) {
          int min_index = i;

          for (int j = i + 1; j < n; j++) {
              if (a[j] < a[min_index]) {
                  min_index = j;
              }
          }

          swap(a[i], a[min_index]);
      }
  }

Khác biệt so với C++:
  - Python dùng len(a) để lấy số phần tử, trong khi C++ dùng a.size().
  - Python không cần khai báo kiểu int cho biến i, j và min_index; C++ cần khai báo kiểu dữ liệu.
  - Python dùng range() để tạo dãy chỉ số lặp, trong khi C++ dùng vòng lặp for với điều kiện.
  - Python dùng tuple assignment: a[i], a[min_index] = a[min_index], a[i] để hoán đổi hai phần tử. C++ thường dùng swap().
  """
    n = len(a)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]


mang = [64, 25, 12, 22, 11]
selection_sort(mang)

print(f"Danh sách sau khi sắp xếp: {mang}")

mang_2 = [5, 3, 8, 1, 2]
selection_sort(mang_2)
print(f"Danh sách sau khi sắp xếp: {mang_2}")

mang_3 = [1, 2, 3, 4, 5]
selection_sort(mang_3)
print(f"Danh sách sau khi sắp xếp: {mang_3}")