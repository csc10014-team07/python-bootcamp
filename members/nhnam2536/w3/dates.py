from datetime import date, timedelta
import re

WEEKDAYS = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
}


def parse_due(text: str, today: date) -> date:
  """Parse due date text into a date object."""
  clean_text = text.strip().lower()

  # 1. "tomorrow" case
  if clean_text == "tomorrow":
    return today + timedelta(days=1)

  # 2. "in X days" case
  match = re.match(r"^in\s+(\d+)\s+days?$", clean_text)
  if match:
    days = int(match.group(1))
    return today + timedelta(days=days)

  # 3. "days in week" case
  if clean_text in WEEKDAYS:
    target_weekday = WEEKDAYS[clean_text]
    days_ahead = target_weekday - today.weekday()
    if days_ahead <= 0:  # case: same day or day of previous week -> move to next week
      days_ahead += 7
    return today + timedelta(days=days_ahead)

  # 4. ISO date: "YYYY-MM-DD" case
  try:
    return date.fromisoformat(text.strip())
  except ValueError:
    raise ValueError(f"Unrecognized date format: '{text}'")