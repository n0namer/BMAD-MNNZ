# Template Progressive Unlock System

**Version:** 1.0
**Purpose:** Prevent template overwhelm by starting with 6 core templates and progressively unlocking more based on usage and mastery.

---

## System Overview

**Problem:** 39 templates overwhelm new users, many never used, no guidance on which templates for which situations.

**Solution:** 4-tier progressive unlock system based on usage patterns, workflow completions, and mastery signals.

---

## Tier System

### Tier 1: Core (Always Available)
**Unlock:** Immediately (new users)
**Count:** 6 templates
**Usage:** Fundamental workflows

**Templates:**
1. `workflow-plan.template.md` - Track workflow progress (ongoing)
2. `project-snapshot.template.md` - Current state snapshot (5 min)
3. `project-plan.template.md` - Project planning (15-30 min)
4. `project-journal.template.md` - Daily logging (2 min per entry)
5. `project-decisions.template.md` - Decision documentation (5 min)
6. `goals.template.yaml` - Annual goal cascade (30-60 min initial setup)

**Rationale:** These 6 templates cover 80% of daily workflow needs for new users.

---

### Tier 2: Intermediate
**Unlock Trigger:** 3 completed workflows
**Count:** 12 templates
**Usage:** Deeper analysis and tracking

**Templates:**

**Business Analysis (4 templates):**
- `business/business-model-canvas.template.md` - BMC framework
- `business/lean-canvas.template.md` - Lean startup validation
- `business/swot.template.md` - SWOT analysis
- `business/okrs.template.md` - OKR goal setting

**Personal Development (3 templates):**
- `personal/eisenhower-matrix.template.md` - Priority management
- `personal/gtd.template.md` - Getting Things Done system
- `personal/pomodoro.template.md` - Time management

**Review Cycles (3 templates):**
- `reviews/daily-review.template.md` - Daily retrospective
- `reviews/weekly-review.template.md` - Weekly planning
- `reviews/monthly-review.template.md` - Monthly review

**TRIZ (2 templates):**
- `triz-quick.template.md` - Quick contradiction analysis (10 min)
- `triz-structured.template.md` - Structured problem-solving (30 min)

**Unlock Notification:**
```
🎉 New Templates Unlocked! (Tier 2: Intermediate)

You've completed 3 workflows. These templates are now available:
- business-model-canvas - Strategic planning
- eisenhower-matrix - Priority management
- weekly-review - Weekly retrospectives
- triz-quick - Problem-solving
- [+8 more]

Use `/templates tier2` to see all
```

---

### Tier 3: Advanced
**Unlock Trigger:** 10 workflows + specific usage patterns
**Count:** 15 templates
**Usage:** Specialized analysis and optimization

**Unlock Conditions:**
- **Base:** 10 completed workflows
- **TRIZ path:** Used TRIZ → unlocks `ariz-full.template.md`
- **Finance path:** Used financial analysis → unlocks finance templates
- **Health path:** Used health tracking → unlocks health templates

**Templates:**

**Finance (6 templates):**
- `finance/npv.template.md` - Net present value analysis
- `finance/dcf.template.md` - Discounted cash flow
- `finance/monte-carlo.template.md` - Monte Carlo simulation
- `finance/capm.template.md` - Capital asset pricing
- `finance/kelly-criterion.template.md` - Betting strategy
- `finance/real-options.template.md` - Options analysis

**Health (6 templates):**
- `health/smart-goals.template.md` - Health goal setting
- `health/habit-loop.template.md` - Habit formation
- `health/macros-tracking.template.md` - Nutrition tracking
- `health/progressive-overload.template.md` - Fitness planning
- `health/recovery-protocols.template.md` - Recovery tracking
- `health/health-belief-model.template.md` - Behavior change

**Business Advanced (2 templates):**
- `business/porters-five-forces.template.md` - Competitive analysis
- `business/value-proposition-canvas.template.md` - Value design

**Personal Advanced (1 template):**
- `personal/deliberate-practice.template.md` - Skill mastery

**Unlock Notification:**
```
🚀 Advanced Templates Unlocked! (Tier 3)

Based on your usage patterns:
✅ Used financial analysis → 6 finance templates
✅ Used health tracking → 6 health templates
✅ Completed 10 workflows → 3 business templates

[View all 15 templates]
```

---

### Tier 4: Expert
**Unlock Trigger:** 25 workflows + mastery signals
**Count:** 6 templates
**Usage:** Expert-level analysis and custom workflows

**Mastery Signals:**
- High accuracy (80%+ estimates within ±20%)
- Fast execution (avg 20% faster than estimated)
- Consistent usage (10+ workflows in last quarter)
- Advanced technique usage (TRIZ, ARIZ, Monte Carlo)

**Templates:**

**Expert-Level:**
- `ariz-full.template.md` - Full ARIZ algorithm (2-4 hours)
- `personal/atomic-habits.template.md` - Advanced habit design
- `personal/growth-mindset.template.md` - Mindset transformation
- `reviews/quarterly-review.template.md` - Quarterly retrospective
- Custom workflow templates (user-created)
- Advanced multi-domain integration templates

**Unlock Notification:**
```
🏆 Expert Templates Unlocked! (Tier 4)

Mastery demonstrated:
✅ 25+ workflows completed
✅ 85% estimation accuracy
✅ Consistent advanced technique usage

Expert templates now available:
- ariz-full - Complete ARIZ algorithm
- atomic-habits - Advanced habit engineering
- quarterly-review - Strategic retrospectives
- [+3 more]
```

---

## Usage Tracking

### Memory Storage

**Key:** `user-context:template-usage:{user-id}`

**Structure:**
```yaml
user_template_usage:
  # Core metrics
  total_workflows: 12
  completed_workflows: 10
  workflows_in_last_quarter: 8
  tier_unlocked: 2

  # Template usage
  templates_used:
    workflow-plan:
      count: 12
      last_used: "2026-02-05"
      avg_completion_time: "5min"
    project-snapshot:
      count: 10
      last_used: "2026-02-04"
      avg_completion_time: "3min"
    triz-quick:
      count: 3
      last_used: "2026-02-03"
      avg_completion_time: "12min"

  # Mastery signals
  mastery_signals:
    triz_used: true
    triz_count: 3
    ariz_used: false
    finance_analysis_used: true
    health_tracking_used: false
    batch_mode_used: false
    retrospective_completed: 5
    estimate_accuracy_pct: 85
    avg_speed_vs_estimate: 0.8  # 20% faster

  # Unlock history
  unlock_history:
    - tier: 1
      unlocked_at: "2026-01-01T00:00:00Z"
      trigger: "initial"
    - tier: 2
      unlocked_at: "2026-01-15T10:30:00Z"
      trigger: "3 workflows completed"

  # Notifications shown
  unlock_notifications_shown:
    - "tier2"
```

---

## Template Recommendations

### Context-Aware Suggestions

**When user starts specific workflow steps:**

#### Step 08: Deep Plan
```
💡 Recommended template: project-plan.template.md
Status: 🔓 Available (Tier 1)

This template helps structure comprehensive planning.
Estimated time: 15-30 min

[Load template] [Skip]
```

#### Step 04: Consilium (with financial goal)
```
💡 Recommended template: business-model-canvas.template.md
Status: 🔓 Unlocked (Tier 2)

Detected financial/business goal. This template structures your business model.
Estimated time: 20-40 min

[Load template] [Skip]
```

#### Step 04.5: TRIZ Analysis
```
💡 Recommended template: triz-quick.template.md
Status: 🔓 Unlocked (Tier 2)

Quick contradiction analysis for your problem.
Estimated time: 10 min

Advanced option (locked): ariz-full.template.md
Unlock after: 10 workflows (current: 7/10)

[Load triz-quick] [Skip]
```

### Locked Template Handling

**When template is locked:**
```
💡 Recommended template: monte-carlo.template.md
Status: 🔒 Locked (Tier 3: Advanced)

Unlock requirements:
- 10 completed workflows (current: 7/10)
- Financial analysis usage (not yet used)

Alternative (available now): business-model-canvas.template.md
This covers strategic planning and can help now.

[Use alternative] [See unlock path]
```

---

## Commands

### List Available Templates

**Show current tier:**
```bash
/templates
```

**Output:**
```
📚 Available Templates (Tier 1: Core)

1. workflow-plan - Track workflow progress ✅ Used 12x
2. project-snapshot - Current state (5 min) ✅ Used 10x
3. project-plan - Project planning (15-30 min) ✅ Used 8x
4. project-journal - Daily logging (2 min) ✅ Used 15x
5. project-decisions - Decision docs (5 min) ✅ Used 5x
6. goals - Annual goal cascade (30-60 min) ✅ Used 1x

Progress to Tier 2: ██████░░░░ 60% (2/3 workflows)
Next unlock: 1 more workflow

Use `/templates tier2` to preview locked templates
Use `/templates all` to see full catalog with lock status
```

**Show all tiers:**
```bash
/templates all
```

**Output:**
```
📚 Template Catalog (39 total)

### Tier 1: Core ✅ UNLOCKED (6 templates)
[List of 6 core templates with usage counts]

### Tier 2: Intermediate ✅ UNLOCKED (12 templates)
[List of 12 intermediate templates with usage counts]

### Tier 3: Advanced 🔒 LOCKED (15 templates)
Unlock: 10 workflows (current: 7/10)
[List of 15 advanced templates grayed out]

### Tier 4: Expert 🔒 LOCKED (6 templates)
Unlock: 25 workflows + mastery (current: 7 workflows)
[List of 6 expert templates grayed out]

Use `/templates progress` to see unlock roadmap
```

**Show specific tier:**
```bash
/templates tier2
```

**Output:**
```
📚 Tier 2: Intermediate (12 templates)
Status: ✅ UNLOCKED (unlocked on 2026-01-15)

Business Analysis:
1. business-model-canvas - BMC framework (20-40 min) ○ Not used yet
2. lean-canvas - Lean validation (15 min) ○ Not used yet
3. swot - SWOT analysis (10 min) ✅ Used 2x
4. okrs - OKR goals (15 min) ○ Not used yet

Personal Development:
5. eisenhower-matrix - Priority management (5 min) ✅ Used 4x
6. gtd - Getting Things Done (30 min) ○ Not used yet
7. pomodoro - Time management (ongoing) ✅ Used 8x

Review Cycles:
8. daily-review - Daily retro (5 min) ○ Not used yet
9. weekly-review - Weekly planning (15 min) ✅ Used 3x
10. monthly-review - Monthly review (30 min) ○ Not used yet

TRIZ:
11. triz-quick - Quick analysis (10 min) ✅ Used 3x
12. triz-structured - Structured solving (30 min) ○ Not used yet

Use `/templates load {name}` to load a template
```

### Check Unlock Progress

```bash
/templates progress
```

**Output:**
```
🎯 Template Unlock Progress

Tier 1: Core
✅ UNLOCKED (2026-01-01)
6 templates available

Tier 2: Intermediate
✅ UNLOCKED (2026-01-15)
12 templates available
Trigger: Completed 3 workflows

Tier 3: Advanced
🔄 IN PROGRESS (70% complete)
Unlock requirements:
- 10 workflows: ███████░░░ 7/10 (70%)
- Finance path: ○ Not started
- Health path: ○ Not started
- TRIZ path: ✅ TRIZ used 3x (ARIZ unlockable)

Paths available:
- Complete 3 more workflows → Unlock all Tier 3
- Use financial analysis → Unlock 6 finance templates
- Use health tracking → Unlock 6 health templates

Tier 4: Expert
🔒 LOCKED (28% complete)
Unlock requirements:
- 25 workflows: ███░░░░░░░ 7/25 (28%)
- Estimate accuracy 80%+: ✅ 85% (achieved)
- Speed 20%+ faster: ✅ 20% faster (achieved)
- Consistent usage: ○ 8/10 workflows needed

Next unlock: Complete 3 more workflows → Tier 3
Keep current accuracy and speed → Tier 4 when workflows hit 25
```

---

## Implementation Details

### Update Triggers

**Post-task hook (after workflow completion):**
```javascript
// Check if workflow completed
if (workflow.status === "COMPLETED") {
  // Increment counters
  userContext.completed_workflows += 1;
  userContext.total_workflows += 1;

  // Check unlock conditions
  if (userContext.tier_unlocked === 1 && userContext.completed_workflows >= 3) {
    unlockTier(2);
    showNotification("tier2_unlocked");
  }

  if (userContext.tier_unlocked === 2 && userContext.completed_workflows >= 10) {
    unlockTier(3);
    showNotification("tier3_unlocked");
  }

  // Track template usage
  updateTemplateUsage(workflow.templates_used);

  // Update mastery signals
  updateMasterySignals(workflow);
}
```

**Post-edit hook (after template usage):**
```javascript
// Track which template was used
trackTemplateUsage(template_name, completion_time);

// Update recommendations
updateRecommendations(user_context, current_step);
```

### Notification Timing

**Show unlock notification:**
- After step-09-complete.md (workflow completion)
- Before user sees next workflow selection
- Once per tier (don't spam)

**Notification format:**
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 **Tier {N} Unlocked: {Tier Name}**

You've unlocked {count} new templates!

Highlights:
- {template1} - {benefit}
- {template2} - {benefit}
- {template3} - {benefit}

[View all {count} templates] [Continue workflow]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Benefits

### For New Users
- ✅ Not overwhelmed (6 vs 39 templates)
- ✅ Clear learning path
- ✅ Progressive complexity
- ✅ Discover templates when ready

### For Experienced Users
- ✅ Access to all tools when demonstrated capability
- ✅ Personalized recommendations
- ✅ Usage-based unlocking (not time-based)
- ✅ Expert templates for advanced needs

### For System
- ✅ Higher template adoption (focused set)
- ✅ Better user engagement (unlock motivation)
- ✅ Guided learning path
- ✅ Data-driven improvements (track which templates never unlock)

---

## Future Enhancements

### Phase 2 (After Initial Rollout)
- Custom unlock paths based on domain (finance, health, business, personal)
- Template recommendations based on goal similarity
- Cross-project template reuse suggestions
- Template effectiveness tracking (completion rate, satisfaction)

### Phase 3 (Advanced)
- User-created templates (auto-tier to Tier 4)
- Template mashups (combine multiple templates)
- AI-suggested template creation based on patterns
- Community template sharing (with tier metadata)

---

## Appendix: Complete Template List

### Tier 1: Core (6)
1. workflow-plan.template.md
2. project-snapshot.template.md
3. project-plan.template.md
4. project-journal.template.md
5. project-decisions.template.md
6. goals.template.yaml

### Tier 2: Intermediate (12)
7. business/business-model-canvas.template.md
8. business/lean-canvas.template.md
9. business/swot.template.md
10. business/okrs.template.md
11. personal/eisenhower-matrix.template.md
12. personal/gtd.template.md
13. personal/pomodoro.template.md
14. reviews/daily-review.template.md
15. reviews/weekly-review.template.md
16. reviews/monthly-review.template.md
17. triz-quick.template.md
18. triz-structured.template.md

### Tier 3: Advanced (15)
19. finance/npv.template.md
20. finance/dcf.template.md
21. finance/monte-carlo.template.md
22. finance/capm.template.md
23. finance/kelly-criterion.template.md
24. finance/real-options.template.md
25. health/smart-goals.template.md
26. health/habit-loop.template.md
27. health/macros-tracking.template.md
28. health/progressive-overload.template.md
29. health/recovery-protocols.template.md
30. health/health-belief-model.template.md
31. business/porters-five-forces.template.md
32. business/value-proposition-canvas.template.md
33. personal/deliberate-practice.template.md

### Tier 4: Expert (6)
34. ariz-full.template.md
35. personal/atomic-habits.template.md
36. personal/growth-mindset.template.md
37. reviews/quarterly-review.template.md
38. (Custom user templates)
39. (Advanced multi-domain templates)

---

**Last Updated:** 2026-02-05
**Version:** 1.0
**Status:** Ready for implementation
