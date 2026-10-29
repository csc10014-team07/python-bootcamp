import math


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(self.__str__())

    def __str__(self) -> str:
        return (
            f"Plan is infeasible: need {self.needed_h} hours, "
            f"but only {self.available_h} hours are available."
        )


def check_feasible(tasks, available_h: float) -> None:
    if not math.isfinite(available_h) or available_h < 0:
        raise ValueError("available_h must be finite and non-negative")

    needed_h = 0.0

    for task in tasks:
        effort = task.effort_h

        if not math.isfinite(effort) or effort < 0:
            raise ValueError(
                "task effort_h must be finite and non-negative"
            )

        needed_h += effort

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)

