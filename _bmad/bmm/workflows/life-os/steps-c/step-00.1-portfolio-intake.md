---
id: step-00.1-portfolio-intake
title: Portfolio Intake (Batch Collection)
version: 1.0.0
status: active
category: collection
track: batch
estimated_duration: 15-30 min
requires:
  - data/batch-quick-score.md
  - data/portfolio-collection-protocol.md
  - data/portfolio-quick-score-ui.md
  - data/portfolio-recommendation-engine.md
outputs:
  - memory: portfolio:{session-id}:intake
  - memory: portfolio:{session-id}:quick-scores
  - routing: step-01 (with track pre-selection)
---

# Step 00.1: Portfolio Intake (Batch Collection)

## STEP GOAL

Collect 3-10 ideas for batch comparison and data-driven track selection (Deep vs. Standard).

**Use When:** Multiple ideas, quarterly planning, backlog grooming, user says "compare several things"
**Skip When:** Single urgent idea, partial analysis exists, emergency decision

---

## MANDATORY EXECUTION RULES

**ALWAYS:** Min 3 ideas | Score 3 dimensions | Auto-save to memory | Comparison table | Track recommendations | WIP capacity check | Save deferred ideas
**NEVER:** Process one-by-one | Skip user approval | Overcommit WIP | Skip quick scoring

---

## WORKFLOW SEQUENCE

### Phase 1: Collection (5-15 min)

**Reference:** `data/portfolio-collection-protocol.md`

**Steps:** Prompt count (3-10) | Collect name, description, domain, complexity (1-10) | Auto-save | Display summary
**Time:** 2-3 min/idea

---

### Step-Specific Subprocess Optimization Rules

- 🎯 Score EACH idea in parallel subprocess (Pattern 2 + 4)
- ⚡ 3x-10x speedup via parallel execution
- 🚫 DO NOT BE LAZY - score ALL ideas in parallel
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess unavailable, achieve outcome in main context thread

### Batch Quick-Scoring (Parallel Subprocesses)

**DO NOT BE LAZY - Launch parallel subprocesses:**
- Subprocess per idea (3-10 subprocesses running concurrently)

**Each subprocess:**
1. Loads data/batch-quick-score.md
2. Scores one idea on 3 criteria:
   - Impact (1-10)
   - Feasibility (1-10)
   - Fit with goals (1-10)
3. Calculates quick-score average
4. Returns structured score to parent

**Subprocess returns (per idea):**
```json
{
  "idea_name": "AI Assistant",
  "impact_score": 8,
  "feasibility_score": 7,
  "fit_score": 8,
  "quick_score": 7.7,
  "rationale": "High impact, moderate feasibility"
}
```

**Parent aggregates all scores into comparison table**

**Performance gain:** 18-30 min sequential → 6-10 min parallel (3x speedup)

**Graceful fallback:** If parallel subprocess unavailable, score sequentially in main context.

---

### Phase 2: Quick Scoring (6-30 min)

**Reference:** `data/batch-quick-score.md`

| Dimension | Weight | 0-3 | 4-7 | 8-10 |
|-----------|--------|-----|-----|------|
| Impact | 40% | Minor | Meaningful | Transformative |
| Feasibility | 30% | Blockers | Challenging | Clear path |
| Fit | 30% | Misaligned | Reasonable | Perfect timing |

**Formula:** `Quick Score = (Impact × 0.4) + (Feasibility × 0.3) + (Fit × 0.3)` → Range: 0.0-10.0
**Time:** 2-3 min/idea

---

### Phase 3: Comparison & Selection (2-5 min)

**Reference:** `data/portfolio-quick-score-ui.md`

**Table:** Sort by Quick Score | Show all dimensions | Track suggestions | Insights
**Menu:** [S]elect | [M]odify scores | [A]uto-accept | [C]omments | [R]e-sort | [D]one

---

### Phase 4: Recommendations (Auto-Generated)

**Reference:** `data/portfolio-recommendation-engine.md`

| Quick Score | Complexity | Track | Action |
|-------------|-----------|-------|--------|
| ≥7.5 | ≥7 | Deep | Process with full elicitation |
| ≥6.0 | <7 | Standard | Streamlined elicitation |
| 4.0-5.9 | Any | Defer | Save with revisit trigger |
| <4.0 | Any | Reject | Archive |

**Outputs:** Process now | Defer list | WIP capacity check | Overcommitment warnings

---

### Phase 5: Routing

**Deep Track:** Score ≥7.5 + Complexity ≥7 → step-01 full elicitation + all DEEP steps
**Standard Track:** Score ≥6.0 + Complexity <7 → step-01 streamlined + selective DEEP steps
**Deferred:** Save scores, reason, revisit trigger

**Context passed to step-01:** `{idea_id, quick_score, track, total_evaluated, rank, comparative_advantage}`

---

## MEMORY SAVE PROTOCOL

```bash
# 1. Intake: portfolio:{session-id}:intake:complete → {date, ideas, duration}
# 2. Scores: portfolio:{session-id}:quick-scores:matrix → {scores, selection, deferred, tracks}
# 3. Deferred: portfolio:deferred:{idea-id} → {idea, score, reason, trigger}
# 4. Insights: shared-knowledge:bmad:portfolio:comparison-pattern → {insights}
```

---

## QUALITY GATES

**Required:** ≥3 ideas scored | Complete dimensions | Table reviewed | WIP aligned | Deferred triggers | User approval
**Red Flags:** All <6.0 | 5+ selected | Inconsistent scores | No diversity

---

## SUCCESS CRITERIA

✅ 3-10 ideas with metadata | All dimensions scored | Table reviewed | Tracks assigned | Saved to memory | User approved | Context prepared
❌ <3 ideas | Incomplete scoring | No approval | WIP violations

---

## EXAMPLE SESSION

```
Claude: How many ideas? [3-10]
User: 5

[Collects metadata → Auto-saves → Scores 3 dimensions]

Portfolio Comparison:
| # | Idea | I | F | Fit | Score | Track |
|---|------|---|---|-----|-------|-------|
| 1 | AI Assistant | 9 | 7 | 8 | 8.1 | Deep |
| 2 | Knowledge Base | 8 | 8 | 7 | 7.7 | Standard |
| 3 | Morning Routine | 6 | 9 | 8 | 7.4 | Standard |
| 4 | Side Hustle | 7 | 5 | 6 | 6.1 | Defer |
| 5 | Learn Rust | 5 | 6 | 4 | 5.0 | Defer |

WIP: 1/3 used | [A]uto-accept | [S]elect | [M]odify
User: A

Starting AI Assistant (Deep Track) → step-01...
```

---

## NOTES

**Data Files:** `batch-quick-score.md`, `portfolio-collection-protocol.md`, `portfolio-quick-score-ui.md`, `portfolio-recommendation-engine.md`
**Time:** Collection 6-30min | Scoring 6-30min | Comparison 2-5min | **Total: 15-65min** (scales with count)
