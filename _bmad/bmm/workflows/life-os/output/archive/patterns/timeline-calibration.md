# Timeline Calibration Archive

**Purpose:** Track estimate accuracy over time to calibrate Speed Multipliers and complexity scoring.

**Last Updated:** 2026-02-05
**Total Retrospectives:** 0
**Calibration Status:** Not enough data (need 3+ ideas)

---

## Calibration Metrics

### Overall Accuracy

**Target:** 80%+ ideas within ±30% variance

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Ideas within ±20% | 0/0 (N/A) | 60%+ | ⏳ Awaiting data |
| Ideas within ±30% | 0/0 (N/A) | 80%+ | ⏳ Awaiting data |
| Ideas with >50% variance | 0/0 (N/A) | <10% | ⏳ Awaiting data |
| Average variance | N/A | ±25% | ⏳ Awaiting data |

---

## Speed Multiplier Calibration

### Current Multipliers (Default)

Based on data/speed-multipliers.yaml:

| Context | Default | Calibrated | Sample Size | Confidence |
|---------|---------|------------|------------|------------|
| LLM Backend | 12x | - | 0 | N/A |
| LLM Frontend | 8x | - | 0 | N/A |
| LLM Full-Stack | 10x | - | 0 | N/A |
| Non-LLM | 1x | - | 0 | N/A |

**Status:** Using default multipliers (no calibration data yet)

---

## Complexity Factor Calibration

### Current Factors (Default)

| Factor | Weight | Calibrated | Accuracy | Sample Size |
|--------|--------|------------|----------|------------|
| Technical Complexity | 1.0 | - | N/A | 0 |
| Frontend Complexity | 1.0 | - | N/A | 0 |
| Backend Complexity | 1.0 | - | N/A | 0 |
| Integration Complexity | 1.0 | - | N/A | 0 |
| Learning Curve (new tech) | 1.0 | - | N/A | 0 |

**Recommendations:** After 5+ ideas, will calibrate based on observed patterns

---

## Variance Patterns

### By Complexity Level

*No data yet*

**Will show:**
- Do higher complexity ideas always overrun?
- Do lower complexity ideas finish early?
- What's the optimal complexity threshold?

### By Domain

*No data yet*

**Will show:**
- Which domains have best estimate accuracy?
- Which domains consistently overrun?
- Domain-specific adjustment factors

### By Track (Standard vs Deep)

*No data yet*

**Will show:**
- Does Deep Track have better/worse accuracy?
- Are estimates systematically off for one track?

---

## Calibration Adjustment History

### Q1 2026

*No adjustments yet (awaiting first retrospectives)*

**Future format:**
```yaml
adjustment_id: cal-2026-q1-001
date: 2026-03-31
factor: speed_multiplier_backend
old_value: 12x
new_value: 15x
reason: "8 completed ideas averaged 15x actual (not 12x)"
sample_size: 8
confidence: HIGH
applied_by: Quarterly Review
```

---

## Estimation Accuracy Trends

```
Target: Improving accuracy quarter over quarter

Q1 2026: N/A (baseline)
Q2 2026: TBD
Q3 2026: TBD
Q4 2026: TBD

Goal: Reach 80%+ accuracy by Q4 2026
```

---

## Common Estimate Errors

*Will populate after analyzing retrospectives*

**Examples of future insights:**
- Frontend UI polish always +40%
- First-time tech adds +75%
- Integration with 3rd party APIs +50%
- Testing/QA consistently underestimated by 30%

---

## Calibration Update Log

*No calibrations yet.*

**Next calibration:** Q1 2026 Quarterly Review (after 3+ retrospectives)

---

## Calibration Protocol

**Triggered by:** Quarterly Review (Step V-04)

**Process:**
1. Load all retrospectives from quarter
2. Calculate variance for each completed idea
3. Group by domain, complexity, track
4. Identify systematic patterns
5. Propose adjustments to speed multipliers and factors
6. User approves adjustments
7. Update configuration files
8. Store in memory for future reference

**Minimum Data Requirements:**
- 3+ ideas for initial calibration
- 5+ ideas for HIGH confidence adjustments
- 10+ ideas for domain-specific calibration

---

**Status:** Ready to receive retrospective data
**Next Action:** Complete ideas and run Step 09 retrospective
