---
name: 'step-09-task-layer'
description: 'Break down approved project into executable tasks'
nextStepFile: null
---

# Step 09: Task Layer Implementation

**Purpose**: Break down approved project into executable tasks

**Prerequisites**:
- ✅ Step 08 (Deep Planning) completed
- ✅ Project approved and resourced
- ✅ Foundation layers accessible

**When to use**:
- After project approval (idea → project transition)
- Before starting implementation work
- When project complexity requires task breakdown

---

## 🎯 Task Layer Structure

**3-Level Hierarchy** (per IDEAL-BEHAVIOR.md Section 1.12):

```yaml
project:
  id: proj-2024-005
  name: "SaaS Dashboard Implementation"

  epics:
    - id: epic-001
      name: "User Authentication"
      tasks:
        - id: task-001-a
          name: "Setup JWT auth"
          estimate: 4h
          dependencies: []

        - id: task-001-b
          name: "Implement login UI"
          estimate: 6h
          dependencies: [task-001-a]

    - id: epic-002
      name: "Dashboard Backend"
      tasks:
        - id: task-002-a
          name: "Design database schema"
          estimate: 3h
          dependencies: []
```

---

## 📋 Task Decomposition Algorithm

**Input**: Step 08 deep plan
**Output**: Executable task list with dependencies

```bash
# 1. Parse deep plan deliverables
DELIVERABLES=$(extract_deliverables_from_step08)

# 2. Group into epics (logical components)
EPICS=$(group_by_component "$DELIVERABLES")

# 3. Break epics into tasks (atomic work units)
for EPIC in $EPICS; do
    TASKS=$(decompose_epic "$EPIC" --max-size 8h)

    # 4. Identify dependencies
    DEPENDENCIES=$(analyze_dependencies "$TASKS")

    # 5. Validate no circular dependencies
    if has_circular_deps "$DEPENDENCIES"; then
        echo "❌ Circular dependency detected - review task structure"
        exit 1
    fi

    # 6. Store in project file
    save_tasks "$EPIC" "$TASKS" "$DEPENDENCIES"
done
```

---

## ⏱️ Estimation Guidelines

**Task Size Rules**:
- **Maximum**: 8 hours (1 workday)
- **Optimal**: 2-4 hours (half-day)
- **Too Large**: If > 8h, decompose further into subtasks

**Estimation Factors**:
- Technical complexity (from Step 08)
- Developer experience level
- External dependencies (APIs, data, approvals)
- Testing time (typically 30-50% of dev time)

---

## 🔗 Dependency Management

**Types of Dependencies**:

1. **Sequential** (finish-to-start):
   ```yaml
   task-002:
     depends_on: [task-001]  # Must complete 001 before starting 002
   ```

2. **Parallel** (can run concurrently):
   ```yaml
   task-003:
     depends_on: []  # Independent, start anytime
   ```

3. **External** (blocks outside this project):
   ```yaml
   task-004:
     depends_on: [external:api-approval]  # Waiting on external factor
   ```

**Critical Path Calculation**:
```bash
# Identify longest dependency chain
CRITICAL_PATH=$(calculate_critical_path "$ALL_TASKS")
PROJECT_DURATION=$(sum_estimates "$CRITICAL_PATH")
echo "Minimum project duration: $PROJECT_DURATION hours"
```

---

## 📊 Integration with Workflow

**Step 08 → Step 09 Transition**:
- Step 08 produces: Deliverables list + architecture decisions
- Step 09 consumes: Deliverables → Tasks with estimates + dependencies

**Step 09 → Implementation Transition**:
- Task layer complete → Ready for execution
- Tasks stored in: `data/projects/{project-id}/tasks.yaml`
- Track progress with: `scripts/dashboard.sh`

---

## 🔍 Validation Checklist

Before exiting Step 09, verify:

- [ ] All Step 08 deliverables mapped to tasks
- [ ] No task > 8 hours estimate
- [ ] Dependencies identified and validated (no circular)
- [ ] Critical path calculated (realistic timeline)
- [ ] External dependencies documented (risks flagged)
- [ ] Tasks stored in version control
- [ ] Team notified and assigned

---

## 🛠️ Tools & Commands

**Create task structure**:
```bash
# Generate tasks from Step 08 plan
npx claude-flow@v3alpha workflow execute \
    --step step-09 \
    --input data/projects/{project-id}/step-08-plan.md \
    --output data/projects/{project-id}/tasks.yaml
```

**Visualize dependencies**:
```bash
# Generate dependency graph
python3 scripts/visualize-tasks.py \
    --input data/projects/{project-id}/tasks.yaml \
    --output output/task-graph.png
```

**Validate task structure**:
```bash
# Check for issues
bash scripts/validate-tasks.sh data/projects/{project-id}/tasks.yaml
```

---

## 🎯 Success Criteria

**Step 09 is complete when**:
1. All deliverables from Step 08 have corresponding tasks
2. Task estimates are realistic (validated by team)
3. Dependencies mapped with no circular refs
4. Critical path calculated (project timeline known)
5. Tasks ready for assignment and execution

**Output Artifacts**:
- `tasks.yaml` - Task structure with metadata
- `task-graph.png` - Visual dependency diagram
- `critical-path.md` - Timeline and risk analysis

---

## 📖 See Also

- Step 08: Deep Planning (produces deliverables for this step)
- IDEAL-BEHAVIOR.md Section 1.12 (Task Layer specification)
- `data/projects/` (project file structure)
- `scripts/dashboard.sh` (task progress tracking)
