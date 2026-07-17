# PORTFOLIO DEPENDENCIES & TIMELINE MAP

**Analysis Date:** February 6, 2026
**Visual Format:** ASCII Timeline + Dependency Matrix + Gantt Chart

---

## 🗺️ DEPENDENCY MATRIX (Who Blocks Whom?)

```
┌────────┬───────┬────────┬────────┬────────┬────────┬────────┐
│ Idea # │ 001   │ 002    │ 003    │ 004    │ 005    │ 006    │ 007
├────────┼───────┼────────┼────────┼────────┼────────┼────────┼────────┐
│ 001    │ NONE  │ none   │ none   │ none   │ none   │ WEAK   │ none  │
│ 002    │ none  │ NONE   │ none   │ none   │ none   │ none   │ none  │
│ 003    │ none  │ none   │ NONE   │ WEAK   │ none   │ none   │ none  │
│ 004    │ none  │ none   │ WEAK   │ NONE   │ none   │ none   │ none  │
│ 005    │ none  │ none   │ none   │ none   │ NONE   │ none   │ none  │
│ 006    │ WEAK  │ none   │ none   │ none   │ none   │ NONE   │ BLOCK*│
│ 007    │ none  │ none   │ none   │ none   │ none   │ BLOCKS │ NONE  │
└────────┴───────┴────────┴────────┴────────┴────────┴────────┴────────┘

Legend:
NONE  = No dependency
WEAK  = Optional synergy (nice-to-have, not blocking)
BLOCKS= Hard blocker (cannot start until predecessor done)
BLOCK*= WIP conflict, not true blocker (can defer until Mar 7)
```

### Detailed Dependency Explanations

**Idea 006 (Consilium) ← Idea 007 (Franchise):**
- **Type:** WIP conflict (not true dependency)
- **Issue:** Both want to consume 20-30h/week capacity
- **Current WIP:** 3/3 projects (at limit)
- **Solution:** Defer Idea 006 start to Mar 7 when Idea 007 completes
- **Impact:** 0 (no technical dependency, only resource conflict)

**Idea 001 + Idea 006 (Synergy):**
- **Type:** Weak synergy (future enhancement)
- **Opportunity:** Katana strategies → Consilium "Finance Advisor" mode
- **Timing:** Phase 2+ of Consilium (v1.1+), not MVP blocker
- **Value:** Medium (nice-to-have integration)

**Idea 003 + Idea 004 (Weak Synergy):**
- **Type:** Operational synergy
- **Opportunity:** VK recipes content + VK bot distribution
- **Timing:** Independent execution, can integrate later
- **Value:** Low-medium (modest cross-promotion opportunity)

**All Other Pairs:**
- **Result:** No dependencies (fully independent projects)

---

## 📅 MASTER TIMELINE: FEBRUARY - JULY 2026

### Visual Timeline (ASCII Gantt)

```
IDEA    FEB        MAR        APR        MAY        JUN        JUL
────────────────────────────────────────────────────────────────────────

007     ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        [SPRINT 30d] [SUPPORT 4w+]
        ▲                          ▲
        Feb 6 START               Mar 7 COMPLETE

001     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░
        [EPIC L ACTIVE] [LIVE TRADING] [COMPLETE]
        ▲                                      ▲
        Feb 6 ONGOING                          May 4 TARGET

003         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
            [MONETIZATION LIVE] [GROWTH]
            ▲                          ▲
            (IF STARTED) Mar 1        Apr 15 STABLE

006                     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                        [MVP DEV] [BETA] [LAUNCH]
                        ▲                          ▲
                        Mar 7 START                Jun 15 LAUNCH

002                                    ░░░░░░░░░░░░░
                                       [IF ACTIVE] [MVP LIVE]
                                       ▲
                                       May 1 (decision dependent)

004                                                  ░░░░░░░░░░░░░
                                                     [IF ACTIVE] [MVP]
                                                     ▲
                                                     May 15 (decision dependent)

005                                                  [QUEUED]
                                                     Score Apr 1, decide May

Legend:
████  = Active execution / critical path
░░░░  = Planned / conditional execution
▓▓▓▓  = Ongoing (continues)
▲     = Start/milestone date
```

---

## 📊 DETAILED TIMELINE BY IDEA

### IDEA 007 (DepylBrazil Franchise) — PRIMARY TIMELINE

```
FEB 6-7   │ ▲ DECISION GATE: Никита confirmation
FEB 8-14  │ ├─ Step 04 Consilium (Никита analysis)
FEB 15    │ ├─ Team commitment conversation
FEB 19    │ ├─ MILESTONE: Sочи location selection (Виолетта deadline)
FEB 26    │ ├─ Product franshiza finalization (Галина)
MAR 5     │ ├─ MILESTONE: Владимир documentation complete (Мария)
MAR 7     │ └─ ✅ MILESTONE: FRANCHISE v1 COMPLETE
          │    → 2 pilot locations operational
          │    → Revenue live ($100K+/mo)
          │    → Team transitions to support mode
MAR 7+    │ Ongoing: Support & pilot expansion
```

**Success Criteria:**
- ✅ Никита commits (Yes/No decision by Feb 7)
- ✅ All SMART goals met (Feb 5 baseline)
- ✅ 2 pilot locations running by Mar 7
- ✅ CRM + checklists operational
- ✅ Revenue $100K+/month by Mar 15

**Risk Events:**
- Feb 19: Sочи location not available → Backup locations
- Feb 26: Product specs unclear → Consilium deep dive
- Mar 7: Launch date slips → Cascade to Idea 006 start

---

### IDEA 001 (Katana VectorBT) — STEADY PROGRESSION

```
FEB 6     │ ▲ ONGOING: Epic L active (8/11 stories done)
FEB 20    │ ├─ Epic L: 10/11 stories (target)
MAR 6     │ ├─ Epic L: 100% complete
MAR 7-21  │ ├─ Paper Trading validation (2+ weeks)
MAR 22-   │ ├─ Live Trading preparation
APR 1     │ ├─ Live Trading MVP launch
APR 15    │ ├─ Risk validation (drawdown, overfitting checks)
MAY 4     │ └─ ✅ TARGET: ≥3 strategies Scaled-Live
          │    → Passive income generation active
          │    → Live trading monitoring ongoing
MAY 4+    │ Passive: Monitoring + optimization
```

**Success Criteria:**
- ✅ Epic L complete by Mar 6
- ✅ Paper trading successful (Sharpe >1.5)
- ✅ Live trading MVP by Apr 1
- ✅ ≥3 strategies Scaled-Live by May 4
- ✅ Revenue $2-4K/month by May 15

**Risk Events:**
- Mar 6: Epic L slips → May 4 target at risk
- Apr 1: Paper trading shows overfitting → Redesign needed
- Apr 15: Live trading drawdown >15% → Emergency pivot

---

### IDEA 006 (Consilium SaaS) — CONDITIONAL START

```
FEB 6-MAR 6 │ ▲ PREPARATION: L1-L6 plan ready
            │    (no active work, background prep only)
MAR 7       │ ├─ DECISION GATE: Idea 007 complete + WIP freed
MAR 7-8     │ ├─ Week 1: Product brief finalization
MAR 8-29    │ ├─ Weeks 2-4: Infrastructure setup
MAR 22-     │ ├─ Week 3+: Mode 1 development starts
APR 19      │ ├─ Week 8: Mode 1 Live (Meeting Moderator)
APR 26      │ ├─ Mode 2 development starts
MAY 17      │ ├─ Week 12: Mode 2 Live (Task Distributor)
MAY 18-JUN7 │ ├─ Weeks 13-16: Beta testing (50-100 users)
JUN 8-15    │ ├─ Weeks 17-18: Final polish + launch prep
JUN 15      │ └─ ✅ PUBLIC LAUNCH
            │    → MVP with 2 modes live
            │    → Beta retention >40% validated
            │    → 100 paying users target (Month 3)
JUN 15+     │ Growth: Customer acquisition, feedback loop
```

**Success Criteria:**
- ✅ Infrastructure ready by Mar 22
- ✅ Mode 1 live by Apr 19 (Week 8)
- ✅ Mode 2 live by May 17 (Week 12)
- ✅ Beta: >40% Week 1 retention
- ✅ Launch: 100 paying users by Jun 15
- ✅ API costs <$5K/month

**Risk Events:**
- Mar 7: Idea 007 slips → Delay Consilium start
- Apr 19: Mode 1 misses → Compress Mode 2 schedule
- May 18: Beta retention <40% → Pivot to niche use case
- API costs spike to $10K/week → Switch cheaper model

---

### IDEA 003 (VK Recipes Monetization) — CONDITIONAL PARALLEL

```
FEB 10  │ ▲ DECISION: START NOW (if capacity) or DEFER?
FEB 13  │ ├─ IF START: Content strategy finalization
FEB 20  │ ├─ Partner outreach (ad networks, brands)
FEB 27  │ ├─ First ad campaign live
MAR 13  │ ├─ Bot integration starts (simple auto-posting)
MAR 20  │ ├─ Bot MVP live (basic features)
APR 3   │ └─ ✅ EXPECTED: Bot features complete
        │    → Multiple revenue streams active
        │    → $1-5K/month revenue
APR 3+  │ Growth: Expand bot features, scale audience
```

**Success Criteria:**
- ✅ Content strategy locked by Feb 20
- ✅ First ad revenue by Feb 27
- ✅ Bot MVP by Mar 20
- ✅ Revenue $1K+/month by Apr 1
- ✅ Engagement metrics (likes, comments) +30%

**Risk Events:**
- Feb 27: No ad partners responsive → DIY monetization instead
- Mar 20: Bot development blocked by VK API → Manual posting continues
- Apr 1: Audience growth stalled → Re-strategy content calendar

---

### IDEAS 002, 004, 005 — QUEUE & EVALUATE (APRIL)

```
FEB-MAR  │ ▲ HOLD: Not started, awaiting MCDA scores
         │    └─ Idea 002 (Maps Bot) — Fast MVP potential
         │    └─ Idea 004 (VK Bot) — High competition risk
         │    └─ Idea 005 (Sales QA) — Complex, longer timeline

APR 1-6  │ ├─ Rapid MCDA scoring (8-10 hours total)
         │ └─ Decision on top 1-2 winners

APR 7-15 │ ├─ IF IDEA 002 WINS: Quick MVP sprint (2-4 weeks)
         │ │   └─ Target: MVP live by May 1
         │ │
         │ ├─ IF IDEA 005 WINS: Detailed design phase
         │ │   └─ Target: Development starts May 15
         │ │
         │ └─ IF IDEA 004 WINS: Competitive analysis
         │     └─ Target: MVP by May 30 (lower confidence)

APR 15+  │ Execution of selected idea(s)
```

**Decision Criteria (April 1):**
1. MCDA score (primary)
2. Time-to-MVP (secondary: prefer <8 weeks)
3. Revenue ceiling (tertiary: prefer $10K+/month)
4. Resource availability
5. Market timing (any competitors launched?)

**Likely Winner: Idea 002 (Maps Auto-Reply)**
- ✅ Fast MVP (2-4 weeks)
- ✅ High efficiency (40-80h to revenue)
- ✅ Multiple platforms (Yandex, Google, Zoon)
- ✅ Recurring revenue ($5-20K/month potential)
- ⚠️ Requires API access (all 3 platforms)

---

## ⚡ CRITICAL MILESTONES & DECISION GATES

### MUST-COMPLETE DATES

```
2026-02-07  │ [CRITICAL] Idea 007: Никита decision (GO/NO-GO)
2026-02-19  │ [HIGH]     Idea 007: Sочи location selected
2026-03-07  │ [CRITICAL] Idea 007: Franchise v1 COMPLETE
2026-03-07  │ [CRITICAL] Idea 006: Decision to start (WIP freed?)
2026-04-19  │ [HIGH]     Idea 006: Mode 1 live (demo-able)
2026-05-04  │ [HIGH]     Idea 001: Target completion date
2026-06-15  │ [HIGH]     Idea 006: Public launch
```

### CONTINGENCY DATES (If slip >3 days)

```
If Idea 007 slips >3 days (past Feb 19):
 → Reassess Mar 7 completion (likely 1-2 week slip)
 → Defer Idea 006 start to Apr 7 (cascades all Consilium dates)

If Idea 006 slips >2 weeks (past Mar 22 infrastructure):
 → Compress Mode 1 + Mode 2 into 6 weeks (Apr 19 still possible)
 → Or defer public launch to Jul 15

If Idea 001 slips >2 weeks (past May 4):
 → No cascade impact (low priority, passive income)
 → Target Aug 1 instead (acceptable)
```

---

## 🔄 RESOURCE HANDOFF SCHEDULE

### Feb 6 - Mar 7 (Idea 007 Sprint)

```
YOU (Никита):
├─ Idea 007: 5-7 hours/week (consilium, strategy, decisions)
├─ Idea 001: 8-12 hours/week (Epic L review, escalations)
├─ Idea 003: 5-10 hours/week (IF started, strategy + reviews)
└─ Total: 18-29 hours/week ✅ (within capacity)

Галина (Franchise Owner):
├─ CRM setup (40-80h over 30 days)
├─ Product standardization (20-30h)
└─ Team coordination (daily)

Виолетта (Sочи Pilot):
├─ Location search & negotiation (Feb 6-19)
├─ Salon setup & staffing (Feb 20 - Mar 7)
└─ Sales/operations optimization (ongoing)

Мария (Владимир Pilot):
├─ Documentation creation (10 key docs)
├─ Financial modeling (Feb 6-Mar 5)
└─ Process standardization (Feb 20 - Mar 7)
```

### Mar 7 - Jun 15 (Idea 006 Sprint + Idea 001 Finish)

```
YOU (Никита):
├─ Idea 007: 2-3 hours/week (support, escalations only)
├─ Idea 001: 6-10 hours/week (final 3 stories, Live Trading)
├─ Idea 006: 15-20 hours/week (MVP development, decisions)
├─ Ideas 002-004: 2-3 hours/week (April MCDA scoring)
└─ Total: 25-36 hours/week ✅ (within capacity)

Idea 006 Team (TBD):
├─ Backend developer: 200-300 hours (infrastructure)
├─ Frontend developer: 150-200 hours (UI/UX)
└─ DevOps: 50-80 hours (deployment, monitoring)

Idea 001 (Solo):
├─ Katana development: Structured, no handoff needed
└─ Paper Trading validation: Self-managed
```

---

## 📊 BURNOUT PREVENTION CHECKLIST

**Weekly Monitoring (Every Monday):**

```
Week of Feb 6:
□ Actual hours worked: __/50 target
□ Idea 007 status: ___
□ Idea 001 status: ___
□ Stress level (1-10): ___
□ Sleep quality: ___
□ Escalations: ___

Week of Feb 13:
□ Actual hours worked: __/50 target
□ Team commitment check: Done?
□ Idea 003 decision: Made?
□ Escalations: ___

(Repeat weekly through Mar 7)
```

**Warning Signs:**
- Hours consistently >50/week (2 consecutive weeks)
- Missed milestones (>2 slip past dates)
- Decision paralysis (can't decide on Ideas 002-005)
- Sleep <6 hours (3+ nights/week)

**Mitigation Actions:**
- Reduce Idea 003 effort (pause if >45 hours/week)
- Defer Idea 006 start (push to Apr 7)
- Get CRM specialist to handle Bitrix24 setup
- Take 1-2 days off (Idea 007 is marathon, not sprint)

---

## 🎯 POST-TIMELINE VISION (Q3 2026)

```
BY END OF JULY 2026:

Portfolio Status:
├─ Idea 007: Scaled to 3-5 pilot locations
│  └─ Revenue: $200K-500K/month
├─ Idea 001: ≥3 strategies Scaled-Live + 2 more in Paper Trading
│  └─ Revenue: $5-10K/month
├─ Idea 006: 500-1000 active users, 200-500 paying
│  └─ Revenue: $3-10K/month (growth phase)
├─ Idea 003: 20K+ followers, bot fully integrated
│  └─ Revenue: $5-15K/month
└─ Idea 002 (if started): MVP live, first customers acquired
   └─ Revenue: $2-5K/month (early traction)

Total Portfolio Revenue: $215K-540K/month
Annual Run Rate: $2.6M - $6.5M
Average across all projects: ~$100K-150K/month per active idea

Growth Trajectory: Exponential (3-6 month payoff window)
```

---

## 📎 FILES & REFERENCES

- **Full Analysis:** `PORTFOLIO-OPTIMIZATION-ANALYSIS.md`
- **Quick Reference:** `PORTFOLIO-QUICK-REFERENCE.md`
- **This Document:** `PORTFOLIO-DEPENDENCIES-TIMELINE.md`

---

**Created:** February 6, 2026
**Last Updated:** Feb 6, 2026
**Next Review:** Feb 13, 2026 (weekly checkpoint)
**Revision History:** Initial creation
