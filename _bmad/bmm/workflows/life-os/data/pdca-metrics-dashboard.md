# PDCA Metrics Dashboard (Life OS)

**Version:** 1.0
**Purpose:** Track Plan-Do-Check-Act cycle effectiveness and goal achievement metrics
**Integration:** All review steps (v-01 to v-04), goals.yaml, todo-generation-system.md

---

## Overview

The PDCA Metrics Dashboard provides comprehensive tracking of goal execution, cycle velocity, and continuous improvement effectiveness through quantitative KPIs and qualitative insights.

---

## Core Metrics

### 1. Goal Completion Rate

**Formula:** `completed_goals / total_goals × 100%`

```yaml
metric:
  name: "Goal Completion Rate"
  category: "Effectiveness"
  target: 80%  # 80% of goals should be completed
  calculation_period: "quarterly"

  data_sources:
    - goals.yaml → goals[].status
    - Filter: status == 'completed'

  visualization:
    type: "progress_bar"
    color_coding:
      green: ">= 80%"
      yellow: "60-79%"
      red: "< 60%"

  trend:
    lookback: "4 quarters"
    expected: "increasing or stable"
```

**Current Value:** Track in metrics.md after each quarterly review.

---

### 2. Key Result Achievement Rate

**Formula:** `achieved_krs / total_krs × 100%`

```yaml
metric:
  name: "Key Result Achievement Rate"
  category: "Outcomes"
  target: 75%  # 75% of KRs should hit target

  data_sources:
    - goals.yaml → goals[].key_results[]
    - Filter: progress >= 100 OR status == 'completed'

  breakdown:
    by_domain: ["business", "finance", "health", "personal"]
    by_priority: ["P0", "P1", "P2", "P3"]
    by_quarter: ["Q1", "Q2", "Q3", "Q4"]

  visualization:
    type: "stacked_bar_chart"
    x_axis: "quarter"
    y_axis: "achievement_rate"
    segments: "domain"
```

---

### 3. Average Goal Progress

**Formula:** `sum(goals[].progress) / count(goals)`

```yaml
metric:
  name: "Average Goal Progress"
  category: "Execution"
  target: 25%  # 25% progress per quarter (100% per year)

  data_sources:
    - goals.yaml → goals[].key_results[].progress
    - Aggregate: mean(progress)

  calculation:
    frequency: "weekly"
    smoothing: "7-day moving average"

  visualization:
    type: "line_chart"
    x_axis: "week_number"
    y_axis: "average_progress"
    trend_line: true
    target_line: 25  # Show target as horizontal line

  alerts:
    - condition: "progress < 15% at quarter end"
      action: "Flag for adjustment in Quarterly Review"
```

---

### 4. PDCA Cycle Velocity

**Formula:** `goals_adjusted / total_reviews`

```yaml
metric:
  name: "PDCA Cycle Velocity"
  category: "Agility"
  target: 0.30  # 30% of goals adjusted per review cycle

  data_sources:
    - Quarterly Review reports → decisions[].type
    - Filter: type in ['adjust_target', 'extend_deadline', 'pause', 'abandon']

  calculation:
    numerator: count(adjusted_goals)
    denominator: count(active_goals_at_review)

  interpretation:
    too_high: "> 50% (unstable goals)"
    optimal: "20-40% (healthy adaptation)"
    too_low: "< 10% (rigid, not learning)"

  visualization:
    type: "gauge"
    ranges:
      low: "0-10%"
      optimal: "10-40%"
      high: "40-100%"
```

---

### 5. Time to First Action

**Formula:** `days_between(goal.created_at, first_todo.completed_at)`

```yaml
metric:
  name: "Time to First Action"
  category: "Execution Speed"
  target: 7  # Start working within 7 days of goal creation

  data_sources:
    - goals.yaml → goals[].created_at
    - todos.json → todos[].completed_at
    - Match: first completed TODO for each goal

  aggregation:
    by_goal: "individual measurement"
    overall: "median(time_to_action)"

  visualization:
    type: "histogram"
    x_axis: "days_to_first_action"
    y_axis: "count_of_goals"
    bin_size: 3  # 0-3, 4-7, 8-11, etc.

  alerts:
    - condition: "time_to_action > 14 days"
      action: "Flag goal as 'at risk of abandonment'"
```

---

### 6. TODO Completion Rate

**Formula:** `completed_todos / total_todos × 100%`

```yaml
metric:
  name: "TODO Completion Rate"
  category: "Execution"
  target: 80%

  data_sources:
    - todos.json → todos[].status
    - Filter: status == 'completed'

  breakdown:
    by_priority: ["P0", "P1", "P2", "P3"]
    by_type: ["goal_planning", "milestone", "weekly_task"]
    by_week: "week_number"

  visualization:
    type: "weekly_heatmap"
    cells: "week_number × priority"
    color: "completion_rate"

  insights:
    - "Which priorities get neglected?"
    - "Weekly completion patterns?"
```

---

### 7. On-Time Delivery Rate

**Formula:** `completed_before_deadline / total_completed × 100%`

```yaml
metric:
  name: "On-Time Delivery Rate"
  category: "Reliability"
  target: 90%

  data_sources:
    - todos.json → filter(status == 'completed')
    - Compare: completed_at <= effective_deadline

  calculation:
    on_time: completed_at <= deadline
    late: completed_at > deadline
    rate: on_time / (on_time + late)

  analysis:
    average_delay: "mean(days_late for late TODOs)"
    worst_offenders: "TODOs with delay > 7 days"

  visualization:
    type: "split_donut"
    segments: ["on_time", "late"]
    center_label: "{on_time_rate}%"
```

---

### 8. Goal-Portfolio Alignment Score

**Formula:** `aligned_projects / total_projects × 100%`

```yaml
metric:
  name: "Goal-Portfolio Alignment"
  category: "Strategic Alignment"
  target: 85%

  data_sources:
    - portfolio.md → projects[]
    - goals.yaml → goals[]
    - Match: project supports at least 1 active goal

  calculation:
    aligned: project has goal_id reference
    misaligned: project.goal_id == null OR goal.status == 'abandoned'

  visualization:
    type: "sankey_diagram"
    flow: "goals → projects → outcomes"

  insights:
    - "Which goals have no projects?"
    - "Which projects don't support any goal?"
```

---

## Dashboard Layout

### Real-Time Dashboard (CLI Command)

```bash
npx claude-flow@v3alpha pdca dashboard --live
```

**Output:**
```
╔════════════════════════════════════════════════════════════════╗
║              PDCA Metrics Dashboard — 2026-Q1                 ║
╠════════════════════════════════════════════════════════════════╣
║ Goal Completion Rate:          [████████░░] 75% (Target: 80%) ║
║ KR Achievement Rate:            [█████░░░░░] 60% (Target: 75%) ║
║ Average Goal Progress:          [██████░░░░] 62% (Target: 25%/Q) ║
║ PDCA Cycle Velocity:            [███░░░░░░░] 28% (Optimal: 20-40%) ║
║ Time to First Action:           5 days (Target: <7 days) ✅     ║
║ TODO Completion Rate:           [████████░░] 82% (Target: 80%) ║
║ On-Time Delivery:               [████████░░] 87% (Target: 90%) ║
║ Goal-Portfolio Alignment:       [████████░░] 81% (Target: 85%) ║
╠════════════════════════════════════════════════════════════════╣
║ Overall PDCA Health:            [███████░░░] 76% ⚠️             ║
╚════════════════════════════════════════════════════════════════╝

Alerts:
⚠️  KR Achievement below target (60% vs 75%)
⚠️  On-Time Delivery slightly below target

Recommendations:
1. Review Q1 Key Results — some may be too ambitious
2. Add buffer days to high-priority TODOs
3. Consider breaking large KRs into smaller steps
```

---

## Trend Analysis

### Quarter-over-Quarter Comparison

```yaml
trend_analysis:
  metrics: ["goal_completion", "kr_achievement", "todo_completion"]
  periods: ["Q1-2026", "Q2-2026", "Q3-2026", "Q4-2026"]

  visualization:
    type: "multi_line_chart"
    x_axis: "quarter"
    y_axis: "rate (%)"
    lines:
      - "Goal Completion"
      - "KR Achievement"
      - "TODO Completion"

  insights:
    - slope: "increasing/decreasing/stable"
    - seasonality: "patterns by quarter"
    - anomalies: "significant drops or spikes"
```

---

## Forecasting & Predictive Metrics

### Projected Goal Completion (Linear Regression)

```python
def forecast_goal_completion(historical_data, quarters_ahead=1):
    """
    Predict goal completion rate for next N quarters.
    Uses linear regression on past 4 quarters.
    """
    x = [1, 2, 3, 4]  # Q1, Q2, Q3, Q4
    y = historical_data['goal_completion']  # [75, 80, 82, 85]

    # Linear regression: y = mx + b
    m, b = linear_regression(x, y)

    # Forecast next quarter
    forecast = m * (len(x) + quarters_ahead) + b

    # Confidence interval (±10%)
    confidence_lower = forecast * 0.9
    confidence_upper = forecast * 1.1

    return {
        'forecast': forecast,
        'confidence_range': (confidence_lower, confidence_upper),
        'trend': 'increasing' if m > 0 else 'decreasing'
    }
```

**Visualization:**
- Actual data: solid line
- Forecast: dashed line
- Confidence interval: shaded area

---

## Bottleneck Identification

### Automatic Bottleneck Detection

```yaml
bottleneck_analysis:
  triggers:
    - metric: "goal_completion"
      condition: "< 60% for 2 consecutive quarters"
      investigation: "Which goals are stuck?"

    - metric: "kr_achievement"
      condition: "< 50% in any domain"
      investigation: "Which domain needs support?"

    - metric: "todo_completion"
      condition: "< 70% for high-priority TODOs"
      investigation: "Resource constraint or scope issue?"

  root_cause_analysis:
    steps:
      - Identify lowest-performing metric
      - Drill down by domain/priority/type
      - Compare to historical baseline
      - Correlate with external factors (workload, health, etc.)
      - Generate recommendations

  output:
    format: "bottleneck_report.md"
    sections:
      - Detected Bottleneck
      - Contributing Factors
      - Recommended Actions
      - Timeline to Resolution
```

---

## Integration with Review Steps

### Daily Review (v-01)
- Show: TODO completion for today, this week
- Update: Daily TODO count

### Weekly Review (v-02)
- Show: Weekly TODO completion, time to action
- Update: Weekly progress on active KRs

### Monthly Review (v-03)
- Show: Goal progress, KR achievement (month-to-date)
- Update: Monthly metrics snapshot

### Quarterly Review (v-04)
- Show: All core metrics for the quarter
- Update: Quarterly report with full dashboard
- Calculate: PDCA cycle velocity

---

## Data Collection & Storage

### Metrics File Format

**File:** `{bmb_creations_output_folder}/life-os/metrics/metrics.md`

```markdown
# Life OS Metrics

## Overview

Last Updated: 2026-02-05
Current Quarter: Q1 2026

---

## Core Metrics (Current)

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Goal Completion Rate | 80% | 75% | 🟡 |
| KR Achievement Rate | 75% | 60% | 🔴 |
| Average Goal Progress | 25%/Q | 18% | 🟡 |
| TODO Completion Rate | 80% | 82% | 🟢 |
| On-Time Delivery | 90% | 87% | 🟡 |

---

## Historical Data

### Q1 2026

- Goal Completion: 75%
- KR Achievement: 60%
- TODO Completion: 82%
- Recorded: 2026-03-31

### Q4 2025

- Goal Completion: 70%
- KR Achievement: 65%
- TODO Completion: 78%
- Recorded: 2025-12-31
```

---

## CLI Commands

### View Dashboard

```bash
# Real-time dashboard
npx claude-flow@v3alpha pdca dashboard

# Quarterly summary
npx claude-flow@v3alpha pdca dashboard --quarter Q1

# Export to JSON
npx claude-flow@v3alpha pdca dashboard --export ./metrics-Q1.json
```

### Calculate Metrics

```bash
# Calculate all metrics
npx claude-flow@v3alpha pdca calculate --source ./goals.yaml

# Specific metric
npx claude-flow@v3alpha pdca metric goal-completion

# Trend analysis
npx claude-flow@v3alpha pdca trends --lookback 4
```

### Bottleneck Detection

```bash
# Auto-detect bottlenecks
npx claude-flow@v3alpha pdca bottlenecks

# Generate recommendations
npx claude-flow@v3alpha pdca recommend --metric kr-achievement
```

---

## Visualization Specifications

### Goal Completion Progress Chart

```javascript
{
  type: 'line',
  data: {
    labels: ['Week 1', 'Week 2', 'Week 3', ..., 'Week 13'],
    datasets: [
      {
        label: 'Goal 1: SaaS Launch',
        data: [0, 5, 12, 18, 25, 32, 38, 45, 52, 60, 68, 75, 82],
        borderColor: '#4CAF50',
        fill: false
      },
      {
        label: 'Goal 2: Financial Stability',
        data: [0, 8, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
        borderColor: '#2196F3',
        fill: false
      }
    ]
  },
  options: {
    scales: {
      y: { min: 0, max: 100, title: { text: 'Progress (%)' } }
    }
  }
}
```

---

**End of PDCA Metrics Dashboard Documentation**
