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

    The CSV must have exactly the header ``title,importance,effort_h,deadline``
    and deadlines in ISO format (``YYYY-MM-DD``).

    Args:
        path: Path to the CSV file.

    Returns:
        A list of ``Task`` objects, one per data row.

    Raises:
        ValueError: If the header is invalid or any row cannot be parsed.
    """
    tasks = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        expected_headers = ["title", "importance", "effort_h", "deadline"]

        if reader.fieldnames != expected_headers:
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


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks to a JSON file.

    Deadlines are written as ISO-formatted date strings.

    Args:
        tasks: The tasks to save.
        path: Destination path of the JSON file.
    """
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    csv_path = Path(__file__).with_name("tasks.csv")
    json_path = Path(__file__).with_name("tasks.json")

    tasks = load_tasks(csv_path)

    for task in tasks:
        print(task)

    save_json(tasks, json_path)
    print(f"\nSaved {len(tasks)} tasks to {json_path}")
