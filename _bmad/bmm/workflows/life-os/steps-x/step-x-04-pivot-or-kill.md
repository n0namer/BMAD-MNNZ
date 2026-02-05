---
name: 'step-x-04-pivot-or-kill'
description: 'Execute honest assessment when idea is significantly behind or blocked, decide to Pivot (change approach), Kill (stop work), or Persist (continue with caution)'
category: 'exception'
required: false
estimated_minutes: 60
---

# Step X-04: Pivot or Kill Decision Gate

## STEP GOAL

**Execute honest assessment when idea significantly behind or blocked → Decide: Pivot (change approach), Kill (stop work), or Persist (continue with caution)**

**Critical questions:**
- Is the original goal still valid and aligned?
- Can we achieve it with a different approach?
- Is continuing worth the opportunity cost?

---

## WHEN TO USE THIS STEP

**Auto-trigger conditions:**
- ✅ **2+ consecutive weeks** in 🔴 RED status
- ✅ **Milestone gate escalation** → Blocker unresolved for >1 week
- ✅ **Critical blocker discovered** → Cannot proceed without major pivot
- ✅ **ROI turned negative** → Costs exceed expected benefits

**Manual trigger:**
- User explicitly requests pivot-or-kill assessment
- Significant change in external factors (priorities, resources, market)
- Team consensus that current approach isn't working

---

## MANDATORY EXECUTION RULES

**CRITICAL:** This is an exception workflow - only run when triggered by conditions above.

**Anti-patterns to avoid:**
- ❌ **Sunk cost fallacy:** "Already invested X hours, can't stop now"
- ❌ **Optimism bias:** "Just one more week and it'll work"
- ❌ **Status quo bias:** "Killing feels like failure"
- ❌ **Analysis paralysis:** "Need more data before deciding"

**Healthy mindsets:**
- ✅ Killing bad ideas is a skill (prevents wasted effort)
- ✅ Pivoting early is better than pivoting late
- ✅ WIP capacity is precious (opportunity cost real)
- ✅ Learning what doesn't work is valuable

**Execution optimization:**
- 🎯 Use subprocess for pivot decision framework scoring (Pattern 3: Data Operations)
- 💬 Return structured score + decision only

---

## MANDATORY SEQUENCE

### 1. Prepare Assessment

**Create:** `output/step-x-04-decision-{idea-id}.md`

**Template sections:**
1. **Current Situation:** Original intent, actual progress, status history
2. **Root Cause Analysis:** Primary cause, contributing factors, learnings
3. **Decision:** KILL/PIVOT/PERSIST + rationale + confidence
4. **Next Actions:** From appropriate protocol

**Be brutally honest - avoid sunk cost fallacy**

---

### 2. Scoring Framework (Subprocess)

📖 **Full framework:** `data/pivot-or-kill-scoring.md`

**Launch a subprocess that:**
1. Loads idea's original goals, scoring, and Deep Plan
2. Loads current status from pulse tracker and milestone gates
3. Loads pivot-or-kill-scoring.md with scoring rubrics
4. Scores 4 dimensions (0-10 each):
   - **Goal Alignment:** Still aligned with user's goals.yaml?
   - **ROI Potential:** Expected value vs invested effort
   - **Feasibility with Pivot:** Can different approach succeed?
   - **Opportunity Cost:** What's being sacrificed by continuing?
5. Calculates total score (0-40)
6. Returns structured recommendation with threshold mapping

**Subprocess returns:** Concise scoring report (150-200 lines) instead of loading full pivot-or-kill-scoring.md (700+ lines).

**Graceful fallback:** If subprocess unavailable, load `data/pivot-or-kill-scoring.md` and manually score 4 dimensions.

**Score 4 dimensions (0-10 each):**
- Goal alignment, ROI potential, Feasibility with pivot, Opportunity cost (reverse)

**Thresholds:** 0-15 = KILL | 16-25 = PIVOT | 26-40 = PERSIST

---

### 3. Apply Decision Protocol

**Based on score:**

#### Kill Decision Protocol Loading (Subprocess)

**KILL (0-15)** → 📖 `data/kill-decision-protocol.md`
- Update tracking, run archive script, create retrospective, store in memory, free WIP

**Launch a subprocess that (if KILL decision):**
1. Loads data/kill-decision-protocol.md
2. Extracts kill procedure section (archive steps, WIP release, memory storage)
3. Returns formatted kill actions (typically 30-40 lines instead of 180)

**Subprocess returns:** Kill decision checklist ready to execute

**Graceful fallback:** If subprocess unavailable, use manual kill procedure in main context.

#### Pivot Decision Protocol Loading (Subprocess)

**PIVOT (16-25)** → 📖 `data/pivot-protocol.md`
- Create pivot plan, re-run step-02-score + step-03-plan, update tracking, store pattern

**Launch a subprocess that (if PIVOT decision):**
1. Loads data/pivot-protocol.md
2. Extracts pivot planning section for current idea domain
3. Returns pivot plan template + re-run steps (typically 40-60 lines instead of 220)

**Subprocess returns:** Pivot plan structure + next steps

**Graceful fallback:** If subprocess unavailable, create pivot plan manually in main context.

#### Persist Decision Protocol Loading (Subprocess)

**PERSIST (26-40)** → 📖 `data/persist-protocol.md`
- Document rationale, set commit date (2-4 weeks max), update tracking, add reminder
- **CRITICAL:** If still blocked at commit date → Auto-trigger KILL

**Launch a subprocess that (if PERSIST decision):**
1. Loads data/persist-protocol.md
2. Extracts commitment documentation section
3. Returns rationale template + commit date setup (typically 25-35 lines instead of 140)

**Subprocess returns:** Persist commitment documentation

**Graceful fallback:** If subprocess unavailable, document rationale + set reminder manually.

---

### 4. Save Decision

**Save to:**
1. Decision doc: `output/step-x-04-decision-{idea-id}.md`
2. Tracking file: `tracking/{idea-id}.md`
3. Memory: `shared-knowledge:decisions:pivot-or-kill:{idea-id}:{decision}`

---

## MENU OPTIONS

```
📍 Step X-04: Pivot or Kill Decision Gate [EXCEPTION] ~60 min
⚠️ Triggered by: {Condition}

Steps: Assessment → Root cause → Score (0-40) → Execute protocol

[✅ Start] [❓ Learn more] [⏸️ Pause]
```

---

## SUCCESS CRITERIA

**This step succeeds when:**
- ✅ Decision made with clear rationale
- ✅ Score calculated objectively (0-40)
- ✅ Appropriate protocol executed completely
- ✅ All artifacts saved (decision doc, tracking, memory)
- ✅ Next actions clear and scheduled

**This step fails when:**
- ❌ Decision avoided or postponed
- ❌ Scoring influenced by sunk cost fallacy
- ❌ Protocol incomplete (missing steps)
- ❌ No commit date set for PERSIST decisions

---

## INTEGRATION WITH LIFE OS

**When this step impacts other systems:**
- **Quarterly Review (step-04):** Killed/pivoted ideas reviewed for patterns
- **Goals Discovery (step-00):** Learnings feed into future goal selection
- **Deep Plan (step-08):** Pivot plans integrated into replanning

**Frequency:** Exception-driven (not routine)

**Success metric:** 80%+ of pivot/kill decisions feel "right" 3 months later

---

## EXAMPLES

### Example 1: KILL Decision
```
Score: 12/40 (low ROI, high opportunity cost)
Decision: KILL "Build personal CRM app"
Reason: Better alternatives exist (use existing tools), learning backend = 100+ hours
Next: Archive learnings, start higher-priority idea from backlog
```

### Example 2: PIVOT Decision
```
Score: 22/40 (goal valid, approach broken)
Decision: PIVOT "Write technical book" → Blog series instead
Reason: Same content, smaller chunks, lower risk
Next: Re-run scoring and planning with blog format
```

### Example 3: PERSIST Decision
```
Score: 28/40 (almost done, temporary blocker)
Decision: PERSIST "Launch side project MVP"
Reason: Waiting on API access (granted in 2 weeks), 85% complete
Next: Continue, reassess if still blocked in 2 weeks
```

---

**END OF STEP X-04**
