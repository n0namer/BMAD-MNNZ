# M7: Retrospective Protocol - Implementation Summary

## Overview

Implemented comprehensive retrospective protocol to learn from execution outcomes and calibrate future estimates.

**Status:** ✅ COMPLETE

**Date:** 2026-02-05

---

## Files Created

### 1. Core Protocol Document
**File:** `data/retrospective-protocol.md`

**Purpose:** Complete retrospective methodology

**Contents:**
- When to run retrospectives (completed, killed, quarterly, manual)
- Data collection (planned vs actual)
- Calculated metrics (accuracy ratio, speed multiplier validation, complexity delta)
- 6 retrospective questions (timeline, complexity, speed, wins, improvements, recommendations)
- Calibration learning system
- Report template
- Integration points
- Memory storage

### 2. Dedicated Retrospective Step
**File:** `steps-v/step-v-05-retrospective.md`

**Purpose:** Full guided retrospective workflow

**Contents:**
- Load planned data from Deep Plan (step-08)
- Load actual data from Execution Tracking (step-x-01, step-x-02)
- Calculate accuracy metrics automatically
- Guide through 6 retrospective questions
- Generate structured report
- Store in memory
- Update calibration files (speed-multipliers.yaml, complexity-calibration.yaml)

**Estimated time:** 5-10 minutes

### 3. Calibration Database
**File:** `data/complexity-calibration.yaml`

**Purpose:** Track and adjust complexity scoring weights

**Contents:**
- 7 complexity factors with adjustable weights
- Calibration history (date, factor, adjustment, reason, confidence)
- Learned patterns from retrospectives
- Domain-specific adjustments
- Common pitfalls discovered
- Accuracy metrics tracking

**Initial state:** Baseline (not yet calibrated)

---

## Files Modified

### 1. Step 09 - Complete
**File:** `steps-c/step-09-complete.md`

**Changes:**
- Added retrospective trigger at completion
- 3 options: [R] Run Now, [L] Later, [S] Skip
- Integrated into success criteria

### 2. Step V-04 - Quarterly Review
**File:** `steps-v/step-04-quarterly-review.md`

**Changes:**
- Added Section 13: Calibration Review
- Loads all retrospectives from quarter
- Calculates accuracy distribution (excellent/good/poor)
- Identifies Speed Multiplier adjustments per domain
- Detects common patterns across completed ideas
- Updates data/speed-multipliers.yaml
- Updates data/complexity-calibration.yaml (via complexity-calibration.yaml)

**Integration:**
- Search memory: `retrospective:*` namespace
- Display aggregate accuracy metrics
- Propose calibration adjustments
- Store quarterly calibration updates

### 3. Speed Multipliers Database
**File:** `data/speed-multipliers.yaml`

**Changes:**
- Added `calibration_history` section (retrospective-driven adjustments)
- Added `adjusted_multipliers` section (running averages after calibration)
- Updated metadata (version 2.0, integration with retrospective)
- Added `calibration_status`, `total_retrospectives`, `average_accuracy` fields

### 4. Step X-04 - Pivot or Kill
**File:** `steps-x/step-x-04-pivot-or-kill.md`

**Changes:**
- Enhanced KILL retrospective template
- Added calibration data section (planned vs actual complexity/timeline)
- Added "Why estimates were off" capture
- Store retrospective in memory (`retrospective:idea-{id}:killed:{date}`)
- Learnings feed into quarterly calibration

---

## Workflow Integration

### Learning Loop

```
┌─────────────────────────────────────────────────────┐
│ 1. PLAN (Step 08 - Deep Plan)                      │
│    - Estimate timeline: 2 weeks                     │
│    - Estimate complexity: 6/10                      │
│    - Speed Multiplier: 10x                          │
│    - Store in Deep Plan output                      │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│ 2. EXECUTE (Steps 1-8, Step X-01 tracking)         │
│    - Track actual timeline                          │
│    - Record blockers                                │
│    - Note complexity encountered                    │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│ 3. COMPLETE or KILL (Step 09 or Step X-04)         │
│    - Trigger retrospective prompt                   │
│    - Options: [R] Run, [L] Later, [S] Skip         │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│ 4. RETROSPECTIVE (Step V-05)                       │
│    - Compare planned vs actual                      │
│    - Calculate accuracy ratio                       │
│    - Document learnings                             │
│    - Save to memory                                 │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│ 5. CALIBRATION (Quarterly Review - Step V-04)      │
│    - Aggregate all retrospectives from quarter      │
│    - Calculate accuracy distribution                │
│    - Identify patterns (e.g., frontend 30% longer)  │
│    - Adjust Speed Multipliers                       │
│    - Update complexity weights                      │
│    - Store adjustments in memory                    │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│ 6. IMPROVED ESTIMATES (Next Planning - Step 08)    │
│    - Use adjusted Speed Multiplier: 10x → 9x       │
│    - Use updated complexity weights                 │
│    - Apply learned patterns                         │
│    - Better estimates for similar ideas             │
└─────────────────────────────────────────────────────┘
```

---

## Memory Storage Structure

### Per-Idea Retrospective
**Namespace:** `retrospective`

**Key:** `idea-{id}:{date}` or `idea-{id}:killed:{date}`

**Content:**
```json
{
  "idea_id": "001",
  "idea_name": "Katana",
  "status": "COMPLETED" | "KILLED",
  "planned_duration": "2 weeks",
  "actual_duration": "2.5 weeks",
  "accuracy": "good",
  "variance": "+25%",
  "planned_complexity": 6,
  "actual_complexity": 7,
  "speed_multiplier_assumed": "10x",
  "speed_multiplier_actual": "8x",
  "learnings": ["Frontend polish took longer", "LLM excellent for backend"],
  "adjustments": ["Increase frontend complexity weight"]
}
```

### Calibration Updates
**Namespace:** `shared-knowledge`

**Keys:**
- `calibration:speed-multiplier:{domain}:Q{N}`
- `calibration:complexity:{factor}:Q{N}`
- `patterns:retrospective:{pattern-name}`

**Purpose:** Cross-project learning (available to all projects globally)

---

## Success Metrics

### Retrospective Completion Rate
**Target:** 80%+ of completed ideas have retrospectives

**Tracking:** Count retrospectives vs completed ideas per quarter

### Estimate Accuracy Improvement
**Target:** 80%+ ideas within ±30% variance

**Tracking:**
- Accuracy ratio distribution (excellent/good/poor)
- Trend over time (improving/stable/declining)

### Speed Multiplier Calibration
**Target:** ±20% accuracy on Speed Multiplier

**Tracking:**
- Actual vs assumed multiplier
- Per-domain adjustments
- Confidence levels (high/medium/low based on sample size)

### Complexity Scoring Accuracy
**Target:** ±2 points average variance

**Tracking:**
- Actual vs planned complexity scores
- Per-factor weight adjustments
- Learned patterns application

---

## Usage Examples

### Scenario 1: Completed Idea (Excellent Accuracy)
```
Idea: "Katana"
Planned: 2 weeks, 6/10 complexity, 10x multiplier
Actual: 2.1 weeks, 6/10 complexity, 9.5x multiplier
Variance: +5% (excellent)

Retrospective:
- Timeline: Excellent (within ±20%)
- Complexity: Accurate (±0 points)
- Speed Multiplier: Accurate (10x → 9.5x = -5%)

Calibration: No adjustments needed
Confidence: High (estimates were accurate)
```

### Scenario 2: Completed Idea (Poor Accuracy)
```
Idea: "Content Platform MVP"
Planned: 1 week, 4/10 complexity, 15x multiplier
Actual: 3 weeks, 7/10 complexity, 5x multiplier
Variance: +200% (poor)

Retrospective:
- Timeline: Poor (>50% variance)
- Complexity: Underestimated by 3 points
- Speed Multiplier: Overestimated (15x → 5x = -67%)

Learnings:
- Frontend polish took 2x longer than expected
- LLM not as effective for UI work
- CMS integration more complex than assumed

Calibration:
- Speed Multiplier: saas_web_app 15x → 10x (-33%)
- Complexity: Increase ui_polish weight 0.10 → 0.15 (+50%)
- Pattern: "Frontend polish always takes longer" (add 1.4x multiplier)

Confidence: Medium (1 idea, need more data)
```

### Scenario 3: Killed Idea
```
Idea: "Personal CRM App"
Planned: 4 weeks, 7/10 complexity, 8x multiplier
Actual: 3 weeks invested before kill, 9/10 complexity encountered
Status: KILLED (no backend skills, ROI turned negative)

Retrospective:
- Timeline: N/A (didn't complete)
- Complexity: Underestimated by 2 points
- Speed Multiplier: Lower than expected (backend learning curve)

Learnings:
- Underestimated backend complexity
- Skill gap (no PostgreSQL experience)
- Better alternatives exist (use existing tools)

Calibration:
- Pattern: "First-time tech has learning curve" (add 50-100% buffer)
- Common pitfall: "Backend skills required for custom CRM" (use no-code instead)

Confidence: Medium (killed idea, partial data)
```

---

## Quarterly Calibration Example

**Q1 2026 - End of Quarter:**

**Retrospectives completed:** 5 ideas

**Accuracy distribution:**
- Excellent (±20%): 2 ideas (40%)
- Good (±20-50%): 2 ideas (40%)
- Poor (>50%): 1 idea (20%)

**Average variance:** +28% (good, within target)

**Speed Multiplier adjustments:**
- saas_web_app: 10x → 9x (-10%, "Frontend polish underestimated")
- api_backend: 15x → 18x (+20%, "LLM excellent at API boilerplate")

**Complexity adjustments:**
- ui_polish: 0.10 → 0.15 (+50%, "Consistently underestimated")

**Learned patterns:**
- "Frontend polish always takes longer" (8/10 web apps, +30-50%)
- "LLM excellent for API/backend" (5/5 backend APIs, -20% faster)

**Applied adjustments:**
- Update speed-multipliers.yaml
- Update complexity-calibration.yaml
- Store in memory for all projects

**Impact on next estimates:**
- Future saas_web_app ideas use 9x multiplier (not 10x)
- UI complexity weighted higher (0.15 instead of 0.10)
- Frontend estimates include 1.4x buffer

**Confidence:** Medium (5 ideas), improving to High (10+ ideas)

---

## Integration with Other Systems

### Step 08 (Deep Plan)
**Input:** Uses adjusted Speed Multipliers and complexity weights

**Output:** Better timeline estimates based on learnings

### Step V-04 (Quarterly Review)
**Input:** All retrospectives from quarter

**Output:** Calibration adjustments, learned patterns

### Step X-04 (Pivot or Kill)
**Input:** Captures calibration data even for killed ideas

**Output:** Retrospective with learnings for future filtering

### Memory System
**Input:** Per-idea retrospectives + quarterly calibrations

**Output:** Cross-project learning (globally shared knowledge)

---

## Best Practices

### When to Run Retrospectives

**Always:**
- After idea completion (Step 09)
- After idea killed (Step X-04)
- Quarterly review (Step V-04)

**Optional:**
- Mid-project (if major pivot occurred)
- Ad-hoc (user explicitly requests)

### Time Investment

**Per-idea retrospective:** 5-10 minutes

**Quarterly calibration:** 20-30 minutes (aggregate analysis)

**ROI:** High (prevents future estimate errors, saves weeks of wasted effort)

### Honesty Protocol

**Be brutally honest:**
- Don't sugarcoat failures
- Capture what went wrong
- Avoid sunk cost fallacy
- Focus on learning, not blame

**Ask "why" repeatedly:**
- Why was estimate off?
- Why did that assumption fail?
- Why did LLM underperform?
- Why did blocker emerge?

---

## Future Enhancements

### Potential Additions
1. **Automated pattern detection** (ML on retrospectives)
2. **Cross-user calibration** (aggregate across all Life OS users)
3. **Domain-specific templates** (specialized questions per domain)
4. **Visual dashboards** (accuracy trends over time)
5. **Confidence intervals** (probabilistic estimates instead of point estimates)

### Success Indicators
- Estimate accuracy improves from 50% → 80%+ over 6 months
- Speed Multiplier adjustments stabilize (fewer adjustments needed)
- Learned patterns reused across multiple ideas
- Users proactively run retrospectives (not just when prompted)

---

## Completion Checklist

✅ Core protocol document created (`data/retrospective-protocol.md`)
✅ Dedicated step file created (`steps-v/step-v-05-retrospective.md`)
✅ Calibration database created (`data/complexity-calibration.yaml`)
✅ Step 09 modified (retrospective trigger)
✅ Step V-04 modified (calibration review)
✅ Speed multipliers updated (calibration_history + adjusted_multipliers)
✅ Step X-04 modified (capture learnings from killed ideas)
✅ Memory storage structure defined
✅ Integration points documented
✅ Success metrics defined

---

**Implementation Status:** ✅ COMPLETE

**Ready for:** Real-world usage tracking and calibration

**Next step:** Execute ideas, complete retrospectives, observe accuracy improvement over time

---

**Last Updated:** 2026-02-05
