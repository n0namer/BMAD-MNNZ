# Pulse Tracker Update Protocol

## Save Locations

### 1. Append to Execution Tracker

**File:** `output/{idea-id}-execution-tracker.md`

```markdown
## Week {N} Pulse - {Date}

**Progress:** {Summary from Q1}
**Status:** 🟢/🟡/🔴
**Blockers:** {From Q2}
**Next Priority:** {From Q3}

---
```

### 2. Update Memory

**Namespace:** `execution:tracking`

```bash
npx claude-flow@v3alpha memory store \
  --namespace "execution:tracking" \
  --key "{idea-id}:pulse-week-{N}" \
  --content "{
    date: 'YYYY-MM-DD',
    progress: 'summary',
    status: 'green|yellow|red',
    blockers: ['list'],
    nextPriority: 'objective',
    completionPercent: N
  }"
```

### 3. Update Idea Metadata

**File:** `data/goals.yaml`

```yaml
ideas:
  - id: {idea-id}
    lastPulse: {YYYY-MM-DD}
    currentStatus: green|yellow|red
    completionPercent: {N}
    weeksInProgress: {N}
    consecutiveRedWeeks: {N}  # For alert triggers
```

---

## Output Deliverables

1. **Pulse Report** - Markdown file appended to execution tracker
2. **Memory Entry** - Structured data for trend analysis
3. **Updated Metadata** - goals.yaml with latest status
4. **Alerts (if triggered)** - Notifications for escalation
