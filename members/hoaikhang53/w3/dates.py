from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse a due date from an ISO date, relative date, or weekday name."""
    text = text.strip()

    # 1. Parse an ISO date, e.g. "2026-10-30"
    try:
        return date.fromisoformat(text)
    except ValueError:
        pass

    # 2. Parse relative dates
    normalized = text.lower()

    if normalized == "tomorrow":
        return today + timedelta(days=1)

    if normalized == "today":
        return today

    # Parse "in N days", e.g. "in 3 days"
    parts = normalized.split()
    if (
        len(parts) == 3
        and parts[0] == "in"
        and parts[1].isdigit()
        and parts[2] in ("day", "days")
    ):
        return today + timedelta(days=int(parts[1]))

    # 3. Parse weekday names, e.g. "Fri"
    weekdays = {
        "mon": 0,
        "tue": 1,
        "wed": 2,
        "thu": 3,
        "fri": 4,
        "sat": 5,
        "sun": 6,
    }

    if normalized in weekdays:
        target_weekday = weekdays[normalized]
        days_ahead = (target_weekday - today.weekday()) % 7

        # If today is the target weekday, choose next week's occurrence.
        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date expression: {text}")
