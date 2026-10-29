from datetime import date

from shared.contract import Block, Task
from shared.study_planner.allocate import allocate


def make_tasks():
    a = Task("A", 5, 6.0, date(2026, 10, 25))
    b = Task("B", 4, 10.0, date(2026, 10, 30))
    return a, b


def test_allocate_greedy_partial_for_last_task():
    a, b = make_tasks()

    assert allocate([a, b], 8.0) == [Block(a, 6.0), Block(b, 2.0)]


def test_allocate_enough_hours_for_everything():
    a, b = make_tasks()

    assert allocate([a, b], 20.0) == [Block(a, 6.0), Block(b, 10.0)]


def test_allocate_exact_fit_stops_without_empty_block():
    a, b = make_tasks()

    assert allocate([a, b], 6.0) == [Block(a, 6.0)]


def test_allocate_keeps_input_order():
    a, b = make_tasks()

    blocks = allocate([b, a], 12.0)

    assert [blk.task.title for blk in blocks] == ["B", "A"]
    assert blocks == [Block(b, 10.0), Block(a, 2.0)]


def test_allocate_no_hours():
    a, b = make_tasks()

    assert allocate([a, b], 0) == []


def test_allocate_no_tasks():
    assert allocate([], 8.0) == []
