# MCP Conflict Resolution Framework

## Overview

This guide provides structured methodology for resolving conflicts between outputs from parallel MCP (Model Context Protocol) server executions during EMBER Consilium evidence gathering phase.

## MCP Conflict Types & Resolution Strategies

### 1. Contradictory Claims (Direct Opposition)

**Definition:** Two or more MCPs make directly opposing factual claims

**Example:**
```
MCP-A (brave-search): "Option A is market leader, 45% share"
MCP-B (perplexity): "Option A market share declining, now 32%"
```

**Resolution Strategy:**
1. Identify source publication for each claim
   - Assess publication date (newer = more accurate typically)
   - Assess publisher credibility (tier 1, 2, 3)
   - Verify sample size if statistical claim
2. Compare publication quality
   - Peer-reviewed vs. industry report vs. news article
   - Methodological rigor (described or obscure?)
   - Source independence (unbiased or vendor-biased?)
3. Determine credibility winner
   ```
   IF newer_date AND higher_credibility → Accept newer
   IF same_date AND different_credibility → Accept higher credibility
   IF conflicting → Manual investigation required
   ```
4. Document losing claim as "alternative claim from source [X]"
5. Confidence penalty: -3% per unresolved contradiction

**Confidence Adjustment:**
```
Resolved contradiction (clear winner): -1%
Unresolved contradiction (both plausible): -5%
Multiple unresolved contradictions (3+): -15%
```

---

### 2. Temporal Divergence (Different Timeframes)

**Definition:** Same metric measured at different times, showing change

**Example:**
```
MCP-A (octocode 2024): "Option B had 5000 GitHub stars in 2023"
MCP-B (brave-search 2025): "Option B has 8000 GitHub stars now"
```

**Resolution Strategy:**
1. Establish timeline of measurements
   - Chronological ordering of data points
   - Identify if trend or snapshot
2. Assess rate of change
   - Is change expected or anomalous?
   - Is trend accelerating or slowing?
   - Any external events explaining change?
3. Use most recent data IF:
   - Both sources equally credible
   - Change is expected/explained
   - Trend is stable
4. Document trend IF:
   - Change is significant
   - Could affect decision
   - Impacts evaluation factors
5. No confidence penalty (temporal divergence is expected)

**Use Case:**
Use temporal data to assess momentum and trajectory rather than absolute values

---

### 3. Different Metrics (Incomparable Dimensions)

**Definition:** MCPs report on different dimensions rather than contradicting same dimension

**Example:**
```
MCP-A (brave-search): "Option A is popular (market penetration: 35%)"
MCP-B (octocode): "Option A has poor code documentation (GitHub rating: 2.3/5)"
MCP-C (perplexity): "Option A is most technically mature (maturity index: 8/10)"
```

**Resolution Strategy:**
1. Recognize as **complementary, not contradictory**
   - Both metrics can be true simultaneously
   - Different dimensions measure different things
2. Assess whether each metric is evaluation factor
   - Market adoption is one factor
   - Code quality is separate factor
   - Technical maturity is separate factor
3. Add as separate evaluation factors if missing
4. No conflict resolution needed (not contradictory)
5. No confidence penalty (different dimensions)

**Key Insight:**
Option can be market-leading (metric A) while having poor documentation (metric B). Both are true and both should inform decision.

---

### 4. Interpretation Divergence (Different Conclusions from Same Data)

**Definition:** MCPs cite same data but draw different conclusions

**Example:**
```
MCP-A (perplexity): "Option A's declining user growth indicates market saturation—
                    RECOMMENDATION: Avoid, market is mature"
MCP-B (sequentialthinking): "Option A's declining growth rate is normal for mature product—
                            RECOMMENDATION: Accept, stable market position"
```

**Resolution Strategy:**
1. Extract common underlying data
   - Identify what both agree on (usually the data)
   - Identify where conclusions diverge
2. Assess reasoning quality for each interpretation
   - Logic soundness (does it follow from data?)
   - Completeness (all relevant factors considered?)
   - Bias potential (is conclusion biased toward MCP specialty?)
3. Evaluate interpretation credibility
   - Which reasoning is more robust?
   - Which takes more factors into account?
   - Which is less biased?
4. Document both interpretations as "valid perspectives"
   - Don't eliminate either
   - Present as range of possible conclusions
   - Let human decision-maker choose
5. Confidence penalty: -2% per interpretation divergence (uncertainty)

**Key Insight:**
Same data can support multiple valid interpretations. Don't force false resolution; present range.

---

### 5. Credibility Divergence (Different Source Quality)

**Definition:** MCPs cite sources with significantly different credibility levels

**Example:**
```
MCP-A (brave-search): "McKinsey consulting report ranks Option A as top choice"
                      [Tier 1 source: peer-reviewed, large sample, institutional]

MCP-B (perplexity): "Reddit community consensus favors Option B"
                    [Tier 3 source: anecdotal, self-selected, unverified]
```

**Resolution Strategy:**
1. Assess credibility of each source
   - Apply explicit credibility scoring (see step-03c)
   - Rate on 1-5 scale with clear criteria
2. Weight MCP outputs by credibility
   ```
   Weighted_Output = MCP_Output × (MCP_Credibility_Score / 5)
   ```
3. Accept higher-credibility source for that dimension
4. Document lower-credibility source as "alternative view with lower credibility"
5. No confidence penalty if credibility difference clear (weighting resolves it)

**Confidence Adjustment:**
```
Minor credibility difference (2 point gap): -0% (weighting sufficient)
Major credibility difference (3+ point gap): -1% (uncertainty about which is right)
Equal credibility, different claims: -3% (genuine conflict)
```

---

## Weighted MCP Integration

When reconciliation complete, apply credibility-weighted integration:

```
Final_Evidence_Score = 
  (brave_search_finding × brave_credibility) +
  (perplexity_finding × perplexity_credibility) +
  (octocode_finding × octocode_credibility) +
  ... / sum(all_credibility_scores)
```

**Example:**
```
Claim about Option A's market maturity:

brave-search result: 4/5 rating (credibility 4.5/5) = 1.8
perplexity result: 4/5 rating (credibility 4.2/5) = 1.68
octocode result: 3/5 rating (credibility 3.8/5) = 1.14
sequentialthinking result: 4/5 rating (credibility 4.0/5) = 1.6

Weighted Average = (1.8 + 1.68 + 1.14 + 1.6) / (4.5 + 4.2 + 3.8 + 4.0)
                 = 6.22 / 16.5
                 = 3.77 / 5.0 (not simple average of 3.75)
```

---

## Unresolved Conflicts: When to Escalate

**Escalate conflict for manual investigation IF:**

1. **Contradictory claims where:**
   - Both sources equally credible
   - Publication dates close (within 30 days)
   - Claim impacts critical evaluation factor
   - Contradiction reverses recommendation direction

2. **Interpretation divergence where:**
   - Both reasoning chains valid
   - Leads to opposite recommendations
   - Confidence impact is >5%

3. **Multiple conflicts clustering around single factor:**
   - 3+ unresolved conflicts impact same evaluation dimension
   - Creates ambiguity about factor rating
   - Can't proceed with confidence

**Escalation Protocol:**
```
1. Document conflict in detail with evidence
2. Request decision-maker input: "Which interpretation aligns with your context?"
3. Conduct targeted additional research if time permits
4. If still unresolved: Reduce confidence by 10-15% for affected factor
5. Present both interpretations in matrix evaluation
6. Let stakeholder choose based on their preference
```

---

## MCP Conflict Tracking

**Document all conflicts in:**
```
{output_folder}/mcp-conflicts-{date}.md
```

**Template:**
```markdown
## MCP Conflict Log

### Conflict [number]
- **Type:** [Contradictory / Temporal / Different Metrics / Interpretation / Credibility]
- **MCPs Involved:** [MCP-A vs MCP-B]
- **Claim A:** [exact quote]
- **Claim B:** [exact quote]
- **Resolution:** [resolved / unresolved]
- **Method:** [which strategy applied]
- **Confidence Impact:** -[X]%
- **Status:** [Active in evaluation / Resolved]
```

---

## MCP Selection Tuning Based on Conflicts

If particular MCP consistently produces conflicting outputs:

1. **Reduce weight** of that MCP in future analyses
2. **Question credibility** of its sources
3. **Supplement with alternative** MCP in same domain
4. **Document pattern** for organizational learning
5. **Consider removing** from stack if consistently problematic

**Example:**
```
If brave-search regularly returns outdated data:
  → Reduce brave-search weight from 30% to 15%
  → Supplement with perplexity-mcp for recency validation
  → Note pattern for future MCP selection
```

---

## Summary: Conflict Resolution Decision Tree

```
MCP OUTPUT CONFLICT DETECTED
    ↓
Is it CONTRADICTORY CLAIM?
├─ YES → Compare source credibility & date → Accept higher/newer
└─ NO → Is it TEMPORAL DIVERGENCE?
        ├─ YES → Use most recent IF credible → No penalty
        └─ NO → Is it DIFFERENT METRICS?
                ├─ YES → Add as separate factors → No conflict
                └─ NO → Is it INTERPRETATION DIVERGENCE?
                        ├─ YES → Present both → Penalty -2%
                        └─ NO → Is it CREDIBILITY DIVERGENCE?
                                ├─ YES → Weight by credibility → No penalty
                                └─ NO → UNKNOWN TYPE → Escalate
