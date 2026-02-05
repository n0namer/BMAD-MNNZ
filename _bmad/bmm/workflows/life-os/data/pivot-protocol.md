# PIVOT Decision Protocol

## What PIVOT Means

- Keep original goal, change approach/scope
- Re-run scoring and planning with new constraints
- Reset execution tracking
- Status stays: IN_PROGRESS (PIVOTED)

---

## When to Choose PIVOT

- **Goal still valid and aligned:** Original intent is sound
- **Different path is viable:** Evidence-based alternative exists
- **Learned enough to make better plan:** New understanding changes approach
- **Score range:** 16-25/40

---

## Execution Steps

### 1. Create Pivot Plan

File: `output/step-x-04-pivot-plan-{idea-id}.md`

```markdown
# Pivot Plan: {Idea Name}

## What's Changing

**Original approach:**
{What wasn't working}

**New approach:**
{Significantly different strategy}

**Why this will work better:**
{Evidence/rationale for pivot}

---

## New Scope

**Original scope:**
{What was originally planned}

**Revised scope:**
{What gets descoped/simplified}

**New constraints:**
- {Constraint 1}
- {Constraint 2}

**New timeline estimate:** {X weeks}

---

## Re-Scored Priorities

**Original score:** {X}/10
**New score after pivot:** {Y}/10

**What changed:**
{Why pivot improves viability}
```

---

### 2. Re-run Planning

**Execute these steps in order:**

1. **Step 02 - Score:** Re-run with pivot context
   - Use new understanding
   - Update complexity estimate
   - Revise effort estimate

2. **Step 03 - Make Plan:** Execute with revised approach
   - New milestones based on pivot
   - Updated dependencies
   - Reset status to GREEN

3. **Reset execution tracking:**
   - Clear previous status history
   - Mark as PIVOTED
   - Start fresh progress tracking

---

### 3. Update Tracking File

File: `tracking/{idea-id}.md`

```markdown
Status: IN_PROGRESS (PIVOTED)
Pivot date: {ISO_DATE}
Pivot reason: {Brief reason}
New approach: {Summary}

## Pivot History
- **Original approach:** {What didn't work}
- **New approach:** {What we're trying now}
```

---

### 4. Memory Update

**Store pivot pattern:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "patterns:pivot:{idea-id}" \
  --content "{
    original_approach: '{What didn't work}',
    why_failed: '{Root cause}',
    new_approach: '{Revised strategy}',
    rationale: '{Why this will work}',
    learnings: [...]
  }"
```

---

## Example: PIVOT Decision

```
Idea: "Write technical book"
Trigger: 2 weeks red, scope too large
Score: 22/40 (goal valid, approach broken)
Decision: PIVOT
New approach: Write blog series instead (same content, smaller chunks)
Next: Re-run scoring and planning with blog format
```

---

## Pivot Risk Assessment

**Before executing pivot, evaluate:**

| Risk Level | Indicators |
|------------|-----------|
| **Low** | Simple scope reduction, clear path forward |
| **Medium** | New skills needed, moderate uncertainty |
| **High** | Major unknowns, speculative approach |

**If pivot risk is HIGH:** Consider KILL instead

---

## Success Criteria

**A good pivot:**
- ✅ Addresses root cause of original failure
- ✅ Significantly different from original approach
- ✅ Evidence-based (not just optimism)
- ✅ Simpler/smaller than original plan
- ✅ Maintains alignment with core goal

**A bad pivot:**
- ❌ Minor tweaks to broken approach
- ❌ Based on wishful thinking
- ❌ Increases complexity/scope
- ❌ Drifts from original goal
