"""Task model for study planning."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represents a task with importance, estimated effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")
        self.effort_h = float(self.effort_h)

    def days_left(self, today: date) -> int:
        """Calculate days remaining until deadline, never returning below 0."""
        return max(0, (self.deadline - today).days)
