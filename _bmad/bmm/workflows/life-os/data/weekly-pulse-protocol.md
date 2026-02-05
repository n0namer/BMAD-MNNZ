# Weekly Pulse Protocol - 3-Question Template

## Template Structure

```markdown
## Weekly Pulse: {Idea Name}
**Date:** {YYYY-MM-DD}
**Week:** {Week number in execution}
**Executor:** {Name}

---

### Q1: Progress This Week
**What got done?**

- [ ] Milestone/feature/achievement 1
- [ ] Milestone/feature/achievement 2
- [ ] Milestone/feature/achievement 3

**Key wins:**
- {Concrete accomplishment}

**Completion %:** {Estimated overall progress}

---

### Q2: Blockers/Risks
**What's preventing progress?**

**Current Blockers:**
- 🚧 {Technical/resource/external blocker}
- 🚧 {Another blocker if applicable}

**Severity:**
- 🟢 Minor: Can work around
- 🟡 Moderate: Slowing progress 20-40%
- 🔴 Critical: Work stopped or >40% delay

**Resolution Plan:**
- {Action to unblock}
- {ETA for resolution}

---

### Q3: Next Week Priority
**What's the single most important thing to complete?**

**Primary Focus:**
- {One clear objective}

**Success Criteria:**
- {How to know it's done}

**Dependencies:**
- {What must happen first}

---

## Status Assessment

**Formula:**
```
Actual Progress vs. Planned Progress (from milestones)
- 🟢 On Track: ±20% variance
- 🟡 At Risk: 20-40% behind, recoverable with action
- 🔴 Blocked: >40% behind or critical blocker present
```

**Current Status:** [Auto-calculated or manual override]

**Trend:** [↗️ Improving | ➡️ Stable | ↘️ Declining]
```

---

## Usage Examples

### Example 1: Healthy Progress

```markdown
## Weekly Pulse: Mobile App MVP

**Week:** 3
**Date:** 2026-02-05

### Q1: Progress This Week
- [x] User authentication flow completed
- [x] Database schema finalized
- [x] 3 core screens designed

**Completion:** 35% (target 30%)

### Q2: Blockers/Risks
**Current Blockers:** None

**Minor Concerns:**
- Third-party API docs unclear (workaround in progress)

### Q3: Next Week Priority
Complete user profile screen with edit functionality

**Status:** 🟢 On Track
```

### Example 2: At Risk

```markdown
## Weekly Pulse: Content Platform

**Week:** 5
**Date:** 2026-02-05

### Q1: Progress This Week
- [x] Backend API endpoints (2/5 done)
- [ ] Frontend integration (blocked)

**Completion:** 40% (target 55%)

### Q2: Blockers/Risks
🚧 **BLOCKER:** Designer unavailable for 2 more weeks
🚧 **RISK:** Third-party service pricing unclear

**Severity:** 🟡 Moderate (25% behind)

**Resolution:**
- Use placeholder UI for now
- Email vendor for pricing by Friday

### Q3: Next Week Priority
Complete remaining 3 API endpoints + placeholder UI

**Status:** 🟡 At Risk - recoverable with action
```

### Example 3: Critical Issues

```markdown
## Weekly Pulse: E-commerce Integration

**Week:** 7
**Date:** 2026-02-05

### Q1: Progress This Week
- [ ] Payment gateway integration (still blocked)
- [x] Minor bug fixes

**Completion:** 45% (target 70%) - **25% behind**

### Q2: Blockers/Risks
🚧 **CRITICAL:** Payment gateway API access denied (3rd week)
🚧 **CRITICAL:** Budget overrun by 40%

**Severity:** 🔴 Critical - work stopped

**Resolution:**
- Escalate to vendor CEO (tomorrow)
- **TRIGGER:** Pivot-or-kill analysis if not resolved by Friday

### Q3: Next Week Priority
**BLOCKED** - Resolve payment gateway OR pivot to alternative

**Status:** 🔴 Blocked

**ALERT:** 2 consecutive red weeks → Triggering step-x-04
```

---

## Best Practices

### Do's
- ✅ Be honest about status (red weeks are data, not failure)
- ✅ Focus on ONE priority for next week
- ✅ Document blockers with resolution plans
- ✅ Update immediately after completion (don't wait)
- ✅ Use pulse to course-correct early

### Don'ts
- ❌ Skip pulses when behind (most critical time!)
- ❌ List >3 priorities for next week (dilutes focus)
- ❌ Blame external factors without action plan
- ❌ Report green status with hidden problems
- ❌ Ignore repeated blockers (escalate!)
