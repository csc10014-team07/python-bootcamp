from datetime import date

import pytest

from shared.contract import Task
from shared.study_planner.parse import parse_csv


def test_parse_csv_valid(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6.0,2026-10-30\n"
        "Assignment,3,4.0,2026-10-28\n",
        encoding="utf-8",
    )

    tasks = parse_csv(path)

    assert len(tasks) == 2
    assert isinstance(tasks[0], Task)
    assert tasks[0].title == "DS exam"
    assert tasks[0].importance == 5
    assert tasks[0].effort_h == 6.0
    assert tasks[0].deadline == date(2026, 10, 30)


def test_parse_csv_invalid_header(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "name,importance,effort_h,deadline\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="header"):
        parse_csv(path)


def test_parse_csv_invalid_importance(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        "title,importance,effort_h,deadline\nDS exam,high,6.0,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="line 2"):
        parse_csv(path)
