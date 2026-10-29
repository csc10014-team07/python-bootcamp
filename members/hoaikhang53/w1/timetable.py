def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group course codes by the day of the week they are held.

    Args:
        courses: A list of ``(course, day)`` tuples, e.g. ``("CSC10014", "Mon")``.

    Returns:
        A dict mapping each day to the alphabetically sorted list of courses
        held on that day.
    """
    result = {}

    for course, day in courses:
        result.setdefault(day, []).append(course)

    for day, day_courses in result.items():
        day_courses.sort()

    return result


if __name__ == "__main__":
    # Trường hợp A: Có môn học vào hai ngày khác nhau
    print(
        "Trường hợp A:",
        by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]),
    )

    # Trường hợp B: Tất cả môn học cùng một ngày
    print("Trường hợp B:", by_day([("CSC10002", "Wed"), ("CSC10001", "Wed")]))

    # Trường hợp C: Danh sách rỗng
    print("Trường hợp C:", by_day([]))
