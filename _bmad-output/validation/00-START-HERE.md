---
title: "PRD vs Brief Validation - START HERE"
date: 2026-02-27
---

# ⚡ PRD vs Brief Validation - START HERE

**Validation Complete:** ✓ 2026-02-27
**Project:** katana-vectorbt
**Coverage:** 46.9% (17 gaps identified)
**Status:** Ready for team review

---

## 📊 Key Finding

**The PRD covers only 46.9% of Brief requirements.**

| Category | Items | Coverage | Status |
|----------|-------|----------|--------|
| CRITICAL | 10 | 37.5% | 🔴 BLOCKING |
| HIGH | 7 | 30.0% | 🟡 IMPORTANT |
| MEDIUM | 6 | 66.7% | 🟠 MANAGEABLE |
| DEFERRED | 14 | N/A | 🟢 BY DESIGN |

---

## 🎯 What You Need to Do

### Immediately (Next 48 hours)
1. **Read:** VALIDATION-SUMMARY.md (10 min)
   - See: "Decision Matrix: Phase 1a vs Phase 1b"
   - Choose: Option A (recommended), B, or C

2. **Decide:** Phase 1a scope
   - Option A: Add all 10 CRITICAL gaps (+3-5 weeks) ✓ RECOMMENDED
   - Option B: Add 5, defer 5 (+1-2 weeks)
   - Option C: Defer all (no timeline change) ✗ NOT RECOMMENDED

3. **Communicate:** Decision to team (architect, lead dev, PM)

### This Week (2026-03-01 to 2026-03-06)
1. **Read:** GAP-PRD-vs-BRIEF.md (detailed)
   - See: Parts 1-2 (CRITICAL + HIGH gaps with specs)

2. **Create:** JIRA issues for each gap (label: FROM_BRIEF_GAP)

3. **Update:** PRD with Phase 1a additions (if Option A chosen)

4. **Create:** Validation checklist for Phase 1 go-live

### Weekly Reviews (2026-03-06 onwards)
- [ ] Checkpoint 1: 2026-03-06 (week 1)
- [ ] Checkpoint 2: 2026-03-13 (week 2)
- [ ] Checkpoint 3: 2026-03-20 (week 3)
- [ ] Final check: Before go-live

---

## 📁 Document Guide

### 1. VALIDATION-SUMMARY.md (Executive Brief)
**For:** PMs, team leads, stakeholders
**Time:** 10 minutes
**Contains:**
- Coverage metrics
- Critical gaps checklist
- Decision matrix (A/B/C)
- Effort breakdown
- Timeline impact
- Weekly action items

**→ Read this FIRST**

---

### 2. GAP-PRD-vs-BRIEF.md (Detailed Analysis)
**For:** Architects, technical leads, developers
**Time:** 30-45 minutes
**Contains:**
- Executive summary
- Part 1: CRITICAL gaps (10 items, detailed)
- Part 2: HIGH gaps (7 items, detailed)
- Part 3: PARTIAL coverage (6 items)
- Part 4: PRD-only items (Phase 1b/2)
- Part 5: Validation summary
- Part 6: Remediation plan
- Part 7: Recommendations

**→ Read PARTS 1-2 for gap details**

---

### 3. REQUIREMENTS-MATRIX.md (Traceability)
**For:** Developers, QA, implementers
**Time:** 20-30 minutes
**Contains:**
- CRITICAL requirements table (10 items)
- HIGH requirements table (7 items)
- MEDIUM requirements table (6 items)
- Phase 1a/1b effort breakdown
- Total effort: 128 hours

**→ Use as reference during implementation**

---

### 4. INDEX.md (Navigation)
**For:** Finding specific information
**Contains:**
- Quick navigation by role
- Document descriptions
- Key metrics summary
- File locations
- Weekly progress tracking

**→ Use to find what you need**

---

## 🔴 Critical Gaps (10 Items)

These are BLOCKING go-live if not addressed:

1. **Mandatory Baseline** - KatanaTransformer requirement validation
2. **MTF 6 Caches** - OHLCVStore PostgreSQL backend specification
3. **MTF Independence** - NO cross-TF bias gating rule
4. **MTF Kill-Switch** - Thresholds and monitoring logic
5. **H4 Independent** - H4 as peer timeframe (not legacy special)
6. **115 Parameters** - Complete parameter taxonomy (16 categories)
7. **DFF Flat Params** - 6 types with per-role specs (no variant_id)
8. **DFF-Calendar** - DFF + calendar safety integration rules
9. **Kill-Switch 40%** - Individual rocket MaxDD limit
10. **Kill-Switch 50%** - Portfolio/bucket MaxDD limit

**→ See GAP-PRD-vs-BRIEF.md Parts 1-2 for details**

---

## ⏰ Timeline Impact

### Current State
- Phase 1 planned: ~2026-03-09
- PRD coverage: 46.9% (incomplete)

### Option A (RECOMMENDED) - Add All Gaps
- Effort: 110 hours
- Timeline: +3-5 weeks
- New date: ~2026-03-23
- Risk: LOW ✓

### Option B - Add 5, Defer 5
- Effort: 55 hours + 54 hours (Phase 1b)
- Timeline: +1-2 weeks
- New date: ~2026-03-16
- Risk: MEDIUM

### Option C - Defer All
- Effort: 0 (Phase 1a) + 164 hours (Phase 1b)
- Timeline: No change
- New date: ~2026-03-09
- Risk: HIGH ✗

**→ OPTION A is recommended for quality and Brief compliance**

---

## ✅ Sign-Off Checklist

Who needs to approve:
- [ ] **Architect:** "I understand gaps and approve Phase 1a scope"
- [ ] **Lead Dev:** "We can deliver in 3-5 weeks"
- [ ] **PM:** "New timeline approved"
- [ ] **NIKITA:** "Validated and ready to implement"

---

## 📞 Questions?

### For gap definitions
→ Read GAP-PRD-vs-BRIEF.md Parts 1-2

### For effort estimates
→ Read REQUIREMENTS-MATRIX.md

### For timeline impact
→ Read VALIDATION-SUMMARY.md "Decision Matrix"

### For executive decision
→ Read VALIDATION-SUMMARY.md (full document)

### For implementation details
→ Use REQUIREMENTS-MATRIX.md as reference

---

## 🚀 Next Step

**Read VALIDATION-SUMMARY.md and decide Phase 1a scope (Option A/B/C)**

**Estimated time:** 10 minutes
**File location:** `d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad-output\validation\VALIDATION-SUMMARY.md`

---

**Report Status:** COMPLETE ✓
**Generated:** 2026-02-27 by Claude Code Analysis Agent
**All files:** `/validation/` directory (4 main files + supporting docs)

