# Comparative Scoring Examples

**Purpose:** Demonstrate how comparative ranking prevents scoring inflation and forces meaningful differentiation.

---

## Example 1: Business Ideas (3 Ideas)

### Problem: Absolute Scoring Inflation

**Absolute mode results:**
- **Idea A: Launch SaaS Product**
  - Impact: 4.0, Confidence: 3.5, Effort: 4.0, Strategic: 4.0, Risk: 3.5
  - **Overall: 3.8**
- **Idea B: Optimize Sales Process**
  - Impact: 3.5, Confidence: 4.0, Effort: 3.5, Strategic: 3.5, Risk: 4.0
  - **Overall: 3.7**
- **Idea C: Content Marketing Campaign**
  - Impact: 3.8, Confidence: 3.8, Effort: 3.5, Strategic: 4.0, Risk: 3.8
  - **Overall: 3.8**

**Problem:** All ideas scored 3.7-3.8. No clear winner. User can't prioritize.

### Solution: Comparative Ranking

**Step 1: Comparative questions**

**Impact Magnitude - Which has bigger potential impact?**
- Launch SaaS: Could generate $1M+ revenue
- Optimize Sales: 20% efficiency gain
- Content Marketing: Increase leads by 30%

**User choice:** [A] Launch SaaS (transformative vs incremental)

**Strategic Fit - Which aligns better with long-term direction?**
- Launch SaaS: Core business model
- Optimize Sales: Supports existing business
- Content Marketing: Lead generation tactic

**User choice:** [A] Launch SaaS (builds competitive moat)

**Execution Confidence - Which are you more confident executing?**
- Launch SaaS: Many unknowns, complex
- Optimize Sales: Clear process, proven methods
- Content Marketing: Team has experience

**User choice:** [B] Optimize Sales (lower risk, known path)

**Time-to-Value - Which delivers value faster?**
- Launch SaaS: 6-12 months to revenue
- Optimize Sales: Results in 1-2 months
- Content Marketing: Leads in 2-3 months

**User choice:** [B] Optimize Sales (fastest ROI)

**Resource Efficiency - Which uses resources more efficiently?**
- Launch SaaS: $50K investment, 6 months
- Optimize Sales: $5K, 2 months
- Content Marketing: $15K, 3 months

**User choice:** [B] Optimize Sales (10x better ROI)

**Risk Level - Which has lower risk?**
- Launch SaaS: High failure risk, big investment
- Optimize Sales: Low risk, reversible
- Content Marketing: Medium risk, moderate cost

**User choice:** [B] Optimize Sales (safest bet)

**Step 2: Aggregate rankings**

| Idea | Wins | Rank | Normalized Score |
|------|------|------|------------------|
| Launch SaaS | 2/6 | 2nd | **4.5** |
| Optimize Sales | 4/6 | **1st** | **5.0** |
| Content Marketing | 0/6 | 3rd | **4.0** |

**Step 3: Forced differentiation achieved**

✅ Clear priority: Optimize Sales (5.0) > Launch SaaS (4.5) > Content Marketing (4.0)

✅ Differentiation: Δ(1-2) = 0.5, Δ(2-3) = 0.5

✅ User insight: "We should do Sales optimization NOW (quick win), then invest in SaaS (long-term), and use content marketing to support both."

---

## Example 2: Personal Goals (5 Ideas)

### Problem: Grade Inflation

**Absolute mode results:**
1. Learn Python: 4.0
2. Improve Fitness: 3.8
3. Read 20 Books: 3.9
4. Side Project: 3.7
5. Learn Guitar: 3.6

**Problem:** All scores 3.6-4.0 (0.4 range). Difficult to prioritize.

### Solution: Comparative Ranking with Forced Choice

**Initial comparative ranking:**
- Python: 4.2
- Fitness: 4.1
- Books: 3.9
- Side Project: 3.8
- Guitar: 3.6

**Forced tiebreaker triggered (Python vs Fitness within 0.3):**

```
⚠️ Scores are very close:
- Learn Python: 4.2
- Improve Fitness: 4.1

Which is more important to you RIGHT NOW?
[A] Learn Python (rank higher)
[B] Improve Fitness (rank higher)
[T]ie is OK (keep close scores)
```

**User choice:** [B] Improve Fitness

**Reason:** "Health is foundation. Without energy, can't learn Python effectively."

**Final ranking:**

| Rank | Goal | Score | Reason |
|------|------|-------|--------|
| 1st | Improve Fitness | 5.0 | Foundation for everything else |
| 2nd | Learn Python | 4.5 | Career critical, high ROI |
| 3rd | Read 20 Books | 4.0 | Knowledge building, supports goals |
| 4th | Side Project | 3.5 | Fun but lower priority |
| 5th | Learn Guitar | 3.0 | Nice to have, can defer |

**Result:**
✅ Clear focus: Fitness FIRST, then Python, then Books
✅ User commitment: "I'll start gym tomorrow (Fitness), code 30min/day (Python), read before bed (Books). Side project and guitar are on hold."

---

## Example 3: Portfolio Intake (7 Ideas from Batch Mode)

### Problem: Portfolio Overload

User completed step-00.1 (portfolio intake) with 7 ideas:

1. Redesign website
2. Launch newsletter
3. Build mobile app
4. Improve customer support
5. Expand to new market
6. Hire 2 developers
7. Automate reporting

**All scored 3.5-4.2 in batch-quick-score.**

### Solution: Comparative Matrix

**Step 1: Batch comparison matrix**

| Idea | Impact | Strategic | Execution | Time | Resources | Risk | Total |
|------|--------|-----------|-----------|------|-----------|------|-------|
| Website | 3 | 4 | 5 | 4 | 4 | 5 | 25 |
| Newsletter | 4 | 3 | 5 | 5 | 5 | 5 | 27 |
| Mobile App | 5 | 5 | 2 | 1 | 1 | 2 | 16 |
| Support | 4 | 4 | 4 | 4 | 4 | 4 | 24 |
| New Market | 5 | 5 | 3 | 2 | 2 | 2 | 19 |
| Hire Devs | 3 | 4 | 3 | 3 | 2 | 4 | 19 |
| Automate | 3 | 3 | 5 | 5 | 5 | 5 | 26 |

**Step 2: Sort by total score**

| Rank | Idea | Score | Normalized |
|------|------|-------|------------|
| 1st | Newsletter | 27 | 5.0 |
| 2nd | Automate | 26 | 4.5 |
| 3rd | Website | 25 | 4.0 |
| 4th | Support | 24 | 3.5 |
| 5th | New Market | 19 | 3.0 |
| 6th | Hire Devs | 19 | 3.0 |
| 7th | Mobile App | 16 | 2.5 |

**Step 3: Forced differentiation (New Market vs Hire Devs tied at 19)**

```
⚠️ Multiple ideas scored identically:
- Expand to New Market: 19
- Hire 2 Developers: 19

Which enables more progress RIGHT NOW?
[M] New Market (rank higher)
[D] Hire Devs (rank higher)
```

**User choice:** [D] Hire Devs

**Reason:** "Need team capacity before expansion. Devs enable Newsletter, Website, and Automation."

**Final ranking adjusted:**

| Rank | Idea | Score | Action |
|------|------|-------|--------|
| 1st | Newsletter | 5.0 | START Q1 |
| 2nd | Automate | 4.5 | START Q1 |
| 3rd | Website | 4.0 | START Q2 |
| 4th | Support | 3.5 | START Q2 |
| 5th | Hire Devs | 3.0 | START Q3 (after budget) |
| 6th | New Market | 2.5 | DEFER to Q4 |
| 7th | Mobile App | 2.0 | DEFER (requires team + market) |

**Result:**
✅ Clear roadmap: Q1 (Newsletter + Automation), Q2 (Website + Support), Q3 (Hiring), Q4 (Market expansion)
✅ Portfolio balance: 30% high priority (5.0-4.0), 40% medium (3.5-3.0), 30% deferred (2.5-2.0)

---

## Key Insights from Examples

### 1. Comparative Ranking Prevents Inflation
- **Before:** All ideas 3.5-4.0 (no differentiation)
- **After:** Clear spread 2.0-5.0 (actionable priorities)

### 2. Forced Choice Creates Clarity
- When scores too close, user must articulate WHY one idea is better
- Reveals true priorities and trade-offs

### 3. Batch Mode Scales to Portfolios
- Can handle 7+ ideas simultaneously
- Matrix view shows patterns (e.g., "quick wins" cluster)
- Enables portfolio-level decisions (Q1 vs Q2 vs defer)

### 4. Ranking Reasons Drive Action
- "Fitness is foundation" → Clear commitment to start gym
- "Devs enable other projects" → Sequence dependencies
- "Mobile app requires team + market" → Logical deferral

### 5. Distribution Rules Enforce Balance
- No more than 30% in "Critical Priority" bucket
- Forces prioritization: Can't make everything urgent
- Realistic capacity planning

---

## When to Use Each Mode

| Mode | Use When | Benefit | Example |
|------|----------|---------|---------|
| **Absolute** | Single idea, or very different ideas | Independent scoring | Evaluate one new business idea |
| **Comparative** | 2-3 similar ideas need prioritization | Forces differentiation | Choose between Python, Fitness, Books |
| **Batch** | 4+ ideas from portfolio intake | Side-by-side comparison | Quarterly planning with 7 initiatives |

---

## Anti-Patterns to Avoid

### ❌ Bad: Absolute scoring with grade inflation
```
Idea A: 3.8
Idea B: 3.7
Idea C: 3.8
→ Can't tell which to do first
```

### ✅ Good: Comparative ranking with clear winner
```
Rank 1: Idea B (5.0) - Do this first
Rank 2: Idea A (4.5) - Do this second
Rank 3: Idea C (4.0) - Do this third
→ Clear action plan
```

### ❌ Bad: Accepting tied scores without forced choice
```
Idea A: 4.1
Idea B: 4.1
→ User skips differentiation
```

### ✅ Good: Forcing tiebreaker
```
Idea A: 4.1
Idea B: 4.1
⚠️ Which is more important RIGHT NOW?
→ User commits to A (4.5) > B (4.0)
```

### ❌ Bad: Overloading high priority bucket
```
7 ideas, all scored 4.5-5.0
→ Can't do 7 things at once
```

### ✅ Good: Distribution enforcement
```
⚠️ More than 30% of ideas in "Critical" bucket.
Please redistribute: Keep top 2 at 5.0, move others to 4.0-3.0
→ Realistic priorities
```

---

## Integration with Portfolio Intake (Step 00.1)

**Automatic workflow:**

1. User completes step-00.1 with 5 ideas
2. Batch-quick-score gives initial estimates (3.5-4.2)
3. Step-05 automatically triggers **Comparative Mode**
4. User refines rankings with forced choices
5. System assigns normalized scores
6. Ideas flow to step-06 (integration) with clear priorities

**Result:** Portfolio intake → Comparative scoring → Prioritized backlog (in one session)

---

## Success Criteria

✅ **Scoring differentiation achieved:**
- No more "all 3.5-4.0" results
- Clear gaps between ranks (0.5+ points)
- Forced distribution across priority buckets

✅ **User clarity improved:**
- User can articulate why Idea A > Idea B
- Clear action plan (what to do first, second, third)
- Confidence in priorities

✅ **Portfolio balance maintained:**
- 30% critical, 40% high, 30% medium/deferred
- Realistic capacity allocation
- Roadmap sequencing based on dependencies

---

**See also:**
- `comparative-scoring-criteria.yaml` - Full methodology and configuration
- `step-05-scoring.md` - Implementation in workflow
- `batch-quick-score.md` - Integration with portfolio intake
