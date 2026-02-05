# KILL Decision Protocol

## What KILL Means

- Stop work immediately
- Archive learnings and artifacts
- Free WIP capacity (open slot for new idea)
- Mark status: KILLED

---

## When to Choose KILL

- **ROI turned negative:** Benefits < costs
- **Goal no longer aligned:** With life priorities
- **Better opportunities emerged:** Higher-value ideas waiting
- **Persistent blockers:** With no viable workaround
- **Score range:** 0-15/40

---

## Execution Steps

### 1. Update Tracking File

File: `tracking/{idea-id}.md`

```markdown
Status: KILLED
Killed date: {ISO_DATE}
Reason: {Brief reason}
```

---

### 2. Archive the Killed Idea

**Windows:**
```powershell
cd scripts
.\archive-idea.ps1 -IdeaId "{idea-id}" -Status "killed" -Reason "{kill_reason}"
```

**macOS/Linux:**
```bash
cd scripts
./archive-idea.sh {idea-id} killed "{kill_reason}"
```

**This automatically:**
- Saves to quarterly archive folder
- Includes pivot-or-kill analysis
- Stores in global memory
- Enables pattern mining

---

### 3. Create Retrospective

File: `output/idea-{idea-id}-killed-retro.md`

```markdown
# Retrospective: {Idea Name}

## What We Tried
{Summary of approach}

## Why We Stopped
{Root causes from assessment}

## What We Learned
{Key insights - prevents repeating mistakes}

## Reusable Artifacts
{Code, docs, patterns worth keeping}

## Calibration Data (for future estimates)

**Planned vs Actual:**
- Planned complexity: {X}/10
- Actual complexity encountered: {Y}/10
- Planned timeline: {Z} weeks
- Actual time invested: {W} weeks (before kill)

**Why estimates were off:**
{Specific assumptions that were wrong}

**Recommendations for similar ideas:**
- {Recommendation 1}
- {Recommendation 2}
```

---

### 4. Memory Archival

**Archive learnings:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "archive:killed:{idea-id}" \
  --content "{Retrospective summary + learnings}"
```

**Store calibration data:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "retrospective" \
  --key "idea-{idea-id}:killed:{date}" \
  --content "{
    status: 'KILLED',
    planned_complexity: {X},
    actual_complexity: {Y},
    planned_duration: '{Z} weeks',
    invested_duration: '{W} weeks',
    learnings: [...],
    assumptions_wrong: [...],
    recommendations: [...]
  }"
```

---

### 5. Free WIP Slot

- Update `data/goals.yaml` → Remove from active WIP
- Update quarterly tracking → Mark as KILLED
- **Celebrate the hard decision** (killing bad ideas is success!)

---

## Example: KILL Decision

```
Idea: "Build personal CRM app"
Trigger: 3 weeks red, critical blocker (no backend skills)
Score: 12/40 (low ROI, high opportunity cost)
Decision: KILL
Reason: Better alternatives exist (use existing tools), learning backend = 100+ hours
Next: Archive learnings, start higher-priority idea from backlog
```

---

## Healthy Mindsets

✅ **Remember:**
- Killing bad ideas is a SKILL (prevents wasted effort)
- Sunk cost is irrelevant (past hours can't be recovered)
- WIP capacity is precious (opportunity cost is real)
- Learning what doesn't work is valuable
- "No" to this = "Yes" to something better
