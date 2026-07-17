# MCDA Delta Analysis: Score Changes & Impacts

**Analysis Date:** 2026-02-06
**Threshold:** Flagging changes >0.5 points

---

## 📊 CHANGE SUMMARY

| Idea | Previous | NEW | Delta | Flag | Impact |
|------|----------|-----|-------|------|--------|
| 001-Katana | 10.0 | 10.0 | 0 | — | ✅ Stable |
| 002-Maps Bot | 5.5 | 5.5 | 0 | — | ✅ Stable |
| 003-VK Recipes | 8.0 | 8.0 | 0 | — | ✅ Stable |
| 004-VK Bot | 5.5 | 5.5 | 0 | — | ✅ Stable |
| 005-Sales QA | 8.5 | 8.5 | 0 | — | ✅ Stable |
| **006-Consilium** | 7.0 | 5.0 | **-2.0** | 🚩 **MAJOR** | ❌ Downgrade |
| **007-DepylBrazil** | 7.5 | 6.5 | **-1.0** | 🚩 **MODERATE** | ⚠️ Conditional |

---

## 🚩 FLAGGED CHANGES (>0.5 points)

### 1️⃣ CONSILIUM SaaS: -2.0 POINT DROP (7.0 → 5.0)
**Severity:** 🔴 MAJOR CHANGE

#### What Changed?

| Criterion | Old | New | Change | Reason |
|-----------|-----|-----|--------|--------|
| **Impact** | 4 | 3 | -1 | Market crowded, PMF unproven (Notion, Asana, ChatGPT all offer similar) |
| **Confidence** | 3 | 2 | -1 | Consumer SaaS execution risk high, team scaling needed |
| **Effort** | 1 | 1 | 0 | Unchanged (400-800 hrs = HIGH) |
| **Alignment** | 4 | 3 | -1 | Distraction risk from Katana/Sales QA, WIP condition conflict |
| **Risk** | 2 | 1 | -1 | PMF unproven (consumer SaaS 90% failure rate), churn risk high |

#### Root Cause Analysis

**Primary drivers:**
1. **Consumer SaaS market reality:** 90% of consumer SaaS fail. PMF validation = critical, not optional.
2. **Risk underestimation:** Initial scoring gave too much credit to "Life OS IP productization" without validating demand.
3. **Confidence gap:** Team scaling (hiring/outsourcing) not yet resolved; solo execution risky for consumer market.
4. **Competitive landscape:** ChatGPT + Notion + Asana + dedicated coaching tools = crowded space. Differentiation unclear.

#### Scoring Recalculation

**OLD:** (4 + 3 + 1 + 4 + 2) / 5 × 2.5 = 14/5 × 2.5 = 2.8 × 2.5 = **7.0/10**

**NEW:** (3 + 2 + 1 + 3 + 1) / 5 × 2.5 = 10/5 × 2.5 = 2.0 × 2.5 = **5.0/10**

#### Impact on Roadmap

| Before | After |
|--------|-------|
| Recommendation: PROCEED (with conditions) | Recommendation: **DEFER** (Q3+) |
| Timeline: MVP 12w, Beta 4w, Launch 2w = 18w | Timeline: Validate PMF 4w first (experimental) |
| Status: PLANNED | Status: **EXPERIMENTAL** |
| Risk threshold: Moderate | Risk threshold: **HIGH until PMF proven** |

#### New Conditional Path

```
GATE 1: 4-Week PMF Validation Sprint (Start immediately)
├─ Hypothesis: "2-mode Consilium MVP can achieve >40% Week 1 retention"
├─ Budget: $2-5k (API costs, basic infrastructure)
├─ Test group: 20-50 beta users (friends, colleagues, existing Life OS users)
├─ Success metric: >40% Week 1 retention OR >70% NPS
├─ Failure metric: <30% retention, negative feedback on UX
└─ Decision: If FAIL → STOP, PIVOT or DEFER. If PASS → Proceed to full MVP.

GATE 2: Full MVP Only If GATE 1 Passes
├─ Timeline: 12 weeks (Mar-May)
├─ Budget: $50k+ (team, infrastructure, API costs)
└─ Target: 500+ beta users, LTV:CAC >2:1
```

---

### 2️⃣ DEPYLBRAZIL FRANCHISE: -1.0 POINT DROP (7.5 → 6.5)
**Severity:** 🟡 MODERATE CHANGE

#### What Changed?

| Criterion | Old | New | Change | Reason |
|-----------|-----|-----|--------|--------|
| **Impact** | 4 | 4 | 0 | Unchanged (scaling potential, recurring revenue) |
| **Confidence** | 4 | 3 | -1 | Nikita commitment pending (72-hour decision window, Feb 5-7) |
| **Effort** | 2 | 2 | 0 | Unchanged (130-205 hrs over 30 days) |
| **Alignment** | 3 | 2 | -1 | Operational burden on Galina high, limited Nikita involvement |
| **Risk** | 2 | 2 | 0 | Unchanged (moderate mitigations: NDA, pilots, SMART discipline) |

#### Root Cause Analysis

**Primary drivers:**
1. **Commitment uncertainty:** Nikita's decision = Feb 7 deadline (72-hour discovery window). Not yet committed.
2. **Operational risk:** Franchise model = ongoing support (CRM, training, troubleshooting). Galina = critical bottleneck.
3. **Alignment gap:** Nikita's stated goals (Katana, Sales QA) don't include "franchise founder." This is Galina's passion.

#### Scoring Recalculation

**OLD:** (4 + 4 + 2 + 3 + 2) / 5 × 2.5 = 15/5 × 2.5 = 3.0 × 2.5 = **7.5/10**

**NEW:** (4 + 3 + 2 + 2 + 2) / 5 × 2.5 = 13/5 × 2.5 = 2.6 × 2.5 = **6.5/10**

#### Impact on Roadmap

| Before | After |
|--------|-------|
| Status: ACTIVE (15% complete) | Status: **CONDITIONAL** |
| Next step: Step 04 (Consilium) | Next step: **DECISION GATE (Feb 7)** |
| Assumption: Nikita committed | Assumption: **PENDING** |
| Risk level: Moderate | Risk level: **CONDITIONAL** |

#### Conditional Path

```
DECISION GATE: Feb 7, 2026 (Nikita 72-hour discovery)

IF NIKITA COMMITS ("Yes, let's do this"):
├─ Trigger: ✅ Full 30-day sprint (Feb 7 - Mar 7)
├─ Team: Galina (lead), Violta (Sochi location), Maria (Vladimir location)
├─ Budget: Fixed + KPI bonus (terms TBD)
├─ Output: Franchise v1 (product, CRM, docs, training, 2 pilot locations)
├─ Score: 6.5/10 → proceed (operational risk managed by clear goals)
└─ Next: 30-day execution, daily standups

IF NIKITA DECLINES ("Not now, too much on my plate"):
├─ Trigger: ❌ Archive for future (Q3 or later)
├─ Team: Galina can self-fund/lead with advisors
├─ Output: Continue 2-location operation, plan franchise later
├─ Score: 6.5/10 → defer (not abandoned, just delayed)
└─ Next: Formal handoff, archive case study

IF NIKITA HESITATES ("Maybe, let me think"):
├─ Trigger: ⏸️ 72-hour extension (Feb 10 deadline)
├─ Action: Deep dive on specific concerns (financial model, time, risk)
├─ Score: 6.5/10 → decision still pending
└─ Next: Feb 10 final call
```

---

## 📈 STABILITY ANALYSIS (Unchanged Scores)

| Idea | Score | Reason for Stability |
|------|-------|----------------------|
| **Katana** | 10.0 | All criteria strong, minimal uncertainty |
| **Sales QA** | 8.5 | Technology proven, market validated, integration work = normal execution |
| **VK Recipes** | 8.0 | Existing asset, monetization = standard playbook, risk mitigated |
| **Maps Bot** | 5.5 | Consistently weak across criteria, no new info to change scoring |
| **VK Bot** | 5.5 | High effort + moderate market + platform risk = stable low score |

---

## 🎯 PORTFOLIO IMPACT SUMMARY

### Tier Shifts

```
BEFORE Re-scoring:
├─ Tier 1 (Execute): Katana (10.0), Sales QA (8.5)
├─ Tier 2 (Secondary): Recipes (8.0), Consilium (7.0), DepylBrazil (7.5)
└─ Tier 3 (Backlog): Maps (5.5), VK Bot (5.5)

AFTER Re-scoring:
├─ Tier 1 (Execute): Katana (10.0), Sales QA (8.5)
├─ Tier 2 (Secondary): Recipes (8.0), DepylBrazil (6.5 conditional)
└─ Tier 3 (Backlog): Consilium (5.0 ← MOVED), Maps (5.5), VK Bot (5.5)
```

### Strategic Implications

1. **Katana remains anchor** (10.0) — no change, execution continues
2. **Sales QA confirmed as Tier 1** (8.5) — proceed with MVP scope, Apr start
3. **Consilium drops out of near-term** (7.0 → 5.0) — major shift, affects planning
4. **DepylBrazil conditional** (7.5 → 6.5) — Feb 7 decision gate, not dead but uncertain
5. **Secondary tier stable** (Recipes 8.0) — can run parallel, low commitment

### Execution Readiness

| Project | Readiness | Timeline | Notes |
|---------|-----------|----------|-------|
| Katana | ✅ HIGH | Feb-May | Clear path, no gates |
| Sales QA | ✅ HIGH | Apr-Jul | Scope review needed (Feb 10), then proceed |
| Recipes | ✅ MEDIUM | Feb+ | Can start anytime, low effort |
| DepylBrazil | ⚠️ CONDITIONAL | Feb-Mar | Decision gate Feb 7, then 30-day sprint |
| Consilium | ❌ BLOCKED | Q3+ | Requires 4-week PMF validation gate first |
| Maps Bot | ❌ LOW | Q3/Q4 | Keep warm, no resource allocation |
| VK Bot | ❌ LOW | Q3/Q4 | Keep warm, market validation needed first |

---

## 📋 DELTA CHANGE DOCUMENTATION

### Change Type: Recalibration (not new insight, re-evaluation of existing data)

**What triggered re-scoring?**
- Comprehensive MCDA analysis across all 7 ideas
- Cross-validation with Life OS goals and timeline constraints
- Consumer SaaS market risk review (Consilium specific)
- Nikita's commitment status check (DepylBrazil specific)

**Data sources:**
- Idea briefs (all 7 files)
- Life OS workflow outputs (006-Consilium, 007-DepylBrazil)
- Strategic context (2026 goals, portfolio balance, resource constraints)

**Confidence level:**
- Katana (95%): Data-driven, phases 3-4 complete, Epic L in progress
- Sales QA (85%): Market validated, but MVP scope TBD
- Consilium (60%): Consumer SaaS inherently risky, PMF unproven, estimate-based
- DepylBrazil (70%): SMART goals clear, but Nikita commitment = wild card

---

## 🔔 ACTION ITEMS FROM DELTA ANALYSIS

### Immediate (This week)

- [ ] **Feb 7:** Nikita makes DepylBrazil commitment decision
- [ ] **Feb 10:** Sales QA MVP scope finalized (integrations, languages, use cases)
- [ ] **Feb 10:** Consilium PMF validation sprint parameters confirmed (budget, test group size, metrics)

### Short-term (Next 2 weeks)

- [ ] If DepylBrazil = YES: Kick off 30-day sprint (team standups, daily progress)
- [ ] If Consilium proceeds to validation: Launch 4-week PMF experiment (beta signup, tracking)
- [ ] Sales QA: Team assignment, technical spike on Whisper/Zadarma/Mango APIs

### Medium-term (Next month)

- [ ] Katana: Complete Epic L, begin Paper Trading phase
- [ ] Recipes: Launch monetization strategy (ads + partnerships)
- [ ] Consilium: Evaluate PMF results (Gate 1 pass/fail decision)

---

## 📊 SCORING TRANSPARENCY

**Methodology:**
- 5 criteria (IMPACT, CONFIDENCE, EFFORT, ALIGNMENT, RISK)
- 1-5 scale per criterion
- EFFORT and RISK criteria INVERTED (low effort/low risk = high score)
- Formula: (I+C+E+A+R)/5 × 2.5 = Score/10
- Capped at 10.0

**Limitations:**
- Scores are estimates (no hard data on market size, unit economics for most ideas)
- Confidence in Consilium/DepylBrazil lower due to commitment/market uncertainties
- External factors (market shifts, team changes, funding) not modeled

**Updating scores:**
- Quarterly review recommended (after each quarter's learnings)
- Major project milestones should trigger score updates
- External events (market shifts, competitor moves) warrant immediate review

---

## 🎯 CONCLUSION

**Two major score changes identified:**
1. **Consilium SaaS (-2.0):** Downgrade from 7.0 to 5.0 — defer to Q3, validate PMF first
2. **DepylBrazil (-1.0):** Conditional from 7.5 to 6.5 — decision gate Feb 7

**All other scores stable,** confirming initial Tier 1/2/3 classification.

**Portfolio consequence:** Clearer execution path (Katana + Sales QA primary), fewer competing initiatives, explicit validation gates for high-risk ideas.

---

**Generated:** 2026-02-06
**Next Review:** After Feb 7 DepylBrazil decision and Feb 10 Sales QA scope finalization
