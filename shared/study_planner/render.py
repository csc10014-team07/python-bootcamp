from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Convert study blocks into a readable study plan."""

    if not blocks:
        return "No study blocks planned."

    lines = ["Study Plan", "=========="]
    total_hours = 0.0

    for index, block in enumerate(blocks, start=1):
        task = block.task

        line = (
            f"{index}. {task.title} — {block.hours:.1f} hours "
            f"(Importance: {task.importance}/5, "
            f"Deadline: {task.deadline.isoformat()})"
        )

        lines.append(line)
        total_hours += block.hours

    lines.append("")
    lines.append(f"Total study time: {total_hours:.1f} hours")

    return "\n".join(lines)
