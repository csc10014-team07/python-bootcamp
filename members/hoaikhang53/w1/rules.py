def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons = []

    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"need {needed_credits} more credits")

    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")

    return reasons

# Trường hợp A: Đủ điều kiện đăng ký
print("Case A:")
credits, gpa = 120, 3.0
print(f"Credits: {credits}, GPA: {gpa}")
print(f"Can register: {can_register_thesis(credits, gpa)}")
print(f"Missing requirements: {missing(credits, gpa)}")

# Trường hợp B: Thiếu tín chỉ
print("\nCase B:")
credits, gpa = 118, 2.5
print(f"Credits: {credits}, GPA: {gpa}")
print(f"Can register: {can_register_thesis(credits, gpa)}")
print(f"Missing requirements: {missing(credits, gpa)}")

# Trường hợp C: GPA không đạt
print("\nCase C:")
credits, gpa = 125, 1.8
print(f"Credits: {credits}, GPA: {gpa}")
print(f"Can register: {can_register_thesis(credits, gpa)}")
print(f"Missing requirements: {missing(credits, gpa)}")

# Trường hợp D: Thiếu cả tín chỉ và GPA
print("\nCase D:")
credits, gpa = 115, 1.5
print(f"Credits: {credits}, GPA: {gpa}")
print(f"Can register: {can_register_thesis(credits, gpa)}")
print(f"Missing requirements: {missing(credits, gpa)}")