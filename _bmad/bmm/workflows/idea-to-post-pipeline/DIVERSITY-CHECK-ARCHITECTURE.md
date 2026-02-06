# Diversity Checking Architecture
## Parallel Implementation for idea-to-post-pipeline

**Status:** Architecture Design Document (ADR-001)
**Date:** 2026-01-30
**Version:** 1.0

---

## 1. EXECUTIVE SUMMARY

This document designs a **parallel diversity checking system** that prevents similar content generation in the idea-to-post-pipeline. The system:

- **Integrates at 2 points:** Before angle selection (CREATE mode) and before batch execution (YOLO mode)
- **Uses hierarchical parallel execution:** Multiple agents compare current idea/post against existing content simultaneously
- **Triggers consilium intelligently:** When similarity score < 60%, spawns expert agents for differentiation analysis
- **Maintains BMAD compliance:** All new components are step files with YAML frontmatter
- **Optimizes performance:** Agent pooling + embedding cache + batch processing = 50% faster than sequential

---

## 2. INTEGRATION ARCHITECTURE

### 2.1 CREATE Mode (steps-c/)

**Current Flow:**
```
c-03a-select-idea.md
    ↓
c-03b-select-angle.md
    ↓
c-03c-draft.md
```

**New Flow:**
```
c-03a-select-idea.md
    ↓
[NEW] c-03a-diversity-check.md ← INSERTION POINT 1
    ├─ Parallel similarity analysis
    ├─ Score calculation (0-100)
    └─ Consilium trigger logic
    ↓
c-03b-select-angle.md (unchanged, but receives diversity report)
    ↓
c-03c-draft.md (unchanged)
```

**Key:** New step is inserted BETWEEN idea selection and angle selection as a quality gate.

### 2.2 YOLO Mode (steps-yolo/)

**Current Flow:**
```
yolo-01-input.md
    ↓
yolo-02-parallel-execute.md (parallel: add ideas, research, write)
    ↓
yolo-03-self-check.md
```

**New Flow:**
```
yolo-01-input.md
    ↓
[NEW] yolo-02a-diversity-check.md ← INSERTION POINT 2
    ├─ Parallel diversity scoring for all input ideas
    ├─ Cross-idea similarity matrix
    └─ Filter/tag ideas with diversity flags
    ↓
yolo-02-parallel-execute.md (enhanced with diversity-tagged ideas)
    ↓
yolo-03-self-check.md
```

**Key:** New step runs in parallel for batch efficiency, output feeds into existing parallel execute step.

---

## 3. NEW STEP FILES

### 3.1 CREATE Mode: `c-03a-diversity-check.md`

**File Location:** `_bmad/bmm/workflows/idea-to-post-pipeline/steps-c/c-03a-diversity-check.md`

**YAML Frontmatter:**
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

**Purpose:** Prevent duplicate/similar posts by analyzing diversity BEFORE writing

**Execution Flow:**

```
STEP GOAL:
Analyze diversity of selected idea against existing posts
Output: diversity_score (0-100) + consilium suggestion (if triggered)

EXECUTION SEQUENCE:

1. LOAD DATA
   ├─ Current idea details (title, category)
   ├─ All existing posts (from posts_content.csv)
   └─ Embedding cache (for fast similarity search)

2. INITIALIZE PARALLEL SIMILARITY ANALYSIS
   │
   ├─ Main Coordinator Agent spawns:
   │  ├─ Agent 1: Load posts DB (1 agent, sequential)
   │  ├─ Agent 2-N: Parallel similarity scoring
   │  │  ├─ Agent 2: Score vs post_001
   │  │  ├─ Agent 3: Score vs post_002
   │  │  ├─ Agent N: Score vs post_N
   │  │  └─ (Up to 8 agents in parallel, reuse if posts > 8)
   │  └─ Similarity Aggregator: Collect results
   │
   └─ Progress: [████░░░░] 50% completed

3. CALCULATE DIVERSITY SCORE
   │
   ├─ Input: Array of similarity_scores [0.45, 0.82, 0.61, ...]
   ├─ Formula: diversity_score = 100 - MAX(similarity_scores)
   │  └─ Example: max_similarity = 82% → diversity_score = 18
   │
   └─ Result: diversity_score = 42 (BELOW THRESHOLD)

4. DECISION GATE: diversity_score >= 60?
   │
   ├─ IF YES (diverse enough)
   │  ├─ Status: ✅ PASS
   │  ├─ Store: diversity_score in memory
   │  └─ Action: Proceed to angle selection
   │
   ├─ IF NO (too similar)
   │  ├─ Status: ⚠️ LOW DIVERSITY DETECTED
   │  ├─ Similar posts found: [post_089, post_112]
   │  └─ Action: Branch to consilium trigger
   │
   └─ If NO: Present options to user

5. CONSILIUM TRIGGER (if diversity_score < 60)
   │
   ├─ Display: "Similar post detected (82% similarity with post_112)"
   │
   ├─ Menu Options:
   │  ├─ [A] ANALYZE WITH CONSILIUM (spawns agents)
   │  ├─ [O] OVERRIDE (accept risk, proceed)
   │  └─ [B] BACK (cancel, select different idea)
   │
   └─ Wait for user selection

6a. IF [A] ANALYZE WITH CONSILIUM:
   │
   ├─ Call: c-03a-consilium-analyze.md
   │  └─ Returns: 3-5 differentiation suggestions
   │
   ├─ Display suggestions to user
   ├─ User selects preferred strategy
   └─ Proceed to angle selection with strategy noted

6b. IF [O] OVERRIDE:
   │
   ├─ Log: "User accepted similarity risk"
   ├─ Store: diversity_score + "override" flag
   └─ Proceed to angle selection

6c. IF [B] BACK:
   │
   ├─ Return to c-03a-select-idea.md
   └─ User can select different idea

7. PASS DATA TO NEXT STEP
   │
   └─ Forward to c-03b-select-angle.md:
      ├─ diversity_score
      ├─ similar_posts_ids
      ├─ consilium_suggestions (if triggered)
      └─ differentiation_strategy (if selected)
```

**Parallel Optimization Details:**

```
Agent Pool Strategy:
┌─────────────────────────────────────────────┐
│ Agent Reuse Pattern                         │
├─────────────────────────────────────────────┤
│ Pool Size: min(8, num_existing_posts)       │
│ Pre-warm: Yes (agents stay warm between     │
│           similarity checks)                │
│ Communication: Via shared memory hooks      │
│ Caching: Embedding cache + similarity      │
│          score cache (TTL: 1 hour)          │
└─────────────────────────────────────────────┘

Performance Target:
┌─────────────────────────────────────────────┐
│ Posts Count  │ Sequential  │ Parallel (6A)  │
├──────────────┼─────────────┼────────────────┤
│ 10 posts     │ 8 sec       │ 2 sec (4x)     │
│ 50 posts     │ 25 sec      │ 6 sec (4x)     │
│ 200 posts    │ 80 sec      │ 16 sec (5x)    │
└─────────────────────────────────────────────┘

Speedup via:
  • Parallel agents: N agents → O(posts/N) time
  • Embedding cache: Skip recomputation
  • Similarity cache: Reuse scores from memory
  • Batch context: Share baseline with all agents
```

**User Interface:**

```
═══════════════════════════════════════════════════════════════
  🔍 DIVERSITY CHECK: Analyzing...
═══════════════════════════════════════════════════════════════

Idea: "5 инструментов для автоматизации"
Category: automation

Checking against 145 existing posts in parallel...

[████████████░░░░░░░░░░░░░░░░░░░░░░░░] 42% complete
Agents: 6/6 active | Time elapsed: 2s | ETA: 3s

═══════════════════════════════════════════════════════════════

RESULTS:

Diversity Score: 42/100 ⚠️ LOW

Most Similar Posts:
  1. post_089 "4 инструмента для экономии времени" (82% similar)
  2. post_112 "Автоматизация процессов: инструменты" (79% similar)
  3. post_045 "Как сэкономить время с помощью ИИ" (71% similar)

═══════════════════════════════════════════════════════════════

ACTION REQUIRED:

Your idea is very similar to existing posts. What would you like to do?

[A] ANALYZE WITH CONSILIUM
    → Let agents discuss differentiation strategies
    → Takes ~2 min, suggests how to make it unique

[O] OVERRIDE
    → Accept the risk and proceed anyway
    → Post may not perform well if very similar

[B] BACK
    → Return to idea selection
    → Choose a different idea to write about

═══════════════════════════════════════════════════════════════

Your choice: [A|O|B]
```

---

### 3.2 CREATE Mode: `c-03a-consilium-analyze.md`

**File Location:** `_bmad/bmm/workflows/idea-to-post-pipeline/steps-c/c-03a-consilium-analyze.md`

**YAML Frontmatter:**
```yaml
---
description: Consilium analysis for finding differentiation strategies
name: step-c-03a-consilium-analyze
nextStepFile: (return to c-03a-diversity-check.md with results)
type: consilium-discussion
subprocess: true
maxAgents: 4
topology: hierarchical
consensus: raft
---
```

**Purpose:** When similarity detected, spawn expert agents to collaboratively identify differentiation angles

**Execution Flow:**

```
STEP GOAL:
Given similar posts, propose 3-5 unique differentiation strategies
Output: Ranked suggestions with reasoning

EXECUTION SEQUENCE:

1. INITIALIZE CONSILIUM (Hierarchical Topology)
   │
   ├─ Coordinator Role: Agent_coordinator
   │  └─ Manages discussion, consolidates findings
   │
   ├─ Content Analyst Role: Agent_content-analyst
   │  └─ Analyzes the similar post(s) in detail
   │  └─ Identifies existing positioning, angles, audience
   │
   ├─ Strategy Innovator Role: Agent_strategy-innovator
   │  └─ Proposes novel angles not covered in similar posts
   │  └─ Thinks about different target audiences
   │
   └─ Market Analyst Role: Agent_market-analyst
      └─ Identifies market gaps and positioning opportunities
      └─ Evaluates competitiveness of suggestions

2. AGENT COMMUNICATION (via shared memory)
   │
   ├─ Agent_content-analyst posts findings:
   │  "Similar post focuses on tool comparison for mid-market.
   │   Angles covered: cost savings, integration, ease of use.
   │   Missing: security aspects, compliance requirements."
   │
   ├─ Agent_strategy-innovator responds:
   │  "Opportunity 1: Security-focused angle (B2Enterprise)
   │   Opportunity 2: Legal/compliance angle (Regulated industries)
   │   Opportunity 3: Implementation guide for non-technical (SMB)
   │   Opportunity 4: ROI calculation framework (Finance teams)"
   │
   ├─ Agent_market-analyst evaluates:
   │  "Highest opportunity: Security angle - high CTR, no competition
   │   Good: Compliance angle - niche, ready-to-buy audience
   │   OK: Implementation guide - high supply, medium demand"
   │
   └─ Agent_coordinator synthesizes:
      "Top 3 suggestions (ranked by opportunity):
       1. Security compliance angle
       2. ROI calculator framework
       3. Implementation guide for non-technical"

3. RANK SUGGESTIONS
   │
   ├─ Criteria:
   │  ├─ Uniqueness: How different from existing posts (0-100)
   │  ├─ Audience size: Potential reader count
   │  ├─ Conversion potential: Likelihood of leading to action
   │  └─ Effort required: How much reworking needed
   │
   └─ Output: 3-5 ranked suggestions with scores

4. RETURN SUGGESTIONS
   │
   └─ Forward to c-03a-diversity-check.md for user selection
```

**Consilium Discussion Example:**

```
═══════════════════════════════════════════════════════════════
  🎯 CONSILIUM: Differentiation Analysis in Progress
═══════════════════════════════════════════════════════════════

Topic: "5 инструментов для автоматизации"
Similar to: post_089 (82% match)

Agents: content-analyst, strategy-innovator, market-analyst

[Starting consilium discussion...]

Agent_content-analyst:
  "The existing post covers 5 automation tools for general use:
   Zapier, Make, Airtable, Pipedrive, Slack.

   Positioning: SMB/startups, cost-saving focus
   Angles covered:
   ✓ Cost savings (primary)
   ✓ Integration capabilities
   ✓ Ease of use
   ✗ Security considerations
   ✗ Specific use case focus
   ✗ Implementation complexity"

Agent_strategy-innovator:
  "I see multiple differentiation angles:

   ANGLE 1: Security & Compliance
   "5 Automation Tools That Don't Compromise Security"
   → Target: Regulated industries (finance, healthcare, legal)
   → Hook: Compliance requirements for automation
   → Positioning: Different from cost-focused post

   ANGLE 2: ROI Calculator
   "ROI Framework: Calculate Return on Automation Investment"
   → Target: Finance/operations teams
   → Hook: Concrete numbers instead of tool list
   → Positioning: Quantitative vs qualitative

   ANGLE 3: Specific Industry Focus
   "5 Automation Tools for [Legal Firms|Healthcare|Real Estate]"
   → Target: Specific vertical
   → Hook: Industry-specific problems
   → Positioning: Niche vs generalist"

Agent_market-analyst:
  "Market opportunity analysis:

   SECURITY ANGLE: 🟢 HIGH OPPORTUNITY
   ├─ Existing content: Low (few competitors)
   ├─ Search demand: Medium-High (security + automation)
   ├─ Audience size: 50K+ (regulated sectors)
   └─ Conversion potential: High (high-value customers)

   ROI ANGLE: 🟡 MEDIUM OPPORTUNITY
   ├─ Existing content: Medium (some calculators exist)
   ├─ Search demand: Medium
   ├─ Audience size: 100K+ (decision makers)
   └─ Conversion potential: High

   INDUSTRY ANGLE: 🟡 MEDIUM OPPORTUNITY
   ├─ Existing content: Medium (for each vertical)
   ├─ Search demand: Low-Medium (niche)
   ├─ Audience size: 10K-30K per vertical
   └─ Conversion potential: Very High (specific need)"

Agent_coordinator:
  "CONSILIUM CONSENSUS:

   Top 3 Differentiation Strategies:

   1️⃣ SECURITY & COMPLIANCE FOCUS (Score: 92/100)
   Strategy: Reframe entire post around security angle
   Why: Large audience, low competition, high value
   Effort: Moderate (need security research)

   2️⃣ ROI CALCULATION FRAMEWORK (Score: 78/100)
   Strategy: Add calculator + spreadsheet template
   Why: Unique format, decision-maker focused
   Effort: High (requires calculation methodology)

   3️⃣ LEGAL FIRMS USE CASE (Score: 71/100)
   Strategy: Reposition for specific vertical
   Why: Niche opportunity, high conversion
   Effort: Low-Moderate (adjust examples)"

═══════════════════════════════════════════════════════════════

RECOMMENDATION: Use Strategy #1 (Security angle)

Would you like to proceed with this differentiation strategy?

[Y] YES - Proceed to angle selection with security focus
[N] NO - Try different strategy
[B] BACK - Cancel consilium, use original idea

═══════════════════════════════════════════════════════════════
```

---

### 3.3 YOLO Mode: `yolo-02a-diversity-check.md`

**File Location:** `_bmad/bmm/workflows/idea-to-post-pipeline/steps-yolo/yolo-02a-diversity-check.md`

**YAML Frontmatter:**
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

**Purpose:** Score ALL ideas simultaneously for diversity before batch execution

**Key Difference from CREATE mode:**
- Analyzes MULTIPLE ideas in parallel
- Generates cross-idea similarity matrix (ideas checking against each other + existing posts)
- Flags potentially duplicate ideas
- Optimizes with maximum agent pooling

**Execution Flow:**

```
STEP GOAL:
For N input ideas, compute diversity scores in parallel
Output: Annotated idea list with diversity flags

EXECUTION SEQUENCE:

1. LOAD DATA (Parallel)
   │
   ├─ Agent_db-loader: Load posts_content.csv (all existing posts)
   ├─ Agent_ideas-loader: Load input ideas from yolo-01
   ├─ Agent_cache-loader: Pre-warm embedding cache
   └─ Progress: [█████████░] 90% complete

2. BATCH GROUPING (Optimize parallel work)
   │
   ├─ Group similar-topic ideas:
   │  ├─ Group A: [Idea_1, Idea_3] (both "automation")
   │  ├─ Group B: [Idea_2] (unique "marketing")
   │  └─ Group C: [Idea_4, Idea_5] (both "tools")
   │
   ├─ Benefit: Share baseline comparison context within groups
   └─ Reduction: 50% fewer comparisons needed

3. PARALLEL DIVERSITY SCORING
   │
   ├─ Agent Pool: 6 agents (reused, not spawned per idea)
   │
   ├─ Idea_1 Assignment:
   │  ├─ Agent_1: Score vs [existing posts 1-30]
   │  ├─ Agent_2: Score vs [existing posts 31-60]
   │  └─ Agent_3: Score vs [existing posts 61-145]
   │  └─ Result: diversity_score_1 = 67
   │
   ├─ Idea_2 Assignment:
   │  ├─ Agent_4: Score vs [existing posts 1-30]
   │  ├─ Agent_5: Score vs [existing posts 31-60]
   │  └─ Agent_6: Score vs [existing posts 61-145]
   │  └─ Result: diversity_score_2 = 82
   │
   ├─ Idea_3 Assignment (Agent reuse):
   │  ├─ Agent_1 (reused): Score vs [existing posts 1-30]
   │  └─ [Similar pattern for remaining]
   │  └─ Result: diversity_score_3 = 45 ⚠️
   │
   └─ Progress: [████████████░] 85% complete (3/5 ideas scored)

4. CROSS-IDEA SIMILARITY MATRIX
   │
   ├─ Compare ideas against EACH OTHER (find internal duplicates)
   │
   ├─ Matrix Result:
   │  │         Idea_1  Idea_2  Idea_3  Idea_4  Idea_5
   │  ├─ Idea_1  100%    15%     72%     20%     10%
   │  ├─ Idea_2   15%    100%    18%     25%     12%
   │  ├─ Idea_3   72%    18%     100%    22%     15%
   │  ├─ Idea_4   20%    25%     22%     100%    68%
   │  └─ Idea_5   10%    12%     15%     68%     100%
   │
   ├─ Issues Detected:
   │  ├─ Idea_1 & Idea_3: 72% similar → FLAG: Consider removing Idea_3
   │  └─ Idea_4 & Idea_5: 68% similar → FLAG: Combine into one
   │
   └─ Recommendation: Process 4 ideas instead of 5 (remove Idea_3)

5. AGGREGATE RESULTS & ANNOTATE
   │
   ├─ Output: Enhanced idea list
   │  └─ For each idea:
   │     ├─ diversity_score (0-100)
   │     ├─ similar_existing_ids ([post_089, post_112])
   │     ├─ similar_ideas_ids ([Idea_3])
   │     ├─ diversity_flag: "✓ PASS" | "⚠️ WARNING" | "🚫 DUPLICATE"
   │     └─ consilium_recommended: true|false
   │
   └─ Example row:
      Idea_5: {
        title: "Marketing for SaaS",
        diversity_score: 82,
        similar_existing_ids: [],
        similar_ideas_ids: [],
        diversity_flag: "✓ PASS",
        consilium_recommended: false
      }

6. BATCH CONSILIUM (Optional)
   │
   ├─ IF multiple low-diversity ideas detected:
   │  └─ Spawn consilium to discuss batch strategy
   │  └─ Example: "Combine Idea_4 & Idea_5 into one comprehensive post"
   │
   └─ Display recommendations to user

7. PASS DATA TO NEXT STEP
   │
   └─ Forward to yolo-02-parallel-execute.md:
      ├─ Enhanced idea list with diversity annotations
      ├─ Batch consilium suggestions (if generated)
      └─ Recommended action (which ideas to process)
```

**Performance & Optimization:**

```
AGENT POOL OPTIMIZATION (6 agents)
┌──────────────────────────────────────────────┐
│ Traditional Sequential Approach              │
├──────────────────────────────────────────────┤
│ For each idea:                               │
│   For each existing post:                    │
│     Calculate similarity (30-50ms)           │
│                                              │
│ Total: 5 ideas × 145 posts × 40ms = 29 sec  │
└──────────────────────────────────────────────┘

WITH PARALLEL POOL (6 agents)
┌──────────────────────────────────────────────┐
│ 5 ideas scored in 3 parallel waves:          │
│ Wave 1: Idea_1-3 vs posts (6 agents)         │
│   └─ Time: 145÷6 agents × 40ms = 970ms      │
│ Wave 2: Idea_4-5 vs posts (6 agents reuse)   │
│   └─ Time: 145÷6 × 40ms = 970ms             │
│                                              │
│ Total: ~2 sec (14x faster!)                  │
│                                              │
│ + Embedding cache: saves 50% (1 sec) ✓      │
│ + Batch context: saves 20% (200ms) ✓        │
│                                              │
│ Final: ~1 sec for entire batch               │
└──────────────────────────────────────────────┘

MEMORY SAVINGS (Cache Strategy)
┌──────────────────────────────────────────────┐
│ Without cache: 5 × 145 = 725 comparisons     │
│ With cache:                                   │
│  - Similar existing posts reused (80/145)    │
│  - Cross-idea results cached                 │
│  - Effective: 160 unique comparisons         │
│  - Reduction: 78% fewer calculations!        │
└──────────────────────────────────────────────┘
```

---

## 4. CSV SCHEMA CHANGES

### 4.1 posts_content.csv

**Add columns:**

```csv
# Existing columns (unchanged)
id,title,idea_id,angle_id,version,content_500,content_250,content_100,status,date,quality_score,...

# NEW COLUMNS (added after status)
,diversity_score,similar_posts_ids,diversity_check_date,consilium_triggered,consilium_suggestions,differentiation_strategy

# Example rows:
post_001,"AI Content in 3h","idea_045","angle_12","v1","...","...","...","published","2026-01-25",87,"75","[post_089, post_112]","2026-01-30T10:15:00Z",false,"[]","none"

post_002,"5 Automation Tools","idea_082","angle_34","v2","...","...","...","draft","2026-01-27",92,"45","[post_088, post_112, post_201]","2026-01-30T10:20:00Z",true,"['security-focus','roi-calculator','implementation-guide']","security-focus"
```

**New Column Specs:**

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `diversity_score` | INT (0-100) | Uniqueness vs existing posts | 75 |
| `similar_posts_ids` | JSON array | IDs of >70% similar posts | ["post_089", "post_112"] |
| `diversity_check_date` | ISO 8601 | When check was performed | "2026-01-30T10:15:00Z" |
| `consilium_triggered` | BOOLEAN | Was consilium run | true |
| `consilium_suggestions` | JSON array | Proposed strategies | ["security-focus", "roi-calc"] |
| `differentiation_strategy` | STRING | Chosen strategy | "security-focus" |

### 4.2 ideas_research.csv

**Add columns:**

```csv
# Existing columns (unchanged)
id,title,category,status,research_date,...

# NEW COLUMNS (added)
,diversity_score,similar_ideas_ids,similar_posts_ids,consilium_required

# Example rows:
idea_045,"ИИ контент за 3ч","automation","researched","2026-01-25","82","[]","[post_089, post_112]",false

idea_082,"5 инструментов","automation","researched","2026-01-27","45","[idea_025]","[post_088, post_112]",true
```

**New Column Specs:**

| Column | Type | Description |
|--------|------|-------------|
| `diversity_score` | INT (0-100) | Uniqueness at idea level |
| `similar_ideas_ids` | JSON array | Ideas with >70% similarity |
| `similar_posts_ids` | JSON array | Existing posts with >70% similarity |
| `consilium_required` | BOOLEAN | Flag for consilium analysis |

### 4.3 metrics_tracking.csv

**Add tracking for diversity effectiveness:**

```csv
# Existing columns (unchanged)
date,metric,value,...

# Add tracking rows:
2026-01-30,diversity_score_avg,68.5
2026-01-30,posts_with_low_diversity,3
2026-01-30,consilium_analyses_run,2
2026-01-30,differentiation_strategies_used,["security-focus", "roi-calc", "niche-vertical"]
```

---

## 5. PARALLEL EXECUTION PLAN

### 5.1 Agent Spawning Strategy

**Create Mode (Single Idea Analysis):**

```
Main Execution Thread
│
├─ Phase 1: Load (1 agent)
│  └─ Sequential: Load posts DB, embeddings
│
├─ Phase 2: Parallel Similarity Scoring
│  │
│  └─ Agent Pool: 6-8 agents (hierarchical)
│     ├─ Agent_1: Compare vs posts_1-25
│     ├─ Agent_2: Compare vs posts_26-50
│     ├─ Agent_3: Compare vs posts_51-75
│     ├─ Agent_4: Compare vs posts_76-100
│     ├─ Agent_5: Compare vs posts_101-125
│     ├─ Agent_6: Compare vs posts_126-145
│     ├─ [Agent_7: Compare vs cache (if >200 posts)]
│     └─ [Agent_8: Compare vs cache (if >200 posts)]
│
├─ Phase 3: Aggregation (1 agent)
│  └─ Collect similarity scores, calculate diversity_score
│
├─ Phase 4: Decision (Main thread)
│  └─ Check threshold, decide consilium or proceed
│
└─ Phase 5: Consilium (if triggered)
   │
   └─ Agent Pool: 4 agents (hierarchical)
      ├─ Agent_coordinator: Lead discussion
      ├─ Agent_content-analyst: Analyze similar post
      ├─ Agent_strategy-innovator: Propose angles
      └─ Agent_market-analyst: Evaluate opportunity
```

**YOLO Mode (Batch Ideas Analysis):**

```
Main Execution Thread
│
├─ Phase 1: Load (3 agents in parallel)
│  ├─ Agent_posts-loader: Load posts DB
│  ├─ Agent_ideas-loader: Load input ideas
│  └─ Agent_cache-prewarmer: Pre-warm embeddings
│
├─ Phase 2: Batch Grouping (1 agent)
│  └─ Group similar topics for context reuse
│
├─ Phase 3: Parallel Batch Scoring
│  │
│  └─ Agent Pool: 6 agents (hierarchical)
│     │
│     ├─ Wave 1: Ideas 1-3
│     │  ├─ Agent_1: Idea_1 vs posts
│     │  ├─ Agent_2: Idea_2 vs posts
│     │  ├─ Agent_3: Idea_3 vs posts
│     │  └─ [+ 3 more agents for parallel sub-scoring]
│     │
│     ├─ Wave 2: Ideas 4-5 (agents reused)
│     │  ├─ Agent_1 (reused): Idea_4 vs posts
│     │  ├─ Agent_2 (reused): Idea_5 vs posts
│     │  └─ [agents recycle between waves]
│     │
│     └─ Total time: O(N ideas / 6 agents)
│
├─ Phase 4: Cross-Idea Matrix (2 agents)
│  ├─ Agent_matrix-builder: Generate similarity matrix
│  └─ Agent_anomaly-detector: Flag duplicates
│
├─ Phase 5: Aggregation & Annotation (1 agent)
│  └─ Build enhanced idea list with flags
│
└─ Phase 6: Batch Consilium (if needed)
   │
   └─ Agent Pool: 4 agents (if >2 low-diversity ideas)
      └─ Discuss batch strategy (combine? pivot? remove?)
```

### 5.2 Agent Communication Pattern

**Memory-Based Communication (Hooks):**

```
Agents communicate via shared memory namespace:
  shared-knowledge:diversity:*

Message Flow:
1. Agent_1 writes similarity score
   └─ memory.store("diversity:idea_82:vs_posts", {...})

2. Agent_2 reads and aggregates
   └─ memory.search("diversity:idea_82:vs_*")

3. Aggregator synthesizes results
   └─ memory.store("diversity:idea_82:final_score", 45)

4. Consilium reads from memory
   └─ memory.retrieve("diversity:idea_82:*")

5. Post-task hook auto-saves findings
   └─ Consolidates results into posts_content.csv
```

**RAFT Consensus (if consilium):**

```
Agent_coordinator maintains authoritative state:
├─ Receives proposals from all agents
├─ Validates against criteria
├─ Commits to final suggestions
└─ Logs decision rationale
```

---

## 6. DATA FLOW DIAGRAM

### 6.1 CREATE Mode Flow

```
User Input
    ↓
c-03a-select-idea.md
    ↓ (user selects idea_82)
c-03a-diversity-check.md
    ├─ Load posts_content.csv (145 posts)
    ├─ Load idea_82 data
    ├─ Spawn 6 agents → Score against all posts (parallel)
    ├─ Aggregate scores → diversity_score = 45
    ├─ Check: 45 < 60? YES
    │
    ├─ OPTION A: Counsel user → Branch to consilium
    │  ├─ c-03a-consilium-analyze.md (4 agents discuss)
    │  └─ Return: 3 differentiation suggestions
    │
    ├─ OPTION B: User overrides → Store flag
    │
    └─ → c-03b-select-angle.md
         └─ Forward: diversity_score, consilium_suggestions

c-03b-select-angle.md
    ├─ Display angles with diversity notes
    └─ User selects angle

c-03c-draft.md
    └─ Write post (informed by diversity analysis)
```

### 6.2 YOLO Mode Flow

```
User Input (5 ideas)
    ↓
yolo-01-input.md
    ├─ Store: ideas list
    └─ Pass to diversity check

yolo-02a-diversity-check.md
    ├─ Load 145 existing posts (1 agent)
    ├─ Load 5 input ideas (1 agent)
    ├─ Pre-warm embeddings (1 agent)
    │
    ├─ Parallel Phase: 6 agents score all ideas (1 sec)
    ├─ Cross-idea matrix: Detect duplicates
    ├─ Batch consilium (if needed): 2 ideas too similar
    │
    └─ Output: Annotated idea list
       ├─ Idea_1: diversity_score=82 ✓
       ├─ Idea_2: diversity_score=78 ✓
       ├─ Idea_3: diversity_score=45 ⚠️ (similar to Idea_1)
       ├─ Idea_4: diversity_score=71 ✓
       └─ Idea_5: diversity_score=88 ✓

yolo-02-parallel-execute.md
    ├─ Use annotated idea list
    ├─ Process ideas with ✓ flag (4 ideas)
    ├─ Tag posts with diversity metadata
    └─ Execute existing parallel workflow

yolo-03-self-check.md → yolo-04+ (unchanged)
```

---

## 7. IMPLEMENTATION CHECKLIST

### Phase 1: Step Files

- [ ] Create `c-03a-diversity-check.md`
  - [ ] YAML frontmatter with subprocess configuration
  - [ ] User interface (showing similarity results)
  - [ ] Threshold logic (>=60 to pass)
  - [ ] Decision menu (consilium / override / back)
  - [ ] Error handling

- [ ] Create `c-03a-consilium-analyze.md`
  - [ ] YAML frontmatter
  - [ ] Agent spawning logic (4 agents, hierarchical)
  - [ ] Consilium discussion protocol
  - [ ] Suggestion ranking algorithm
  - [ ] Return data format

- [ ] Create `yolo-02a-diversity-check.md`
  - [ ] YAML frontmatter with batch optimization
  - [ ] Batch grouping logic
  - [ ] Parallel scoring for multiple ideas
  - [ ] Cross-idea similarity matrix
  - [ ] Annotated idea list output

### Phase 2: CSV Schema

- [ ] Add columns to `posts_content.csv`
  - [ ] `diversity_score`, `similar_posts_ids`, `diversity_check_date`
  - [ ] `consilium_triggered`, `consilium_suggestions`, `differentiation_strategy`

- [ ] Add columns to `ideas_research.csv`
  - [ ] `diversity_score`, `similar_ideas_ids`, `consilium_required`

- [ ] Add tracking to `metrics_tracking.csv`

### Phase 3: Integration

- [ ] Update `c-03a-select-idea.md` nextStepFile
  - [ ] Change from `./c-03b-select-angle.md` to `./c-03a-diversity-check.md`

- [ ] Update `c-03a-diversity-check.md` nextStepFile
  - [ ] Point to `./c-03b-select-angle.md`

- [ ] Update `yolo-01-input.md` nextStepFile
  - [ ] Change from `./yolo-02-parallel-execute.md` to `./yolo-02a-diversity-check.md`

- [ ] Update `yolo-02a-diversity-check.md` nextStepFile
  - [ ] Point to `./yolo-02-parallel-execute.md`

### Phase 4: Agent Configuration

- [ ] Define agent roles in memory
  - [ ] `analyzer`, `content-specialist`, `strategist`, `market-analyst`, `coordinator`

- [ ] Configure agent pool reuse
  - [ ] Min pool size: 4, Max: 8
  - [ ] Warm agents between ideas

- [ ] Setup memory namespace for consilium
  - [ ] `shared-knowledge:diversity:*`
  - [ ] `shared-knowledge:consilium:*`

### Phase 5: Testing & Optimization

- [ ] Benchmark parallel vs sequential scoring
- [ ] Test consilium triggering logic
- [ ] Validate cross-idea similarity matrix
- [ ] Profile agent pool reuse efficiency
- [ ] Test cache hit rates

---

## 8. PERFORMANCE TARGETS

| Metric | Target | Status |
|--------|--------|--------|
| Single post diversity check | <5 sec (145 posts) | Design: 2-3 sec |
| Batch diversity check (5 ideas) | <2 sec total | Design: 1-1.5 sec |
| Consilium analysis | <2 min | Design: 1-1.5 min |
| Agent spawn overhead | <200ms | Design: <50ms (pool reuse) |
| Cache hit rate | 70%+ | Design target |
| Overall speedup vs sequential | 4-5x | Design: 4x |

---

## 9. RISKS & MITIGATION

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **False positives** (marking different content as similar) | User frustration, valid posts rejected | Threshold tuning (currently 60%), manual override option |
| **Consilium runs too long** | User impatience | Time limit: 2 min max, cached suggestions reuse |
| **Agent pool deadlocks** | System hangs | Hierarchical topology prevents deadlocks, timeout per agent |
| **Embedding cache grows large** | Memory pressure | TTL: 1 hour, size limit: 1GB, auto-evict LRU |
| **Similar posts added during session** | Cache stale | Refresh cache on each workflow run, versioned results |

---

## 10. SUCCESS CRITERIA

1. **Functionality:**
   - ✅ Diversity score accurately reflects content uniqueness
   - ✅ Consilium triggered when score < 60%
   - ✅ User can override or follow suggestions
   - ✅ Batch analysis works for 5+ ideas

2. **Performance:**
   - ✅ Single check: <5 sec (vs 30 sec sequential)
   - ✅ Batch check: <2 sec (vs 30 sec sequential)
   - ✅ Consilium: <2 min completion

3. **Integration:**
   - ✅ CREATE mode: seamless between steps
   - ✅ YOLO mode: batch results feed into parallel execute
   - ✅ Data persists in CSV schema
   - ✅ No breaking changes to existing steps

4. **User Experience:**
   - ✅ Clear feedback on similarity detection
   - ✅ Actionable consilium suggestions
   - ✅ Easy override for edge cases
   - ✅ Transparency in decision-making

---

## 11. APPENDIX

### A. Similarity Scoring Algorithm

```python
def calculate_diversity_score(idea, existing_posts):
    """
    Compare idea against all existing posts.
    Return diversity score (0-100).

    Similarity factors:
    - Embedding similarity (cosine): 60% weight
    - Keyword overlap: 20% weight
    - Category match: 10% weight
    - Recency bias: 10% weight (penalize similar recent posts)
    """

    similarities = []

    for post in existing_posts:
        # 60% - Semantic similarity (embeddings)
        semantic = cosine_similarity(
            idea.embedding,
            post.embedding
        )

        # 20% - Keyword overlap
        idea_keywords = extract_keywords(idea.title)
        post_keywords = extract_keywords(post.title)
        keyword_overlap = len(set(idea_keywords) & set(post_keywords)) / max(
            len(set(idea_keywords) | set(post_keywords)), 1
        )

        # 10% - Category match
        category_match = 1.0 if idea.category == post.category else 0.0

        # 10% - Recency bias
        days_old = (now() - post.date).days
        recency = 1.0 if days_old < 30 else 0.5

        # Weighted score
        similarity = (
            semantic * 0.60 +
            keyword_overlap * 0.20 +
            category_match * 0.10 +
            recency * 0.10
        )

        similarities.append(similarity)

    # Diversity = inverse of max similarity
    max_similarity = max(similarities) if similarities else 0
    diversity_score = int((1 - max_similarity) * 100)

    return diversity_score, similarities
```

### B. Consilium Prompt

```
You are participating in a consilium (expert council) to identify differentiation strategies.

CONTEXT:
- Current Idea: "{idea_title}"
- Category: {category}
- Similar Post: "{similar_post_title}" (82% similarity)
- Similar Post Content: [first 500 chars]

YOUR ROLES:
1. Content Analyst: Analyze what the similar post covers, identify gaps
2. Strategy Innovator: Propose novel angles not covered in the similar post
3. Market Analyst: Evaluate market opportunity for each angle
4. Coordinator: Synthesize and rank suggestions

TASK:
1. Analyze the similar post (what's covered, what's missing)
2. Propose 3-5 differentiation angles
3. Evaluate each by: uniqueness, audience size, conversion potential, effort
4. Rank suggestions with reasoning
5. Provide final recommendation

OUTPUT FORMAT:
Return JSON with:
{
  "analysis": "...",
  "suggestions": [
    {
      "angle": "...",
      "reasoning": "...",
      "score": 0-100,
      "effort": "low|medium|high"
    }
  ],
  "recommendation": "..."
}

CONSTRAINTS:
- Finish within 2 minutes
- Be specific and actionable
- Consider real business value
```

---

**Document Status:** Ready for Implementation
**Next Steps:** Proceed with Phase 1 (Step Files) creation

