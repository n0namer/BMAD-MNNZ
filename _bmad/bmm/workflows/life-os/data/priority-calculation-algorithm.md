# Priority Calculation Algorithm

## Sorting Algorithm

**3-level priority sort:**
1. **Priority:** critical (4) → high (3) → medium (2) → low (1)
2. **Due date:** Overdue first, then earliest due_date, then no due_date last
3. **Energy level:** high → medium → low (within same priority/due_date)

## Pseudo-code

```python
tasks.sort(key=lambda t: (
    -priority_score(t.priority),  # Descending (critical first)
    due_date_score(t.due_date),    # Ascending (earliest first)
    -energy_score(t.energy_level)  # Descending (high first)
))
```

## Scoring Functions

**Priority Score:**
```
critical = 4
high = 3
medium = 2
low = 1
```

**Due Date Score:**
```
overdue = 0 (highest priority)
today = 1
tomorrow = 2
this_week = 3-7
no_due_date = 999 (lowest priority)
```

**Energy Score:**
```
high = 3
medium = 2
low = 1
```
