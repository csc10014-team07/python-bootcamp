def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    result = []

    if credits < 120:
        result.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        result.append(f"need GPA {2.0 - gpa:.1f} more")

    return result


def main():
    print(can_register_thesis(118, 2.5))
    print(missing(118, 2.5))

    print(can_register_thesis(120, 2.0))
    print(missing(120, 2.0))

    print(can_register_thesis(110, 1.5))
    print(missing(110, 1.5))


if __name__ == "__main__":
    main()
