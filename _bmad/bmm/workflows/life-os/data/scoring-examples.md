# Scoring Examples - WRONG vs RIGHT

## Overview

This document shows examples of **low-quality** vs **high-quality** scoring to help you understand what makes a good scoring rationale.

---

## Example 1: Impact Criterion

### ❌ WRONG (Low Quality)

**Score:** 4/5

**Rationale:** "This will have a big impact on users."

**Problems:**
- No quantification
- No evidence
- No ceiling explanation ("Why not 5?")
- Vague language ("big impact")

---

### ✅ RIGHT (High Quality)

**Score:** 4/5

**Rationale:**
"This feature will save users an average of 15 minutes per day (based on 3 user interviews and time-tracking data). Extrapolated to 1,000 active users, this equals 250 hours/day or ~$12,500/month in productivity gains (assuming $50/hour average value).

**Why not 5/5?** Impact is limited to power users (40% of user base). Casual users (60%) gain only 2-3 minutes/day. To reach 5/5, we'd need to redesign the onboarding flow to make this feature accessible to all users (scope expansion not planned)."

**Why This Works:**
- ✅ Quantified metrics (15 min/day, 1,000 users, $12,500/month)
- ✅ Evidence cited (user interviews, time-tracking data)
- ✅ Ceiling explained (limited to power users)
- ✅ Specific and actionable

---

## Example 2: Confidence Criterion

### ❌ WRONG (Low Quality)

**Score:** 3/5

**Rationale:** "We're somewhat confident but there are risks."

**Problems:**
- No specific risks identified
- No validation evidence
- No mitigation plan
- Unclear what drives the score

---

### ✅ RIGHT (High Quality)

**Score:** 3/5

**Rationale:**
"Team has successfully delivered 2 similar projects in the past 6 months (authentication system, payment gateway), so core technical approach is proven.

**Uncertainty factors:**
1. **API integration** with third-party vendor (no prior experience) - mitigated by 2-week prototype sprint
2. **Data migration** from legacy system (unknown data quality) - risk assessment in progress
3. **Regulatory compliance** (GDPR) - legal review scheduled

**Why not 5/5?** Until prototype validates API integration and data migration risks are quantified, we retain medium uncertainty. Confidence will increase to 4/5 after prototype completion (Week 3)."

**Why This Works:**
- ✅ Past project evidence cited
- ✅ Specific risks identified (3 factors)
- ✅ Mitigation strategies outlined
- ✅ Clear path to higher confidence

---

## Example 3: Effort Criterion

### ❌ WRONG (Low Quality)

**Score:** 4/5 (high effort)

**Rationale:** "This will take a lot of time and resources."

**Problems:**
- No sizing estimate (hours, weeks, FTEs)
- No breakdown of work
- No comparison to similar projects
- Unclear what drives the effort

---

### ✅ RIGHT (High Quality)

**Score:** 4/5 (high effort)

**Rationale:**
"**T-shirt sizing:** XL (estimated 12-16 weeks, 3 FTEs)

**Breakdown:**
- Backend development: 6 weeks (2 engineers)
- Frontend implementation: 4 weeks (1 engineer)
- Data migration: 3 weeks (1 engineer + DBA support)
- Testing & QA: 3 weeks (parallel with dev)
- Integration & deployment: 2 weeks (all hands)

**Dependencies:**
- Requires legal review completion (external blocker, 2-week delay risk)
- Needs database schema approval (internal, low risk)

**Comparison:** Similar projects (auth system, payment gateway) took 8-10 weeks with 2 FTEs. This is 50% larger due to data migration complexity.

**Why not 5/5?** We're reusing 30% of code from previous projects (authentication module, API framework), which reduces effort from what would otherwise be 18-20 weeks."

**Why This Works:**
- ✅ Specific sizing (12-16 weeks, 3 FTEs)
- ✅ Detailed breakdown by workstream
- ✅ Dependencies identified
- ✅ Comparison to similar projects
- ✅ Effort reduction explained

---

## Example 4: Strategic Alignment Criterion

### ❌ WRONG (Low Quality)

**Score:** 5/5

**Rationale:** "Aligns perfectly with our strategy."

**Problems:**
- No reference to specific goals
- No theory of change
- No metrics linkage
- Generic language

---

### ✅ RIGHT (High Quality)

**Score:** 5/5

**Rationale:**
"**Goal Mapping (from goals.yaml):**
- **Primary:** Increase user retention from 60% to 75% by Q4 (Goal 1.2)
- **Secondary:** Reduce customer support tickets by 30% (Goal 2.1)

**Theory of Change:**
This feature addresses the #1 user complaint (slow task completion) identified in Q1 user research. By reducing friction in core workflow, we expect:
1. Daily active usage to increase 20-25% (retention proxy metric)
2. Support tickets re: "how to do X" to drop 40% (support reduction)

**Success Metrics:**
- Retention rate (tracked weekly in analytics)
- Task completion time (A/B test with control group)
- Support ticket volume (Zendesk dashboard)

**Why 5/5?** This is a direct, high-leverage intervention on our top priority goal (retention). No other initiative this quarter has a stronger goal linkage."

**Why This Works:**
- ✅ Explicit mapping to goals.yaml
- ✅ Theory of change explained
- ✅ Metrics linked to goal KPIs
- ✅ Clear reasoning for perfect score

---

## Example 5: Risk Criterion

### ❌ WRONG (Low Quality)

**Score:** 2/5 (low risk)

**Rationale:** "There are some risks but nothing major."

**Problems:**
- No specific risks identified
- No risk register
- No mitigation plan
- No blast radius assessment

---

### ✅ RIGHT (High Quality)

**Score:** 2/5 (low risk)

**Rationale:**
"**Risk Register (Top 3):**

1. **Technical:** API rate limits from vendor (P=30%, I=Medium)
   - **Mitigation:** Caching layer + fallback to async processing
   - **Blast radius:** Max 10% of requests delayed by 5 minutes

2. **Operational:** Team member on leave during critical phase (P=20%, I=Low)
   - **Mitigation:** Cross-training completed, documentation in place
   - **Blast radius:** 1-week delay in worst case

3. **Market:** Competitor launches similar feature (P=40%, I=Low)
   - **Mitigation:** Our differentiation is integration depth, not feature parity
   - **Blast radius:** Minimal impact on adoption

**Why 2/5 (low risk)?** All risks have mitigation plans in place, and blast radius is contained. No "bet-the-company" downside.

**Why not 1/5?** API rate limit risk is real and could degrade UX temporarily. Once caching is proven in production (Week 4), risk drops to 1/5."

**Why This Works:**
- ✅ Specific risks identified (3 top risks)
- ✅ Probability + impact assessed
- ✅ Mitigation strategies outlined
- ✅ Blast radius quantified
- ✅ Clear reasoning for score

---

## Example 6: Complete Scoring Summary

### ❌ WRONG (Low Quality)

```markdown
## Scoring Summary

**Criteria Scores (1–5):**
- Impact: 4 — Big impact
- Confidence: 3 — Some uncertainty
- Effort: 4 — Lots of work
- Strategic Alignment: 5 — Good fit
- Risk: 2 — Low risk

**Overall Score:** 7.2/10
```

**Problems:**
- No evidence
- No rationale depth
- No weighted calculation shown
- No sensitivity analysis
- ~50 words (target: 600-800)

---

### ✅ RIGHT (High Quality)

```markdown
## Scoring Summary

**Criteria Scores (1–5):**

**Impact: 4/5** — Saves users avg 15 min/day (based on 3 interviews + time-tracking). Extrapolated to 1,000 users = $12,500/month productivity gain. Why not 5? Limited to power users (40% of base). Casual users gain only 2-3 min/day.

**Confidence: 3/5** — Team delivered 2 similar projects (auth, payments) successfully. Uncertainties: (1) API integration with vendor (no prior exp), (2) data migration quality unknown, (3) GDPR compliance pending legal review. Prototype sprint (Week 2-3) will validate API risk. Why not 5? Until prototype succeeds, retain medium uncertainty.

**Effort: 4/5** — T-shirt: XL (12-16 weeks, 3 FTEs). Breakdown: Backend (6w, 2eng), Frontend (4w, 1eng), Data migration (3w), Testing (3w parallel), Deployment (2w). Dependencies: legal review (2w delay risk). Comparison: similar projects took 8-10w/2FTE; this is +50% due to migration. Why not 5? Reusing 30% of code (auth module, API framework) reduces from 18-20w baseline.

**Strategic Alignment: 5/5** — Directly targets Goal 1.2 (increase retention 60%→75% by Q4) and Goal 2.1 (reduce support tickets -30%). Addresses #1 user complaint (slow tasks). Theory of change: reduce friction → +20-25% daily usage → retention boost. Metrics: retention rate (weekly), task time (A/B test), support tickets (Zendesk). Why 5? No other initiative has stronger goal linkage this quarter.

**Risk: 2/5** — Risk register: (1) API rate limits (P=30%, I=Med, mitigation: caching + async fallback, blast radius: 10% requests delayed 5min), (2) Team leave (P=20%, I=Low, mitigation: cross-training done, blast radius: 1w delay), (3) Competitor launch (P=40%, I=Low, mitigation: our differentiation is depth not parity). Why 2? All risks mitigated, no "bet-company" downside. Why not 1? API risk real until caching proven in prod (Week 4).

**Overall Score:** 7.2/10 (weighted MCDA)

**Weighted Calculation:**
```
Impact:      4.0 * 0.25 =  1.00
Confidence:  3.0 * 0.15 =  0.45
Effort:      4.0 * -0.20 = -0.80
Strategic:   5.0 * 0.25 =  1.25
Risk:        2.0 * -0.15 = -0.30
                Total =  1.60 → Normalized to 7.2/10
```

**Sensitivity Analysis:**
- If prototype succeeds (Confidence → 4): Score = 7.5/10
- If reuse increases to 50% (Effort → 3): Score = 7.8/10
- If impact extends to casual users (Impact → 5): Score = 8.2/10

**Decision Rationale:**
- **Proceed** - Strong strategic fit (5/5 alignment) justifies high effort
- **Mitigate** - Validate API integration in prototype (Week 2-3)
- **Optimize** - Explore ways to extend impact to casual users (future iteration)
```

**Why This Works:**
- ✅ Every score justified with reasoning
- ✅ Evidence provided (data, interviews, past projects)
- ✅ "Why not higher?" explained for each
- ✅ Weighted calculation shown
- ✅ Sensitivity analysis included
- ✅ Clear decision with rationale
- ✅ ~650 words (meets 600-800 target)

---

## Summary: Quality Checklist

When reviewing your scoring output, verify:

- ☐ Every score justified with reasoning (not just numbers)
- ☐ Evidence provided (data, competitor analysis, interviews)
- ☐ "Why not higher?" ceiling explained for each criterion
- ☐ Weighted calculation shown (MCDA)
- ☐ Sensitivity analysis included (what-if scenarios)
- ☐ Clear decision with rationale
- ☐ 600-800 words total output

**Reference this document during Step 5 Quality Self-Validation checkpoint.**
