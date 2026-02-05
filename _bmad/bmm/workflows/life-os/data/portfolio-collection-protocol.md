# Portfolio Collection Protocol

**Version:** 1.0.0
**Purpose:** Structured intake process for batch idea collection
**Used by:** step-00.1-portfolio-intake.md

---

## Phase 1: Intake Setup

**Initial Prompt:**
```
📋 Portfolio Intake Mode

How many ideas do you want to evaluate today?
Recommended: 3-10 ideas for meaningful comparison

[Number]: ___
```

---

## Phase 2: Per-Idea Collection

**Template for Each Idea:**

```markdown
### Idea {N}: {Short Name}

**Description** (1-2 sentences):
{What is it? What problem does it solve?}

**Domain**:
[Work/Personal/Learning/Side Project/Health/Relationships/Finance/Other]

**Initial Complexity Guess** (1-10):
1-3: Simple (clear path, familiar tools)
4-7: Moderate (some unknowns, mixed skills)
8-10: Complex (research needed, new territory)

[A]dd another idea | [D]one collecting
```

**Required Fields:**
- Short name (3-8 words)
- Description (1-2 sentences, <100 words)
- Domain selection
- Complexity guess (1-10)

**Optional Fields:**
- Urgency notes
- Stakeholders
- Initial constraints

---

## Phase 3: Auto-Save After Each Entry

**CLI Command:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "portfolio:{session-id}" \
  --key "intake:idea-{N}" \
  --content "{
    id: {N},
    name: {short_name},
    description: {desc},
    domain: {domain},
    complexity_guess: {1-10},
    timestamp: {ISO_timestamp}
  }"
```

**Storage Structure:**
```json
{
  "id": 1,
  "name": "AI Product Assistant",
  "description": "Build an AI-powered product assistant to help users with complex tasks",
  "domain": "Work",
  "complexity_guess": 7,
  "timestamp": "2026-02-05T10:30:00Z"
}
```

---

## Phase 4: Collection Summary

**After collecting all ideas, display:**

```
📊 Collection Summary

Total ideas collected: {N}
Domains: {domain breakdown}
Complexity range: {min}-{max}
Collection duration: {X} minutes

Ready to score?
[C]ontinue to scoring | [R]eview entries | [A]dd more ideas
```

---

## Quality Checks

**Before proceeding to scoring:**
- [ ] At least 3 ideas collected (meaningful comparison requires 3+)
- [ ] All ideas have complete fields (name, description, domain, complexity)
- [ ] Descriptions are clear and distinct (no duplicates)
- [ ] Complexity guesses provided (even if rough)

**Red Flags:**
- Only 1-2 ideas collected (suggest collecting more for comparison)
- Vague descriptions (e.g., "make things better")
- All ideas in same domain with same complexity (limited diversity)

---

## Time Budget

- **Setup prompt:** 1 min
- **Per idea collection:** 2-3 min each
- **Summary review:** 1-2 min

**Total for 5 ideas:** ~12-18 minutes
