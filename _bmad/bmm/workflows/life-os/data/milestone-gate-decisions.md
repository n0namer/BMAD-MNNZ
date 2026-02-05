# Milestone Gate Decision Framework

## ✅ PASS - Continue to Next Milestone

**Conditions (ALL must be true):**
- ✅ **All success criteria met** (100% or 90%+ with minor gaps)
- ✅ **Timeline variance ≤30%** (e.g., 2-week milestone completed in ≤18 days)
- ✅ **No critical blockers** for next milestone
- ✅ **Quality standards met** (no major technical debt)
- ✅ **ROI still positive** (goal remains valuable)

**Actions:**
- Mark milestone as COMPLETE
- Proceed to next milestone in step-x-02 execution tracking
- Update overall goal progress
- Save lessons learned to memory

---

## ⚠️ ADJUST - Revise Plan

**Conditions (ONE or more):**
- ⚠️ **Partial completion (70-89%)** - Significant progress but gaps remain
- ⚠️ **Timeline variance 30-50%** - Behind schedule but recoverable
- ⚠️ **Scope creep detected** - Original plan needs refinement
- ⚠️ **Recoverable blockers** - Issues can be resolved with plan changes
- ⚠️ **Quality issues** - Needs rework but not fundamental redesign

**Actions:**
1. **Determine Adjustment Type:**
   - **Rescope:** Remove/defer non-critical items
   - **Extend timeline:** Add buffer to remaining milestones
   - **Reallocate resources:** Change time allocation or priorities
   - **Add support:** Get help, tools, or training

2. **Update Plan:**
   - Revise remaining milestones in step-x-01 planning file
   - Adjust success criteria if needed (with justification)
   - Recalculate timeline and resource needs

3. **Document:**
   - Save adjusted plan to `goals.yaml` and tracking file
   - Log reason for adjustment in memory
   - Set new review date

4. **Communicate:**
   - Notify stakeholders (if applicable)
   - Update expectations

**Resume execution with adjusted plan.**

---

## 🚨 ESCALATE - Trigger Pivot-or-Kill Decision

**Conditions (ONE or more):**
- 🚨 **Completion <70%** - Significant gap from target
- 🚨 **Timeline variance >50%** - More than double expected time
- 🚨 **Critical blocker discovered** - Fundamental issue (technical impossibility, dependency failure, resource unavailable)
- 🚨 **ROI now negative** - Goal no longer worth pursuing (market changed, better alternatives emerged)
- 🚨 **Quality unrecoverable** - Would require complete redesign
- 🚨 **Repeated failures** - This is 2nd+ failed milestone gate

**Actions:**
1. **STOP current execution** - Do not proceed to next milestone
2. **Gather data** for pivot-or-kill analysis:
   - Sunk cost (time/resources spent)
   - Remaining effort to complete
   - Current value/ROI assessment
   - Alternative approaches available

3. **Proceed to Step X-04 (Pivot-or-Kill Decision)**
   - Full retrospective and decision process
   - Options: Kill goal, Pivot to new approach, Double-down with major replanning

**Do NOT continue execution until pivot-or-kill decision made.**
