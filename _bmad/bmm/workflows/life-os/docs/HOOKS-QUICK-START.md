# Life OS Hooks - Quick Start Guide

**5-Minute Setup** | **Zero Manual File Management** | **Automated Lifecycle Transitions**

---

## What You Get

Automatic file movement when workflow steps complete:

```
✅ Complete L1-S3 → idea-007.yaml moves: inbox/ → evaluated/
✅ Complete L2-S1 → idea-007.yaml moves: evaluated/ → planned/
✅ Complete L2-S3 (GO) → idea-007.yaml moves: planned/ → active/ (if capacity available)
```

---

## 1-Minute Setup

### Step 1: Verify System (30 seconds)

```powershell
# Check daemon
npx claude-flow@v3alpha daemon status

# Start if needed
npx claude-flow@v3alpha daemon start
```

### Step 2: Initialize Hooks (30 seconds)

```powershell
# Navigate to Life OS
cd "d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os"

# Initialize session with hooks
npx claude-flow@v3alpha hooks session-start --session-id "life-os-$(Get-Date -Format 'yyyyMMdd')"
```

### Done!

The hooks system is now active. Files will automatically move when you complete L1-S3, L2-S1, or L2-S3 steps.

---

## How To Use

### Automatic Mode (Recommended)

Just work through your Life OS workflow normally. When you complete a step:

1. **Say:** "Complete L1-S3 for idea-007"
2. **Claude executes:** DFVC evaluation
3. **Hook triggers:** Moves `idea-007.yaml` from `inbox/` → `evaluated/`
4. **Memory logs:** Transition saved to global memory

### Manual Mode (Testing/Debugging)

```powershell
# Test transition (dry run)
.\scripts\transition-manager.ps1 `
    -Action "transition-inbox-evaluated" `
    -IdeaId "007" `
    -StepName "L1-S3" `
    -DryRun

# Execute transition
.\scripts\transition-manager.ps1 `
    -Action "transition-inbox-evaluated" `
    -IdeaId "007" `
    -StepName "L1-S3"
```

---

## Transitions

| Step Complete | File Movement | Capacity Check |
|---------------|---------------|----------------|
| **L1-S3** (DFVC evaluation) | `inbox/` → `evaluated/` | No |
| **L2-S1** (Detailed analysis) | `evaluated/` → `planned/` | No |
| **L2-S3** (GO decision) | `planned/` → `active/` | ✅ Yes (max 5) |

---

## Capacity Management

### What Happens When 5/5 Active?

If you try to activate a 6th project:

```
❌ CAPACITY FULL: Cannot activate (5/5 projects active)
Please complete or archive an active project first
```

The file remains in `planned/` folder until capacity becomes available.

### Check Current Capacity

```powershell
# Count active projects
Get-ChildItem "output\active\*.yaml" | Measure-Object

# Dashboard view (shows capacity + status)
.\scripts\dashboard.ps1
```

### Free Up Capacity

```powershell
# Complete a project
.\scripts\archive-idea.ps1 -IdeaId "003" -Status "completed"

# Kill a project
.\scripts\archive-idea.ps1 -IdeaId "005" -Status "killed" -Reason "Market validation failure"
```

---

## Troubleshooting

### Hook Not Triggering?

```powershell
# 1. Check daemon
npx claude-flow@v3alpha daemon status

# 2. Re-initialize hooks
npx claude-flow@v3alpha hooks session-start --session-id "life-os-$(Get-Date -Format 'yyyyMMdd')"

# 3. Verify task naming includes step identifier
# ✅ Good: "Complete L1-S3 for idea-007"
# ❌ Bad: "Evaluate idea 007"
```

### File Not Moving?

```powershell
# Check file exists in source folder
Get-ChildItem "output\inbox\idea-*.yaml"

# Verify idea ID matches filename
# File must be: idea-007.yaml
# IdeaId must be: "007"
```

### Memory Not Saving?

```powershell
# Check memory backend
npx claude-flow@v3alpha memory status

# Create namespace if missing
npx claude-flow@v3alpha memory namespace create --name "life-os-transitions" --global
```

---

## Memory & History

### View Transition History

```powershell
# All transitions for idea-007
npx claude-flow@v3alpha memory search -q "idea-007" --namespace "life-os-transitions"

# All failed transitions
npx claude-flow@v3alpha memory search -q "success:false" --namespace "life-os-transitions"

# All capacity blocks
npx claude-flow@v3alpha memory search -q "capacity-check-failed" --namespace "life-os-transitions"
```

### Why Memory Matters

Every transition is logged with:
- ✅ Timestamp
- ✅ Source/target folders
- ✅ Success/failure status
- ✅ Idea ID and step name

This creates:
- **Audit trail** - Full history of all movements
- **Pattern learning** - Hooks system learns optimal timing
- **Cross-session continuity** - Works across multiple Claude sessions
- **Rollback capability** - Recover from errors

---

## Advanced Usage

### Custom Hook Configuration

Edit `.claude-flow/hooks-config.json` to customize:
- Trigger patterns
- Action scripts
- Memory TTL
- Validation rules
- Notifications

### Add Custom Transitions

```json
{
  "pattern": "L3-S2",
  "description": "Execution complete - prepare retrospective",
  "action": "transition-active-retrospective",
  "params": {
    "source_folder": "active",
    "target_folder": "retrospective"
  }
}
```

### Debug Mode

```powershell
# Enable verbose logging
$env:CLAUDE_FLOW_LOG_LEVEL = "debug"

# Run with debug output
.\scripts\transition-manager.ps1 `
    -Action "transition-inbox-evaluated" `
    -IdeaId "007" `
    -StepName "L1-S3" `
    -Verbose
```

---

## Files & Locations

| File | Purpose |
|------|---------|
| `docs/HOOKS-CONFIGURATION.md` | Full documentation (this guide's big brother) |
| `docs/HOOKS-QUICK-START.md` | This quick-start guide |
| `.claude-flow/hooks-config.json` | Hook trigger configuration |
| `scripts/transition-manager.ps1` | File movement script |

---

## Next Steps

1. **Test with sample idea** - Create `test-001` and run through lifecycle
2. **Monitor first real transition** - Watch it happen with your first real idea
3. **Check memory** - Search for your transitions in global memory
4. **Customize** - Edit `hooks-config.json` to add custom triggers
5. **Read full docs** - See `HOOKS-CONFIGURATION.md` for advanced features

---

## Support

**Need help?** Check the full documentation:
- **Full Guide:** `docs/HOOKS-CONFIGURATION.md`
- **Troubleshooting:** Section 10 in full guide
- **Claude Flow Hooks:** `.claude-flow/docs/HOOKS-REFERENCE.md`

---

**Setup Time:** < 1 minute
**Manual Work Saved:** 100% (zero file management)
**Audit Trail:** Complete (all transitions logged)
**Configuration Complete:** ✅
