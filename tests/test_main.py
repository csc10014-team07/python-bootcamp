from datetime import date

from shared.study_planner.__main__ import main


def test_main_end_to_end(tmp_path, monkeypatch, capsys):
    # Arrange: create a sample tasks CSV.
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "Maths revision,5,3,2026-10-28\n"
        "Essay writing,4,2,2026-11-02\n"
        "Read history,2,1,2026-11-10\n",
        encoding="utf-8",
    )

    # Fix today's date so prioritisation is deterministic.
    class FixedDate(date):
        @classmethod
        def today(cls):
            return cls(2026, 10, 27)

    monkeypatch.setattr(
        "shared.study_planner.__main__.date",
        FixedDate,
    )

    # Act: run the CLI entry point with 4 available hours.
    main([str(csv_file), "--hours", "4"])

    # Assert: verify the complete rendered study plan.
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
