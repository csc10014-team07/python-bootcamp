import csv
import math
from datetime import date

from shared.contract import Task


def parse_csv(path) -> list[Task]:
    tasks = []

    expected_header = ["title", "importance", "effort_h", "deadline"]

    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        header = next(reader, None)

        if header != expected_header:
            raise ValueError("Line 1: invalid CSV header")

        for line_number, row in enumerate(reader, start=2):
            if not row or all(value.strip() == "" for value in row):
                continue

            try:
                if len(row) != 4:
                    raise ValueError("expected 4 columns")

                title = row[0].strip()
                if not title:
                    raise ValueError("title cannot be empty")

                importance = int(row[1].strip())
                if not 1 <= importance <= 5:
                    raise ValueError("importance must be between 1 and 5")

                effort_h = float(row[2].strip())
                if not math.isfinite(effort_h) or effort_h < 0:
                    raise ValueError("effort_h must be finite and non-negative")

                deadline = date.fromisoformat(row[3].strip())

                tasks.append(
                    Task(
                        title=title,
                        importance=importance,
                        effort_h=effort_h,
                        deadline=deadline,
                    )
                )

            except (ValueError, TypeError) as error:
                raise ValueError(f"line {line_number}: {error}") from error

    return tasks
