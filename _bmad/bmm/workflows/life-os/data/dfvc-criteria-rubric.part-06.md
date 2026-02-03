| **0.0-2.9** | **Reject** | Do not pursue | Fundamental flaws (poor fit, unviable economics) |

### Multi-Dimensional Gate (All Dimensions Matter)

**VETO RULE**: If ANY dimension scores <3.0, project is automatically **LOW PRIORITY** regardless of total score.

**Rationale**: A 9.0 Desirability project with 2.0 Feasibility will fail. All four dimensions must clear minimum thresholds.

| Dimension | Minimum Threshold | Veto Trigger |
|-----------|-------------------|--------------|
| Desirability (D) | ≥4.0 | <3.0 (market doesn't care) |
| Feasibility (F) | ≥4.0 | <3.0 (can't build it) |
| Viability (V) | ≥4.0 | <3.0 (unsustainable economics) |
| Competition (C) | ≥3.0 | <2.0 (impossible to win) |

### Portfolio Balancing

When prioritizing multiple projects, balance:
- **Quick wins** (High F + V, moderate D + C) - Build momentum
- **Moonshots** (High D + V, low F + C) - Long-term upside
- **Cash cows** (High V + C, moderate D + F) - Sustain operations
- **Strategic bets** (High D + C, moderate F + V) - Market positioning

**Example Portfolio**:
- 60% Quick wins (score 6.5-7.5)
- 20% Moonshots (score 7.0-8.5, but high variance)
- 15% Cash cows (score 6.0-7.0, stable)
- 5% Strategic bets (score 5.5-7.0, strategic value)

---

## 8. Usage Workflow

### Step 1: Gather Evidence
For each sub-criterion, collect quantitative data:
- Market research, customer interviews, surveys
- Technical audits, resource inventories, dependency maps
- Financial models (CLV, CAC, margin, payback)
- Competitive analysis, SWOT, Porter's Five Forces

### Step 2: Score Each Sub-Criterion
Use scoring scales (1-10) with evidence-based anchors. Avoid subjective guesses.

### Step 3: Calculate Dimension Scores
Apply sphere-specific weights to sub-criteria within each dimension (D, F, V, C).

### Step 4: Calculate Total Score
Apply sphere-specific weights to D, F, V, C dimensions.

### Step 5: Apply Veto Rules
Check if any dimension <3.0. If yes → Reject or deprioritize.

### Step 6: Compare Against Portfolio
Rank all projects by total score, apply portfolio balancing strategy.

### Step 7: Document and Review
Store scoring artifacts, revisit quarterly as market/resources change.

---

## 9. Anti-Patterns & Common Mistakes

### Mistake 1: Ignoring Evidence Requirements
**Problem**: Scoring based on gut feeling, not data.

**Example**: Assigning Market Size = 8 without TAM/SAM analysis.

**Fix**: Require evidence for each score. If evidence unavailable → Score = 5 (neutral) or conduct research sprint.

---

### Mistake 2: Overweighting Single Dimension
**Problem**: Pursuing high Desirability project despite impossible Feasibility.

**Example**: "Everyone wants this!" (D=9) but "We have no developers" (F=2).

**Fix**: Apply veto rules. Reject projects with ANY dimension <3.0.

---

### Mistake 3: Static Scoring (No Revisit)
**Problem**: Market changes, but scores remain fixed from initial assessment.

**Example**: Scored in Q1 2023, still using same scores in Q4 2024 (2 years later).

**Fix**: Quarterly review cadence. Update scores as market, resources, competition evolve.

---

### Mistake 4: Mismatched Sphere Weights
**Problem**: Using Business weights for Personal project, or Finance weights for Creative project.

**Example**: Personal learning project penalized for low Market Size (irrelevant criterion).

**Fix**: Always select appropriate sphere weights before scoring. Custom weights allowed if predefined spheres don't fit.

---

### Mistake 5: Confusing Scoring Scales
**Problem**: Mixing 1-10 scale with 0-100 scale, or inverting scales (higher = worse).

**Example**: Technical Complexity scored 9 = "very complex" when 9 should = "trivial" (easier).

**Fix**: Use consistent 1-10 scale where **10 = BEST** for ALL sub-criteria. Invert negative criteria (e.g., complexity → simplicity).

---

## 10. Integration with Life-OS

### Workflow Integration Points

**Pre-Work (Ideation → Validation)**:
- Use D/F/V/C rubric in `idea-validation.md` step
- Score all ideas before adding to project backlog
- Filter out projects with Total Score <5.0 (Medium priority threshold)

**Active Work (Planning → Execution)**:
- Reference D/F/V/C scores in `project-charter.md` (Why This Project section)
- Use Competition score to inform differentiation strategy
- Use Feasibility score to allocate resources and set timelines

**Retrospective (Review → Learning)**:
- Compare predicted D/F/V/C scores vs. actual outcomes
- Calibrate scoring model (were high-scoring projects actually successful?)
- Update sphere weights based on retrospective data

### Storage & Retrieval

**File Location**: `_bmad/life-os/projects/{project-name}/dfvc-score.md`

**Template**:
```markdown
# D/F/V/C Score - {Project Name}

**Sphere**: {Business | Finance | Personal | etc.}
**Scored Date**: {YYYY-MM-DD}
**Scored By**: {Name}

## Desirability (D = {score}/10)
- Market Size: {score} - {justification}
- Need Intensity: {score} - {justification}
- Willingness to Pay: {score} - {justification}
- Competitive Advantage: {score} - {justification}

## Feasibility (F = {score}/10)
- Technical Complexity: {score} - {justification}
- Time to MVP: {score} - {justification}
- Resource Availability: {score} - {justification}
- Dependencies: {score} - {justification}

## Viability (V = {score}/10)
- Unit Economics: {score} - {justification}
- Gross Margin: {score} - {justification}
- Payback Period: {score} - {justification}
- Operational Leverage: {score} - {justification}

## Competition (C = {score}/10)
- Five Forces: {score} - {justification}
- Barriers to Entry: {score} - {justification}
- Threat of Substitutes: {score} - {justification}
- Market Timing: {score} - {justification}

## Total Score: {total}/10
**Priority**: {Critical | High | Medium | Low | Reject}

## Decision: {Proceed | Further Analysis | Pivot | Reject}
**Next Steps**: {Action items based on decision}
```

---

## 11. Version History

- **v1.0** (2026-02-01): Initial rubric with 4 dimensions, 16 sub-criteria, 7 sphere weight tables, 3 worked examples
- **Future**: Add risk-adjusted scoring (confidence intervals), sensitivity analysis (what-if scenarios)

---

## 12. References & Related Frameworks

