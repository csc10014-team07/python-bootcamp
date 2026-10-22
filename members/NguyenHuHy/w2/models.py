
from dataclasses import dataclass
from datetime import date
import math


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("title cannot be empty")

        if not isinstance(self.importance, int) or not 1 <= self.importance <= 5:
            raise ValueError("importance must be between 1 and 5")

        if not math.isfinite(self.effort_h) or self.effort_h < 0:
            raise ValueError("effort_h must be finite and non-negative")

        if not isinstance(self.deadline, date):
            raise ValueError("deadline must be a date")

    def days_left(self, today: date) -> int:
        return max(0, (self.deadline - today).days)
