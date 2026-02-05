# Milestone Definition Protocol

## Overview

Milestones are extracted from the Deep Plan L2-L4 structure. Each milestone represents a major phase or deliverable.

## Auto-Suggest Template

```
💡 **Suggested Milestones (from Deep Plan):**

Based on your L2-L4 structure, I suggest these milestones:

1. **Milestone 1:** {L2 area 1} - {L3 workstream completion}
   - Target Date: [Ask user]
   - Success Criteria: [Auto-suggest from L4 stages]

2. **Milestone 2:** {L2 area 2} - {L3 workstream completion}
   - Target Date: [Ask user]
   - Success Criteria: [Auto-suggest from L4 stages]

3. **Milestone 3:** {L2 area 3} - {L3 workstream completion}
   - Target Date: [Ask user]
   - Success Criteria: [Auto-suggest from L4 stages]

[Additional milestones if >3 L2 areas]

**Review and confirm each milestone:**
```

## Per-Milestone Confirmation Template

```
📍 **Milestone {N}: {Suggested name}**

**Suggested Success Criteria (from Deep Plan):**
- {Criterion 1 from L4/L5}
- {Criterion 2 from L4/L5}
- {Criterion 3 from L4/L5}

**Questions:**
1. Target date for this milestone: [YYYY-MM-DD]
2. Are these success criteria measurable and complete? [Y/N]
3. What could prevent achieving this milestone? (Blocker risks)

**Blocker Risks Examples:**
- Dependency on external team/resource
- Technical unknowns requiring research
- Budget/approval gates
- Skill gaps requiring training
```

## Milestone Output Structure

```markdown
### Milestone {N}: {Name}
**Target Date:** {YYYY-MM-DD}
**Success Criteria:**
- {Measurable criterion 1}
- {Measurable criterion 2}
- {Measurable criterion 3}

**Blocker Risks:**
- {What could prevent this}
- {Dependencies}
- {Unknowns}

**Status:** Not Started
**Actual Completion:** [TBD]
```

## Validation Rules

- ✅ Target date must be future date in YYYY-MM-DD format
- ✅ Success criteria must be measurable (avoid "better", "improved" without numbers)
- ✅ At least 1 blocker risk identified per milestone
- ✅ Milestones must be sequential (M2 target > M1 target)

## Execution Rule

**CRITICAL:** Confirm each milestone with user before proceeding to next.
