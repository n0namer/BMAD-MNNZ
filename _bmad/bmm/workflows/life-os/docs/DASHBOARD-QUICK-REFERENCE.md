# Dashboard Quick Reference Card

## 🚀 Common Commands

```bash
# Full dashboard
./scripts/dashboard.sh

# Windows
.\scripts\dashboard.ps1

# Specific views
./scripts/dashboard.sh planned      # Planned ideas
./scripts/dashboard.sh metrics      # Extended metrics
./scripts/dashboard.sh project 1    # Project detail
./scripts/dashboard.sh refresh      # Force refresh
```

## 📊 Status Indicators

| Symbol | Meaning | Threshold |
|--------|---------|-----------|
| 🟢 | On Track | ±20% of plan |
| 🟡 | At Risk | 20-40% variance |
| 🔴 | Blocked | >40% variance |

## 🎯 WIP Status

| Status | Count | Action |
|--------|-------|--------|
| 🟢 HEALTHY | 0-2 | Can start new work |
| 🟡 AT CAPACITY | 2-3 | Complete 1 before starting |
| 🔴 OVERLOAD | 3+ | Must complete urgently |

## ⚠️ Common Alerts

| Alert | Threshold | Action |
|-------|-----------|--------|
| Pulse Overdue | 7 days | Run `/pulse` |
| Milestone Overdue | 0 days | Review timeline |
| Chronic Blocker | 2+ weeks | Consider pivot-or-kill |
| WIP Capacity | 3+ active | Complete before starting |

## 📈 Key Metrics

| Metric | Target | Formula |
|--------|--------|---------|
| Estimate Accuracy | 80%+ | % within ±20% |
| Speed Multiplier | 8-15x | LLM speedup |
| Completion Rate | 80%+ | Completed/Total |
| Duration Variance | ±15% | (Actual-Plan)/Plan |

## 🔧 Quick Config

Edit `data/dashboard-config.yaml`:

```yaml
# Adjust WIP limits
wip_limits:
  healthy: "0-2"
  at_capacity: "2-3"

# Change alert timing
alerts:
  pulse_overdue_days: 7
  chronic_blocker_weeks: 3

# Display options
display:
  max_active_projects: 10
  show_completed: true
```

## 📁 Data Sources

1. **Memory** (primary): `npx claude-flow@v3alpha memory search`
2. **Files** (fallback): `output/*-execution-tracker.md`

## 🎯 Decision Tree

```
Check Dashboard
├─ WIP < 3?
│  ├─ Yes → Check Planned Ideas
│  │  ├─ >0 planned → Start highest priority
│  │  └─ 0 planned → Run /consilium
│  └─ No → Complete current work first
│
├─ Red alerts?
│  ├─ Pulse overdue → Run /pulse
│  ├─ Milestone overdue → Review timeline
│  └─ 3+ weeks blocked → Pivot-or-kill decision
│
└─ All green?
   └─ Continue current work, maintain momentum
```

## 💡 Pro Tips

1. **Check daily** - 30 seconds each morning
2. **Act on alerts** - Don't ignore warnings
3. **Respect WIP** - Quality over quantity
4. **Review metrics weekly** - Track improvement
5. **Use detail views** - Drill down when needed

## 🔍 Troubleshooting

| Problem | Solution |
|---------|----------|
| No data shown | Check daemon: `npx claude-flow@v3alpha daemon status` |
| Wrong WIP count | Force refresh: `./scripts/dashboard.sh refresh` |
| Metrics incorrect | Verify memory: `npx claude-flow@v3alpha memory search -q "execution:tracking"` |

## 📚 See Also

- [Full Guide](./DASHBOARD-GUIDE.md)
- [Execution Tracking](./EXECUTION-TRACKING-GUIDE.md)
- [Configuration](../data/dashboard-config.yaml)
