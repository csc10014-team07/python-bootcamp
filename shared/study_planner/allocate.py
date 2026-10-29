from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    if hours < 0:
        raise ValueError("Available hours cannot be negative")

    blocks = []
    remaining = hours
    for task in tasks:
        if task.effort_h < 0:
            raise ValueError(f"Task effort cannot be negative: {task.title}")
        if remaining <= 0:
            break
        given = min(task.effort_h, remaining)
        blocks.append(Block(task, given))
        remaining -= given
    return blocks
