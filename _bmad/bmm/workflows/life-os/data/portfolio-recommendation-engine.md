# Portfolio Recommendation Engine

**Version:** 1.0.0
**Purpose:** Auto-generate recommendations for which ideas to process vs. defer
**Used by:** step-00.1-portfolio-intake.md

---

## Recommendation Algorithm

### Input Data
- Quick Scores for all ideas (sorted descending)
- User's current WIP capacity (X/3 slots)
- Complexity guesses (1-10)
- Domain diversity

### Output
- Ideas to process now (Deep Track)
- Ideas to process now (Standard Track)
- Ideas to defer (with revisit triggers)
- Capacity warnings

---

## Selection Rules

### Rule 1: Top Scorer to Deep Track (if ≥7.5)
```
IF max(Quick Scores) >= 7.5 AND complexity >= 7 THEN
  Assign top idea to Deep Track
ELSE
  Assign top idea to Standard Track
END
```

### Rule 2: Fill Remaining Capacity with Standard Track
```
remaining_capacity = WIP_limit - current_WIP - deep_track_count

FOR each idea in sorted_list (descending Quick Score):
  IF Quick Score >= 6.0 AND remaining_capacity > 0 THEN
    Assign to Standard Track
    remaining_capacity -= 1
  ELSE
    Break loop
  END
END
```

### Rule 3: Defer Low Scorers
```
FOR each unassigned idea:
  IF Quick Score >= 4.0 THEN
    Defer with revisit trigger
  ELSE
    Reject (archive)
  END
END
```

---

## Output Template

```markdown
## My Recommendations

### Process Now (Deep Track)
**{Idea A}** - Quick Score {X.X}
Rationale: {Why this deserves full analysis}
Track: DEEP (full workflow, all steps)

### Process Now (Standard Track)
**{Idea B}** - Quick Score {X.X}
**{Idea C}** - Quick Score {X.X}
Rationale: {Why these are strong candidates for streamlined process}
Track: STANDARD (quick + selective DEEP steps)

### Defer for Later Review
**{Idea D}** - Quick Score {X.X}
Reason: {Why not now - e.g., capacity, timing, dependencies}
Revisit trigger: {When to reconsider - e.g., Q2 2026, after Idea A complete}

**{Idea E}** - Quick Score {X.X}
Reason: {Why not now}
Revisit trigger: {When to reconsider}

### Archive (Reject)
**{Idea F}** - Quick Score {X.X}
Reason: Low score across all dimensions, not aligned with goals

### Capacity Check
Current WIP: {X}/3 slots
Selected for processing: {Y} ideas (1 Deep + {Y-1} Standard)
Available capacity: {3-X} slots

⚠️ Warning: {if Y > available capacity, show overcommitment warning}
```

---

## Rationale Generation Logic

**Deep Track rationale templates:**
- "Highest overall score, worth thorough analysis"
- "High impact + high complexity = needs deep planning"
- "Strategic breakthrough potential"
- "Game-changing but risky - needs Consilium + TRIZ"

**Standard Track rationale templates:**
- "Strong candidate, leverage streamlined process"
- "Balanced scores, clear execution path"
- "Good fit + feasibility, moderate impact"
- "Quick win opportunity"

**Defer rationale templates:**
- "Solid idea but capacity constrained (revisit in {timeframe})"
- "High impact but low feasibility (needs more research first)"
- "Good timing later (align with {milestone})"
- "Resource constraints (defer until {condition})"

**Reject rationale templates:**
- "Low priority across all dimensions"
- "Not aligned with current goals"
- "Weak impact + weak feasibility"
- "Better alternatives available"

---

## Capacity Warnings

**Overcommitment Warning:**
```
⚠️ Capacity Alert

You selected {Y} ideas but only have {Z} WIP slots available.

Options:
1. Prioritize top {Z} ideas (defer rest)
2. Increase WIP limit (not recommended - may reduce focus)
3. Fast-track current WIP to free slots
4. Defer some selections to next quarter

Recommendation: Process top {Z} ideas now, defer rest
```

**Underutilization Warning:**
```
ℹ️ Capacity Available

You have {Z} WIP slots but selected only {Y} ideas.

Consider:
- Adding more ideas from this batch (Quick Score >= 6.0)
- Revisiting deferred backlog
- Keeping capacity for urgent incoming requests
```

---

## Revisit Triggers

**Trigger templates:**

| Trigger Type | Template |
|--------------|----------|
| **Time-based** | "Revisit in {Q2 2026}" |
| **Milestone-based** | "After {Idea A} completes" |
| **Condition-based** | "When {budget/skills/resources} available" |
| **Quarterly** | "Include in next quarterly review" |
| **Research-based** | "After {research question} resolved" |

**Examples:**
- "Revisit in Q3 2026 when budget cycle resets"
- "After AI Product Assistant completes (estimated 3 months)"
- "When React Native expertise acquired"
- "Include in next quarterly portfolio review (April 2026)"
- "After feasibility spike on ML approach"

---

## Diversity Heuristics

**Domain Balance:**
- Warn if all selected ideas in same domain (e.g., all Work, no Personal/Health)
- Suggest: "Consider adding {domain} idea for balance"

**Complexity Balance:**
- Warn if all ideas are high complexity (8-10) - burnout risk
- Warn if all ideas are low complexity (1-3) - underutilization
- Recommend: Mix of complexity levels

**Impact Distribution:**
- Ideal: 1-2 high-impact (8-10), 2-3 medium-impact (5-7)
- Avoid: All low-impact or all high-impact (variance issue)

---

## User Override Support

**Allow manual changes to recommendations:**

```
My recommendations shown above.

Accept these?
[A]ccept all | [S]elect manually | [M]odify specific idea

If [S]elect manually:
  Show numbered list
  User types selections: "1,3,5"

If [M]odify specific idea:
  Prompt: "Which idea? [1-N]"
  Options: [Move to Deep] [Move to Standard] [Defer] [Reject]
```

---

## Example Output

```markdown
## My Recommendations

### Process Now (Deep Track)
**AI Product Assistant** - Quick Score 8.4
Rationale: Highest overall score (8.4), high complexity (7), strategic breakthrough potential. Worth full DEEP analysis including Consilium and TRIZ.

### Process Now (Standard Track)
**Personal Knowledge Base** - Quick Score 7.7
**Morning Routine App** - Quick Score 7.4
Rationale: Strong candidates with balanced scores. Clear execution path allows streamlined Standard Track (skip Consilium, lighter TRIZ).

### Defer for Later Review
**Side Hustle Research** - Quick Score 6.1
Reason: Capacity constrained (2 slots available, 3 ideas selected)
Revisit trigger: Q2 2026 or after AI Product Assistant completes

**Learn Rust** - Quick Score 5.0
Reason: Good idea but weak timing (conflicts with current priorities)
Revisit trigger: Include in next quarterly review (April 2026)

### Capacity Check
Current WIP: 1/3 slots (Fitness Tracker in progress)
Selected for processing: 3 ideas (1 Deep + 2 Standard)
Available capacity: 2 slots

✅ Capacity OK: Selected ideas fit available slots
```

---

## Integration with Memory

**Save recommendations:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "portfolio:{session-id}" \
  --key "recommendations" \
  --content "{
    deep_track: [{idea_id, score, rationale}],
    standard_track: [{idea_id, score, rationale}],
    deferred: [{idea_id, score, reason, revisit_trigger}],
    rejected: [{idea_id, score, reason}],
    capacity_status: {current, selected, available, overcommitted}
  }"
```
