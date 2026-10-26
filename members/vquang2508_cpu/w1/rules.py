def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons = []
    if credits < 120:
        needed = 120 - credits
        reasons.append(f"need {needed} more credits")
    if gpa < 2.0:
        reasons.append(f"gpa {gpa} is below minimum requirement 2.0")
    return reasons


so_tin_chi = 115
diem_gpa = 2.4

print(f"Kiểm tra với 115 tín chỉ và GPA {diem_gpa}:")
print("Đủ điều kiện làm luận văn không?", can_register_thesis(so_tin_chi, diem_gpa))
print("Các lý do còn thiếu:", missing(so_tin_chi, diem_gpa))

so_tin_chi = 150
diem_gpa = 1.9

print(f"Kiểm tra với 150 tín chỉ và GPA {diem_gpa}:")
print("Đủ điều kiện làm luận văn không?", can_register_thesis(so_tin_chi, diem_gpa))
print("Các lý do còn thiếu:", missing(so_tin_chi, diem_gpa))
