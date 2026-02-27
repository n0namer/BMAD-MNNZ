# Task Filtering Rules

## Project Filter

**Include only:**
- Status = `IN_PROGRESS`

**Exclude:**
- Status = `PLANNED`, `ARCHIVED`, `KILLED`, `COMPLETED`

## Task Date Filter

**Include tasks where:**
- `due_date == today` (tasks due today)
- `in_progress_today == true` (tasks actively being worked on)
- `due_date < today AND status != COMPLETED` (overdue tasks)

**Exclude:**
- `due_date > today` (future tasks)
- `status == COMPLETED` (already done)
- Tasks in archived/killed projects

## Subprocess Calculations

### Task Counts
- **total_tasks**: All tasks matching filters above
- **completed**: status == COMPLETED AND completion_date == today
- **in_progress**: status == IN_PROGRESS
- **not_started**: status == NOT_STARTED
- **overdue**: due_date < today AND status != COMPLETED

### Progress Metrics
- **completion_rate**: (completed / total_tasks) * 100
- **estimated_time_remaining**: SUM(task.estimated_hours WHERE status != COMPLETED)
- **time_spent_today**: SUM(task.time_spent_hours WHERE updated_today == true)

### Priority Distribution
- **high_priority_count**: COUNT WHERE priority == HIGH
- **medium_priority_count**: COUNT WHERE priority == MEDIUM
- **low_priority_count**: COUNT WHERE priority == LOW

### Blocker Detection
- **has_blocker**: task.blockers.length > 0
- **severity**: HIGH if overdue OR high_priority, MEDIUM if blocking other tasks, LOW otherwise
- **recommendation**: Auto-generated based on blocker type

## Sort Order

1. **Overdue tasks** (ascending by due_date, oldest first)
2. **High priority** (by dependencies - unblocked first)
3. **Medium priority** (by estimated_hours - shortest first)
4. **Low priority** (by due_date)

## Graceful Fallback

If subprocess unavailable:
1. Load portfolio file → extract active project IDs
2. Load execution tracker for each active project
3. Filter tasks manually using rules above
4. Calculate metrics in-line
5. Return same JSON schema as subprocess
