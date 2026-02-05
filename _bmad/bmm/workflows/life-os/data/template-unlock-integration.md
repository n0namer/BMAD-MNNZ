# Template Unlock System Integration Guide

**Version:** 1.0
**Purpose:** How to integrate progressive template unlocking with existing Life OS workflow

---

## Integration Points

### 1. Session Start (First Time User)

**File:** `step-00-goals-discovery.md` or session initialization

**Add to beginning:**

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 Welcome to Life OS Templates
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You have access to **6 core templates** to get started:
- workflow-plan - Track your progress (ongoing)
- project-snapshot - Quick status updates (5 min)
- project-plan - Comprehensive planning (15-30 min)
- project-journal - Daily logging (2 min per entry)
- project-decisions - Document key decisions (5 min)
- goals - Annual goal cascade (30-60 min)

✨ More templates unlock as you complete workflows:
  - Tier 2 (12 templates): After 3 workflows
  - Tier 3 (15 templates): After 10 workflows + domain usage
  - Tier 4 (6 templates): After 25 workflows + mastery

Use `/templates` to see available templates anytime.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Implementation:**
```javascript
// Check if first time user
if (!userContext.template_usage || userContext.completed_workflows === 0) {
  showTemplateWelcome();
  initializeTemplateUsage(userContext);
}
```

---

### 2. Step 04: Consilium (Context-Aware Recommendations)

**File:** `steps-c/step-04-consilium.md`

**Add after specialist selection:**

```markdown
## 💡 Template Recommendation

Based on your goal type, consider using:

{{#if goal_type === "finance" || goal_type === "business"}}
  **business-model-canvas.template.md**
  Status: {{#if tier_unlocked >= 2}}✅ Available{{else}}🔒 Unlock after 3 workflows{{/if}}
  Time: 20-40 min | Category: Business | Tier: 2

  This template helps structure your business model using 9 building blocks.

  {{#if tier_unlocked >= 2}}
    [Load template] [Skip]
  {{else}}
    Complete {{3 - completed_workflows}} more workflows to unlock this template.
    Alternative: Use project-plan.template.md (available now)
  {{/if}}
{{/if}}

{{#if goal_type === "health"}}
  **smart-goals.template.md**
  Status: {{#if tier_unlocked >= 3}}✅ Available{{else}}🔒 Unlock after 10 workflows{{/if}}
  Time: 15 min | Category: Health | Tier: 3

  SMART framework specifically for health goals.

  {{#if tier_unlocked >= 3}}
    [Load template] [Skip]
  {{else}}
    Alternative: Use goals.template.yaml (available now) for any goal type
  {{/if}}
{{/if}}

{{#if goal_type === "personal"}}
  **eisenhower-matrix.template.md**
  Status: {{#if tier_unlocked >= 2}}✅ Available{{else}}🔒 Unlock after 3 workflows{{/if}}
  Time: 5 min | Category: Personal | Tier: 2

  Priority management for personal goals.

  {{#if tier_unlocked >= 2}}
    [Load template] [Skip]
  {{else}}
    Complete {{3 - completed_workflows}} more workflows to unlock.
  {{/if}}
{{/if}}
```

**Implementation:**
```javascript
function recommendTemplate(goalType, userContext) {
  const recommendations = {
    finance: "business-model-canvas",
    business: "business-model-canvas",
    health: tier >= 3 ? "smart-goals" : "goals",
    personal: tier >= 2 ? "eisenhower-matrix" : "goals"
  };

  const template = recommendations[goalType] || "project-plan";
  return {
    template,
    available: checkTemplateAvailable(template, userContext),
    alternative: getAlternativeTemplate(template, userContext)
  };
}
```

---

### 3. Step 04.5: TRIZ Analysis (TRIZ Template Recommendations)

**File:** `steps-c/step-04.5-triz-analysis.md`

**Add before TRIZ execution:**

```markdown
## 💡 TRIZ Template Options

Choose your TRIZ approach:

### Option 1: Quick TRIZ (Recommended for first time)
**Template:** triz-quick.template.md
Status: {{#if tier_unlocked >= 2}}✅ Available{{else}}🔒 Unlock after 3 workflows{{/if}}
Time: 10 min | Difficulty: Intermediate

Quick contradiction analysis with 3-5 inventive principles.

{{#if tier_unlocked >= 2}}
  [Use triz-quick] [Learn more]
{{else}}
  Complete {{3 - completed_workflows}} more workflows to unlock.
  For now, use manual TRIZ process described below.
{{/if}}

### Option 2: Structured TRIZ
**Template:** triz-structured.template.md
Status: {{#if tier_unlocked >= 2}}✅ Available{{else}}🔒 Unlock after 3 workflows{{/if}}
Time: 30 min | Difficulty: Intermediate

Comprehensive TRIZ with full contradiction matrix.

{{#if tier_unlocked >= 2}}
  [Use triz-structured] [Learn more]
{{/if}}

### Option 3: Full ARIZ (Expert)
**Template:** ariz-full.template.md
Status: {{#if tier_unlocked >= 4}}✅ Available{{else}}🔒 Unlock after 25 workflows + mastery{{/if}}
Time: 2-4 hours | Difficulty: Expert

Complete ARIZ algorithm for complex problems.

{{#if tier_unlocked >= 4}}
  [Use ariz-full] [Learn more]
{{else}}
  Unlock path: Complete 25 workflows with high mastery signals
  Current: {{completed_workflows}}/25 workflows
{{/if}}

---

{{#if tier_unlocked < 2}}
**Manual TRIZ Process (No template):**
Continue with the guided TRIZ process below...
{{/if}}
```

**Implementation:**
```javascript
// Track TRIZ usage for tier unlocking
function trackTRIZUsage(trizType, userContext) {
  userContext.triz_count = (userContext.triz_count || 0) + 1;

  // TRIZ used 5+ times → unlocks ARIZ path
  if (userContext.triz_count >= 5 && userContext.completed_workflows >= 10) {
    unlockTemplate("ariz-full", userContext);
  }
}
```

---

### 4. Step 08: Deep Plan (Project Plan Template)

**File:** `steps-c/step-08-deep-plan.md`

**Add at the beginning:**

```markdown
## 💡 Template Recommendation: Deep Plan

**Recommended:** project-plan.template.md
Status: ✅ Available (Tier 1: Core)
Time: 15-30 min | Difficulty: Beginner

This template provides:
- L1-L6 deep plan structure
- RACI matrix for L2 areas
- Plan quality metrics
- If-then action planning

{{#if user_has_used_project_plan}}
  You've used this template {{usage_count}}x before.
  [Load previous plan] [Create new plan] [Skip template]
{{else}}
  **First time using this template?**
  It will help structure your deep plan with best practices.
  [Load template] [Skip and use manual process]
{{/if}}

---

{{#if template_choice === "manual"}}
**Manual Deep Plan Process:**
Continue with the guided deep plan below...
{{/if}}
```

---

### 5. Step 09: Complete (Unlock Notifications)

**File:** `steps-v/step-09-complete.md`

**Add after workflow completion:**

```markdown
## ✅ Workflow Complete

{{workflow_summary}}

---

{{#if completed_workflows === 3 && tier_unlocked === 1}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 **Tier 2 Unlocked: Intermediate Templates**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Congratulations! You've completed 3 workflows.
**12 new templates** are now available:

**Business Analysis (4):**
- business-model-canvas - Strategic planning (20-40 min)
- lean-canvas - Lean startup validation (15 min)
- swot - SWOT analysis (10 min)
- okrs - OKR goal setting (15 min)

**Personal Development (3):**
- eisenhower-matrix - Priority management (5 min)
- gtd - Getting Things Done (30 min)
- pomodoro - Time management (ongoing)

**Review Cycles (3):**
- daily-review - Daily retrospective (5 min)
- weekly-review - Weekly planning (15 min)
- monthly-review - Monthly review (30 min)

**TRIZ Problem-Solving (2):**
- triz-quick - Quick analysis (10 min)
- triz-structured - Structured solving (30 min)

Use `/templates tier2` to explore all new templates.

**Next milestone:** Complete 10 workflows to unlock Tier 3 (15 advanced templates)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{{/if}}

{{#if completed_workflows === 10 && tier_unlocked === 2}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 **Tier 3 Unlocked: Advanced Templates**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Excellent progress! You've completed 10 workflows.
**15 advanced templates** are now available:

**Finance (6 templates):**
- npv, dcf, monte-carlo, capm, kelly-criterion, real-options

**Health (6 templates):**
- smart-goals, habit-loop, macros-tracking, progressive-overload,
  recovery-protocols, health-belief-model

**Business Advanced (2):**
- porters-five-forces, value-proposition-canvas

**Personal Advanced (1):**
- deliberate-practice

Use `/templates tier3` to explore all advanced templates.

**Next milestone:** Complete 25 workflows with mastery to unlock Tier 4 (6 expert templates)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{{/if}}

{{#if completed_workflows === 25 && mastery_achieved}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 **Tier 4 Unlocked: Expert Templates**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Outstanding! You've achieved mastery level.
**6 expert templates** are now available:

**Mastery Achieved:**
✅ 25+ workflows completed
✅ Estimation accuracy: {{estimate_accuracy}}%
✅ Speed improvement: {{speed_improvement}}%
✅ Advanced technique usage

**Expert Templates:**
- ariz-full - Complete ARIZ algorithm (2-4 hours)
- atomic-habits - Advanced habit engineering (60 min)
- growth-mindset - Mindset transformation (45 min)
- quarterly-review - Strategic retrospective (60 min)
- Custom user templates
- Multi-domain integration

Use `/templates tier4` to explore all expert templates.

You now have access to **all 39 templates**. Congratulations!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{{/if}}
```

**Implementation:**
```javascript
function checkUnlockNotification(userContext) {
  const { completed_workflows, tier_unlocked } = userContext;

  // Tier 2 unlock
  if (completed_workflows === 3 && tier_unlocked === 1) {
    unlockTier(2, userContext);
    return "tier2_unlocked";
  }

  // Tier 3 unlock
  if (completed_workflows === 10 && tier_unlocked === 2) {
    unlockTier(3, userContext);
    return "tier3_unlocked";
  }

  // Tier 4 unlock
  if (completed_workflows >= 25 && tier_unlocked === 3 && checkMastery(userContext)) {
    unlockTier(4, userContext);
    return "tier4_unlocked";
  }

  return null;
}
```

---

### 6. Review Templates (Auto-Suggest Based on Schedule)

**Trigger:** Time-based or workflow stage

**Weekly Review (Monday mornings):**
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Weekly Review Time
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

It's Monday morning. Time for your weekly review!

{{#if tier_unlocked >= 2}}
  **Recommended:** weekly-review.template.md
  Status: ✅ Available (Tier 2)
  Time: 15 min

  PDCA retrospective with goal tracking.

  [Start weekly review] [Skip this week]
{{else}}
  **Weekly reviews unlock after 3 workflows.**
  Current: {{completed_workflows}}/3

  For now, manually review your goals from goals.template.yaml

  [View goals] [Skip]
{{/if}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Monthly Review (1st of month):**
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Monthly Review Time
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

New month! Time for monthly review.

{{#if tier_unlocked >= 2}}
  **Recommended:** monthly-review.template.md
  Status: ✅ Available (Tier 2)
  Time: 30 min

  Review last month's progress and plan ahead.

  [Start monthly review] [Skip this month]
{{else}}
  Monthly reviews unlock after 3 workflows.
{{/if}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Quarterly Review (1st of Q2/Q3/Q4):**
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 Quarterly Review Time
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

New quarter! Time for strategic retrospective.

{{#if tier_unlocked >= 4}}
  **Recommended:** quarterly-review.template.md
  Status: ✅ Available (Tier 4)
  Time: 60 min

  Strategic quarterly retrospective with deep analysis.

  [Start quarterly review] [Skip this quarter]
{{else}}
  Quarterly reviews unlock at Tier 4 (25 workflows + mastery).
  Current: {{completed_workflows}}/25

  Alternative: Use monthly-review.template.md ({{tier_unlocked >= 2 ? "available" : "unlock after 3 workflows"}})

  {{#if tier_unlocked >= 2}}
    [Use monthly review instead] [Skip]
  {{/if}}
{{/if}}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Memory Storage Integration

### User Context Structure

**Storage Key:** `user-context:template-usage:{user-id}`

```yaml
template_usage:
  # Core metrics
  total_workflows: 12
  completed_workflows: 10
  workflows_last_quarter: 8
  tier_unlocked: 2
  tier_unlock_history:
    - tier: 1
      date: "2026-01-01T00:00:00Z"
      trigger: "initial"
    - tier: 2
      date: "2026-01-15T10:30:00Z"
      trigger: "3 workflows completed"

  # Template usage tracking
  templates_used:
    workflow-plan:
      count: 12
      last_used: "2026-02-05T09:00:00Z"
      avg_time_minutes: 5
    project-plan:
      count: 8
      last_used: "2026-02-04T14:30:00Z"
      avg_time_minutes: 25
    triz-quick:
      count: 3
      last_used: "2026-02-03T11:00:00Z"
      avg_time_minutes: 12

  # Mastery signals
  mastery:
    estimate_accuracy_pct: 85
    avg_speed_multiplier: 0.8  # 20% faster
    triz_count: 3
    ariz_count: 0
    finance_analysis_used: false
    health_tracking_used: false

  # Unlock notifications shown
  notifications_shown:
    - "tier2_unlocked"

  # Recommendations declined
  declined_recommendations:
    - template: "business-model-canvas"
      date: "2026-02-03"
      reason: "not_now"
```

### Update Hooks

**Post-task hook (after workflow completion):**
```javascript
hooks.post_task = function(workflow, userContext) {
  // Increment counters
  userContext.completed_workflows += 1;
  userContext.total_workflows += 1;

  // Check tier unlocks
  checkTierUnlock(userContext);

  // Update template usage if template was used
  if (workflow.template_used) {
    updateTemplateUsage(workflow.template_used, workflow.time_spent, userContext);
  }

  // Update mastery signals
  updateMasterySignals(workflow, userContext);

  // Save to memory
  saveUserContext(userContext);
};
```

**Post-edit hook (after template file edited):**
```javascript
hooks.post_edit = function(file, userContext) {
  // Check if file is a template output
  const template = detectTemplate(file);

  if (template) {
    trackTemplateUsage(template.name, userContext);
  }
};
```

---

## Quick Implementation Checklist

- [x] Create `data/template-unlock-system.md` (system documentation)
- [x] Create `data/template-tier-mapping.yaml` (tier classifications)
- [x] Create `data/template-commands.md` (CLI reference)
- [x] Create `data/template-unlock-integration.md` (this file)
- [ ] Update Tier 1 templates with tier metadata (6 templates) - IN PROGRESS
- [ ] Update Tier 2 templates with tier metadata (12 templates) - PARTIAL
- [ ] Update Tier 3 templates with tier metadata (15 templates)
- [ ] Update Tier 4 templates with tier metadata (6 templates)
- [ ] Add template recommendations to step-04-consilium.md
- [ ] Add template recommendations to step-04.5-triz-analysis.md
- [ ] Add template recommendations to step-08-deep-plan.md
- [ ] Add unlock notifications to step-09-complete.md
- [ ] Implement `/templates` command handler
- [ ] Implement tier unlock logic in post-task hook
- [ ] Implement template usage tracking
- [ ] Implement mastery signal calculation
- [ ] Test end-to-end workflow with unlocking

---

**Version:** 1.0
**Last Updated:** 2026-02-05
**Status:** Integration guide complete, implementation in progress
