---
stepsCompleted: ['step-01-detect-mode', 'step-02-load-context', 'step-03-risk-and-testability', 'step-04-coverage-plan', 'step-05-generate-output']
lastStep: 'step-05-generate-output'
lastSaved: '2026-02-26'
workflowType: 'testarch-test-design'
mode: 'system-level'
project: 'katana-vectorbt'
inputDocuments:
  - 'katana-v-02-prd-katana-vectorbt-2026-01-18.md'
---

# TEA → BMAD Handoff: katana-vectorbt Test Design

**Purpose:** Bridge document between the test design outputs (Architecture + QA docs) and BMAD epic/story decomposition. Ensures test requirements are properly scheduled into implementation sprints.

**Date:** 2026-02-26
**From:** TEA Agent (testarch-test-design workflow)
**To:** BMAD Dev Agent / Sprint Planning
**Status:** Ready for BMAD integration

---

## Summary of Test Design Outputs

Two companion documents produced:

| Document | Location | Audience | Purpose |
|----------|----------|----------|---------|
| `test-design-architecture.md` | `_bmad-output/zone1/` | Architects + Dev Team | 28 risks, 11 high-priority, testability gaps, 5 blockers (B-001 to B-005) |
| `test-design-qa.md` | `_bmad-output/zone1/` | Dev/QA Engineer | ~180 tests across P0–P3, execution strategy, effort estimates |

---

## Blockers That Must Become Implementation Stories

These are pre-conditions for QA test development. Each should be a story in the current or next sprint:

| Blocker ID | Story Title | Priority | Epic Target | Blocks |
|------------|-------------|----------|-------------|--------|
| B-001 | Add `seed` parameter to all optimization, backtest, and Monte Carlo calls for deterministic reproducibility | P0 | Epic J | All integration tests asserting numeric results |
| B-002 | Add `ClockProtocol` injectable abstraction to `CalendarSafety` and `KatanaTransformer` | P0 | Wave 4 | All Calendar Safety integration tests |
| B-003 | Expose Optuna in-memory study factory as pytest fixture (`create_study(storage="in-memory", seed=N)`) | P0 | Epic J | All optimization pipeline integration tests |
| B-004 | Add `schema_version` field to all JSON artifacts (progress.json, events.ndjson, risk_flags.json, signal_quality.json, pa_patterns.json, optimizer_summary.json) | P0 | Epic J | Backward compatibility tests (FR0.2a) |
| B-005 | Add `--n-workers N` CLI flag to all mass_optimize commands (default=1 for CI) | P0 | Epic J | CI-safe optimization tests (prevents OOM) |

---

## Test Infrastructure Stories (New Work in `tests/` directory)

These are test development tasks that should be scheduled alongside implementation stories:

| Story | Sprint | Effort | Dependencies |
|-------|--------|--------|-------------|
| Create deterministic OHLCV fixtures for 6 TFs (frozen parquet files, SHA256-hashed) | Sprint 1 Epic J | 1 day | - |
| Implement `FakeClock` and `ClockProtocol` base classes in `tests/fixtures/` | Sprint 1 Epic J | 0.5 day | B-002 |
| Implement `ArtifactRegistry.validate_schema()` test utility | Sprint 2 Epic J | 0.5 day | B-004 |
| Implement `FakeRocketRegistry` test stub for circuit breaker tests | Wave 4 Sprint 1 | 1 day | - |
| Configure PostgreSQL test container in CI (GitHub Actions + Docker Compose) | Wave 4 Sprint 1 | 1 day | Wave 4 schema |
| Write P0 test suite (52 tests) — Signal Framework, Data Integrity, Quality Gates, Rollback | Sprint 2–3 Epic J | 3–4 weeks | B-001 through B-005 |
| Write P1 test suite (68 tests) — Optimization Pipeline, Wave 4, Risk Suite, Dashboard | Sprint 3–4 Epic J | 3–4 weeks | P0 infrastructure |
| Write P2/P3 tests (60 tests) — Edge cases, performance benchmarks | Sprint 4–5 Epic J | 2–3 weeks | P1 infrastructure |

---

## Risk Items for Epic/Story Acceptance Criteria

The following risks from the Architecture doc should be reflected in implementation story acceptance criteria. Dev stories must include these as explicit ACs to prevent regression:

### Must Include in Epic J Stories (FR-OPT-*)

1. **R-001 (Score 9):** Every optimization story must include: "DSR-adjusted Sharpe is the objective; raw IS Sharpe is NOT used."
2. **R-009 (Score 6):** Every parameter profile story must include: "`active_param_count ≤ 70` invariant enforced; trials violating this return TrialPruned before backtest runs."
3. **R-003 (Score 6):** Every backtest story must include: "`data_hash` (SHA256) recorded in Run Journal; `freeze_dataset()` called at backtest start."

### Must Include in Wave 4 Stories (FR-W4-*)

4. **R-007 (Score 6):** Every DFF story must include: "`prepare_features()` guarantees 0% NaN in all `dist_*` columns; `DataIntegrityError` raised if violated."
5. **R-015 (Score 4):** Every per-TF story must include: "0% parameter bleed from other TF studies confirmed by per-TF study name isolation (`_1m_`, `_5m_`, etc.)."
6. **R-008 (Score 6):** Every Calendar Safety story must include: "Pair-specific filtering validated — non-affected pairs unblocked; affected pairs blocked; MaxDD reduction ≥10%."

### Must Include in Rocket Portfolio Stories (FR-65 through FR-97)

7. **R-006 (Score 6):** Circuit breaker story must include: "Triggers within 60 seconds of 6+ simultaneous rocket deaths."
8. **R-021 (Score 4):** Wilson Score story must include: "N<50 → skip kill switch; N≥50 → apply LCB formula at 95% confidence."

### Must Include in All Stories (General)

9. **R-011 (Score 6):** All run-producing stories: "Artifact integrity check passes — SHA256 data_hash stored in Run Journal."
10. **R-010 (Score 6):** Rollback story: "Time-to-rollback ≤ 5 minutes; single CLI command restores last known-good champion."

---

## Coverage Gaps vs Phase 1 Dashboard Stories (1.1–1.5)

The PRD notes: "basic generator exists but doesn't cover AC Phase 1 — Static HTML Report Artifact (Story 1.1–1.5)."

QA test plan includes these gaps in P1-DASH-001 through P1-DASH-004. The following ACs from FR1–FR8 are NOT yet covered by existing tests:

| AC Gap | FR | Test | Status |
|--------|-----|------|--------|
| Net P&L prominently displayed with correct calculation | FR1 | P1-DASH-001 | Not tested |
| Profit Factor calculated from loaded JSON (no backend) | FR2 | P1-DASH-001 | Not tested |
| Cost impact breakdown (commissions + slippage + market impact) | FR3 | P1-DASH-001 | Not tested |
| schema_version parsing + fallback warning for v1.0 artifacts | FR0.2a | P1-DASH-002 | Not tested |
| Parameter comparison 2–5 runs side-by-side with diff highlighting | FR7 | P1-DASH-004 | Not tested |
| Data export in 3 formats | FR8 | P1-DASH-003 | Not tested |

**Action:** Add story to Phase 1 Dashboard epic: "Close AC gaps for FR1–FR8 and add tests P1-DASH-001 through P1-DASH-004."

---

## Execution Timeline Recommendation

| Phase | Timeline | Tests | Focus |
|-------|----------|-------|-------|
| Sprint 1 (Epic J kickoff) | Week 1–2 | Infrastructure setup + B-001 to B-005 | Blockers resolved; test fixtures created |
| Sprint 2 (Epic J implementation) | Week 3–6 | ~52 P0 tests written | Signal correctness, data integrity, offline gates |
| Sprint 3 (Epic J integration) | Week 7–10 | ~68 P1 tests written | Optimization pipeline, Wave 4, risk suite |
| Sprint 4 (Wave 4 + Dashboard) | Week 11–14 | ~38 P2 + 22 P3 tests | Edge cases, performance benchmarks |
| Weekly (ongoing) | Ongoing | Full regression | 350+ existing + 180 new = 530+ total |

---

## Quality Gates for BMAD Sprint Planning

Use these as Definition of Done (DoD) gates for Epic J and Wave 4 stories:

- [ ] DSR ≥ 0.95 for any promoted strategy (offline validation in CI)
- [ ] PBO < 0.50 for any promoted strategy
- [ ] WF degradation ≤ 15% (OOS vs IS)
- [ ] MaxDD ≤ 25% at portfolio level
- [ ] 0% data leakage detected (automated leakage detection suite)
- [ ] 0% NaN in `dist_*` columns after `prepare_features()`
- [ ] `active_param_count ≤ 70` for 100% of trials
- [ ] Time-to-rollback ≤ 5 minutes
- [ ] All P0 tests passing in CI before any story merges to main
- [ ] Circuit breaker triggers within 60s in integration test

---

**End of Handoff Document**

**Next steps for BMAD Sprint Planning:**
1. Convert B-001 through B-005 into implementation stories for Sprint 1.
2. Add test infrastructure stories to Sprint 1 backlog.
3. Add risk ACs from this handoff into relevant Epic J and Wave 4 story acceptance criteria.
4. Schedule P0 test development alongside implementation (not after) to enable continuous validation.
5. Configure nightly and weekly CI jobs for performance + Wave 4 regression.
