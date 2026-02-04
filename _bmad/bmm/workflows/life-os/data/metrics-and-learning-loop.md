---
document: metrics-and-learning-loop
version: 1.0
phase: 4
purpose: Track Life OS effectiveness and continuously improve through data
integration: Claude Flow Memory + post-project feedback
---

# Life OS Metrics & Learning Loop

**Phase:** 4 (Full Ecosystem)
**Status:** Implementation Ready

---

## 1. Metrics Overview

**What we measure:**

1. **Workflow Metrics** - Completion rates, time investment, step effectiveness
2. **Framework Metrics** - Usage frequency, effectiveness ratings, ROI
3. **Success Metrics** - Project completion, goal achievement, user satisfaction
4. **System Metrics** - Auto-suggest accuracy, memory usage, performance

**Why we measure:**

- Improve auto-suggest algorithm (which frameworks to recommend when)
- Identify most/least effective frameworks (focus improvements)
- Optimize workflow steps (reduce time, increase value)
- Personalize experience (learn user preferences)

---

## 2. Data Collection Points

### 2.1 Workflow Step Completion

**Tracked automatically after each step:**

```yaml
step_metrics:
  step_01_collect_ideas:
    started: {timestamp}
    completed: {timestamp}
    duration_minutes: {calculated}
    domain_detected: {Business|Finance|Health|Personal}
    design_thinking_used: true
    empathy_scores:
      - who_benefits: {confidence 1-10}
      - pain_solved: {clarity 1-10}
      - why_now: {urgency 1-10}

  step_02_roles_discovery:
    started: {timestamp}
    completed: {timestamp}
    duration_minutes: {calculated}
    roles_assigned: {count}
    domains_covered: [{list}]
    frameworks_matched: [{list}]

  step_03_specialist_match:
    started: {timestamp}
    completed: {timestamp}
    duration_minutes: {calculated}
    domain_primary: {name}
    frameworks_shortlisted: [{list}]
    tier_distribution: {tier_1: N, tier_2: N, tier_3: N}

  step_04_consilium:
    started: {timestamp}
    completed: {timestamp}
    duration_minutes: {calculated}
    mode: {Lite|Deep}
    specialists_count: {N}
    divergence_percent: {%}
    six_hats_distribution: {hat_counts}
    consensus_strength: {weak|moderate|strong}
    triz_triggered: {true|false}
    scamper_used: {true|false}

  step_04_5_triz_analysis:
    started: {timestamp}
    completed: {timestamp}
    duration_minutes: {calculated}
    trigger_reason: {divergence|scoring_conflict|user_request}
    mode: {Quick|Structured|Full_ARIZ}
    contradictions_found: {count}
    principles_applied: [{list}]
    resolution_confidence: {1-10}

  step_05_scoring:
    started: {timestamp}
    completed: {timestamp}
    duration_minutes: {calculated}
    mcda_total_score: {X/10}
    stage_gate_result: {PASS|CONDITIONAL|FAIL}
    domain_criteria_used: [{list}]
    scoring_conflicts_detected: {count}
    override_applied: {true|false}
    override_reason: {text|null}

  step_06_integration:
    started: {timestamp}
    completed: {timestamp}
    duration_minutes: {calculated}
    portfolio_slot_assigned: {true|false}
    wip_limit_status: {within|at_limit|exceeded}
    strategic_bucket: {name}

  step_07_calendar_sync:
    started: {timestamp}
    completed: {timestamp}
    duration_minutes: {calculated}
    time_blocks_created: {count}
    weekly_hours_allocated: {N}
    conflicts_detected: {count}
    conflicts_resolved: {count}

  step_08_deep_plan:
    started: {timestamp}
    completed: {timestamp}
    duration_minutes: {calculated}
    levels_created: {L1-L6}
    l2_phases_count: {N}
    l3_milestones_count: {N}
    l4_tasks_count: {N}
    l5_subtasks_count: {N}
    l6_checklists_count: {N}
    quality_gate_score: {X}/7
    triz_used_for_planning: {true|false}

  step_09_complete:
    started: {timestamp}
    completed: {timestamp}
    duration_minutes: {calculated}
    snapshot_created: {true|false}
    journal_initialized: {true|false}
    execution_ready: {true|false}
```

**Storage after each step:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:metrics:steps:{project_id}:{step_id}" \
  --content "{step_metrics_json}"
```

---

### 2.2 Framework Usage Tracking

**Per-framework metrics collected after template completion:**

```yaml
framework_usage:
  framework_name: {OKRs|TRIZ|NPV|Pomodoro|etc}
  framework_tier: {1|2|3}
  project_id: {id}
  domain: {Business|Finance|Health|Personal}
  suggested_by: {auto-suggest|consilium|user-selected|not-suggested}
  suggestion_confidence: {0-1 if auto-suggested}
  suggestion_trigger: {keyword|divergence|scoring_conflict|synergy|none}
  user_accepted: {true|false}
  time_invested_minutes: {X}
  completed: {true|false}
  abandoned_at_step: {step_name|null}
  effectiveness_rating: {1-5 stars}
  user_comment: {optional text}
  roi_perception: {High|Medium|Low|Negative}
  would_use_again: {true|false}
  synergy_frameworks: [{if used with others}]
  synergy_effectiveness: {1-5 stars|null}
  breakthrough_achieved: {true|false}
  breakthrough_description: {text|null}
```

**Collection trigger:** After framework template completed or abandoned.

**Feedback prompt to user:**

```
--- Framework Feedback ---

{Framework Name} analysis complete!

Quick feedback (30 seconds):

1. How helpful was {Framework Name}?
   [5] Breakthrough insight
   [4] Very helpful
   [3] Moderately helpful
   [2] Slightly helpful
   [1] Not helpful

2. Time investment: {X} min - Was it worth it?
   [Good ROI]  [Okay]  [Too much time]

3. Would you use {Framework} again for similar projects?
   [Yes] [Maybe] [No]

4. (Optional) Any specific insight or comment?
   ___

[Submit Feedback] [Skip]
```

**Storage:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:metrics:framework:{project_id}:{framework_name}" \
  --content "{framework_usage_json}"
```

---

### 2.3 Project Outcome Tracking

**Post-completion metrics (from Project Snapshot template):**

```yaml
project_outcome:
  project_id: {id}
  project_name: {name}
  domain: {primary domain}
  started_date: {date}
  completed_date: {date}
  duration_weeks: {actual}
  estimated_duration_weeks: {from deep plan}
  duration_accuracy_percent: {actual/estimated * 100}
  completion_status: {Completed|Abandoned|On_Hold|Pivoted}
  goal_achieved: {true|false|partial}

  success_metrics:
    - metric: {name}
      baseline: {value}
      target: {value}
      actual: {value}
      achievement_percent: {%}

  frameworks_used: [{list}]
  frameworks_count: {N}
  most_valuable_framework: {name}
  least_valuable_framework: {name}

  workflow_steps_completed: {count}/{total}
  steps_skipped: [{list}]
  bottleneck_step: {step_name|null}

  deep_plan_adherence: {High|Medium|Low}
  scope_changes: {count}
  scope_change_reasons: [{list}]

  would_recommend_workflow: {true|false}
  overall_satisfaction: {1-10}
  key_learning: {text}
  improvement_suggestion: {text|null}
```

**Collection trigger:** When user completes Step 09 or explicitly marks project as done/abandoned.

**Storage:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:metrics:outcome:{project_id}" \
  --content "{project_outcome_json}"
```

---

### 2.4 Auto-Suggest Performance Tracking

**Per suggestion event tracked:**

```yaml
auto_suggest_event:
  event_id: {uuid}
  timestamp: {date}
  project_id: {id}
  step: {step_number}
  trigger_type: {keyword|consilium_divergence|scoring_conflict|synergy_detected|domain_match}
  trigger_detail: {specific trigger description}

  frameworks_suggested:
    - name: {framework}
      confidence: {0-1}
      rank: {1|2|3}
  top_suggestion: {framework}
  top_confidence: {0-1}

  user_action: {accepted|declined|tell_me_more|skip|accepted_alternative}
  accepted_framework: {name|null}
  time_to_decide_seconds: {N}

  if_accepted:
    effectiveness_rating: {1-5 stars after use}
    confidence_vs_effectiveness_delta: {confidence - normalized_rating}
    correct_suggestion: {true if rating >= 3.5}
```

**Storage:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:metrics:autosuggest:{event_id}" \
  --content "{auto_suggest_event_json}"
```

---

### 2.5 Execution Phase Metrics

**Tracked during steps-e (execution workflow):**

```yaml
execution_metrics:
  project_id: {id}
  update_count: {N}
  rescoring_count: {N}
  rescoring_results: [{old_score, new_score, reason}]
  deep_plan_revisions: {count}
  milestone_completion_rate: {%}
  tasks_completed_on_time: {%}
  blockers_encountered: [{description, resolution, days_blocked}]
  pivot_occurred: {true|false}
  kill_decision_evaluated: {true|false}
  kill_decision_result: {Continue|Pivot|Kill|null}
```

---

### 2.6 Review Phase Metrics

**Tracked during steps-v (validation/review workflow):**

```yaml
review_metrics:
  review_type: {daily|weekly|monthly}
  timestamp: {date}
  projects_reviewed: {count}
  portfolio_health_score: {1-10}
  wip_compliance: {true|false}
  projects_at_risk: [{project_id, risk_reason}]
  actions_taken: [{action, project_id}]
  time_spent_minutes: {N}
```

---

## 3. Metrics Dashboard

### 3.1 Workflow Health

**System-wide dashboard showing step-level performance:**

```
-- Life OS Workflow Health (Last 30 days) --

Projects Started: {N}
Projects Completed: {N} ({%} completion rate)
Avg Time per Project: {X} hours
Most Common Domain: {domain} ({%})

Step Completion Rates:
  Step 01 (Collect Ideas):     {%}
  Step 02 (Roles Discovery):   {%}
  Step 03 (Specialist Match):  {%}
  Step 04 (Consilium):         {%}
  Step 04.5 (TRIZ Analysis):   {%} (when triggered)
  Step 05 (Scoring):           {%}
  Step 06 (Integration):       {%}
  Step 07 (Calendar Sync):     {%}
  Step 08 (Deep Plan):         {%}
  Step 09 (Complete):          {%}

Bottleneck Detection:
  Lowest completion: Step {N} ({step_name}) at {%}
  Longest avg duration: Step {N} ({step_name}) at {X} min
  Most skipped: Step {N} ({step_name}) - {count} times

Drop-off Analysis:
  Projects abandoned at Step 01-03: {%} (early stage)
  Projects abandoned at Step 04-05: {%} (analysis paralysis)
  Projects abandoned at Step 06-07: {%} (capacity issues)
  Projects abandoned at Step 08-09: {%} (planning fatigue)
```

**Interpretation guide:**

| Completion Rate | Assessment | Action |
|-----------------|------------|--------|
| >= 90%          | Healthy    | No action needed |
| 75-89%          | Moderate   | Monitor, gather feedback |
| 60-74%          | Concerning | Investigate bottleneck, simplify step |
| < 60%           | Critical   | Redesign step, make optional, or merge |

---

### 3.2 Framework Effectiveness Rankings

**Per-domain effectiveness with acceptance and satisfaction metrics:**

```
-- Framework Effectiveness Ranking --

BUSINESS DOMAIN:
  Rank | Framework           | Avg Rating | Acceptance | Would Reuse
  1    | OKRs                | 4.7        | 92%        | 87%
  2    | Lean Canvas         | 4.5        | 88%        | 84%
  3    | SWOT                | 4.2        | 84%        | 79%
  4    | Porter Five Forces  | 4.0        | 71%        | 68%
  5    | BCG Matrix          | 3.8        | 65%        | 61%

FINANCE DOMAIN:
  Rank | Framework           | Avg Rating | Acceptance | Would Reuse
  1    | NPV                 | 4.8        | 96%        | 93%
  2    | Monte Carlo Sim     | 4.4        | 76%        | 72%
  3    | DCF                 | 4.1        | 72%        | 68%
  4    | Real Options        | 3.9        | 58%        | 55%
  5    | Unit Economics      | 4.3        | 82%        | 78%

HEALTH DOMAIN:
  Rank | Framework           | Avg Rating | Acceptance | Would Reuse
  1    | Habit Loop          | 4.6        | 91%        | 88%
  2    | Progressive Overload| 4.5        | 85%        | 82%
  3    | Health Belief Model  | 4.3        | 78%        | 74%
  4    | Deliberate Practice | 4.2        | 74%        | 71%
  5    | Periodization       | 4.0        | 68%        | 65%

PERSONAL DEVELOPMENT:
  Rank | Framework           | Avg Rating | Acceptance | Would Reuse
  1    | Pomodoro            | 4.7        | 92%        | 90%
  2    | Atomic Habits       | 4.6        | 92%        | 88%
  3    | Eisenhower Matrix   | 4.4        | 88%        | 84%
  4    | Getting Things Done | 4.3        | 82%        | 78%
  5    | Feynman Technique   | 4.1        | 75%        | 72%

UNIVERSAL METHODS:
  Rank | Framework           | Avg Rating | Acceptance | Context
  1    | Design Thinking     | 4.8        | 100% (embedded) | Step 01
  2    | Six Thinking Hats   | 4.5        | 100% (embedded) | Step 04
  3    | TRIZ Quick          | 4.3        | 67%        | When suggested
  4    | TRIZ Structured     | 4.7        | 45%        | High barrier
  5    | SCAMPER             | 4.1        | 72%        | Step 04 option
  6    | Full ARIZ           | 4.9        | 22%        | Very high barrier
```

**Key insight pattern:** Frameworks with low acceptance but high satisfaction (TRIZ Structured, ARIZ) indicate an onboarding problem, not a quality problem. Action: improve introductions and lower perceived complexity.

---

### 3.3 Auto-Suggest Accuracy Dashboard

```
-- Auto-Suggest Performance (Last 30 days) --

Total Suggestions Made: {N}
Accepted: {N} ({%} acceptance rate)       Target: >= 60%
Effectiveness of Accepted: {X} avg       Target: >= 4.0

Confidence Calibration:
  High Conf (>= 85%):  {X} avg effectiveness   | {%} acceptance
  Medium Conf (70-84%): {X} avg effectiveness   | {%} acceptance
  Low Conf (< 70%):    {X} avg effectiveness    | {%} acceptance

False Positives (rated <= 2 stars): {N} ({%})   Target: < 20%
False Negatives (user found better): {N} ({%})  Target: < 15%

Trigger Performance:
  Trigger Type               | Suggestions | Accepted | Avg Rating
  Consilium Divergence >= 40%| {N}         | {%}      | {X}
  Keyword Match (high conf)  | {N}         | {%}      | {X}
  Scoring Conflict           | {N}         | {%}      | {X}
  Synergy Detection          | {N}         | {%}      | {X}
  Domain Default             | {N}         | {%}      | {X}

Confidence-Effectiveness Correlation: R^2 = {value}   Target: >= 0.70
```

**Calibration check:**

| Confidence Bucket | Expected Effectiveness | Actual | Status |
|-------------------|----------------------|--------|--------|
| 90-100%           | >= 4.5 stars          | {X}    | {OK/Overconfident/Underconfident} |
| 80-89%            | >= 4.0 stars          | {X}    | {OK/Overconfident/Underconfident} |
| 70-79%            | >= 3.5 stars          | {X}    | {OK/Overconfident/Underconfident} |
| 60-69%            | >= 3.0 stars          | {X}    | {OK/Overconfident/Underconfident} |

If overconfident in a bucket: reduce base confidence for that range by 5%.
If underconfident: increase by 3%.

---

### 3.4 Synergy Discovery Map

**Tracking which framework combinations work best together:**

```
-- Framework Synergy Rankings (by combined effectiveness) --

Top 10 Combinations:

Rank | Combination                    | Avg Rating | Usage Count | Pattern
1    | TRIZ + Business Model Canvas   | 4.9        | {N}         | TRIZ resolves contradiction, BMC structures solution
2    | Pomodoro + Deliberate Practice  | 4.8        | {N}         | Pomodoro structures time, DP fills blocks
3    | NPV + Monte Carlo Simulation   | 4.7        | {N}         | NPV calculates value, MC quantifies risk
4    | Atomic Habits + Health Belief   | 4.6        | {N}         | HBM assesses readiness, AH implements
5    | OKRs + Eisenhower Matrix       | 4.6        | {N}         | OKRs set direction, Eisenhower prioritizes daily
6    | Lean Canvas + SWOT             | 4.5        | {N}         | SWOT informs Canvas assumptions
7    | DCF + Real Options             | 4.5        | {N}         | DCF baseline, RO captures flexibility value
8    | Progressive Overload + Period. | 4.4        | {N}         | PO sets principles, Periodization plans cycles
9    | GTD + Pomodoro                 | 4.4        | {N}         | GTD captures/organizes, Pomodoro executes
10   | Design Thinking + TRIZ Quick   | 4.3        | {N}         | DT defines problem, TRIZ resolves constraints

Synergy Threshold: Combinations with >= 4.5 avg and >= 5 uses
  get added to auto-suggest as recommended pairings.
```

**Negative synergies (combinations that waste time):**

```
Anti-Synergies (avg rating < 3.0 when combined):

  Combination                    | Avg Rating | Issue
  ARIZ + Quick TRIZ              | 2.8        | Redundant - full ARIZ includes quick analysis
  NPV + Unit Economics           | 2.9        | Overlapping financial analysis, confuses users
  Multiple Tier 3 frameworks     | 2.5        | Complexity overload, diminishing returns
```

---

## 4. Learning Loop Implementation

### 4.1 Monthly Learning Loop

**Automated monthly analysis process (1st of each month):**

```
Monthly Learning Loop - Process Flow

INPUT:
  - All step_metrics from past 30 days
  - All framework_usage from past 30 days
  - All project_outcomes from past 30 days
  - All auto_suggest_events from past 30 days

STEP 1: Calculate KPIs

  kpis:
    projects_started: count(projects where started in period)
    projects_completed: count(projects where completed in period)
    completion_rate: projects_completed / projects_started
    avg_time_per_project: mean(project.total_duration_hours)
    domain_distribution: group_count(projects by domain)
    framework_ratings: mean(framework_usage.effectiveness_rating) per framework
    auto_suggest_accuracy: count(accepted AND rating >= 3.5) / count(suggestions)
    user_satisfaction: mean(project_outcome.overall_satisfaction)

STEP 2: Identify Patterns

  patterns:
    bottleneck_steps: steps where completion_rate < 80%
    low_rated_frameworks: frameworks where avg_rating < 3.5
    high_rated_frameworks: frameworks where avg_rating >= 4.5
    high_synergy_pairs: pairs where combined_rating >= 4.5 AND usage >= 5
    negative_synergy_pairs: pairs where combined_rating < 3.0
    trigger_accuracy: per trigger, acceptance_rate AND effectiveness
    drop_off_points: steps where most abandonments occur
    time_estimate_accuracy: actual_duration vs estimated_duration correlation

STEP 3: Generate Recommendations

  For each bottleneck_step:
    - IF completion_rate < 60%: recommend redesign or make optional
    - IF completion_rate 60-80%: recommend simplification or better guidance
    - IF avg_duration > 2x median: recommend time optimization

  For each low_rated_framework:
    - IF acceptance_rate also low: consider removing from auto-suggest
    - IF acceptance_rate high but rating low: improve template quality
    - IF used < 5 times: insufficient data, continue monitoring

  For each trigger_type:
    - IF acceptance_rate < 50%: reduce trigger weight by 10%
    - IF acceptance_rate > 80%: increase trigger weight by 5%
    - IF accuracy < 60%: investigate trigger logic

STEP 4: Update System Parameters

  Updates applied:
    - framework.base_confidence adjusted per rating trends
    - trigger.weight adjusted per accuracy
    - synergy_boost added for confirmed high-synergy pairs
    - anti_synergy_penalty added for confirmed negative pairs
    - step time estimates updated from actual data

STEP 5: Store Report

  Store monthly report to global memory for cross-session access.
```

**Storage:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:metrics:monthly:{year}-{month}" \
  --content "{monthly_report_json}"
```

---

### 4.2 Algorithm Update Rules

**Framework Base Confidence Adjustments:**

```
Rule 1: Rating-Based Adjustment
  IF framework.avg_rating_30d >= 4.5 AND usage_count >= 10:
    framework.base_confidence += 0.02 (cap at 0.95)

  IF framework.avg_rating_30d <= 3.0 AND usage_count >= 5:
    framework.base_confidence -= 0.03 (floor at 0.30)

  IF framework.avg_rating_30d between 3.0 and 4.5:
    No change (stable range)

Rule 2: Acceptance-Based Adjustment
  IF framework.acceptance_rate_30d > 80%:
    framework.suggestion_priority += 1

  IF framework.acceptance_rate_30d < 40%:
    framework.suggestion_priority -= 1
    IF consecutive_months_below_40 >= 3:
      flag for review (possible removal from auto-suggest)

Rule 3: Trend-Based Adjustment
  IF framework.avg_rating trending DOWN for 3 consecutive months:
    alert("Framework {name} declining - investigate template quality")

  IF framework.avg_rating trending UP for 3 consecutive months:
    alert("Framework {name} improving - consider promoting to higher tier")
```

**Trigger Weight Adjustments:**

```
For each trigger_type:
  accuracy = accepted_and_effective_count / total_suggestion_count

  IF accuracy < 0.50:
    trigger.weight *= 0.90  (reduce 10% - inaccurate trigger)

  IF accuracy between 0.50 and 0.80:
    No change (acceptable range)

  IF accuracy > 0.80:
    trigger.weight *= 1.05  (boost 5% - high-accuracy trigger)

  Bounds: 0.1 <= trigger.weight <= 2.0
```

**Synergy Multiplier Updates:**

```
For each framework_pair:
  IF pair.combined_rating >= 4.7 AND pair.usage_count >= 10:
    pair.synergy_boost = 0.15  (strong synergy confirmed)
    Add to auto-suggest combo recommendations

  IF pair.combined_rating >= 4.5 AND pair.usage_count >= 5:
    pair.synergy_boost = 0.10  (moderate synergy detected)

  IF pair.combined_rating < 3.0 AND pair.usage_count >= 5:
    pair.anti_synergy_penalty = -0.10  (negative synergy confirmed)
    Remove from combo recommendations
    Add warning when both selected
```

---

### 4.3 User Feedback Integration

**Three types of feedback signals:**

**1. Explicit Feedback (60% weight in scoring)**

Collected through prompts:
- Star ratings (1-5) after framework use
- ROI perception (High/Medium/Low/Negative)
- Would-use-again response (Yes/Maybe/No)
- Free-text comments (optional)
- Overall project satisfaction (1-10)

**2. Implicit Feedback (25% weight in scoring)**

Derived from behavior:
- Completion rate: Did user finish the framework template?
- Time spent: Proportional to template complexity (longer = more engagement)
- Return usage: Did user select this framework in subsequent projects?
- Skip rate: How often skipped when suggested?

**3. Negative Signals (15% weight in scoring)**

Derived from abandonment:
- Abandoned mid-framework (started but did not complete)
- Declined suggestion (counted only if high confidence >= 80%)
- Removed framework after initial selection
- Low time investment (< 2 minutes = likely dismissed)

**Composite Framework Score Calculation:**

```
composite_score(framework, user) =
    (explicit_rating / 5.0) * 0.60
  + (completion_rate) * 0.10
  + (return_usage_rate) * 0.15
  + (1.0 - abandonment_rate) * 0.10
  + (1.0 - decline_rate) * 0.05

Scale: 0.0 to 1.0 (multiply by 5 for star equivalent)

Example:
  explicit_rating = 4.0 => 0.80 * 0.60 = 0.48
  completion_rate = 0.90 => 0.90 * 0.10 = 0.09
  return_usage = 0.70 => 0.70 * 0.15 = 0.105
  abandonment = 0.10 => 0.90 * 0.10 = 0.09
  decline = 0.20 => 0.80 * 0.05 = 0.04

  Total = 0.805 => 4.025 stars equivalent
```

---

### 4.4 Decay and Recency

**Older data should matter less than recent data:**

```
Recency weighting:
  Last 30 days: weight = 1.0
  31-90 days: weight = 0.7
  91-180 days: weight = 0.4
  181-365 days: weight = 0.2
  > 365 days: weight = 0.1

Application:
  When calculating framework averages, apply recency weight
  to each data point before aggregation.

  weighted_avg = sum(rating_i * recency_weight_i) / sum(recency_weight_i)
```

This ensures the system adapts to changing user preferences and framework improvements over time.

---

## 5. Continuous Improvement Protocols

### 5.1 A/B Testing Framework Suggestions

**Test different suggestion strategies to improve acceptance:**

```yaml
ab_test_definition:
  test_id: {uuid}
  hypothesis: {what we expect to learn}
  variant_a: {control - current behavior}
  variant_b: {treatment - new behavior}
  primary_metric: {acceptance_rate|effectiveness_rating|time_to_decide}
  secondary_metrics: [{list}]
  duration_days: 30
  min_sample_size: 50
  statistical_method: chi_square  # for proportions
  significance_level: 0.05
```

**Example tests:**

```yaml
test_1:
  hypothesis: "Showing confidence % increases acceptance rate"
  variant_a: "Show confidence percentage (current)"
  variant_b: "Hide confidence, show only recommendation text"
  metric: acceptance_rate

test_2:
  hypothesis: "Showing framework synergy increases combo usage"
  variant_a: "Suggest frameworks individually (current)"
  variant_b: "Suggest frameworks as pairs when synergy >= 4.5"
  metric: combo_usage_rate

test_3:
  hypothesis: "Shorter framework descriptions increase acceptance for beginners"
  variant_a: "Full description with all details (current)"
  variant_b: "One-sentence description + 'Learn more' link"
  metric: acceptance_rate (filtered to beginner segment)

test_4:
  hypothesis: "TRIZ Quick preview reduces barrier to TRIZ Structured"
  variant_a: "Suggest TRIZ Structured directly (current)"
  variant_b: "Offer TRIZ Quick first, then upsell to Structured"
  metric: triz_structured_acceptance_rate
```

**Results analysis protocol:**

```
After {duration_days} days:

1. Check sample size >= min_sample_size for both variants
2. Calculate metric for variant_a and variant_b
3. Run statistical test at significance_level
4. IF significant AND variant_b better:
     Implement variant_b as new default
     Log decision to memory
5. IF not significant:
     Extend test by 15 days OR increase sample
6. IF significant AND variant_a better:
     Keep variant_a, log that hypothesis was wrong
```

---

### 5.2 User Segmentation

**Personalize suggestions based on detected user patterns:**

```yaml
segments:
  power_user:
    criteria:
      - completed_projects >= 10
      - frameworks_used_unique >= 5
      - uses_advanced_features: true  # TRIZ, Monte Carlo, etc.
    behavior:
      - Seeks advanced and complex frameworks
      - High tolerance for time investment
      - Values depth over simplicity
    customization:
      - Show all framework tiers including Tier 3
      - Skip beginner explanations
      - Proactively suggest synergy combinations
      - Offer A/B test participation
      - Show confidence percentages

  regular_user:
    criteria:
      - completed_projects between 4 and 9
      - frameworks_used_unique between 3 and 4
    behavior:
      - Comfortable with standard frameworks
      - Moderate time investment tolerance
      - Balanced depth/simplicity preference
    customization:
      - Show Tier 1 and Tier 2 frameworks
      - Standard explanations
      - Suggest synergies only for well-tested pairs
      - Hide confidence percentages

  beginner:
    criteria:
      - completed_projects <= 3
      - frameworks_used_unique <= 2
    behavior:
      - Needs guidance and reassurance
      - Prefers simple, well-known frameworks
      - Low tolerance for complexity
    customization:
      - Show only Tier 1 frameworks initially
      - Extra explanations and examples
      - No TRIZ/ARIZ suggestions (too complex)
      - Hand-holding mode in consilium
      - Simplified scoring display

  domain_specialist:
    criteria:
      - 80%+ projects in one domain
      - domain_frameworks_used >= 3 unique in that domain
    behavior:
      - Deep expertise in one area
      - Uses domain-specific frameworks heavily
      - May resist cross-domain suggestions
    customization:
      - Pre-populate domain frameworks
      - Skip domain detection step
      - Advanced mode for domain-specific templates
      - Suggest cross-domain frameworks gently (as experiments)
```

**Segment detection logic:**

```
On each project start:
  1. Count user's completed projects (from memory)
  2. Count unique frameworks used
  3. Calculate domain distribution
  4. Assign segment based on criteria (first match wins)
  5. Apply customization rules throughout workflow
```

**Segment transitions:**

```
beginner -> regular_user:
  When completed_projects reaches 4 AND frameworks_used >= 3
  Notification: "You've leveled up! More frameworks now available."

regular_user -> power_user:
  When completed_projects reaches 10 AND uses_advanced_features
  Notification: "Advanced mode unlocked. Full framework access enabled."

any -> domain_specialist:
  When 80%+ projects in one domain AND domain_frameworks >= 3
  Notification: "Detected {domain} specialization. Optimizing for your expertise."
```

---

### 5.3 Error Detection and Correction

**Automated detection of negative patterns:**

```
Pattern 1: Step Bottleneck Detection

  FOR each step IN workflow:
    IF step.completion_rate < 75% for 2 consecutive months:
      ALERT: "Bottleneck at {step_name}"
      ACTIONS:
        - Analyze abandonment reasons (time? complexity? unclear?)
        - Generate simplification recommendations
        - Consider making step optional or merging with adjacent step

Pattern 2: Framework Overload Detection

  FOR each project:
    IF project.frameworks_count >= 4 AND project.satisfaction < 7:
      ALERT: "Possible framework overload in {project_name}"
      ACTIONS:
        - Reduce max simultaneous framework suggestions to 2
        - Add warning when user selects 4th framework
        - Track if reducing count improves satisfaction

Pattern 3: Abandonment Pattern Detection

  FOR each abandoned project:
    last_step = project.last_completed_step
    IF count(abandoned at last_step) / count(all reaching last_step) > 0.25:
      ALERT: "High abandonment rate at {last_step}"
      ACTIONS:
        - Survey users who abandoned at this step
        - Compare with completed projects (what was different?)
        - Test simplified version of problematic step

Pattern 4: Stale Framework Detection

  FOR each framework:
    IF framework.usage_count_90d == 0 AND framework.was_previously_used:
      ALERT: "Framework {name} not used in 90 days"
      ACTIONS:
        - Check if superseded by better alternative
        - Consider archiving from active suggestions
        - Verify template still works correctly

Pattern 5: Confidence Miscalibration Detection

  FOR each confidence_bucket:
    expected_effectiveness = bucket_midpoint / 100 * 5  # scale to 5 stars
    actual_effectiveness = mean(ratings in bucket)

    IF abs(expected - actual) > 0.8:
      ALERT: "Confidence miscalibrated in {bucket} range"
      ACTIONS:
        - Adjust confidence calculation weights
        - Review trigger logic for that confidence range
        - Retrain confidence model with recent data
```

---

### 5.4 Quarterly Deep Review

**Every quarter, perform comprehensive system analysis:**

```
Quarterly Review Checklist:

1. FRAMEWORK AUDIT
   [ ] Review all frameworks with avg rating < 3.5
   [ ] Identify frameworks never suggested (missing triggers?)
   [ ] Check for new frameworks to add (research trends)
   [ ] Update tier assignments based on performance data
   [ ] Refresh synergy matrix with latest data

2. WORKFLOW OPTIMIZATION
   [ ] Analyze step-by-step flow times
   [ ] Identify redundant or overlapping steps
   [ ] Check if step order is optimal
   [ ] Review step skip patterns (what can be made optional?)
   [ ] Update time estimates from actual data

3. AUTO-SUGGEST CALIBRATION
   [ ] Run full confidence calibration analysis
   [ ] Update trigger weights from quarterly data
   [ ] Test new trigger hypotheses
   [ ] Review and close completed A/B tests
   [ ] Design new A/B tests for next quarter

4. USER EXPERIENCE
   [ ] Review user satisfaction trends
   [ ] Analyze feedback comments for common themes
   [ ] Check segment distribution changes
   [ ] Update segment criteria if needed
   [ ] Identify friction points from time-on-step data

5. SYSTEM HEALTH
   [ ] Verify all metrics collection points active
   [ ] Check data completeness (% of projects with full metrics)
   [ ] Audit memory storage usage
   [ ] Clean up outdated or corrupted metric entries
   [ ] Update this document with learnings
```

---

## 6. Metrics Export and Reporting

### 6.1 User-Facing Quarterly Report

**Generated automatically and presented to user:**

```markdown
# Your Life OS Quarterly Report: {Quarter} {Year}

## Overview
- Projects Completed: {N}
- Success Rate: {%} ({achieved}/{total} goals met)
- Total Time Invested: {X} hours
- Avg Time per Project: {X} hours

## Projects by Domain
- Business: {N} projects ({%} success)
- Finance: {N} projects ({%} success)
- Health: {N} projects ({%} success)
- Personal Development: {N} projects ({%} success)

## Your Most Effective Frameworks

1. **{Framework 1}** - Used {N} times, {X} avg rating
   - Best for: {detected pattern}
   - Your insight: "{most recent comment}"

2. **{Framework 2}** - Used {N} times, {X} avg rating
   - Best for: {detected pattern}
   - Your insight: "{most recent comment}"

3. **{Framework 3}** - Used {N} times, {X} avg rating
   - Best for: {detected pattern}
   - Your insight: "{most recent comment}"

## Your Power Combos

You combined **{Framework A} + {Framework B}** {N} times
with {X} avg rating - this is your strongest synergy.

## Time Investment Analysis

- Most efficient domain: {domain} ({X} hrs avg)
- Most intensive domain: {domain} ({X} hrs avg)
- Time estimate accuracy: {%} (actual vs planned)

## Recommendations Based on Your Data

1. {Personalized recommendation based on patterns}
2. {Personalized recommendation based on gaps}
3. {Personalized recommendation based on trends}

## Compared to Last Quarter

- Completion rate: {current}% vs {previous}% ({up/down} {delta}%)
- Satisfaction: {current} vs {previous} ({up/down} {delta})
- Time efficiency: {current} hrs vs {previous} hrs ({up/down} {delta})
```

---

### 6.2 System-Wide Insights Storage

**Quarterly insights stored to global memory for cross-session access:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:insights:quarterly:{year}-Q{quarter}" \
  --content "{
    period: '{year}-Q{quarter}',
    total_projects: {N},
    completion_rate: {%},
    avg_satisfaction: {X}/10,
    top_frameworks: [{ranked list}],
    most_effective_combo: '{pair}',
    bottleneck_step: '{step_name}',
    auto_suggest_accuracy: {%},
    confidence_correlation_r2: {value},
    segments: {
      power_users: {N},
      regular_users: {N},
      beginners: {N},
      domain_specialists: {N}
    },
    key_learnings: ['{learning_1}', '{learning_2}', '{learning_3}'],
    actions_taken: ['{action_1}', '{action_2}'],
    next_quarter_priorities: ['{priority_1}', '{priority_2}']
  }"
```

---

### 6.3 Cross-Project Pattern Sharing

**Patterns discovered in metrics that benefit all projects:**

```bash
# Store reusable insight
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:patterns:{pattern_name}" \
  --content "{
    pattern: '{description}',
    discovered_from: 'metrics analysis {date}',
    evidence: '{data supporting the pattern}',
    applicability: '{when to apply}',
    confidence: {0-1}
  }"
```

**Example patterns to detect and share:**

| Pattern | Detection Rule | Shared Insight |
|---------|---------------|----------------|
| Planning fatigue | > 3 projects abandon at Deep Plan | Offer lightweight plan option |
| Analysis paralysis | Consilium takes > 30 min | Suggest Lite mode default |
| Framework resistance | Same framework declined 3+ times | Stop suggesting to this user |
| Domain momentum | 3+ projects in same domain succeed | User has domain expertise, advance mode |
| Synergy discovery | New combo rates > 4.5 with N >= 5 | Add to recommended pairings |

---

## 7. Integration Points

### 7.1 Memory Integration Map

```
Metrics Data Flow:

  Step Completion
    -> post-task hook
    -> life-os:metrics:steps:{project_id}:{step_id}
    -> Monthly aggregation
    -> life-os:metrics:monthly:{year}-{month}

  Framework Usage
    -> feedback prompt (explicit)
    -> life-os:metrics:framework:{project_id}:{framework}
    -> Monthly aggregation
    -> Framework rankings update

  Auto-Suggest Events
    -> auto-logged on suggestion
    -> life-os:metrics:autosuggest:{event_id}
    -> Monthly accuracy analysis
    -> Trigger weight updates

  Project Outcomes
    -> Step 09 completion OR explicit close
    -> life-os:metrics:outcome:{project_id}
    -> Quarterly report generation
    -> Pattern discovery
```

### 7.2 Hook Integration

```yaml
hooks_used:
  post-task:
    trigger: After each workflow step completes
    action: Store step_metrics to memory
    namespace: shared-knowledge
    key_pattern: "life-os:metrics:steps:{project_id}:{step_id}"

  session-end:
    trigger: When user ends session
    action: Flush pending metrics, trigger consolidation
    ensures: No metrics lost between sessions

  consolidate:
    trigger: Every 5 minutes (background worker)
    action: Deduplicate metrics entries, update aggregates
    ensures: Clean data for monthly analysis
```

### 7.3 Workflow File Cross-References

```
Files that feed metrics:
  workflow.md                    -> Step definitions and flow
  steps-c/step-01 through 09   -> Step completion events
  steps-e/step-01 through 04   -> Execution phase events
  steps-v/step-01 through 03   -> Review phase events
  templates/project-snapshot     -> Project outcome data
  templates/project-journal      -> Ongoing project metrics
  data/domain-framework-integration -> Framework catalog

Files that consume metrics:
  data/domain-framework-integration -> Updated rankings
  data/framework-synergy-matrix     -> Updated synergy scores
  data/search-decision-protocol     -> Updated trigger weights
  workflow-plan.md                   -> Updated time estimates
```

---

## 8. Success Criteria

### 8.1 Metrics System Health

**The metrics system itself is working correctly if:**

| Criterion | Target | Measurement |
|-----------|--------|-------------|
| Data completeness | >= 70% of projects have full metrics | count(full_metrics) / count(projects) |
| Feedback collection rate | >= 50% of framework uses get ratings | count(rated) / count(used) |
| Monthly loop execution | Runs every month | check memory for monthly reports |
| Auto-suggest tracking | 100% of suggestions logged | count(logged) / count(displayed) |
| Storage reliability | 0 lost metric entries | audit count vs expected |
| Report generation | Quarterly reports created | check memory for quarterly reports |

### 8.2 System Improvement Targets

**The learning loop is producing results if:**

| Criterion | Target | Timeframe |
|-----------|--------|-----------|
| Auto-suggest acceptance rate | >= 60% | Ongoing |
| Auto-suggest effectiveness (accepted) | >= 4.0 avg stars | Ongoing |
| Confidence-effectiveness correlation | R^2 >= 0.70 | Within 3 months |
| User satisfaction with workflow | >= 4.0/5.0 avg | Ongoing |
| Low-rated frameworks identified | Within 1 month of decline | Monthly loop |
| Low-rated frameworks improved | Within 1 quarter | Quarterly review |
| High-synergy pairs in auto-suggest | Within 2 months of discovery | Monthly loop |
| Bottleneck steps identified | Within 1 month | Monthly loop |
| Bottleneck steps addressed | Within 1 quarter | Quarterly review |
| Project completion rate | >= 70% | Ongoing |

### 8.3 Long-Term Goals (6-12 months)

| Goal | Target | How Measured |
|------|--------|--------------|
| Personalized suggestions | Segment-specific accuracy >= 70% | Per-segment acceptance rate |
| Framework catalog optimized | No framework with avg < 3.0 for 2+ quarters | Rating trends |
| Synergy catalog | >= 15 confirmed high-synergy pairs | Synergy map size |
| Time estimates accurate | Within 20% of actual for 80% of projects | Duration accuracy |
| User retention | >= 80% of users complete 2+ projects | Return usage rate |
| Zero stale frameworks | All frameworks used at least once per quarter | Usage audit |

---

## 9. Implementation Notes

### 9.1 Phase 4 Dependencies

This metrics system requires:
- Phase 1-3 workflow steps operational (data sources)
- Claude Flow Memory accessible (storage backend)
- Post-task hooks active (automatic collection)
- User feedback prompts integrated into step completion flow

### 9.2 Bootstrap Period

For the first 30 days of operation:
- Insufficient data for meaningful statistics
- Use default confidence values from domain-framework-integration.md
- Do not run A/B tests (need baseline first)
- Collect data passively, present first monthly report at day 31
- Mark all insights as "preliminary" until N >= 20 projects

### 9.3 Privacy Considerations

- All metrics are user-local (stored in user's Claude Flow memory)
- No metrics shared externally without explicit consent
- User can request metrics deletion at any time
- Aggregated patterns stored in shared-knowledge are anonymized

### 9.4 Graceful Degradation

If metrics collection fails:
- Workflow continues normally (metrics are non-blocking)
- Missing data points marked as null in aggregations
- Monthly loop skips calculations with insufficient data
- User notified only if > 50% of data missing

---

**Metrics System Version:** 1.0
**Last Updated:** 2026-02-04
**Status:** Implementation Ready
**Integration:** Claude Flow Memory + post-project feedback
**Phase:** 4 (Full Ecosystem)
