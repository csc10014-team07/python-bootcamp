from datetime import date
from shared.contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    def calculate_priority_score(task: Task) -> float:
        days_left = (task.deadline - today).days
        if days_left <= 0:
            days_left = 1
        return task.importance / days_left

    return sorted(tasks, key=calculate_priority_score, reverse=True)