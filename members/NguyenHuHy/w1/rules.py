def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons: list[str] = []

    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        reasons.append(f"need GPA of at least 2.0 (current GPA: {gpa})")

    return reasons


print(can_register_thesis(120, 2.5))
print(can_register_thesis(118, 3.0))

print(missing(118, 1.8))
print(missing(120, 3.0))