# Portfolio Templates

## Integration Summary Template

```markdown
## Integration Summary

**Bucket:** {bucket}
**Portfolio Health:** {healthy/imbalanced} — {notes}
**Integration Pattern:** {pattern}
**Dependencies:** {list or none}
**BMAD Workflow:** {suggested} — {start/defer/skip}
**Timeline (High-Level):** {start} → {end} ({capacity}/week)
**WIP Decision:** {allow/defer/kill/override}
```

## Stage Gate Template

```markdown
## Stage Gate: Plan Readiness

**Gate Decision:** {Proceed/Revise/Pause}
**DoD Checklist:** {met/not met}
**Notes:** {brief rationale}
```

## Decision Log Template

```markdown
# Decision Log

## {today} — {project_title}
- Context: Portfolio Integration
- Decision: {bucket} / {pattern} / WIP {decision}
- Rationale: {brief rationale}
```

## Integration Pattern Options

1. **Standalone** - Independent project with no dependencies
2. **Platform Extension** - Builds on existing platform/codebase
3. **Bundle** - Group of related projects executed together
4. **Enabler** - Infrastructure/tooling that supports other projects
