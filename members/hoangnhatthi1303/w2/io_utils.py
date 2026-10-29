import csv
import json
from dataclasses import asdict
from datetime import date

from .models import Task


def load_tasks(path) -> list[Task]:
    tasks = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        expected = ["title", "importance", "effort_h", "deadline"]
        if reader.fieldnames != expected:
            raise ValueError("Invalid CSV header")

        for line_number, row in enumerate(reader, start=2):
            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"]),
                )
                tasks.append(task)
            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(f"Invalid row at line {line_number}: {exc}") from exc

    return tasks


def save_json(tasks, path):
    data = [{**asdict(task), "deadline": task.deadline.isoformat()} for task in tasks]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
