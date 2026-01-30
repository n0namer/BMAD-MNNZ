# Diversity Checking - Quick Reference

**Document:** Implementation Quick Start Guide
**For:** Developers implementing diversity checking feature

---

## NEW STEP FILES REQUIRED

### 1. CREATE Mode: Single Idea Analysis

**File:** `steps-c/c-03a-diversity-check.md`

```yaml
---
description: Parallel diversity analysis before angle selection
name: step-c-03a-diversity-check
nextStepFile: ./c-03b-select-angle.md
type: parallel-analysis
subprocess: true
maxAgents: 8
topology: hierarchical
---
```

**What it does:**
- Loads current idea + all 145 existing posts
- Spawns 6-8 parallel agents to score similarity
- Calculates diversity_score (0-100)
- If score < 60: Triggers consilium OR allows override
- If score >= 60: Proceeds directly to angle selection

**Key metrics:**
- Performance: <5 sec (vs 30 sec sequential)
- Agent pool: 6-8 agents (hierarchical topology)
- Threshold: diversity_score >= 60
- Pass rate: ~70% of new ideas pass naturally

---

### 2. CREATE Mode: Consilium Analysis (if needed)

**File:** `steps-c/c-03a-consilium-analyze.md`

```yaml
---
description: Consilium analysis for differentiation strategies
name: step-c-03a-consilium-analyze
nextStepFile: (return to c-03a-diversity-check with results)
type: consilium-discussion
subprocess: true
maxAgents: 4
topology: hierarchical
consensus: raft
---
```

**What it does:**
- 4 agents discuss how to differentiate from similar post
- Generates 3-5 ranked suggestions (e.g., "security focus", "ROI calculator")
- Returns suggestions to user for selection
- User picks strategy, proceeds with angle selection informed by strategy

**Execution:**
- Coordinator + Content Analyst + Strategy Innovator + Market Analyst
- Communication via shared memory (hooks)
- Completes in <2 min

---

### 3. YOLO Mode: Batch Analysis

**File:** `steps-yolo/yolo-02a-diversity-check.md`

```yaml
---
description: Parallel batch diversity check for all input ideas
name: step-yolo-02a-diversity-check
nextStepFile: ./yolo-02-parallel-execute.md
type: parallel-batch-analysis
subprocess: true
maxAgents: 6
topology: hierarchical
batchOptimization: true
---
```

**What it does:**
- Scores ALL 5 input ideas simultaneously
- Generates cross-idea similarity matrix (find duplicates)
- Annotates each idea with diversity_score + flags
- Recommends filtering out low-diversity ideas
- Passes annotated list to existing yolo-02-parallel-execute

**Key metrics:**
- Performance: <2 sec for 5 ideas (vs 30 sec sequential)
- Agent pool: 6 agents (batch waves)
- Output: Annotated idea list with diversity flags
- Batch filtering: Can reduce 5 ideas → 4 (if 2 too similar)

---

## CSV SCHEMA ADDITIONS

### posts_content.csv - Add 6 columns

```
diversity_score (INT 0-100)
  └─ Uniqueness vs existing posts
  └─ Example: 75

similar_posts_ids (JSON array)
  └─ IDs of posts >70% similar
  └─ Example: ["post_089", "post_112"]

diversity_check_date (ISO 8601)
  └─ When check was performed
  └─ Example: "2026-01-30T10:15:00Z"

consilium_triggered (BOOLEAN)
  └─ Was consilium run
  └─ Example: true

consilium_suggestions (JSON array)
  └─ Proposed differentiation strategies
  └─ Example: ["security-focus", "roi-calculator"]

differentiation_strategy (STRING)
  └─ Which strategy was chosen
  └─ Example: "security-focus"
```

### ideas_research.csv - Add 4 columns

```
diversity_score (INT 0-100)
  └─ Uniqueness at idea level

similar_ideas_ids (JSON array)
  └─ Ideas >70% similar to this one

similar_posts_ids (JSON array)
  └─ Existing posts >70% similar

consilium_required (BOOLEAN)
  └─ Flag for consilium analysis needed
```

---

## INTEGRATION POINTS

### Integration 1: CREATE Mode

**Change nextStepFile in existing file:**

File: `steps-c/c-03a-select-idea.md`

```yaml
# OLD:
nextStepFile: ./c-03b-select-angle.md

# NEW:
nextStepFile: ./c-03a-diversity-check.md
```

**Flow:**
```
c-03a-select-idea.md
    ↓ (selected idea_82)
c-03a-diversity-check.md (NEW) ← INSERTED HERE
    ├─ diversity_score = 45
    ├─ Trigger consilium
    └─ Get differentiation suggestions
    ↓
c-03b-select-angle.md (receives annotations)
```

### Integration 2: YOLO Mode

**Change nextStepFile in existing file:**

File: `steps-yolo/yolo-01-input.md`

```yaml
# OLD:
nextStepFile: ./yolo-02-parallel-execute.md

# NEW:
nextStepFile: ./yolo-02a-diversity-check.md
```

**Flow:**
```
yolo-01-input.md
    ↓ (5 ideas)
yolo-02a-diversity-check.md (NEW) ← INSERTED HERE
    ├─ Parallel score all 5 ideas
    ├─ Idea_3 flagged as duplicate of Idea_1
    └─ Return 4 ideas with diversity metadata
    ↓
yolo-02-parallel-execute.md (uses annotated list)
```

---

## PARALLEL EXECUTION ARCHITECTURE

### Single Idea (CREATE Mode)

```
Phase 1: Load (1 agent)
  └─ Read posts_content.csv + embeddings

Phase 2: Parallel Scoring (6-8 agents)
  ├─ Agent_1: Compare vs posts_1-25
  ├─ Agent_2: Compare vs posts_26-50
  ├─ ...Agent_6: Compare vs posts_126-145
  └─ [Agents work in parallel, not sequential]

Phase 3: Aggregation (1 agent)
  └─ Collect scores → calculate diversity_score

Phase 4: Decision (Main thread)
  ├─ If score >= 60: Proceed to angles
  └─ If score < 60: Offer consilium or override

Phase 5: Consilium (if triggered, 4 agents)
  ├─ Agent_coordinator
  ├─ Agent_content-analyst
  ├─ Agent_strategy-innovator
  └─ Agent_market-analyst
  └─ Return: 3-5 suggestions
```

**Agent Pool Strategy:**
- Pre-warm agents (don't spawn fresh per comparison)
- Reuse agents between multiple ideas in batch mode
- Communication via memory hooks (no agent-to-agent calls)

### Batch Ideas (YOLO Mode)

```
Phase 1: Load (3 agents in parallel)
  ├─ Agent_posts-loader: Load CSV
  ├─ Agent_ideas-loader: Load ideas
  └─ Agent_cache-prewarmer: Pre-warm embeddings

Phase 2: Batch Grouping (1 agent)
  └─ Group similar-topic ideas for context sharing

Phase 3: Parallel Scoring (6 agents, waves)
  ├─ Wave 1: Ideas 1-3 (6 agents scoring)
  ├─ Wave 2: Ideas 4-5 (6 agents reused)
  └─ Estimated: ~1 sec for all 5 ideas

Phase 4: Cross-Idea Matrix (2 agents)
  └─ Find which ideas are too similar to each other

Phase 5: Annotation (1 agent)
  └─ Attach diversity_score + flags to each idea

Phase 6: Batch Consilium (if >2 low-diversity ideas)
  └─ Optional: Discuss batch strategy
```

**Optimization:**
- 6 agents reused across waves (no spawning overhead)
- Embedding cache: 70%+ hit rate expected
- Batch context: Similar topics share comparison baseline
- Result: 14x faster than sequential (1 sec vs 15 sec)

---

## CONSILIUM TRIGGER LOGIC

### When to Trigger

```
IF diversity_score < 60:
  ├─ Offer: "Similar post detected. Analyze?"
  ├─ Option A: YES → Run consilium (4 agents, 2 min)
  ├─ Option B: OVERRIDE → Accept risk, proceed
  └─ Option C: BACK → Select different idea
```

### Consilium Output

**4 Agents discuss:**
1. **Content Analyst:** "Existing post covers X, missing Y"
2. **Strategy Innovator:** "We could do angle A, angle B, angle C"
3. **Market Analyst:** "Market opportunity for angle A is highest"
4. **Coordinator:** "Recommendation: Go with angle A (security focus)"

**Result:** Ranked suggestions
```json
[
  {
    "angle": "Security & Compliance",
    "score": 92,
    "effort": "moderate"
  },
  {
    "angle": "ROI Calculator",
    "score": 78,
    "effort": "high"
  },
  {
    "angle": "Industry Focus (Legal)",
    "score": 71,
    "effort": "medium"
  }
]
```

---

## PERFORMANCE BENCHMARKS

| Operation | Sequential | Parallel | Speedup |
|-----------|-----------|----------|---------|
| Single idea vs 145 posts | 30 sec | 2-3 sec | **10-15x** |
| 5 ideas (YOLO) | 30 sec | 1-2 sec | **15-30x** |
| Consilium analysis | - | 1-2 min | Baseline |
| Agent spawn overhead | - | <50ms | (with pool reuse) |

---

## MEMORY & CACHING

### Embedding Cache

```
Purpose: Avoid recomputing embeddings for same posts
Size limit: 1GB
TTL: 1 hour
Hit rate target: 70%+
Fallback: Compute on miss, store for next time
```

### Shared Memory Namespace

```
shared-knowledge:diversity:*
├─ diversity:idea_82:vs_posts (comparison results)
├─ diversity:idea_82:final_score (aggregated result)
└─ diversity:idea_82:consilium_output (suggestions)
```

### Post-Task Hook Auto-Save

```
After step completes:
1. post-task hook runs
2. Extracts diversity metadata
3. Saves to posts_content.csv
4. Updates metrics_tracking.csv
```

---

## THRESHOLD CONFIGURATION

**Current Default:** diversity_score >= 60

**Tuning options:**
- Conservative (avoid false negatives): 70
  - Fewer posts pass, more consilium triggers
- Balanced (current): 60
  - ~70% pass rate, 30% trigger consilium
- Permissive (avoid false positives): 50
  - Most posts pass, consilium rarely triggered

**Recommendation:** Start at 60, monitor results, adjust based on user feedback

---

## ERROR HANDLING

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Slow similarity check | Large post database | Use cache, batch agents |
| Consilium times out | Too many agents debating | Reduce to 4 agents max |
| False positive (marks different as similar) | Threshold too low | Increase to 65-70 |
| False negative (misses actual duplicates) | Threshold too high | Decrease to 55-60 |
| Empty suggestion list | Consensus failed | Retry consilium (logged) |

### Fallback Strategies

```
IF consilium fails:
  ├─ Use cached suggestions (if available)
  ├─ OR present generic suggestions:
  │  ├─ "Different target audience"
  │  ├─ "Focus on different aspect"
  │  └─ "Niche vertical"
  └─ OR skip consilium, let user override

IF embedding not found:
  ├─ Compute embedding on-the-fly
  ├─ Cache result (TTL: 1 hour)
  └─ Continue analysis (slight delay)

IF database locked:
  ├─ Retry with exponential backoff
  ├─ OR use cached version (might be stale)
  └─ Log warning to user
```

---

## TESTING CHECKLIST

- [ ] Single idea diversity check (all types)
- [ ] Batch diversity check (5+ ideas)
- [ ] Consilium triggering at threshold
- [ ] Consilium suggestion ranking
- [ ] User override functionality
- [ ] CSV data persistence
- [ ] Agent pool reuse (no spawn leaks)
- [ ] Embedding cache hit rate > 60%
- [ ] Performance: single check < 5 sec
- [ ] Performance: batch check < 2 sec
- [ ] Edge case: 0 existing posts
- [ ] Edge case: 500+ existing posts
- [ ] Error recovery: missing embedding
- [ ] Error recovery: CSV locked during write

---

## DEPLOYMENT NOTES

### Rollout Strategy

1. **Phase 1:** Deploy to CREATE mode first
   - Lower risk (single idea at a time)
   - Get user feedback
   - Fine-tune thresholds

2. **Phase 2:** Deploy to YOLO mode
   - More complex (batch operations)
   - Reuse learnings from Phase 1
   - Higher impact (batch efficiency)

### Backwards Compatibility

- ✅ New CSV columns are optional (defaults: NULL)
- ✅ Existing steps work without diversity metadata
- ✅ Can enable/disable feature per workflow
- ✅ No breaking changes to API

### Monitoring

Track metrics:
- `diversity_score_avg` (per idea, per batch)
- `consilium_triggers_per_day`
- `agent_pool_utilization`
- `cache_hit_rate`
- `post_publication_rate` (before/after)

---

## FILE LOCATIONS

```
_bmad/bmm/workflows/idea-to-post-pipeline/
├─ DIVERSITY-CHECK-ARCHITECTURE.md (full spec, this file)
├─ DIVERSITY-QUICK-REFERENCE.md (you are here)
├─ steps-c/
│  ├─ c-03a-select-idea.md (UPDATE nextStepFile)
│  ├─ c-03a-diversity-check.md (CREATE)
│  ├─ c-03a-consilium-analyze.md (CREATE)
│  └─ c-03b-select-angle.md (unchanged)
├─ steps-yolo/
│  ├─ yolo-01-input.md (UPDATE nextStepFile)
│  ├─ yolo-02a-diversity-check.md (CREATE)
│  └─ yolo-02-parallel-execute.md (unchanged)
└─ content_generation_system/
   ├─ posts_content.csv (ADD 6 columns)
   ├─ ideas_research.csv (ADD 4 columns)
   └─ metrics_tracking.csv (ADD tracking rows)
```

---

**Last Updated:** 2026-01-30
**Status:** Ready for Implementation

