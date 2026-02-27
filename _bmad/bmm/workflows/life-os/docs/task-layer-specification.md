# Task Layer Specification - Life OS Workflow System

**Created:** 2026-02-06
**Purpose:** Complete technical specification for task data model, storage, sync, and linkage
**Source:** IDEAL-BEHAVIOR-REFERENCE.md Section 1.12
**Status:** ✅ IMPLEMENTATION CONTRACT

---

## Overview

The Task Layer is the execution engine of Life OS. It bridges high-level goals and projects into actionable daily work with time-block calendar integration, progress tracking, and external tool synchronization.

**Key Principles:**
- ✅ **Traceability:** Every task links to a project and goal (no orphans)
- ✅ **Realistic Planning:** Energy levels + capacity constraints drive scheduling
- ✅ **Calendar-First:** Tasks are not just lists but time-blocked commitments
- ✅ **Progress Transparency:** Task completion automatically updates project and goal progress

---

## 1. Task Data Model (Source of Truth)

### 1.1 Primary Storage

**Phase 1-2:** Markdown files in project folders
**Phase 3:** Supabase `tasks` table (with optional Markdown mirror for git history)

### 1.2 Task Schema

```yaml
task_id: string          # Unique ID (e.g., "task-001-setup-db")
project_id: string       # Parent project (e.g., "project-002")
goal_id: string          # Linked goal from goals.yaml (e.g., "2026-business-q1-1")
title: string            # Task title (max 100 chars)
description: string      # Detailed description (markdown)
status: enum             # [todo, in_progress, blocked, done, cancelled]
priority: enum           # [critical, high, medium, low]
due_date: date|null      # Optional. ISO 8601 (e.g., "2026-02-15"). If null → scheduled via week plan or calendar
estimate_hours: number   # Effort estimate (0.5 - 40 hours)
actual_hours: number     # Actual time spent (tracked)
energy_level: enum       # [high, medium, low] - required mental energy
dependencies: string[]   # Other task_ids that must complete first
tags: string[]           # Labels (e.g., ["coding", "frontend", "urgent"])
created_at: timestamp
updated_at: timestamp
completed_at: timestamp  # Set when status = done
```

### 1.3 Field Definitions

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `task_id` | string | ✅ Yes | Unique identifier | Format: `task-NNN-short-name` |
| `project_id` | string | ✅ Yes | Parent project reference | Must reference active project |
| `goal_id` | string | ✅ Yes | Goal linkage for traceability | From goals.yaml (e.g., `2026-business-q1-1`) |
| `title` | string | ✅ Yes | Short task name | Max 100 characters |
| `description` | string | ❌ Optional | Full task details | Markdown format |
| `status` | enum | ✅ Yes | Current state | `todo`, `in_progress`, `blocked`, `done`, `cancelled` |
| `priority` | enum | ✅ Yes | Urgency level | `critical`, `high`, `medium`, `low` |
| `due_date` | date | ❌ Optional | Hard deadline | ISO 8601 format. Null = scheduled via week plan |
| `estimate_hours` | number | ✅ Yes | Planned effort | Range: 0.5 - 40 hours |
| `actual_hours` | number | ❌ Optional | Actual time tracked | Defaults to 0, updated on completion |
| `energy_level` | enum | ✅ Yes | Mental effort required | `high`, `medium`, `low` (for time-of-day scheduling) |
| `dependencies` | string[] | ❌ Optional | Blocking tasks | Array of task_ids (empty if none) |
| `tags` | string[] | ❌ Optional | Categorization labels | Free-form tags |
| `created_at` | timestamp | Auto | Creation timestamp | ISO 8601 with timezone |
| `updated_at` | timestamp | Auto | Last modification | ISO 8601 with timezone |
| `completed_at` | timestamp | Auto | Completion timestamp | Set when `status = done` |

### 1.4 Mandatory vs Optional Fields

**Mandatory Fields (Cannot Create Task Without):**
- `task_id`
- `project_id`
- `goal_id`
- `title`
- `status`
- `estimate_hours`
- `energy_level`

**Optional Fields:**
- `due_date` (scheduled via week plan if null)
- `description`
- `actual_hours` (tracked during execution)
- `dependencies`
- `tags`
- `completed_at` (auto-set on completion)

### 1.5 Status Lifecycle

```
todo → in_progress → done
  ↓         ↓          ↑
blocked → cancelled   (recovery)
```

**Status Transitions:**
- `todo` → `in_progress`: User starts working
- `in_progress` → `done`: Work completed
- `todo` → `blocked`: Dependency not met
- `blocked` → `todo`: Dependency resolved
- `any` → `cancelled`: Task no longer needed

---

## 2. Storage Options & Sync Rules

### 2.1 Phase 1: Markdown-First (MVP)

**Primary Storage:** Markdown files with YAML frontmatter

**File Structure:**
```
projects/
  project-002-life-os-v3/
    tasks/
      task-001-setup-db.md
      task-002-build-api.md
      task-003-frontend.md
```

**Example Task File:**
```markdown
---
task_id: task-001-setup-db
project_id: project-002
goal_id: 2026-business-q1-1
title: Setup PostgreSQL database
status: in_progress
priority: high
due_date: 2026-02-10
estimate_hours: 4
actual_hours: 2.5
energy_level: high
dependencies: []
tags: [backend, database, infrastructure]
created_at: 2026-02-01T10:00:00Z
updated_at: 2026-02-06T14:30:00Z
completed_at: null
---

# Setup PostgreSQL database

## Description
Initialize PostgreSQL database with:
- User authentication schema
- Projects and tasks tables
- Goals relationship schema

## Acceptance Criteria
- [ ] Database running locally
- [ ] All migrations applied
- [ ] Test data seeded
```

**Sync:** None (local only, Git for version control)
**Source of Truth:** Markdown files

### 2.2 Phase 2: Hybrid with Todoist

**Primary:** Markdown files (authoritative)
**Mirror:** Todoist (for mobile/calendar integration)

**Sync Direction:** **One-way (Markdown → Todoist)**

**Sync Rules:**
1. **Task Creation:** New Markdown task → Create in Todoist via API
2. **Task Updates:** Markdown changes → Update Todoist (title, due_date, priority)
3. **Task Completion:** Todoist completion webhook → Mark `status = done` in Markdown
4. **Conflict Resolution:** Markdown always wins (if both modified, Markdown overwrites Todoist)
5. **Sync Frequency:** Immediate (on task create/update)

**Todoist Field Mapping:**
| Life OS Field | Todoist Field | Notes |
|---------------|---------------|-------|
| `task_id` | `description` (hidden) | Store as `[task-001]` prefix |
| `title` | `content` | Direct mapping |
| `due_date` | `due.date` | ISO 8601 format |
| `priority` | `priority` | Map: critical=4, high=3, medium=2, low=1 |
| `status` | `is_completed` | `done` = true, others = false |
| `project_id` | `project_id` | Create Todoist project per Life OS project |
| `tags` | `labels` | Direct array mapping |

**What's NOT Synced:**
- `goal_id` (not available in Todoist)
- `estimate_hours` / `actual_hours` (not native in Todoist)
- `energy_level` (not native in Todoist)
- `dependencies` (Todoist has limited dependency support)

**Webhook Setup (Todoist → Life OS):**
```javascript
// Todoist completion webhook handler
POST /webhooks/todoist-completion
{
  "event_name": "item:completed",
  "event_data": {
    "id": "todoist-item-id",
    "content": "[task-001] Setup database"
  }
}

// Life OS handler:
1. Extract task_id from content prefix
2. Load Markdown file
3. Update status = done, completed_at = now()
4. Update actual_hours (if tracked externally)
5. Trigger project progress update
```

### 2.3 Phase 3: Supabase Database

**Primary:** Supabase `tasks` table (authoritative)
**Mirror:** Markdown files (optional, for git history)

**Sync Direction:** **Two-way (Supabase ↔ Todoist)**

**Database Schema (PostgreSQL):**
```sql
CREATE TABLE tasks (
  task_id TEXT PRIMARY KEY,
  project_id TEXT NOT NULL REFERENCES projects(project_id),
  goal_id TEXT NOT NULL,
  title TEXT NOT NULL CHECK (LENGTH(title) <= 100),
  description TEXT,
  status TEXT NOT NULL CHECK (status IN ('todo','in_progress','blocked','done','cancelled')),
  priority TEXT NOT NULL CHECK (priority IN ('critical','high','medium','low')),
  due_date DATE,
  estimate_hours NUMERIC(4,1) CHECK (estimate_hours BETWEEN 0.5 AND 40),
  actual_hours NUMERIC(5,1) DEFAULT 0,
  energy_level TEXT NOT NULL CHECK (energy_level IN ('high','medium','low')),
  dependencies TEXT[] DEFAULT '{}',
  tags TEXT[] DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  completed_at TIMESTAMPTZ
);

-- Indexes for performance
CREATE INDEX idx_tasks_project ON tasks(project_id);
CREATE INDEX idx_tasks_goal ON tasks(goal_id);
CREATE INDEX idx_tasks_status_due ON tasks(status, due_date);
CREATE INDEX idx_tasks_priority ON tasks(priority);

-- Auto-update updated_at
CREATE TRIGGER update_tasks_updated_at
  BEFORE UPDATE ON tasks
  FOR EACH ROW
  EXECUTE FUNCTION update_updated_at_column();
```

**Sync Strategy (Supabase ↔ Todoist):**
1. **Supabase → Todoist:** Database triggers fire on INSERT/UPDATE → API call to Todoist
2. **Todoist → Supabase:** Webhook on completion → Update Supabase row
3. **Conflict Resolution:** Last-write-wins with `updated_at` timestamp check

**Supabase Triggers:**
```sql
-- Trigger on task creation
CREATE FUNCTION sync_task_to_todoist()
RETURNS TRIGGER AS $$
BEGIN
  PERFORM net.http_post(
    url := 'https://api.todoist.com/rest/v2/tasks',
    headers := jsonb_build_object('Authorization', 'Bearer ' || current_setting('app.todoist_token')),
    body := jsonb_build_object(
      'content', NEW.title,
      'due_date', NEW.due_date,
      'priority', CASE NEW.priority
        WHEN 'critical' THEN 4
        WHEN 'high' THEN 3
        WHEN 'medium' THEN 2
        ELSE 1
      END,
      'project_id', (SELECT todoist_project_id FROM projects WHERE project_id = NEW.project_id)
    )
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER task_created_sync
  AFTER INSERT ON tasks
  FOR EACH ROW
  EXECUTE FUNCTION sync_task_to_todoist();
```

---

## 3. Task ↔ Project ↔ Goal Linkage

### 3.1 Hierarchical Structure

```
Year Goal (goals.yaml: 2026-business)
    ↓ decomposed into
Quarterly Goal (2026-business-q1-1: "Ship v3.0 by Q1")
    ↓ implemented as
Project (project-002: "Life OS v3.0 Implementation")
    ↓ broken down into
Tasks (task-001, task-002, ..., task-018)
    ↓ executed as
Daily TODO (generated from week plan)
```

### 3.2 Traceability Rules

**RULE 1: No Orphan Tasks**
- Every task MUST have `project_id` (tasks cannot exist without a parent project)
- Validation at creation: `SELECT 1 FROM projects WHERE project_id = :project_id AND status = 'ACTIVE'`

**RULE 2: Goal Linkage**
- Every project SHOULD link to `goal_id` (one-off projects can skip if not goal-driven)
- Tasks inherit `goal_id` from parent project
- Alternative: Task-level `goal_id` override (for multi-goal projects)

**RULE 3: Progress Tracking**

**Primary Method (Task Count):**
```
Goal Progress = done_tasks / total_tasks × 100%

Where:
- done_tasks = COUNT(*) WHERE goal_id = :goal_id AND status = 'done'
- total_tasks = COUNT(*) WHERE goal_id = :goal_id AND status IN ('todo','in_progress','blocked','done')
```

**Secondary Method (Hours-Based Forecasting):**
```
Goal Progress (Forecast) = actual_hours / estimate_hours × 100%

Where:
- actual_hours = SUM(actual_hours) WHERE goal_id = :goal_id
- estimate_hours = SUM(estimate_hours) WHERE goal_id = :goal_id
```

**Use Case for Secondary Method:**
- Capacity forecasting: "10 hours spent, 30 estimated → 33% complete → 20 hours remaining"
- Velocity tracking: "Spent 10h, completed 3 tasks → 3.3h per task average"

### 3.3 Validation Gates

**At Task Creation:**
- ✅ Project exists: `SELECT 1 FROM projects WHERE project_id = :project_id`
- ✅ Project is ACTIVE: `projects.status = 'ACTIVE'`
- ✅ Goal exists: Check `goal_id` in `goals.yaml` or `goals` table

**At Task Completion:**
- ✅ Set `completed_at = NOW()`
- ✅ Update project progress: `project.progress = (done_tasks / total_tasks) × 100`
- ✅ Update goal progress: Recalculate across all tasks with `goal_id`
- ✅ Check milestone: If project milestone reached → Notify user

**At Project Completion:**
- ✅ All tasks must be `done` or `cancelled` (no open tasks)
- ✅ Validation query: `SELECT COUNT(*) FROM tasks WHERE project_id = :project_id AND status IN ('todo','in_progress','blocked')`
- ✅ If count > 0 → Reject completion, show remaining tasks

### 3.4 Traceability Queries

**Find All Tasks for a Goal:**
```sql
SELECT t.*, p.title as project_title
FROM tasks t
LEFT JOIN projects p ON p.project_id = t.project_id
WHERE t.goal_id = '2026-business-q1-1'
ORDER BY t.priority DESC, t.due_date ASC;
```

**Find Origin Idea for a Task:**
```sql
SELECT i.*
FROM tasks t
LEFT JOIN projects p ON p.project_id = t.project_id
LEFT JOIN ideas i ON i.id = p.origin_idea_id
WHERE t.task_id = 'task-001-setup-db';
```

**Project Progress Dashboard:**
```sql
SELECT
  p.project_id,
  p.title,
  p.goal_id,
  COUNT(t.task_id) as total_tasks,
  SUM(CASE WHEN t.status = 'done' THEN 1 ELSE 0 END) as done_tasks,
  ROUND(SUM(CASE WHEN t.status = 'done' THEN 1 ELSE 0 END)::numeric / COUNT(t.task_id) * 100, 1) as progress_percent,
  SUM(t.estimate_hours) as total_hours,
  SUM(t.actual_hours) as spent_hours
FROM projects p
LEFT JOIN tasks t ON t.project_id = p.project_id
WHERE p.status = 'ACTIVE'
GROUP BY p.project_id, p.title, p.goal_id
ORDER BY progress_percent ASC;
```

---

## 4. Daily TODO Generation Algorithm

### 4.1 Source Data

**Inputs:**
1. **Week Plan:** `projects/project-XXX/week-plan.md` (task_ids scheduled for current week)
2. **Task Due Dates:** From `task.due_date` field
3. **Energy Levels:** From `task.energy_level` (high/medium/low)
4. **User Capacity:** From Step 00.6 resource assessment (default: 4-6 hours/day)
5. **Current Date:** `target_date = TODAY()`

### 4.2 Algorithm Steps

```python
def generate_daily_todo(target_date: date, user_capacity_hours: float = 6.0):
    """
    Generate daily TODO list for target_date.

    Returns: List of tasks scheduled by time-of-day (morning/afternoon/evening)
    """

    # STEP 0: Parse week plan
    week_plan_tasks = parse_week_plan(target_date)  # Returns task_ids scheduled this week

    # STEP 1: Fetch candidate tasks
    candidates = db.query("""
        SELECT t.*
        FROM tasks t
        LEFT JOIN projects p ON p.project_id = t.project_id
        WHERE t.status IN ('todo', 'in_progress')
          AND p.status = 'ACTIVE'
          AND (
            (t.due_date IS NOT NULL AND t.due_date <= :target_date)
            OR t.task_id = ANY(:week_plan_tasks)
          )
          AND NOT EXISTS (
            SELECT 1 FROM tasks dep
            WHERE dep.task_id = ANY(t.dependencies)
              AND dep.status NOT IN ('done', 'cancelled')
          )
    """, target_date=target_date, week_plan_tasks=week_plan_tasks)

    # STEP 2: Sort by priority and due date
    candidates.sort(key=lambda t: (
        priority_weight(t.priority),      # critical=4, high=3, medium=2, low=1
        t.due_date or date.max,           # Earlier due dates first, nulls last
        -energy_match_score(t, target_date)  # Match energy to time-of-day
    ))

    # STEP 3: Filter by capacity
    selected_tasks = []
    total_hours = 0.0

    for task in candidates:
        if total_hours + task.estimate_hours <= user_capacity_hours:
            selected_tasks.append(task)
            total_hours += task.estimate_hours
        else:
            break  # Capacity reached

    # STEP 4: Balance energy levels by time-of-day
    schedule = {
        'morning': [],    # 8am-12pm (high energy)
        'afternoon': [],  # 1pm-5pm (medium energy)
        'evening': []     # 6pm-9pm (low energy)
    }

    for task in selected_tasks:
        if task.energy_level == 'high':
            schedule['morning'].append(task)
        elif task.energy_level == 'medium':
            schedule['afternoon'].append(task)
        else:  # low
            schedule['evening'].append(task)

    # STEP 5: Output formatted TODO
    return format_daily_todo(target_date, schedule, total_hours)


def parse_week_plan(target_date: date) -> List[str]:
    """
    Extract task_ids from week-plan.md for the week containing target_date.
    """
    week_start = target_date - timedelta(days=target_date.weekday())
    week_plan_file = f"projects/project-XXX/week-plan.md"

    # Parse markdown file, extract lines like:
    # - [ ] task-001-setup-db (Mon-Tue, 4h)
    # Return: ['task-001-setup-db', 'task-002-build-api', ...]
    pass


def priority_weight(priority: str) -> int:
    """Map priority to numeric weight for sorting."""
    return {'critical': 4, 'high': 3, 'medium': 2, 'low': 1}.get(priority, 1)


def energy_match_score(task: Task, target_date: date) -> float:
    """
    Score how well task's energy_level matches user's typical energy by time-of-day.
    Higher score = better match.
    """
    # Placeholder: Could integrate with user's circadian rhythm data
    # For now, assume standard: high energy 8am-12pm, medium 1pm-5pm, low 6pm-9pm
    return 1.0 if task.energy_level in ['high', 'medium'] else 0.5


def format_daily_todo(target_date: date, schedule: dict, total_hours: float) -> str:
    """
    Generate markdown output for daily TODO file.
    """
    output = f"""# Daily TODO: {target_date.strftime('%A, %B %d, %Y')}

**Total Planned:** {total_hours}h · **Capacity:** 6h

---

## Morning (High Energy) 8:00 - 12:00
"""
    for task in schedule['morning']:
        output += f"- [ ] **{task.title}** ({task.estimate_hours}h) · {task.priority.upper()}\n"
        output += f"  - Project: {task.project_id}\n"
        if task.due_date:
            output += f"  - Due: {task.due_date}\n"

    output += "\n## Afternoon (Medium Energy) 1:00 - 5:00\n"
    for task in schedule['afternoon']:
        output += f"- [ ] {task.title} ({task.estimate_hours}h) · {task.priority.upper()}\n"

    output += "\n## Evening (Low Energy) 6:00 - 9:00\n"
    for task in schedule['evening']:
        output += f"- [ ] {task.title} ({task.estimate_hours}h) · {task.priority.upper()}\n"

    return output
```

### 4.3 Output Location

**File Path:** `_output/daily-todos/YYYY-MM-DD.md`

**Example Output:**
```markdown
# Daily TODO: Thursday, February 06, 2026

**Total Planned:** 6.0h · **Capacity:** 6h

---

## Morning (High Energy) 8:00 - 12:00

- [ ] **Implement Section 1.12 (Life OS v3.0)** (3h) · HIGH
  - Project: project-002-life-os-v3
  - Due: 2026-02-10

- [ ] **Review PR #142** (2h) · HIGH
  - Project: project-002-life-os-v3
  - Due: 2026-02-07

## Afternoon (Medium Energy) 1:00 - 5:00

- [ ] Update documentation (1h) · MEDIUM
  - Project: project-002-life-os-v3

## Evening (Low Energy) 6:00 - 9:00

(No tasks scheduled)
```

### 4.4 Advanced Features

**Dynamic Capacity Adjustment:**
- Track actual completion rate: `actual_hours / estimate_hours` per day
- Adjust future capacity: If consistently over/under estimate → suggest new daily capacity

**Energy-Based Optimization:**
- Learn user's actual peak performance times (via completion velocity tracking)
- Adjust time-of-day assignments based on historical data

**Dependency Auto-Unblock:**
- When task marked `done` → Check if any `blocked` tasks can now start
- Auto-move `blocked` → `todo` if all dependencies resolved

---

## 5. Task Completion Definition

### 5.1 Completion Criteria

A task is considered **"done"** when ALL of the following are true:

1. ✅ `status = done` (set explicitly by user or system)
2. ✅ `completed_at` timestamp is set (auto-populated on status change)
3. ✅ `actual_hours` recorded (can be 0 if instant, but must be set)
4. ✅ Linked project progress updated (trigger automatic recalculation)

### 5.2 Completion Workflow

**User Action:**
```
User clicks [Mark Done] → System executes:

1. Validate preconditions:
   - Task is not blocked (dependencies all done)
   - Task belongs to ACTIVE project

2. Update task record:
   UPDATE tasks
   SET status = 'done',
       completed_at = NOW(),
       actual_hours = COALESCE(actual_hours, estimate_hours)  -- Default if not tracked
   WHERE task_id = :task_id;

3. Update project progress:
   UPDATE projects
   SET progress_percent = (
     SELECT ROUND(SUM(CASE WHEN status='done' THEN 1 ELSE 0 END)::numeric / COUNT(*) * 100, 1)
     FROM tasks WHERE project_id = :project_id
   )
   WHERE project_id = :project_id;

4. Check milestone:
   IF project.progress_percent >= milestone.target_percent THEN
     NOTIFY user: "🎉 Milestone reached: {milestone.title}"
   END IF;

5. Update goal progress:
   -- Recalculate across all tasks with same goal_id
   UPDATE goals
   SET progress_percent = (
     SELECT ROUND(SUM(CASE WHEN t.status='done' THEN 1 ELSE 0 END)::numeric / COUNT(*) * 100, 1)
     FROM tasks t
     WHERE t.goal_id = :goal_id
   )
   WHERE goal_id = :goal_id;

6. Log to memory:
   CALL memory_store(
     key := 'life-os:tasks:' || :task_id || ':completed',
     value := jsonb_build_object(
       'completed_at', NOW(),
       'actual_hours', actual_hours,
       'estimate_hours', estimate_hours,
       'velocity', actual_hours / estimate_hours  -- <1 = faster than expected
     )
   );

7. Generate next suggestions:
   -- Find tasks that were blocked by this task
   UPDATE tasks
   SET status = 'todo'
   WHERE :task_id = ANY(dependencies)
     AND status = 'blocked'
     AND NOT EXISTS (
       SELECT 1 FROM tasks dep
       WHERE dep.task_id = ANY(tasks.dependencies)
         AND dep.status NOT IN ('done', 'cancelled')
     );
```

### 5.3 Automatic Triggers on Completion

| Trigger | Action | Purpose |
|---------|--------|---------|
| **Project Progress Update** | Recalculate `project.progress_percent` | Keep dashboard accurate |
| **Goal Progress Update** | Recalculate `goal.progress_percent` | Track long-term objectives |
| **Milestone Check** | Notify if milestone reached | Celebrate wins |
| **Dependency Unblock** | Auto-change `blocked` → `todo` | Keep workflow flowing |
| **Next Task Suggestion** | Show top 3 next tasks from same project | Maintain momentum |
| **Memory Log** | Store completion event in Claude Flow memory | Learn task velocity patterns |
| **Calendar Update** | Delete associated calendar event (if exists) | Clean up schedule |

### 5.4 Blocked Task Rules

**Definition:** A task with `status = blocked` cannot be worked on until all dependencies are resolved.

**Blocking Conditions:**
- At least one task in `dependencies[]` is not `done` or `cancelled`

**Auto-Unblock Logic:**
```sql
-- Check if task should be unblocked
SELECT task_id
FROM tasks t
WHERE t.status = 'blocked'
  AND NOT EXISTS (
    SELECT 1 FROM tasks dep
    WHERE dep.task_id = ANY(t.dependencies)
      AND dep.status NOT IN ('done', 'cancelled')
  );

-- If query returns task_id → Change status to 'todo'
```

**UI Display:**
- Show in "Blocked Queue" dashboard view
- Display blocking tasks: "⚠️ Blocked by: task-003, task-007"
- Suggest alternative tasks from same project (no blockers)

---

## 6. Calendar Integration (Time Blocks)

### 6.1 Time Block Creation

**Trigger Points:**
1. Daily TODO generation (automatic)
2. Manual task scheduling (user action)
3. Week plan creation (batch scheduling)

**Default Duration:** `task.estimate_hours` converted to calendar blocks

**Placement Rules:**
- Respect `energy_level`:
  - `high` → Morning (8am-12pm)
  - `medium` → Afternoon (1pm-5pm)
  - `low` → Evening (6pm-9pm)
- Respect user's work hours preference (from profile)
- Avoid existing calendar conflicts (check availability)

### 6.2 Calendar Event Schema

```yaml
event_id: string         # Unique calendar event ID (e.g., "cal-evt-001")
task_id: string          # Linked task (e.g., "task-001-setup-db")
title: string            # Task title
start: datetime          # ISO 8601 with timezone (e.g., "2026-02-06T09:00:00-08:00")
end: datetime            # start + estimate_hours
calendar: string         # "Work" or "Personal"
color: string            # Priority-based (critical=red, high=orange, medium=blue, low=gray)
reminders: number[]      # Minutes before [15, 60] (15min, 1hour)
location: string         # Optional (e.g., "Home Office", "Meeting Room A")
attendees: string[]      # Optional (for collaborative tasks)
```

**Example Calendar Event:**
```json
{
  "event_id": "cal-evt-042",
  "task_id": "task-001-setup-db",
  "title": "Setup PostgreSQL database",
  "start": "2026-02-06T09:00:00-08:00",
  "end": "2026-02-06T13:00:00-08:00",
  "calendar": "Work",
  "color": "#FF6B6B",
  "reminders": [15, 60],
  "location": "Home Office",
  "attendees": []
}
```

### 6.3 Sync with External Calendar

**Phase 1: No External Sync**
- Markdown-only
- Calendar events stored in `_output/calendar/YYYY-MM.md`

**Phase 2: One-Way Sync (Life OS → Google Calendar)**

**Integration:**
```javascript
// Google Calendar API integration
async function syncTaskToCalendar(task) {
  const event = {
    summary: task.title,
    start: {
      dateTime: calculateStartTime(task.energy_level),
      timeZone: 'America/Los_Angeles'
    },
    end: {
      dateTime: calculateEndTime(task.energy_level, task.estimate_hours),
      timeZone: 'America/Los_Angeles'
    },
    colorId: getPriorityColor(task.priority),
    reminders: {
      useDefault: false,
      overrides: [
        { method: 'popup', minutes: 15 },
        { method: 'popup', minutes: 60 }
      ]
    },
    extendedProperties: {
      private: {
        task_id: task.task_id,
        project_id: task.project_id
      }
    }
  };

  await calendar.events.insert({
    calendarId: 'primary',
    resource: event
  });
}

function calculateStartTime(energy_level) {
  const today = new Date();
  switch(energy_level) {
    case 'high': return new Date(today.setHours(9, 0, 0));  // 9am
    case 'medium': return new Date(today.setHours(13, 0, 0)); // 1pm
    case 'low': return new Date(today.setHours(18, 0, 0));  // 6pm
  }
}
```

**Phase 3: Two-Way Sync (Life OS ↔ Google Calendar)**

**Sync Scenarios:**

| Change | Direction | Action |
|--------|-----------|--------|
| Task created in Life OS | Life OS → Calendar | Create event |
| Task completed in Life OS | Life OS → Calendar | Delete event |
| Task rescheduled in Life OS | Life OS → Calendar | Update event start/end |
| Event rescheduled in Calendar | Calendar → Life OS | Update `task.due_date` |
| Event deleted in Calendar | Calendar → Life OS | Mark task as "unscheduled" (not cancelled) |

**Conflict Resolution:**

```python
def handle_calendar_conflict(task, calendar_event):
    """
    Resolve conflicts when both task and calendar event are modified.
    """
    if task.updated_at > calendar_event.updated:
        # Task modified more recently → Task wins
        sync_task_to_calendar(task)
    else:
        # Calendar modified more recently → Calendar wins
        update_task_from_calendar(task, calendar_event)

    # Log conflict for user review
    log_conflict(task, calendar_event, resolution='last_write_wins')
```

**Special Cases:**

1. **Task Completed Before Event:**
   - Action: Delete calendar event
   - Reason: No need to block time for finished work

2. **Calendar Event Deleted:**
   - Action: Mark task as "unscheduled" (NOT cancelled)
   - Reason: User may want to reschedule, not abandon task

3. **Recurring Tasks:**
   - Action: Create recurring calendar event with same frequency
   - Example: Daily standup → Daily calendar event

### 6.4 Time Block Optimization

**Gap Filling:**
- If user has <6 hours scheduled → Suggest low-priority tasks to fill gaps

**Buffer Time:**
- Add 15-minute buffers between tasks (prevent context-switching fatigue)

**Focus Blocks:**
- Group similar tasks together (e.g., 3 coding tasks in morning block)

**Break Scheduling:**
- Auto-insert 10-min breaks every 90 minutes (Pomodoro-style)

---

## 7. API Reference (Phase 3)

### 7.1 Core Endpoints

**Create Task:**
```http
POST /api/tasks
Content-Type: application/json

{
  "project_id": "project-002",
  "goal_id": "2026-business-q1-1",
  "title": "Setup database",
  "status": "todo",
  "priority": "high",
  "estimate_hours": 4,
  "energy_level": "high",
  "due_date": "2026-02-10",
  "tags": ["backend", "infrastructure"]
}

Response: 201 Created
{
  "task_id": "task-019-setup-db",
  "created_at": "2026-02-06T10:00:00Z"
}
```

**Update Task:**
```http
PATCH /api/tasks/:task_id
Content-Type: application/json

{
  "status": "in_progress",
  "actual_hours": 2.5
}

Response: 200 OK
{
  "task_id": "task-001",
  "updated_at": "2026-02-06T14:30:00Z"
}
```

**Complete Task:**
```http
POST /api/tasks/:task_id/complete
Content-Type: application/json

{
  "actual_hours": 4.5
}

Response: 200 OK
{
  "task_id": "task-001",
  "status": "done",
  "completed_at": "2026-02-06T17:00:00Z",
  "project_progress": 67,
  "goal_progress": 45
}
```

**Get Daily TODO:**
```http
GET /api/tasks/daily?date=2026-02-06

Response: 200 OK
{
  "date": "2026-02-06",
  "capacity_hours": 6,
  "scheduled_hours": 6,
  "tasks": [
    {
      "task_id": "task-001",
      "title": "Setup database",
      "time_of_day": "morning",
      "estimate_hours": 3,
      "priority": "high"
    }
  ]
}
```

### 7.2 Webhook Endpoints (External Integrations)

**Todoist Completion Webhook:**
```http
POST /webhooks/todoist/completion
Content-Type: application/json

{
  "event_name": "item:completed",
  "event_data": {
    "id": "todoist-12345",
    "content": "[task-001] Setup database"
  }
}

Response: 200 OK
{
  "status": "processed",
  "task_id": "task-001",
  "updated": true
}
```

---

## 8. Performance & Scalability

### 8.1 Query Optimization

**Critical Queries (<200ms target):**

1. **Daily TODO Generation:**
```sql
-- Index required: (status, project.status, due_date)
EXPLAIN ANALYZE
SELECT t.*
FROM tasks t
LEFT JOIN projects p ON p.project_id = t.project_id
WHERE t.status IN ('todo', 'in_progress')
  AND p.status = 'ACTIVE'
  AND (t.due_date <= CURRENT_DATE OR t.task_id = ANY(:week_plan_tasks));
```

2. **Project Progress Dashboard:**
```sql
-- Index required: (project_id, status)
EXPLAIN ANALYZE
SELECT
  p.project_id,
  COUNT(t.task_id) as total,
  SUM(CASE WHEN t.status='done' THEN 1 ELSE 0 END) as done
FROM projects p
LEFT JOIN tasks t ON t.project_id = p.project_id
WHERE p.status = 'ACTIVE'
GROUP BY p.project_id;
```

### 8.2 Caching Strategy

| Data | Cache Duration | Invalidation Trigger |
|------|----------------|---------------------|
| Daily TODO | No cache (real-time) | N/A |
| Project Progress | 5 minutes | Task status change |
| Goal Progress | 10 minutes | Task completion |
| Calendar Events | No cache | Real-time sync required |

### 8.3 Scaling Considerations

**Up to 100 Tasks:**
- Markdown files sufficient
- No database needed

**100-1000 Tasks:**
- Migrate to Supabase
- Add HNSW indexing for search

**1000+ Tasks:**
- Partition tasks by year/quarter
- Archive completed tasks >1 year old
- Implement full-text search (PostgreSQL FTS)

---

## 9. Testing Scenarios

### 9.1 Unit Tests

**Task Creation:**
- ✅ Valid task created successfully
- ❌ Reject task with invalid `project_id`
- ❌ Reject task with `estimate_hours < 0.5` or `> 40`
- ❌ Reject task with invalid `status` enum value

**Task Completion:**
- ✅ Status changes to `done`, `completed_at` set
- ✅ Project progress updated correctly
- ✅ Goal progress updated correctly
- ✅ Blocked tasks auto-unblocked if dependencies resolved

**Daily TODO Generation:**
- ✅ Tasks sorted by priority and due date
- ✅ Capacity constraint respected (total_hours <= 6)
- ✅ Energy levels matched to time-of-day
- ✅ Blocked tasks excluded from TODO

### 9.2 Integration Tests

**Todoist Sync (Phase 2):**
- ✅ Task created in Life OS → appears in Todoist
- ✅ Task completed in Todoist → marked done in Life OS
- ✅ Conflict resolution (last-write-wins)

**Calendar Sync (Phase 3):**
- ✅ Task scheduled → calendar event created
- ✅ Task completed → calendar event deleted
- ✅ Calendar event rescheduled → task due_date updated

### 9.3 Performance Tests

**Load Scenarios:**
- 100 tasks: Daily TODO generation <50ms
- 1000 tasks: Daily TODO generation <200ms
- 10,000 tasks: Daily TODO generation <1s (with indexing)

---

## 10. Migration Guide

### 10.1 Phase 1 → Phase 2 (Add Todoist Sync)

**Steps:**
1. Export all tasks from Markdown to JSON
2. Create Todoist projects (one per Life OS project)
3. Create Todoist tasks via API (with `[task-id]` prefix)
4. Setup webhook endpoint for Todoist completions
5. Test round-trip sync (Life OS → Todoist → Life OS)

**Migration Script:**
```bash
#!/bin/bash
# Migrate Markdown tasks to Todoist
python scripts/migrate-to-todoist.py \
  --source projects/ \
  --todoist-token $TODOIST_API_TOKEN \
  --dry-run false
```

### 10.2 Phase 2 → Phase 3 (Add Supabase)

**Steps:**
1. Create Supabase project and `tasks` table
2. Export Markdown tasks to Supabase (bulk insert)
3. Verify data integrity (count tasks, check linkages)
4. Switch application to read from Supabase (not Markdown)
5. Keep Markdown as backup (optional mirror)

**Migration Script:**
```sql
-- Bulk insert from JSON export
INSERT INTO tasks (task_id, project_id, goal_id, title, status, priority, estimate_hours, energy_level, due_date, created_at)
SELECT
  t.task_id,
  t.project_id,
  t.goal_id,
  t.title,
  t.status,
  t.priority,
  t.estimate_hours,
  t.energy_level,
  t.due_date,
  t.created_at
FROM json_populate_recordset(NULL::tasks, '[...]') t;
```

---

## 11. Appendix

### 11.1 Example Week Plan

**File:** `projects/project-002/week-plan.md`

```markdown
# Week Plan: Feb 3 - Feb 9, 2026

**Project:** Life OS v3.0 Implementation
**Goal:** 2026-business-q1-1 (Ship v3.0 by Q1 end)
**Capacity:** 30 hours (6h/day × 5 days)

---

## Monday, Feb 3
- [ ] task-015-implement-section-1-9 (4h) · HIGH
- [ ] task-016-test-scoring-criteria (2h) · MEDIUM

## Tuesday, Feb 4
- [ ] task-017-implement-section-1-12 (3h) · HIGH
- [ ] task-018-calendar-integration (3h) · HIGH

## Wednesday, Feb 5
- [ ] task-019-ui-components (4h) · MEDIUM
- [ ] task-020-documentation-update (2h) · LOW

## Thursday, Feb 6
- [ ] task-021-testing-full-workflow (5h) · CRITICAL
- [ ] task-022-bug-fixes (1h) · HIGH

## Friday, Feb 7
- [ ] task-023-deployment-prep (3h) · HIGH
- [ ] task-024-user-onboarding-guide (2h) · MEDIUM

---

**Progress:** 0/10 tasks complete (0%)
**Estimated:** 30 hours
**Actual:** 0 hours (track as you go)
```

### 11.2 Example Daily TODO (Generated)

**File:** `_output/daily-todos/2026-02-06.md`

```markdown
# Daily TODO: Thursday, February 06, 2026

**Total Planned:** 6.0h · **Capacity:** 6h · **Progress:** 0/3 tasks done

---

## Morning (High Energy) 8:00 - 12:00

- [ ] **🔴 task-021-testing-full-workflow** (5h) · CRITICAL
  - Project: project-002-life-os-v3
  - Goal: 2026-business-q1-1
  - Due: 2026-02-07 (tomorrow!)
  - Description: Run end-to-end tests for all workflows

---

## Afternoon (Medium Energy) 1:00 - 5:00

- [ ] **🟠 task-022-bug-fixes** (1h) · HIGH
  - Project: project-002-life-os-v3
  - Goal: 2026-business-q1-1
  - Due: 2026-02-07
  - Description: Fix critical bugs from QA

---

## Evening (Low Energy) 6:00 - 9:00

(No tasks scheduled - Take a break! 🎉)
```

### 11.3 Task Dependencies Example

**Scenario:** Building a SaaS product

```yaml
# Dependency Graph
tasks:
  - task_id: task-001-database-setup
    dependencies: []  # No blockers

  - task_id: task-002-api-auth
    dependencies: [task-001-database-setup]  # Needs DB first

  - task_id: task-003-api-endpoints
    dependencies: [task-001-database-setup, task-002-api-auth]  # Needs DB + Auth

  - task_id: task-004-frontend-ui
    dependencies: [task-003-api-endpoints]  # Needs API first

  - task_id: task-005-integration-tests
    dependencies: [task-004-frontend-ui]  # Needs everything
```

**Execution Order:**
1. `task-001` (no blockers, can start immediately)
2. `task-002` (waits for task-001 to complete)
3. `task-003` (waits for both task-001 AND task-002)
4. `task-004` (waits for task-003)
5. `task-005` (waits for task-004)

**Critical Path:** task-001 → task-002 → task-003 → task-004 → task-005 (all tasks are on critical path)

---

## Document Status

**Version:** 1.0
**Last Updated:** 2026-02-06
**Status:** ✅ READY FOR IMPLEMENTATION
**Source:** IDEAL-BEHAVIOR-REFERENCE.md Section 1.12

**Next Steps:**
1. Implement Task Data Model (Phase 1: Markdown)
2. Build Daily TODO Generation Algorithm
3. Create Calendar Integration (Phase 2: One-way sync)
4. Add Supabase Migration (Phase 3)

**Related Documents:**
- `IDEAL-BEHAVIOR-REFERENCE.md` Section 1.12 (source)
- `IDEAL-BEHAVIOR-REFERENCE.md` Section 1.13 (UI integration)
- `IDEAL-BEHAVIOR-REFERENCE.md` Section 1.14 (Planning data model for Gantt/roadmap)
