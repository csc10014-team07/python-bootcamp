"""Command-line tool for planning tasks within an available time budget."""

import argparse
import sys
from collections.abc import Sequence
from datetime import date as PythonDate
from pathlib import Path

from members.Khoa_2512.w2.io_utils import load_tasks
from members.Khoa_2512.w2.models import Task


def days_until(deadline: PythonDate, today: PythonDate) -> int:
    """Return the number of days between today and the deadline."""
    return (deadline - today).days


def priority(task: Task, today: PythonDate) -> float:
    """Calculate a task's priority based on importance, urgency, and effort."""
    days_left = days_until(task.deadline, today)
    urgency = 10 if days_left <= 0 else 1 / days_left

    return (task.importance * 2 + urgency * 5) / task.effort_h


def plan_tasks(
    tasks: list[Task],
    hours: float,
    today: PythonDate,
) -> list[Task]:
    """Select tasks that fit within the available hours, prioritizing urgency."""
    if hours <= 0:
        raise ValueError("hours must be greater than 0")

    candidates = [task for task in tasks if task.effort_h > 0]
    candidates.sort(
        key=lambda task: priority(task, today),
        reverse=True,
    )

    selected: list[Task] = []
    remaining = hours

    for task in candidates:
        if task.effort_h <= remaining:
            selected.append(task)
            remaining -= task.effort_h

    return selected


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Plan tasks within an available time budget."
    )

    parser.add_argument("file", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available hours for tonight",
    )
    parser.add_argument(
        "--today",
        type=PythonDate.fromisoformat,
        default=PythonDate.today(),
        metavar="YYYY-MM-DD",
        help="Today's date (default: current date)",
    )

    args = parser.parse_args(argv)

    if args.hours <= 0:
        parser.error("--hours must be greater than 0")

    return args


def main() -> int:
    """Run the task planner and return an exit code."""
    args = parse_args()

    if not Path(args.file).is_file():
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(args.file)
    except OSError as exc:
        print(
            f"Error: cannot read file '{args.file}': {exc}",
            file=sys.stderr,
        )
        return 1

    selected = plan_tasks(tasks, args.hours, args.today)

    print(f"Tonight ({args.hours:.1f} h):")
    for index, task in enumerate(selected, start=1):
        print(f"{index:2}. {task.title} ...... {task.effort_h:.1f} h")

    return 0


if __name__ == "__main__":
    sys.exit(main())
