from datetime import date, timedelta

from shared.contract import Task
from shared.study_planner.prioritise import prioritise

TODAY = date(2026, 10, 22)


def make_task(title, importance, days_until_deadline):
    return Task(
        title=title,
        importance=importance,
        effort_h=1.0,
        deadline=TODAY + timedelta(days=days_until_deadline),
    )


def test_higher_priority_score_comes_first():
    tasks = [
        make_task("Low", 1, 10),
        make_task("High", 5, 1),
    ]

    result = prioritise(tasks, TODAY)

    assert [task.title for task in result] == ["High", "Low"]


def test_higher_importance_gets_higher_priority():
    tasks = [
        make_task("Low importance", 1, 5),
        make_task("High importance", 5, 5),
    ]

    result = prioritise(tasks, TODAY)

    assert [task.title for task in result] == [
        "High importance",
        "Low importance",
    ]


def test_nearer_deadline_gets_higher_priority():
    tasks = [
        make_task("Later", 3, 10),
        make_task("Sooner", 3, 2),
    ]

    result = prioritise(tasks, TODAY)

    assert [task.title for task in result] == ["Sooner", "Later"]


def test_overdue_task_uses_one_day_denominator():
    tasks = [
        make_task("Overdue", 3, -5),
        make_task("Due tomorrow", 2, 1),
    ]

    result = prioritise(tasks, TODAY)

    assert [task.title for task in result] == ["Overdue", "Due tomorrow"]


def test_task_due_today_uses_one_day_denominator():
    tasks = [
        make_task("Due today", 4, 0),
        make_task("Due tomorrow", 3, 1),
    ]

    result = prioritise(tasks, TODAY)

    assert [task.title for task in result] == [
        "Due today",
        "Due tomorrow",
    ]


def test_empty_task_list():
    assert prioritise([], TODAY) == []


def test_single_task():
    task = make_task("Only task", 3, 5)

    result = prioritise([task], TODAY)

    assert result == [task]


def test_equal_scores_preserve_original_order():
    first = make_task("First", 2, 2)
    second = make_task("Second", 4, 4)

    result = prioritise([first, second], TODAY)

    assert [task.title for task in result] == ["First", "Second"]


def test_returns_new_list_without_modifying_original():
    first = make_task("Later", 1, 10)
    second = make_task("Sooner", 5, 1)
    tasks = [first, second]

    result = prioritise(tasks, TODAY)

    assert result is not tasks
    assert tasks == [first, second]
    assert result == [second, first]


def test_mixed_tasks_are_sorted_by_priority_score():
    tasks = [
        make_task("Task A", 2, 4),  # Score: 0.5
        make_task("Task B", 3, 2),  # Score: 1.5
        make_task("Task C", 5, 10),  # Score: 0.5
        make_task("Task D", 4, 1),  # Score: 4.0
    ]

    result = prioritise(tasks, TODAY)

    assert [task.title for task in result] == [
        "Task D",
        "Task B",
        "Task A",
        "Task C",
    ]
