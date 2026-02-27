# Task Extraction Protocol

## Query Logic

**Filter criteria:**
```
- status = "todo" (not completed, not in-progress)
- project.status = "ACTIVE" or "IN_PROGRESS"
- (due_date <= TARGET_DATE) OR (task in week plan) OR (no due_date AND priority >= "high")
```

## Data Structure Per Task

```yaml
task_id: "task-123"
project_id: "proj-456"
project_name: "Example Project"
title: "Complete API endpoint"
priority: "high" # critical | high | medium | low
estimate_hours: 2.5
energy_level: "high" # high | medium | low
due_date: "2026-02-08"
dependencies: [] # optional
status: "todo"
```

## Search Methods

**Primary:** `npx claude-flow@v3alpha memory search -q "tasks project:{project-id} status:todo"`

**Fallback:** Read tasks from `{bmb_creations_output_folder}/life-os/projects/{project-id}/tasks/*.md`

## Week Plan Integration

**Extract from week plan:**
- Project ID, name
- Planned tasks for current week
- Tasks marked for TARGET_DATE specifically

**Fallback:** If week plan not found, fetch all active tasks matching filter criteria
