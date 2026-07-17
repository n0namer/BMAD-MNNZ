---
title: "Requirements Traceability Matrix"
date: 2026-02-27
scope: phase1_full
matrix_type: brief_to_prd
---

# Requirements Traceability Matrix: Brief → PRD

**Purpose:** Map each Brief requirement to its PRD coverage level and identify gaps.
**Format:** Brief Requirement | Brief Section | PRD Status | PRD Section | Gap Type | Severity

---

## CRITICAL REQUIREMENTS

### 1. Mandatory Baseline Requirement
| Field | Value |
|-------|-------|
| **Brief Requirement** | ALL testing/optimization/validation MUST use KatanaTransformer (docs/KATANA_ORIGINAL.md source, katana/katana_transformer.py implementation) |
| **Brief Section** | Executive Summary → ⚠️ MANDATORY BASELINE REQUIREMENT (BLOCKING) |
| **PRD Status** | ✗ NOT FOUND |
| **PRD Section** | Not referenced |
| **Gap Type** | Missing functional requirement |
| **Severity** | 🔴 CRITICAL |
| **Acceptance Criteria (from Brief)** | Script must instantiate KatanaTransformer class; rejected if using raw RSI/MA/simple indicators |
| **PRD Acceptance Criteria** | Not defined |
| **Remediation** | ADD: FR-001 (Mandatory Baseline Validation) - "System MUST reject any optimization/backtest that does not use KatanaTransformer.transform() in the trading logic" |
| **Effort** | 4 hours (spec + test case) |
| **Phase** | 1a (before go-live) |

### 2. Multi-Timeframe 6 Independent Caches
| Field | Value |
|-------|-------|
| **Brief Requirement** | 6 independent timeframe caches (1m, 5m, 15m, 1h, 4h, 1d) using PostgreSQL OHLCVStore backend with incremental ingestion; each TF has isolated Optuna study, HNSW index, artifact registry |
| **Brief Section** | Wave 4 Features: Multi-Timeframe Caching & Venture Capital Model |
| **PRD Status** | ⚠️ PARTIALLY MENTIONED |
| **PRD Section** | Multi-Timeframe Trading Architecture (mentions 6 TF but not backend/ingestion details) |
| **Gap Type** | Incomplete architectural specification |
| **Severity** | 🔴 CRITICAL |
| **Backend Detail in Brief** | PostgreSQL OHLCVStore, incremental ingestion (append-only), snapshot hash, per-TF independent caches |
| **Backend Detail in PRD** | Not mentioned; implementation may default to CSV/Parquet |
| **Remediation** | ADD: Section 3.2 (Data Architecture) - "PostgreSQL OHLCVStore with 6 independent cache tables; incremental ingestion with snapshot_hash validation; isolation enforced at schema level" |
| **Effort** | 8 hours (schema spec + migration plan) |
| **Phase** | 1a (critical for data pipeline) |

### 3. MTF Independence Guarantee
| Field | Value |
|-------|-------|
| **Brief Requirement** | NO cross-timeframe bias gating by default (v1.0); each TF trades independently; no HTF→LTF blocking, directional bias inheritance, or netting restrictions |
| **Brief Section** | MTF Independence Guarantee section |
| **PRD Status** | ✗ NOT FOUND |
| **PRD Section** | MTF mentioned but no independence rule stated |
| **Gap Type** | Missing design constraint |
| **Severity** | 🔴 CRITICAL |
| **Design Rule in Brief** | "Default (v1.0): NO cross-timeframe bias gating. Each timeframe trades independently with its own signals and risk management." |
| **Design Rule in PRD** | Not stated; may be violated by implementation |
| **Remediation** | ADD: Architecture → Design Constraints: "NFR-020: By default, each timeframe operates in isolation mode (no HTF→LTF bias transmission, no netting). Cross-TF rules are ONLY applied if explicitly enabled via strategy_profile.mtf_confirmation_mode." |
| **Effort** | 6 hours (constraint spec + validation) |
| **Phase** | 1a (guards against design regression) |

### 4. MTF Kill-Switch Logic
| Field | Value |
|-------|-------|
| **Brief Requirement** | Monitor mtf_block_rate, mtf_delta_DSR_vs_none, mtf_shadow_pnl_blocked; if thresholds exceeded → auto-rollback to "soft_penalty" or "none"; mtf_block_rate_max threshold; kill-switch metrics mandatory |
| **Brief Section** | MTF Conflict Resolution Rules (Consolidated) → Kill-switch logic |
| **PRD Status** | ⚠️ VAGUELY MENTIONED |
| **PRD Section** | Risk Mitigation Strategies (high-level but no specific thresholds or metrics) |
| **Gap Type** | Incomplete specification |
| **Severity** | 🔴 CRITICAL |
| **Metrics in Brief** | mtf_block_rate (%), mtf_delta_DSR_vs_none (basis points), mtf_shadow_pnl_blocked ($) |
| **Metrics in PRD** | Not explicitly defined |
| **Thresholds in Brief** | mtf_block_rate_max (value not stated, implied ~50%), mtf_delta_DSR_vs_none < 0 |
| **Thresholds in PRD** | Not stated |
| **Remediation** | ADD: NFR-021 (MTF Kill-Switch): "(1) Compute mtf_block_rate as % of signals blocked; (2) Compute mtf_delta_DSR_vs_none as DSR(with blocks) - DSR(no blocks); (3) Monitor mtf_shadow_pnl_blocked; (4) If mtf_block_rate > 50% OR mtf_delta_DSR_vs_none < -50bp → trigger auto-rollback, log RCA, reset mtf_confirmation_mode to 'none'" |
| **Effort** | 12 hours (metric implementation + monitoring) |
| **Phase** | 1a (blocks go-live without this) |

### 5. H4 Independent Cache
| Field | Value |
|-------|-------|
| **Brief Requirement** | H4 is NOT special; it is ONE OF 6 independent TF caches with own Optuna study; may optionally act as volatility anchor via dff_h4_override_enabled flag; does NOT block other TF by default |
| **Brief Section** | H4 Role Canonical Definition |
| **PRD Status** | ✗ NOT FOUND |
| **PRD Section** | Mentioned in "Multi-Timeframe Trading" but H4 role not explicitly defined |
| **Gap Type** | Missing role specification |
| **Severity** | 🔴 CRITICAL |
| **Brief Role Definition** | H4 is peer TF (like 1m, 5m, etc.); independent cache; optional volatility reference only if enabled |
| **PRD Role** | Implicit legacy behavior (H4 as dominant higher timeframe?) |
| **Remediation** | ADD: FR-018 (H4 Role Definition): "H4 is a standard timeframe cache (identical to 1m/5m/15m/1h/1d); has its own Optuna study and HNSW index; does NOT authorize or block other TF signals by default; if dff_h4_override_enabled=true, H4 may provide volatility anchor (ATR(H4,14) etc.) for DFF calculations on lower TF, but this is opt-in only" |
| **Effort** | 4 hours (spec + code review) |
| **Phase** | 1a (design correctness) |

### 6. 115 Parameters Wave 4 (Full Taxonomy)
| Field | Value |
|-------|-------|
| **Brief Requirement** | Complete 115-parameter taxonomy across 16 categories; per-parameter type definitions, ranges, conditional dependencies, per-profile active_param_count limits |
| **Brief Section** | Canonical Values Table + 115 Parameters Across 16 Categories |
| **PRD Status** | ⚠️ MENTIONED but NOT DETAILED |
| **PRD Section** | "Wave 4 Features Epic (100+ parameters)" but missing complete taxonomy |
| **Gap Type** | Incomplete specification |
| **Severity** | 🔴 CRITICAL |
| **Parameter Categories in Brief** | Entry signals, exit signals, DFF, risk, calendar, news, rockets, volatility, trend, mean reversion, ... (16 total) |
| **Parameter Categories in PRD** | Not enumerated |
| **Valid Ranges in Brief** | Per-parameter ranges (e.g., RSI period 5–50, MA period 5–200, leverage 0.1–5.0) |
| **Valid Ranges in PRD** | Not specified |
| **Remediation** | ADD: Appendix A (Parameter Taxonomy Table): 115 rows with [param_name, category, type, range_min, range_max, profile_availability, description] |
| **Effort** | 16 hours (spec + table creation + validation rules) |
| **Phase** | 1a (required for Optuna search space) |

### 7. DFF Flat Parameter Structure
| Field | Value |
|-------|-------|
| **Brief Requirement** | DFF has 6 types (atr, stddev, bb_half, range, fixed_pct, corwin_schultz); NO variant_id or dict; type is categorical with per-role flat params (e.g., type=="atr": [length, multiplier]); validation contract per type |
| **Brief Section** | Distance Function Factory (DFF) — Flat Parameter Structure |
| **PRD Status** | ⚠️ MENTIONED but NOT DETAILED |
| **PRD Section** | DFF mentioned in risk section but flat structure not defined |
| **Gap Type** | Incomplete specification |
| **Severity** | 🔴 CRITICAL |
| **DFF Types in Brief** | 6 types with explicit contracts (e.g., atr requires length ∈ [5,50], multiplier ∈ [0.5,5.0]) |
| **DFF Types in PRD** | Not enumerated |
| **Wave 3 vs Wave 4 Migration** | Brief specifies variant_id REMOVED; PRD doesn't mention this breaking change |
| **Remediation** | ADD: Section 3.3 (DFF Specification): "[6 DFF Type Tables showing type, required_params, valid_ranges, per-role_overrides, examples]" |
| **Effort** | 12 hours (spec + table + migration notes) |
| **Phase** | 1a (critical for strategy encoding) |

### 8. DFF-Calendar Integration
| Field | Value |
|-------|-------|
| **Brief Requirement** | DFF integrated into both HARD (120/60 min) and SOFT (30/30 min news) calendar safety layers; DFF can override calendar parameters per-role |
| **Brief Section** | Calendar Safety & DFF Integration |
| **PRD Status** | ✗ NOT FOUND |
| **PRD Section** | Calendar Safety and DFF mentioned separately but no integration spec |
| **Gap Type** | Missing integration specification |
| **Severity** | 🔴 CRITICAL |
| **Integration Rule in Brief** | DFF multipliers apply to calendar event buffer widths; e.g., if dff_type=="bb_half" and bb_width=50bp, calendar buffer = 50bp (instead of fixed 120min) |
| **Integration Rule in PRD** | Not stated; DFF and calendar may conflict |
| **Remediation** | ADD: NFR-022 (DFF-Calendar Integration): "DFF parameters (esp. volatility-based types) can dynamically adjust calendar buffer widths; reconciliation logic ensures event buffers >= critical_threshold; precedence: critical_threshold > dff_override > default" |
| **Effort** | 10 hours (spec + integration logic) |
| **Phase** | 1a (guards against DFF-calendar conflict) |

### 9. Kill-Switch: 40% MaxDD (Individual Rocket)
| Field | Value |
|-------|-------|
| **Brief Requirement** | Rockets (individual strategy) with MaxDD ≥ 40% (peak-to-trough on equity curve after fees/slippage) → immediate stop + blacklist |
| **Brief Section** | Canonical Values Table: Rockets Kill-Switch (Individual) |
| **PRD Status** | ⚠️ VAGUELY MENTIONED |
| **PRD Section** | Risk Mitigation (high-level) but 40% threshold not explicit |
| **Gap Type** | Missing threshold specification |
| **Severity** | 🔴 CRITICAL |
| **Threshold in Brief** | 40% MaxDD (explicit) |
| **Threshold in PRD** | Not stated |
| **Remediation** | ADD: NFR-023 (Individual Rocket Kill-Switch): "For each rocket (strategy_profile=='rocket'), monitor equity curve MaxDD; if MaxDD >= 40% (peak-to-trough after fees/slippage), immediately: (1) stop new trades, (2) close open positions, (3) add to blacklist (skip re-optimization for N periods), (4) notify operator with RCA" |
| **Effort** | 6 hours (monitoring + stop logic) |
| **Phase** | 1a (risk control) |

### 10. Kill-Switch: 50% MaxDD (Portfolio/Rocket Bucket)
| Field | Value |
|-------|-------|
| **Brief Requirement** | Rockets (portfolio/bucket level) with MaxDD ≥ 50% (peak-to-trough of rocket bucket NAV, NOT total portfolio) → freeze + rebalance + RCA |
| **Brief Section** | Canonical Values Table: Rockets Kill-Switch (Portfolio) |
| **PRD Status** | ✗ NOT FOUND |
| **PRD Section** | Risk section mentions portfolio but not 50% threshold |
| **Gap Type** | Missing threshold specification |
| **Severity** | 🔴 CRITICAL |
| **Threshold in Brief** | 50% MaxDD at rocket bucket level (explicit) |
| **Threshold in PRD** | Not stated |
| **Remediation** | ADD: NFR-024 (Rocket Bucket Kill-Switch): "Monitor rocket bucket NAV (NOT total portfolio NAV); if MaxDD >= 50%, immediately: (1) freeze new rocket trades, (2) trigger rebalance_action (reallocate from other buckets or close losers), (3) initiate RCA, (4) notify operator; resume trades only after manual approval or N-period cooling off" |
| **Effort** | 8 hours (portfolio monitoring + rebalance logic) |
| **Phase** | 1a (portfolio-level risk control) |

---

## HIGH-PRIORITY REQUIREMENTS

### 11. Source of Truth Hierarchy
| Field | Value |
|-------|-------|
| **Brief Requirement** | L1 (Brief) > L2 (PRD/Architecture) > L3 (Code) > L4 (Derivatives); sync rules defined; Brief canonical override rule: Brief wins on conflict |
| **Brief Section** | Canonical Hierarchy (Documentation Structure) |
| **PRD Status** | ⚠️ MENTIONED but NO OPERATIONAL RULES |
| **PRD Section** | References "Canonical Override Rule" but doesn't define hierarchy |
| **Gap Type** | Vague governance |
| **Severity** | 🟡 HIGH |
| **Hierarchy in Brief** | 4-level with explicit sync rules and escalation |
| **Hierarchy in PRD** | Implicit "Brief overrides PRD" but no operational procedures |
| **Remediation** | ADD: Section 1 (Governance): "This PRD is synchronized under the Product Brief. Brief = L1 source of truth; PRD = L2 derived specs; code = L3 ground truth for implementation. On conflict: (1) Brief section overrides PRD section, (2) PRD must file correction PR to Brief if implementation differs, (3) monthly sync check" |
| **Effort** | 4 hours (governance doc) |
| **Phase** | 1a (document process) |

### 12. Optuna with 8000 Trials (Per-TF Parallel)
| Field | Value |
|-------|-------|
| **Brief Requirement** | 8000 trials per timeframe, all 6 TF in parallel, conditional search space (define-by-run), QMC init for first 32 trials |
| **Brief Section** | Canonical Values Table (8000 trials); Wave 4 Features |
| **PRD Status** | ⚠️ MENTIONED in Epic but not DETAILED |
| **PRD Section** | "Wave 4 Features Epic" mentions 8000 but not per-TF allocation or parallel model |
| **Gap Type** | Incomplete specification |
| **Severity** | 🟡 HIGH |
| **Trial Allocation in Brief** | 8000 per TF (implied) |
| **Trial Allocation in PRD** | "8000 trials" but unclear if 8000 total or per-TF |
| **Parallel Model in Brief** | All 6 TF run in parallel (mentioned but not detailed) |
| **Parallel Model in PRD** | Not specified; may run sequentially |
| **Remediation** | ADD: NFR-025 (Optimization Budget): "Per timeframe: 8000 trials maximum per run; all 6 TF optimizations execute in parallel using multiprocessing.Pool(6); total elapsed time = max(TF_1_time, ..., TF_6_time); pruning strategy: Median rule after 100 trials; stopping criterion: if no improvement > 1% over 500 trials → stop early" |
| **Effort** | 10 hours (parallelization + pruning logic) |
| **Phase** | 1a (critical for performance) |

### 13. HNSW Index Per Timeframe
| Field | Value |
|-------|-------|
| **Brief Requirement** | Each TF has artifact registry with HNSW vector index; 150x-12,500x faster search vs brute-force; configurable dimensions/ef_construction |
| **Brief Section** | MTF Independence Guarantee (mentions HNSW index) |
| **PRD Status** | ✗ NOT FOUND |
| **PRD Section** | Not mentioned |
| **Gap Type** | Missing technical specification |
| **Severity** | 🟡 HIGH |
| **HNSW Purpose in Brief** | Fast artifact similarity search (parameter fingerprints, performance profiles) |
| **HNSW in PRD** | Not mentioned; artifact lookup may be slow |
| **Remediation** | ADD: NFR-026 (Artifact Index): "Each TF maintains HNSW vector index on artifact fingerprints (parameter vector embedding, 768-dim ); index built after every 100 trials; search query: find K=5 similar past trials; latency target: <100ms per search; ef_construction=200, ef_search=100" |
| **Effort** | 8 hours (HNSW integration) |
| **Phase** | 1b (performance optimization, not blocking) |

### 14. PostgreSQL OHLCVStore Backend
| Field | Value |
|-------|-------|
| **Brief Requirement** | PostgreSQL with OHLCVStore extension/schema; incremental ingestion (append-only); snapshot hash for data integrity; per-TF independent caches |
| **Brief Section** | Multi-Timeframe Trading Architecture → Wave 4 Capabilities |
| **PRD Status** | ✗ NOT FOUND |
| **PRD Section** | Data architecture not specified |
| **Gap Type** | Missing data architecture |
| **Severity** | 🟡 HIGH |
| **Backend in Brief** | PostgreSQL OHLCVStore with incremental ingestion |
| **Backend in PRD** | Not mentioned; could default to Parquet/HDF5 |
| **Remediation** | ADD: Section 3.1 (Data Architecture): "Data backend: PostgreSQL 13+ with OHLCVStore extension; 6 independent cache tables (ohlcv_1m, ohlcv_5m, ..., ohlcv_1d); ingestion: append-only with snapshot_hash versioning; retention: all historical snapshots; queries: index on (symbol, timestamp)" |
| **Effort** | 12 hours (schema design + migration + ingestion pipeline) |
| **Phase** | 1a (required before data ingestion) |

### 15. Strategy Profiles Explicit Definition
| Field | Value |
|-------|-------|
| **Brief Requirement** | 3 profiles (stable, return, rocket) with explicit objective functions, constraints, promotion rules, active_param_count ranges |
| **Brief Section** | Strategy Profiles (Goal Axis) + Parameter Profiles System |
| **PRD Status** | ⚠️ MENTIONED but VAGUE on constraints/promotion |
| **PRD Section** | "Strategy Profiles" section but missing thresholds |
| **Gap Type** | Incomplete specification |
| **Severity** | 🟡 HIGH |
| **Profile Definition in Brief** | stable: robustness >> returns, constraint: DD < 20%, return: Sharpe > 1.0, rocket: win_rate 40–55% |
| **Profile Definition in PRD** | Profiles described but thresholds not precise |
| **Remediation** | ADD: Table (Strategy Profile Specifications): [stable: objective=minimize_dd, constraints=[dd_max=20%, leverage_max=2x, active_params=10–25], promotion_rule=pass_walk_forward_and_3m_live], [return: objective=maximize_sharpe, constraints=[dd_max=30%, sharpe_min=1.0, leverage_max=3x, active_params=25–50], promotion_rule=pass_walk_forward_and_6m_live], [rocket: objective=maximize_cagr, constraints=[dd_max=60%, leverage_max=5x, active_params=40–70], promotion_rule=only_in_rocket_bucket] |
| **Effort** | 6 hours (spec + validation) |
| **Phase** | 1a (required for profile orchestration) |

### 16. Max Leverage Cap 5x (Hard Limit)
| Field | Value |
|-------|-------|
| **Brief Requirement** | Hard cap of 5x leverage across all profiles unless exchange limit lower |
| **Brief Section** | Canonical Values Table: Max Leverage Cap |
| **PRD Status** | ⚠️ MENTIONED but NOT EXPLICIT |
| **PRD Section** | Risk section discusses leverage but 5x not stated as hard cap |
| **Gap Type** | Missing explicit constraint |
| **Severity** | 🟡 HIGH |
| **Cap in Brief** | 5x (explicit hard limit) |
| **Cap in PRD** | Implicit, not enforced |
| **Remediation** | ADD: NFR-027 (Leverage Hard Cap): "INVARIANT: all open positions sum to ≤ 5x notional leverage (or exchange limit if lower); enforcement: pre-trade check in order submission; if leverage would exceed 5x, reject trade with error LOG_LEVERAGE_EXCEEDED; monitor: daily leverage report" |
| **Effort** | 4 hours (pre-trade check logic) |
| **Phase** | 1a (risk control) |

### 17. Rollback Strategy (Auto-Rollback Triggers)
| Field | Value |
|-------|-------|
| **Brief Requirement** | Auto-rollback triggers: (1) MTF kill-switch, (2) individual 40% MaxDD, (3) calendar conflict, (4) data quality; mechanism: restore last known-good snapshot |
| **Brief Section** | Rollback & Data Migration Strategy |
| **PRD Status** | ⚠️ MENTIONED in Risk but NOT systemic |
| **PRD Section** | "Risk Mitigation" but no explicit rollback section |
| **Gap Type** | Incomplete specification |
| **Severity** | 🟡 HIGH |
| **Rollback Triggers in Brief** | 4 explicit triggers with conditions |
| **Rollback Triggers in PRD** | Vague ("mitigated by rollback") |
| **Remediation** | ADD: Section 4 (Operations) → Subsection (Rollback): "Trigger conditions: [trigger_1: mtf_kill_switch activated], [trigger_2: rocket_equity_maxdd >= 40%], [trigger_3: calendar_event_overlap], [trigger_4: data_hash_mismatch]; mechanism: restore snapshot_id from previous known-good run; procedure: (1) stop new trades, (2) close open positions, (3) restore data, (4) reset optimization state, (5) notify operator; approval: operator signs off before resume" |
| **Effort** | 10 hours (rollback logic + snapshot mgmt) |
| **Phase** | 1b (operational, important but not blocking MVP) |

---

## MEDIUM-PRIORITY REQUIREMENTS (WITH GAPS)

| Requirement | Brief Section | PRD Status | Gap | Severity | Remediation Effort |
|-------------|---------------|-----------|-----|----------|-------------------|
| Parameter Profiles (active_param_count ≤ 70) | Parameter Profiles System | ⚠️ Mentioned | Missing active_param_count invariant detail | 🟠 MEDIUM | 4h |
| Capital Buckets (core + rocket) | Capital Buckets | ⚠️ Mentioned | Missing allocation rules, rebalancing | 🟠 MEDIUM | 6h |
| Rockets VC Model | Rockets Venture Capital Model | ⚠️ Mentioned | Missing allocation algorithm, schedule | 🟠 MEDIUM | 8h |
| Calendar Safety HARD (120/60 min) | Calendar Safety & DFF Integration | ⚠️ Mentioned | Missing event database, detection logic | 🟠 MEDIUM | 8h |
| Calendar Safety SOFT (30/30 min) | Calendar Safety & DFF Integration | ⚠️ Mentioned | Missing news API integration, toggle logic | 🟠 MEDIUM | 10h |
| Canonical Values Table | Canonical Values Table (Wave 4 SoT) | ⚠️ Referenced | Not reproduced in PRD; external reference | 🟠 MEDIUM | 2h |

---

## SUMMARY

### Gap Tally
- **CRITICAL Gaps:** 10 items (average remediation effort: 7.8 hours)
- **HIGH Gaps:** 7 items (average remediation effort: 8.4 hours)
- **MEDIUM Gaps:** 6 items (average remediation effort: 6.3 hours)
- **Total Effort:** ~128 hours

### Phase 1a Effort (Blocking Go-Live)
- KatanaTransformer requirement: 4h
- MTF OHLCVStore: 8h
- MTF Independence rule: 6h
- MTF Kill-Switch: 12h
- H4 role: 4h
- 115 Parameters: 16h
- DFF Flat Structure: 12h
- DFF-Calendar: 10h
- Kill-Switch 40%: 6h
- Kill-Switch 50%: 8h
- Governance: 4h
- Optuna 8000/parallel: 10h
- Leverage cap: 4h
- Strategy profiles: 6h
- **TOTAL PHASE 1a: ~110 hours** (Note: can be parallelized; estimate actual: 3–5 weeks if team of 3)

### Phase 1b Effort (Deferred)
- HNSW Index: 8h
- PostgreSQL OHLCVStore: 12h
- Rollback: 10h
- Capital allocation: 6h
- Calendar events: 8h
- News API: 10h
- **TOTAL PHASE 1b: ~54 hours** (1–2 weeks if 1 developer)

---

**Report Generated:** 2026-02-27
**Next Review:** After team decision on Phase 1a/1b scope

