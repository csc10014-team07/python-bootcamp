import pytest
from datetime import date

from shared.contract import Block, Task
from shared.study_planner.allocate import allocate



@pytest.fixture
def tasks():
    return [
        Task("Task A", 5, 2.0, date(2026, 10, 25)),
        Task("Task B", 4, 3.0, date(2026, 10, 26)),
        Task("Task C", 3, 1.0, date(2026, 10, 27)),
    ]


def test_allocate_all_tasks_when_hours_are_sufficient(tasks):
    blocks = allocate(tasks, 10)

    assert len(blocks) == 3
    assert [b.hours for b in blocks] == [2.0, 3.0, 1.0]
    assert [b.task for b in blocks] == tasks
    assert all(isinstance(b, Block) for b in blocks)


def test_allocate_exact_available_hours(tasks):
    blocks = allocate(tasks, 5)

    assert [b.hours for b in blocks] == [2.0, 3.0]
    assert sum(b.hours for b in blocks) == 5.0


def test_partially_allocate_last_task(tasks):
    blocks = allocate(tasks, 3.5)

    assert [b.hours for b in blocks] == [2.0, 1.5]
    assert blocks[-1].task == tasks[1]
    assert sum(b.hours for b in blocks) == pytest.approx(3.5)


def test_zero_hours_returns_empty_list(tasks):
    assert allocate(tasks, 0) == []


@pytest.mark.parametrize("hours", [-1, -10, -0.5])
def test_negative_hours_returns_empty_list(tasks, hours):
    assert allocate(tasks, hours) == []


def test_empty_tasks_returns_empty_list():
    assert allocate([], 5) == []


def test_zero_effort_tasks_are_skipped():
    tasks = [
        Task("Zero effort", 5, 0.0, date(2026, 10, 25)),
        Task("Negative effort", 4, -2.0, date(2026, 10, 26)),
        Task("Valid task", 3, 2.0, date(2026, 10, 27)),
    ]

    blocks = allocate(tasks, 5)

    assert len(blocks) == 1
    assert blocks[0].task == tasks[2]
    assert blocks[0].hours == 2.0


def test_does_not_mutate_tasks(tasks):
    original_tasks = tasks.copy()

    allocate(tasks, 3)

    assert tasks == original_tasks


def test_allocation_preserves_task_order(tasks):
    blocks = allocate(tasks, 4)

    assert [b.task.title for b in blocks] == ["Task A", "Task B"]


def test_tiny_remaining_hours_are_not_allocated():
    tasks = [
        Task("Task A", 5, 1.0, date(2026, 10, 25)),
        Task("Task B", 4, 1.0, date(2026, 10, 26)),
    ]

    blocks = allocate(tasks, 1.0 + 5e-10)

    assert len(blocks) == 1
    assert blocks[0].hours == 1.0