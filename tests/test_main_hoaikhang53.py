import csv
from datetime import date

import pytest

from shared.study_planner.__main__ import main


@pytest.fixture
def fixed_today(monkeypatch):
    """Make the CLI use a predictable date during tests."""
    class FixedDate(date):
        @classmethod
        def today(cls):
            return cls(2026, 10, 27)

    monkeypatch.setattr("shared.study_planner.__main__.date", FixedDate)


def write_tasks_csv(path, rows):
    """Write task rows to a temporary CSV file."""
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "importance", "effort_h", "deadline"])
        writer.writerows(rows)
    return path


def test_main_end_to_end_prioritises_tasks_and_respects_hours(
    tmp_path, fixed_today, capsys
):
    """A sample CSV produces the expected plan within the available time."""
    csv_file = write_tasks_csv(
        tmp_path / "tasks.csv",
        [
            ["Maths revision", 5, 3, "2026-10-28"],
            ["Essay writing", 4, 2, "2026-11-02"],
            ["Read history", 2, 1, "2026-11-10"],
        ],
    )

    main([str(csv_file), "--hours", "4"])

    captured = capsys.readouterr()
    assert captured.out == (
        "Study Plan\n"
        "==========\n"
        "1. Maths revision — 3.0 hours "
        "(Importance: 5/5, Deadline: 2026-10-28)\n"
        "2. Essay writing — 1.0 hours "
        "(Importance: 4/5, Deadline: 2026-11-02)\n"
        "\n"
        "Total study time: 4.0 hours\n"
    )
    assert captured.err == ""


def test_main_with_no_tasks_in_csv(tmp_path, fixed_today, capsys):
    """A CSV containing only its header should produce an empty plan."""
    csv_file = write_tasks_csv(tmp_path / "empty.csv", [])

    main([str(csv_file), "--hours", "4"])

    captured = capsys.readouterr()
    assert "Study Plan" in captured.out
    assert "Total study time: 0.0 hours" in captured.out
    assert captured.err == ""


def test_main_with_zero_available_hours(tmp_path, fixed_today, capsys):
    """Zero available hours should not schedule any study time."""
    csv_file = write_tasks_csv(
        tmp_path / "tasks.csv",
        [["Maths revision", 5, 3, "2026-10-28"]],
    )

    main([str(csv_file), "--hours", "0"])

    captured = capsys.readouterr()
    assert "Maths revision" not in captured.out
    assert "Total study time: 0.0 hours" in captured.out
    assert captured.err == ""


def test_main_missing_csv_reports_error(tmp_path, capsys):
    """A missing CSV should be reported rather than crashing with a traceback."""
    missing_file = tmp_path / "does_not_exist.csv"

    result = main([str(missing_file), "--hours", "4"])

    captured = capsys.readouterr()
    assert captured.err
    assert "does_not_exist.csv" in captured.err
    assert result == 1


def test_main_invalid_csv_value_reports_error(tmp_path, capsys):
    """Invalid numeric data in the CSV should produce a readable error."""
    csv_file = tmp_path / "invalid.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "Maths revision,high,3,2026-10-28\n",
        encoding="utf-8",
    )

    result = main([str(csv_file), "--hours", "4"])

    captured = capsys.readouterr()
    assert captured.err
    assert result == 1
