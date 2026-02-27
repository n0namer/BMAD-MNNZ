# Critical Path Method (CPM) Analysis

## Definition

The **Critical Path** is the longest sequence of dependent milestones from project start to finish. Any delay in critical path milestones delays the entire project.

**Key Properties:**
- All critical path milestones have zero slack
- Total duration equals project minimum duration
- Multiple critical paths can exist
- Critical path can change during project execution

## Critical Path Algorithm

### Step 1: Forward Pass

Calculate earliest start (ES) and earliest finish (EF) for each milestone.

```
ALGORITHM forward_pass(milestones[], project_start):

  1. Initialize all milestones:
     FOR each milestone:
       milestone.ES = null
       milestone.EF = null

  2. Set start milestones (no dependencies):
     FOR each milestone WHERE dependencies.empty():
       milestone.ES = project_start
       milestone.EF = milestone.ES + milestone.duration

  3. Calculate remaining milestones in dependency order:
     WHILE milestones with null ES exist:
       FOR each milestone WHERE ES is null:
         IF all dependencies have calculated EF:
           milestone.ES = MAX(dependency.EF for all dependencies)
           milestone.EF = milestone.ES + milestone.duration
```

### Step 2: Backward Pass

Calculate latest start (LS) and latest finish (LF) for each milestone.

```
ALGORITHM backward_pass(milestones[], project_end):

  1. Initialize all milestones:
     FOR each milestone:
       milestone.LS = null
       milestone.LF = null

  2. Set end milestones (no successors):
     FOR each milestone WHERE no successors exist:
       milestone.LF = project_end
       milestone.LS = milestone.LF - milestone.duration

  3. Calculate remaining milestones in reverse dependency order:
     WHILE milestones with null LF exist:
       FOR each milestone WHERE LF is null:
         IF all successors have calculated LS:
           milestone.LF = MIN(successor.LS for all successors)
           milestone.LS = milestone.LF - milestone.duration
```

### Step 3: Calculate Slack

```
ALGORITHM calculate_slack(milestones[]):

  FOR each milestone:
    # Total Float (slack)
    milestone.total_slack = milestone.LS - milestone.ES

    # Free Float (independent slack)
    successor_ES_values = []
    FOR each successor of milestone:
      successor_ES_values.push(successor.ES)

    IF successor_ES_values.empty():
      milestone.free_slack = project_end - milestone.EF
    ELSE:
      milestone.free_slack = MIN(successor_ES_values) - milestone.EF
```

### Step 4: Identify Critical Path

```
ALGORITHM identify_critical_path(milestones[]):

  # Milestones with zero total slack are on critical path
  critical_milestones = milestones WHERE total_slack == 0

  # Build critical path sequence
  critical_paths = []

  FUNCTION build_path(milestone, path):
    path.append(milestone)

    successors = find_successors(milestone)
    critical_successors = successors WHERE total_slack == 0

    IF critical_successors.empty():
      critical_paths.append(path.copy())
    ELSE:
      FOR each critical_successor:
        build_path(critical_successor, path)

    path.pop()

  # Find all start nodes on critical path
  start_nodes = critical_milestones WHERE dependencies.empty()

  FOR each start_node:
    build_path(start_node, [])

  RETURN critical_paths
```

## Slack Analysis Types

### 1. Total Slack (Total Float)

Maximum time a milestone can be delayed without delaying project completion.

```
Total Slack = LS - ES = LF - EF
```

**Categories:**
- `slack = 0`: Critical path milestone (cannot delay)
- `0 < slack < 1 week`: Near-critical (monitor closely)
- `slack >= 1 week`: Non-critical (flexible scheduling)

### 2. Free Slack (Free Float)

Maximum time a milestone can be delayed without delaying any successor's earliest start.

```
Free Slack = MIN(Successor.ES) - EF
```

**Interpretation:**
- Free slack allows delays without affecting other milestones
- Always: Free Slack ≤ Total Slack

### 3. Independent Slack

Maximum time a milestone can be delayed assuming:
- All predecessors finish at latest finish time
- All successors start at earliest start time

```
Independent Slack = MAX(0, MIN(Successor.ES) - MAX(Predecessor.LF) - Duration)
```

## Critical Path Analysis Table

| Milestone | ES | EF | LS | LF | Total Slack | Free Slack | Critical |
|-----------|----|----|----|----|-------------|------------|----------|
| M1 | W0 | W2 | W0 | W2 | 0 | 0 | YES |
| M2 | W2 | W5 | W2 | W5 | 0 | 0 | YES |
| M3 | W2 | W4.5 | W2.5 | W5 | 0.5 | 0.5 | NO |
| M4 | W5 | W7 | W5 | W7 | 0 | 0 | YES |

**Critical Path:** M1 → M2 → M4 (7 weeks total)

## Risk Assessment

### Critical Path Risk Levels

```
FUNCTION calculate_risk_level(critical_path, milestones[]):

  total_duration = sum(milestone.duration for milestone in critical_path)

  # Calculate risk score
  risk_factors = {
    multiple_paths: count_critical_paths() > 1,
    long_duration: total_duration > 12 weeks,
    many_dependencies: avg_dependencies > 2,
    no_buffer: min_slack_non_critical < 1 week
  }

  risk_score = sum(1 for factor in risk_factors if factor)

  IF risk_score == 0:
    RETURN "LOW"
  ELSE IF risk_score <= 2:
    RETURN "MEDIUM"
  ELSE:
    RETURN "HIGH"
```

**Risk Level Definitions:**

- **LOW:** Single critical path, <12 weeks, adequate buffer in non-critical
- **MEDIUM:** Multiple paths OR long duration OR tight dependencies
- **HIGH:** Multiple risk factors combined, very tight schedule

## Critical Path Visualization

### Highlighting in ASCII

```
Critical path milestones:
  - Use bold characters: ████ instead of ████
  - Add markers: [CRIT] prefix
  - Use double lines: ══> for critical path flow

Non-critical milestones:
  - Standard characters: ████
  - Show slack with ░░░░
  - Use single lines: ──> for regular dependencies
```

### Highlighting in Mermaid

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD

    section Critical Path
    M1: Foundation    :crit, m1, 2026-02-07, 14d
    M2: Core Features :crit, m2, after m1, 21d
    M4: Integration   :crit, m4, after m2 m3, 14d

    section Non-Critical
    M3: UX Design     :m3, after m1, 17d
```

**Mermaid Critical Path Markers:**
- `:crit` - Marks milestone as critical (red color)
- `:active` - Currently in progress (green color)
- `:done` - Completed milestone (gray color)

## Critical Path Monitoring

### Progress Tracking

```
FUNCTION track_critical_path_progress(milestones[], today):

  FOR each milestone in critical_path:
    IF milestone.start_date <= today <= milestone.end_date:
      # Currently executing
      completion_percentage =
        (today - milestone.start_date) / milestone.duration * 100

      status = "ON_TRACK" if on schedule else "DELAYED"

    ELSE IF today > milestone.end_date:
      status = "COMPLETED" if finished else "OVERDUE"

    ELSE:
      status = "PENDING"

  RETURN status_summary
```

### Early Warning Indicators

**Red Flags (Immediate Action Required):**
- Critical milestone delayed by any amount
- Free slack on near-critical milestone exhausted
- Dependency blocking critical path
- Scope creep affecting critical milestones

**Yellow Flags (Monitor Closely):**
- Non-critical slack reduced by >50%
- Critical milestone at risk (external dependency)
- Resource constraints affecting critical path
- Near-critical path within 0.5 weeks of critical

## Resource Leveling Impact

When resources are limited, critical path may change:

```
ALGORITHM resource_constrained_critical_path(milestones[], resources):

  # Standard CPM assuming unlimited resources
  standard_critical_path = calculate_critical_path(milestones)

  # Apply resource constraints
  FOR each milestone in dependency_order:
    IF required_resources > available_resources:
      milestone.start_date = delayed_start_date
      milestone.end_date = delayed_end_date

  # Recalculate critical path with resource delays
  resource_critical_path = calculate_critical_path(adjusted_milestones)

  IF resource_critical_path != standard_critical_path:
    RETURN {
      changed: true,
      new_critical_path: resource_critical_path,
      delay: calculate_delay(resource_critical_path, standard_critical_path)
    }
```

## What-If Analysis

### Impact of Delays

```
FUNCTION simulate_delay(milestone_id, delay_weeks):

  # Apply delay to milestone
  milestone.end_date += delay_weeks

  # Recalculate forward pass
  recalculate_forward_pass()

  # Check impact
  new_project_end = max(milestone.EF for all milestones)
  project_delay = new_project_end - original_project_end

  # Identify newly critical paths
  new_critical_milestones = milestones WHERE total_slack == 0

  RETURN {
    project_delay: project_delay,
    new_critical_path: identify_critical_path(new_critical_milestones),
    affected_milestones: list of affected downstream milestones
  }
```

### Fast-Tracking Analysis

Identify opportunities to overlap dependent milestones:

```
FUNCTION identify_fast_track_opportunities(critical_path):

  opportunities = []

  FOR each pair of sequential milestones (A, B) in critical_path:
    IF B depends on A:
      # Can B start before A finishes?
      IF A has deliverables that can be released early:
        overlap_potential = estimate_overlap(A, B)
        time_savings = overlap_potential * B.duration

        opportunities.push({
          milestone_A: A.id,
          milestone_B: B.id,
          time_savings: time_savings,
          risk: assess_overlap_risk(A, B)
        })

  RETURN opportunities sorted by time_savings DESC
```

## Critical Path Optimization

### Crashing (Add Resources)

```
FUNCTION identify_crash_candidates(critical_path, budget):

  candidates = []

  FOR each milestone in critical_path:
    IF milestone can be accelerated with additional resources:
      cost = calculate_crash_cost(milestone)
      time_saved = calculate_crash_time_savings(milestone)

      IF cost <= budget:
        candidates.push({
          milestone: milestone.id,
          cost: cost,
          time_saved: time_saved,
          cost_per_week: cost / time_saved
        })

  RETURN candidates sorted by cost_per_week ASC
```

**Crashing Priority:**
1. Lowest cost per week saved
2. Earliest milestones first (more impact)
3. Milestones with external dependencies (fixed end dates)
