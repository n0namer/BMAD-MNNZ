# Milestone Variance Calculation

## Timeline Variance

**Formula:**
```
Variance (days) = Actual Completion Date - Planned Completion Date
Variance (%) = (Variance in days / Planned Duration) × 100
```

**Example:**
- Planned: 14 days (Feb 1 - Feb 15)
- Actual: 18 days (Feb 1 - Feb 19)
- Variance: +4 days (+28%)

**Thresholds:**
- ≤30% → Acceptable (PASS)
- 30-50% → Warning (ADJUST)
- >50% → Critical (ESCALATE)

---

## Scope Variance

**Categories:**
- **Added:** New items not in original plan
- **Removed:** Items descoped
- **Deferred:** Items pushed to later milestone

**Analysis Questions:**
- Why did scope change?
- Was change justified?
- How does it affect remaining milestones?
- Should original plan be revised?

---

## Quality Variance

**Assessment Areas:**
- **Meets Quality Standards:** ✅ Yes / ⚠️ Needs Improvement / ❌ No
- **Technical Debt Introduced:** None / Low / Medium / High
- **Rework Required:** None / Minor / Major

**Quality Impact on Gate Decision:**
- High technical debt → Consider ADJUST even if timeline met
- Major rework required → May trigger ESCALATE
- Quality standards not met → Cannot PASS

---

## Root Cause Categories

### Technical Factors
- [ ] Complexity underestimated
- [ ] Technical dependencies delayed
- [ ] Bugs/issues took longer than expected
- [ ] Learning curve steeper than planned
- [ ] Other: {Describe}

### Resource Factors
- [ ] Insufficient time allocated
- [ ] Skills gap (need to learn new tools/concepts)
- [ ] Tools/infrastructure not ready
- [ ] Other: {Describe}

### External Factors
- [ ] Dependencies on others not met
- [ ] Stakeholder delays or changes
- [ ] Market/environment shifts
- [ ] Other: {Describe}

**Pattern Recognition:** Track root causes across multiple milestones to identify systemic issues.
