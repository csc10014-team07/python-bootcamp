"""Check whether a task plan fits within the available hours."""

from .models import Task


class InfeasiblePlan(Exception):
    """Exception raised when a task plan exceeds the available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Initialize the exception with required and available hours."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        """Return a message describing why the plan is infeasible."""
        return (
            f"Plan is infeasible: needs {self.needed_h:g} hours, "
            f"but only {self.available_h:g} hours are available."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan if the tasks require more than the available hours."""
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
