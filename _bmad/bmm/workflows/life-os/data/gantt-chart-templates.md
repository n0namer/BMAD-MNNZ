# Gantt Chart Templates

## ASCII Gantt Format

### Standard 80-Character Layout

```
Project: {project_name}
Timeline: {start_date} → {end_date}

         |  Feb   |  Mar   |  Apr   |
         | W1| W2| W3| W4| W5| W6| W7| W8|
─────────┼───┴───┴───┴───┴───┴───┴───┴───┤
M1 Found │████████░░░░░░░░░░░░░░░░░░░░░░░░│ 2w
M2 Core  │        ████████████░░░░░░░░░░░░│ 3w
M3 UX    │        ░░░░████████░░░░░░░░░░░░│ 2.5w (1.5w slack)
M4 Integ │                    ████████░░░░│ 2w
─────────┴────────────────────────────────┘

Legend:
████ = Work period (critical path bold)
░░░░ = Slack/buffer time
│    = Dependency marker
TODAY: {marker if within range}
```

### Detailed ASCII with Dependencies

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                          PROJECT GANTT CHART
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Project: {project_name}
Timeline: {start_date} → {end_date} ({total_weeks} weeks)
Generated: {ISO_datetime}

         │      February      │        March       │       April        │
         │ W06 │ W07 │ W08 │ W09 │ W10 │ W11 │ W12 │ W13 │ W14 │ W15 │ W16 │
─────────┼─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┤
M1       │█████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
Foundation (2w)   ↓
─────────┼───────────────────────────────────────────────────────────────────┤
M2       │░░░░░░░░░░░░░██████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
Core (3w)         └─── depends on M1                              ↓
─────────┼───────────────────────────────────────────────────────────────────┤
M3       │░░░░░░░░░░░░░░░░░░░██████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
UX (2.5w)         └─── depends on M1, has 1.5w slack              │
─────────┼───────────────────────────────────────────────────────────────────┤
M4       │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░│
Integration (2w)  └───────────────────────────── depends on M2, M3
─────────┴───────────────────────────────────────────────────────────────────┘

CRITICAL PATH: M1 ══> M2 ══> M4 (7 weeks, highlighted with ██)

Legend:
  ████  Work period (on critical path)
  ░░░░  Buffer/slack time
  ─↓──  Dependency arrow
  ══>   Critical path flow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Rendering Rules

1. Each █ = 0.25 weeks (adjust based on total_weeks)
2. Critical path milestones use BOLD or different character
3. Slack shown as ░ after work period
4. Dependencies shown with │ markers
5. TODAY marker if project in progress
6. Grid resolution:
   - ≤8 weeks: Show days (daily grid)
   - ≤16 weeks: Show weeks (weekly grid)
   - >16 weeks: Show weeks with month labels (monthly grouping)

## Mermaid Gantt Format

### Basic Structure

````markdown
```mermaid
gantt
    title {project_name} - Project Timeline
    dateFormat YYYY-MM-DD
    excludes weekends

    section Milestones
    M1: Foundation           :crit, m1, {start_date}, {duration}d
    M2: Core Features        :crit, m2, after m1, {duration}d
    M3: UX Design            :m3, after m1, {duration}d
    M4: Integration          :crit, m4, after m2 m3, {duration}d

    section Critical Path
    Critical Path Duration   :milestone, crit, {end_date}, 0d
```
````

### Complete Mermaid Document

````markdown
# Project Gantt Chart - {project_name}

Generated: {ISO_datetime}
Timeline: {start_date} → {end_date}
Critical Path: M1 → M2 → M4

## Visual Timeline

```mermaid
gantt
    title {project_name} - Project Timeline
    dateFormat YYYY-MM-DD
    excludes weekends
    todayMarker stroke-width:3px,stroke:#f00

    section Foundation Phase
    M1: Foundation & Setup   :crit, active, m1, {m1_start}, {m1_duration}d

    section Development Phase
    M2: Core Features        :crit, m2, after m1, {m2_duration}d
    M3: UX Design            :m3, after m1, {m3_duration}d

    section Integration Phase
    M4: Integration & Test   :crit, m4, after m2 m3, {m4_duration}d

    section Project Milestone
    Project Complete         :milestone, crit, done, {end_date}, 0d
```

## Milestone Details

| ID | Name | Start | End | Duration | Dependencies | Critical |
|----|------|-------|-----|----------|--------------|----------|
| M1 | {name} | {start} | {end} | {weeks}w | - | YES |
| M2 | {name} | {start} | {end} | {weeks}w | M1 | YES |
| M3 | {name} | {start} | {end} | {weeks}w | M1 | NO |
| M4 | {name} | {start} | {end} | {weeks}w | M2, M3 | YES |

## Critical Path Analysis

**Path:** M1 → M2 → M4
**Duration:** {total_weeks} weeks
**Risk Level:** {LOW|MEDIUM|HIGH}

### Slack Analysis

| Milestone | Slack | Earliest Start | Latest Start |
|-----------|-------|----------------|--------------|
| M1 | 0w | {date} | {date} |
| M2 | 0w | {date} | {date} |
| M3 | {slack}w | {date} | {date} |
| M4 | 0w | {date} | {date} |

## Notes

- Critical path milestones marked with `:crit`
- Weekends excluded from duration calculation
- Today marker shows current progress point
````

## Export Formats

### CSV Format

```csv
milestone_id,name,start_date,end_date,duration_weeks,dependencies,critical_path
M1,Foundation,2026-02-07,2026-02-21,2,,YES
M2,Core Features,2026-02-21,2026-03-14,3,M1,YES
M3,UX Design,2026-02-21,2026-03-07,2.5,M1,NO
M4,Integration,2026-03-14,2026-03-28,2,"M2,M3",YES
```

### iCal Format

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Life OS//Gantt Export//EN
BEGIN:VEVENT
DTSTART:20260207
DTEND:20260221
SUMMARY:[M1] Foundation
DESCRIPTION:Project: {project_name}\nDuration: 2 weeks\nCritical: YES
END:VEVENT
...
END:VCALENDAR
```

### JSON Format

```json
{
  "project_id": "{project_id}",
  "project_name": "{project_name}",
  "generated_at": "{ISO_datetime}",
  "timeline": {
    "start_date": "{YYYY-MM-DD}",
    "end_date": "{YYYY-MM-DD}",
    "total_weeks": {weeks},
    "working_days": {days}
  },
  "milestones": [
    {
      "id": "M1",
      "name": "{name}",
      "start_date": "{YYYY-MM-DD}",
      "end_date": "{YYYY-MM-DD}",
      "duration_weeks": {weeks},
      "dependencies": [],
      "on_critical_path": true,
      "slack_weeks": 0,
      "position": {
        "row": 0,
        "start_column": 0,
        "width": {grid_units}
      }
    }
  ],
  "critical_path": {
    "milestones": ["M1", "M2", "M4"],
    "total_weeks": {weeks},
    "percentage_of_timeline": {percent}
  },
  "render_options": {
    "grid_resolution": "weekly",
    "exclude_weekends": true,
    "show_today_marker": true
  }
}
```

## Configuration Schema

```yaml
gantt_config:
  grid_resolution: weekly  # daily | weekly | monthly
  exclude_weekends: true
  show_today_marker: true
  output_formats: [mermaid, ascii, json]
  color_scheme: default
  critical_path_style: bold
  dependency_arrows: true
```
