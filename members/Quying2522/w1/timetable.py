def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for course, day in entries:
        groups.setdefault(day, []).append(course)
    return {day: sorted(courses) for day, courses in groups.items()}


print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))
