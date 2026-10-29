
import argparse
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.allocate import allocate
from shared.study_planner.render import render


def main():
    parser = argparse.ArgumentParser(
        description="Create a study plan for tonight."
    )

    parser.add_argument(
        "file",
        help="Path to the tasks CSV file"
    )

    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours"
    )

    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Today's date in YYYY-MM-DD format"
    )

    args = parser.parse_args()

    if not Path(args.file).is_file():
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        return 1

    try:
        tasks = parse_csv(args.file)

        tasks = prioritise(tasks, args.today)

        blocks = allocate(tasks, args.hours)

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
