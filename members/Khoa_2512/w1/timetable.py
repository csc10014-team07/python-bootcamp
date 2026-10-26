"""Group courses by day and sort course names alphabetically."""


def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group course codes by day and sort each day's courses alphabetically.

    Args:
        courses: A list of tuples containing a course code and its day.

    Returns:
        A dictionary mapping each day to a sorted list of course codes.
    """
    result: dict[str, list[str]] = {}

    for course, day in courses:
        result.setdefault(day, []).append(course)

    for day in result:
        result[day].sort()

    return result


print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))