# Life OS Dashboard Guide

## Overview

The **Life OS Dashboard** provides a visual, at-a-glance overview of all your active projects, WIP status, milestones, and performance metrics. Instead of opening multiple tracking files, you get a comprehensive project overview in seconds.

## Quick Start

```bash
# Show full dashboard
./scripts/dashboard.sh

# Windows PowerShell
.\scripts\dashboard.ps1
```

## What You Get

The dashboard displays:

1. **WIP Status** - Current work-in-progress count with health indicator (🟢/🟡/🔴)
2. **Active Projects** - All IN_PROGRESS ideas with key details
3. **Next Milestones** - Upcoming deadlines per project
4. **Planned Ideas** - Ideas ready to start when capacity allows
5. **Recent Completions** - Completed and killed ideas (last 30 days)
6. **Metrics** - Estimate accuracy, speed multiplier, completion rate
7. **Alerts & Recommendations** - Actionable insights (pulse overdue, blockers, etc.)

## Dashboard Commands

### Full Dashboard

```bash
./scripts/dashboard.sh
```

Displays complete overview with all sections.

### Project Detail View

```bash
./scripts/dashboard.sh project 1
```

Shows detailed view of a specific project:
- Timeline and variance
- All milestones with status
- Weekly pulse history
- Project metrics
- Recommendations

### Planned Ideas

```bash
./scripts/dashboard.sh planned
```

Shows all PLANNED ideas sorted by priority with:
- Estimated duration (with LLM multiplier)
- Next action to start
- WIP availability

### Extended Metrics

```bash
./scripts/dashboard.sh metrics
```

Deep dive into performance metrics:
- Estimate accuracy breakdown (±10%, ±20%, ±40%)
- Speed multiplier by track (Quick/Standard/Deep)
- Completion patterns
- Blocker analysis

### Refresh Dashboard

```bash
./scripts/dashboard.sh refresh
```

Forces data refresh from Claude Flow memory and tracking files.

## Understanding the Dashboard

### WIP Status Indicators

| Status | Meaning | Action |
|--------|---------|--------|
| 🟢 HEALTHY (0-2) | Optimal capacity | Can start new work |
| 🟡 AT CAPACITY (2-3) | At limit | Complete 1 before starting new |
| 🔴 OVERLOAD (3+) | Over capacity | Must complete work urgently |

### Project Status

| Status | Meaning | Variance |
|--------|---------|----------|
| 🟢 On Track | Within ±20% of plan | -20% to +20% |
| 🟡 At Risk | 20-40% variance | -40% to +40% |
| 🔴 Blocked | >40% variance or critical blocker | Beyond ±40% |

### Alerts

**Common Alerts:**

1. **Pulse Overdue** - Weekly pulse check missed
   - **Threshold:** 7 days since last pulse
   - **Action:** Run `/pulse` for that project

2. **Milestone Overdue** - Target date passed without completion
   - **Threshold:** 0 days past target
   - **Action:** Review milestone, adjust timeline

3. **Chronic Blocker** - Project stuck for extended period
   - **Threshold:** 2+ consecutive weeks in 🔴 status
   - **Action:** Consider pivot-or-kill decision

4. **WIP Capacity** - Too much concurrent work
   - **Threshold:** 3+ active projects
   - **Action:** Complete 1 project before starting new

5. **Portfolio Review** - Multiple ideas ready to start
   - **Threshold:** 3+ PLANNED ideas
   - **Action:** Run portfolio review to prioritize

## Data Sources

The dashboard aggregates data from:

1. **Claude Flow Memory** (primary source)
   - `execution:tracking` namespace - Active project tracking
   - `ideas:planned` namespace - Planned ideas
   - `ideas:completed` namespace - Completed projects
   - `portfolio:metrics` namespace - Performance metrics

2. **Tracking Files** (secondary/fallback)
   - `output/*-execution-tracker.md` - Per-project trackers
   - `output/portfolio.md` - Portfolio overview
   - `output/metrics/*.md` - Metrics files
   - `output/goals.yaml` - Weekly goals

**Note:** Dashboard prioritizes memory for speed but falls back to files if memory unavailable.

## Configuration

Dashboard behavior is controlled by `data/dashboard-config.yaml`:

```yaml
dashboard:
  refresh_interval: 300  # Auto-refresh every 5 minutes
  wip_limits:
    healthy: "0-2"       # 🟢
    at_capacity: "2-3"   # 🟡
    overload: "3+"       # 🔴

  alerts:
    pulse_overdue_days: 7
    milestone_overdue_days: 0
    blocked_weeks: 2
    chronic_blocker_weeks: 3

  display:
    max_active_projects: 10
    max_planned_ideas: 5
    show_completed: true
    show_killed: true
```

## Metrics Explained

### Estimate Accuracy

**Definition:** Percentage of projects completed within ±20% of planned duration

**Calculation:**
```
accuracy = (projects_within_threshold / total_completed) * 100
```

**Target:** 80%+ (good estimation skills)

### Speed Multiplier

**Definition:** Average speedup from LLM assistance

**Calculation:**
```
multiplier = avg(actual_speed / planned_speed_without_llm)
```

**Typical Values:**
- Quick Track: 15x (3-5 days → 4-8 hours)
- Standard Track: 12x (2-3 weeks → 1.5-2.5 days)
- Deep Track: 8x (3 months → 11-12 days)

### Completion Rate

**Definition:** Percentage of started projects that complete successfully

**Calculation:**
```
rate = (completed / (completed + killed)) * 100
```

**Target:** 80%+ (high success rate)

### Average Duration Variance

**Definition:** How much actual duration differs from planned duration

**Calculation:**
```
variance = ((avg_actual - avg_planned) / avg_planned) * 100
```

**Target:** ±15% or less

## Example Workflow

### Morning Routine

```bash
# 1. Check dashboard
./scripts/dashboard.sh

# Output shows:
# - WIP: 2/3 (🟢 HEALTHY)
# - Alert: Project X pulse overdue (2 days)
# - Recommendation: 3 PLANNED ideas ready

# 2. Run pulse check for overdue project
# (Execute pulse check workflow)

# 3. Review planned ideas if capacity allows
./scripts/dashboard.sh planned

# 4. Start new project if WIP allows
# (Execute kickoff workflow for highest priority idea)
```

### Weekly Review

```bash
# 1. Check extended metrics
./scripts/dashboard.sh metrics

# Review:
# - Estimate accuracy: Are estimates improving?
# - Speed multiplier: Is LLM assistance consistent?
# - Blocker patterns: Any recurring issues?

# 2. Review each active project
./scripts/dashboard.sh project 1
./scripts/dashboard.sh project 2

# Check:
# - Milestone progress
# - Weekly pulse trends
# - Recommendations

# 3. Update portfolio
# (Run portfolio review if alerts suggest)
```

### Decision Points

**Starting New Work:**
```bash
# 1. Check WIP status
./scripts/dashboard.sh

# If WIP < 3:
#   2. Review planned ideas
./scripts/dashboard.sh planned

#   3. Select highest priority
#   4. Run kickoff for selected idea
```

**Pivot-or-Kill Decision:**
```bash
# 1. Check for chronic blockers
./scripts/dashboard.sh

# If alert shows "3 weeks blocked":
#   2. Review project detail
./scripts/dashboard.sh project X

#   3. Analyze blocker history
#   4. Run pivot-or-kill framework
```

## Troubleshooting

### Dashboard Shows No Data

**Cause:** Memory unavailable and no tracking files found

**Solution:**
```bash
# 1. Check if daemon running
npx claude-flow@v3alpha daemon status

# 2. If stopped, start daemon
npx claude-flow@v3alpha daemon start

# 3. Verify memory accessible
npx claude-flow@v3alpha memory search --query "execution:tracking"

# 4. If no memory data, check for tracking files
ls output/*-execution-tracker.md
```

### WIP Count Incorrect

**Cause:** Stale data or out-of-sync tracking files

**Solution:**
```bash
# 1. Force refresh
./scripts/dashboard.sh refresh

# 2. Verify tracking files match reality
# (Manually check output/*-execution-tracker.md status)

# 3. Update memory if needed
npx claude-flow@v3alpha memory store \
  --namespace "execution:tracking" \
  --key "project-X:status" \
  --value "COMPLETED"
```

### Metrics Seem Wrong

**Cause:** Incomplete historical data or calculation error

**Solution:**
```bash
# 1. Check metrics files
cat output/metrics/metrics.md

# 2. Verify completed projects data
npx claude-flow@v3alpha memory search \
  --query "status:completed"

# 3. Manually recalculate if needed
# (Review PDCA reports and execution trackers)
```

## Customization

### Change WIP Limits

Edit `data/dashboard-config.yaml`:

```yaml
wip_limits:
  healthy: "0-1"      # More conservative (solo dev)
  at_capacity: "1-2"
  overload: "2+"
```

### Adjust Alert Thresholds

```yaml
alerts:
  pulse_overdue_days: 3       # More frequent pulse checks
  chronic_blocker_weeks: 1    # Earlier pivot decisions
```

### Hide Completed/Killed

```yaml
display:
  show_completed: false
  show_killed: false
```

## Integration

### With Weekly Planning

```bash
# Monday morning:
# 1. Review dashboard for week
./scripts/dashboard.sh

# 2. Update weekly goals based on alerts
# (Edit data/goals.yaml)

# 3. Plan week around milestones
./scripts/dashboard.sh planned
```

### With Daily TODO

```bash
# Each morning:
# 1. Check dashboard alerts
./scripts/dashboard.sh | grep "⚠️"

# 2. Prioritize TODO based on alerts
# (Address pulse checks, blockers first)
```

### With Portfolio Review

```bash
# Monthly/quarterly:
# 1. Check extended metrics
./scripts/dashboard.sh metrics

# 2. Identify patterns
# - Estimate accuracy trends
# - Common blocker types
# - Track-specific performance

# 3. Adjust processes
# (Update templates, estimation formulas, etc.)
```

## Best Practices

1. **Check Daily** - Quick dashboard review each morning (30 seconds)
2. **Act on Alerts** - Don't ignore pulse overdue or blocker warnings
3. **Respect WIP Limits** - Avoid starting new work at 🟡 or 🔴
4. **Review Metrics Weekly** - Track improvement in estimates and completion rate
5. **Use Detail Views** - Don't rely only on summary, drill down when needed
6. **Keep Data Fresh** - Run pulse checks regularly to maintain accuracy
7. **Customize for Your Workflow** - Adjust thresholds and alerts to fit your pace

## Advanced Usage

### Export Dashboard

```bash
# Generate markdown report
./scripts/dashboard.sh > output/dashboard-$(date +%Y%m%d).md

# Generate JSON for automation
./scripts/dashboard.sh --format json > output/dashboard.json
```

### Schedule Auto-Refresh

```bash
# Linux/Mac cron
# Run dashboard every 5 minutes, save to file
*/5 * * * * /path/to/scripts/dashboard.sh > /path/to/output/dashboard-latest.md

# Windows Task Scheduler
# Similar setup with PowerShell version
```

### Integrate with Notifications

```bash
# Check for critical alerts and notify
alerts=$(./scripts/dashboard.sh | grep "🔴")
if [ -n "$alerts" ]; then
  # Send notification (e.g., via notify-send, email, Slack)
  echo "$alerts" | notify-send "Life OS Critical Alert"
fi
```

## See Also

- [Execution Tracking Guide](./EXECUTION-TRACKING-GUIDE.md) - Project tracking system
- [Portfolio Management](./PORTFOLIO-MANAGEMENT.md) - Managing multiple ideas
- [PDCA Integration](./PDCA-INTEGRATION-GUIDE.md) - Continuous improvement
- [Metrics Dashboard](../output/metrics/README.md) - Detailed metrics

## Support

For issues or feature requests related to the dashboard:
1. Check this guide first
2. Review `data/dashboard-config.yaml` for configuration options
3. Verify data sources (memory and tracking files)
4. Report bugs or suggest improvements via project issues
