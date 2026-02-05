# Portfolio Quick Score UI

**Version:** 1.0.0
**Purpose:** User interface for batch quick scoring and comparison
**Reference:** data/batch-quick-score.md (scoring methodology)

---

## Comparison Table Format

**After scoring all ideas:**

```markdown
## Portfolio Quick Scores ({N} Ideas)

| Rank | Idea Name | Impact | Feasibility | Fit | Quick Score | Track Suggestion |
|------|-----------|--------|-------------|-----|-------------|------------------|
| 1    | {Idea A}  | 8/10   | 9/10        | 7/10| **8.0**     | Deep Track       |
| 2    | {Idea B}  | 9/10   | 6/10        | 8/10| **7.7**     | Standard Track   |
| 3    | {Idea C}  | 7/10   | 8/10        | 6/10| **7.1**     | Standard Track   |
| 4    | {Idea D}  | 6/10   | 7/10        | 7/10| **6.6**     | Standard Track   |
| 5    | {Idea E}  | 8/10   | 4/10        | 5/10| **5.9**     | Defer            |
| 6    | {Idea F}  | 5/10   | 5/10        | 4/10| **4.7**     | Defer            |

### Insights

**High Potential (Quick Score ≥ 7.5):**
- {Idea A}: High feasibility + strong impact
- {Idea B}: Breakthrough potential but higher risk

**Strong Candidates (Quick Score 6.0-7.4):**
- {Idea C}: Balanced across all dimensions
- {Idea D}: Safe bet, moderate returns

**Defer/Revisit (Quick Score < 6.0):**
- {Idea E}: High impact but feasibility concerns
- {Idea F}: Weak across all dimensions
```

---

## Sort Options

**Default sort:** By Quick Score (descending)

**Alternative sorts:**
```
[S]ort menu:
1. Quick Score (default)
2. Impact (prioritize value)
3. Feasibility (prioritize execution)
4. Fit (prioritize context alignment)
5. Domain (group by category)
```

---

## User Decision Interface

```
What would you like to do?

[S]elect manually - Choose which ideas to process
[M]odify scores - Adjust any quick scores before deciding
[A]uto-accept - Use my recommendations
[C]omments - Add notes to any idea
[R]e-sort - Change sorting criteria
[D]one - Finalize selection
```

### Option Details

**[S]elect manually:**
- Show numbered list of all ideas
- User types idea numbers to select (e.g., "1,3,5")
- Confirm selection before proceeding

**[M]odify scores:**
- Prompt: "Which idea to adjust? [1-N]"
- Show current scores for selected idea
- Allow editing Impact, Feasibility, or Fit
- Recalculate Quick Score automatically

**[A]uto-accept:**
- Use recommendation engine output (see portfolio-recommendation-engine.md)
- Confirm: "Accept recommendations? [Y]es/[N]o"

**[C]omments:**
- Prompt: "Add comment to which idea? [1-N]"
- Free-text note (saved to memory)
- Example: "Revisit in Q3 when budget available"

**[R]e-sort:**
- Show sort menu
- Re-render table with new sort order

**[D]one:**
- Finalize selection
- Proceed to routing logic

---

## Track Suggestion Logic

**Displayed in table column:**

| Quick Score | Track Suggestion |
|-------------|------------------|
| 8.0-10.0    | Deep Track       |
| 6.0-7.9     | Standard Track   |
| 4.0-5.9     | Defer            |
| 0.0-3.9     | Reject           |

**Color Coding (if terminal supports):**
- 🟢 Deep Track (green)
- 🟡 Standard Track (yellow)
- 🟠 Defer (orange)
- 🔴 Reject (red)

---

## Interactive Scoring Flow

**For each idea (2-3 min):**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scoring: Idea {N} - {Name}

Description: {1-2 sentence description}
Domain: {domain}
Complexity: {1-10}

**Impact** (0-10): How much does this move the needle?
[Reference: data/batch-quick-score.md lines 33-101]
Your score: ___

**Feasibility** (0-10): Can we actually do this?
[Reference: data/batch-quick-score.md lines 103-182]
Your score: ___

**Fit** (0-10): Does this align with goals and context?
[Reference: data/batch-quick-score.md lines 184-253]
Your score: ___

Quick Score: {calculated} | Track: {suggestion}

[N]ext idea | [M]odify scores | [S]kip to summary
```

---

## Batch Scoring Progress

**Show progress indicator:**
```
📊 Scoring Progress

Completed: {X}/{N} ideas
Remaining: {N-X} ideas (~{est_time} minutes)

[█████████░░] 80%
```

---

## Quality Validation

**Before finalizing:**

```
⚠️ Quality Check

- [ ] All ideas scored (no missing dimensions)
- [ ] Scores reviewed and confirmed
- [ ] Selection aligns with WIP capacity
- [ ] Deferred ideas have clear reasons

Proceed?
[Y]es, finalize | [N]o, review again
```
