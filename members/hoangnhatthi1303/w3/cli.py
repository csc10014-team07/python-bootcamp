
"""Command-line interface for the study planner."""

import argparse
import sys
from datetime import date
from pathlib import Path

from members.hoangnhatthi1303.w2.io_utils import load_tasks
from shared.contract import Task as PlannerTask
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise


def main(argv: list[str] | None = None) -> int:
    """Load tasks, create a study plan, and print the result."""
    parser = argparse.ArgumentParser(
        description="Create a study plan from a tasks CSV file."
    )
    parser.add_argument("csv_file", type=Path, help="Path to tasks CSV")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date in YYYY-MM-DD format",
    )
    args = parser.parse_args(argv)

    if not args.csv_file.is_file():
        print(
            f"Error: file not found: {args.csv_file}",
            file=sys.stderr,
        )
        return 1

    try:
        today = (
            date.fromisoformat(args.today)
            if args.today
            else date.today()
        )

        if args.hours < 0:
            raise ValueError("Available hours cannot be negative")

        tasks = load_tasks(args.csv_file)

        planner_tasks = [
            PlannerTask(
                title=task.title,
                importance=task.importance,
                effort_h=task.effort_h,
                deadline=task.deadline,
            )
            for task in tasks
        ]

        ordered_tasks = prioritise(planner_tasks, today)
        blocks = allocate(ordered_tasks, args.hours)

    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    total_hours = sum(block.hours for block in blocks)
    print(f"Tonight ({total_hours:.1f} h):")

    if not blocks:
        print("  No tasks scheduled.")
        return 0

    for index, block in enumerate(blocks, start=1):
        print(
            f"  {index}. {block.task.title} ...... "
            f"{block.hours:.1f} h"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
