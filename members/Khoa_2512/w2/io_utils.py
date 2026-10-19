from models import Task
from models import date
def load_tasks(path) -> list[Task]:
    task_list: list[Task] = []
    with open(path, "r") as file:
        lines = file.readlines()
        for n, line in enumerate(lines):
            if n == 0:  
                continue
            try:
                title, importance_str, effort_str, date_str = (
                    line.strip().split(",")
                )
                importance = int(importance_str)
                effort = float(effort_str)

                year, month, day = map(int, date_str.split("-"))

                task_date = date(day, month, year)
                new_task = Task(title, importance, effort, task_date)

                task_list.append(new_task)

            except ValueError as e:
                print(f"Invalid line at index {n}: {line.strip()} — {e}")
    return task_list
