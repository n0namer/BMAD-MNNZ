# Diversity Checking - Implementation Roadmap

**Status:** Ready for Development
**Estimated Effort:** 2-3 developer-days
**Priority:** High (prevents content duplication)
**Complexity:** Medium (parallel execution + consilium)

---

## EXECUTIVE SUMMARY

This document provides a clear, actionable roadmap for implementing diversity checking in the idea-to-post-pipeline. The system prevents similar content generation through:

1. **Pre-generation quality gate** (5 sec check before writing)
2. **Parallel similarity analysis** (6-8 agents scoring simultaneously)
3. **Consilium-based differentiation** (4 agents discussing unique angles when similarity detected)
4. **Batch optimization** (5 ideas scored in <2 sec with agent pooling)

---

## PHASE 1: FOUNDATION (Day 1 - 4 hours)

### Step 1.1: Create `c-03a-diversity-check.md`

**Effort:** 2 hours
**Complexity:** Medium

**Deliverables:**
- [ ] Step file with YAML frontmatter
- [ ] Load existing posts database
- [ ] Spawn 6-8 parallel agents for similarity scoring
- [ ] Aggregate scores → calculate diversity_score
- [ ] Decision gate (threshold >= 60)
- [ ] User menu (consilium / override / back)

**Code skeleton:**
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

# Step execution:
# 1. Load data
# 2. Initialize parallel agents
# 3. Collect results
# 4. Calculate score
# 5. Decision gate
# 6. User menu
```

**Testing:**
- [ ] Test with 50 existing posts
- [ ] Test with 200+ existing posts
- [ ] Measure execution time (<5 sec target)
- [ ] Verify parallel agents all start simultaneously

### Step 1.2: Create CSV Schema Changes

**Effort:** 1 hour
**Complexity:** Low

**Deliverables:**
- [ ] Add 6 columns to `posts_content.csv`
  - diversity_score, similar_posts_ids, diversity_check_date
  - consilium_triggered, consilium_suggestions, differentiation_strategy
- [ ] Add 4 columns to `ideas_research.csv`
  - diversity_score, similar_ideas_ids, similar_posts_ids, consilium_required
- [ ] Backup existing CSVs
- [ ] Migration script (set defaults for existing rows)

**Data Validation:**
- [ ] CSV still loads properly with new columns
- [ ] NULL defaults work correctly
- [ ] No data loss during migration

### Step 1.3: Integration Points (CREATE Mode)

**Effort:** 1 hour
**Complexity:** Low

**Deliverables:**
- [ ] Update `c-03a-select-idea.md` nextStepFile
  - From: `./c-03b-select-angle.md`
  - To: `./c-03a-diversity-check.md`
- [ ] Update `c-03a-diversity-check.md` nextStepFile
  - To: `./c-03b-select-angle.md`
- [ ] Verify workflow chain works without errors
- [ ] Test data forwarding between steps

**End-to-End Test:**
- [ ] Select idea → diversity check → angle selection (no breaks)

---

## PHASE 2: CONSILIUM (Day 1-2 - 4 hours)

### Step 2.1: Create `c-03a-consilium-analyze.md`

**Effort:** 2.5 hours
**Complexity:** High (most complex part)

**Deliverables:**
- [ ] Step file with YAML frontmatter
- [ ] Initialize consilium (4 agents, hierarchical topology)
- [ ] Agent roles: coordinator, content-analyst, strategist, market-analyst
- [ ] Communication protocol (via shared memory)
- [ ] Suggestion ranking algorithm
- [ ] Return structured JSON with suggestions

**Agent Configuration:**
```yaml
Coordinator:
  role: "Lead consilium, consolidate findings"
  timeout: 120 seconds

ContentAnalyst:
  role: "Analyze similar post, identify gaps"
  timeout: 60 seconds

StrategyInnovator:
  role: "Propose novel differentiation angles"
  timeout: 60 seconds

MarketAnalyst:
  role: "Evaluate market opportunity for each angle"
  timeout: 60 seconds

Consensus:
  strategy: "raft"
  timeout: 120 seconds
  output: JSON array with 3-5 suggestions
```

**Testing:**
- [ ] Consilium completes in <2 min
- [ ] All 4 agents start in parallel
- [ ] Suggestions are ranked by opportunity score
- [ ] Can handle edge case: no viable suggestions
- [ ] Timeout handling works (stops at 2 min)

### Step 2.2: Consilium Integration

**Effort:** 1.5 hours
**Complexity:** Medium

**Deliverables:**
- [ ] Wire `c-03a-diversity-check.md` to call `c-03a-consilium-analyze.md`
- [ ] Pass: idea details, similar_posts details
- [ ] Receive: ranked suggestions (JSON)
- [ ] Display menu: user selects preferred strategy
- [ ] Forward selected strategy to `c-03b-select-angle.md`

**Testing:**
- [ ] Low diversity triggers consilium correctly
- [ ] Consilium results display properly
- [ ] User can select strategy
- [ ] Selected strategy forwarded to next step

---

## PHASE 3: YOLO MODE BATCH (Day 2 - 3 hours)

### Step 3.1: Create `yolo-02a-diversity-check.md`

**Effort:** 2 hours
**Complexity:** High (batch optimization required)

**Deliverables:**
- [ ] Step file with YAML frontmatter
- [ ] Load all input ideas + existing posts (3 agents in parallel)
- [ ] Batch grouping logic (group similar-topic ideas)
- [ ] Parallel scoring of all ideas (6 agents, multiple waves)
- [ ] Cross-idea similarity matrix (detect internal duplicates)
- [ ] Annotated output: each idea gets diversity flags
- [ ] Recommend filtering (remove duplicates)

**Key Optimization:**
```
Wave strategy (with 6 agents):
  Wave 1: Ideas 1-3 (6 agents scoring in parallel)
  Wave 2: Ideas 4-5 (6 agents reused - no spawn overhead)
  Wave N: Additional ideas (if any)

Result: 5 ideas scored in 2 sec (vs 150 sec sequential!)
```

**Testing:**
- [ ] Batch check for 5 ideas: <2 sec
- [ ] Batch check for 20 ideas: <5 sec
- [ ] Cross-idea similarity detected correctly
- [ ] Agent pool reuse works (no spawning per wave)
- [ ] Annotated output correct

### Step 3.2: YOLO Integration

**Effort:** 1 hour
**Complexity:** Low

**Deliverables:**
- [ ] Update `yolo-01-input.md` nextStepFile
  - From: `./yolo-02-parallel-execute.md`
  - To: `./yolo-02a-diversity-check.md`
- [ ] Update `yolo-02a-diversity-check.md` nextStepFile
  - To: `./yolo-02-parallel-execute.md`
- [ ] Verify data forwarding: annotated idea list → yolo-02
- [ ] Ensure yolo-02 can skip low-diversity ideas if needed

**Testing:**
- [ ] YOLO mode: input → diversity check → parallel execute (no breaks)
- [ ] Low diversity ideas can be filtered
- [ ] Metadata tagged posts visible in final output

---

## PHASE 4: OPTIMIZATION & CACHING (Day 2-3 - 2 hours)

### Step 4.1: Embedding Cache Implementation

**Effort:** 1 hour
**Complexity:** Medium

**Deliverables:**
- [ ] Implement cache layer for embeddings
  - Storage: `~/.claude-flow/agentdb-global/cache/embeddings/`
  - Format: JSON with TTL (1 hour default)
  - Size limit: 1GB auto-eviction
- [ ] Cache hit rate monitoring
- [ ] Fallback: compute on miss + cache result

**Performance Target:**
- [ ] Cache hit rate: 70%+ (on repeated analyses)
- [ ] Embedding lookup: <10ms (vs 30-50ms compute)

**Testing:**
- [ ] First analysis: computes embeddings
- [ ] Second analysis (same posts): uses cache (<5 sec total)
- [ ] Cache invalidation works (TTL expiry)

### Step 4.2: Memory Hook Integration

**Effort:** 1 hour
**Complexity:** Low

**Deliverables:**
- [ ] Setup shared memory namespace: `shared-knowledge:diversity:*`
- [ ] Post-task hook auto-saves diversity metadata
- [ ] Memory retrieval: consilium suggestions available for future ideas
- [ ] Metrics tracking: add diversity stats to `metrics_tracking.csv`

---

## PHASE 5: TESTING & VALIDATION (Day 3 - 2 hours)

### Step 5.1: Unit Tests

**Deliverables:**
- [ ] Test similarity scoring algorithm (samples)
- [ ] Test diversity threshold logic
- [ ] Test consilium suggestion ranking
- [ ] Test batch grouping optimization

### Step 5.2: Integration Tests

**Deliverables:**
- [ ] Full CREATE mode flow (idea → diversity → angle → draft)
- [ ] Full YOLO mode flow (input → diversity batch → parallel execute)
- [ ] Consilium trigger & suggestion flow
- [ ] CSV persistence (data saved correctly)

### Step 5.3: Performance Benchmarks

**Deliverables:**
- [ ] Single idea check: <5 sec (measure actual vs target)
- [ ] Batch check (5 ideas): <2 sec
- [ ] Consilium: <2 min
- [ ] Agent pool efficiency: 4x+ speedup
- [ ] Cache hit rate: 70%+

**Acceptance Criteria:**
- [ ] All benchmarks meet targets
- [ ] No memory leaks (agent cleanup)
- [ ] No timeout hangs (timeout logic works)

---

## PHASE 6: DOCUMENTATION (Day 3 - 1 hour)

### Step 6.1: User Documentation

**Deliverables:**
- [ ] Update workflow README with diversity checking feature
- [ ] Add step-by-step examples (with screenshots)
- [ ] Document consilium interaction model
- [ ] FAQ: common questions about similarity scores

### Step 6.2: Developer Documentation

**Deliverables:**
- [ ] Code comments in step files
- [ ] Agent configuration reference
- [ ] Memory schema documentation
- [ ] Troubleshooting guide

---

## IMPLEMENTATION CHECKLIST

### Phase 1: Foundation
```
CREATE Mode - Single Idea Analysis
─────────────────────────────────────────
 Day 1, 4 hours

 [ ] Create c-03a-diversity-check.md
     [ ] YAML frontmatter
     [ ] Load posts database
     [ ] Spawn parallel agents
     [ ] Aggregate scores
     [ ] Decision gate
     [ ] User menu

 [ ] CSV schema changes
     [ ] Add 6 columns to posts_content.csv
     [ ] Add 4 columns to ideas_research.csv
     [ ] Migration script
     [ ] Backup existing data

 [ ] Integration: CREATE mode
     [ ] Update c-03a-select-idea.md
     [ ] Update c-03a-diversity-check.md
     [ ] Test workflow chain
     [ ] Verify data forwarding
```

### Phase 2: Consilium
```
Consilium-Based Differentiation
─────────────────────────────────────────
 Day 1-2, 4 hours

 [ ] Create c-03a-consilium-analyze.md
     [ ] Agent spawning (4 agents)
     [ ] Communication protocol
     [ ] Suggestion ranking
     [ ] Timeout handling

 [ ] Consilium integration
     [ ] Call from diversity-check
     [ ] Display suggestions
     [ ] User selection
     [ ] Forward strategy
```

### Phase 3: YOLO Mode
```
Batch Diversity Analysis
─────────────────────────────────────────
 Day 2, 3 hours

 [ ] Create yolo-02a-diversity-check.md
     [ ] Parallel load (3 agents)
     [ ] Batch grouping
     [ ] Parallel scoring (waves)
     [ ] Cross-idea matrix
     [ ] Annotated output

 [ ] YOLO integration
     [ ] Update yolo-01-input.md
     [ ] Update yolo-02a-diversity-check.md
     [ ] Test workflow chain
     [ ] Verify filtering works
```

### Phase 4: Optimization
```
Caching & Performance
─────────────────────────────────────────
 Day 2-3, 2 hours

 [ ] Embedding cache
     [ ] Cache layer implementation
     [ ] TTL management
     [ ] Size limits
     [ ] Hit rate monitoring

 [ ] Memory hooks
     [ ] Namespace setup
     [ ] Post-task hook
     [ ] Metrics tracking
```

### Phase 5: Testing
```
Validation & Benchmarks
─────────────────────────────────────────
 Day 3, 2 hours

 [ ] Unit tests
     [ ] Algorithm accuracy
     [ ] Threshold logic
     [ ] Ranking logic

 [ ] Integration tests
     [ ] CREATE mode flow
     [ ] YOLO mode flow
     [ ] Consilium flow
     [ ] CSV persistence

 [ ] Performance tests
     [ ] Single check <5 sec
     [ ] Batch check <2 sec
     [ ] Consilium <2 min
     [ ] Agent efficiency
     [ ] Cache hit rate >70%
```

### Phase 6: Documentation
```
Docs & Knowledge
─────────────────────────────────────────
 Day 3, 1 hour

 [ ] User documentation
 [ ] Developer documentation
 [ ] Code comments
 [ ] Troubleshooting guide
```

---

## DEPENDENCIES & BLOCKERS

### Required
- ✅ Existing step file structure (c-03a, c-03b, etc.)
- ✅ CSV files (posts_content.csv, ideas_research.csv)
- ✅ Memory/hooks system (for consilium communication)
- ✅ Agent spawning capability (Task tool)

### Optional (Nice-to-have)
- Embedding API (Claude embeddings)
- RuVector for persistent cache (or SQLite fallback)
- Pre-trained similarity models

### Known Risks
| Risk | Mitigation |
|------|-----------|
| False positive similarity | Tune threshold, user override |
| Consilium timeout | 2-min timeout, cached suggestions |
| Agent pool exhaustion | Max 8 agents, queue for others |
| Cache growth | 1GB limit, LRU eviction |

---

## SUCCESS METRICS

### Functionality
- ✅ Diversity score accurately reflects uniqueness
- ✅ Consilium triggered when score < 60%
- ✅ Batch analysis works for 5+ ideas
- ✅ Data persists in CSV

### Performance
- ✅ Single check: <5 sec (vs 30 sec baseline)
- ✅ Batch check: <2 sec (vs 150 sec baseline)
- ✅ Consilium: <2 min (acceptable wait)
- ✅ Cache hit rate: >70%

### User Experience
- ✅ Clear feedback on similarity
- ✅ Actionable suggestions
- ✅ Easy override for edge cases
- ✅ Transparent decision-making

---

## ROLLOUT STRATEGY

### Phase A: Internal Testing (1 day)
- Developers test implementation
- Run performance benchmarks
- Validate edge cases
- Fix bugs before release

### Phase B: Limited Beta (1 day)
- Release to power users
- Collect feedback on threshold
- Monitor for issues
- Adjust before broader rollout

### Phase C: Full Release (1 day)
- Enable for all users
- Monitor metrics (diversity scores, consilium triggers)
- Gather usage patterns
- Iterate based on feedback

---

## MAINTENANCE & ITERATION

### Monthly Review
- [ ] Analyze diversity_score distribution
- [ ] Check consilium effectiveness
- [ ] Review false positive rate
- [ ] Adjust threshold if needed

### Quarterly Optimization
- [ ] Refine similarity algorithm
- [ ] Improve consilium suggestions
- [ ] Optimize agent pool strategy
- [ ] Expand cache capacity if needed

---

## APPENDIX: FILE LOCATIONS

```
_bmad/bmm/workflows/idea-to-post-pipeline/

FILES TO CREATE:
├─ steps-c/
│  ├─ c-03a-diversity-check.md (NEW)
│  ├─ c-03a-consilium-analyze.md (NEW)
│  └─ ...
├─ steps-yolo/
│  ├─ yolo-02a-diversity-check.md (NEW)
│  └─ ...
└─ DIVERSITY-CHECK-ARCHITECTURE.md (reference)
   DIVERSITY-QUICK-REFERENCE.md (quick start)
   DIVERSITY-ARCHITECTURE-DIAGRAMS.md (visuals)
   IMPLEMENTATION-ROADMAP.md (you are here)

FILES TO MODIFY:
├─ steps-c/
│  ├─ c-03a-select-idea.md (update nextStepFile)
│  └─ ...
├─ steps-yolo/
│  ├─ yolo-01-input.md (update nextStepFile)
│  └─ ...
└─ content_generation_system/
   ├─ posts_content.csv (add 6 columns)
   ├─ ideas_research.csv (add 4 columns)
   └─ metrics_tracking.csv (add tracking)
```

---

## QUESTIONS & SUPPORT

**For questions during implementation:**

1. **Architecture questions:** Refer to `DIVERSITY-CHECK-ARCHITECTURE.md`
2. **Quick reference:** Check `DIVERSITY-QUICK-REFERENCE.md`
3. **Visual help:** See `DIVERSITY-ARCHITECTURE-DIAGRAMS.md`
4. **Integration issues:** Review integration points in this document

---

**Document Status:** Ready for Implementation
**Created:** 2026-01-30
**Next Step:** Begin Phase 1 development

