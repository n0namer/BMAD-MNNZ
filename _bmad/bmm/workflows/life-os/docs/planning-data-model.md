# Planning Data Model - Life OS

**Created:** 2026-02-06
**Purpose:** Complete specification of planning data structures, algorithms, and integration rules
**Source:** IDEAL-BEHAVIOR-REFERENCE.md Section 1.14
**Status:** ✅ PERMANENT SPECIFICATION

---

## Table of Contents

1. [Overview](#1-overview)
2. [Milestone Schema](#2-milestone-schema)
3. [Task Dependency Schema](#3-task-dependency-schema)
4. [Gantt Chart Generation Algorithm](#4-gantt-chart-generation-algorithm)
5. [Roadmap Generation](#5-roadmap-generation)
6. [Source of Truth Hierarchy](#6-source-of-truth-hierarchy)
7. [UI Integration](#7-ui-integration)
8. [Examples](#8-examples)

---

## 1. Overview

The Planning Data Model provides the foundation for:
- **Timeline Visualization**: Gantt charts and roadmaps
- **Dependency Management**: Task sequencing and blocking
- **Critical Path Analysis**: Identify bottlenecks and risks
- **Progress Tracking**: Milestone-based project monitoring

**Key Principles:**
- ✅ Data-driven (not manually drawn diagrams)
- ✅ Auto-generated from task/milestone data
- ✅ Real-time updates on changes
- ✅ Critical path automatically calculated

---

## 2. Milestone Schema

### 2.1 Purpose

Milestones define key checkpoints in project timeline. They are used for:
- High-level roadmap generation
- Progress tracking (% complete)
- Dependency validation (tasks must finish before milestone)
- Stakeholder communication (strategic view)

### 2.2 Data Model

```yaml
milestone_id: string       # Unique ID (e.g., "milestone-001-mvp")
project_id: string         # Parent project
title: string              # Milestone name (e.g., "MVP Launch")
description: string        # What defines this milestone as complete
target_date: date          # Planned completion date (ISO 8601)
actual_date: date          # Actual completion (null if not reached)
status: enum               # [not_started, in_progress, completed, missed]
progress_percent: number   # 0-100 (calculated from linked tasks)
dependencies: string[]     # Other milestone_ids that must complete first
critical_path: boolean     # Is this on critical path? (auto-calculated)
deliverables: string[]     # List of artifacts expected (files, features, etc.)
validation_criteria: string[] # How to verify milestone is truly done
created_at: timestamp
updated_at: timestamp
```

### 2.3 Field Specifications

| Field | Type | Required | Description | Validation Rules |
|-------|------|----------|-------------|------------------|
| `milestone_id` | string | ✅ YES | Unique identifier | Must be unique across project, format: `milestone-NNN-slug` |
| `project_id` | string | ✅ YES | Parent project reference | Must exist in projects table/folder |
| `title` | string | ✅ YES | Milestone name | Max 100 chars, descriptive |
| `description` | string | ❌ NO | Detailed description | Markdown supported |
| `target_date` | date | ✅ YES | Planned completion | ISO 8601, must be >= project.start_date |
| `actual_date` | date | ❌ NO | Actual completion | Set when status = completed |
| `status` | enum | ✅ YES | Current status | One of: not_started, in_progress, completed, missed |
| `progress_percent` | number | ✅ YES | 0-100 completion | Auto-calculated: done_tasks / total_tasks × 100 |
| `dependencies` | array | ❌ NO | Dependent milestones | Must be valid milestone_ids from same project |
| `critical_path` | boolean | ✅ YES | On critical path? | Auto-calculated by Gantt algorithm |
| `deliverables` | array | ❌ NO | Expected outputs | List of files, features, artifacts |
| `validation_criteria` | array | ❌ NO | Completion definition | How to verify milestone is done |
| `created_at` | timestamp | ✅ YES | Creation time | Auto-set on creation |
| `updated_at` | timestamp | ✅ YES | Last update time | Auto-set on any change |

### 2.4 Storage

**Phase 1-2 (Markdown):**
```yaml
# File: projects/project-XXX/milestones.yaml

milestones:
  - milestone_id: "milestone-001-foundation"
    project_id: "project-002"
    title: "Foundation Complete"
    description: "Resource assessment, goals.yaml, speed multipliers ready"
    target_date: "2026-01-15"
    actual_date: "2026-01-14"
    status: "completed"
    progress_percent: 100
    dependencies: []
    critical_path: true
    deliverables:
      - "goals.yaml"
      - "resource-assessment.md"
      - "speed-multipliers.md"
    validation_criteria:
      - "All foundation data collected"
      - "Speed multiplier calculated"
    created_at: "2025-12-20T10:00:00Z"
    updated_at: "2026-01-14T15:30:00Z"

  - milestone_id: "milestone-002-core-workflow"
    project_id: "project-002"
    title: "Core Workflow Complete"
    description: "L1-L2 steps implemented with BMAD integration"
    target_date: "2026-02-15"
    actual_date: null
    status: "in_progress"
    progress_percent: 67
    dependencies: ["milestone-001-foundation"]
    critical_path: true
    deliverables:
      - "L1 steps implementation"
      - "L2 steps implementation"
      - "Memory system integration"
    validation_criteria:
      - "All L1-L2 steps working"
      - "BMAD integration tested"
      - "Memory search operational"
    created_at: "2025-12-20T10:00:00Z"
    updated_at: "2026-02-06T09:00:00Z"
```

**Phase 3 (Supabase):**
```sql
CREATE TABLE milestones (
  milestone_id TEXT PRIMARY KEY,
  project_id TEXT NOT NULL REFERENCES projects(id),
  title TEXT NOT NULL,
  description TEXT,
  target_date DATE NOT NULL,
  actual_date DATE,
  status TEXT NOT NULL CHECK (status IN ('not_started', 'in_progress', 'completed', 'missed')),
  progress_percent INTEGER NOT NULL DEFAULT 0 CHECK (progress_percent >= 0 AND progress_percent <= 100),
  dependencies TEXT[] DEFAULT '{}',
  critical_path BOOLEAN NOT NULL DEFAULT false,
  deliverables TEXT[] DEFAULT '{}',
  validation_criteria TEXT[] DEFAULT '{}',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Index for quick queries
CREATE INDEX idx_milestones_project ON milestones(project_id);
CREATE INDEX idx_milestones_status ON milestones(status);
CREATE INDEX idx_milestones_target_date ON milestones(target_date);
CREATE INDEX idx_milestones_critical_path ON milestones(critical_path);
```

### 2.5 Progress Calculation

**Auto-Calculate from Linked Tasks:**
```python
def calculate_milestone_progress(milestone_id: str) -> int:
    """
    Calculate milestone progress based on linked tasks

    Returns: 0-100 integer percentage
    """
    # Get all tasks linked to this milestone
    tasks = get_tasks_for_milestone(milestone_id)

    if not tasks:
        return 0  # No tasks linked

    # Count completed tasks
    done_tasks = [t for t in tasks if t.status == 'done']

    # Calculate percentage
    progress = (len(done_tasks) / len(tasks)) * 100

    return int(progress)  # Round to integer

# Trigger: Run after any task status change
def on_task_status_change(task_id: str, new_status: str):
    # Find milestone linked to this task
    milestone = get_milestone_for_task(task_id)

    if milestone:
        # Recalculate progress
        new_progress = calculate_milestone_progress(milestone.milestone_id)

        # Update milestone
        update_milestone(milestone.milestone_id, {
            'progress_percent': new_progress,
            'updated_at': now()
        })
```

### 2.6 Status Transitions

```
not_started → in_progress → completed
            ↓                   ↓
            └─────→ missed ←────┘
```

**Transition Rules:**
- `not_started` → `in_progress`: First linked task started
- `in_progress` → `completed`: progress_percent = 100 AND target_date not exceeded
- `in_progress` → `missed`: target_date exceeded AND progress_percent < 100
- `completed` → (no transitions allowed, permanent state)

---

## 3. Task Dependency Schema

### 3.1 Purpose

Task dependencies define execution order constraints. Used for:
- Preventing tasks from starting before prerequisites done
- Critical path calculation (which tasks cannot be delayed)
- Resource allocation (which tasks can run in parallel)
- Timeline generation (Gantt chart sequencing)

### 3.2 Dependency Types

```yaml
# 1. Finish-to-Start (FS) - Most common
#    Task B cannot START until Task A FINISHES
predecessor: "task-001-setup-db"
successor: "task-002-build-api"
type: "FS"
# Interpretation: API build cannot start until DB setup finishes

# 2. Start-to-Start (SS) - Parallel dependency
#    Task B cannot START until Task A STARTS
predecessor: "task-003-design-ui"
successor: "task-004-implement-ui"
type: "SS"
# Interpretation: UI implementation can start as soon as design starts (parallel work)

# 3. Finish-to-Finish (FF) - Synchronization
#    Task B cannot FINISH until Task A FINISHES
predecessor: "task-005-backend-tests"
successor: "task-006-integration-tests"
type: "FF"
# Interpretation: Integration tests must wait for backend tests to finish before they can finish

# 4. Start-to-Finish (SF) - Rare
#    Task B cannot FINISH until Task A STARTS
predecessor: "task-007-deploy-prod"
successor: "task-008-shutdown-staging"
type: "SF"
# Interpretation: Staging shutdown can't finish until prod deploy starts
```

### 3.3 Data Model

```yaml
dependency_id: string      # Unique ID (e.g., "dep-001-task-a-to-b")
project_id: string         # Parent project
predecessor_id: string     # Task that must happen first
successor_id: string       # Task that depends on predecessor
dependency_type: enum      # [FS, SS, FF, SF] (default: FS)
lag_days: number           # Additional delay (e.g., 2 = wait 2 days after predecessor)
lead_days: number          # Allow early start (e.g., -1 = start 1 day before)
is_hard: boolean           # Hard constraint (cannot violate) vs soft (prefer but not strict)
created_at: timestamp
```

### 3.4 Field Specifications

| Field | Type | Required | Description | Validation Rules |
|-------|------|----------|-------------|------------------|
| `dependency_id` | string | ✅ YES | Unique identifier | Format: `dep-NNN-predecessor-to-successor` |
| `project_id` | string | ✅ YES | Parent project | Must match predecessor and successor project |
| `predecessor_id` | string | ✅ YES | Task that comes first | Must be valid task_id |
| `successor_id` | string | ✅ YES | Task that depends | Must be valid task_id, cannot equal predecessor |
| `dependency_type` | enum | ✅ YES | Type of dependency | One of: FS, SS, FF, SF (default: FS) |
| `lag_days` | number | ❌ NO | Delay after predecessor | >= 0, mutually exclusive with lead_days |
| `lead_days` | number | ❌ NO | Early start allowance | <= 0, mutually exclusive with lag_days |
| `is_hard` | boolean | ✅ YES | Hard constraint? | Default: true (cannot violate) |
| `created_at` | timestamp | ✅ YES | Creation time | Auto-set on creation |

### 3.5 Validation Rules

**Critical Validations (MUST enforce):**

1. **No Circular Dependencies:**
```python
def detect_circular_dependencies(project_id: str) -> List[str]:
    """
    Use DFS to detect cycles in dependency graph

    Returns: List of task_ids in circular path (empty if no cycle)
    """
    graph = build_dependency_graph(project_id)
    visited = set()
    stack = set()
    cycle_path = []

    def dfs(node):
        if node in stack:
            # Cycle detected
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                cycle_path.append(node)
                return True

        stack.remove(node)
        return False

    for task in graph:
        if dfs(task):
            return cycle_path[::-1]  # Reverse to show cycle order

    return []  # No cycle

# Error handling
cycle = detect_circular_dependencies("project-002")
if cycle:
    raise ValidationError(f"Circular dependency detected: {' → '.join(cycle)}")
```

2. **Same Project Constraint:**
```python
def validate_dependency(dependency):
    predecessor_project = get_task(dependency.predecessor_id).project_id
    successor_project = get_task(dependency.successor_id).project_id

    if predecessor_project != successor_project:
        raise ValidationError(
            f"Dependency spans multiple projects: "
            f"predecessor in {predecessor_project}, successor in {successor_project}"
        )
```

3. **Mutually Exclusive Lag/Lead:**
```python
def validate_lag_lead(dependency):
    if dependency.lag_days and dependency.lead_days:
        raise ValidationError(
            f"Cannot specify both lag ({dependency.lag_days}) "
            f"and lead ({dependency.lead_days}). Use one or neither."
        )
```

### 3.6 Storage

**Phase 1-2 (Markdown):**
```yaml
# File: projects/project-XXX/dependencies.yaml

dependencies:
  - dependency_id: "dep-001-db-to-api"
    project_id: "project-002"
    predecessor_id: "task-001-setup-db"
    successor_id: "task-002-build-api"
    dependency_type: "FS"
    lag_days: 0
    lead_days: null
    is_hard: true
    created_at: "2026-01-20T10:00:00Z"

  - dependency_id: "dep-002-design-to-ui"
    project_id: "project-002"
    predecessor_id: "task-003-design-ui"
    successor_id: "task-004-implement-ui"
    dependency_type: "SS"
    lag_days: 1
    lead_days: null
    is_hard: false
    created_at: "2026-01-20T10:05:00Z"
```

**Phase 3 (Supabase):**
```sql
CREATE TABLE task_dependencies (
  dependency_id TEXT PRIMARY KEY,
  project_id TEXT NOT NULL REFERENCES projects(id),
  predecessor_id TEXT NOT NULL REFERENCES tasks(task_id),
  successor_id TEXT NOT NULL REFERENCES tasks(task_id),
  dependency_type TEXT NOT NULL CHECK (dependency_type IN ('FS', 'SS', 'FF', 'SF')),
  lag_days INTEGER DEFAULT 0 CHECK (lag_days >= 0),
  lead_days INTEGER DEFAULT 0 CHECK (lead_days <= 0),
  is_hard BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  -- Constraints
  CONSTRAINT different_tasks CHECK (predecessor_id != successor_id),
  CONSTRAINT lag_or_lead CHECK (
    (lag_days = 0) OR (lead_days = 0)  -- Cannot have both
  )
);

-- Indexes
CREATE INDEX idx_dependencies_project ON task_dependencies(project_id);
CREATE INDEX idx_dependencies_predecessor ON task_dependencies(predecessor_id);
CREATE INDEX idx_dependencies_successor ON task_dependencies(successor_id);
```

---

## 4. Gantt Chart Generation Algorithm

### 4.1 Purpose

Generate task timeline with critical path analysis for project planning and tracking.

**Outputs:**
- Earliest/latest start and finish times for each task
- Total slack (float) for each task
- Critical path (sequence of zero-slack tasks)
- Gantt bar positions for UI rendering

### 4.2 Input Data

```python
@dataclass
class GanttInput:
    project_id: str
    start_date: date               # Project start date
    due_date: date                 # Project deadline
    tasks: List[Task]              # All tasks with estimate_hours
    dependencies: List[Dependency] # All task dependencies
    milestones: List[Milestone]    # Milestone checkpoints
    team_capacity: float           # Hours per day (e.g., 6.0 = 6h/day)
```

### 4.3 Algorithm Steps

#### Step 1: Build Dependency Graph

```python
def build_dependency_graph(dependencies: List[Dependency]) -> Dict[str, List[Edge]]:
    """
    Create adjacency list representation of task dependencies

    Returns: {task_id: [Edge(successor_id, type, lag)]}
    """
    graph = defaultdict(list)

    for dep in dependencies:
        edge = Edge(
            target=dep.successor_id,
            type=dep.dependency_type,
            lag=dep.lag_days,
            lead=dep.lead_days
        )
        graph[dep.predecessor_id].append(edge)

    # Detect cycles
    cycle = detect_circular_dependencies_dfs(graph)
    if cycle:
        raise ValueError(f"Circular dependency detected: {cycle}")

    return graph
```

#### Step 2: Topological Sort

```python
def topological_sort(tasks: List[Task], graph: Dict) -> List[Task]:
    """
    Order tasks so dependencies are respected

    Uses Kahn's algorithm (BFS-based)
    """
    # Calculate in-degrees
    in_degree = {task.task_id: 0 for task in tasks}
    for task_id, edges in graph.items():
        for edge in edges:
            in_degree[edge.target] += 1

    # Queue of tasks with no dependencies
    queue = [task for task in tasks if in_degree[task.task_id] == 0]
    sorted_tasks = []

    while queue:
        task = queue.pop(0)
        sorted_tasks.append(task)

        # Reduce in-degree of successors
        for edge in graph[task.task_id]:
            successor_id = edge.target
            in_degree[successor_id] -= 1

            if in_degree[successor_id] == 0:
                queue.append(get_task(successor_id))

    if len(sorted_tasks) != len(tasks):
        raise ValueError("Cycle detected (topological sort incomplete)")

    return sorted_tasks
```

#### Step 3: Forward Pass (Earliest Start/Finish)

```python
def forward_pass(
    tasks: List[Task],
    graph: Dict,
    start_date: date,
    team_capacity: float
) -> Dict[str, TaskTiming]:
    """
    Calculate earliest start and finish times

    Formula:
    - ES = MAX(predecessor.EF + lag) OR start_date (if no predecessors)
    - EF = ES + (estimate_hours / team_capacity)
    """
    timing = {}

    for task in tasks:  # Must be in topological order
        # Find earliest start based on predecessors
        earliest_start = start_date

        for dep in get_dependencies_to(task.task_id):
            pred_timing = timing[dep.predecessor_id]

            if dep.dependency_type == 'FS':
                # Finish-to-Start: wait for predecessor to finish
                candidate = pred_timing.earliest_finish + timedelta(days=dep.lag_days)
            elif dep.dependency_type == 'SS':
                # Start-to-Start: wait for predecessor to start
                candidate = pred_timing.earliest_start + timedelta(days=dep.lag_days)
            elif dep.dependency_type == 'FF':
                # Finish-to-Finish: handled in backward pass
                continue
            elif dep.dependency_type == 'SF':
                # Start-to-Finish: rare, complex logic
                candidate = pred_timing.earliest_start + timedelta(days=dep.lag_days)

            earliest_start = max(earliest_start, candidate)

        # Calculate finish
        duration_days = task.estimate_hours / team_capacity
        earliest_finish = earliest_start + timedelta(days=duration_days)

        timing[task.task_id] = TaskTiming(
            earliest_start=earliest_start,
            earliest_finish=earliest_finish
        )

    return timing
```

#### Step 4: Backward Pass (Latest Start/Finish)

```python
def backward_pass(
    tasks: List[Task],
    graph: Dict,
    due_date: date,
    team_capacity: float,
    forward_timing: Dict[str, TaskTiming]
) -> Dict[str, TaskTiming]:
    """
    Calculate latest start and finish times (working backwards from deadline)

    Formula:
    - LF = MIN(successor.LS - lag) OR due_date (if no successors)
    - LS = LF - (estimate_hours / team_capacity)
    """
    timing = copy.deepcopy(forward_timing)

    # Reverse topological order
    for task in reversed(tasks):
        # Find latest finish based on successors
        latest_finish = due_date

        for dep in get_dependencies_from(task.task_id):
            succ_timing = timing[dep.successor_id]

            if dep.dependency_type == 'FS':
                # Finish-to-Start: must finish before successor starts
                candidate = succ_timing.latest_start - timedelta(days=dep.lag_days)
            elif dep.dependency_type == 'SS':
                # Start-to-Start: complex, use earliest
                continue
            elif dep.dependency_type == 'FF':
                # Finish-to-Finish: must finish when successor finishes
                candidate = succ_timing.latest_finish - timedelta(days=dep.lag_days)
            elif dep.dependency_type == 'SF':
                # Start-to-Finish: rare
                candidate = succ_timing.latest_finish - timedelta(days=dep.lag_days)

            latest_finish = min(latest_finish, candidate)

        # Calculate start
        duration_days = task.estimate_hours / team_capacity
        latest_start = latest_finish - timedelta(days=duration_days)

        timing[task.task_id].latest_start = latest_start
        timing[task.task_id].latest_finish = latest_finish

    return timing
```

#### Step 5: Calculate Slack (Float)

```python
def calculate_slack(timing: Dict[str, TaskTiming]) -> Dict[str, TaskSlack]:
    """
    Calculate total slack and free slack

    Total Slack: How much task can be delayed without delaying project
    Free Slack: How much task can be delayed without delaying successors
    """
    slack = {}

    for task_id, t in timing.items():
        # Total slack
        total_slack_days = (t.latest_start - t.earliest_start).days

        # Free slack (requires successor analysis)
        free_slack_days = total_slack_days  # Default

        for dep in get_dependencies_from(task_id):
            succ_timing = timing[dep.successor_id]

            if dep.dependency_type == 'FS':
                gap = (succ_timing.earliest_start - t.earliest_finish).days
                free_slack_days = min(free_slack_days, gap - dep.lag_days)

        slack[task_id] = TaskSlack(
            total_slack_days=total_slack_days,
            free_slack_days=free_slack_days
        )

    return slack
```

#### Step 6: Identify Critical Path

```python
def identify_critical_path(
    tasks: List[Task],
    timing: Dict[str, TaskTiming],
    slack: Dict[str, TaskSlack]
) -> List[str]:
    """
    Critical tasks = tasks where total_slack = 0
    Critical path = longest sequence from start to end
    """
    # Find all critical tasks (slack = 0)
    critical_tasks = [
        task.task_id for task in tasks
        if slack[task.task_id].total_slack_days == 0
    ]

    # Build critical path sequence (DFS from start to end)
    graph = build_dependency_graph_filtered(critical_tasks)

    def dfs_longest_path(node, visited, path):
        visited.add(node)
        path.append(node)

        max_path = path.copy()

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                candidate = dfs_longest_path(neighbor, visited, path)
                if len(candidate) > len(max_path):
                    max_path = candidate

        path.pop()
        visited.remove(node)
        return max_path

    # Find start nodes (no predecessors)
    start_nodes = [t for t in critical_tasks if not get_dependencies_to(t)]

    longest = []
    for start in start_nodes:
        path = dfs_longest_path(start, set(), [])
        if len(path) > len(longest):
            longest = path

    return longest
```

### 4.4 Output Format (JSON)

```json
{
  "project_id": "project-002",
  "start_date": "2026-02-01",
  "end_date": "2026-03-15",
  "critical_path_duration_days": 32,
  "total_slack_days": 5,
  "tasks": [
    {
      "task_id": "task-001-setup-db",
      "title": "Setup database",
      "earliest_start": "2026-02-01",
      "earliest_finish": "2026-02-03",
      "latest_start": "2026-02-01",
      "latest_finish": "2026-02-03",
      "total_slack_days": 0,
      "free_slack_days": 0,
      "is_critical": true,
      "dependencies": [],
      "bar_color": "red",
      "bar_start_x": 0,
      "bar_width": 2
    },
    {
      "task_id": "task-002-build-api",
      "title": "Build API",
      "earliest_start": "2026-02-03",
      "earliest_finish": "2026-02-10",
      "latest_start": "2026-02-05",
      "latest_finish": "2026-02-12",
      "total_slack_days": 2,
      "free_slack_days": 1,
      "is_critical": false,
      "dependencies": ["task-001-setup-db"],
      "bar_color": "blue",
      "bar_start_x": 2,
      "bar_width": 7
    }
  ],
  "critical_path": [
    "task-001-setup-db",
    "task-003-implement-core",
    "task-007-integration-tests",
    "task-012-deployment"
  ],
  "milestones": [
    {
      "milestone_id": "milestone-001-mvp",
      "title": "MVP Launch",
      "target_date": "2026-03-15",
      "position_x": 42,
      "is_on_critical_path": true
    }
  ]
}
```

### 4.5 UI Rendering

```javascript
// Convert JSON to Gantt chart visual
function renderGanttChart(data) {
  const canvas = document.getElementById('gantt-canvas');
  const ctx = canvas.getContext('2d');

  // Draw timeline axis
  drawTimelineAxis(ctx, data.start_date, data.end_date);

  // Draw task bars
  data.tasks.forEach((task, index) => {
    const y = index * 40 + 50;  // Task row position
    const x = calculateXPosition(task.earliest_start, data.start_date);
    const width = calculateWidth(task.earliest_start, task.earliest_finish);

    // Draw bar
    ctx.fillStyle = task.bar_color;
    ctx.fillRect(x, y, width, 30);

    // Draw task label
    ctx.fillStyle = 'black';
    ctx.fillText(task.title, x + 5, y + 20);

    // Draw slack indicator (if > 0)
    if (task.total_slack_days > 0) {
      const slackWidth = calculateWidth(
        task.earliest_finish,
        task.latest_finish
      );
      ctx.fillStyle = 'rgba(255, 255, 0, 0.3)';
      ctx.fillRect(x + width, y, slackWidth, 30);
    }
  });

  // Draw dependency arrows
  data.tasks.forEach(task => {
    task.dependencies.forEach(depId => {
      drawArrow(ctx, depId, task.task_id);
    });
  });

  // Draw milestones
  data.milestones.forEach(milestone => {
    const x = calculateXPosition(milestone.target_date, data.start_date);
    drawDiamond(ctx, x, 20, milestone.title);
  });

  // Highlight critical path
  drawCriticalPath(ctx, data.critical_path);
}
```

---

## 5. Roadmap Generation

### 5.1 Purpose

High-level timeline showing milestones for stakeholder communication. Less granular than Gantt (milestone-based, not task-based).

**Use Cases:**
- Executive/client presentations
- Portfolio overview (multiple projects)
- Strategic planning sessions
- Progress reporting

### 5.2 Input Data

```python
@dataclass
class RoadmapInput:
    milestones: List[Milestone]  # All milestones across projects
    phases: List[Phase]          # Optional project phases
    projects: List[Project]      # For multi-project roadmaps
```

### 5.3 Generation Rules

#### Rule 1: Group Milestones by Phase

```python
def group_by_phase(milestones: List[Milestone], phases: List[Phase]) -> Dict:
    """
    If phases defined, group milestones by phase
    Otherwise, show flat timeline
    """
    if not phases:
        return {'default': milestones}

    grouped = {phase.phase_id: [] for phase in phases}

    for milestone in milestones:
        phase = find_phase_for_milestone(milestone, phases)
        grouped[phase.phase_id].append(milestone)

    return grouped
```

#### Rule 2: Place Milestones on Timeline

```python
def generate_roadmap(
    milestones: List[Milestone],
    start_date: date,
    end_date: date
) -> RoadmapData:
    """
    Generate roadmap visualization data
    """
    # Calculate timeline scale (months or quarters)
    duration_days = (end_date - start_date).days

    if duration_days <= 90:
        scale = 'weeks'
    elif duration_days <= 365:
        scale = 'months'
    else:
        scale = 'quarters'

    # Position milestones on timeline
    positioned = []
    for milestone in milestones:
        x_position = calculate_position(
            milestone.target_date,
            start_date,
            end_date,
            scale
        )

        positioned.append({
            'milestone': milestone,
            'x_position': x_position,
            'status_color': get_status_color(milestone.status)
        })

    return RoadmapData(
        scale=scale,
        milestones=positioned,
        dependencies=build_milestone_dependencies(milestones)
    )
```

#### Rule 3: Show Dependencies Between Milestones

```python
def build_milestone_dependencies(milestones: List[Milestone]) -> List[Arrow]:
    """
    Generate arrows connecting dependent milestones
    """
    arrows = []

    for milestone in milestones:
        for dep_id in milestone.dependencies:
            predecessor = find_milestone(dep_id)

            arrows.append(Arrow(
                from_milestone=dep_id,
                to_milestone=milestone.milestone_id,
                style='dotted',  # Dotted for milestone dependencies
                color=get_dependency_color(predecessor, milestone)
            ))

    return arrows
```

#### Rule 4: Highlight Current Period

```python
def add_current_period_marker(roadmap: RoadmapData) -> RoadmapData:
    """
    Add "Today" marker and shade past/present/future
    """
    today = date.today()

    # Calculate x position for today
    today_x = calculate_position(
        today,
        roadmap.start_date,
        roadmap.end_date,
        roadmap.scale
    )

    # Add marker
    roadmap.markers.append(TodayMarker(
        x_position=today_x,
        label='Today',
        style='vertical-line'
    ))

    # Add shading zones
    roadmap.zones = [
        Zone(start=0, end=today_x, color='gray', opacity=0.1, label='Past'),
        Zone(start=today_x, end=today_x+10, color='blue', opacity=0.05, label='Present'),
        Zone(start=today_x+10, end=roadmap.width, color='white', opacity=0, label='Future')
    ]

    return roadmap
```

#### Rule 5: Add Progress Indicators

```python
def add_progress_indicators(roadmap: RoadmapData) -> RoadmapData:
    """
    Show completion percentage and status for each milestone
    """
    for milestone in roadmap.milestones:
        # Progress badge
        milestone.progress_badge = ProgressBadge(
            text=f"{milestone.milestone.progress_percent}%",
            color=get_progress_color(milestone.milestone.progress_percent)
        )

        # Status indicator
        status = determine_milestone_status(milestone.milestone)
        milestone.status_indicator = StatusIndicator(
            icon=status.icon,
            color=status.color,
            label=status.label
        )

    return roadmap

def determine_milestone_status(milestone: Milestone) -> Status:
    """
    Determine if milestone is on track, at risk, or delayed
    """
    today = date.today()

    if milestone.status == 'completed':
        return Status(icon='✅', color='green', label='Done')

    days_to_target = (milestone.target_date - today).days

    if days_to_target < 0:
        # Overdue
        return Status(icon='⚠️', color='red', label='Delayed')

    # Calculate expected progress
    project_start = get_project(milestone.project_id).start_date
    total_duration = (milestone.target_date - project_start).days
    elapsed = (today - project_start).days
    expected_progress = (elapsed / total_duration) * 100

    actual_progress = milestone.progress_percent

    if actual_progress >= expected_progress - 10:
        return Status(icon='⏳', color='green', label='On Track')
    elif actual_progress >= expected_progress - 25:
        return Status(icon='⚠️', color='yellow', label='At Risk')
    else:
        return Status(icon='🔴', color='red', label='Falling Behind')
```

### 5.4 Output Format (Markdown)

```markdown
# Project Roadmap: Life OS v3.0

**Timeline:** Jan 2026 - Mar 2026
**Critical Path Duration:** 32 days
**Status:** ⏳ In Progress (67% complete)

---

## Q1 2026

### Phase 1: Foundation (✅ Completed)
───────────────────────────────────────────────────────────────
◆ **Jan 15, 2026**: Foundation Complete
   **Status:** ✅ Done (100%)
   **Deliverables:**
   - ✅ goals.yaml
   - ✅ resource-assessment.md
   - ✅ speed-multipliers.md
   **Validation:** All foundation data collected, speed multiplier calculated

---

### Phase 2: Core Implementation (⏳ In Progress)
───────────────────────────────────────────────────────────────
◆ **Feb 15, 2026**: Core Workflow Complete
   **Status:** ⏳ On Track (67%)
   **Deliverables:**
   - ✅ L1 steps implementation
   - ⏳ L2 steps implementation (80% done)
   - ⏳ Memory system integration (testing)
   **Dependencies:** Foundation Complete ✅
   **Validation:** All L1-L2 steps working, BMAD integration tested

─────────────────────────────── TODAY ───────────────────────────

◆ **Mar 15, 2026**: MVP Launch
   **Status:** ⏸️ Not Started (0%)
   **Deliverables:**
   - ⏸️ CLI + Web UI
   - ⏸️ Documentation
   - ⏸️ First user onboarding
   **Dependencies:** Core Workflow Complete ⏳
   **Risk:** Timeline tight, Core must finish by Feb 20 to be on track

---

## Legend
- ✅ Done
- ⏳ In Progress (On Track)
- ⚠️ At Risk (Behind Schedule)
- ⏸️ Not Started
- 🔴 Critical Path Milestone
```

### 5.5 Output Format (JSON for UI)

```json
{
  "project_id": "project-002",
  "title": "Life OS v3.0",
  "timeline": {
    "start_date": "2026-01-01",
    "end_date": "2026-03-31",
    "scale": "months",
    "today_position": 45
  },
  "phases": [
    {
      "phase_id": "phase-001-foundation",
      "title": "Foundation",
      "status": "completed",
      "progress_percent": 100,
      "milestones": [
        {
          "milestone_id": "milestone-001-foundation",
          "title": "Foundation Complete",
          "target_date": "2026-01-15",
          "actual_date": "2026-01-14",
          "status": "completed",
          "progress_percent": 100,
          "x_position": 15,
          "status_indicator": {
            "icon": "✅",
            "color": "green",
            "label": "Done"
          },
          "deliverables": [
            {"name": "goals.yaml", "status": "done"},
            {"name": "resource-assessment.md", "status": "done"},
            {"name": "speed-multipliers.md", "status": "done"}
          ]
        }
      ]
    },
    {
      "phase_id": "phase-002-core",
      "title": "Core Implementation",
      "status": "in_progress",
      "progress_percent": 67,
      "milestones": [
        {
          "milestone_id": "milestone-002-core-workflow",
          "title": "Core Workflow Complete",
          "target_date": "2026-02-15",
          "actual_date": null,
          "status": "in_progress",
          "progress_percent": 67,
          "x_position": 45,
          "status_indicator": {
            "icon": "⏳",
            "color": "green",
            "label": "On Track"
          },
          "dependencies": ["milestone-001-foundation"]
        }
      ]
    }
  ],
  "dependencies": [
    {
      "from": "milestone-001-foundation",
      "to": "milestone-002-core-workflow",
      "style": "dotted",
      "color": "gray"
    }
  ],
  "markers": [
    {
      "type": "today",
      "x_position": 37,
      "label": "Today"
    }
  ]
}
```

---

## 6. Source of Truth Hierarchy

### 6.1 For Gantt Chart

**Primary Source:** Task dependencies (task-level detail)

- Task estimates (`task.estimate_hours`)
- Task dependencies (`task_dependencies` table/file)
- Dependency types (FS/SS/FF/SF)
- Lag/lead times

**Secondary Source:** Milestone target dates (high-level checkpoints)

- Milestone deadlines constrain task schedules
- If task.earliest_finish > milestone.target_date → flag risk

**Constraints:**

- `project.start_date`: Earliest any task can start
- `project.due_date`: Latest any task can finish
- `team_capacity`: Hours per day available

**Update Triggers:**

```python
# Trigger 1: Task dependency added/removed
def on_dependency_change(project_id: str):
    regenerate_gantt_chart(project_id)
    recalculate_critical_path(project_id)
    check_milestone_feasibility(project_id)

# Trigger 2: Task estimate changed
def on_task_estimate_change(task_id: str):
    project_id = get_task(task_id).project_id
    regenerate_gantt_chart(project_id)
    update_milestone_timeline(project_id)

# Trigger 3: Task completed
def on_task_complete(task_id: str):
    project_id = get_task(task_id).project_id
    update_milestone_progress(project_id)
    recalculate_remaining_timeline(project_id)
```

### 6.2 For Roadmap

**Primary Source:** Milestone target dates (strategic view)

- `milestone.target_date`: When milestone planned
- `milestone.status`: Current state
- `milestone.progress_percent`: Completion tracking

**Secondary Source:** Milestone dependencies (sequencing)

- `milestone.dependencies`: Which milestones must finish first
- Validate target dates respect dependencies

**Context:** Project phases (if applicable)

- Group milestones by phase for visual clarity
- Phases are optional (not required for roadmap)

**Update Triggers:**

```python
# Trigger 1: Milestone date changed
def on_milestone_date_change(milestone_id: str):
    validate_milestone_dependencies(milestone_id)
    regenerate_roadmap(get_project_id(milestone_id))
    notify_stakeholders_if_delay(milestone_id)

# Trigger 2: Milestone completed
def on_milestone_complete(milestone_id: str):
    update_milestone_status(milestone_id, 'completed')
    regenerate_roadmap(get_project_id(milestone_id))
    check_dependent_milestones(milestone_id)

# Trigger 3: Milestone progress updated
def on_milestone_progress_change(milestone_id: str):
    regenerate_roadmap(get_project_id(milestone_id))
    update_status_indicators(milestone_id)
```

### 6.3 Validation Rules

**Milestone Feasibility:**
```python
def validate_milestone_feasibility(milestone: Milestone) -> List[str]:
    """
    Check if milestone target date is achievable given linked tasks
    """
    errors = []

    # Get all tasks linked to milestone
    tasks = get_tasks_for_milestone(milestone.milestone_id)

    # Run Gantt algorithm
    gantt = generate_gantt_chart(tasks)

    # Find latest task finish
    latest_finish = max(t.earliest_finish for t in gantt.tasks)

    # Compare to milestone target
    if latest_finish > milestone.target_date:
        days_over = (latest_finish - milestone.target_date).days
        errors.append(
            f"Milestone '{milestone.title}' target date {milestone.target_date} "
            f"is {days_over} days before latest task finishes ({latest_finish}). "
            f"Adjust milestone date or compress task timeline."
        )

    return errors
```

**Project Deadline Feasibility:**
```python
def validate_project_deadline(project: Project) -> List[str]:
    """
    Check if project due date is achievable given critical path
    """
    errors = []

    # Generate Gantt chart
    gantt = generate_gantt_chart(project.project_id)

    # Check critical path duration
    critical_path_days = gantt.critical_path_duration_days
    project_duration = (project.due_date - project.start_date).days

    if critical_path_days > project_duration:
        shortage = critical_path_days - project_duration
        errors.append(
            f"Project '{project.title}' critical path ({critical_path_days} days) "
            f"exceeds available timeline ({project_duration} days) by {shortage} days. "
            f"Options: (1) Extend deadline, (2) Add resources, (3) Reduce scope."
        )

    return errors
```

### 6.4 Error Handling

**Timeline at Risk (Critical Path Exceeds Deadline):**

```python
def handle_timeline_risk(project: Project, gantt: GanttData):
    """
    Suggest compression strategies when timeline at risk
    """
    shortage_days = gantt.critical_path_duration_days - \
                   (project.due_date - project.start_date).days

    if shortage_days > 0:
        # Calculate suggestions
        suggestions = []

        # Option 1: Add resources (increase team capacity)
        current_capacity = project.team_capacity
        required_capacity = current_capacity * (1 + shortage_days / gantt.critical_path_duration_days)
        suggestions.append(
            f"Increase team capacity from {current_capacity}h/day to {required_capacity:.1f}h/day "
            f"(add {required_capacity - current_capacity:.1f} hours/day)"
        )

        # Option 2: Reduce scope (remove non-critical tasks)
        non_critical_tasks = [t for t in gantt.tasks if not t.is_critical]
        hours_savable = sum(t.estimate_hours for t in non_critical_tasks)
        suggestions.append(
            f"Remove or defer non-critical tasks ({len(non_critical_tasks)} tasks, {hours_savable}h total)"
        )

        # Option 3: Extend deadline
        new_due_date = project.start_date + timedelta(days=gantt.critical_path_duration_days)
        suggestions.append(
            f"Extend deadline from {project.due_date} to {new_due_date} (+{shortage_days} days)"
        )

        # Notify
        notify_user({
            'type': 'timeline_risk',
            'project_id': project.project_id,
            'message': f"⚠️ Project timeline at risk: {shortage_days} days short",
            'suggestions': suggestions
        })
```

---

## 7. UI Integration

### 7.1 Project Detail Page → Timeline Tab

**Display:**
- Gantt chart (generated from Section 4 algorithm)
- Critical path highlighted in red
- Milestone markers on timeline
- Drag-and-drop task rescheduling

**Features:**
```javascript
// Gantt chart component
<GanttChart
  projectId="project-002"
  tasks={ganttData.tasks}
  dependencies={ganttData.dependencies}
  criticalPath={ganttData.critical_path}
  milestones={ganttData.milestones}
  onTaskDrag={(taskId, newStartDate) => {
    // Update task start date
    updateTask(taskId, { planned_start: newStartDate });

    // Regenerate Gantt (dependencies may shift)
    regenerateGantt(projectId);
  }}
  onDependencyAdd={(predecessorId, successorId) => {
    createDependency({
      predecessor_id: predecessorId,
      successor_id: successorId,
      dependency_type: 'FS'
    });
  }}
/>
```

### 7.2 Portfolio Dashboard → Roadmap View

**Display:**
- Roadmap across all active projects (Section 5 algorithm)
- Filter by project, phase, or status
- Cross-project dependencies (if any)

**Features:**
```javascript
// Roadmap component
<Roadmap
  projects={activeProjects}
  milestones={allMilestones}
  startDate={portfolioStartDate}
  endDate={portfolioEndDate}
  scale="months"
  onMilestoneClick={(milestoneId) => {
    navigateToProject(milestone.project_id);
  }}
  filters={{
    projects: selectedProjects,
    phases: selectedPhases,
    status: selectedStatuses
  }}
/>
```

### 7.3 Today View → Dependency Warnings

**Display:**
- If task has unmet dependencies → Show "⚠️ Blocked by: [task-xxx]"
- Suggest alternative tasks from same project (no blockers)

**Logic:**
```python
def get_today_tasks_with_warnings(user_id: str) -> List[TaskWithWarnings]:
    """
    Fetch today's tasks and annotate with dependency warnings
    """
    tasks = get_today_tasks(user_id)

    tasks_with_warnings = []
    for task in tasks:
        warnings = []

        # Check dependencies
        deps = get_dependencies_to(task.task_id)
        unmet = [d for d in deps if get_task(d.predecessor_id).status != 'done']

        if unmet:
            blocker_titles = [get_task(d.predecessor_id).title for d in unmet]
            warnings.append({
                'type': 'blocked',
                'message': f"⚠️ Blocked by: {', '.join(blocker_titles)}",
                'action': 'suggest_alternatives'
            })

        tasks_with_warnings.append(TaskWithWarnings(
            task=task,
            warnings=warnings
        ))

    return tasks_with_warnings
```

---

## 8. Examples

### 8.1 Example Project: "Life OS v3.0 Implementation"

#### Milestones

```yaml
milestones:
  - milestone_id: "milestone-001-foundation"
    project_id: "project-002"
    title: "Foundation Complete"
    target_date: "2026-01-15"
    status: "completed"
    progress_percent: 100
    critical_path: true

  - milestone_id: "milestone-002-core-workflow"
    project_id: "project-002"
    title: "Core Workflow Complete"
    target_date: "2026-02-15"
    status: "in_progress"
    progress_percent: 67
    dependencies: ["milestone-001-foundation"]
    critical_path: true

  - milestone_id: "milestone-003-mvp-launch"
    project_id: "project-002"
    title: "MVP Launch"
    target_date: "2026-03-15"
    status: "not_started"
    progress_percent: 0
    dependencies: ["milestone-002-core-workflow"]
    critical_path: true
```

#### Task Dependencies

```yaml
dependencies:
  - dependency_id: "dep-001-db-to-api"
    predecessor_id: "task-001-setup-db"
    successor_id: "task-002-build-api"
    dependency_type: "FS"
    lag_days: 0
    is_hard: true

  - dependency_id: "dep-002-api-to-ui"
    predecessor_id: "task-002-build-api"
    successor_id: "task-003-build-ui"
    dependency_type: "FS"
    lag_days: 1  # Wait 1 day after API done to start UI
    is_hard: true

  - dependency_id: "dep-003-ui-to-tests"
    predecessor_id: "task-003-build-ui"
    successor_id: "task-004-write-tests"
    dependency_type: "SS"  # Tests can start as soon as UI starts
    lag_days: 0
    is_hard: false  # Soft dependency
```

#### Generated Gantt Chart

```
Project: Life OS v3.0 Implementation
Timeline: Feb 1 - Mar 15, 2026 (43 days)
Critical Path Duration: 32 days
Total Slack: 11 days

Task Timeline:
─────────────────────────────────────────────────────────────────
                  Feb               Mar
Task              1  5  10  15  20  25  1  5  10  15
─────────────────────────────────────────────────────────────────
Setup DB          ██                                        [CRITICAL]
Build API            ████████                               [CRITICAL]
Build UI                     ██████████                     [CRITICAL]
Write Tests                  ░░░░░░░░░░██                  (2d slack)
Integration Tests                      ██████               [CRITICAL]
Deploy                                       ██             [CRITICAL]
─────────────────────────────────────────────────────────────────
Milestones:
               ◆ Foundation (Jan 15) ✅
                             ◆ Core Workflow (Feb 15) ⏳
                                                ◆ MVP (Mar 15) ⏸️

Legend: ██ Critical Path | ░░ Slack Available
```

### 8.2 Example Roadmap

```markdown
# Portfolio Roadmap: Q1 2026

**Projects:** 3 active
**Timeline:** Jan - Mar 2026
**Overall Status:** ⏳ On Track

---

## Life OS v3.0 Implementation
───────────────────────────────────────────────────────────────
◆ Jan 15: Foundation ✅ (100%)
◆ Feb 15: Core Workflow ⏳ (67%)  ← Critical Path
◆ Mar 15: MVP Launch ⏸️ (0%)

## Personal Finance Dashboard
───────────────────────────────────────────────────────────────
◆ Jan 31: Data Model ✅ (100%)
◆ Feb 28: UI Complete ⚠️ (45%)  ← At Risk (expected 60%)
◆ Mar 31: Beta Launch ⏸️ (0%)

## Health Tracker App
───────────────────────────────────────────────────────────────
◆ Feb 15: Design Complete ✅ (100%)
◆ Mar 15: MVP Ready ⏳ (80%)
◆ Apr 15: Public Launch ⏸️ (0%)

────────────────── TODAY ──────────────────
```

---

## Document Status

**Version:** 1.0
**Last Updated:** 2026-02-06
**Status:** ✅ PERMANENT SPECIFICATION
**Source:** IDEAL-BEHAVIOR-REFERENCE.md Section 1.14

**Next Review:** When major architectural changes proposed

---

## Related Documentation

- [IDEAL-BEHAVIOR-REFERENCE.md](./IDEAL-BEHAVIOR-REFERENCE.md) - Complete system behavior specification
- [Task Layer Specification](./task-layer-spec.md) - Task data model and rules
- [UI Minimum Screens](./ui-screens-spec.md) - UI requirements and queries
- [Data Model Overview](./data-model-overview.md) - Complete data architecture

---

**End of Document**
