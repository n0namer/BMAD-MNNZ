---
name: 'step-v-05-retrospective'
description: 'Run retrospective protocol for completed idea'
---

# Step V-05: Retrospective

## STEP GOAL

Learn from completed idea execution to calibrate future estimates and improve recommendations.

## WHEN TO USE

After completing or killing an idea to extract learnings and update calibration data.

## MANDATORY EXECUTION RULES

- 🛑 NEVER generate content without user input
- 📖 Read complete step file before taking action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ Speak in `{communication_language}` config style
- 🎯 Compare planned vs actual execution data
- 🎯 Analyze retrospective in subprocess (Pattern 2)
- 💬 Return structured retrospective findings and calibration updates, not raw execution logs
- 📊 Calculate accuracy metrics
- 💡 Document learnings and adjustments
- 💾 Store calibration updates in memory

## MANDATORY SEQUENCE

### 1-4. Retrospective Analysis Protocol (Subprocess)

**Launch a subprocess that:**
1. Loads data/retrospective-protocol.md
2. Loads data/retrospective-calibration.md
3. Loads data/retrospective-questions.md
4. Loads planned data from Deep Plan (step-08)
5. Loads actual execution data (step-x-01, step-x-02)
6. Calculates accuracy metrics
7. Asks retrospective questions
8. Returns structured retrospective findings

```
[C] - Continue with subprocess analysis
[M] - Manual data entry (no subprocess)
[A] - Abort retrospective
```

**Subprocess loads:**
- **Planned:** Estimated duration, complexity score, Speed Multiplier, assumptions
- **Actual:** Start date, completion date, actual complexity, blockers, pivots

**Subprocess calculates:**
- **Accuracy Ratio:** `Actual Duration / Planned Duration`
- **Speed Multiplier Validation:** `Actual Speed / Assumed Speed`
- **Complexity Delta:** `Actual Complexity - Planned Complexity`

📖 **Calibration formulas:** `data/retrospective-calibration.md`

**Subprocess asks:**

**Q1: Timeline Accuracy**
- [E] Excellent (±20%), [G] Good (±20-50%), [P] Poor (>50%)
- If [P], ask follow-up: Why? ([U]nderestimated, [O]verestimated, [B]lockers, [S]cope creep, [X]other)

**Q2-Q6:** Complexity assessment, Speed Multiplier validation, what went well, what could improve, recommendations

📖 **Full question set:** `data/retrospective-questions.md`

**Subprocess returns:**
```json
{
  "idea_id": "...",
  "planned": {
    "duration_weeks": 4,
    "complexity": 6,
    "speed_multiplier": 1.5
  },
  "actual": {
    "duration_weeks": 5.5,
    "complexity": 7,
    "blockers": [...]
  },
  "metrics": {
    "accuracy_ratio": 1.375,
    "timeline_accuracy": "good",
    "complexity_delta": 1
  },
  "learnings": {
    "went_well": [...],
    "could_improve": [...],
    "recommendations": [...]
  },
  "calibration_adjustments": {
    "domain": "...",
    "old_multiplier": 1.5,
    "new_multiplier": 1.7,
    "confidence": "medium",
    "sample_size": 3
  }
}
```

**Context savings:** ~1,000 lines (execution logs + protocols) → ~80 lines (structured retrospective)

**Graceful fallback:** If subprocess unavailable, load data and protocols in main context.

**If [M] (Manual):** Ask user to provide planned and actual data directly without subprocess.

---

### 5. Generate Retrospective Report

Create report using template from `data/retrospective-report-template.md`:

**Report structure:**
- Timeline comparison table
- What went well / could improve
- Key learnings
- Calibration adjustments
- Recommendations
- Confidence level + sample size

Save to: `output/retrospective-{idea-id}-{date}.md`

Ask user:
```
[S] - Save report and update calibration
[E] - Edit report before saving
[A] - Abort without saving
```

---

### 6. Store in Memory

**If [S]:**

Store retrospective, calibration updates, and learned patterns using commands from `data/retrospective-calibration.md`.

**Memory namespaces:**
- `retrospective:idea-{id}:{date}` - Full retrospective data
- `shared-knowledge:calibration:speed-multiplier:{domain}` - Adjusted multipliers
- `shared-knowledge:patterns:retrospective:{pattern-name}` - Learned patterns

---

### 7. Update Calibration Files

**Update data/speed-multipliers.yaml:**
- Add calibration_history entry (date, domain, multipliers, adjustment, reason, sample_size)
- Recalculate running average for domain

**Update data/mcda-methodology.yaml:**
- If complexity scoring needs adjustment, add to complexity_calibration section

📖 **Calibration methods:** `data/retrospective-calibration.md`

---

### 8. Completion Message

```
✅ **Retrospective Complete!**

📊 **Summary:**
- Timeline accuracy: {Excellent/Good/Poor}
- Speed Multiplier: {Before}x → {After}x ({domain})
- Key learning: {Main insight}

📁 **Saved:**
- Retrospective report: output/retrospective-{id}-{date}.md
- Memory storage: retrospective:idea-{id}:{date}
- Calibration update: {domain} multiplier adjusted

🔮 **Impact on future estimates:**
Future {domain} ideas will use {adjusted}x Speed Multiplier based on {sample_size} completed ideas.

---

[R]eturn to quarterly review
[V]iew full retrospective report
[D]one
```

## MENU OPTIONS

After completion:
- **[R]** - Return to quarterly review
- **[V]** - View full retrospective report
- **[D]** - Done

## SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- Planned vs actual data compared
- Accuracy metrics calculated
- Learnings documented
- Calibration updates stored in memory
- System gets smarter for next time

### ❌ SYSTEM FAILURE
- No data comparison
- No calibration updates
- Learnings not stored

**Master Rule:** Always store retrospective learnings in memory for future improvement.

## RELATED FILES

📖 Questions: `data/retrospective-questions.md`
📖 Calibration: `data/retrospective-calibration.md`
📖 Report Template: `data/retrospective-report-template.md`
