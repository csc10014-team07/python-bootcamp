def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check whether a student is eligible to register for the thesis.

    Args:
        credits: Number of credits the student has earned.
        gpa: The student's current GPA.

    Returns:
        True if the student has at least 120 credits and a GPA of at least 2.0,
        otherwise False.
    """
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """List the requirements a student still has to meet for thesis registration.

    Args:
        credits: Number of credits the student has earned.
        gpa: The student's current GPA.

    Returns:
        A list of human-readable messages describing each unmet requirement.
        The list is empty if all requirements are met.
    """
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
