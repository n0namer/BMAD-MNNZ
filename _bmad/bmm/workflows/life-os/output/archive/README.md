# Idea Archive

## Purpose
This archive systematically stores completed and killed ideas to enable pattern learning, calibration, and future reference.

## Structure

```
archive/
├─ completed/           # Successfully completed ideas
│  ├─ 2026-q1/         # Organized by quarter
│  ├─ 2026-q2/
│  └─ ...
├─ killed/             # Ideas stopped via pivot-or-kill
│  ├─ 2026-q1/
│  ├─ 2026-q2/
│  └─ ...
└─ patterns/           # Learned patterns from archive
   ├─ success-patterns.md       # What works well
   ├─ failure-patterns.md       # What to avoid
   ├─ domain-insights.md        # Domain-specific learnings
   └─ timeline-calibration.md   # Estimate accuracy tracking
```

## How Ideas Are Archived

### Automatic Archival

**Step 09 (Complete):** Offers archive option after idea completion
**Step X-04 (Pivot-or-Kill):** Automatically archives killed ideas

### Manual Archival

**Windows:**
```powershell
cd scripts
.\archive-idea.ps1 -IdeaId "001" -Status "completed"
.\archive-idea.ps1 -IdeaId "006" -Status "killed" -Reason "Market validation failure"
```

**macOS/Linux:**
```bash
cd scripts
./archive-idea.sh 001 completed
./archive-idea.sh 006 killed "Market validation failure"
```

## Archive Entry Format

Each archived idea includes:
- **Metadata:** Domain, complexity, score, timeline
- **Retrospective:** What went well, what could improve
- **Key Learnings:** Patterns and recommendations
- **Timeline Variance:** Planned vs actual duration
- **Artifacts:** Links to deep plans, scoring, execution tracking
- **Pattern Tags:** For searchability and pattern mining

## Pattern Mining

### Quarterly Process

During **Step V-04 (Quarterly Review)**, the system:

1. Loads all archived ideas from the quarter
2. Analyzes for common patterns (success and failure)
3. Proposes pattern definitions
4. User approves patterns
5. Patterns saved to `patterns/` folder
6. Patterns stored in global memory

### Pattern Application

Approved patterns auto-trigger recommendations during:
- **Step 02:** Scoring (complexity adjustments)
- **Step 03:** Planning (timeline adjustments)
- **Step 08:** Deep Plan (architecture recommendations)

Example:
```
💡 Pattern Match Detected: P002-Frontend-Polish

Your idea includes frontend work. Pattern P002 shows:
- 10/10 past ideas with frontend took 40% longer than estimated
- Recommendation: Add 1.4x multiplier to frontend complexity

Apply this adjustment? [Yes] [No] [Tell me more]
```

## Search Archive

**Using CLI:**
```bash
# Search completed ideas in Finance domain
npx claude-flow@v3alpha memory search -q "archive completed finance"

# Search ideas killed for market validation
npx claude-flow@v3alpha memory search -q "archive killed market-validation"

# Find ideas with >30% variance
npx claude-flow@v3alpha memory search -q "archive variance +30%"
```

**Using pattern tags:**
```bash
# Ideas with frontend complexity
npx claude-flow@v3alpha memory search -q "archive #frontend-complexity"

# Ideas with LLM acceleration
npx claude-flow@v3alpha memory search -q "archive #llm-acceleration"
```

## Benefits

### Immediate
- Systematic storage (not scattered in output/ folder)
- Easy retrieval of past work
- Pattern-based recommendations for similar ideas

### Long-term
- System learns from experience (self-improving)
- Calibration improves estimate accuracy over time
- Avoid repeating mistakes (failure patterns)
- Accelerate similar ideas (success patterns)

## Archive Statistics

**Current Status:**
- Total Archived: 0 ideas
- Completed: 0 ideas
- Killed: 0 ideas
- Patterns Discovered: 0

**Target:**
- Archive 80%+ completed ideas
- Discover 5+ patterns per quarter (after 10+ archived ideas)
- Achieve 80%+ estimate accuracy within ±30% variance

---

**Last Updated:** 2026-02-05
**Next Pattern Mining:** Q1 2026 Quarterly Review
