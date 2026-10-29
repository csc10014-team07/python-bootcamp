import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    text = text.strip().lower()

    try:
        return date.fromisoformat(text)
    except ValueError:
        pass

    if text == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in (\d+) days?", text)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    weekdays = {
        "mon": 0,
        "tue": 1,
        "wed": 2,
        "thu": 3,
        "fri": 4,
        "sat": 5,
        "sun": 6,
    }

    if text in weekdays:
        target_weekday = weekdays[text]
        days_ahead = (target_weekday - today.weekday()) % 7

        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: {text}")
