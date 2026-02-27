# Capacity Calculation Guide

## Capacity Logic

```python
total_allocated_hours = 0
daily_tasks = []

for task in sorted_tasks:
    if total_allocated_hours + task.estimate_hours <= daily_capacity_hours:
        daily_tasks.append(task)
        total_allocated_hours += task.estimate_hours
    else:
        # Skip task (over capacity)
        pass

# If capacity not filled and more tasks available, add more
while total_allocated_hours < daily_capacity_hours and remaining_tasks:
    task = next_task_from_remaining()
    if total_allocated_hours + task.estimate_hours <= daily_capacity_hours:
        daily_tasks.append(task)
        total_allocated_hours += task.estimate_hours
```

## Capacity Validation

- **MIN:** 3 hours (at least some meaningful work)
- **MAX:** 6 hours (realistic daily capacity)
- **IDEAL:** 4-5 hours (balanced workload)

## Resource Assessment Integration

**Read:** {resourceAssessmentFile} → extract `daily_capacity_hours`

**Fallback:** If file not found, default to 5 hours/day
