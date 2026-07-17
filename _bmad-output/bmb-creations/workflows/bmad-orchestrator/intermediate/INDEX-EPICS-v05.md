# Katana V05 - Epic Planning Index

**Created:** 2026-02-26  
**Status:** READY FOR SPRINT PLANNING  
**Total Coverage:** 5 Epics, 25 Stories, 122 Story Points

---

## Quick Navigation

### Primary Document
**File:** `katana-v-05-epics.md`
- Complete epic definitions
- 25 detailed stories
- Acceptance criteria, story points, dependencies
- Delivery artifacts for each story

### Summary & Execution Plan
**File:** `EPICS-CREATION-SUMMARY.md`
- Executive summary
- Recommended execution sequence (5 phases)
- Quality standards
- Next steps

---

## Epic Structure

All 5 epics follow consistent structure:
- **Description:** Clear purpose and scope
- **Acceptance Criteria:** 1-5 per epic
- **Stories:** 5 stories per epic
- **Dependencies:** Inter-epic and inter-story
- **Deliverables:** Specific files/components
- **Test Requirements:** Minimum coverage

---

## Quick Epic Reference

| Epic | Blocker | Priority | Stories | Points | Focus |
|------|---------|----------|---------|--------|-------|
| E-STRATEGY-LIFECYCLE | BLOCKER-1 | CRITICAL | 5 | 34 | State machine, approvals |
| E-JOURNAL-SCHEMA | BLOCKER-2 | CRITICAL | 5 | 40 | Data layer, schema |
| E-TELEMETRY-METRICS | BLOCKER-3 | HIGH | 5 | 30 | Metrics tracking |
| E-COMPARE-WORKFLOW | BLOCKER-4 | HIGH | 5 | 25 | Run comparison |
| E-AUDIT-TRAIL | BLOCKER-5 | HIGH | 5 | 25 | Auditability |

---

## Story Reference (Quick Lookup)

### E-STRATEGY-LIFECYCLE
1. S-STRATEGY-001: State machine transitions (13 pts)
2. S-STRATEGY-002: Approval workflow (8 pts)
3. S-STRATEGY-003: Kill-switch mechanism (5 pts)
4. S-STRATEGY-004: State timeline (5 pts)
5. S-STRATEGY-005: Rejection/resubmit logic (3 pts)

### E-JOURNAL-SCHEMA
1. S-JOURNAL-001: manifest.json structure (8 pts)
2. S-JOURNAL-002: summary.json v3.0 (10 pts)
3. S-JOURNAL-003: events.ndjson (8 pts)
4. S-JOURNAL-004: Postgres schema (8 pts)
5. S-JOURNAL-005: Reproducibility verifier (6 pts)

### E-TELEMETRY-METRICS
1. S-TELEMETRY-001: Time-to-Status instrumentation (6 pts)
2. S-TELEMETRY-002: MTIF calculation (6 pts)
3. S-TELEMETRY-003: Log Diving Rate (6 pts)
4. S-TELEMETRY-004: Metrics dashboard (8 pts)
5. S-TELEMETRY-005: Alert rules (4 pts)

### E-COMPARE-WORKFLOW
1. S-COMPARE-001: Comparison algorithm (7 pts)
2. S-COMPARE-002: Run selection UI (5 pts)
3. S-COMPARE-003: Delta visualization (6 pts)
4. S-COMPARE-004: Metric selection (4 pts)
5. S-COMPARE-005: Export functionality (3 pts)

### E-AUDIT-TRAIL
1. S-AUDIT-001: Audit trail collection (6 pts)
2. S-AUDIT-002: Verification algorithm (7 pts)
3. S-AUDIT-003: Audit UI (6 pts)
4. S-AUDIT-004: Reproduce Run button (4 pts)
5. S-AUDIT-005: Diagnostic tool (2 pts)

---

## Recommended Reading Order

**For Architects:**
1. E-STRATEGY-LIFECYCLE (Epic 1) → system design patterns
2. E-JOURNAL-SCHEMA (Epic 2) → data architecture
3. E-AUDIT-TRAIL (Epic 5) → system verification

**For Product Managers:**
1. EPICS-CREATION-SUMMARY.md → timeline and phases
2. All epics → user-facing features
3. Dependencies chart → release planning

**For Developers:**
1. katana-v-05-epics.md → detailed specs
2. Story point estimates → capacity planning
3. Delivery artifacts → implementation targets

**For QA/Test:**
1. All stories → test requirement review
2. Acceptance criteria → test case development
3. Test coverage targets → test plan creation

---

## Key Metrics Dashboard

```
Total Work:           122 story points
Est. Timeline:        12-16 weeks
Team Capacity Req:    6-8 engineers
Critical Path:        E-STRATEGY-LIFECYCLE → (E-JOURNAL-SCHEMA || E-TELEMETRY-METRICS) → ...
Phase Duration:       ~3 weeks per phase (with parallelization)
Min. Test Coverage:   125+ unit tests
Quality Gates:        All acceptance criteria + test coverage
```

---

## Dependency Map

```
Foundation (Weeks 1-5)
├─ E-STRATEGY-LIFECYCLE ←─┐
│  ├─ S-STRATEGY-001     │
│  ├─ S-STRATEGY-002     │
│  ├─ S-STRATEGY-003     │
│  ├─ S-STRATEGY-004     │
│  └─ S-STRATEGY-005     │
│                        │
└─ E-JOURNAL-SCHEMA      │
   ├─ S-JOURNAL-001      │
   ├─ S-JOURNAL-002      │
   ├─ S-JOURNAL-003      │
   ├─ S-JOURNAL-004      │
   └─ S-JOURNAL-005      │
                         │
Analysis Layer (Weeks 6-13)
├─ E-TELEMETRY-METRICS ──┘ [depends on both Foundation epics]
├─ E-COMPARE-WORKFLOW ────→ [depends on E-JOURNAL-SCHEMA]
└─ E-AUDIT-TRAIL ─────────→ [depends on E-JOURNAL-SCHEMA + E-STRATEGY-LIFECYCLE]
```

---

## Sprint Planning Template

### Sprint N: E-STRATEGY-LIFECYCLE
**Capacity:** {X} story points / 2 weeks
**Stories:**
- [ ] S-STRATEGY-001 (13 pts) - CRITICAL
- [ ] S-STRATEGY-002 (8 pts) - HIGH
- [ ] S-STRATEGY-003 (5 pts) - HIGH
- [ ] S-STRATEGY-004 (5 pts) - MEDIUM
- [ ] S-STRATEGY-005 (3 pts) - MEDIUM

**Deliverables:**
- State machine implementation
- Approval workflow service
- Kill-switch handler
- Timeline visualization
- Resubmission logic

---

## Global Memory Reference

**Key:** `swarm:docs:epics-updated`
**Namespace:** `shared-knowledge`
**Content:** Epic creation tracking and metadata

This document and all supporting files are automatically synchronized to the global knowledge base for cross-project visibility and reuse.

---

## Quality Standards

Each story verified for:
- ✓ Acceptance criteria completeness
- ✓ Story point reasonableness
- ✓ Dependency clarity
- ✓ Test requirement specification
- ✓ Artifact clarity

Each epic verified for:
- ✓ Complete story set (5 stories)
- ✓ Total point range (25-40 points)
- ✓ Test coverage requirements (25+ tests)
- ✓ Clear success criteria

---

## Version History

| Version | Date | Status | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-26 | ACTIVE | Initial creation - 5 epics, 25 stories |

---

## Contact & Support

**Questions about epics?**
- Review `katana-v-05-epics.md` for detailed information
- Check dependencies section for story relationships
- See EPICS-CREATION-SUMMARY.md for execution guidance

**Need to modify epics?**
- Keep story points consistent with complexity
- Update dependencies when changing scope
- Maintain acceptance criteria completeness
- Update test coverage requirements

---

**Document Created:** 2026-02-26
**Last Updated:** 2026-02-26
**Status:** READY FOR SPRINT PLANNING

---

**Quick Links:**
- Primary Document: [katana-v-05-epics.md](./katana-v-05-epics.md)
- Summary & Plan: [EPICS-CREATION-SUMMARY.md](./EPICS-CREATION-SUMMARY.md)
- This Index: [INDEX-EPICS-v05.md](./INDEX-EPICS-v05.md)
