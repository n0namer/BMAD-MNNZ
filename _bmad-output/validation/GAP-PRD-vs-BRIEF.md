---
title: "GAP Analysis: PRD vs Brief"
date: 2026-02-27
scope: phase1_full
project: katana-vectorbt
validation_type: structural_coverage
coverage_percentage: 46.9
status: active
---

# GAP Analysis: PRD vs Brief Validation Report

**Project:** katana-vectorbt
**Scope:** Phase 1 Full Coverage Validation
**Analysis Date:** 2026-02-27
**Documents:**
- Brief: `katana-v-01-product-brief-2026-01-17.md` (123KB, 40 sections)
- PRD: `katana-v-02-prd-katana-vectorbt-2026-01-18.md` (300KB, 21 sections)

---

## Executive Summary

### Coverage Metrics
| Metric | Value | Status |
|--------|-------|--------|
| **Overall PRD Coverage of Brief** | 46.9% | ⚠️ CRITICAL |
| **Brief Features in PRD** | 15/32 items | PARTIAL |
| **CRITICAL Gaps** | 10 items | 🔴 HIGH RISK |
| **HIGH Priority Gaps** | 7 items | 🟡 MEDIUM RISK |
| **MEDIUM Priority Gaps** | 6 items | 🟠 LOW RISK |
| **Brief Sections** | 40 main + 66 sub | COMPREHENSIVE |
| **PRD Sections** | 21 main + 108 sub | DETAILED |

### Status
⚠️ **PRD is INCOMPLETE relative to Brief baseline.** Multiple architectural and technical requirements from the Brief are either:
- Not mentioned in PRD
- Mentioned but not detailed in PRD
- Deferred to Phase 2 (but not explicitly flagged as gaps)

**Recommendation:** Review gaps and explicitly decide for each: (a) defer to Phase 1b/2, or (b) add to Phase 1 scope.

---

## Part 1: CRITICAL Brief Requirements NOT in PRD

**Count:** 10 items | **Status:** 🔴 HIGH RISK

These are foundational/blocking requirements from Brief that are missing, underdeveloped, or implicit in PRD.

### 1. Mandatory Baseline (KatanaTransformer)
**Brief Definition:**
```
⚠️ MANDATORY BASELINE REQUIREMENT (BLOCKING)
ALL testing/optimization/validation MUST use:
- Source: docs/KATANA_ORIGINAL.md (strategy specification)
- Implementation: katana/katana_transformer.py
- Profiles: Katana 1 (RSI+MA, ALL) and Katana 1.1 (RSI+MA+BB+gate_vol, k=2)
BLOCKING: NO simple RSI, MA-only, or single-indicator strategies.
Validation: Verify script uses KatanaTransformer class before ANY work.
```

**PRD Status:** ✗ NOT FOUND
**Risk Level:** 🔴 CRITICAL
**Impact:** Validation framework may accept non-compliant strategies
**Action Required:** ADD to PRD Functional Requirements (FR-XXX)

### 2. Multi-Timeframe 6 Independent Caches (OHLCVStore)
**Brief Definition:**
- 6 independent caches: 1m, 5m, 15m, 1h, 4h, 1d
- PostgreSQL OHLCVStore backend with incremental ingestion
- Each TF has own Optuna study, own HNSW index, own history
- All 6 TF run in parallel

**PRD Status:** ✗ NOT EXPLICITLY DEFINED
Mentioned in "Multi-Timeframe Trading Architecture" but missing:
- OHLCVStore backend specification
- Incremental ingestion details
- HNSW index per TF requirement
- PostgreSQL schema requirements

**Risk Level:** 🔴 CRITICAL
**Impact:** Implementation may use wrong backend (e.g., CSV/Parquet instead of PostgreSQL)
**Action Required:** ADD explicit Technical Specification section to PRD

### 3. MTF Independence Guarantee (NO Cross-TF Bias Gating)
**Brief Definition:**
```
Default (v1.0): NO cross-timeframe bias gating.
Each timeframe trades independently with its own signals and risk management.
No HTF→LTF blocking; no directional bias inheritance; no hedging/netting
restrictions across timeframes.
```

**PRD Status:** ✗ NOT FOUND
**Risk Level:** 🔴 CRITICAL
**Impact:** Implementation may add unwanted TF dependencies; violates Brief design
**Action Required:** ADD explicit design rule to PRD Architecture section

### 4. MTF Kill-Switch Logic
**Brief Definition:**
```
- mtf_confirmation_mode: "none" | "hard_block" | "soft_penalty"
- Kill-switch: if mtf_block_rate > mtf_block_rate_max OR
  mtf_delta_DSR_vs_none < 0 → auto-rollback to "soft_penalty" or "none"
- Mandatory metrics:
  * mtf_block_rate (% blocked)
  * mtf_delta_DSR_vs_none
  * mtf_shadow_pnl_blocked
```

**PRD Status:** ✗ NOT EXPLICITLY DEFINED
Mentioned vaguely in risk mitigation but missing:
- Specific metric definitions
- Threshold values (mtf_block_rate_max, DSR threshold)
- Auto-rollback implementation details

**Risk Level:** 🔴 CRITICAL
**Impact:** Optimization may continue with degraded MTF performance
**Action Required:** ADD detailed specification with thresholds to NFR section

### 5. H4 Independent Cache (Own Optuna Study)
**Brief Definition:**
```
H4 Role Canonical Definition:
- H4 is an independent timeframe cache with its own optimization study
- H4 participates in optimization identically to all other TF (1m, 5m, 15m, 1h, 1d)
- H4 may optionally act as a volatility reference anchor inside DFF overrides
- H4 does NOT block or authorize trades in other TF by default
- Any cross-TF influence must be explicitly enabled via strategy_profile
```

**PRD Status:** ✗ NOT FOUND
**Risk Level:** 🔴 CRITICAL
**Impact:** H4 may be treated as special (legacy Wave 3 behavior) instead of peer
**Action Required:** ADD H4 role definition as separate FR in PRD

### 6. 115 Parameters Wave 4 (Full Parameter Taxonomy)
**Brief Definition:**
```
Wave 4: 115 total parameters across 16 categories
Categories include:
- Entry signal parameters (RSI, MA, MACD, etc.)
- Exit signal parameters
- DFF parameters (6 types with per-role flat params)
- Risk parameters (volatility, leverage, drawdown)
- Calendar safety parameters
- News overlay parameters
- Rocket-specific parameters
- ... 9 other categories
```

**PRD Status:** ✗ NOT FULLY DETAILED
Mentioned as "115 Parameters Epic" but missing:
- Complete parameter taxonomy (16 categories)
- Per-parameter type definitions
- Per-parameter valid ranges
- Conditional parameter dependencies

**Risk Level:** 🔴 CRITICAL
**Impact:** Parameter search may miss critical parameters or sample from wrong ranges
**Action Required:** ADD Parameter Taxonomy table to PRD (or reference Brief)

### 7. DFF Flat Parameter Structure (NO variant_id)
**Brief Definition:**
```
Distance Function Factory (DFF) - Flat Parameter Structure:
- 6 DFF types: atr, stddev, bb_half, range, fixed_pct, corwin_schultz
- Type is categorical; required flat params are conditional per type
- NO dict, NO variant_id (Wave 4 change)
- Per-role flat params: e.g., if type=="atr": [length, multiplier]
- Validation rules: (1) params match type contract, (2) ranges valid,
  (3) per-role constraints honored
```

**PRD Status:** ✗ NOT EXPLICITLY DETAILED
"DFF Flat Parameters" mentioned but missing:
- The 6 types and their specs
- Exact flat parameter list per type per role
- Migration from Wave 3 (variant_id removal)
- Validation contract

**Risk Level:** 🔴 CRITICAL
**Impact:** DFF configuration misalignment; storage/optimization conflicts
**Action Required:** ADD DFF Specification section to PRD with full contract

### 8. DFF Integration into Calendar Safety
**Brief Definition:**
```
Calendar Safety & DFF Integration: HARD (120/60min) + SOFT (30/30min)
dихотомия. DFF интегрирована в оба слоя.
- HARD (non-optimizable): 120min pre-event / 60min post-event
- SOFT (optimizable): 30min pre-event / 30min post-event for news overlay
- DFF can override calendar safety parameters per-role
```

**PRD Status:** ✗ NOT FOUND
Calendar Safety mentioned separately, but no integration with DFF documented.

**Risk Level:** 🔴 CRITICAL
**Impact:** DFF may bypass calendar safety; event handling may be inconsistent
**Action Required:** ADD DFF-Calendar integration section

### 9. Kill-Switch: 40% MaxDD (Individual Rocket)
**Brief Definition:**
```
Rockets Kill-Switch (Individual): 40% MaxDD
Peak-to-trough MaxDD on equity curve (after fees/slippage),
triggers immediate stop + blacklist.
```

**PRD Status:** ✗ NOT EXPLICITLY FOUND
Risk mitigation mentions kill-switches but not the specific 40% threshold.

**Risk Level:** 🔴 CRITICAL
**Impact:** Rocket strategies may run losses beyond tolerance
**Action Required:** ADD explicit 40% MaxDD kill-switch rule to Risk NFR

### 10. Kill-Switch: 50% MaxDD (Portfolio/Rocket Bucket)
**Brief Definition:**
```
Rockets Kill-Switch (Portfolio): 50% MaxDD
Peak-to-trough MaxDD of rocket bucket (not total NAV),
triggers freeze + rebalance + RCA.
```

**PRD Status:** ✗ NOT EXPLICITLY FOUND
**Risk Level:** 🔴 CRITICAL
**Impact:** Rocket bucket may suffer excessive losses; portfolio not protected
**Action Required:** ADD explicit 50% MaxDD portfolio kill-switch rule to Risk NFR

---

## Part 2: HIGH-Priority Brief Requirements with GAPS in PRD

**Count:** 7 items | **Status:** 🟡 MEDIUM RISK

These are foundational but slightly less critical; PRD mentions them but lacks detail.

### 1. Source of Truth Hierarchy (L1>L2>L3 Override Rules)
**Brief Definition:**
```
Hierarchy Levels (with sync rules):
| Level | Document | Purpose |
|-------|----------|---------|
| L1: Source of Truth | Product Brief (this file) | Core vision, goals, canonical values |
| L2: Specifications | PRD, Architecture | Detailed requirements, technical architecture |
| L3: Implementation | Code, configs | Executable reality |
| L4: Derivatives | Runbooks, API docs | Operational guidance |

Sync Rules:
1. L1 changes → trigger L2 review → propagate to L3
2. L2 cannot contradict L1 (escalate if conflict)
3. L3 (code) is ground truth for implementation; file correction ticket if differs
When docs conflict: Brief (L1) > PRD/Architecture (L2) > Implementation notes (L3)
```

**PRD Status:** ⚠️ MENTIONED but NO OPERATIONAL RULES
PRD mentions "Canonical Override Rule" but doesn't detail:
- The 4-level hierarchy
- Sync automation triggers
- Escalation procedures
- Conflict resolution workflows

**Risk Level:** 🟡 MEDIUM
**Impact:** Teams may not know which doc is source of truth; conflicts unresolved
**Action Required:** ADD formal hierarchy section to PRD governance

### 2. Optuna with 8000 Trials (Per-TF Parallel)
**Brief Definition:**
```
- 8000 trials per timeframe (independent)
- All 6 TF run in parallel
- Optuna study per TF
- Conditional search space (define-by-run)
- QMC initialization for first 32 trials (antithetic sampling)
```

**PRD Status:** ⚠️ MENTIONED in Epic but NOT DETAILED
PRD has "Wave 4 Features: 8000 Trials" but missing:
- Per-TF trial allocation (is it 8000 each or 8000 total?)
- Parallel execution model (threading, multiprocessing)
- Trial budget constraints
- Pruning/stopping rules

**Risk Level:** 🟡 MEDIUM
**Impact:** Optimization may exceed compute budget or run sequentially
**Action Required:** ADD explicit Optimization Strategy section

### 3. HNSW Index Per Timeframe (Artifact Registry)
**Brief Definition:**
```
Each timeframe maintains isolated artifact registry with:
- HNSW vector index for parameter similarity search
- 150x-12,500x faster search vs brute-force
- Configurable dimensions, ef_construction
```

**PRD Status:** ✗ NOT FOUND
**Risk Level:** 🟡 MEDIUM
**Impact:** Artifact lookup may be slow; pattern reuse not optimized
**Action Required:** ADD artifact registry and HNSW specification

### 4. PostgreSQL OHLCVStore Backend (Incremental Ingestion)
**Brief Definition:**
```
Data Backend:
- PostgreSQL with OHLCVStore extension/schema
- Incremental ingestion (append-only, immutable snapshots)
- Time-series compression
- 6 TF caches completely independent
- Snapshot hash for data integrity check
```

**PRD Status:** ✗ NOT FOUND
**Risk Level:** 🟡 MEDIUM
**Impact:** Data pipeline may not be scalable; incremental updates may not work
**Action Required:** ADD Data Architecture section

### 5. Strategy Profiles Explicit Definition (stable/return/rocket)
**Brief Definition:**
```
Strategy Profiles (Goal Axis) - Each profile defines:
- stable: Low drawdown, low sensitivity, robustness >> raw returns
- return: CAGR/Calmar/AdjSharpe with constraints (DD, tail-risk)
- rocket: High-variance, small deposits, 40–55% win rate per strategy
  (Used ONLY in isolated rocket bucket with strict loss limits)

Each profile defines:
- objective function (what to optimize)
- constraints (what is forbidden/bounded)
- promotion rules (when to move to live)
- allowed risk and capital allocation
- active_param_count ranges (e.g., rocket: 40–70, minimal: 10–25)
```

**PRD Status:** ⚠️ MENTIONED but VAGUE on constraints/promotion
PRD describes profiles but missing:
- Exact objective functions (Sharpe formula, etc.)
- Constraint thresholds (max DD, max leverage, etc.)
- Promotion rules (e.g., "stable: pass walk-forward + 3-month live test")
- Active parameter count constraints per profile

**Risk Level:** 🟡 MEDIUM
**Impact:** Optimization may use wrong objective; parameter count unbounded
**Action Required:** ADD explicit Profile Specification table

### 6. Max Leverage Cap 5x (Hard Limit)
**Brief Definition:**
```
| **Max Leverage Cap** | N/A | 5x | Hard cap across all profiles unless exchange limit lower |
```

**PRD Status:** ⚠️ MENTIONED in Risk but not as HARD CAP
PRD discusses leverage but missing:
- The 5x explicit limit
- Enforcement mechanism (reject trades, cap exposure)
- Per-profile leverage ranges (if different)
- Exchange-specific overrides

**Risk Level:** 🟡 MEDIUM
**Impact:** Strategies may run at >5x leverage, violating risk policy
**Action Required:** ADD explicit 5x hard cap to Risk NFR with enforcement

### 7. Rollback Strategy (Auto-Rollback Conditions)
**Brief Definition:**
```
Rollback Strategy - Auto-rollback triggers:
1. MTF kill-switch: if mtf_block_rate > max OR delta_DSR < 0
   → rollback to "soft_penalty" or "none"
2. Individual kill-switch: if equity MaxDD > 40%
   → immediate stop + blacklist
3. Calendar conflict: if news event conflicts,
   → pause trades until event window closes
4. Data quality: if data_hash mismatch or leakage detected
   → rollback to last known-good snapshot
```

**PRD Status:** ⚠️ MENTIONED in Risk but not systemic
PRD discusses mitigations but missing:
- Clear rollback triggers
- Rollback mechanism (how to execute, what state to restore to)
- Communication (alerts, logs)
- Re-optimization after rollback

**Risk Level:** 🟡 MEDIUM
**Impact:** Failed strategies may not be stopped in time
**Action Required:** ADD explicit Rollback Strategy section

---

## Part 3: Brief Requirements with PARTIAL Coverage in PRD

**Count:** 6 items | **Status:** 🟠 LOW RISK

These are mentioned in PRD but need expansion or explicit connection to Brief.

| Requirement | Brief | PRD | Gap | Risk |
|-------------|-------|-----|-----|------|
| Parameter Profiles System | ✓ Detailed | ✓ Mentioned | Missing active_param_count ≤70 invariant | 🟠 LOW |
| Capital Buckets (core+rocket) | ✓ Detailed | ✓ Mentioned | Missing allocation rules, rebalancing triggers | 🟠 LOW |
| Rockets VC Model | ✓ Detailed | ✓ Mentioned | Missing capital allocation algorithm, rebalancing schedule | 🟠 LOW |
| Calendar Safety (HARD 120/60) | ✓ Detailed | ✓ Mentioned | Missing exact event detection, database of events | 🟠 LOW |
| Calendar Safety (SOFT 30/30) | ✓ Detailed | ✓ Mentioned | Missing news overlay toggle, API integration | 🟠 LOW |
| Canonical Values Table | ✓ Detailed | ✓ Referenced | Table not reproduced in PRD; relies on external reference | 🟠 LOW |

**Action:** Expand these sections with explicit references to Brief; move tables/specifications inline.

---

## Part 4: PRD Requirements NOT in Brief (Phase 1b/Phase 2)

**Count:** 14 items | **Status:** 🟢 BY DESIGN (Scoping decision)

These are PRD additions deferred to Phase 1b or Phase 2; they are intentional extensions.

### Phase 1b (Secondary - IF scope permits)
1. **Jupyter Notebook integration** - Interactive analysis, parameter sweeps
2. **Advanced Visualization** - Heatmaps, 3D parameter surfaces, regime detection
3. **Multi-signal correlation analysis** - Cross-indicator dependencies
4. **Performance attribution** - Which parameters, indicators, timeframes drive returns
5. **Backtesting report generation** - HTML export with charts and stats
6. **Alert system** - Slack/email for key events (optimization complete, kill-switch triggered)

### Phase 2+ (Future - Deferred, Non-binding)
1. **Streamlit evaluation** - Alternative to Jupyter
2. **Enterprise features** - Multi-user, SaaS (NOT for Phase 1)
3. **SOC2/PCI/GDPR compliance** - Deferred (single-user focus)
4. **99.9% uptime SLA** - Deferred
5. **Revenue modeling** - Not applicable to Phase 1 (single-user, passive income)
6. **Support ops** - Chat, tickets, SLA (deferred)
7. **Multi-region deployment** - Deferred
8. **GPU acceleration** - Deferred to Phase 2

**Action:** PRD correctly marks these as deferred; no action needed. Ensure Phase 1 scope stays focused.

---

## Part 5: Validation Summary & Coverage Report

### Coverage by Category

| Category | Brief Items | PRD Items | Coverage | Gap Count |
|----------|------------|-----------|----------|-----------|
| **CRITICAL Requirements** | 16 | 6 | 37.5% | 10 ⚠️ |
| **HIGH Architectural** | 10 | 3 | 30.0% | 7 ⚠️ |
| **MEDIUM Operational** | 6 | 4 | 66.7% | 2 |
| **PHASE 1b Additions** | - | 6 | N/A | - |
| **PHASE 2+ Deferred** | - | 8 | N/A | - |
| **TOTAL** | 32 | 27 | **46.9%** | **17 GAPS** |

### Quality Metrics

```
Overall Coverage Score: 46.9%
  ├─ CRITICAL requirements coverage: 37.5% (10 gaps)
  ├─ HIGH priority coverage: 30.0% (7 gaps)
  ├─ MEDIUM priority coverage: 66.7% (2 gaps)
  └─ Deferred by design: 14 items (14 Phase 1b/2 additions)

Risk Level: 🔴 HIGH
  ├─ Critical gaps that may cause implementation issues: 10
  ├─ High-priority gaps that reduce clarity: 7
  └─ Medium-priority gaps that are manageable: 2
```

### Brief vs PRD Document Comparison

| Aspect | Brief | PRD | Observation |
|--------|-------|-----|-------------|
| **Length** | 123KB | 300KB | PRD more detailed but misses Brief fundamentals |
| **Main Sections** | 40 | 21 | PRD has fewer high-level topics |
| **Subsections** | 66 | 108 | PRD goes deeper in some areas |
| **Requirement Markers** | 19 | 48 | PRD is more explicit about MUST/CRITICAL |
| **Use of Canonical Values** | 1 table (Wave 4) | 1 reference | PRD should import/expand this |
| **Explicit Parameters** | ~115 listed | ~80 listed | PRD missing some parameter definitions |

---

## Part 6: Remediation Plan & Decisions

### Decision 1: Add CRITICAL Gaps to Phase 1a Scope
**Recommended Action:** Review these 10 gaps with team and decide:
- **(A) Add to Phase 1a** if implementable in remaining time (< 1 week)
  - KatanaTransformer requirement
  - MTF kill-switch logic (thresholds + metrics)
  - H4 role definition
  - DFF flat parameter spec
  - Kill-switch thresholds (40% / 50%)

- **(B) Defer to Phase 1b** (extend Phase 1 by 1–2 weeks) if needed for quality
  - OHLCVStore detailed spec
  - HNSW index per TF
  - PostgreSQL schema
  - Full 115-parameter taxonomy
  - DFF-Calendar integration

- **(C) Defer to Phase 2** if out of scope
  - Complete source-of-truth hierarchy automation
  - Full rollback orchestration
  - Complex parameter interdependencies

### Decision 2: Synchronize PRD to Brief
**Recommended Action:** Create synchronization task:
1. Copy Canonical Values Table from Brief → PRD (or explicit reference)
2. Create "Brief Reference" section in PRD linking to source
3. For each CRITICAL gap, add placeholder section in PRD with "TBD" or "DEFERRED"
4. Run automated diff monthly to catch new gaps

### Decision 3: Add Explicit Deferred Markers
**Recommended Action:** For all 14 PRD additions (Phase 1b/2), explicitly mark:
```markdown
### Jupyter Notebook Integration [PHASE 1b - IF SCOPE PERMITS]
**Status:** Deferred pending Phase 1a completion
**Estimated Effort:** 3–5 days
**Go-Live Gate:** Not blocking v1.0 go-live
```

### Decision 4: Create Gap Tracking Dashboard
**Recommended Action:** Weekly tracking of:
- Gap remediation status (which gaps → Phase 1a/1b/2)
- Decision sign-off (who approved deferral)
- Impact assessment (if gap deferred, what compensating control added)

---

## Part 7: Recommendations

### Immediate Actions (Before Phase 1 Go-Live)
1. **Conduct gap review meeting** with architect + lead developer
   - Decide: Phase 1a (add now) vs Phase 1b (extend Phase 1) vs Phase 2 (defer)
   - Estimate effort for each add-now scenario

2. **Document decision** in PRD "Delivery Phases" section
   - "Gap from Brief → Added to Phase 1a per decision XYZ on 2026-02-27"
   - "Gap from Brief → Deferred to Phase 1b per RFC-123"

3. **Expand PRD for Phase 1a decisions**
   - Add 2–3 page sections for each decided gap
   - Include Acceptance Criteria for each new requirement

4. **Create validation checklist** for Phase 1 go-live
   - "Verify KatanaTransformer in use" [from GAP #1]
   - "Verify MTF kill-switch thresholds in config" [from GAP #4]
   - "Verify H4 cache independent" [from GAP #5]

### Before Phase 1b Scope Planning
1. **Prioritize Phase 1b from PRD deferred items**
   - Map: which deferred Brief gaps unblock which Phase 1b features

2. **Create Phase 1b PRD addendum**
   - Explicit list of new Epics/Stories for Phase 1b
   - Cross-reference to Brief (which Brief gaps now added)

3. **Update timeline estimates**
   - If adding gaps now → Phase 1 may extend 1–2 weeks
   - Plan Phase 1b accordingly

### Process Improvements
1. **Implement Brief-First Sync Rule**
   - Monthly: Brief changes → PRD review/update
   - Quarterly: Full gap analysis (like this report)

2. **Add to CI/CD**
   - Automated check: "Are all Brief sections referenced in PRD?"
   - Generate gap report on each PRD commit

3. **Document Canonical Hierarchy**
   - Add formal documentation of L1>L2>L3>L4 hierarchy
   - Define override procedures and escalation paths

---

## Appendix: Full Gap Item List

### CRITICAL Gaps (Phase 1 Blocking)
- [ ] 1. Mandatory Baseline (KatanaTransformer requirement)
- [ ] 2. Multi-Timeframe 6 caches (OHLCVStore backend specification)
- [ ] 3. MTF Independence Guarantee (NO cross-TF bias gating rule)
- [ ] 4. MTF Kill-Switch Logic (thresholds + metrics)
- [ ] 5. H4 Independent Cache (own Optuna study)
- [ ] 6. 115 Parameters Wave 4 (full taxonomy, 16 categories)
- [ ] 7. DFF Flat Parameter Structure (6 types, no variant_id)
- [ ] 8. DFF-Calendar Integration
- [ ] 9. Kill-Switch: 40% MaxDD (Individual Rocket)
- [ ] 10. Kill-Switch: 50% MaxDD (Portfolio/Rocket Bucket)

### HIGH Priority Gaps (Architectural Clarity)
- [ ] 11. Source of Truth Hierarchy (L1>L2>L3>L4 with sync rules)
- [ ] 12. Optuna with 8000 Trials (per-TF parallel specification)
- [ ] 13. HNSW Index Per Timeframe (artifact registry)
- [ ] 14. PostgreSQL OHLCVStore Backend (incremental ingestion)
- [ ] 15. Strategy Profiles Explicit Definition (objectives, constraints, promotion)
- [ ] 16. Max Leverage Cap 5x (hard limit enforcement)
- [ ] 17. Rollback Strategy (auto-rollback triggers + mechanism)

### MEDIUM Priority Gaps (Expansion)
- [ ] 18. Parameter Profiles System (active_param_count ≤ 70 invariant detail)
- [ ] 19. Capital Buckets (allocation rules, rebalancing)
- [ ] 20. Rockets VC Model (capital allocation algorithm)
- [ ] 21. Calendar Safety expansion (event database, news API)
- [ ] 22. Canonical Values Table (reproduce in PRD inline)

---

## Sign-Off

**Analysis Completed:** 2026-02-27 by Claude Code Analysis Agent
**Validation Scope:** Phase 1 Full Coverage (katana-vectorbt)
**Next Steps:** (1) Review with team, (2) Decide Phase 1a/1b/2 for each gap, (3) Update PRD accordingly

**Approvals Required:**
- [ ] Architect: Gap decision sign-off
- [ ] Lead Dev: Effort estimate validation
- [ ] PM: Timeline impact acknowledgment
- [ ] Author (NIKITA): Remediation plan approval

---

**End of Report**
