"""I/O utilities for loading and saving tasks."""

import csv
import json
from datetime import date
from pathlib import Path

try:
    from .models import Task
except ImportError:
    from models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file.

    Expected header: title,importance,effort_h,deadline.
    Raises ValueError with the line number if any row is invalid.
    """
    path = Path(path)
    tasks: list[Task] = []

    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            return tasks

        expected_header = ["title", "importance", "effort_h", "deadline"]
        cleaned_header = [col.strip() for col in header]
        if cleaned_header != expected_header:
            raise ValueError(
                f"Invalid CSV header: expected {expected_header}, got {cleaned_header}"
            )

        for line_number, row in enumerate(reader, start=2):
            if not row or all(not field.strip() for field in row):
                continue
            if len(row) != 4:
                raise ValueError(
                    f"Invalid row on line {line_number}: expected 4 columns, got {len(row)}"
                )
            try:
                title = row[0].strip()
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = date.fromisoformat(row[3].strip())
                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)
            except Exception as exc:
                raise ValueError(
                    f"Invalid row at line {line_number}: {exc}"
                ) from exc

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks to a JSON file."""
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]
    path = Path(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
