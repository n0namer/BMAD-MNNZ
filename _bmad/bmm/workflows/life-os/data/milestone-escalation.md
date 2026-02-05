# Milestone Escalation Protocol

## When to Escalate

**ESCALATE if ANY of these conditions are met:**

1. **Completion <70%** - Significant gap from target
2. **Timeline variance >50%** - More than double expected time
3. **Critical blocker discovered** - Fundamental technical/resource issue
4. **ROI now negative** - Goal no longer worth pursuing
5. **Quality unrecoverable** - Would require complete redesign
6. **Repeated failures** - This is 2nd+ failed milestone gate

---

## Escalation Actions

### 1. STOP Current Execution
- Do not proceed to next milestone
- Pause all work on this goal
- Document current state

### 2. Gather Data for Pivot-or-Kill Analysis

**Sunk Cost Assessment:**
- Total time invested so far
- Resources consumed
- Opportunity cost (what else could have been done)

**Remaining Effort:**
- Estimated time to complete with current approach
- Additional resources needed
- Risk of further delays

**Value Assessment:**
- Current ROI (has it changed since goal start?)
- Market/environment changes
- Alternative approaches available
- Strategic importance now vs. when started

**Blocker Analysis (if applicable):**
- Nature of blocker (technical, resource, external)
- Workarounds explored
- Likelihood of resolution
- Time/cost to resolve

### 3. Create Pivot-or-Kill Trigger Document

**File:** `_bmad/bmm/workflows/life-os/output/goal-{id}-pivot-trigger.md`

```markdown
# Pivot-or-Kill Trigger: Goal {ID}

**Triggered By:** Milestone {N} Gate Review
**Date:** {Date}
**Reason:** {Why escalated}

**Data for Step X-04:**
- Sunk cost: {Time/resources spent}
- Remaining effort: {Estimated completion time}
- Current ROI: {Positive/Negative/Uncertain}
- Blocker: {Description if applicable}

**Next Step:** Proceed to step-x-04-pivot-or-kill.md
```

### 4. Proceed to Step X-04

**Options in Step X-04:**
- **Kill:** Abandon goal, cut losses
- **Pivot:** Change approach, rescope dramatically
- **Double-down:** Major replanning with renewed commitment

---

## Escalation Examples

### Example 1: Technical Blocker
```
Milestone 2 of software project
- Completion: 45%
- Timeline variance: +80% (planned 2 weeks, took 3.6 weeks)
- Critical blocker: Third-party API deprecated, no replacement available
- Decision: ESCALATE
- Trigger: Fundamental technical impossibility
```

### Example 2: ROI Negative
```
Milestone 3 of learning project
- Completion: 65%
- Timeline variance: +60%
- Market shift: Certification no longer valued by employers
- Decision: ESCALATE
- Trigger: ROI now negative
```

### Example 3: Repeated Failure
```
Milestone 2 (second attempt after first ADJUST)
- Completion: 72%
- Timeline variance: +55%
- Pattern: Same blockers as first attempt
- Decision: ESCALATE
- Trigger: 2nd failed milestone gate
```

---

## Post-Escalation Protocol

1. **Save gate decision to memory:**
   ```bash
   npx claude-flow@v3alpha memory store \
     --namespace "shared-knowledge" \
     --key "goals:milestone-gates:goal-{id}:escalation" \
     --content "ESCALATED: {Reason} | Completion: {X}% | Variance: {±X%}"
   ```

2. **Update tracking file:**
   - Mark milestone as 🚨 ESCALATED
   - Add escalation reason
   - Link to pivot-trigger document

3. **Schedule Step X-04:**
   - Block calendar time for pivot-or-kill decision
   - Gather stakeholder input if needed
   - Prepare data for analysis

---

## Prevention Tips

**To avoid escalation:**
- Run Step X-03 (Milestone Gate) on schedule - don't skip reviews
- Choose ADJUST early when variance appears
- Address root causes immediately
- Validate ROI at each milestone
- Test critical dependencies early in project
