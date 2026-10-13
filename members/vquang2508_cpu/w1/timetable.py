from collections import defaultdict


def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = defaultdict(list)
    for course, day in schedule:
        result[day].append(course)

    return {day: sorted(courses) for day, courses in result.items()}

thoi_khoa_bieu = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
gom_nhom = by_day(thoi_khoa_bieu)

print(f"Thời khóa biểu ban đầu: {thoi_khoa_bieu}")
print("Kết quả gom nhóm theo ngày:", gom_nhom)