# Energy-Level Balancing Algorithm

## Time Block Allocation Strategy

### Morning Block (8am-12pm)
**Energy Level:** HIGH
**Capacity:** ~4 hours
**Recommended Tasks:**
- Overdue high-priority tasks (clear debt first)
- Complex/deep work tasks (architecture, design, critical decisions)
- Tasks requiring sustained focus
- Tasks with dependencies blocking others

**Algorithm:**
1. If overdue high-priority exists → allocate to morning
2. Else, allocate highest-priority unblocked tasks
3. Fill remaining time with medium-priority tasks
4. Target: 3-4 hours of work (allow buffer for breaks)

### Afternoon Block (12pm-5pm)
**Energy Level:** MEDIUM
**Capacity:** ~5 hours
**Recommended Tasks:**
- Medium-priority tasks
- Collaborative tasks (reviews, meetings)
- Tasks with moderate complexity
- Follow-up tasks from morning blockers

**Algorithm:**
1. Allocate remaining high-priority tasks (if any)
2. Fill with medium-priority tasks
3. Include collaborative/review tasks
4. Target: 4-5 hours of work

### Evening Block (5pm-9pm)
**Energy Level:** LOW-MEDIUM
**Capacity:** ~2-3 hours
**Recommended Tasks:**
- Low-priority tasks
- Administrative work (updates, logging, planning)
- Quick wins (<1 hour tasks)
- Prep for tomorrow

**Algorithm:**
1. Allocate low-priority tasks
2. Include short tasks (<1h from any priority)
3. Leave buffer for reflection/planning
4. Target: 2-3 hours maximum

## Load Balancing Rules

### Rule 1: Don't Overload
- Morning should not exceed 4 hours estimated
- Afternoon should not exceed 5 hours estimated
- Evening should not exceed 3 hours estimated
- Total daily capacity: ~12 hours (overestimate to account for interruptions)

### Rule 2: Dependency Respect
- Tasks with dependencies MUST be scheduled before dependent tasks
- If dependency not completable today, defer dependent task

### Rule 3: Energy Matching
- HIGH energy tasks → Morning only
- MEDIUM energy tasks → Morning or Afternoon
- LOW energy tasks → Any time block

### Rule 4: Priority Override
- Overdue tasks override energy matching (do them first regardless)
- High-priority unblocked tasks take precedence over lower priority

## Focus Recommendation Generation

**Format:** "Complete [task] first, then [task]"

**Logic:**
1. If overdue exists:
   - "Complete overdue task [task-id] first, then [next-highest-priority]"
2. Else if high-priority with blocker exists:
   - "Resolve blocker for [task-id], then [next-task]"
3. Else:
   - "Start with [highest-priority-unblocked], then [next-task]"

**Next task selection:**
- Choose highest-priority unblocked task
- Or shortest estimated_hours task if all same priority
- Or task with most dependencies blocking others

## Example Allocation

**Input:**
- 8 tasks total
- 3 high-priority (2h, 3h, 1h)
- 3 medium-priority (2h, 1.5h, 2.5h)
- 2 low-priority (1h, 0.5h)
- 1 overdue (3h, high-priority)

**Output:**
```json
{
  "morning": ["task-012 (overdue, 3h)", "task-003 (high, 2h)"],
  "afternoon": ["task-007 (high, 1h)", "task-015 (medium, 2h)", "task-020 (medium, 1.5h)"],
  "evening": ["task-025 (low, 1h)", "task-030 (low, 0.5h)"]
}
```

**Total Estimated:** 11.5h (within daily capacity)
