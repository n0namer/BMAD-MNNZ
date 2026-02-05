---
name: 'step-x-03-milestone-gate'
description: 'Validate milestone completion against success criteria, analyze variances, and decide whether to PASS, ADJUST, or ESCALATE'
category: 'execution'
required: true
estimated_minutes: 20
---

# Step X-03: Milestone Gate Review

## STEP GOAL

Validate milestone completion against success criteria, analyze variances, and decide whether to:
- **PASS** - Continue to next milestone as planned
- **ADJUST** - Revise plan (rescope, extend timeline, reallocate resources)
- **ESCALATE** - Trigger pivot-or-kill decision (step-x-04)

**Purpose:** Prevent runaway commitments by enforcing quality gates at key checkpoints.

---

## WHEN TO USE

### Automatic Triggers
- **Milestone target date reached** - Scheduled review (from step-x-01 planning)
- **Date check automation** - System alerts when milestone date arrives

### Manual Triggers
- **Major phase completion** - When you believe milestone is complete (early or on-time)
- **Critical blocker discovered** - Immediate gate review to assess impact
- **Significant scope change** - Re-evaluate milestone validity

### Frequency
- **Every milestone** defined in step-x-01 (typically 2-6 week intervals)
- **Ad-hoc** when major variances detected in execution tracking

---

## MANDATORY RULES

- ✅ Review on schedule; never skip gates or move goalposts
- ✅ Calculate variance honestly; document root causes
- ✅ Save gate decision to memory + tracking file
- ✅ Proceed to step-x-04 if ESCALATE; don't continue without it
- 🎯 Use subprocess for milestone variance calculation (Pattern 3: Data Operations)
- 💬 Return structured variance analysis only

---

## MANDATORY SEQUENCE

### 1. Success Criteria Check

Evaluate each criterion from step-x-01:
- ✅ Met (100%) | ⚠️ Partial (50-99%) | ❌ Not Met (0-49%)

Calculate overall completion average.

---

### 2. Variance Analysis (Subprocess)

📖 Methods: data/milestone-variance-calc.md

**Launch a subprocess that:**
1. Loads milestone definition from kickoff (step-x-01)
2. Loads current progress from pulse tracker
3. Loads milestone-variance-calc.md with calculation formulas
4. Calculates:
   - **Timeline Variance:** (Actual Date - Planned Date) / Planned Duration × 100
   - **Scope Variance:** (Completed Tasks / Total Tasks) × 100
   - **Quality Variance:** Technical debt score, standards compliance %
5. Identifies root causes by pattern matching:
   - Technical (complexity underestimated, bugs discovered)
   - Resource (capacity overestimated, skill gaps)
   - External (dependencies delayed, requirements changed)
6. Returns structured variance report with severity ratings

**Subprocess returns:** Concise variance analysis (150-200 lines) instead of loading full milestone-variance-calc.md (600+ lines).

**Graceful fallback:** If subprocess unavailable, load `data/milestone-variance-calc.md` and manually calculate timeline/scope/quality variance.

Analyze:
- **Timeline:** Days variance from plan (%)
- **Scope:** What added/removed/deferred
- **Quality:** Standards met, technical debt level

Root causes: Technical (complexity, bugs) | Resource (time, skills) | External (dependencies, market)

---

### 3. Gate Decision

📖 Framework: data/milestone-gate-decisions.md | Escalation: data/milestone-escalation.md

#### Milestone Gate Decisions Loading (Subprocess)

**Launch a subprocess that:**
1. Loads data/milestone-gate-decisions.md
2. Extracts decision criteria matching current completion % and variance
3. Filters to PASS/ADJUST/ESCALATE thresholds only
4. Returns applicable decision logic (typically 20-30 lines instead of 150)

**Subprocess returns:** Decision outcome + decision logic only

**Graceful fallback:** If subprocess unavailable, use standard gate criteria (70%/30% variance) in main context.

- **PASS:** All criteria met, variance ≤30%, quality OK
- **ADJUST:** 70-89% complete OR 30-50% variance
- **ESCALATE:** <70% complete OR >50% variance OR critical blockers

---

### 4. Save & Update

**Update tracking file:**
```markdown
## Milestone {N}: {Name}

**Status:** ✅ COMPLETE | ⚠️ ADJUSTED | 🚨 ESCALATED
**Review Date:** {Date}
**Gate Decision:** {PASS/ADJUST/ESCALATE}
**Completion:** {X}%
**Timeline Variance:** {±X days}

**Notes:** {Brief summary of decision rationale}
```

**Save to memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "goals:milestone-gates:goal-{id}:milestone-{N}" \
  --content "Gate Review: {Decision} | Completion: {X}% | Variance: {±X days} | Reason: {Summary}"
```

**If ADJUSTED:** Update remaining milestones in goals.yaml or tracking file

**If ESCALATED:** Create pivot-trigger document and proceed to step-x-04

---

## REVIEW TEMPLATE (QUICK FORMAT)

📖 Full template: data/milestone-review-template.md

```markdown
## Milestone {N}: {Name}

**Target Date:** {Planned} | **Actual:** {Completed}
**Owner:** {Person}

### Success Criteria
| Criterion | Status | Notes |
|-----------|--------|-------|
| {Criterion 1} | ✅/⚠️/❌ | {Brief} |
| {Criterion 2} | ✅/⚠️/❌ | {Brief} |

**Completion:** {X}%

### Variance
- **Timeline:** {±X days} ({±X%})
- **Scope Changes:** {Added/Removed/Deferred}
- **Quality:** {Status} | Tech Debt: {Level}

### Root Causes (if needed)
- Technical: {Factor}
- Resource: {Factor}
- External: {Factor}

### Decision
**Gate:** [PASS / ADJUST / ESCALATE]
**Reason:** {1-2 sentences}
**Next:** {Action}
```

---

## MENU

1. Run gate review
2. View criteria thresholds
3. Calculate variance methods
4. See escalation protocol
5. Next step (PASS → continue | ESCALATE → step-x-04)

---

## SUCCESS CRITERIA

**Step complete when:**
- ✅ All success criteria evaluated
- ✅ Variance analysis documented (timeline, scope, quality)
- ✅ Root causes identified (if applicable)
- ✅ Gate decision made (PASS/ADJUST/ESCALATE)
- ✅ Tracking file updated with decision
- ✅ Gate decision saved to memory
- ✅ If ADJUSTED: Plan revised and documented
- ✅ If ESCALATED: Pivot-trigger created and step-x-04 initiated

---

## FAILURE CONDITIONS

**Abort this step if:**
- ❌ No milestone defined to review (go back to step-x-01)
- ❌ Execution tracking not started (complete step-x-02 first)
- ❌ Success criteria unclear (revisit step-x-01 planning)

**Warning signs:**
- ⚠️ Declaring PASS when criteria not fully met (self-deception)
- ⚠️ Choosing ADJUST repeatedly (pattern suggests ESCALATE needed)
- ⚠️ Avoiding ESCALATE due to sunk cost fallacy

---

**File:** `_bmad/bmm/workflows/life-os/steps-x/step-x-03-milestone-gate.md`
**Version:** 1.0.0
**Last Updated:** 2026-02-05
