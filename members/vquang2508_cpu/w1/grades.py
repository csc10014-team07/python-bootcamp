"""Grade calculation utilities."""

import statistics


def summary(scores: list[float]) -> dict[str, float]:
    """Compute summary statistics for a list of numeric scores.

    Args:
        scores: A list of numeric scores (floats or ints).

    Returns:
        A dictionary containing "min", "max", "mean" (rounded to 2 decimal places),
        and "median" (rounded to 2 decimal places).

    Raises:
        ValueError: If scores is empty.
    """
    if not scores:
        raise ValueError("Danh sách điểm không được để trống.")

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(statistics.mean(scores), 2),
        "median": round(statistics.median(scores), 2),
    }


if __name__ == "__main__":
    diem_nhap = [7.5, 9.0, 6.0, 8.0]
    ket_qua = summary(diem_nhap)
    print(f"Dữ liệu đầu vào: {diem_nhap}")
    print("Kết quả trả về:", ket_qua)
