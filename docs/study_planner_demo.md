# Study Planner Demo

## 1. Goal

Demonstrate how the Study Planner creates an optimized schedule from a task list CSV file based on deadlines, task importance, estimated effort, and available hours.

---

## 2. Pipeline Overview

The study planning workflow consists of 4 main steps:

1. **`parse_csv`**: Reads and parses tasks from a CSV file into structured task objects.
2. **`prioritise`**: Computes priority scores (`importance / days_left`) and orders tasks so that urgent and important tasks are scheduled first.
3. **`allocate`**: Greedily allocates available study hours to tasks in order of priority until the available time is exhausted.
4. **`render`**: Formats the scheduled task blocks into a clean, human-readable study schedule.

---

## 3. Sample Input Data

The demonstration uses the sample file at `samples/tasks.csv`:

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

- **`DS exam`**: Importance 5/5, estimated effort 6.0 hours, deadline `2026-10-30`.
- **`Assignment`**: Importance 4/5, estimated effort 1.5 hours, deadline `2026-10-27`.

---

## 4. Command-Line Execution

Run the command from the repository root:

```bash
python -m members.hoangnhatthi1303.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
```

### Example Output

```text
Tonight (2.0 h):
  1. Assignment ...... 1.5 h
  2. DS exam ...... 0.5 h
```

### Explanation

With `--today 2026-10-26` and `--hours 2`:
- **`Assignment`** has only 1 day left before its deadline (`2026-10-27`), giving it a higher urgency priority score ($4 / 1 = 4.0$). It receives its full requested time of **1.5 hours**.
- Remaining available study time is $2.0 - 1.5 = 0.5$ hours.
- **`DS exam`** receives the remaining **0.5 hours** of study time.

---

## 5. Python API Walkthrough

You can also run the core pipeline directly in Python:

```python
from datetime import date
from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render

# 1. Parse CSV file
tasks = parse_csv("samples/tasks.csv")

# 2. Prioritise tasks for reference date
today = date(2026, 10, 26)
ordered_tasks = prioritise(tasks, today)

# 3. Allocate available study hours
blocks = allocate(ordered_tasks, hours=2.0)

# 4. Render the resulting study schedule
print(render(blocks))
```

### Output from `render()`

```text
Study Plan
==========
1. Assignment — 1.5 hours (Importance: 4/5, Deadline: 2026-10-27)
2. DS exam — 0.5 hours (Importance: 5/5, Deadline: 2026-10-30)

Total study time: 2.0 hours
```

---

## 6. Try It Yourself

- **More hours**: Change `--hours 8` to allocate full time to both `Assignment` (1.5 h) and `DS exam` (6.0 h).
- **Different date**: Change `--today 2026-10-29` to observe how task priority shifts as deadlines approach.
- **Zero hours**: Test edge cases with `--hours 0` to verify how the planner handles zero available time.