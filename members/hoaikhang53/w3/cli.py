import argparse
import csv
import sys
from datetime import date
from pathlib import Path

from .dates import parse_due


def load_tasks(csv_path: str, today: date) -> list[dict]:
    """Read tasks from a CSV file and parse their deadlines."""
    tasks = []

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {"title", "importance", "effort_h", "deadline"}
        if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
            raise ValueError(
                "CSV must contain title, importance, effort_h, and deadline columns"
            )

        for index, row in enumerate(reader):
            title = row["title"].strip()
            if not title:
                raise ValueError(f"Row {index + 2}: title cannot be empty")

            importance = int(row["importance"])
            effort = float(row["effort_h"])

            if effort < 0:
                raise ValueError(f"Row {index + 2}: effort_h cannot be negative")

            deadline = parse_due(row["deadline"], today)

            tasks.append({
                "title": title,
                "importance": importance,
                "effort_h": effort,
                "deadline": deadline,
                "index": index,
            })

    return tasks


def make_plan(tasks: list[dict], hours: float) -> list[tuple[str, float]]:
    """Allocate available hours to tasks in priority order."""
    tasks = sorted(
        tasks,
        key=lambda task: (
            task["deadline"],
            -task["importance"],
            task["index"],
        ),
    )

    plan = []
    remaining = hours

    for task in tasks:
        if remaining <= 0:
            break

        if task["effort_h"] <= 0:
            continue

        allocated = min(task["effort_h"], remaining)
        plan.append((task["title"], allocated))
        remaining = round(remaining - allocated, 10)

    return plan


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a task plan from a CSV file."
    )
    parser.add_argument("csv_file", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available working hours",
    )
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        metavar="YYYY-MM-DD",
        help="Reference date (defaults to today)",
    )

    args = parser.parse_args()

    if args.hours < 0:
        parser.error("--hours must be non-negative")

    csv_path = Path(args.csv_file)

    if not csv_path.is_file():
        print(f"Error: CSV file not found: {args.csv_file}", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(str(csv_path), args.today)
        plan = make_plan(tasks, args.hours)
    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Tonight ({args.hours:.1f} h):")

    if not plan:
        print("  No tasks to schedule.")
        return 0

    for index, (title, allocated) in enumerate(plan, start=1):
        dots = "." * max(2, 18 - len(title))
        print(f"  {index}. {title} {dots} {allocated:.1f} h")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
