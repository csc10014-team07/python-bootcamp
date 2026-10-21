class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Infeasible plan: need {self.needed_h} hours, "
            f"but only {self.available_h} hours available."
        )


def check_feasible(tasks, available_h: float) -> None:
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)


# Test
if __name__ == "__main__":
    from dataclasses import dataclass

    @dataclass
    class Task:
        title: str
        effort_h: float

    tasks = [
        Task("DS exam", 6),
        Task("Assignment", 1.5),
    ]

    try:
        check_feasible(tasks, available_h=5)
    except InfeasiblePlan as error:
        print(error)
        print("Needed:", error.needed_h)
        print("Available:", error.available_h)
