import argparse
import sys
from datetime import date

from members.Quying2522.w2.io_utils import load_tasks
from members.Quying2522.w2.models import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    return sorted(
        tasks,
        key=lambda t: t.importance / max(1, t.days_left(today)),
        reverse=True,
    )


def allocate(tasks: list[Task], hours: float) -> list[tuple[Task, float]]:
    plan = []
    remaining = hours
    for task in tasks:
        if remaining <= 0:
            break
        given = min(task.effort_h, remaining)
        if given > 0:
            plan.append((task, given))
            remaining -= given
    return plan


def render(plan: list[tuple[Task, float]], hours: float) -> str:
    lines = [f"Tonight ({hours:.1f} h):"]
    width = max((len(t.title) for t, _ in plan), default=0)
    for i, (task, given) in enumerate(plan, start=1):
        dots = "." * (width - len(task.title) + 6)
        lines.append(f"  {i}. {task.title} {dots} {given:.1f} h")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="cli", description="Tonight's study plan")
    parser.add_argument("csv", help="path to tasks CSV")
    parser.add_argument("--hours", type=float, required=True, help="hours available")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        metavar="YYYY-MM-DD",
        help="override today's date (default: real today)",
    )
    args = parser.parse_args(argv)
    today = args.today or date.today()

    try:
        tasks = load_tasks(args.csv)
    except FileNotFoundError:
        print(f"error: file not found: {args.csv}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"error: invalid CSV: {e}", file=sys.stderr)
        return 1

    plan = allocate(prioritise(tasks, today), args.hours)
    print(render(plan, args.hours))
    return 0


if __name__ == "__main__":
    sys.exit(main())
