# Life OS Automation Scripts

**Location**: `_bmad/bmm/workflows/life-os/scripts/`

## Available Scripts

### 1. Idea Archive (`archive-idea.ps1` / `archive-idea.sh`)
**Purpose**: Move completed/killed ideas to archive
**Usage**:
```bash
# Windows
.\scripts\archive-idea.ps1 -IdeaId "idea-2024-001"

# Linux/macOS
bash scripts/archive-idea.sh idea-2024-001
```

**What it does**:
- Moves idea file from `data/ideas/` to `_archive/ideas/YYYY/`
- Updates idea index
- Stores archive metadata in memory

---

### 2. Project Completion (`complete-project.ps1` / `complete-project.sh`)
**Purpose**: Mark project as complete and archive
**Usage**:
```bash
# Windows
.\scripts\complete-project.ps1 -ProjectId "proj-2024-005"

# Linux/macOS
bash scripts/complete-project.sh proj-2024-005
```

**What it does**:
- Updates project status to COMPLETED
- Moves to archive with completion timestamp
- Generates project retrospective template

---

### 3. Idea to Project (`create-project-from-idea.ps1` / `create-project-from-idea.sh`)
**Purpose**: Convert scored idea into active project
**Usage**:
```bash
# Windows
.\scripts\create-project-from-idea.ps1 -IdeaId "idea-2024-003"

# Linux/macOS
bash scripts/create-project-from-idea.sh idea-2024-003
```

**What it does**:
- Creates project structure from idea template
- Inherits scoring data and foundation context
- Initializes Step 08 deep planning checklist

---

### 4. Dashboard (`dashboard.ps1` / `dashboard.sh`)
**Purpose**: View current Life OS status
**Usage**:
```bash
# Windows
.\scripts\dashboard.ps1

# Linux/macOS
bash scripts/dashboard.sh
```

**Output**:
- Active ideas count and top 5 by score
- Active projects with progress %
- Pending reminders
- Foundation layer status

---

### 5. Kill Project (`kill-project.ps1` / `kill-project.sh`)
**Purpose**: Cancel and archive failed/abandoned project
**Usage**:
```bash
# Windows
.\scripts\kill-project.ps1 -ProjectId "proj-2024-002" -Reason "Resource constraints"

# Linux/macOS
bash scripts/kill-project.sh proj-2024-002 "Resource constraints"
```

**What it does**:
- Marks project as KILLED
- Stores kill reason for learning
- Archives with metadata for retrospective analysis

---

### 6. Review Reminders (`review-reminders.ps1` / `review-reminders.sh`)
**Purpose**: Check and display scheduled reviews
**Usage**:
```bash
# Windows
.\scripts\review-reminders.ps1

# Linux/macOS
bash scripts/review-reminders.sh
```

**Output**:
- Overdue reviews (red)
- Due today (yellow)
- Upcoming this week (green)

---

### 7. Transition Manager (`transition-manager.ps1`)
**Purpose**: Manage workflow state transitions
**Usage**:
```powershell
.\scripts\transition-manager.ps1 -Action "advance" -CurrentStep "step-05" -EntityId "idea-2024-003"
```

**What it does**:
- Validates transition prerequisites
- Updates workflow state
- Triggers appropriate hooks
- Stores transition history

---

## Integration with Life OS Workflow

**Step 01** (Collect Ideas):
- Use `create-project-from-idea.sh` when idea reaches Step 08

**Step 05** (Scoring):
- Scripts read scoring data for prioritization
- Dashboard displays top-scored ideas

**Step 08** (Deep Planning):
- `complete-project.sh` triggered on project success
- `kill-project.sh` triggered on project abandonment

**Step 00** (Foundation):
- All scripts check foundation layers before execution
- Fail-fast if foundation incomplete

---

## Error Handling

All scripts include:
- Input validation
- File existence checks
- Rollback on failure
- Logging to `.claude-flow/logs/automation.log`

---

## Maintenance

**Location**: Scripts stored in version control
**Testing**: Each script includes `--dry-run` flag for testing
**Documentation**: Inline comments explain each operation
