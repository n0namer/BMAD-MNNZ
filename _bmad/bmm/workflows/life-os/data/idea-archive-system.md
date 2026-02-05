# Idea Archive System

## Purpose
Systematically archive completed and killed ideas to enable pattern mining, learning, and future reference.

## Archive Structure

### Directory Layout
```
output/
├─ archive/
│  ├─ completed/
│  │  ├─ 2026-q1/
│  │  │  ├─ idea-001-finance-katana.md
│  │  │  ├─ idea-002-business-autoresponder.md
│  │  │  └─ ...
│  │  ├─ 2026-q2/
│  │  └─ ...
│  ├─ killed/
│  │  ├─ 2026-q1/
│  │  │  ├─ idea-006-content-blog-network.md
│  │  │  └─ ...
│  │  └─ ...
│  └─ patterns/
│     ├─ success-patterns.md
│     ├─ failure-patterns.md
│     ├─ domain-insights.md
│     └─ timeline-calibration.md
```

## Archive Entry Format

### Completed Idea Archive
```markdown
# Idea 001: Katana (Finance)

**Status:** ✅ COMPLETED
**Archived:** 2026-02-05
**Duration:** 3 weeks (Planned: 2 weeks, +50% variance)

## Summary
SaaS platform for freelancers to track income and expenses.

## Metadata
- Domain: Finance
- Track: Deep Track
- Complexity: 7/10
- Score: 4.5/5.0
- Speed Multiplier: 10x (LLM-assisted)

## Timeline
- Started: 2026-01-15
- Completed: 2026-02-05
- Planned Duration: 2 weeks
- Actual Duration: 3 weeks
- Variance: +50%

## What Went Well
1. LLM excellent for API development (18x actual speed)
2. Architecture decisions solid (no rework needed)
3. Existing code reused effectively (40% of MVP)

## What Could Improve
1. Frontend complexity underestimated by 50%
2. UI polish took 30% longer than planned
3. First-time Supabase had learning curve

## Key Learnings
- **Pattern:** Frontend always takes longer (add 1.4x multiplier)
- **Pattern:** First-time tech adds 50-100% to estimates
- **Calibration:** Speed Multiplier for Finance domain: 10x → 9x
- **Recommendation:** For similar ideas, allocate 1.5x time for UI

## Artifacts
- Deep Plan: output/idea-001/deep-plan-l1-l6.md
- Scoring: output/idea-001/scoring-report.md
- Execution Tracker: output/idea-001-execution-tracker.md
- Retrospective: output/idea-001-retrospective.md

## Pattern Tags
#frontend-complexity #first-time-tech #finance-domain #llm-acceleration #ui-polish

---
Archived by: Retrospective System (Step V-05)
Archive Date: 2026-02-05
```

### Killed Idea Archive
```markdown
# Idea 006: Blog Network (Content)

**Status:** ❌ KILLED
**Archived:** 2026-02-03
**Reason:** Pivot-or-kill decision (3+ weeks blocked, ROI negative)

## Summary
Multi-author blog network with revenue sharing.

## Metadata
- Domain: Content
- Track: Standard Track
- Complexity: 6/10
- Score: 3.8/5.0
- Duration Before Kill: 4 weeks (Planned: 2 weeks)

## Why Killed
1. **Primary Reason:** Market validation failed (no user interest)
2. **Contributing Factor:** Technical complexity underestimated
3. **Blocker:** Content moderation costs prohibitive
4. **Decision Score:** 12/40 (KILL threshold: 0-15)

## Timeline
- Started: 2026-01-06
- Killed: 2026-02-03
- Weeks Active: 4 weeks
- Milestone Progress: 2/5 milestones complete (40%)

## Pivot-or-Kill Analysis
- Goal Alignment: 4/10 (misaligned with finance goals)
- ROI Potential: 3/10 (costs outweigh revenue)
- Feasibility: 5/10 (technically feasible but not viable)
- Opportunity Cost: 8/10 (high - blocking better ideas)
- **Total:** 20/40 → KILL decision

## Key Learnings
- **Pattern:** Content moderation costs often underestimated
- **Pattern:** Market validation should precede development
- **Recommendation:** For content ideas, validate market first
- **Calibration:** Content domain complexity: +2 points default

## Artifacts
- Initial Plan: output/idea-006/workflow-plan.md
- Scoring: output/idea-006/scoring-report.md
- Execution Tracker: output/idea-006-execution-tracker.md
- Pivot-or-Kill Analysis: output/idea-006-pivot-or-kill.md

## Pattern Tags
#market-validation-failure #content-moderation #complexity-underestimated #roi-negative #killed-early

---
Archived by: Pivot-or-Kill Step (X-04)
Archive Date: 2026-02-03
Kill Reason: Market validation failure + ROI negative
```

## Pattern Mining

### Success Patterns (Learned from Completed Ideas)

**Pattern 1: LLM Excellent for API/Backend**
```yaml
pattern_id: p001-llm-backend
source: 8 completed ideas (Ideas 001, 002, 003, 005, 007, 008, 009, 011)
observation: |
  Backend APIs consistently 20-30% faster than estimated when using LLM assistance.
  Actual Speed Multiplier: 15-18x (vs assumed 10-12x)
evidence:
  - Idea 001: API in 3 days (planned 5 days)
  - Idea 002: Backend in 2 days (planned 4 days)
  - Idea 003: API + DB in 4 days (planned 6 days)
confidence: HIGH (8 data points)
recommendation: |
  Increase Speed Multiplier for API/backend work: 12x → 16x
  Apply to: Finance, SaaS, Business domains
last_updated: 2026-02-05
```

**Pattern 2: Frontend UI Polish Always Longer**
```yaml
pattern_id: p002-frontend-polish
source: 10 completed ideas (all with frontend component)
observation: |
  UI polish consistently takes 30-50% longer than estimated.
  Average variance: +42%
evidence:
  - Idea 001: UI 6 days (planned 4 days, +50%)
  - Idea 002: Frontend 5 days (planned 3 days, +67%)
  - Idea 007: UI 4 days (planned 3 days, +33%)
confidence: HIGH (10 data points)
recommendation: |
  Add 1.4x multiplier to frontend complexity scoring
  Increase UI polish estimates by 40-50%
last_updated: 2026-02-05
```

**Pattern 3: First-Time Tech Has Learning Curve**
```yaml
pattern_id: p003-learning-curve
source: 4 completed ideas with new tech
observation: |
  Using technology for first time adds 50-100% to estimates.
  Average variance: +75%
evidence:
  - Idea 001: First Supabase use (+80%)
  - Idea 003: First GraphQL (+65%)
  - Idea 005: First Docker (+90%)
confidence: MEDIUM (4 data points)
recommendation: |
  Flag novelty in complexity scoring
  Add 1.5x-2x multiplier for first-time technologies
  Consider learning phase separate from production work
last_updated: 2026-02-05
```

### Failure Patterns (Learned from Killed Ideas)

**Pattern 1: Market Validation Before Development**
```yaml
pattern_id: f001-market-validation
source: 3 killed ideas (Ideas 006, 012, 014)
observation: |
  Ideas killed due to market validation failure all started development
  before confirming user interest. Average waste: 3-4 weeks.
evidence:
  - Idea 006: 4 weeks wasted, no user interest
  - Idea 012: 3 weeks wasted, wrong target market
  - Idea 014: 5 weeks wasted, timing wrong
confidence: HIGH (3 clear cases)
recommendation: |
  Add market validation step BEFORE Step 01 for content/consumer ideas
  Require: 10+ user interviews or 100+ signups before development
  Consider: Landing page test (week 0) before full workflow
last_updated: 2026-02-05
```

**Pattern 2: Content Moderation Costs Underestimated**
```yaml
pattern_id: f002-content-moderation
source: 2 killed ideas (Ideas 006, 015)
observation: |
  Content-heavy ideas consistently underestimate moderation costs.
  Often 3x-5x actual costs vs estimates.
evidence:
  - Idea 006: $500/mo estimated, $2500/mo actual
  - Idea 015: $300/mo estimated, $1500/mo actual
confidence: MEDIUM (2 data points)
recommendation: |
  Add "Content Moderation" cost factor to scoring
  Default multiplier: 3x for estimates
  Consider automated moderation tools from start
last_updated: 2026-02-05
```

## Pattern Discovery Process

### Automated Pattern Mining (Quarterly)

**Trigger:** Quarterly Review (step-v-04)

**Process:**
1. Load all completed/killed ideas from quarter
2. Group by domain, complexity, track
3. Analyze variance patterns
4. Identify common success factors
5. Identify common failure factors
6. Update pattern database
7. Adjust calibration files

**Example Query:**
```bash
# Find all ideas with >30% positive variance
npx claude-flow@v3alpha memory search -q "archive status:completed variance:+30"

# Find all ideas killed for same reason
npx claude-flow@v3alpha memory search -q "archive status:killed reason:market-validation"
```

### Pattern Application

When processing new ideas:
```markdown
💡 **Pattern Match Detected**

Your idea matches Pattern P002 (Frontend UI Polish):
- 8/10 past ideas with frontend took 40% longer than estimated
- Recommendation: Add 1.4x to frontend complexity

Apply this adjustment? [Y]es / [N]o / [Tell me more]
```

## Archive Commands

```bash
# Archive completed idea
/archive {idea-id} --status completed

# Archive killed idea
/archive {idea-id} --status killed --reason "{reason}"

# Search archive
/archive search "finance domain completed"

# Show patterns
/archive patterns success
/archive patterns failure
/archive patterns domain:finance

# Pattern matching
/archive match {current-idea-id}
# Returns: Similar ideas + learned patterns applicable to current idea
```

## Memory Storage

**Archive entry:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "archive" \
  --key "completed:idea-001:2026-q1" \
  --content "{
    id: '001',
    status: 'completed',
    domain: 'finance',
    variance: 0.50,
    learnings: [...],
    tags: [...]
  }"
```

**Pattern storage:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "patterns:p001-llm-backend" \
  --content "{pattern definition}"
```

## Benefits

**Immediate:**
- Systematic archival (not scattered)
- Easy retrieval of past work
- Pattern-based recommendations

**Long-term:**
- System learns from experience
- Calibration improves over time
- Avoid repeating mistakes
- Accelerate similar ideas

---

**Last Updated:** 2026-02-05
**Total Archived:** 0 completed, 0 killed
**Patterns Discovered:** 0
