import csv
import json
import math
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path) -> list[Task]:
    tasks = []
    expected_header = ["title", "importance", "effort_h", "deadline"]

    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        header = next(reader, None)

        if header != expected_header:
            raise ValueError("Line 1: invalid CSV header")

        for line_number, row in enumerate(reader, start=2):
            if not row or all(value.strip() == "" for value in row):
                continue

            try:
                if len(row) != 4:
                    raise ValueError("expected 4 columns")

                title = row[0].strip()
                if not title:
                    raise ValueError("title cannot be empty")

                importance = int(row[1].strip())
                effort_h = float(row[2].strip())

                if not math.isfinite(effort_h) or effort_h < 0:
                    raise ValueError("effort_h must be finite and non-negative")

                deadline = date.fromisoformat(row[3].strip())

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )

                tasks.append(task)

            except (ValueError, OverflowError) as error:
                raise ValueError(
                    f"Line {line_number}: {error}"
                ) from error

    return tasks


def save_json(tasks: list[Task], path) -> None:
    data = []

    for task in tasks:
        item = asdict(task)
        item["deadline"] = task.deadline.isoformat()
        data.append(item)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.write("\n")
