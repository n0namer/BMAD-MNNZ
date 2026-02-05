# PERSIST Decision Protocol

## What PERSIST Means

- Continue current plan
- Blocker is temporary, will resolve
- Set commit date for forced reassessment
- Status stays: IN_PROGRESS (PERSISTING)

---

## When to Choose PERSIST

- **High confidence blocker will resolve:** >70% confidence
- **Blocker is external/temporary:** Waiting on someone/something
- **Already 80%+ complete:** Finish line in sight
- **Score range:** 26-40/40

---

## Execution Steps

### 1. Document WHY Continuing

File: `output/step-x-04-persist-rationale-{idea-id}.md`

```markdown
# Persist Rationale: {Idea Name}

## Current Blocker
{What's blocking progress}

## Why We Believe It Will Resolve
{Concrete evidence, not optimism}

**Evidence supporting persistence:**
- {Concrete reason 1}
- {Concrete reason 2}
- {Concrete reason 3}

**Confidence level:** {X}% (must be >70%)

---

## Commit Date

**Reassess on:** {Date - 2-4 weeks max}

**If still blocked at commit date:**
- Auto-trigger KILL decision
- No third chances

**Expected resolution:**
{What needs to happen for blocker to clear}

---

## Risk Assessment

**Persistence risk:** {Low/Medium/High}

**Why:** {Justification}

**Mitigation:**
{What can be done while waiting}
```

---

### 2. Set Commit Date

**CRITICAL:** Commit date is MANDATORY

- **Maximum:** 2-4 weeks from decision
- **Minimum:** 1 week (avoid indefinite waiting)
- **Non-negotiable:** If commit date reached and still blocked → MUST run pivot-or-kill again (usually KILL)

**Add to calendar:**
{How to set reminder for commit date reassessment}

---

### 3. Update Tracking File

File: `tracking/{idea-id}.md`

```markdown
Status: IN_PROGRESS (PERSISTING)
Persist decision date: {ISO_DATE}
Commit date: {Date}
Blocker: {What we're waiting for}
Confidence: {X}%

## Persistence Conditions
- **Will resolve if:** {Condition}
- **Auto-kill if:** Still blocked on {commit_date}
```

---

### 4. Interim Actions

**While waiting, execute:**

- Work on other ideas (don't let WIP slot sit idle)
- Prepare for unblocking (research, setup, dependencies)
- Monitor blocker status weekly
- Document learnings from being blocked

---

## Example: PERSIST Decision

```
Idea: "Launch side project MVP"
Trigger: Milestone gate escalation (waiting on API access)
Score: 28/40 (almost done, temporary blocker)
Decision: PERSIST
Commit date: 2 weeks (when API access granted)
Next: Continue, reassess if still blocked in 2 weeks
```

---

## Warning Signs

**Re-evaluate PERSIST if:**

- ⚠️ Confidence drops below 70%
- ⚠️ New blockers discovered while waiting
- ⚠️ Blocker resolution date keeps slipping
- ⚠️ Opportunity cost increases (better ideas emerge)

---

## Commit Date Reached Protocol

**If commit date reached and still blocked:**

1. **STOP immediately** - No extensions
2. **Run pivot-or-kill again** - Fresh assessment
3. **Default to KILL** - Unless strong evidence for pivot
4. **No third persistence** - Only one persist per idea

**Why this rule exists:**
- Prevents indefinite waiting
- Forces honest reassessment
- Respects opportunity cost
- Avoids sunk cost trap

---

## Success Criteria

**A good persist decision:**
- ✅ Blocker is genuinely external/temporary
- ✅ High confidence (>70%) it will resolve
- ✅ Clear commit date set (2-4 weeks)
- ✅ Interim actions identified
- ✅ Almost complete (>80% done)

**A bad persist decision:**
- ❌ Hope-based (no concrete evidence)
- ❌ Indefinite wait ("eventually will work out")
- ❌ Low confidence (<50%)
- ❌ Multiple blockers stacking
- ❌ Early stage (<50% complete)
