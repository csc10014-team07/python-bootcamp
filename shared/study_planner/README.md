# Study Planner

## Overview

The Study Planner helps students create a study schedule based on task priorities, estimated effort, deadlines, and available study time.

## Components

- `prioritise.py`: orders tasks according to their priority and deadlines.
- `allocate.py`: allocates available study hours to tasks.
- `render.py`: formats the resulting study plan for display.

## Workflow

The planner follows this general workflow:

1. Load tasks from a CSV file.
2. Prioritise tasks based on their importance and deadlines.
3. Allocate available study time to the prioritised tasks.
4. Render the resulting plan.

## Running the Demo

From the repository root, run the following command:

```bash
python -m members.hoangnhatthi1303.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
```

The command uses a sample task CSV and allocates up to two hours of study time.

## Error Handling

The application should report invalid input, missing files, and infeasible study plans clearly.

## Development

Run the project tests from the repository root:

```bash
python -m pytest -v tests/test_w3.py --member hoangnhatthi1303
```