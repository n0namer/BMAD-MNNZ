# Batch Comparison Matrix (C3 Implementation)

## Purpose

Visual matrix for comparing 3-10 ideas simultaneously, enabling relative prioritization and tradeoff analysis.

**Key Benefits:**
- Side-by-side comparison prevents scoring inflation
- Identifies clustering and redundancy
- Highlights dimension tradeoffs (Impact vs Feasibility vs Fit)
- Forces ranking decisions (not all can be top-tier)

---

## Matrix Template

```markdown
## Portfolio Comparison Matrix

Generated: {YYYY-MM-DD HH:mm}
Session: {Session ID}
Ideas Evaluated: {Count}
Context: {Project/Domain}

### Quick Score Rankings

| Rank | Idea Name | Impact | Feasibility | Fit | Quick Score | Track Rec |
|------|-----------|--------|-------------|-----|-------------|-----------|
| 1 | {Name} | {I}/10 | {F}/10 | {Fit}/10 | **{QS}** | Deep |
| 2 | {Name} | {I}/10 | {F}/10 | {Fit}/10 | **{QS}** | Standard |
| 3 | {Name} | {I}/10 | {F}/10 | {Fit}/10 | **{QS}** | Standard |
| 4 | {Name} | {I}/10 | {F}/10 | {Fit}/10 | **{QS}** | Quick |
| 5 | {Name} | {I}/10 | {F}/10 | {Fit}/10 | **{QS}** | Defer |

*Quick Score = (Impact × 0.4) + (Feasibility × 0.3) + (Fit × 0.3)*

### Visual Distribution

**Impact vs Feasibility Grid:**
```
High Impact │
     10  │     ■ Idea D          Legend:
      9  │                       ▲ = High Fit (8-10)
      8  │  ▲ Idea A            ● = Medium Fit (5-7)
      7  │     ● Idea B         ■ = Low Fit (0-4)
      6  │           ● Idea C
      5  │
      4  │
      3  │                 ■ Idea E
      2  │
      1  │
Low      └─────────────────────────────────→
         1  2  3  4  5  6  7  8  9  10
                  Feasibility
```

### Quadrant Analysis

**Q1: High Impact, Low Feasibility (Ambitious)**
- {Ideas in this quadrant}
- **Strategy:** R&D investment, phased approach, risk mitigation
- **Timeline:** 6-12 months
- **Resource needs:** High (expert time, budget)

**Q2: High Impact, High Feasibility (Quick Wins)**
- {Ideas in this quadrant}
- **Strategy:** Prioritize immediately, allocate best resources
- **Timeline:** 1-3 months
- **Resource needs:** Medium-High

**Q3: Low Impact, High Feasibility (Easy Wins)**
- {Ideas in this quadrant}
- **Strategy:** Quick Track or batch with other work
- **Timeline:** <1 month
- **Resource needs:** Low

**Q4: Low Impact, Low Feasibility (Reject)**
- {Ideas in this quadrant}
- **Strategy:** Archive, defer indefinitely, or reject
- **Timeline:** N/A
- **Resource needs:** N/A
```

---

## Comparative Insights

### Forced Ranking Rules

1. **Not all can be 8/10** - Calibrate scores relative to each other
2. **Spread matters** - If all scores cluster 7-9, recalibrate downward
3. **Gaps reveal priorities** - Large gap between rank 2 and 3 = clear tier boundary

### Clustering Detection

**Example: Multiple ideas in same space**

If 3 ideas all score (Impact: 8, Feasibility: 6, Fit: 7):
- **Question:** Are these truly different, or variations of same concept?
- **Action:** Consider combining into single, stronger idea
- **Result:** "Mega-idea" with unified vision and scope

### Combination Opportunities

**Pattern:** 2+ small ideas → 1 bigger idea

```markdown
BEFORE:
- Idea A: Build mobile app (Impact: 6, Feasibility: 8)
- Idea B: Add notification system (Impact: 5, Feasibility: 9)

AFTER:
- Combined: Mobile app with push notifications (Impact: 8, Feasibility: 7.5)
- **Benefit:** Unified UX, shared infrastructure, higher impact
```

---

## Decision Framework

### Recommended Processing Plan

**Immediate (Process Now):**
1. **{Top idea}** - Deep Track (2-4 hours)
   - Rationale: {High impact + good feasibility + strategic fit}
   - Owner: {Person/Team}
   - Start date: {Date}

2. **{Second idea}** - Standard Track (45-60 min)
   - Rationale: {Solid scores across all dimensions}
   - Owner: {Person/Team}
   - Start date: {Date}

**Next Batch (When WIP capacity opens):**
3. **{Third idea}** - Standard Track
   - Waiting on: {Completion of #1 or #2}
   - Expected start: {Date range}

4. **{Fourth idea}** - Quick Track (15-30 min)
   - Waiting on: {Capacity or dependency}
   - Expected start: {Date range}

**Deferred (Revisit Q{N} {Year}):**
5. **{Idea name}**
   - Reason: Low strategic fit (current priorities elsewhere)
   - Reassess: {Trigger condition}

6. **{Idea name}**
   - Reason: Resource constraints (need budget/skills not available)
   - Reassess: {Date or milestone}

**Rejected:**
7. **{Idea name}**
   - Reason: Misaligned with core goals
   - Archive location: {Path/URL}

8. **{Idea name}**
   - Reason: Superseded by higher-value alternative
   - Alternative: {Link to better idea}

---

## Example Scenarios

### Example 1: Product Feature Portfolio (5 Ideas)

**Context:** SaaS product team deciding Q3 roadmap

| Rank | Feature | Impact | Feasibility | Fit | Quick Score | Track |
|------|---------|--------|-------------|-----|-------------|-------|
| 1 | API rate limiting | 9 | 8 | 9 | **8.7** | Deep |
| 2 | User analytics dashboard | 8 | 7 | 8 | **7.7** | Standard |
| 3 | Email templates | 6 | 9 | 7 | **7.2** | Quick |
| 4 | Dark mode UI | 5 | 8 | 6 | **6.2** | Defer |
| 5 | AI chatbot integration | 8 | 3 | 5 | **5.7** | Reject |

**Visual:**
```
10│
 9│  ▲ API Rate Limiting
 8│     ● User Analytics
 7│
 6│        ● Email Templates
 5│              ● Dark Mode
 4│
 3│                          ■ AI Chatbot
 2│
 1│
  └───────────────────────────────────→
  1  2  3  4  5  6  7  8  9  10
           Feasibility
```

**Insights:**
- **API Rate Limiting:** Clear winner (Q2: High Impact + High Feasibility)
- **AI Chatbot:** High impact but infeasible (need ML expertise, 6+ months)
- **Email Templates + Dark Mode:** Consider combining into "UI Enhancement Suite"

**Decision:**
1. Immediate: API Rate Limiting (Deep Track)
2. Next: User Analytics (Standard Track)
3. Quick win: Email Templates (Quick Track)
4. Defer: Dark Mode (low impact, wait for user demand)
5. Reject: AI Chatbot (pivot to rule-based bot instead)

---

### Example 2: Personal Development Goals (7 Ideas)

**Context:** Individual planning personal growth for next 6 months

| Rank | Goal | Impact | Feasibility | Fit | Quick Score | Track |
|------|------|--------|-------------|-----|-------------|-------|
| 1 | Learn Python data science | 9 | 7 | 9 | **8.4** | Deep |
| 2 | Build portfolio website | 7 | 9 | 8 | **7.9** | Standard |
| 3 | Read 12 books | 6 | 8 | 7 | **6.9** | Standard |
| 4 | Morning workout routine | 8 | 6 | 8 | **7.4** | Standard |
| 5 | Start YouTube channel | 7 | 4 | 6 | **5.8** | Defer |
| 6 | Learn guitar | 5 | 5 | 4 | **4.7** | Reject |
| 7 | Meal prep Sundays | 6 | 7 | 7 | **6.6** | Quick |

**Clustering detected:**
- Goals #1, #2, #3 all relate to **career development**
- Goals #4, #7 both relate to **health/habits**

**Combination opportunity:**
- Combine #5 (YouTube) + #1 (Python) = "Document Python learning via video tutorials"
- **New score:** Impact: 9, Feasibility: 6, Fit: 9 → **8.1** (now rank #2!)

**Revised Decision:**
1. Learn Python + document on YouTube (Deep Track) - 2 birds, 1 stone
2. Morning workouts (Standard Track) - foundational habit
3. Portfolio website (Standard Track) - career visibility
4. Meal prep (Quick Track) - supports workout goal
5. Reading goal (defer to structured "1 book/month" vs counting)
6. Guitar (reject - misaligned with career focus right now)

---

## Saving to Memory

### Storage Format

```bash
# Save matrix to global memory
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:consilium:batch-comparison:{date}" \
  --content "$(cat batch-comparison-matrix-output.md)"

# Tag for retrieval
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "bmad:consilium:insights:prioritization-{session-id}" \
  --content "Key insight: {pattern discovered from comparison}"
```

### Archive Location

**Project-specific:**
- `_bmad/bmm/workflows/life-os/output/consilium/batch-comparisons/YYYY-MM-DD-portfolio.md`

**Cross-project patterns:**
- Global memory: `shared-knowledge:bmad:consilium:batch-comparison:*`
- Search: `npx claude-flow@v3alpha memory search -q "portfolio comparison insights"`

---

## Usage Notes

1. **When to use:** Comparing 3+ ideas in same decision context
2. **Calibration:** Score first idea, then others relative to it
3. **Iteration:** First pass = rough scores, second pass = refinement
4. **Constraints:** If >10 ideas, group into themes first (reduce cognitive load)
5. **Follow-up:** Top 2-3 ideas proceed to full Consilium analysis

**File generated:** `batch-comparison-{date}.md`
**Next step:** Feed top ideas into Step 4 (Consilium) for deep analysis
