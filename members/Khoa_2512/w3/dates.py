"""Parse human-readable due dates into Python date objects."""

import re
from datetime import date, timedelta

DAYS: dict[str, int] = {
    "mon": 1,
    "tue": 2,
    "wed": 3,
    "thu": 4,
    "fri": 5,
    "sat": 6,
    "sun": 7,
}


def parse_due(text: str, today: date) -> date:
    """Parse a due-date string and return the corresponding date.

    Supported formats include 'tomorrow', 'in 3 days', weekday
    abbreviations (such as 'mon'), and ISO dates (YYYY-MM-DD).

    Args:
        text: The human-readable due-date string.
        today: The reference date used to calculate relative dates.

    Returns:
        The parsed due date.

    Raises:
        ValueError: If the date format is not recognized.
    """
    data = text.strip().lower()

    if data == "tomorrow":
        return today + timedelta(days=1)

    found = re.match(r"^in\s+(\d+)\s+days?$", data)
    if found:
        delta = int(found.group(1))
        return today + timedelta(days=delta)

    if data in DAYS:
        result = DAYS[data]
        days_ahead = result - today.weekday() - 1

        if days_ahead <= 0:
            days_ahead += 7

        return today + timedelta(days=days_ahead)

    try:
        return date.fromisoformat(data)
    except:
        raise ValueError("Format not recognized.")