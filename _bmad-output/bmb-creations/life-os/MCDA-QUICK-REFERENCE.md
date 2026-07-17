# MCDA Re-Scoring: Quick Reference (1-Page Summary)

**Date:** 2026-02-06 | **Method:** Multi-Criteria Decision Analysis (5 criteria, 1-5 scale)

---

## 📊 SCORE COMPARISON TABLE

| # | Idea | Current | NEW | Change | Recommendation |
|---|------|---------|-----|--------|-----------------|
| 1 | 🎯 **Katana-VectorBT** | 10.0 | **10.0** | ✅ — | **EXECUTE NOW** (Tier 1) |
| 5 | 📞 **Sales QA Platform** | 8.5 | **8.5** | ✅ — | **EXECUTE Q2** (Tier 1) |
| 3 | 🍽️ **VK Recipes** | 8.0 | **8.0** | ✅ — | **SECONDARY** (Tier 2) |
| 7 | 💅 **DepylBrazil Franchise** | 7.5 | **6.5** | 🚩 -1.0 | **CONDITIONAL** (Decision Feb 7) |
| 6 | 🤖 **Consilium SaaS** | 7.0 | **5.0** | 🚩 -2.0 | **DEFER** (Validate PMF first) |
| 2 | 🗺️ **Maps Auto-Reply** | 5.5 | **5.5** | ✅ — | **BACKLOG** (Tier 3) |
| 4 | 🤖 **VK Bot** | 5.5 | **5.5** | ✅ — | **BACKLOG** (Tier 3) |

---

## 🚨 MAJOR CHANGES (Flagged)

### 🚩 CONSILIUM SaaS: -2.0 POINTS (7.0 → 5.0)
**Why downgraded?**
- Consumer SaaS risk underestimated (90% failure rate)
- PMF unvalidated → confidence ↓ (3→2)
- High execution risk → effort ↓ scoring
- Risk: churn high, API vendor dependency

**New recommendation:** **DEFER to Q3** — validate with 4-week PMF experiment first (not 12-week build)

---

### 🚩 DEPYLBRAZIL FRANCHISE: -1.0 POINT (7.5 → 6.5)
**Why downgraded?**
- Nikita's commitment unclear (72-hour decision window)
- Operational burden on Galina underestimated
- Alignment: high ops touch doesn't match goals

**New recommendation:** **CONDITIONAL** — decision point Feb 7
- If Nikita commits: proceed with 30-day sprint (Galina-led)
- If Nikita declines: archive for future

---

## ✅ EXECUTION ROADMAP

### TIER 1: Execute Now
```
🎯 KATANA (10.0/10)
├─ Timeline: 8-12 weeks (Feb-Apr)
├─ Focus: Complete Epic L → Paper Trading → Live
└─ Target: 3+ Scaled-Live strategies by May

📞 SALES QA (8.5/10)
├─ Timeline: 16 weeks (Apr-Jul)
├─ Focus: Narrow MVP (2 integrations, 1 language)
└─ Target: >40% Week 1 retention validation
```

### TIER 2: Secondary / Conditional
```
🍽️ RECIPES (8.0/10)
├─ Timeline: Parallel, 4-8 weeks
├─ Focus: Monetization + bot
└─ Effort: Low commitment (4-6 hrs/week)

💅 DEPYLBRAZIL (6.5/10) — IF Feb 7 YES
├─ Timeline: 30-day sprint (Feb-Mar)
├─ Focus: Franchise packaging v1
└─ Team: Galina-led
```

### TIER 3: Defer / Backlog
```
🤖 CONSILIUM (5.0/10) ← DOWNGRADED
├─ Action: 4-week PMF validation FIRST (not 12-week build)
├─ Validation gate: >40% Week 1 retention
└─ If fails: STOP, if succeeds: continue

🗺️ MAPS BOT (5.5/10)
└─ Keep warm, revisit Q3/Q4

🤖 VK BOT (5.5/10)
└─ Keep warm, revisit Q3/Q4
```

---

## 🎯 MCDA SCORING CRITERIA

| Criterion | Scale | Notes |
|-----------|-------|-------|
| **IMPACT** | 1-5 | Revenue potential, market size, scalability |
| **CONFIDENCE** | 1-5 | Team capability, existing assets, feasibility |
| **EFFORT** | 1-5 | Resource needs [INVERTED: low effort = high score] |
| **ALIGNMENT** | 1-5 | Strategic fit with Life OS goals |
| **RISK** | 1-5 | Risk mitigation [INVERTED: well-mitigated = high score] |

**Formula:** (I + C + E + A + R) / 5 × 2.5 = Score/10

---

## 📊 DETAILED SCORING EXAMPLES

### Example 1: Katana (Highest)
```
Impact: 5 (Passive income, scalable, proven market)
Confidence: 5 (173 tasks done, Epic L 8/11)
Effort: 4 (40-60 hrs = LOW effort)
Alignment: 5 (Direct match to 2026 goal)
Risk: 4 (Well-mitigated, market risk only)

(5+5+4+5+4)/5 × 2.5 = 10.0/10
```

### Example 2: Consilium (Downgraded)
```
OLD Scoring: (4+3+1+4+2)/5 × 2.5 = 7.0/10
NEW Scoring: (3+2+1+3+1)/5 × 2.5 = 5.0/10

Impact: 4→3 (crowded market, PMF unproven)
Confidence: 3→2 (consumer SaaS = hard execution)
Effort: 1 (400-800 hrs = HIGH)
Alignment: 4→3 (distraction risk)
Risk: 2→1 (PMF unproven, churn high = HIGH RISK)
```

---

## 🔑 KEY DECISIONS

| Decision | Status | Deadline |
|----------|--------|----------|
| DepylBrazil commitment (Nikita) | ⏳ Pending | Feb 7, 2026 |
| Sales QA MVP scope finalization | 📋 Todo | Feb 10, 2026 |
| Consilium PMF validation decision | 📋 Todo | Start immediately (4-week sprint) |

---

## 💡 PORTFOLIO TAKEAWAYS

1. **Katana + Sales QA = core** (both 8.5+) → execute in parallel (Q2+)
2. **Recipes = quick win** (8.0) → secondary, can run parallel
3. **DepylBrazil = conditional** (6.5) → decision Feb 7
4. **Consilium = DEFER** (5.0) ← **MAJOR CHANGE from 7.0** → validate PMF first
5. **Maps + VK Bot = backlog** (5.5 each) → revisit Q3/Q4

---

**Full details:** See `MCDA-RESCORING-ALL-7-IDEAS.md`
