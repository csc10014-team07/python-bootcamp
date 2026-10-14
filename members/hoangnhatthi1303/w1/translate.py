
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Return the transpose of a matrix.

    Unlike C++, Python can use zip(*matrix) to transpose rows and columns concisely.
    """
    if not matrix:
        return []

    return [list(row) for row in zip(*matrix)]


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print("Original matrix:")
    for row in matrix:
        print(row)

    result = transpose(matrix)

    print("Transposed matrix:")
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
