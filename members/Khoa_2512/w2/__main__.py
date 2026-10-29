"""Run the task loader and print the loaded tasks."""

from .io_utils import load_tasks


def main() -> None:
    """Load tasks from the test CSV file and print their details."""
    try:
        tasks = load_tasks("members/Khoa_2512/w2/test.csv")
    except OSError as exc:
        raise ValueError("Failed to load file") from exc

    for task in tasks:
        print(
            task.title,
            task.importance,
            task.effort_h,
            task.deadline.year,
            "-",
            task.deadline.month,
            "-",
            task.deadline.day,
        )


if __name__ == "__main__":
    main()
