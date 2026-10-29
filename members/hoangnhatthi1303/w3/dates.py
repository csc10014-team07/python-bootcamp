
"""Utilities for parsing due dates."""

import re
from datetime import date, timedelta

_WEEKDAYS = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tues": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thur": 3,
    "thurs": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse an ISO date, relative date, or weekday into a due date."""
    value = text.strip().lower()

    if not value:
        raise ValueError("Due date cannot be empty")

    if value == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in\s+(\d+)\s+days?", value)
    if match:
        return today + timedelta(days=int(match.group(1)))

    if value in _WEEKDAYS:
        days_ahead = (_WEEKDAYS[value] - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"Unknown due date: {text!r}") from exc
