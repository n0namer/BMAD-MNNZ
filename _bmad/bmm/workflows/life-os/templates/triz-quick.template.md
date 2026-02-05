---
template: triz-quick
mode: create
framework: TRIZ Quick
timeInvestment: quick (5-10 min)
outputs:
  - Append to workflow-plan.md
tier: 2
tier_name: "Intermediate"
unlock_requirement: "3 workflows"
category: "problem-solving"
difficulty: "intermediate"
estimated_time: "10 min"
description: "Quick contradiction analysis using TRIZ principles for rapid problem-solving"
---

# TRIZ Quick Analysis: {Project Name}

**Generated:** {date}
**Mode:** Quick (5-10 minutes)
**Called from:** {Step 4/5/8}
**Analyst:** {user_name}

## 1. Contradiction Statement

**Problem:**
{One sentence description}

**Contradiction:**
Improving {X} worsens {Y}

**Example:**
"Improving launch speed (X) worsens product quality (Y)"

---

## 2. Browse Top 10 Principles

{Display top 10 most common TRIZ principles from triz-quick-patterns.md with brief descriptions}

**Top 10 Most Common Principles:**
1. **Segmentation** - Divide into parts, make sectional
2. **Taking Out** - Extract interfering part
3. **Local Quality** - Different parts have different properties
4. **Asymmetry** - Replace symmetry with asymmetry
5. **Merging** - Combine similar operations in time/space
6. **Universality** - Object performs multiple functions
7. **Nested Doll** - One object inside another
8. **Prior Action** - Perform action in advance
9. **Prior Counteraction** - Create buffer against harm
10. **Parameter Changes** - Change state, concentration, flexibility

---

## 3. Pick 2-3 Principles

**User selects 2-3 principles that seem relevant:**

Selected Principles:
- [ ] Principle {N}: {Name}
- [ ] Principle {M}: {Name}
- [ ] Principle {K}: {Name}

---

## 4. Brainstorm Solutions (5 minutes)

**For each selected principle:**

### Principle {N}: {Name}
**How this applies to our contradiction:**
{User brainstorms 2-3 ideas}

**Best idea:**
{Pick one idea}

---

### Principle {M}: {Name}
(Same structure)

---

### Principle {K}: {Name}
(Same structure)

---

## 5. Best Solution

**From all ideas generated, the best solution is:**

{Solution description}

**Why this works:**
- Improves {X} by {how}
- Maintains or improves {Y} by {how}
- Contradiction resolved: {%}

**Implementation:**
- First step: {action}
- Quick win: {what can be done immediately}
- Full implementation: {timeline}

---

## 6. Append to Workflow Plan

**Add to workflow-plan.md:**

```markdown
## TRIZ Quick Analysis

**Contradiction:** {X} ⇄ {Y}
**Principles Used:** {P1}, {P2}, {P3}
**Solution:** {one-sentence solution}
**Contradiction Resolution:** {%}
**Next Steps:** {immediate action}
```

---

## 7. Memory Storage

**Store in Claude Flow Memory:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:methods:triz:quick:{project_id}:{date}" \
  --content "{
    mode: 'Quick',
    contradiction: '{X} ⇄ {Y}',
    principles: ['{P1}', '{P2}', '{P3}'],
    solution: '{summary}',
    resolution_percent: {%},
    time_invested: '{minutes} min',
    domain: '{Business|Finance|Health|Personal}',
    effectiveness: '{to be rated post-implementation}'
  }"
```

---

**Return to:** {Step 4/5/8} with resolved contradiction

**Template Version:** 1.0
**Time Investment:** 5-10 minutes
