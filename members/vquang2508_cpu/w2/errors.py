"""Custom exceptions and plan feasibility checks."""

from collections.abc import Iterable
from typing import Any


class InfeasiblePlan(Exception):
    """Exception raised when required hours exceed available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        needed_str = int(self.needed_h) if int(self.needed_h) == self.needed_h else self.needed_h
        avail_str = int(self.available_h) if int(self.available_h) == self.available_h else self.available_h
        return (
            f"Infeasible plan: needed {needed_str} hours, "
            f"but only {avail_str} hours available."
        )


def check_feasible(tasks: Iterable[Any], available_h: float) -> None:
    """Check if task effort sum fits within available hours.

    Raises InfeasiblePlan if needed hours exceed available hours.
    """
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)
