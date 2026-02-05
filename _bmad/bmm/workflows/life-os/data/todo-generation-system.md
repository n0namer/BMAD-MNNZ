# TODO Generation System (PDCA Integration)

**Version:** 1.0
**Purpose:** Automatically generate actionable TODO items from goals.yaml hierarchical structure
**Integration:** Step-00 (Goals Discovery), Step-07 (Calendar Sync), Review Steps (v-01 to v-04)

---

## Overview

The TODO Generation System transforms high-level goals and key results from `goals.yaml` into concrete, actionable TODO items with deadlines, priorities, and calendar integration.

### Key Features

- ✅ **Automatic TODO creation** from goals → key results → milestones → weekly tasks
- ✅ **Priority inheritance** from goal priority (P0-P3)
- ✅ **Deadline calculation** with buffer days
- ✅ **Calendar sync integration** via Step-07
- ✅ **Progress tracking** linked to PDCA metrics dashboard
- ✅ **Dependency resolution** for sequential task execution

---

## Architecture

```
goals.yaml
  ├── goals[]
  │   ├── key_results[]
  │   │   ├── title
  │   │   ├── deadline
  │   │   └── progress
  │   └── timeline
  │       ├── quarters
  │       └── milestones
  ├── quarters[]
  │   └── milestones[]
  ├── months[]
  │   └── milestones[]
  └── weeks[]
      └── tasks[]

                ↓ [TODO Generator Algorithm]

TODO List
  ├── Goal-level TODOs (strategic)
  ├── Key Result TODOs (measurable outcomes)
  ├── Milestone TODOs (quarterly/monthly checkpoints)
  └── Weekly Task TODOs (tactical execution)

                ↓ [Calendar Sync (Step-07)]

Calendar Events
  ├── Deadline events
  ├── Milestone events
  ├── Review events
  └── Task blocks
```

---

## Algorithm Pseudocode

### Main Algorithm

```python
def generate_todos_from_goals(goals_yaml_path):
    """
    Main entry point for TODO generation.
    Reads goals.yaml and generates comprehensive TODO list.
    """
    # Load goals structure
    goals_data = load_yaml(goals_yaml_path)
    todos = []

    # Generate TODOs from different levels
    todos += generate_goal_level_todos(goals_data.goals)
    todos += generate_key_result_todos(goals_data.goals)
    todos += generate_milestone_todos(goals_data.quarters, goals_data.months)
    todos += generate_weekly_task_todos(goals_data.weeks)

    # Resolve dependencies
    todos = resolve_todo_dependencies(todos)

    # Assign priorities
    todos = calculate_priorities(todos, goals_data)

    # Calculate deadlines with buffers
    todos = calculate_deadlines_with_buffers(todos)

    # Save to TODO file
    save_todos(todos, output_path)

    # Trigger calendar sync
    trigger_calendar_sync(todos)

    return todos
```

### Goal-Level TODO Generation

```python
def generate_goal_level_todos(goals):
    """
    Generate strategic TODOs for each goal.
    These are high-level planning and setup tasks.
    """
    todos = []

    for goal in goals:
        if goal.status == 'active':
            # Strategic planning TODO
            todo = {
                'id': f"todo-goal-{goal.id}-plan",
                'title': f"Plan execution strategy for '{goal.title}'",
                'description': f"""
                    Review goal: {goal.description}
                    Define action plan for key results
                    Identify resources and dependencies
                """,
                'type': 'goal_planning',
                'goal_id': goal.id,
                'priority': goal.priority,
                'deadline': calculate_deadline(goal.created_at, buffer_days=7),
                'estimated_time': '2 hours',
                'status': 'pending',
                'created_at': now(),
                'calendar_sync': True
            }
            todos.append(todo)

            # Kickoff TODO
            todo_kickoff = {
                'id': f"todo-goal-{goal.id}-kickoff",
                'title': f"Kickoff: {goal.title}",
                'description': "Start working on first key result",
                'type': 'goal_kickoff',
                'goal_id': goal.id,
                'priority': goal.priority,
                'deadline': calculate_deadline(goal.created_at, buffer_days=14),
                'depends_on': [f"todo-goal-{goal.id}-plan"],
                'estimated_time': '30 minutes',
                'status': 'pending',
                'created_at': now(),
                'calendar_sync': True
            }
            todos.append(todo_kickoff)

    return todos
```

### Key Result TODO Generation

```python
def generate_key_result_todos(goals):
    """
    Generate TODOs for each key result.
    These are outcome-focused tasks with measurable targets.
    """
    todos = []

    for goal in goals:
        for kr in goal.key_results:
            if kr.status in ['not_started', 'in_progress']:
                # Break down KR into actionable steps
                kr_todos = break_down_key_result(kr, goal)

                # Create checkpoint TODOs for progress tracking
                checkpoint_todos = create_progress_checkpoints(kr, goal)

                todos.extend(kr_todos)
                todos.extend(checkpoint_todos)

    return todos

def break_down_key_result(kr, goal):
    """
    Break key result into 3-5 actionable tasks.
    """
    # Example: KR = "Achieve 100 beta users"
    # Tasks: Setup signup, Create onboarding, Launch campaign, Track metrics, Optimize conversion

    tasks = []
    progress_steps = calculate_progress_steps(kr.baseline, kr.target, steps=5)

    for i, step in enumerate(progress_steps):
        task = {
            'id': f"todo-kr-{kr.id}-step-{i+1}",
            'title': f"{kr.title}: Step {i+1}/{len(progress_steps)}",
            'description': f"Reach {step} {kr.unit} (from {kr.baseline} to {kr.target})",
            'type': 'key_result_step',
            'key_result_id': kr.id,
            'goal_id': goal.id,
            'priority': goal.priority,
            'deadline': distribute_deadline(kr.deadline, len(progress_steps), i),
            'target_value': step,
            'estimated_time': '4-8 hours',
            'status': 'pending',
            'created_at': now(),
            'calendar_sync': True
        }
        tasks.append(task)

    return tasks

def create_progress_checkpoints(kr, goal):
    """
    Create review checkpoints to track KR progress.
    """
    checkpoints = []
    review_dates = calculate_review_dates(kr.deadline, frequency='weekly')

    for i, date in enumerate(review_dates):
        checkpoint = {
            'id': f"todo-kr-{kr.id}-checkpoint-{i+1}",
            'title': f"Review progress: {kr.title}",
            'description': f"Check KR progress, update status, adjust tactics if needed",
            'type': 'checkpoint',
            'key_result_id': kr.id,
            'goal_id': goal.id,
            'priority': increment_priority(goal.priority),  # Higher priority for reviews
            'deadline': date,
            'estimated_time': '30 minutes',
            'status': 'pending',
            'created_at': now(),
            'calendar_sync': True,
            'review_type': 'kr_progress'
        }
        checkpoints.append(checkpoint)

    return checkpoints
```

### Milestone TODO Generation

```python
def generate_milestone_todos(quarters, months):
    """
    Generate TODOs for quarterly and monthly milestones.
    These are checkpoint tasks to ensure on-track progress.
    """
    todos = []

    # Quarterly milestones
    for quarter in quarters.values():
        for milestone in quarter.get('milestones', []):
            todo = {
                'id': f"todo-milestone-{quarter['name']}-{hash(milestone['title'])}",
                'title': f"Milestone: {milestone['title']}",
                'description': f"Quarter: {quarter['name']}, Due: {milestone['date']}",
                'type': 'milestone',
                'quarter': quarter['name'],
                'priority': 'P1',  # Milestones are always high priority
                'deadline': milestone['date'],
                'buffer_days': 3,  # Complete 3 days before deadline
                'estimated_time': 'varies',
                'status': milestone.get('status', 'planned'),
                'created_at': now(),
                'calendar_sync': True
            }
            todos.append(todo)

    # Monthly milestones
    for month_key, month in months.items():
        for milestone_text in month.get('milestones', []):
            # Parse milestone text (format: "Task description (Week N)")
            title, week = parse_milestone(milestone_text)

            todo = {
                'id': f"todo-milestone-{month_key}-{hash(title)}",
                'title': f"Monthly Milestone: {title}",
                'description': f"Month: {month['name']}, Target: {week}",
                'type': 'monthly_milestone',
                'month': month_key,
                'priority': 'P2',
                'deadline': calculate_week_deadline(month_key, week),
                'estimated_time': 'varies',
                'status': 'planned',
                'created_at': now(),
                'calendar_sync': True
            }
            todos.append(todo)

    return todos
```

### Weekly Task TODO Generation

```python
def generate_weekly_task_todos(weeks):
    """
    Generate TODOs for weekly tasks.
    These are tactical, immediate-action items.
    """
    todos = []

    for week_key, week in weeks.items():
        for task_text in week.get('tasks', []):
            todo = {
                'id': f"todo-week-{week_key}-{hash(task_text)}",
                'title': task_text,
                'description': f"Week {week['week_number']}: {week['theme']}",
                'type': 'weekly_task',
                'week': week_key,
                'quarter': week['quarter'],
                'priority': 'P2',  # Tactical tasks, medium priority
                'deadline': week['end_date'],
                'estimated_time': '2-4 hours',
                'status': week['status'],
                'created_at': now(),
                'calendar_sync': True,
                'auto_schedule': True  # Let calendar sync auto-schedule these
            }
            todos.append(todo)

    return todos
```

---

## Priority Calculation

### Priority Inheritance Rules

```python
def calculate_priorities(todos, goals_data):
    """
    Calculate TODO priority based on:
    1. Parent goal priority (P0-P3)
    2. TODO type (strategic > milestone > tactical)
    3. Deadline proximity
    4. Dependency chain (blocking tasks = higher priority)
    """
    for todo in todos:
        base_priority = get_goal_priority(todo.goal_id, goals_data)
        type_modifier = get_type_priority_modifier(todo.type)
        deadline_modifier = get_deadline_priority_modifier(todo.deadline)
        dependency_modifier = get_dependency_priority_modifier(todo, todos)

        # Calculate final priority
        priority_score = (
            priority_to_score(base_priority) +
            type_modifier +
            deadline_modifier +
            dependency_modifier
        )

        todo.priority = score_to_priority(priority_score)
        todo.priority_score = priority_score  # For sorting

    return sorted(todos, key=lambda t: t.priority_score, reverse=True)

def get_type_priority_modifier(todo_type):
    """
    Strategic > Milestone > Checkpoint > Tactical
    """
    modifiers = {
        'goal_planning': +20,
        'goal_kickoff': +15,
        'milestone': +10,
        'checkpoint': +5,
        'key_result_step': 0,
        'weekly_task': -5
    }
    return modifiers.get(todo_type, 0)

def get_deadline_priority_modifier(deadline):
    """
    Closer deadlines = higher priority.
    """
    days_until = (deadline - today()).days

    if days_until <= 3:
        return +30  # Urgent
    elif days_until <= 7:
        return +20  # Important
    elif days_until <= 14:
        return +10  # Soon
    else:
        return 0  # Normal
```

---

## Deadline Calculation with Buffers

```python
def calculate_deadlines_with_buffers(todos):
    """
    Add buffer days to deadlines to avoid last-minute rushes.
    """
    for todo in todos:
        if todo.get('buffer_days'):
            # Subtract buffer days from deadline
            todo.effective_deadline = todo.deadline - timedelta(days=todo.buffer_days)
        else:
            # Default buffer based on TODO type
            default_buffer = get_default_buffer(todo.type)
            todo.effective_deadline = todo.deadline - timedelta(days=default_buffer)

        # For calendar sync, use effective deadline
        todo.calendar_event_date = todo.effective_deadline

    return todos

def get_default_buffer(todo_type):
    """
    Default buffer days by TODO type.
    """
    buffers = {
        'goal_planning': 7,      # Plan 1 week before goal start
        'milestone': 3,          # Complete 3 days before milestone
        'checkpoint': 0,         # No buffer for reviews (fixed dates)
        'key_result_step': 2,    # 2-day buffer for KR steps
        'weekly_task': 1         # 1-day buffer for weekly tasks
    }
    return buffers.get(todo_type, 1)  # Default 1 day
```

---

## Dependency Resolution

```python
def resolve_todo_dependencies(todos):
    """
    Build dependency graph and order TODOs accordingly.
    """
    # Build dependency graph
    graph = build_dependency_graph(todos)

    # Topological sort to get execution order
    ordered_todos = topological_sort(graph)

    # Mark dependencies in TODO metadata
    for todo in ordered_todos:
        deps = graph.get_dependencies(todo.id)
        todo.depends_on = [d.id for d in deps]
        todo.blocks = [b.id for b in graph.get_blocked_by(todo.id)]

    return ordered_todos

def build_dependency_graph(todos):
    """
    Dependencies:
    1. Explicit: specified in 'depends_on' field
    2. Implicit: goal_planning → goal_kickoff → key_result_steps
    3. Sequential: step 1 → step 2 → step 3 (for KR steps)
    """
    graph = DependencyGraph()

    for todo in todos:
        graph.add_node(todo)

        # Explicit dependencies
        if 'depends_on' in todo:
            for dep_id in todo.depends_on:
                graph.add_edge(dep_id, todo.id)

        # Implicit dependencies
        if todo.type == 'goal_kickoff':
            plan_todo_id = f"todo-goal-{todo.goal_id}-plan"
            graph.add_edge(plan_todo_id, todo.id)

        if todo.type == 'key_result_step':
            # Sequential: step N depends on step N-1
            step_num = extract_step_number(todo.id)
            if step_num > 1:
                prev_step_id = f"todo-kr-{todo.key_result_id}-step-{step_num-1}"
                graph.add_edge(prev_step_id, todo.id)

    return graph
```

---

## Calendar Sync Integration

### Trigger Calendar Sync (Step-07)

```python
def trigger_calendar_sync(todos):
    """
    Send TODOs to Step-07 (Calendar Sync) for scheduling.
    """
    calendar_events = []

    for todo in todos:
        if todo.get('calendar_sync', False):
            event = {
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'type': map_todo_type_to_event_type(todo.type),
                'date': todo.effective_deadline,
                'duration': estimate_duration(todo.estimated_time),
                'reminder': calculate_reminder(todo.deadline, todo.priority),
                'auto_schedule': todo.get('auto_schedule', False),
                'metadata': {
                    'goal_id': todo.goal_id,
                    'key_result_id': todo.get('key_result_id'),
                    'priority': todo.priority,
                    'status': todo.status
                }
            }
            calendar_events.append(event)

    # Call Step-07 calendar sync API
    sync_to_calendar(calendar_events)

    return calendar_events

def calculate_reminder(deadline, priority):
    """
    Set reminder times based on priority.
    """
    if priority == 'P0':
        return ['-3 days', '-1 day', '-2 hours']
    elif priority == 'P1':
        return ['-1 week', '-1 day']
    elif priority == 'P2':
        return ['-3 days']
    else:
        return ['-1 day']
```

---

## Output Format

### TODO List JSON Schema

```json
{
  "generated_at": "2026-02-05T12:00:00Z",
  "source": "goals.yaml",
  "total_todos": 47,
  "by_priority": {
    "P0": 5,
    "P1": 12,
    "P2": 20,
    "P3": 10
  },
  "by_type": {
    "goal_planning": 2,
    "goal_kickoff": 2,
    "key_result_step": 15,
    "checkpoint": 8,
    "milestone": 10,
    "weekly_task": 10
  },
  "todos": [
    {
      "id": "todo-goal-001-plan",
      "title": "Plan execution strategy for 'Launch SaaS Product MVP'",
      "description": "Review goal, define action plan, identify resources",
      "type": "goal_planning",
      "goal_id": "goal-001",
      "key_result_id": null,
      "priority": "P0",
      "priority_score": 95,
      "deadline": "2026-01-15",
      "effective_deadline": "2026-01-08",
      "buffer_days": 7,
      "estimated_time": "2 hours",
      "status": "pending",
      "depends_on": [],
      "blocks": ["todo-goal-001-kickoff"],
      "calendar_sync": true,
      "calendar_event_date": "2026-01-08",
      "created_at": "2026-01-01T00:00:00Z"
    },
    {
      "id": "todo-kr-001-step-1",
      "title": "Achieve 100 beta users: Step 1/5",
      "description": "Reach 20 users (from 0 to 100)",
      "type": "key_result_step",
      "goal_id": "goal-001",
      "key_result_id": "kr-001",
      "priority": "P0",
      "priority_score": 85,
      "deadline": "2026-01-25",
      "effective_deadline": "2026-01-23",
      "buffer_days": 2,
      "estimated_time": "4-8 hours",
      "target_value": 20,
      "status": "pending",
      "depends_on": ["todo-goal-001-kickoff"],
      "blocks": ["todo-kr-001-step-2"],
      "calendar_sync": true,
      "auto_schedule": false,
      "created_at": "2026-01-01T00:00:00Z"
    }
  ]
}
```

---

## Usage Examples

### Example 1: Generate TODOs on Goals Creation

```bash
# After Step-00 (Goals Discovery) completes:
npx claude-flow@v3alpha todo generate \
  --source "./goals.yaml" \
  --output "./todos.json" \
  --calendar-sync true
```

### Example 2: Regenerate TODOs After Goals Update

```bash
# After Monthly Review (Step v-03) updates goals:
npx claude-flow@v3alpha todo regenerate \
  --source "./goals.yaml" \
  --merge-existing true \
  --preserve-completed true
```

### Example 3: Query TODOs by Priority

```bash
# Get high-priority TODOs for this week:
npx claude-flow@v3alpha todo list \
  --priority P0,P1 \
  --deadline-before "2026-02-12" \
  --status pending
```

---

## Integration with PDCA Cycle

### Plan Phase (Step-00: Goals Discovery)
- Initial TODO generation from goals.yaml
- Strategic planning TODOs created

### Do Phase (Steps 1-8: Execution)
- TODOs drive execution via calendar events
- Progress tracked in TODO completion status

### Check Phase (Review Steps v-01 to v-04)
- TODO completion rates analyzed
- Checkpoint TODOs trigger progress reviews

### Act Phase (Adjustment Steps e-01 to e-04)
- TODOs regenerated based on goal adjustments
- Priorities recalculated

---

## Metrics & Monitoring

### TODO Completion Metrics

```yaml
metrics:
  completion_rate:
    formula: "completed_todos / total_todos * 100"
    target: 80%
    current: 0%

  on_time_completion:
    formula: "completed_before_deadline / completed_todos * 100"
    target: 90%
    current: 0%

  average_completion_time:
    formula: "sum(completion_time) / count(completed)"
    target: "< 5 days"
    current: null

  dependency_chain_length:
    formula: "max(chain_length for all todos)"
    target: "< 5"
    current: 0
```

---

## Error Handling

### Missing Goal Data
```python
if not goals_data.goals:
    raise ValueError("No goals found in goals.yaml. Run Step-00 first.")
```

### Circular Dependencies
```python
if graph.has_cycle():
    cycles = graph.find_cycles()
    raise ValueError(f"Circular dependencies detected: {cycles}")
```

### Invalid Deadlines
```python
if todo.deadline < today():
    logger.warning(f"TODO {todo.id} has past deadline. Skipping.")
    continue
```

---

## Best Practices

1. **Keep TODO granularity appropriate**
   - Goal-level: Strategic (weeks)
   - KR-level: Outcome-focused (days)
   - Weekly tasks: Tactical (hours)

2. **Review and regenerate regularly**
   - After each Monthly Review (Step v-03)
   - When goals change significantly
   - When new projects added (Step-01)

3. **Use calendar sync for accountability**
   - Block time for high-priority TODOs
   - Set aggressive reminders for P0 items
   - Auto-schedule weekly tasks in preferred time slots

4. **Track TODO completion in reviews**
   - Daily Review: Check today's TODOs
   - Weekly Review: Analyze completion rate
   - Monthly Review: Adjust TODO generation strategy

---

**End of TODO Generation System Documentation**
