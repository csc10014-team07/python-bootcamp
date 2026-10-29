import argparse
from datetime import date

from .allocate import allocate
from .parse import parse_csv
from .prioritise import prioritise
from .render import render


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="python -m shared.study_planner",
        description="Build a study plan from a tasks CSV.",
    )
    parser.add_argument("csv", help="path to the tasks CSV file")
    parser.add_argument(
        "--hours", type=float, required=True, help="total hours available"
    )
    args = parser.parse_args(argv)

    tasks = parse_csv(args.csv)
    tasks = prioritise(tasks, date.today())
    blocks = allocate(tasks, args.hours)
    print(render(blocks))


if __name__ == "__main__":
    main()
