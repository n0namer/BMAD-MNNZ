# Subprocess Integration Guide

**For Step File Maintainers**

This guide shows exactly how to integrate subprocess optimization patterns into Life OS workflow step files.

---

## QUICK START

### 3 Subprocess Patterns Available

1. **Template Loader** - Reduce 1,000+ template lines → 200-400 lines
2. **Example Loader** - Reduce 300+ example lines → 80-150 lines
3. **Search Parallelizer** - Reduce 6-10s search time → 4-6s

### How to Choose Your Pattern

**In your step file, ask:**

1. "Do we load templates from disk?"
   - YES → Use **Pattern 1: Template Loader**
   - NO → Continue

2. "Do we show examples to users?"
   - YES → Use **Pattern 2: Example Loader**
   - NO → Continue

3. "Do we search for patterns/options using Search Orchestrator?"
   - YES → Use **Pattern 3: Search Parallelizer**
   - NO → No subprocess optimization needed

---

## PATTERN 1: TEMPLATE LOADER

### When to Use
- step-04.5 (TRIZ templates)
- step-05 (MCDA templates)
- step-06 (Integration template)
- step-08 (Planning templates)
- step-09 (Project snapshot template)

### Step File Format

**In YAML frontmatter, add:**
```yaml
---
name: 'step-05-scoring'
templates:
  mcda: '../data/mcda-criteria-detailed.md'
subprocessLoadingStrategy: 'on-demand'
---
```

**In step content, add before template reference section:**

```markdown
#### MCDA Criteria Definitions Loading (Subprocess - Pattern 1)

**Launch a subprocess that:**
1. Loads `data/mcda-criteria-detailed.md`
2. Filters to domain-specific criteria (from step-01 or auto-detected)
3. Returns ONLY relevant criteria (60-80 lines instead of 300+)

**Subprocess command:**
```bash
node scripts/subprocess-template-loader.js "mcda-criteria-detailed" "data" \
  --context "{projectDomain: 'business'}"
```

**Subprocess returns:**
```json
{
  "success": true,
  "templateName": "mcda-criteria-detailed",
  "lines": 75,
  "lineSavings": 225,
  "sections": 5,
  "preFilledFields": 1
}
```

**Graceful fallback:** If subprocess unavailable, load full file in main context.

**Performance gain:** 75% context reduction for MCDA criteria
```

### Complete Step File Example

```markdown
# Step 5: Scoring

## Subprocess Template Loading Integration

### 1. MCDA Criteria Loading

**User action:** Selects scoring approach, needs criteria definitions

**Subprocess launches automatically:**
```bash
node scripts/subprocess-template-loader.js "mcda-criteria-detailed" "data" \
  --context "{domain: 'business'}"
```

**Subprocess returns:** 60-80 lines (domain-specific criteria only)

**Fallback:** If subprocess unavailable, proceed with full criteria list (300+ lines)

### 2. Template Usage

Present the subprocess-returned criteria to user:
- Business domain: Market Opportunity, Competitive Advantage, etc.
- Finance domain: Expected Value, Option Value, etc.
- User can: Adjust weights, confirm, or [L]oad all criteria

**Context savings:** ~225 lines saved by loading only domain criteria
```

---

## PATTERN 2: EXAMPLE LOADER

### When to Use
- step-00 (Foundation check examples)
- step-00.5 (Project stage examples)
- step-00.6 (Resource assessment examples)
- step-00.7 (Optimization examples)
- step-04 (Validation examples)
- step-05 (Scoring examples)

### Step File Format

**In step content, add:**

```markdown
#### Example Loading (Subprocess - Pattern 2)

**When user says "Show examples" or "[?] Examples":**

**Launch a subprocess that:**
1. Loads `data/{examples-file}.md`
2. Parses examples by category
3. Matches 2-3 examples relevant to:
   - User's domain (from workflow-plan or user input)
   - Current question/challenge
4. Returns ONLY matching examples (80-150 lines instead of 300+)

**Subprocess command:**
```bash
node scripts/subprocess-example-loader.js "validation-examples.md" "business" "[scoring,quality]"
```

**Subprocess returns:**
```json
{
  "success": true,
  "exampleFile": "validation-examples.md",
  "totalAvailable": 12,
  "matching": 3,
  "linesSaved": 550,
  "reduction": "75%"
}
```

**Graceful fallback:** If subprocess unavailable, show all examples.

**Performance gain:** 75% context reduction for examples
```

### Complete Step File Example

```markdown
# Step 4: Consilium (Expert Review)

### Validation Examples (Subprocess)

**When asking for quality examples:**

The subprocess will automatically load 2-3 examples matching:
- Your domain (business/finance/health/personal)
- Current quality challenge
- Similar to your project stage

**Subprocess runs automatically on [?] Examples:**
```bash
node scripts/subprocess-example-loader.js "validation-examples.md" "{domain}" "{searchTerms}"
```

**Expected output:** 2-3 relevant examples instead of all 12 examples

**Context savings:** ~550 lines saved by loading only relevant examples

**All examples available?** User can request `[L]oad all examples` for full reference
```

---

## PATTERN 3: SEARCH PARALLELIZER

### When to Use
- step-00 (Goals discovery - Search Orchestrator)
- step-00.5 (Project stage - Search Orchestrator)
- step-00.6 (Resource assessment - Search Orchestrator)
- step-00.7 (Optimization intelligence - Search Orchestrator)
- step-01 (Collect ideas - Search Orchestrator)
- step-02 (Roles discovery - Search Orchestrator)
- step-03 (Specialist match - Search Orchestrator)

### Step File Format

**In step content, find "Search Orchestrator Protocol" section and add:**

```markdown
### Search Orchestrator (Parallel Subprocess - Pattern 3)

**When user needs help finding patterns or making decisions:**

The system automatically launches 3 parallel search subprocesses:

**Subprocess 1: CLI Memory Search (1.5s timeout)**
```bash
npx claude-flow@v3alpha memory search -q "{user_query}"
```
Returns: Patterns from project memory

**Subprocess 2: Local MD Search (1.5s timeout)**
```bash
rg "{search_terms}" data/ --json
```
Returns: Matching sections from local documentation

**Subprocess 3: Web/MCP Search (2s timeout)**
- Perplexity API, GitHub search, or other configured sources
- Returns: External patterns and best practices

**Aggregation (after all 3 complete):**
1. Combine results from all sources
2. Rank by relevance + source credibility
3. Present top 2-4 results to user
4. User selects one, or requests different search

**Parallel command:**
```bash
node scripts/subprocess-search-parallel.js "{user_query}" --timeout 5000
```

**Returns:**
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

**Graceful fallback:** If parallel unavailable, search sequentially (6-10s)

**Performance gain:** 30-40% time reduction (6-10s → 4-6s)
```

### Complete Step File Example

```markdown
# Step 1: Collect Ideas

## Search Orchestrator Integration

### When Searching for Idea Sources

The system automatically parallelizes searches across 3 sources:

1. **Memory search** - Find similar projects you've worked on
2. **Local search** - Find templates, patterns, best practices
3. **Web search** - Find external inspiration, benchmarks, competitors

**All 3 run in parallel (4-6s total) instead of sequential (6-10s)**

**Example workflow:**
```
User: "Help me find idea sources for my startup"

System launches 3 parallel subprocesses:
- Subprocess 1: Search memory for startup patterns
- Subprocess 2: Search local for business frameworks
- Subprocess 3: Search web for startup best practices

All 3 complete in 4-6 seconds (35% faster)

Results aggregated by relevance:
Top 4 results shown to user
```

**Context savings:** 30-40% time reduction, enabling faster user interactions
```

---

## INTEGRATION CHECKLIST

### For each step file you're updating:

- [ ] Identify which pattern(s) apply (1, 2, and/or 3)
- [ ] Add pattern documentation to step file
- [ ] Include subprocess command example
- [ ] Include JSON return format example
- [ ] Add graceful fallback instructions
- [ ] Document performance gains/savings
- [ ] Test with subprocess available
- [ ] Test with subprocess unavailable (fallback)

### Testing Checklist

For **Pattern 1 (Template Loader):**
- [ ] `node scripts/subprocess-template-loader.js "triz-quick" "triz"`
- [ ] Verify returns correct lines count
- [ ] Verify pre-fills work with context
- [ ] Verify fallback works when template missing

For **Pattern 2 (Example Loader):**
- [ ] `node scripts/subprocess-example-loader.js "validation-examples.md" "business"`
- [ ] Verify returns only matching examples
- [ ] Verify scoring works correctly
- [ ] Verify fallback works when file missing

For **Pattern 3 (Search Parallelizer):**
- [ ] `node scripts/subprocess-search-parallel.js "authentication pattern"`
- [ ] Verify all 3 search sources complete
- [ ] Verify time is <5 seconds
- [ ] Verify fallback works when npx unavailable

---

## REAL-WORLD EXAMPLES

### Example 1: Step 5 (Scoring) - Both Pattern 1 and 2

**BEFORE (no subprocess):**
```
Load templates:
- mcda-criteria-detailed.md (300 lines)
- comparative-ranking-protocol.md (200 lines)
- stage-gate-mapping.md (400 lines)

Load examples:
- scoring-examples.md (309 lines)
- comparative-scoring-examples.md (341 lines)

TOTAL CONTEXT: ~1,550 lines per step execution
```

**AFTER (with subprocess):**
```
Load via subprocess 1:
- mcda-criteria-detailed.md → FILTERED → 75 lines (saved 225)
- comparative-ranking-protocol.md → FILTERED → 50 lines (saved 150)

Load via subprocess 2:
- scoring-examples.md → FILTERED → 150 lines (saved 159)
- comparative-scoring-examples.md → FILTERED → 100 lines (saved 241)

TOTAL CONTEXT: ~375 lines per step execution
SAVINGS: 1,175 lines (75% reduction!)
```

### Example 2: Step 1 (Collect Ideas) - Pattern 3 Only

**BEFORE (sequential search):**
```
Step 1: "Find idea sources"
→ Search memory (2-3 seconds)
→ Search local files (1-2 seconds)
→ Search web (3-5 seconds)

TOTAL TIME: 6-10 seconds
```

**AFTER (parallel search):**
```
Step 1: "Find idea sources"
→ Subprocess launches 3 parallel searches
  ├─ Search memory (2-3s in parallel)
  ├─ Search local (1-2s in parallel)
  └─ Search web (3-5s in parallel)
→ All complete together: 4-6 seconds

TOTAL TIME: 4-6 seconds
TIME SAVINGS: 2-4 seconds per search (30-40% faster)
```

### Example 3: Foundation Steps (0-0.7) - Pattern 2 Only

**BEFORE (all examples loaded):**
```
Foundation check: Load 280-line examples file
Project stage: Load 260-line examples file
Resource assessment: Load 300-line examples file
Optimization intelligence: Load 270-line examples file

TOTAL: ~1,110 lines for foundation steps
```

**AFTER (subprocess filtering):**
```
Foundation check: Subprocess returns 100-line examples → saved 180
Project stage: Subprocess returns 100-line examples → saved 160
Resource assessment: Subprocess returns 120-line examples → saved 180
Optimization intelligence: Subprocess returns 100-line examples → saved 170

TOTAL: ~420 lines for foundation steps
SAVINGS: 690 lines (62% reduction!)
```

---

## MARKDOWN TEMPLATE

**Copy-paste this into your step file where you want subprocess integration:**

```markdown
### {Operation} Loading (Subprocess - Pattern {1|2|3})

**Launch a subprocess that:**
1. [Description of what subprocess does]
2. [Second step]
3. [Third step]

**Subprocess command:**
```bash
node scripts/subprocess-{template|example|search}-{loader|parallel}.js "{parameter}" [--context/--domain/--timeout] "{value}"
```

**Subprocess returns:**
```json
{
  "success": true,
  "message": "..."
}
```

**Graceful fallback:** If subprocess unavailable, [fallback behavior].

**Performance gain:** [Context or time reduction]
```

---

## TROUBLESHOOTING

### Subprocess not found
- Check: `ls scripts/subprocess-*.js`
- Fix: Run `chmod +x scripts/subprocess-*.js` (Unix)

### Node.js not available
- Check: `node --version`
- Fix: Install Node.js v14+

### Template/example file not found
- Check: Path in subprocess command matches actual location
- Fix: Update file path relative to step execution directory

### Timeout exceeded
- Check: Increase `--timeout` parameter
- Fix: Subprocess will gracefully fall back after timeout

### Filter returned no results
- Check: Domain or search terms too specific
- Fix: Use broader domain or empty domain ("") for all results

---

## PERFORMANCE SUMMARY

| Pattern | Context Saved | Time Saved | Best For |
|---------|--------------|-----------|----------|
| **Template Loader** | 50-80% | N/A | 5 template-heavy steps |
| **Example Loader** | 67-75% | N/A | 6-8 example-heavy steps |
| **Search Parallelizer** | N/A | 30-40% | 7 search-intensive steps |
| **ALL COMBINED** | **55% avg** | **25% avg** | **Full workflow** |

**Total project impact:**
- Context reduction: ~8,000 lines per session
- Time reduction: ~25-30% faster user interactions
- Token efficiency: +15-20% due to smaller context

---

## NEXT STEPS

1. **Implement in steps:** Follow integration checklist
2. **Test locally:** Run subprocess tests in your environment
3. **Measure results:** Track actual context/time savings
4. **Iterate:** Adjust timeouts, fallback strategies based on real data
5. **Document:** Update step file documentation with actual metrics
