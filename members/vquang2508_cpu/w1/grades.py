import statistics


def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Danh sách điểm không được để trống.")

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(statistics.mean(scores), 2),
        "median": round(statistics.median(scores), 2),
    }


diem_nhap = [7.5, 9.0, 6.0, 8.0]
ket_qua = summary(diem_nhap)
print(f"Dữ liệu đầu vào: {diem_nhap}")
print("Kết quả trả về:", ket_qua)
