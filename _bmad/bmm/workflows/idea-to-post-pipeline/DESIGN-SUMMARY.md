# Diversity Checking Architecture - Design Summary

**Prepared:** 2026-01-30
**Status:** Complete & Ready for Implementation
**Effort Estimate:** 2-3 developer-days

---

## WHAT IS BEING DESIGNED?

A **parallel diversity checking system** that prevents similar content generation in the idea-to-post-pipeline by:

1. **Pre-generation analysis** - Check if new idea is too similar to existing posts before writing
2. **Parallel execution** - Score against 145+ existing posts simultaneously (6-8 agents)
3. **Intelligent consilium** - When similarity detected, spawn 4 agents for differentiation analysis
4. **Batch optimization** - Score multiple ideas in parallel (YOLO mode)

---

## NEW STEP FILES REQUIRED

### 1. CREATE Mode: Single Idea Analysis

**File:** `steps-c/c-03a-diversity-check.md`

```
What: Check if idea is too similar to existing posts
Where: Between "select idea" and "select angle"
How: Parallel agents score similarity
Time: <5 sec
Output: diversity_score (0-100) + decision gate
```

**Key features:**
- Loads existing posts database (145+ posts)
- Spawns 6-8 parallel agents for similarity scoring
- Calculates diversity_score (inverse of max similarity)
- If score >= 60: Proceed to angle selection
- If score < 60: Offer consilium analysis or override

### 2. CREATE Mode: Consilium Analysis

**File:** `steps-c/c-03a-consilium-analyze.md`

```
What: Discuss how to differentiate from similar post
When: Triggered by diversity_check if similarity detected
How: 4 agents debate, propose angles
Time: ~2 min
Output: 3-5 ranked differentiation suggestions
```

**Key features:**
- 4 agents with expert roles: coordinator, analyst, strategist, market analyst
- Communication via shared memory (asynch)
- Consensus via RAFT (coordinator maintains truth)
- Returns ranked suggestions (e.g., "security focus", "ROI calculator")
- User selects preferred strategy

### 3. YOLO Mode: Batch Analysis

**File:** `steps-yolo/yolo-02a-diversity-check.md`

```
What: Score all input ideas for diversity simultaneously
Where: Between "input" and "parallel execute"
How: Batch waves with agent pool reuse
Time: <2 sec for 5 ideas
Output: Annotated idea list with diversity flags
```

**Key features:**
- Parallel load: 3 agents load posts + ideas + embeddings
- Batch grouping: Group similar-topic ideas
- Parallel scoring: 6 agents in waves (agents reused between waves)
- Cross-idea matrix: Detect duplicates within batch
- Annotated output: Each idea tagged with diversity_score + flags

---

## INTEGRATION POINTS

### Integration 1: CREATE Mode

**Current flow:**
```
c-03a-select-idea.md → c-03b-select-angle.md → c-03c-draft.md
```

**New flow:**
```
c-03a-select-idea.md
    ↓
[NEW] c-03a-diversity-check.md
    ├─ If diversity_score >= 60 → proceed
    └─ If diversity_score < 60 → offer consilium
    ↓
c-03b-select-angle.md → c-03c-draft.md
```

**Changes needed:**
- Update `c-03a-select-idea.md` → nextStepFile = `./c-03a-diversity-check.md`
- Update `c-03a-diversity-check.md` → nextStepFile = `./c-03b-select-angle.md`

### Integration 2: YOLO Mode

**Current flow:**
```
yolo-01-input.md → yolo-02-parallel-execute.md → yolo-03-self-check.md
```

**New flow:**
```
yolo-01-input.md
    ↓
[NEW] yolo-02a-diversity-check.md
    └─ Returns: Annotated idea list (4-5 ideas, filtered)
    ↓
yolo-02-parallel-execute.md → yolo-03-self-check.md
```

**Changes needed:**
- Update `yolo-01-input.md` → nextStepFile = `./yolo-02a-diversity-check.md`
- Update `yolo-02a-diversity-check.md` → nextStepFile = `./yolo-02-parallel-execute.md`

---

## CSV SCHEMA CHANGES

### posts_content.csv - Add 6 Columns

| Column | Type | Purpose | Example |
|--------|------|---------|---------|
| `diversity_score` | INT (0-100) | How unique vs existing posts | 75 |
| `similar_posts_ids` | JSON array | Which posts are >70% similar | ["post_089", "post_112"] |
| `diversity_check_date` | ISO 8601 | When check was performed | "2026-01-30T10:15:00Z" |
| `consilium_triggered` | BOOLEAN | Was consilium run | true |
| `consilium_suggestions` | JSON array | Proposed strategies | ["security-focus", "roi-calc"] |
| `differentiation_strategy` | STRING | Selected strategy | "security-focus" |

### ideas_research.csv - Add 4 Columns

| Column | Type | Purpose |
|--------|------|---------|
| `diversity_score` | INT (0-100) | Uniqueness at idea level |
| `similar_ideas_ids` | JSON array | Ideas >70% similar to this |
| `similar_posts_ids` | JSON array | Posts >70% similar to this |
| `consilium_required` | BOOLEAN | Needs consilium analysis |

---

## PARALLEL EXECUTION PLAN

### Single Idea (CREATE Mode)

```
Phase 1: Load (1 agent)
  └─ Read posts_content.csv + embeddings (2 sec)

Phase 2: Parallel Scoring (6-8 agents)
  ├─ Agent_1: Compare vs posts_1-25 (parallel)
  ├─ Agent_2: Compare vs posts_26-50 (parallel)
  ├─ ...
  └─ Agent_6: Compare vs posts_126-145 (parallel)
  └─ All agents run simultaneously (38 ms, not 240 ms!)

Phase 3: Aggregation (1 agent)
  └─ Collect scores, calculate diversity_score (5 ms)

Phase 4: Decision & Consilium (if triggered)
  ├─ If diversity_score < 60:
  │  └─ Spawn 4 agents for consilium discussion (2 min)
  └─ Return suggestions to user

Total time: ~2 sec (+ 2 min if consilium triggered)
```

### Batch Ideas (YOLO Mode)

```
Phase 1: Parallel Load (3 agents)
  ├─ Load posts DB
  ├─ Load ideas
  └─ Pre-warm embeddings
  └─ All parallel (100 ms)

Phase 2: Batch Grouping (1 agent)
  └─ Group similar topics (20 ms)

Phase 3: Parallel Scoring (Waves with 6-agent pool)
  ├─ Wave 1: Ideas 1-3 (6 agents) - 38 ms
  ├─ Wave 2: Ideas 4-5 (6 agents reused) - 39 ms
  └─ Agents warm between waves (no spawn overhead!)

Phase 4: Cross-Idea Matrix (2 agents)
  └─ Find duplicates within batch (50 ms)

Phase 5: Annotate (1 agent)
  └─ Tag each idea with diversity flags (20 ms)

Total time: ~1-2 sec for 5 ideas (vs 150 sec sequential!)
```

---

## PERFORMANCE TARGETS & BENCHMARKS

| Operation | Sequential | Parallel | Target | Speedup |
|-----------|-----------|----------|--------|---------|
| Single idea check (145 posts) | 30 sec | 2-3 sec | <5 sec | **10-15x** |
| Batch check (5 ideas) | 150 sec | 1-2 sec | <2 sec | **25-75x** |
| Consilium analysis | - | 120 sec | <2 min | Baseline |
| Agent spawn (pool reuse) | - | <50 ms | - | **4x faster** |

**Key optimizations:**
- Agent pool reuse (6 agents warm between tasks)
- Embedding cache (70%+ hit rate)
- Batch context sharing (group similar topics)

---

## CONSILIUM TRIGGER LOGIC

### When Triggered

```
If diversity_score < 60 (too similar):
  ├─ Show similar posts to user
  ├─ Offer 3 options:
  │  ├─ [A] ANALYZE (run consilium)
  │  ├─ [B] OVERRIDE (accept risk)
  │  └─ [C] BACK (select new idea)
```

### Consilium Process

```
4 agents discuss how to differentiate:

1. Content Analyst:
   "Existing post covers X, missing Y, focuses on audience A"

2. Strategy Innovator:
   "We could do angle B (different audience), angle C (different aspect)"

3. Market Analyst:
   "Angle B has larger market, higher conversion potential"

4. Coordinator:
   "Recommendation: Go with angle B (security focus)"

Result: 3-5 ranked suggestions with reasoning
User picks preferred strategy
Proceeds with strategy noted
```

---

## AGENT SPECIFICATIONS

### CREATE Mode: Diversity Check

```
Pool size: 6-8 agents
Topology: Hierarchical (coordinator controls)
Duration: <2 sec (parallel scoring)
Communication: Result aggregation only
```

### CREATE Mode: Consilium Analysis

```
Pool size: 4 agents
Roles:
  - Agent_coordinator (RAFT leader)
  - Agent_content-analyst
  - Agent_strategy-innovator
  - Agent_market-analyst

Topology: Hierarchical (coordinator leader)
Duration: ~2 min (discussion + consensus)
Communication: Via shared memory (async)
Consensus: RAFT (coordinator maintains truth)
```

### YOLO Mode: Batch Analysis

```
Pool size: 6 agents (reused across waves)
Topology: Hierarchical
Waves: N/6 (ideas divided by 6)
Duration: <2 sec (all waves combined)
Communication: Memory aggregation
```

---

## MEMORY & CACHING STRATEGY

### Embedding Cache

```
Location: ~/.claude-flow/agentdb-global/cache/embeddings/
Format: JSON with TTL (1 hour default)
Size: Max 1GB (LRU eviction when exceeded)
Hit rate target: 70%+
```

### Shared Memory Namespace

```
shared-knowledge:diversity:*
├─ idea_82:vs_posts (comparison results from agents)
├─ idea_82:final_score (aggregated diversity score)
└─ idea_82:consilium_output (suggestions from consilium)
```

### Post-Task Hook Auto-Save

```
After step completes:
1. Extract diversity metadata
2. Save to memory (shared-knowledge:diversity:*)
3. Update posts_content.csv
4. Track metrics (metrics_tracking.csv)
```

---

## RISK MITIGATION

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| **False positives** (marks different as similar) | Medium | User frustration | Threshold tuning (60%), manual override |
| **Consilium timeout** | Low | User wait | 2-min max, cached suggestions backup |
| **Agent pool exhaustion** | Low | System hang | Max 8 agents, queue overflow handling |
| **Cache grows too large** | Low | Memory pressure | 1GB limit, LRU eviction |
| **Embedding not found** | Low | Fallback compute | Compute on miss, cache result |

---

## SUCCESS CRITERIA

### Functionality
- ✅ Diversity score accurately reflects content uniqueness
- ✅ Consilium triggers when score < 60%
- ✅ User can override for edge cases
- ✅ Batch analysis works for 5+ ideas
- ✅ Data persists in CSV schema

### Performance
- ✅ Single check: <5 sec (vs 30 sec baseline)
- ✅ Batch check: <2 sec (vs 150 sec baseline)
- ✅ Consilium: <2 min (acceptable wait)
- ✅ Cache hit rate: >70%
- ✅ Agent efficiency: 4x+ speedup

### User Experience
- ✅ Clear feedback on similarity detection
- ✅ Actionable consilium suggestions
- ✅ Transparent decision-making
- ✅ Easy override for edge cases
- ✅ No disruption to existing workflow

---

## IMPLEMENTATION EFFORT

### Timeline: 2-3 Developer-Days

**Day 1 (8 hours):**
- Phase 1: Foundation (4 hrs) - diversity-check step + CSV schema
- Phase 2: Consilium (4 hrs) - consilium step + integration

**Day 2 (8 hours):**
- Phase 3: YOLO Mode (3 hrs) - batch diversity check + integration
- Phase 4: Optimization (2 hrs) - caching, memory hooks
- Phase 5: Testing (3 hrs) - unit & integration tests

**Day 3 (4-8 hours):**
- Phase 5+6: Final testing (2 hrs) - performance benchmarks
- Phase 6: Documentation (2-4 hrs) - user & dev docs

---

## DELIVERABLES CHECKLIST

### Step Files
- [ ] `steps-c/c-03a-diversity-check.md` (NEW)
- [ ] `steps-c/c-03a-consilium-analyze.md` (NEW)
- [ ] `steps-yolo/yolo-02a-diversity-check.md` (NEW)

### Integration
- [ ] Update `c-03a-select-idea.md` (nextStepFile)
- [ ] Update `yolo-01-input.md` (nextStepFile)

### Data Schema
- [ ] Update `posts_content.csv` (add 6 columns)
- [ ] Update `ideas_research.csv` (add 4 columns)
- [ ] Migration script (set defaults)

### Documentation
- [ ] DIVERSITY-CHECK-ARCHITECTURE.md (full spec) ✅
- [ ] DIVERSITY-QUICK-REFERENCE.md (quick start) ✅
- [ ] DIVERSITY-ARCHITECTURE-DIAGRAMS.md (visuals) ✅
- [ ] IMPLEMENTATION-ROADMAP.md (dev roadmap) ✅
- [ ] User documentation & examples
- [ ] Troubleshooting guide

---

## NEXT STEPS

1. **Review** this design document
2. **Validate** approach with stakeholders
3. **Begin** Phase 1 implementation
4. **Test** each phase before proceeding
5. **Deploy** with limited beta first
6. **Monitor** metrics post-launch

---

## REFERENCE DOCUMENTS

All detailed documentation has been created:

| Document | Purpose | Location |
|----------|---------|----------|
| **Architecture Spec** | Complete technical design (80+ pages) | `DIVERSITY-CHECK-ARCHITECTURE.md` |
| **Quick Reference** | Implementation quick start (5 pages) | `DIVERSITY-QUICK-REFERENCE.md` |
| **Architecture Diagrams** | Visual flows & architecture (10+ diagrams) | `DIVERSITY-ARCHITECTURE-DIAGRAMS.md` |
| **Implementation Roadmap** | Phase-by-phase developer guide (6 pages) | `IMPLEMENTATION-ROADMAP.md` |
| **Design Summary** | This document (executive overview) | `DESIGN-SUMMARY.md` |

---

**Status:** ✅ Architecture Design COMPLETE
**Ready for:** Implementation
**Created:** 2026-01-30

Questions? Refer to:
- Architecture details → DIVERSITY-CHECK-ARCHITECTURE.md
- Quick reference → DIVERSITY-QUICK-REFERENCE.md
- Visual guides → DIVERSITY-ARCHITECTURE-DIAGRAMS.md
- Dev roadmap → IMPLEMENTATION-ROADMAP.md

