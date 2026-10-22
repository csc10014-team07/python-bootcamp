"""CLI entrypoint for running `python -m members.vquang2508_cpu.w2`."""

import sys
from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    local_csv = Path(__file__).resolve().parent / "tasks.csv"
    repo_sample_csv = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"

    if local_csv.exists():
        csv_path = local_csv
    elif repo_sample_csv.exists():
        csv_path = repo_sample_csv
    else:
        print("Error: sample tasks.csv not found.", file=sys.stderr)
        sys.exit(1)

    print(f"Loading tasks from: {csv_path.name}")
    print("-" * 50)
    tasks = load_tasks(csv_path)

    if not tasks:
        print("No tasks found.")
        return

    for idx, task in enumerate(tasks, start=1):
        print(
            f"{idx}. {task.title:<15} | Importance: {task.importance}/5 | "
            f"Effort: {task.effort_h}h | Deadline: {task.deadline}"
        )


if __name__ == "__main__":
    main()
