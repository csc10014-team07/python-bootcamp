from .io_utils import load_tasks


def main() -> None:
    sample_csv = "tasks.csv"
    try:
        tasks = load_tasks(sample_csv)
        print("Loaded tasks successfully:")
        for t in tasks:
            print(
                f"- {t.title} (Importance: {t.importance}, Effort:"
                f" {t.effort_h}h, Deadline: {t.deadline})"
            )
    except (OSError, ValueError) as e:
        print(f"Error loading tasks: {e}")


if __name__ == "__main__":
    main()
