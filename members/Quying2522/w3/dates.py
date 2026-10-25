import re
from datetime import date, timedelta

WEEKDAYS = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]


def parse_due(text: str, today: date) -> date:
    s = text.strip().lower()

    if s == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in (\d+) days?", s)
    if match:
        return today + timedelta(days=int(match.group(1)))

    for index, name in enumerate(WEEKDAYS):
        if s in (name, name[:3]):
            ahead = (index - today.weekday()) % 7 or 7
            return today + timedelta(days=ahead)

    try:
        return date.fromisoformat(s)
    except ValueError:
        raise ValueError(f"cannot parse due date: {text!r}") from None


if __name__ == "__main__":
    today = date(2026, 10, 26)  # thứ Hai

    assert parse_due("2026-10-30", today) == date(2026, 10, 30)
    assert parse_due("tomorrow", today) == date(2026, 10, 27)
    assert parse_due("in 3 days", today) == date(2026, 10, 29)
    assert parse_due("in 1 day", today) == date(2026, 10, 27)
    assert parse_due("Fri", today) == date(2026, 10, 30)
    assert parse_due("friday", today) == date(2026, 10, 30)
    assert parse_due("Sun", today) == date(2026, 11, 1)
    assert parse_due("Mon", today) == date(2026, 11, 2)  # hôm nay là thứ Hai -> tuần sau
    assert parse_due("  TOMORROW ", today) == date(2026, 10, 27)

    for bad in ["", "next week", "funday", "in x days", "2026-13-40", "30/10/2026"]:
        try:
            parse_due(bad, today)
        except ValueError:
            continue
        raise AssertionError(f"{bad!r} should raise ValueError")

    print("all ok")