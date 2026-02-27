# UI Screens Specification - Life OS v3.0

**Created:** 2026-02-06
**Purpose:** Complete specification of minimum viable UI screens for Life OS
**Source:** IDEAL-BEHAVIOR-REFERENCE.md Section 1.13
**Status:** ✅ Implementation Ready

---

## Overview

This document defines the **5 mandatory screens** required for Life OS v3.0 MVP:

1. **Portfolio Dashboard** - Active projects overview and capacity monitoring
2. **Decision Queue** - Evaluated ideas waiting for GO/NO-GO decisions
3. **Today View** - Daily TODO list with time blocks
4. **Calendar View** - Weekly/monthly timeline visualization
5. **Project Detail Page** - Complete project information with tabs

Each screen includes:
- Data requirements (SQL queries)
- UI components (shadcn/ui mapping)
- Example views
- Query optimization strategies

---

## 1. Portfolio Dashboard

### 1.1 Purpose
Overview of all active projects, capacity monitoring, and priority management.

### 1.2 Data Requirements

```sql
SELECT
  projects.id,
  projects.title,
  projects.status,
  projects.progress_percent,
  projects.priority,
  projects.due_date,
  COUNT(tasks.id) as total_tasks,
  SUM(CASE WHEN tasks.status = 'done' THEN 1 ELSE 0 END) as completed_tasks,
  projects.origin_idea_id
FROM projects
LEFT JOIN tasks ON tasks.project_id = projects.id
WHERE projects.status IN ('ACTIVE', 'PLANNED')
GROUP BY projects.id
ORDER BY projects.priority DESC, projects.due_date ASC
```

**Indexes Required:**
```sql
CREATE INDEX idx_projects_portfolio ON projects (status, priority, due_date);
CREATE INDEX idx_tasks_project ON tasks (project_id, status);
```

### 1.3 UI Components

| Component | shadcn/ui | Usage |
|-----------|-----------|-------|
| Header | `Typography` + `Badge` | Title and capacity indicator |
| Filters | `Select` + `Tabs` | Status, priority, sphere filters |
| Sort Controls | `DropdownMenu` | Sort by priority/date/progress |
| Project Cards | `Card` + `CardHeader` + `CardContent` | Project display |
| Progress Bar | `Progress` | Completion percentage |
| Status Badge | `Badge` | ACTIVE/PLANNED status |
| Priority Badge | `Badge` (color variants) | HIGH/MEDIUM/LOW |
| Action Buttons | `Button` + `ButtonGroup` | View/Edit/Archive actions |

### 1.4 Example View

```
Portfolio Dashboard                                    3/5 Active (60% capacity)
───────────────────────────────────────────────────────────────────────────────
[Filters: Status ▼] [Priority ▼] [Sphere ▼]        [Sort: Priority ▼]

┌─────────────────────────────────────────────────────────────────────┐
│ 🔴 Life OS v3.0 Implementation                        Progress: 67% │
│ Due: 2026-03-15 · Business · 12/18 tasks done                       │
│ [View Details] [Edit]                                               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ 🟠 Personal Finance Dashboard                         Progress: 45% │
│ Due: 2026-02-28 · Finance · 5/11 tasks done                         │
│ [View Details] [Edit]                                               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ 🟡 Health Tracking App                                Progress: 23% │
│ Due: 2026-04-10 · Health · 3/13 tasks done                          │
│ [View Details] [Edit]                                               │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.5 Responsive Behavior

- **Desktop (>1024px):** 2-column grid, all filters visible
- **Tablet (768-1024px):** 1-column, filters in dropdown
- **Mobile (<768px):** Single column, swipe cards, bottom sheet filters

### 1.6 Performance Targets

- **Initial Load:** <500ms (with cache)
- **Filter/Sort:** <100ms (client-side)
- **Refresh:** <200ms (incremental update)

---

## 2. Decision Queue

### 2.1 Purpose
Display all evaluated ideas waiting for GO/NO-GO/WAIT decision.

### 2.2 Data Requirements

```sql
SELECT
  ideas.id,
  ideas.title,
  ideas.sphere,
  ideas.score,
  ideas.decision_status,
  ideas.evaluated_at,
  ideas.track_type
FROM ideas
WHERE ideas.status = 'EVALUATED'
  AND ideas.decision_status IS NULL
ORDER BY ideas.score DESC, ideas.evaluated_at ASC
```

**Indexes Required:**
```sql
CREATE INDEX idx_ideas_decision_queue ON ideas (status, decision_status, score DESC);
CREATE INDEX idx_ideas_evaluated_at ON ideas (evaluated_at);
```

### 2.3 UI Components

| Component | shadcn/ui | Usage |
|-----------|-----------|-------|
| Header | `Typography` + `Badge` | Title with pending count |
| Filters | `Select` + `Slider` | Track type, sphere, score range |
| Idea Cards | `Card` | Idea display with metadata |
| Score Badge | `Badge` (color-coded) | 0.0-5.0 score with color |
| Track Badge | `Badge` | Quick/Standard/Deep indicator |
| Decision Buttons | `Button` (variants) | GO (green), NO-GO (red), WAIT (yellow) |
| Details Dialog | `Dialog` + `DialogContent` | Full idea review modal |

### 2.4 Score Badge Color Logic

```typescript
function getScoreBadgeColor(score: number): string {
  if (score >= 4.0) return "green"; // HIGH priority
  if (score >= 3.0) return "yellow"; // MEDIUM priority
  return "red"; // LOW priority
}
```

### 2.5 Example View

```
Decision Queue                                           5 ideas waiting
───────────────────────────────────────────────────────────────────────────────
[Filters: Track ▼] [Sphere ▼] [Score ▼]               [Sort: Score ▼]

┌─────────────────────────────────────────────────────────────────────┐
│ SaaS Project Management Tool                          Score: 4.5/5.0 │
│ 🟢 HIGH Priority · Business · Deep Track · Evaluated: 2 days ago     │
│ [GO ✅] [NO-GO ❌] [WAIT ⏸️] [View Details]                          │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ Health Tracking App                                   Score: 3.2/5.0 │
│ 🟡 MEDIUM Priority · Health · Standard · Evaluated: 5 days ago       │
│ [GO ✅] [NO-GO ❌] [WAIT ⏸️] [View Details]                          │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ E-commerce Platform                                   Score: 2.1/5.0 │
│ 🔴 LOW Priority · Wealth · Quick Track · Evaluated: 7 days ago       │
│ [GO ✅] [NO-GO ❌] [WAIT ⏸️] [View Details]                          │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.6 Decision Actions

**GO Button:**
- Move file: `ideas-bank/evaluated/` → `ideas-bank/planned/`
- Update: `decision_status = "GO"`, `decided_at = NOW()`
- Log to memory: `life-os:ideas:{id}:decision-go`
- Prompt: "Ready to activate now? (Create project)"

**NO-GO Button:**
- Move file: `ideas-bank/evaluated/` → `ideas-bank/archive/rejected/`
- Update: `decision_status = "NO-GO"`, `rejected_reason = [prompt user]`
- Log to memory: `life-os:ideas:{id}:decision-no-go`

**WAIT Button:**
- Move file: `ideas-bank/evaluated/` → `ideas-bank/archive/postponed/`
- Update: `decision_status = "WAIT"`, `review_after = [prompt date]`
- Log to memory: `life-os:ideas:{id}:decision-wait`

### 2.7 Performance Targets

- **Initial Load:** <300ms
- **Decision Action:** <200ms (includes file move)
- **Filter:** <50ms (client-side)

---

## 3. Today View

### 3.1 Purpose
Daily TODO list with time blocks and energy-aware task distribution.

### 3.2 Data Requirements

```sql
SELECT
  tasks.id,
  tasks.title,
  tasks.project_id,
  projects.title as project_title,
  tasks.status,
  tasks.priority,
  tasks.estimate_hours,
  tasks.energy_level,
  tasks.due_date,
  calendar_events.start_time,
  calendar_events.end_time
FROM tasks
LEFT JOIN projects ON projects.id = tasks.project_id
LEFT JOIN calendar_events ON calendar_events.task_id = tasks.id
WHERE projects.status = 'ACTIVE'
  AND tasks.status IN ('todo','in_progress','blocked')
  AND (
    (tasks.due_date IS NOT NULL AND tasks.due_date <= CURRENT_DATE)
    OR calendar_events.start_time::date = CURRENT_DATE
  )
ORDER BY calendar_events.start_time ASC, tasks.priority DESC
```

**Indexes Required:**
```sql
CREATE INDEX idx_tasks_today ON tasks (due_date, status, priority);
CREATE INDEX idx_calendar_today ON calendar_events (start_time);
CREATE INDEX idx_projects_active ON projects (status);
```

### 3.3 UI Components

| Component | shadcn/ui | Usage |
|-----------|-----------|-------|
| Header | `Typography` + metrics | Date, completion, hours |
| Time Blocks | `Card` (timeline layout) | Hourly schedule (8am-8pm) |
| Task Cards | `Card` + `Checkbox` | Individual task display |
| Energy Indicator | `Badge` (color-coded) | 🔴 High, 🟡 Medium, 🔵 Low |
| Timer | `Button` + Timer component | Start/stop Pomodoro timer |
| Quick Actions | `Button` + `DropdownMenu` | Mark done, reschedule, skip |

### 3.4 Energy Level Mapping

```typescript
const energyConfig = {
  high: {
    icon: "🔴",
    label: "High Energy",
    color: "red",
    timeOfDay: "morning" // 8am-12pm
  },
  medium: {
    icon: "🟡",
    label: "Medium Energy",
    color: "yellow",
    timeOfDay: "afternoon" // 2pm-6pm
  },
  low: {
    icon: "🔵",
    label: "Low Energy",
    color: "blue",
    timeOfDay: "evening" // 6pm-8pm
  }
};
```

### 3.5 Example View

```
Today: Thursday, Feb 6, 2026                          3/8 tasks done · 6h planned
───────────────────────────────────────────────────────────────────────────────
Morning (High Energy)                                              8:00 - 12:00
┌─────────────────────────────────────────────────────────────────────┐
│ ✅ Review PR #142 (Life OS v3.0)                      2h · 🔴 High   │
│ Started: 8:30am · Completed: 10:15am                               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ ⏳ Implement Section 1.9 (Life OS v3.0)               3h · 🔴 High   │
│ Scheduled: 10:30am - 1:30pm                    [Mark Done] [Start] │
└─────────────────────────────────────────────────────────────────────┘

Afternoon (Medium Energy)                                        2:00 - 6:00
┌─────────────────────────────────────────────────────────────────────┐
│ 📝 Update documentation (Life OS v3.0)                1h · 🟡 Medium │
│ Scheduled: 2:00pm - 3:00pm                     [Mark Done] [Start] │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ 🔨 Refactor scoring logic (Finance Dashboard)        2h · 🟡 Medium │
│ Scheduled: 3:00pm - 5:00pm                     [Mark Done] [Start] │
└─────────────────────────────────────────────────────────────────────┘

Evening (Low Energy)                                             6:00 - 8:00
┌─────────────────────────────────────────────────────────────────────┐
│ 📧 Review emails and messages                         1h · 🔵 Low    │
│ Scheduled: 6:00pm - 7:00pm                     [Mark Done] [Start] │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.6 Task Completion Flow

```typescript
async function markTaskDone(taskId: string) {
  // 1. Update task status
  await db.tasks.update({
    where: { id: taskId },
    data: {
      status: 'done',
      completed_at: new Date(),
      actual_hours: calculateActualHours() // from timer
    }
  });

  // 2. Update project progress
  await updateProjectProgress(task.project_id);

  // 3. Delete calendar event
  await db.calendar_events.deleteMany({
    where: { task_id: taskId }
  });

  // 4. Log to memory
  await memory.store({
    key: `life-os:tasks:${taskId}:completed`,
    value: { completed_at: new Date(), actual_hours: task.actual_hours }
  });

  // 5. Check for milestone completion
  await checkMilestoneProgress(task.project_id);
}
```

### 3.7 Performance Targets

- **Initial Load:** <200ms (must be instant)
- **Task Completion:** <100ms (optimistic UI update)
- **Timer Sync:** <50ms (local state)

---

## 4. Calendar View

### 4.1 Purpose
Visual timeline of all scheduled tasks across weeks/months with drag-and-drop rescheduling.

### 4.2 Data Requirements

```sql
SELECT
  calendar_events.id,
  calendar_events.task_id,
  tasks.title,
  tasks.project_id,
  projects.title as project_title,
  projects.color,
  calendar_events.start_time,
  calendar_events.end_time,
  calendar_events.calendar_type
FROM calendar_events
LEFT JOIN tasks ON tasks.id = calendar_events.task_id
LEFT JOIN projects ON projects.id = tasks.project_id
WHERE calendar_events.start_time >= :start_date
  AND calendar_events.start_time <= :end_date
ORDER BY calendar_events.start_time ASC
```

**Indexes Required:**
```sql
CREATE INDEX idx_calendar_range ON calendar_events (start_time, end_time);
CREATE INDEX idx_calendar_type ON calendar_events (calendar_type);
```

### 4.3 UI Components

| Component | shadcn/ui | Usage |
|-----------|-----------|-------|
| View Switcher | `Tabs` | Day / Week / Month / Agenda |
| Calendar Grid | Custom (react-big-calendar) | Timeline layout |
| Event Blocks | Draggable `Card` | Color-coded by project |
| Sidebar | `Sheet` | Unscheduled tasks list |
| Filters | `Select` + `Checkbox` | Calendar type, project, priority |
| Quick Add | `Popover` + `Form` | Create new event/task |

### 4.4 Event Color Coding

```typescript
function getEventColor(priority: string, isCritical: boolean): string {
  if (isCritical) return "red"; // Critical path tasks

  switch (priority) {
    case "critical": return "red";
    case "high": return "orange";
    case "medium": return "blue";
    case "low": return "gray";
    default: return "blue";
  }
}
```

### 4.5 Example Week View

```
Week of Feb 3 - Feb 9, 2026                               [Day][Week][Month]
───────────────────────────────────────────────────────────────────────────────
         Mon 3      Tue 4      Wed 5      Thu 6      Fri 7      Sat 8  Sun 9
8:00  ┌─────────┐
      │ PR #142 │
10:00 └─────────┘  ┌─────────┐  ┌─────────┐  ┌─────────┐
                   │Section   │  │Testing  │  │Deploy   │
12:00              │1.9       │  │         │  │         │
                   └─────────┘  └─────────┘  └─────────┘
2:00               ┌─────────┐  ┌─────────┐
                   │Docs     │  │Review   │
4:00               └─────────┘  └─────────┘
                                            ┌─────────┐
6:00                                        │Weekend  │
                                            │Tasks    │
8:00                                        └─────────┘

Unscheduled Tasks (Sidebar)
───────────────────────────
🔴 Fix bug #123 (2h)
🟠 Write tests (3h)
🟡 Update README (1h)
```

### 4.6 Drag-and-Drop Rescheduling

```typescript
async function handleEventDrop(event: CalendarEvent, newStart: Date) {
  // 1. Calculate new end time
  const duration = event.end_time - event.start_time;
  const newEnd = new Date(newStart.getTime() + duration);

  // 2. Update calendar event
  await db.calendar_events.update({
    where: { id: event.id },
    data: {
      start_time: newStart,
      end_time: newEnd
    }
  });

  // 3. Update task due date (if applicable)
  if (event.task_id) {
    await db.tasks.update({
      where: { id: event.task_id },
      data: { due_date: newStart }
    });
  }

  // 4. Check for conflicts
  await checkScheduleConflicts(newStart, newEnd);
}
```

### 4.7 Performance Targets

- **View Switch:** <300ms (with cache)
- **Drag-and-Drop:** <100ms (optimistic update)
- **Filter:** <50ms (client-side)

---

## 5. Project Detail Page

### 5.1 Purpose
Complete project information with plan, risks, tasks, and progress tracking.

### 5.2 Data Requirements

```sql
-- Main project data
SELECT * FROM projects WHERE id = :project_id;

-- Tasks breakdown
SELECT
  tasks.status,
  COUNT(*) as count,
  SUM(tasks.estimate_hours) as total_hours,
  SUM(tasks.actual_hours) as spent_hours
FROM tasks
WHERE tasks.project_id = :project_id
GROUP BY tasks.status;

-- Linked goal
SELECT * FROM goals
WHERE id = (SELECT goal_id FROM projects WHERE id = :project_id);

-- Origin idea
SELECT * FROM ideas
WHERE id = (SELECT origin_idea_id FROM projects WHERE id = :project_id);

-- Recent activity
SELECT * FROM activity_log
WHERE project_id = :project_id
ORDER BY created_at DESC
LIMIT 10;
```

**Indexes Required:**
```sql
CREATE INDEX idx_tasks_breakdown ON tasks (project_id, status);
CREATE INDEX idx_activity_project ON activity_log (project_id, created_at DESC);
```

### 5.3 UI Components

| Component | shadcn/ui | Usage |
|-----------|-----------|-------|
| Header | `Typography` + status badges | Title, status, priority |
| Progress Bar | `Progress` (large) | Overall completion |
| Tabs | `Tabs` + `TabsList` + `TabsContent` | Overview/Tasks/Plan/Risks/Timeline/Activity |
| Metrics Cards | `Card` (small, grid) | Key metrics display |
| Kanban Board | Custom (dnd-kit) | Task status columns |
| Risk Matrix | Custom chart | Likelihood × Impact |
| Gantt Chart | Custom (react-gantt) | Timeline with dependencies |
| Activity Feed | `ScrollArea` + timeline | Recent changes log |

### 5.4 Tab Specifications

#### 5.4.1 Overview Tab

**Content:**
- Key metrics (tasks, time, budget)
- Linked goal with progress
- Origin idea reference
- Quick stats

**Data:**
```typescript
interface ProjectOverview {
  metrics: {
    tasks_done: number;
    tasks_total: number;
    hours_spent: number;
    hours_estimated: number;
    budget_spent: number;
    budget_total: number;
  };
  goal: {
    id: string;
    title: string;
    progress_percent: number;
    status: "on_track" | "at_risk" | "delayed";
  };
  origin_idea: {
    id: string;
    title: string;
    score: number;
    evaluated_at: Date;
  };
}
```

#### 5.4.2 Tasks Tab

**Content:**
- Kanban board with 4 columns: TODO / IN PROGRESS / BLOCKED / DONE
- Drag-and-drop between columns
- Filter by priority, assignee, energy level

**Columns:**
```typescript
const taskColumns = [
  { id: "todo", title: "To Do", status: "todo" },
  { id: "in_progress", title: "In Progress", status: "in_progress" },
  { id: "blocked", title: "Blocked", status: "blocked" },
  { id: "done", title: "Done", status: "done" }
];
```

#### 5.4.3 Plan Tab

**Content:**
- Milestones with target dates
- Dependencies graph
- Resource allocation

**Data Model:**
```typescript
interface ProjectPlan {
  milestones: {
    id: string;
    title: string;
    target_date: Date;
    status: "not_started" | "in_progress" | "completed";
    progress_percent: number;
    dependencies: string[];
  }[];
  dependencies: {
    predecessor_id: string;
    successor_id: string;
    type: "FS" | "SS" | "FF" | "SF";
  }[];
}
```

#### 5.4.4 Risks Tab

**Content:**
- Risk matrix (2×2 or 3×3 grid)
- Risk register table
- Mitigation strategies

**Risk Levels:**
```typescript
const riskMatrix = {
  likelihood: ["low", "medium", "high"],
  impact: ["low", "medium", "high"],
  severity: {
    "low-low": "green",
    "low-medium": "yellow",
    "medium-medium": "orange",
    "high-high": "red"
  }
};
```

#### 5.4.5 Timeline Tab

**Content:**
- Gantt chart with critical path
- Milestone markers
- Today indicator
- Drag to reschedule

**Generation:**
- Use algorithm from Section 1.14.3 (IDEAL-BEHAVIOR-REFERENCE.md)
- Highlight critical path in red
- Show task dependencies as arrows

#### 5.4.6 Activity Tab

**Content:**
- Chronological log of all changes
- Who did what when
- Filters by action type

**Activity Types:**
```typescript
const activityTypes = [
  "task_created",
  "task_completed",
  "task_updated",
  "milestone_reached",
  "risk_added",
  "status_changed",
  "comment_added"
];
```

### 5.5 Example View

```
Life OS v3.0 Implementation                            🔴 HIGH · ⏳ ACTIVE
Progress: ████████████████████░░░░ 67% (12/18 tasks)  Due: Mar 15, 2026
───────────────────────────────────────────────────────────────────────────────
[Overview] [Tasks] [Plan] [Risks] [Timeline] [Activity]

Overview
────────
📊 Key Metrics
  • Tasks: 12/18 done (6 remaining)
  • Time: 48h spent / 72h estimated (67%)
  • Budget: $1,200 / $2,000 (60%)

🎯 Linked Goal
  → 2026-business-q1-1: "Ship v3.0 by Q1 end"
  → Progress to goal: 67% (on track ✅)

💡 Origin Idea
  → idea-042: "Complete Life OS system with memory + UI"
  → Score: 4.7/5.0 (evaluated 2025-12-20)

Recent Activity
───────────────
• 2h ago: Task "Review PR #142" marked as done by @user
• 5h ago: Task "Implement Section 1.9" started by @user
• 1d ago: Risk "UI complexity" severity reduced (HIGH → MEDIUM)
```

### 5.6 Performance Targets

- **Initial Load:** <500ms (with cache)
- **Tab Switch:** <100ms (lazy load content)
- **Kanban Drag:** <50ms (optimistic update)

---

## 6. Query Optimization Strategy

### 6.1 Critical Queries (Must Be <200ms)

1. **Portfolio Dashboard**
   - Index: `(project.status, project.priority, project.due_date)`
   - Cache: 5 minutes (invalidate on project create/update)

2. **Decision Queue**
   - Index: `(idea.status, idea.score DESC, idea.evaluated_at)`
   - Cache: 10 minutes (invalidate on idea evaluation)

3. **Today View**
   - Index: `(task.due_date, task.priority, calendar_event.start_time)`
   - Cache: None (real-time required)

4. **Calendar View**
   - Index: `(calendar_event.start_time, calendar_event.calendar_type)`
   - Cache: 10 minutes (invalidate on event create/update)

5. **Project Detail**
   - Index: `(project.id)` + denormalized task counts
   - Cache: 2 minutes (invalidate on task/project update)

### 6.2 Caching Implementation

**Redis Strategy:**
```typescript
const cacheConfig = {
  portfolio: {
    key: "dashboard:portfolio:${userId}",
    ttl: 300, // 5 minutes
    invalidate: ["project:create", "project:update"]
  },
  decision_queue: {
    key: "dashboard:decisions:${userId}",
    ttl: 600, // 10 minutes
    invalidate: ["idea:evaluate"]
  },
  calendar: {
    key: "calendar:${userId}:${startDate}:${endDate}",
    ttl: 600, // 10 minutes
    invalidate: ["event:create", "event:update"]
  }
};
```

### 6.3 Database Indexes

**Priority Indexes (Create First):**
```sql
-- Portfolio Dashboard
CREATE INDEX idx_projects_portfolio ON projects (status, priority, due_date);
CREATE INDEX idx_tasks_project_status ON tasks (project_id, status);

-- Decision Queue
CREATE INDEX idx_ideas_decisions ON ideas (status, decision_status, score DESC);

-- Today View
CREATE INDEX idx_tasks_today ON tasks (due_date, status, priority);
CREATE INDEX idx_calendar_today ON calendar_events (start_time);

-- Calendar View
CREATE INDEX idx_calendar_range ON calendar_events (start_time, end_time);

-- Project Detail
CREATE INDEX idx_tasks_breakdown ON tasks (project_id, status);
CREATE INDEX idx_activity_log ON activity_log (project_id, created_at DESC);
```

### 6.4 Query Optimization Techniques

**1. Denormalization:**
```sql
-- Add computed columns to projects table
ALTER TABLE projects ADD COLUMN task_count_total INT DEFAULT 0;
ALTER TABLE projects ADD COLUMN task_count_done INT DEFAULT 0;

-- Update via trigger
CREATE TRIGGER update_project_task_counts
AFTER INSERT OR UPDATE OR DELETE ON tasks
FOR EACH ROW EXECUTE FUNCTION update_task_counts();
```

**2. Materialized Views:**
```sql
-- Portfolio summary (refresh every 5 minutes)
CREATE MATERIALIZED VIEW portfolio_summary AS
SELECT
  projects.id,
  projects.title,
  projects.status,
  projects.progress_percent,
  COUNT(tasks.id) as total_tasks,
  SUM(CASE WHEN tasks.status = 'done' THEN 1 ELSE 0 END) as completed_tasks
FROM projects
LEFT JOIN tasks ON tasks.project_id = projects.id
WHERE projects.status IN ('ACTIVE', 'PLANNED')
GROUP BY projects.id;

CREATE UNIQUE INDEX idx_portfolio_summary ON portfolio_summary (id);
```

**3. Pagination:**
```typescript
// Infinite scroll for large lists
const ITEMS_PER_PAGE = 20;

async function fetchPortfolio(page: number) {
  return await db.projects.findMany({
    where: { status: { in: ['ACTIVE', 'PLANNED'] } },
    orderBy: [{ priority: 'desc' }, { due_date: 'asc' }],
    skip: page * ITEMS_PER_PAGE,
    take: ITEMS_PER_PAGE,
    include: {
      tasks: {
        select: { id: true, status: true }
      }
    }
  });
}
```

### 6.5 Performance Monitoring

**Metrics to Track:**
```typescript
interface QueryMetrics {
  endpoint: string;
  duration_ms: number;
  cache_hit: boolean;
  row_count: number;
  timestamp: Date;
}

// Alert if query exceeds threshold
if (duration_ms > 200) {
  logSlowQuery({
    endpoint,
    duration_ms,
    query_plan: explainAnalyze(query)
  });
}
```

---

## 7. Responsive Design Breakpoints

### 7.1 Screen Size Targets

| Breakpoint | Width | Layout | Notes |
|------------|-------|--------|-------|
| Mobile | <640px | Single column | Bottom nav, cards full-width |
| Tablet | 640-1024px | 1-2 columns | Sidebar collapses to drawer |
| Desktop | 1024-1440px | 2-3 columns | Standard layout |
| Wide | >1440px | 3-4 columns | Extra sidebar space |

### 7.2 Component Adaptations

**Portfolio Dashboard:**
- Mobile: Single column, swipe cards
- Tablet: 1 column, filters in sheet
- Desktop: 2 columns, all filters visible

**Decision Queue:**
- Mobile: Vertical stack, bottom sheet actions
- Tablet: 1 column, inline actions
- Desktop: 2 columns, sidebar filters

**Today View:**
- Mobile: Vertical timeline, compact cards
- Tablet: Half-hour increments, side agenda
- Desktop: Full hourly view, dual-pane

**Calendar View:**
- Mobile: Agenda view only (day list)
- Tablet: Week view (compressed)
- Desktop: Full week/month view

**Project Detail:**
- Mobile: Tabs at bottom, single pane
- Tablet: Tabs at top, scrollable content
- Desktop: Tabs + sidebar, multi-pane

---

## 8. Accessibility (WCAG 2.1 AA Compliance)

### 8.1 Keyboard Navigation

**All screens must support:**
- Tab: Navigate between interactive elements
- Enter: Activate buttons/links
- Arrow keys: Navigate lists/calendars
- Escape: Close modals/dialogs
- Space: Toggle checkboxes

### 8.2 Screen Reader Support

**ARIA Labels Required:**
```tsx
<Card aria-label={`Project ${title}, ${progress}% complete`}>
  <Progress
    value={progress}
    aria-label={`Progress: ${progress}%`}
    role="progressbar"
    aria-valuemin={0}
    aria-valuemax={100}
    aria-valuenow={progress}
  />
</Card>
```

### 8.3 Color Contrast

**Minimum Ratios:**
- Normal text: 4.5:1
- Large text (18pt+): 3:1
- UI components: 3:1

**Color-Blind Safe Palette:**
- Use icons + text (not color alone)
- Critical path: Red + diagonal stripes
- High priority: Orange + "!"
- Done: Green + checkmark

### 8.4 Focus Indicators

```css
*:focus-visible {
  outline: 2px solid var(--focus-color);
  outline-offset: 2px;
  border-radius: 4px;
}
```

---

## 9. Implementation Checklist

### Phase 1: Foundation (Week 1)
- [ ] Setup Next.js 14 project with shadcn/ui
- [ ] Configure Supabase client and auth
- [ ] Create database schema (projects, tasks, ideas, calendar_events)
- [ ] Implement authentication flow
- [ ] Setup Redis caching

### Phase 2: Core Screens (Week 2)
- [ ] Portfolio Dashboard (2 days)
- [ ] Decision Queue (1 day)
- [ ] Today View (2 days)
- [ ] Calendar View (2 days)
- [ ] Project Detail Page (3 days)

### Phase 3: Optimization (Week 3)
- [ ] Add database indexes
- [ ] Implement caching strategy
- [ ] Optimize slow queries (<200ms target)
- [ ] Add loading states and skeletons
- [ ] Implement error boundaries

### Phase 4: Polish (Week 4)
- [ ] Responsive design testing (mobile/tablet)
- [ ] Accessibility audit (WCAG 2.1 AA)
- [ ] Performance testing (Lighthouse >90)
- [ ] User acceptance testing
- [ ] Deploy to production

---

## 10. Related Documentation

**Implementation References:**
- [IDEAL-BEHAVIOR-REFERENCE.md](./IDEAL-BEHAVIOR-REFERENCE.md) - Section 1.13 (source of truth)
- [IDEAL-BEHAVIOR-REFERENCE.md](./IDEAL-BEHAVIOR-REFERENCE.md) - Section 1.11 (tech stack)
- [IDEAL-BEHAVIOR-REFERENCE.md](./IDEAL-BEHAVIOR-REFERENCE.md) - Section 1.12 (task data model)
- [IDEAL-BEHAVIOR-REFERENCE.md](./IDEAL-BEHAVIOR-REFERENCE.md) - Section 1.14 (planning data model)

**Component Library:**
- shadcn/ui documentation: https://ui.shadcn.com/
- React Big Calendar: https://github.com/jquense/react-big-calendar
- dnd-kit: https://dndkit.com/

**Performance:**
- Next.js optimization: https://nextjs.org/docs/app/building-your-application/optimizing
- Lighthouse CI: https://github.com/GoogleChrome/lighthouse-ci

---

## Document Status

**Version:** 1.0
**Status:** ✅ Ready for Implementation
**Last Updated:** 2026-02-06
**Next Review:** After Phase 2 completion (Week 2)

**Changelog:**
- v1.0 (2026-02-06): Initial specification based on IDEAL-BEHAVIOR-REFERENCE.md Section 1.13
