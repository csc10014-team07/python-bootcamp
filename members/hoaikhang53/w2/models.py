from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("Importance must be 1-5")

    def days_left(self, today: date) -> int:
        return max(0, (self.deadline - today).days)


if __name__ == "__main__":
    task = Task(
        title="Finish homework", importance=3, effort_h=2.5, deadline=date(2026, 10, 25)
    )

    print(task.days_left(date(2026, 10, 19)))
    print(task.days_left(date(2026, 10, 25)))
    print(task.days_left(date(2026, 10, 27)))
