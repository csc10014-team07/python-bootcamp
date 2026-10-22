"""Study planner module for greedy hours allocation."""

try:
    from shared.contract import Block, Task
except ImportError:
    from ..contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Greedily allocate available study hours across tasks.

    Iterates through tasks in the given order and allocates up to each task's
    effort_h until the available study hours are exhausted.

    Args:
        tasks: A prioritized list of tasks to allocate study time for.
        hours: Total available study hours.

    Returns:
        A list of Block instances containing the task and allocated hours.
    """
    if hours <= 0:
        return []

    remaining_hours = float(hours)
    blocks: list[Block] = []

    for task in tasks:
        if remaining_hours <= 1e-9:
            break
        if task.effort_h <= 0:
            continue

        allocated_h = min(task.effort_h, remaining_hours)
        blocks.append(Block(task=task, hours=allocated_h))
        remaining_hours -= allocated_h

    return blocks
