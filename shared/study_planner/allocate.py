from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    blocks = []
    remaining = hours
    for task in tasks:
        if remaining <= 0:
            break
        given = min(task.effort_h, remaining)
        blocks.append(Block(task, given))
        remaining -= given
    return blocks