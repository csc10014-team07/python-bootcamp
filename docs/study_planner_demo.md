# Study Planner Demo

## Goal

Demonstrate how the Study Planner creates a schedule from a sample CSV file.

## Command

Run from the repository root:

```bash
python -m members.hoangnhatthi1303.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
```

## Example Output

```text
Tonight (2.0 h):
  1. Assignment ...... 1.5 h
  2. DS exam ...... 0.5 h
```

## Explanation

The planner reads tasks from the CSV file, prioritises them, and allocates the available two hours to the selected tasks.

The output shows each scheduled task and its allocated study time.

## Try It Yourself

Change `--hours` to a different value to explore how the study plan changes. You can also change `--today` to test the planner against a different reference date.