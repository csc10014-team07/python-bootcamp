class InfeasiblePlan(Exception):
    def __init__(self, needed_h, available_h):
        self.needed_h = needed_h
        self.available_h = available_h

        super().__init__(
            f"Need {needed_h} hours, but only {available_h} hours available"
        )


def check_feasible(tasks, available_h):
    total = 0

    for task in tasks:
        total += task.effort_h

    if total > available_h:
        raise InfeasiblePlan(total, available_h)
