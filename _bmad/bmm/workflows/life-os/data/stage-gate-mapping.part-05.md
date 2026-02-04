
**Action Items:** ___________________________________________
```

### Gate 5: Done Checklist

```markdown
## Gate 5: Completion Review

**Project:** [Project Name]
**Date:** [Date]
**Reviewer:** [Name]

### Success Metrics
- Target metrics: ___________
- Achieved metrics: ___________
- Success rate: ___% (vs. 100% target)

### Learnings
**What worked well:**
- ___________________________________________

**What didn't work:**
- ___________________________________________

**Key insights:**
- ___________________________________________

### Opportunities
- [ ] Room for improvement (ITERATE)
- [ ] Expansion to new domain (SCALE)
- [ ] Complete as-is (ARCHIVE)

### Decision
- [ ] **ARCHIVE** - Success, no immediate follow-up
- [ ] **ITERATE** - Create V2 with enhancements: ___________
- [ ] **SCALE** - Expand to new domain: ___________

**Rationale:** ___________________________________________

**Next Steps:** ___________________________________________
```

---

## INTEGRATION WITH LIFE OS WORKFLOW

### Automatic Gate Triggers

The Life OS workflow automatically triggers gates at appropriate points:

```yaml
# steps-c/step-01-collect-ideas.md
on_completion:
  trigger_gate: G0
  decision_required: true
  auto_advance_if: "decision == GO"

# steps-c/step-04-consilium.md
on_completion:
  trigger_gate: G1
  decision_required: true
  auto_advance_if: "decision == GO"

# steps-c/step-05-scoring.md
on_completion:
  trigger_gate: G2
  decision_required: true
  auto_advance_if: "decision == GO"

# steps-c/step-06-integration.md
on_completion:
  trigger_gate: G3
  decision_required: true
  auto_advance_if: "decision == GO"

# steps-v/step-02-weekly-review.md
on_completion:
  trigger_gate: G4
  for_each: "active_project"
  decision_required: true
  auto_kill_check: true
```

### Memory Storage of Gate Decisions

All gate decisions stored in dual memory:

```bash
# Markdown file
.bmad_output/bmb-creations/life-os/decisions/gate-G{N}-{project-id}-{timestamp}.md

# Claude Flow memory
npx claude-flow@v3alpha memory store \
  --namespace "life-os:decisions" \
  --key "gates:{project_id}:G{N}:{timestamp}" \
  --content "{decision + rationale + criteria_met + next_steps}"
```

---

## REFERENCES

**Based on:**
- Robert G. Cooper's Stage-Gate® methodology
- Lean Portfolio Management principles
- Agile gate adaptation (gates between sprints)
- Personal Kanban WIP limits (max 2 active)

**Adapted for:**
- Personal and business portfolio management
- AI-assisted decision-making (consilium)
- Quantitative scoring (RICE, MCDA, D/F/V/C)
- Persistent memory across sessions
- Proactive kill criteria automation

---

## VERSION HISTORY

- **v1.0** (2026-02-01): Initial stage-gate mapping for Life OS
  - 6 gates defined (G0-G5)
  - Go/Kill/Hold/Recycle logic
  - Auto-kill trigger automation
  - Workflow step mapping
  - Decision criteria checklists

