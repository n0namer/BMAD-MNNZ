# Pivot-or-Kill Scoring Framework (0-40 Scale)

## Four Dimensions

### 1. Goal Alignment (0-10)

**Question:** Is this idea still aligned with quarterly/annual goals?

| Score | Meaning |
|-------|---------|
| 0-2 | No longer aligned, priorities shifted |
| 3-5 | Weakly aligned, marginal fit |
| 6-8 | Still aligned but lower priority |
| 9-10 | Highly aligned with core goals |

**Scoring tips:**
- Review original goals from `data/goals.yaml`
- Check against current quarterly objectives
- Consider life priority shifts

---

### 2. ROI Potential (0-10)

**Question:** Will benefits still exceed costs if completed?

| Score | Meaning |
|-------|---------|
| 0-2 | Costs vastly exceed benefits, negative ROI |
| 3-5 | ROI marginal, unclear value |
| 6-8 | Positive ROI but lower than expected |
| 9-10 | High ROI, benefits far exceed costs |

**Factors to consider:**
- Time invested (hours/days)
- Opportunity cost (other ideas delayed)
- Mental energy (frustration, context switches)
- Expected benefits (tangible + intangible)

---

### 3. Feasibility with Pivot (0-10)

**Question:** Does a viable alternative approach exist?

| Score | Meaning |
|-------|---------|
| 0-2 | No viable alternative, fundamental blocker |
| 3-5 | Alternative exists but high risk/cost |
| 6-8 | Clear alternative with reasonable cost |
| 9-10 | Simple pivot available, high confidence |

**Scoring tips:**
- Evaluate if pivot can solve root cause
- Estimate effort for pivot vs. starting new
- Consider evidence supporting pivot

---

### 4. Opportunity Cost (0-10, REVERSE SCORED)

**Question:** Are other ideas waiting worth pursuing?

| Score | Meaning |
|-------|---------|
| 0-2 | Many high-value ideas waiting (high opportunity cost) |
| 3-5 | Some good alternatives available |
| 6-8 | Few compelling alternatives |
| 9-10 | No better alternatives, this is best use of time |

**Scoring tips:**
- Review backlog ideas
- Compare value/effort ratios
- Consider urgency of waiting ideas
- **Higher score = LESS opportunity cost**

---

## Total Score Interpretation

**Sum all four dimensions:**

| Range | Decision | Meaning |
|-------|----------|---------|
| **0-15** | KILL | Low alignment, low ROI, high opportunity cost |
| **16-25** | PIVOT | Goal valid, approach needs change |
| **26-40** | PERSIST | Temporary setback, high confidence |

---

## Scoring Example

```markdown
| Dimension | Score | Notes |
|-----------|-------|-------|
| Goal alignment | 7 | Still aligned but lower priority than originally |
| ROI potential | 5 | Benefits unclear, costs mounting |
| Feasibility with pivot | 4 | Alternative exists but risky |
| Opportunity cost | 3 | Better ideas waiting in backlog |

Total: 19/40 → PIVOT decision
```

---

## Anti-Patterns

❌ **Don't inflate scores due to:**
- Sunk cost fallacy ("Already invested X hours")
- Optimism bias ("Just one more week")
- Status quo bias ("Killing feels like failure")

✅ **Do be honest about:**
- Current reality vs. original expectations
- Actual progress vs. planned progress
- Real alternatives available
