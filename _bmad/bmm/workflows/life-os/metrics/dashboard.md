# Life OS Metrics Dashboard

## Overview

The Life OS Metrics Dashboard provides real-time tracking of PDCA (Plan-Do-Check-Act) cycle progress, helping you maintain alignment with goals, optimize productivity, and prevent burnout.

## Core Metrics

### 1. Completion Rate
**Definition**: Percentage of planned tasks completed within timeframe

**Calculation**:
```
Completion Rate = (Completed Tasks / Total Planned Tasks) × 100
```

**Tracking Frequency**:
- Daily: Tasks completed today vs planned
- Weekly: Weekly task completion
- Monthly: Monthly task completion

**Healthy Range**: 70-85% (100% indicates under-planning, <60% indicates over-commitment)

**Data Source**: `todos/archive/*.md` vs `todos/*.md`

---

### 2. Velocity
**Definition**: Rate of task completion over time

**Calculation**:
```
Velocity = Tasks Completed / Time Period
Trend = (Current Period Velocity / Previous Period Velocity - 1) × 100
```

**Tracking Frequency**:
- Daily average (7-day rolling)
- Weekly average
- Monthly trend

**Healthy Range**: Stable ±10% week-over-week (high variance indicates inconsistent planning)

**Data Source**: `todos/archive/*.md` timestamps

---

### 3. Focus Time
**Definition**: Actual deep work hours vs planned hours

**Calculation**:
```
Focus Time Efficiency = (Actual Focus Hours / Planned Focus Hours) × 100
```

**Tracking Frequency**:
- Daily: Hours logged today
- Weekly: Total focus hours
- Monthly: Average daily focus time

**Healthy Range**: 4-6 hours/day of deep work (Cal Newport's recommendations)

**Data Source**: `reviews/daily/*.md` time tracking, calendar data

---

### 4. Goal Progress
**Definition**: Percentage progress toward hierarchical goals

**Calculation**:
```
Goal Progress = (Completed Milestones / Total Milestones) × 100
```

**Tracking Levels**:
- Annual: % toward yearly OKRs
- Half-Year (H1/H2): % toward semester goals
- Quarterly: % toward Q1/Q2/Q3/Q4 goals
- Monthly: % toward monthly targets

**Healthy Range**: ≥50% by mid-period (frontloading prevents cramming)

**Data Source**: `goals.yaml`, `reviews/weekly/*.md`, `reviews/monthly/*.md`

---

### 5. Alignment Score
**Definition**: Percentage of daily tasks directly supporting strategic goals

**Calculation**:
```
Alignment Score = (Goal-Aligned Tasks / Total Tasks) × 100
```

**Tracking Frequency**:
- Daily: % aligned tasks today
- Weekly: Average daily alignment
- Monthly: Alignment trend

**Healthy Range**: ≥60% (Pareto principle: 60% strategic, 40% operational)

**Data Source**: `todos/*.md` (tasks tagged with goal IDs), `goals.yaml`

---

### 6. Burnout Risk
**Definition**: Indicators of overwork and insufficient recovery

**Calculation**:
```
Burnout Risk = Weighted Average of:
- Weekly Hours: (Hours > 50) × 30%
- Rest Days: (Days < 1/week) × 25%
- Focus Decline: (Velocity Drop > 20%) × 20%
- Health Neglect: (Health Tasks < 3/week) × 15%
- Sleep Deficit: (Sleep < 7h avg) × 10%
```

**Risk Levels**:
- Low: <30%
- Medium: 30-60%
- High: 60-80%
- Critical: >80%

**Tracking Frequency**:
- Weekly assessment
- Monthly trend analysis

**Data Source**: `reviews/weekly/*.md`, `calendar.ics`, `health/*.md`

---

### 7. Domain Balance
**Definition**: Time distribution across life domains

**Calculation**:
```
Domain Balance = (Hours in Domain / Total Hours) × 100
```

**Domains**:
- **Finance**: Revenue generation, budgeting, investments
- **Business**: Strategy, operations, growth
- **Health**: Exercise, nutrition, sleep, mental health
- **Personal**: Family, hobbies, learning, social

**Healthy Distribution** (example targets):
- Finance: 25-35%
- Business: 30-40%
- Health: 15-20%
- Personal: 10-15%

**Tracking Frequency**:
- Weekly: Domain hours logged
- Monthly: Balance trend

**Data Source**: `todos/*.md` (domain tags), `reviews/weekly/*.md`

---

## Data Sources

### Primary Sources

| Source | Location | Content | Update Frequency |
|--------|----------|---------|------------------|
| **Active TODOs** | `todos/*.md` | Current tasks | Real-time |
| **Archived TODOs** | `todos/archive/*.md` | Completed tasks | Daily |
| **Daily Reviews** | `reviews/daily/*.md` | Time tracking, reflections | Daily |
| **Weekly Reviews** | `reviews/weekly/*.md` | Goal progress, learnings | Weekly |
| **Monthly Reviews** | `reviews/monthly/*.md` | Metrics, adjustments | Monthly |
| **Goals Definition** | `goals.yaml` | OKRs, milestones | Quarterly |
| **Calendar Data** | `calendar.ics` | Scheduled events | Real-time |
| **Health Logs** | `health/*.md` | Sleep, exercise, nutrition | Daily |

### Data Format Expectations

**TODO Files** (`todos/*.md`):
```markdown
## 2026-02-05 Wednesday

- [ ] #finance #goal-annual-1 Review Q1 budget allocation ~2h
- [x] #business #goal-q1-2 Draft partnership proposal ~3h
- [x] #health Morning workout ~1h
```

**Daily Review** (`reviews/daily/2026-02-05.md`):
```markdown
## Time Tracking
- Focus Time: 5.5h (planned: 6h)
- Meetings: 2h
- Admin: 1.5h

## Tasks Completed: 8/10 (80%)
```

**Goals File** (`goals.yaml`):
```yaml
annual:
  - id: goal-annual-1
    description: "Increase revenue by 30%"
    milestones: 4
    completed: 1
```

---

## Visualization

### 1. CLI Display (ASCII Charts)

**Daily Summary**:
```
╔════════════════════════════════════════════════╗
║        LIFE OS DASHBOARD - 2026-02-05         ║
╠════════════════════════════════════════════════╣
║ Completion Rate:  80% ████████░░              ║
║ Focus Time:       5.5h / 6h (92%)             ║
║ Alignment Score:  75% ███████░░░              ║
║ Burnout Risk:     25% ██░░░░░░░░ [LOW]        ║
╠════════════════════════════════════════════════╣
║ VELOCITY (7-day avg): 12 tasks/day ▲ +5%     ║
║ DOMAIN BALANCE:                                ║
║   Finance:   30% ███░░░░░░░                   ║
║   Business:  35% ████░░░░░░                   ║
║   Health:    20% ██░░░░░░░░                   ║
║   Personal:  15% █░░░░░░░░░                   ║
╚════════════════════════════════════════════════╝
```

**Weekly Trend**:
```
COMPLETION RATE (Last 7 Days)
100% ┤
 90% ┤     ●
 80% ┤   ●   ● ●
 70% ┤ ●       ● ●
 60% ┤           ●
     └─────────────
     Mon Wed Fri Sun
```

### 2. CSV Export

**Format** (`metrics/exports/metrics-2026-02.csv`):
```csv
Date,Completion_Rate,Velocity,Focus_Time,Goal_Progress,Alignment_Score,Burnout_Risk,Finance_Pct,Business_Pct,Health_Pct,Personal_Pct
2026-02-01,75,11,5.0,45,70,20,28,38,18,16
2026-02-02,82,12,5.5,46,72,22,30,35,20,15
2026-02-03,78,13,6.0,48,75,25,32,33,19,16
```

### 3. HTML Dashboard (Optional)

**Features**:
- Interactive charts (Chart.js)
- Date range filtering
- Drill-down to daily details
- Export to PDF

**Location**: `metrics/html/dashboard.html`

---

## Metrics Calculation Scripts

### Script 1: Data Collection (`collect_metrics.py`)

**Purpose**: Extract raw data from source files

**Input**: `todos/`, `reviews/`, `goals.yaml`

**Output**: `metrics/raw/data-YYYY-MM-DD.json`

**Run Frequency**: Daily (automated via cron/Task Scheduler)

**Key Functions**:
- Parse TODO markdown files
- Extract time tracking from reviews
- Calculate task completion rates
- Map tasks to goal IDs

---

### Script 2: Metrics Calculator (`calculate_metrics.py`)

**Purpose**: Compute all 7 core metrics

**Input**: `metrics/raw/data-*.json`

**Output**: `metrics/calculated/metrics-YYYY-MM-DD.json`

**Run Frequency**: Daily + on-demand

**Key Functions**:
- Aggregate multi-day data
- Calculate trends (velocity, burnout risk)
- Compute weighted scores (alignment, balance)

---

### Script 3: Dashboard Generator (`generate_dashboard.py`)

**Purpose**: Create visualizations

**Input**: `metrics/calculated/metrics-*.json`

**Output**:
- CLI: stdout (ASCII charts)
- CSV: `metrics/exports/metrics-YYYY-MM.csv`
- HTML: `metrics/html/dashboard.html`

**Run Frequency**: On-demand via CLI

**Usage**:
```bash
# Show today's metrics
python metrics/scripts/generate_dashboard.py --mode cli --date today

# Generate weekly report
python metrics/scripts/generate_dashboard.py --mode cli --period week

# Export to CSV
python metrics/scripts/generate_dashboard.py --mode csv --period month
```

---

### Script 4: Alert System (`alert_system.py`)

**Purpose**: Monitor thresholds and send notifications

**Input**: `metrics/calculated/metrics-*.json`

**Output**: Notifications (stdout, email, Slack)

**Run Frequency**: Daily (automated)

**Alert Triggers**:

| Condition | Severity | Action |
|-----------|----------|--------|
| Burnout Risk >70% | **CRITICAL** | Immediate notification + suggest rest day |
| Goal Progress <50% (mid-quarter) | **HIGH** | Weekly reminder + suggest re-prioritization |
| Completion Rate <60% (3 days) | **MEDIUM** | Suggest reducing commitments |
| Focus Time <4h/day (5 days) | **MEDIUM** | Review time management |
| Alignment Score <50% (7 days) | **HIGH** | Schedule strategic review |

**Example Alert**:
```
⚠️ CRITICAL ALERT ⚠️
Burnout Risk: 75% (HIGH)

Indicators:
- Weekly Hours: 56h (target: <50h)
- Rest Days: 0 this week (target: ≥1)
- Sleep Avg: 6.2h (target: ≥7h)

Recommendation:
Block tomorrow as recovery day. Delegate 3 tasks.
```

---

## Automated Collection Setup

### Linux/macOS (cron)

**Edit crontab**:
```bash
crontab -e
```

**Add entries**:
```cron
# Collect metrics daily at 11:59 PM
59 23 * * * cd /path/to/life-os && python metrics/scripts/collect_metrics.py

# Run alerts daily at 8:00 AM
0 8 * * * cd /path/to/life-os && python metrics/scripts/alert_system.py

# Generate weekly report on Sundays at 6:00 PM
0 18 * * 0 cd /path/to/life-os && python metrics/scripts/generate_dashboard.py --mode cli --period week
```

### Windows (Task Scheduler)

**PowerShell Script** (`metrics/scripts/run_metrics.ps1`):
```powershell
cd D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os
python metrics\scripts\collect_metrics.py
python metrics\scripts\alert_system.py
```

**Task Scheduler Setup**:
1. Open Task Scheduler
2. Create Task → "Life OS Metrics Collection"
3. Trigger: Daily at 11:59 PM
4. Action: Run PowerShell script
5. Settings: Run whether user is logged on or not

---

## Dependencies

### Python Requirements (`metrics/requirements.txt`)

```txt
# Data processing
pandas>=2.0.0
pyyaml>=6.0

# Visualization
matplotlib>=3.7.0  # Optional, for HTML dashboard
plotly>=5.14.0     # Optional, for interactive charts

# Utilities
python-dateutil>=2.8.0
```

**Install**:
```bash
pip install -r metrics/requirements.txt
```

---

## Usage Examples

### Daily Check-In
```bash
# Quick status
python metrics/scripts/generate_dashboard.py --mode cli --date today

# Output:
# Completion Rate: 80%
# Focus Time: 5.5h / 6h
# Burnout Risk: 25% [LOW]
```

### Weekly Review
```bash
# Full weekly report
python metrics/scripts/generate_dashboard.py --mode cli --period week

# Export to CSV for further analysis
python metrics/scripts/generate_dashboard.py --mode csv --period week
```

### Goal Progress Check
```bash
# Check quarterly goal progress
python metrics/scripts/calculate_metrics.py --metric goal_progress --level quarterly

# Output:
# Q1 2026 Progress: 48% (Target: ≥50% by mid-quarter)
# At Risk Goals:
# - goal-q1-2: 35% (behind by 15%)
```

### Burnout Prevention
```bash
# Check burnout indicators
python metrics/scripts/alert_system.py --check burnout

# Output:
# Burnout Risk: 35% [MEDIUM]
# Weekly Hours: 52h (target: <50h)
# Recommendation: Schedule 1 rest day this week
```

---

## Maintenance

### Data Retention
- **Raw Data**: Keep 90 days (`metrics/raw/`)
- **Calculated Metrics**: Keep 1 year (`metrics/calculated/`)
- **Exports**: Keep 2 years (`metrics/exports/`)

**Cleanup Script** (`metrics/scripts/cleanup.py`):
```bash
# Remove data older than retention period
python metrics/scripts/cleanup.py --dry-run
python metrics/scripts/cleanup.py --execute
```

### Backup
```bash
# Weekly backup to cloud storage
tar -czf life-os-metrics-$(date +%Y%m%d).tar.gz metrics/
# Upload to Google Drive / Dropbox / S3
```

---

## Customization

### Adding Custom Metrics

**1. Define Metric** (in `metrics/config.yaml`):
```yaml
custom_metrics:
  - name: "Learning Hours"
    description: "Time spent on skill development"
    calculation: "sum(tasks[tag='learning'].hours)"
    healthy_range: "5-7 hours/week"
    data_source: "todos/*.md"
```

**2. Implement Calculation** (in `calculate_metrics.py`):
```python
def calculate_learning_hours(data, period='week'):
    learning_tasks = [t for t in data['tasks'] if 'learning' in t['tags']]
    return sum(t['hours'] for t in learning_tasks)
```

**3. Add to Dashboard** (in `generate_dashboard.py`):
```python
def render_learning_hours(metrics):
    hours = metrics['learning_hours']
    print(f"Learning Hours: {hours}h/week")
```

---

## Troubleshooting

### Issue: Metrics Not Updating

**Check**:
1. Data collection script running? (`metrics/raw/` has recent files)
2. File permissions correct?
3. Python dependencies installed?

**Fix**:
```bash
# Manual collection
python metrics/scripts/collect_metrics.py --verbose

# Check logs
tail -n 50 metrics/logs/collection.log
```

### Issue: Incorrect Calculations

**Check**:
1. Data format matches expectations? (see "Data Format Expectations")
2. Goal IDs consistent across files?
3. Timezones correct in timestamps?

**Fix**:
```bash
# Validate data format
python metrics/scripts/validate_data.py

# Recalculate from scratch
python metrics/scripts/calculate_metrics.py --recalculate-all
```

---

## Best Practices

### 1. Consistent Tagging
- Always use standardized tags in TODOs: `#finance`, `#business`, `#health`, `#personal`
- Link tasks to goal IDs: `#goal-annual-1`, `#goal-q1-2`

### 2. Accurate Time Tracking
- Log actual time spent (not just planned)
- Update daily reviews with focus time

### 3. Regular Reviews
- Check dashboard daily (2 min)
- Deep dive weekly (15 min)
- Adjust targets quarterly

### 4. Act on Alerts
- Burnout risk >60%? Schedule recovery immediately
- Goal progress <50% mid-quarter? Re-prioritize ruthlessly
- Alignment <60%? Say "no" to non-strategic tasks

---

## Future Enhancements

### Phase 2 (Optional)
- [ ] Machine learning predictions (velocity forecasting)
- [ ] Mobile app integration (iOS/Android dashboard)
- [ ] Real-time sync with calendar APIs (Google Calendar, Outlook)
- [ ] Slack/Discord bot for daily updates
- [ ] Comparative benchmarking (vs past quarters/years)

### Phase 3 (Advanced)
- [ ] Team dashboard (for business domain collaboration)
- [ ] Integration with financial tools (Mint, YNAB)
- [ ] Health tracking APIs (Fitbit, Apple Health)
- [ ] AI-powered recommendations (GPT-4 analysis)

---

## Appendix: File Structure

```
metrics/
├── dashboard.md              # This file
├── config.yaml               # Metric definitions, thresholds
├── requirements.txt          # Python dependencies
├── scripts/
│   ├── collect_metrics.py    # Data extraction
│   ├── calculate_metrics.py  # Metric computation
│   ├── generate_dashboard.py # Visualization
│   ├── alert_system.py       # Threshold monitoring
│   ├── cleanup.py            # Data retention management
│   └── validate_data.py      # Format validation
├── raw/
│   └── data-YYYY-MM-DD.json  # Daily raw data
├── calculated/
│   └── metrics-YYYY-MM-DD.json # Computed metrics
├── exports/
│   └── metrics-YYYY-MM.csv   # CSV exports
├── html/
│   └── dashboard.html        # Interactive web dashboard
└── logs/
    └── collection.log        # Error logs
```

---

## Quick Reference

### Commands
```bash
# Daily check
python metrics/scripts/generate_dashboard.py --mode cli --date today

# Weekly report
python metrics/scripts/generate_dashboard.py --mode cli --period week

# Export CSV
python metrics/scripts/generate_dashboard.py --mode csv --period month

# Run alerts
python metrics/scripts/alert_system.py

# Validate data
python metrics/scripts/validate_data.py
```

### Healthy Ranges
- Completion Rate: 70-85%
- Velocity: Stable ±10%
- Focus Time: 4-6h/day
- Goal Progress: ≥50% by mid-period
- Alignment Score: ≥60%
- Burnout Risk: <30%
- Domain Balance: Finance 25-35%, Business 30-40%, Health 15-20%, Personal 10-15%

---

**Last Updated**: 2026-02-05
**Version**: 1.0.0
**Maintainer**: Life OS System
