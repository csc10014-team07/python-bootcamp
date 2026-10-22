
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    deadline: date

    def days_left(self, today: date) -> int:
        if not isinstance(today, date):
            raise TypeError("today must be a date")

        if not isinstance(self.deadline, date):
            raise TypeError("deadline must be a date")

        return max(0, (self.deadline - today).days)
