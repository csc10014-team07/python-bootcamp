"""Load task data from a CSV file."""

from pathlib import Path

from .models import Task, date


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file and return a list of valid tasks.

    Args:
        path: The path to the CSV file containing task data.

    Returns:
        A list of valid Task objects. Invalid lines are skipped and reported.
    """
    task_list: list[Task] = []
    with open(path, "r") as file:
        lines = file.readlines()
        for n, line in enumerate(lines):
            if n == 0:
                continue
            try:
                title, importance_str, effort_str, date_str = line.strip().split(",")
                importance = int(importance_str)
                effort = float(effort_str)

                year, month, day = map(int, date_str.split("-"))

                task_date = date(day, month, year)
                new_task = Task(title, importance, effort, task_date)

                task_list.append(new_task)

            except ValueError as e:
                print(f"Invalid line at index {n}: {line.strip()} — {e}")
    return task_list
