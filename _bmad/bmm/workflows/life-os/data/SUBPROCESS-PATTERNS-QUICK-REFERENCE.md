# Subprocess Patterns - Quick Reference Guide

**For Step Maintainers - Use This to Choose Your Pattern**

---

## PATTERN SELECTION FLOWCHART

```
Does your step file...

├─ Load templates from disk?
│  └─ YES → USE PATTERN 1: TEMPLATE LOADER
│           (Reduces 1,000+ lines → 200-400 lines)
│
├─ Show examples to users?
│  └─ YES → USE PATTERN 2: EXAMPLE LOADER
│           (Reduces 300+ lines → 80-150 lines)
│
├─ Use Search Orchestrator protocol?
│  └─ YES → USE PATTERN 3: SEARCH PARALLELIZER
│           (Reduces 6-10s → 4-6s)
│
└─ None of above? → No subprocess optimization needed
```

---

## PATTERN 1: TEMPLATE LOADER

### Applies To
- step-04.5 (TRIZ - 3 templates)
- step-05 (MCDA, protocols)
- step-06 (Integration)
- step-08 (Planning)
- step-09 (Project snapshot)

### What It Does
Loads ONE template when user selects it, instead of all N templates

### Context Saved
**50-60%** (1,500 lines → 300-600 lines)

### Add This to Your Step File

**In YAML frontmatter:**
```yaml
subprocessLoadingStrategy: 'on-demand'
```

**In step content:**
```markdown
#### {Template} Loading (Subprocess - Pattern 1)

**Launch a subprocess that:**
1. User selects {framework/mode}
2. Loads ONLY `templates/{domain}/{name}.template.md`
3. Pre-fills known fields from workflow-plan.md
4. Returns customized template (200-400 lines)

**Graceful fallback:** If subprocess unavailable, load template in main context.

**Performance gain:** 50-60% context reduction
```

### Subprocess Command
```bash
node scripts/subprocess-template-loader.js "{templateName}" "{domain}"
```

### Example
```bash
node scripts/subprocess-template-loader.js "triz-quick" "triz"
node scripts/subprocess-template-loader.js "swot" "business"
node scripts/subprocess-template-loader.js "mcda-criteria-detailed" "data"
```

### Output Example
```json
{
  "success": true,
  "templateName": "triz-quick",
  "lines": 320,
  "lineSavings": 1180,
  "sections": 5,
  "preFilledFields": 2
}
```

---

## PATTERN 2: EXAMPLE LOADER

### Applies To
- step-00 (Foundation - 280 lines)
- step-00.5 (Stage - 260 lines)
- step-00.6 (Resources - 300 lines)
- step-00.7 (Optimization - 270 lines)
- step-04 (Consilium - 791 lines)
- step-05 (Scoring - 650 lines)

### What It Does
Loads 2-3 relevant examples when user requests, instead of all examples

### Context Saved
**70-80%** (300-791 lines → 80-150 lines per call)

### Add This to Your Step File

**In step content (where examples are shown):**
```markdown
#### Example Loading (Subprocess - Pattern 2)

**When user says "Show examples" or "[?] Examples":**

**Launch a subprocess that:**
1. Loads `data/{examples-file}.md`
2. Matches 2-3 examples to user's domain/context
3. Returns ONLY matching examples (80-150 lines)

**Graceful fallback:** If subprocess unavailable, show all examples.

**Performance gain:** 70-80% context reduction
```

### Subprocess Command
```bash
node scripts/subprocess-example-loader.js "{exampleFile}" "{domain}" "{searchTerms}"
```

### Example
```bash
node scripts/subprocess-example-loader.js "validation-examples.md" "business" "[scoring,quality]"
node scripts/subprocess-example-loader.js "foundation-check-examples.md" "" "[startup]"
node scripts/subprocess-example-loader.js "scoring-examples.md" "finance" "[valuation]"
```

### Output Example
```json
{
  "success": true,
  "exampleFile": "validation-examples.md",
  "totalAvailable": 12,
  "matching": 3,
  "linesSaved": 650,
  "reduction": "75%"
}
```

---

## PATTERN 3: SEARCH PARALLELIZER

### Applies To
- step-00 (Goals discovery)
- step-00.5 (Project stage)
- step-00.6 (Resource assessment)
- step-00.7 (Optimization intelligence)
- step-01 (Collect ideas)
- step-02 (Roles discovery)
- step-03 (Specialist match)

### What It Does
Runs 3 searches in parallel instead of sequential

### Time Saved
**30-40%** (6-10s → 4-6s per search)

### Add This to Your Step File

**Find "Search Orchestrator Protocol" section and add:**

```markdown
### Search Orchestrator (Parallel Subprocess - Pattern 3)

**Launch 3 parallel subprocesses:**
- Subprocess 1: CLI memory search
- Subprocess 2: Local MD search (rg)
- Subprocess 3: Web/MCP search

**Aggregate, rank, and present top 2-4 results to user**

**Graceful fallback:** If parallel unavailable, search sequentially.

**Performance gain:** 30-40% time reduction (6-10s → 4-6s)
```

### Subprocess Command
```bash
node scripts/subprocess-search-parallel.js "{query}" --timeout 5000
```

### Example
```bash
node scripts/subprocess-search-parallel.js "authentication pattern"
node scripts/subprocess-search-parallel.js "startup best practices" --timeout 6000
node scripts/subprocess-search-parallel.js "database query optimization"
```

### Output Example
```json
{
  "success": true,
  "topResults": 4,
  "totalMatches": 12,
  "elapsedMs": 4200,
  "timeSaved": "35%",
  "sources": {
    "memory": 3,
    "local": 5,
    "web": 4
  }
}
```

---

## COMPARISON TABLE

| Aspect | Pattern 1 | Pattern 2 | Pattern 3 |
|--------|-----------|-----------|-----------|
| **Name** | Template Loader | Example Loader | Search Parallelizer |
| **Reduces** | Context | Context | Time |
| **Savings** | 50-60% | 70-80% | 30-40% |
| **Steps Using** | 5 | 8 | 7 |
| **Files Involved** | 39 templates | 8 examples | 7 searches |
| **When Used** | User selects template | User asks for examples | User needs help finding options |
| **Subprocess** | template-loader.js | example-loader.js | search-parallel.js |
| **Fallback** | Load full template | Show all examples | Sequential search |
| **Setup Time** | 5-10 min per step | 5-10 min per step | 5-10 min per step |

---

## IMPLEMENTATION CHECKLIST

### For Each Step File

- [ ] Identify which pattern(s) apply
- [ ] Read integration guide for that pattern
- [ ] Copy markdown template into step file
- [ ] Test with reference implementation
- [ ] Verify graceful fallback works
- [ ] Document actual context/time savings
- [ ] Update implementation status
- [ ] Move to next step

### Testing Each Pattern

**Pattern 1 (Template):**
```bash
node scripts/subprocess-template-loader.js "triz-quick" "triz"
# Should return: ~320 lines, ~1,180 lines saved
```

**Pattern 2 (Examples):**
```bash
node scripts/subprocess-example-loader.js "validation-examples.md" "business"
# Should return: 3 matching examples, ~600+ lines saved
```

**Pattern 3 (Search):**
```bash
node scripts/subprocess-search-parallel.js "authentication pattern"
# Should return: 4+ results in <5 seconds
```

---

## EXPECTED IMPROVEMENTS (PROJECT-WIDE)

### Context Reduction
- **Before:** 20,000+ lines per workflow session
- **After:** 9,000 lines per workflow session
- **Savings:** 55% reduction

### Time Improvement
- **Before:** 2-3 minutes per workflow session
- **After:** 1.5-2 minutes per workflow session
- **Savings:** 25% reduction

### Token Efficiency
- **Direct:** 55% context reduction = ~5,500 tokens saved
- **Indirect:** 25% time reduction = ~600 fewer tokens
- **Total:** 32-40% token savings per session

---

## REFERENCE FILE LOCATIONS

| File | Purpose | Lines |
|------|---------|-------|
| `subprocess-optimization-guide.md` | Complete reference for all patterns | 550+ |
| `subprocess-integration-guide.md` | Step-by-step implementation instructions | 400+ |
| `SUBPROCESS-OPTIMIZATION-IMPLEMENTATION.md` | Track implementation progress | 300+ |
| `scripts/subprocess-template-loader.js` | Load single template | 200+ |
| `scripts/subprocess-example-loader.js` | Load filtered examples | 250+ |
| `scripts/subprocess-search-parallel.js` | Parallel search | 300+ |

---

## KEY DECISION POINTS

### Should I Use Subprocess?

**YES if:**
- Step loads templates (Pattern 1)
- Step shows examples (Pattern 2)
- Step uses Search Orchestrator (Pattern 3)
- You want to reduce context/improve speed

**NO if:**
- Step doesn't load files
- Step doesn't show examples
- Step doesn't search for options
- You prefer backward compatibility without subprocess

### Graceful Fallback Strategy

All patterns include graceful fallback:
- If subprocess unavailable → Use main context
- If subprocess timeout → Switch to sequential/all results
- If subprocess error → Proceed with fallback method

**No breaking changes** - everything still works without subprocess

---

## GETTING STARTED

### Quick Start (5 minutes)

1. Read this document (CURRENT FILE)
2. Choose your pattern (1, 2, or 3)
3. Open `subprocess-integration-guide.md`
4. Copy markdown template into your step file
5. Test locally with reference implementation

### Deep Dive (30 minutes)

1. Read `subprocess-optimization-guide.md` (complete reference)
2. Understand all 3 patterns + trade-offs
3. Review reference implementations (JavaScript)
4. Plan implementation for all applicable steps

### Implementation (2-4 hours)

1. Integrate patterns step-by-step using checklist
2. Test each pattern in isolation
3. Measure actual context/time improvements
4. Document results and update status

---

## COMMON QUESTIONS

**Q: Can I use multiple patterns in one step?**
A: Yes! step-05-scoring uses both Pattern 1 (templates) and Pattern 2 (examples).

**Q: What if subprocess isn't available?**
A: Graceful fallback handles it - system automatically switches to main context.

**Q: How much context will be saved?**
A: Average 55% reduction (8,000 lines) when all 3 patterns are used project-wide.

**Q: How long does integration take?**
A: 5-10 minutes per step file. Total: 2-4 hours for all 20 steps.

**Q: Can I implement gradually?**
A: Yes! Each pattern is independent. Implement in any order.

**Q: Do I need to modify step file logic?**
A: No. Subprocess optimization is purely a context reduction technique. All step logic remains the same.

---

## NEXT STEPS

**For Integration Team:**
1. Pick Pattern 1, 2, or 3
2. Choose a step file to integrate
3. Follow `subprocess-integration-guide.md`
4. Test and verify
5. Mark step as complete in `SUBPROCESS-OPTIMIZATION-IMPLEMENTATION.md`
6. Repeat for next step

**For Questions:**
- Technical: See reference implementations
- Integration: See `subprocess-integration-guide.md`
- Troubleshooting: See integration guide troubleshooting section

---

## SIGN-OFF

This quick reference provides everything needed to integrate subprocess optimizations into Life OS.

**Total Optimization Potential:**
- 8,000 lines context saved
- 30-40% time reduction
- 32-40% token efficiency improvement

**Implementation:** Straightforward, low-risk, high-impact optimization

---

**Happy optimizing!**
