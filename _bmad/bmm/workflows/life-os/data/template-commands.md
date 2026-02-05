# Template Commands Reference

**Version:** 1.0
**Purpose:** Command-line interface for template management and discovery

---

## Available Commands

### 1. List Templates

**Show current tier (default view):**
```
/templates
```

**Output Example:**
```
📚 Available Templates (Tier 1: Core)

Currently available (6 templates):

1. workflow-plan - Track workflow progress ✅ Used 12x
   Time: ongoing | Category: tracking

2. project-snapshot - Quick project status ✅ Used 10x
   Time: 5 min | Category: tracking

3. project-plan - Comprehensive planning ✅ Used 8x
   Time: 15-30 min | Category: planning

4. project-journal - Daily logging ✅ Used 15x
   Time: 2 min per entry | Category: tracking

5. project-decisions - Decision docs ✅ Used 5x
   Time: 5 min | Category: tracking

6. goals - Annual goal cascade ✅ Used 1x
   Time: 30-60 min initial | Category: planning

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Progress to Tier 2: ██████░░░░ 60% (2/3 workflows)
Next unlock: Complete 1 more workflow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Commands:
  /templates all       - Show all tiers with lock status
  /templates tier2     - Preview Tier 2 templates
  /templates progress  - See unlock roadmap
  /templates load {name} - Load a specific template
```

---

### 2. Show All Templates

**Command:**
```
/templates all
```

**Output Example:**
```
📚 Template Catalog (39 total templates)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 1: Core ✅ UNLOCKED (6 templates)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tracking (4):
  ✅ workflow-plan - Workflow progress tracker (ongoing)
  ✅ project-snapshot - Status snapshot (5 min)
  ✅ project-journal - Daily logging (2 min per entry)
  ✅ project-decisions - Decision documentation (5 min)

Planning (2):
  ✅ project-plan - Comprehensive plan (15-30 min)
  ✅ goals - Annual goal cascade (30-60 min initial)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 2: Intermediate ✅ UNLOCKED (12 templates)
Unlocked: 2026-01-15 (after 3 workflows)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Business (4):
  ✅ business-model-canvas - BMC framework (20-40 min)
  ✅ lean-canvas - Lean validation (15 min)
  ✅ swot - SWOT analysis (10 min)
  ✅ okrs - OKR goals (15 min)

Personal (3):
  ✅ eisenhower-matrix - Priority mgmt (5 min)
  ✅ gtd - Getting Things Done (30 min)
  ✅ pomodoro - Time management (ongoing)

Reviews (3):
  ✅ daily-review - Daily retro (5 min)
  ✅ weekly-review - Weekly planning (15 min)
  ✅ monthly-review - Monthly review (30 min)

TRIZ (2):
  ✅ triz-quick - Quick analysis (10 min)
  ✅ triz-structured - Structured solving (30 min)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 3: Advanced 🔒 LOCKED (15 templates)
Unlock: 10 workflows OR domain-specific usage
Progress: 70% (7/10 workflows)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Finance (6 templates) 🔒
  Need: Use financial analysis
  🔒 npv - Net present value (20 min)
  🔒 dcf - Discounted cash flow (30 min)
  🔒 monte-carlo - Simulation (40 min)
  🔒 capm - Asset pricing (15 min)
  🔒 kelly-criterion - Betting strategy (10 min)
  🔒 real-options - Options valuation (25 min)

Health (6 templates) 🔒
  Need: Use health tracking
  🔒 smart-goals - Health goals (15 min)
  🔒 habit-loop - Habit formation (20 min)
  🔒 macros-tracking - Nutrition (ongoing)
  🔒 progressive-overload - Fitness (20 min)
  🔒 recovery-protocols - Recovery (15 min)
  🔒 health-belief-model - Behavior change (30 min)

Business Advanced (2) 🔒
  Need: 10 workflows
  🔒 porters-five-forces - Competitive analysis (30 min)
  🔒 value-proposition-canvas - Value design (25 min)

Personal Advanced (1) 🔒
  Need: 10 workflows
  🔒 deliberate-practice - Skill mastery (ongoing)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 4: Expert 🔒 LOCKED (6 templates)
Unlock: 25 workflows + mastery signals
Progress: 28% (7/25 workflows)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Mastery Required:
  ✅ Estimate accuracy >= 80% (current: 85%)
  ✅ Speed >= 20% faster (current: 20% faster)
  ○ Consistent usage (need 10 workflows, have 8)
  ○ Advanced techniques (TRIZ/ARIZ/Monte Carlo)

Templates:
  🔒 ariz-full - Complete ARIZ (2-4 hours)
  🔒 atomic-habits - Habit engineering (60 min)
  🔒 growth-mindset - Mindset transformation (45 min)
  🔒 quarterly-review - Strategic retro (60 min)
  🔒 Custom user templates (varies)
  🔒 Multi-domain integration (varies)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Use `/templates progress` for detailed unlock roadmap
Use `/templates tier{N}` to see specific tier details
Use `/templates load {name}` to load a template
```

---

### 3. Show Specific Tier

**Command:**
```
/templates tier2
```

**Output Example:**
```
📚 Tier 2: Intermediate (12 templates)
Status: ✅ UNLOCKED on 2026-01-15
Trigger: Completed 3 workflows

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Business Analysis (4 templates)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. business-model-canvas - BMC framework
   Time: 20-40 min | Difficulty: Intermediate
   Usage: ○ Not used yet
   Description: Strategic planning with 9 building blocks
   [Load template]

2. lean-canvas - Lean startup validation
   Time: 15 min | Difficulty: Intermediate
   Usage: ○ Not used yet
   Description: Rapid business model validation
   [Load template]

3. swot - SWOT analysis
   Time: 10 min | Difficulty: Intermediate
   Usage: ✅ Used 2x (last: 2026-02-03)
   Description: Strengths, weaknesses, opportunities, threats
   [Load template]

4. okrs - OKR goal setting
   Time: 15 min | Difficulty: Intermediate
   Usage: ○ Not used yet
   Description: Objectives and key results framework
   [Load template]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Personal Development (3 templates)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5. eisenhower-matrix - Priority management
   Time: 5 min | Difficulty: Intermediate
   Usage: ✅ Used 4x (last: 2026-02-04)
   Description: Urgent/important prioritization
   [Load template]

6. gtd - Getting Things Done
   Time: 30 min | Difficulty: Intermediate
   Usage: ○ Not used yet
   Description: Complete productivity system
   [Load template]

7. pomodoro - Time management
   Time: ongoing | Difficulty: Intermediate
   Usage: ✅ Used 8x (last: 2026-02-05)
   Description: 25-min focused work sessions
   [Load template]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Review Cycles (3 templates)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8. daily-review - Daily retrospective
   Time: 5 min | Difficulty: Intermediate
   Usage: ○ Not used yet
   Description: Quick daily PDCA check
   [Load template]

9. weekly-review - Weekly planning
   Time: 15 min | Difficulty: Intermediate
   Usage: ✅ Used 3x (last: 2026-02-05)
   Description: Weekly PDCA retrospective
   [Load template]

10. monthly-review - Monthly review
    Time: 30 min | Difficulty: Intermediate
    Usage: ○ Not used yet
    Description: Monthly goals and metrics
    [Load template]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRIZ Problem-Solving (2 templates)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

11. triz-quick - Quick contradiction analysis
    Time: 10 min | Difficulty: Intermediate
    Usage: ✅ Used 3x (last: 2026-02-03)
    Description: Rapid TRIZ problem-solving
    [Load template]

12. triz-structured - Structured TRIZ
    Time: 30 min | Difficulty: Intermediate
    Usage: ○ Not used yet
    Description: Comprehensive contradiction matrix
    [Load template]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Most Used: pomodoro (8x), eisenhower-matrix (4x)
Least Used: 7 templates never used

Suggestion: Try daily-review or gtd next

Use `/templates load {name}` to load a template
```

---

### 4. Show Unlock Progress

**Command:**
```
/templates progress
```

**Output Example:**
```
🎯 Template Unlock Progress

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 1: Core
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: ✅ UNLOCKED (2026-01-01)
Templates: 6 available
Usage: All 6 templates used at least once

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 2: Intermediate
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: ✅ UNLOCKED (2026-01-15)
Trigger: Completed 3 workflows
Templates: 12 available
Usage: 5/12 templates used (42%)

Top 3: pomodoro (8x), eisenhower-matrix (4x), weekly-review (3x)
Never used: 7 templates

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 3: Advanced
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: 🔄 IN PROGRESS (70% complete)
Unlock: 10 workflows OR domain-specific usage

Progress to unlock:
  Base requirement: ███████░░░ 7/10 workflows (70%)
  Need: 3 more workflows

Unlock paths available:
  Path 1: Complete 3 more workflows
    → Unlocks: All 15 Tier 3 templates

  Path 2: Use financial analysis (finance/*)
    → Unlocks: 6 finance templates immediately
    → Action: Try business-model-canvas or swot with financial focus

  Path 3: Use health tracking (health/*)
    → Unlocks: 6 health templates immediately
    → Action: Set health goal in step-00

  Path 4: Advanced TRIZ (ariz-full)
    → Unlocks: When TRIZ used 5+ times
    → Current: 3 TRIZ uses (need 2 more)

Recommended: Complete 3 more workflows (easiest path)
Estimated time: 2-3 days at current pace

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tier 4: Expert
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: 🔒 LOCKED (28% complete)
Unlock: 25 workflows + mastery signals

Progress to unlock:
  Workflows: ███░░░░░░░ 7/25 (28%)
  Estimate accuracy: ✅ 85% (target: >= 80%)
  Speed improvement: ✅ 20% faster (target: >= 20%)
  Consistent usage: 🔄 8/10 workflows (need 2 more in quarter)
  Advanced techniques: ○ Not yet (need TRIZ/ARIZ/Monte Carlo)

Mastery signals breakdown:
  ✅ Accuracy: Achieved (85% within ±20%)
  ✅ Speed: Achieved (avg 20% faster than estimates)
  🔄 Consistency: Almost there (8/10 in Q1)
  ○ Techniques: Try TRIZ 2 more times to unlock ARIZ path

Time to unlock: ~3-4 weeks at current pace
Templates waiting: 6 expert-level templates

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next milestone: Complete 3 workflows → Tier 3 unlocked
Long-term goal: 18 more workflows → Tier 4 unlocked

Keep current pace and quality to unlock all templates!
```

---

### 5. Load Template

**Command:**
```
/templates load workflow-plan
```

**Output Example:**
```
✅ Template loaded: workflow-plan.template.md

Template: Life OS Workflow Plan
Category: Tracking | Tier: 1 (Core)
Estimated time: ongoing
Difficulty: Beginner

Description:
Track workflow progress and status across all Life OS steps.

File created: ./output/workflow-plan-2026-02-05.md

Next steps:
1. Fill in "Idea Summary" section
2. Complete as you progress through workflow
3. Reference in all step files

[Open in editor] [View template guide] [Done]
```

---

### 6. Load Locked Template (Error)

**Command:**
```
/templates load monte-carlo
```

**Output Example:**
```
🔒 Template Locked: monte-carlo.template.md

Template: Monte Carlo Simulation
Category: Finance | Tier: 3 (Advanced)
Estimated time: 40 min
Difficulty: Advanced

Unlock requirements:
  ○ 10 completed workflows (current: 7/10) - 70% there
  ○ Use financial analysis (not yet triggered)

How to unlock:
  Option 1: Complete 3 more workflows (recommended)
  Option 2: Use financial template like business-model-canvas with financial focus

Alternative templates (available now):
  ✅ business-model-canvas - Strategic business planning (Tier 2)
  ✅ swot - SWOT analysis (Tier 2)
  ✅ okrs - OKR goal setting (Tier 2)

These can help with financial planning and are unlocked.

[Use business-model-canvas] [See all alternatives] [Cancel]
```

---

### 7. Recommend Template

**Triggered automatically during workflow:**

**Example 1: Step 08 Deep Plan**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Template Recommendation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For Deep Plan (L1-L6), consider using:

  project-plan.template.md
  Status: ✅ Available (Tier 1)
  Time: 15-30 min

This template helps structure comprehensive planning with
L1-L6 hierarchy, RACI matrix, and quality metrics.

[Load template] [Skip] [Show other options]
```

**Example 2: Step 04 Consilium (Finance Goal Detected)**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Template Recommendation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Detected: Financial/business goal

Recommended template:

  business-model-canvas.template.md
  Status: ✅ Unlocked (Tier 2)
  Time: 20-40 min

This template structures your business model using
9 building blocks for strategic planning.

Using this template will unlock 6 finance templates (Tier 3).

[Load template] [Skip] [Show alternatives]
```

---

## Implementation Notes

### Command Parser

**Location:** `scripts/template-cli.js`

**Usage:**
```javascript
const command = parseTemplateCommand(userInput);

if (command.action === "list") {
  if (command.tier) {
    showTier(command.tier, userContext);
  } else if (command.all) {
    showAllTiers(userContext);
  } else {
    showCurrentTier(userContext);
  }
}

if (command.action === "progress") {
  showUnlockProgress(userContext);
}

if (command.action === "load") {
  loadTemplate(command.templateName, userContext);
}
```

### Integration Points

**Where to trigger recommendations:**
- Step 04: Consilium (detect goal type)
- Step 04.5: TRIZ Analysis (recommend TRIZ templates)
- Step 08: Deep Plan (recommend project-plan)
- Step 09: Complete (show unlock notifications)

**Storage:**
- User context: `user-context:template-usage:{user-id}`
- Recommendations shown: Track to avoid spam

---

**Version:** 1.0
**Last Updated:** 2026-02-05
