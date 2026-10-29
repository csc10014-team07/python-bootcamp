from pathlib import Path

from io_utils import load_tasks


def main() -> None:
    """Load tasks from ``tasks.csv`` next to this file and print them."""
    csv_path = Path(__file__).with_name("tasks.csv")

    tasks = load_tasks(csv_path)

    if not tasks:
        print("No tasks found.")
        return

    print("Study Planner - Tasks")
    print("=====================")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.title}")
        print(f"   Importance: {task.importance}/5")
        print(f"   Effort: {task.effort_h} hours")
        print(f"   Deadline: {task.deadline.isoformat()}")


if __name__ == "__main__":
    main()
