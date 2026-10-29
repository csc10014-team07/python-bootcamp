"""Date parsing utilities for due dates and task deadlines."""

from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse a deadline expression into a concrete date object.

    Supported formats:
        - ISO date format (e.g., 'YYYY-MM-DD')
        - 'today' and 'tomorrow'
        - 'in N days' or 'in N day'
        - Weekday names (e.g., 'Mon', 'Monday', 'Fri', 'Friday'), resolving to the
          next occurrence strictly after today (1 to 7 days ahead).

    Args:
        text: Date string or relative time expression.
        today: Reference date for relative calculations.

    Returns:
        The resolved deadline date.

    Raises:
        ValueError: If the text expression cannot be recognized as a valid date.
    """
    text = text.strip().lower()

    if text == "today":
        return today

    if text == "tomorrow":
        return today + timedelta(days=1)

    parts = text.split()
    if (
        len(parts) == 3
        and parts[0] == "in"
        and parts[1].isdigit()
        and parts[2] in ("day", "days")
    ):
        return today + timedelta(days=int(parts[1]))

    try:
        return date.fromisoformat(text)
    except ValueError:
        pass

    day_map = {
        "mon": 0,
        "monday": 0,
        "tue": 1,
        "tuesday": 1,
        "wed": 2,
        "wednesday": 2,
        "thu": 3,
        "thursday": 3,
        "fri": 4,
        "friday": 4,
        "sat": 5,
        "saturday": 5,
        "sun": 6,
        "sunday": 6,
    }

    if text in day_map:
        target_weekday = day_map[text]
        current_weekday = today.weekday()
        days_ahead = (target_weekday - current_weekday) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Không nhận diện được định dạng ngày hạn: {text}")
