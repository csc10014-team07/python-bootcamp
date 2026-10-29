from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def test_render_empty_blocks():
    assert render([]) == "No study blocks planned."


def test_render_one_block():
    task = Task(
        title="Learn Python",
        importance=5,
        effort_h=3.0,
        deadline=date(2026, 10, 25),
    )
    blocks = [Block(task=task, hours=2.0)]

    result = render(blocks)

    assert "Study Plan" in result
    assert "1. Learn Python" in result
    assert "2.0 hours" in result
    assert "Importance: 5/5" in result
    assert "Deadline: 2026-10-25" in result
    assert "Total study time: 2.0 hours" in result


def test_render_multiple_blocks():
    task1 = Task(
        title="Learn Python",
        importance=5,
        effort_h=3.0,
        deadline=date(2026, 10, 25),
    )
    task2 = Task(
        title="Practice exercises",
        importance=4,
        effort_h=2.0,
        deadline=date(2026, 10, 27),
    )

    blocks = [
        Block(task=task1, hours=2.0),
        Block(task=task2, hours=1.5),
    ]

    result = render(blocks)

    assert "1. Learn Python" in result
    assert "2. Practice exercises" in result
    assert "Total study time: 3.5 hours" in result
