"""Command-line interface for the study planner."""

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

from members.vquang2508_cpu.w3.dates import parse_due
from shared.contract import Task
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def load_planner_tasks(path: str | Path, today: date) -> list[Task]:
    """Load tasks from CSV, supporting both ISO dates and relative deadlines.

    Args:
        path: Path to the tasks CSV file.
        today: Reference date used for relative date calculations.

    Returns:
        A list of Task objects.

    Raises:
        ValueError: If header or row format is invalid.
    """
    tasks: list[Task] = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        expected_header = ["title", "importance", "effort_h", "deadline"]
        if not header or [h.strip() for h in header] != expected_header:
            raise ValueError(
                "Invalid CSV header: expected title,importance,effort_h,deadline"
            )

        for line_number, row in enumerate(reader, start=2):
            if not row or all(c.strip() == "" for c in row):
                continue
            if len(row) != 4:
                raise ValueError(f"Line {line_number}: expected 4 columns")
            title = row[0].strip()
            if not title:
                raise ValueError(f"Line {line_number}: title cannot be empty")
            importance = int(row[1].strip())
            if not 1 <= importance <= 5:
                raise ValueError(
                    f"Line {line_number}: importance must be between 1 and 5"
                )
            effort_h = float(row[2].strip())
            if effort_h < 0:
                raise ValueError(f"Line {line_number}: effort_h must be non-negative")
            deadline = parse_due(row[3].strip(), today)
            tasks.append(
                Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
            )
    return tasks


def main(argv: list[str] | None = None) -> int:
    """Run the study planner CLI to schedule tasks for available study hours.

    Args:
        argv: Optional command-line arguments. If None, sys.argv[1:] is used.

    Returns:
        Exit code: 0 on success, 1 on error.
    """
    parser = argparse.ArgumentParser(description="Study Planner Command Line Tool")
    parser.add_argument(
        "file",
        type=str,
        help="Path to the tasks CSV file",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=str(date.today()),
        help="Reference date in YYYY-MM-DD or relative format (default: today)",
    )

    args = parser.parse_args(argv)

    file_path = Path(args.file)
    if not file_path.is_file():
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        return 1

    if args.hours < 0:
        print("Error: --hours must be non-negative", file=sys.stderr)
        return 1

    try:
        today_date = parse_due(args.today, date.today())
    except ValueError as exc:
        print(f"Error parsing --today: {exc}", file=sys.stderr)
        return 1

    try:
        tasks = load_planner_tasks(file_path, today_date)
        ordered_tasks = prioritise(tasks, today_date)
        blocks = allocate(ordered_tasks, args.hours)

        print(f"Tonight ({args.hours:.1f} h):")
        output = render(blocks)
        if output:
            print(output)
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
