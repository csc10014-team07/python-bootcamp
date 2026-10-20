from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        if self.importance < 1 or self.importance > 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        days = (self.deadline - today).days

        if days < 0:
            return 0

        return days

task = Task(
    "DS exam",
    5,
    6.0,
    date(2026, 10, 30)
)

print(task.days_left(date(2026, 10, 20)))
