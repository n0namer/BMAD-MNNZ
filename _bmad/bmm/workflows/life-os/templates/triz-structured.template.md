---
template: triz-structured
mode: create
framework: TRIZ Structured
timeInvestment: moderate (30-60 min)
outputs:
  - triz-structured-analysis.md (separate document)
  - Executive summary for workflow-plan.md
---

# TRIZ Structured Analysis: {Project Name}

**Generated:** {date}
**Mode:** Structured (30-60 minutes)
**Called from:** {Step 4/5/8}
**Analyst:** {user_name}

---

## 1. Problem Definition

**Problem Statement:**
{Detailed description}

**System Description:**
- Tool (what acts): {component}
- Object (what is acted upon): {component}
- Conflict: {what happens}

**Standard TRIZ formulation:**
"{Tool} acts on {Object} to achieve {useful function}, but this causes {harmful effect}."

---

## 2. Contradiction Analysis

### 2.1 Technical Contradiction

**Improving Parameter:** {X}
- Current value: {value}
- Desired value: {value}

**Worsening Parameter:** {Y}
- Current value: {value}
- Acceptable value: {value}

**Contradiction:**
Improving {X} from {V1} to {V2} worsens {Y} from {V3} to {V4}.

---

### 2.2 Physical Contradiction (if applicable)

**Does the same object need opposite properties?**

{Object} needs to be {Property A} AND {Property B} at the same time.

**Example:** Product needs to be "ready now" AND "thoroughly tested"

---

### 2.3 Administrative Contradiction (if applicable)

**Is there a perceived impossibility?**

"We need {goal} but {constraint} prevents it."

**Example:** "We need ML infrastructure but don't have ML expertise"

---

## 3. Contradiction Matrix

**Parameters:**
- Improving: {X} - Matrix row {N}
- Worsening: {Y} - Matrix column {M}

**Matrix cell [{N}, {M}] recommends principles:**
1. Principle {P1}: {Name}
2. Principle {P2}: {Name}
3. Principle {P3}: {Name}
4. Principle {P4}: {Name}

{Include 10x10 simplified contradiction matrix or link to triz-quick-patterns.md}

---

## 4. Principle Application

**For each recommended principle:**

### Principle {P1}: {Name}

**Definition:**
{From triz-quick-patterns.md}

**How it applies to our problem:**
{Detailed explanation}

**Solution idea:**
{Concrete solution using this principle}

**Feasibility:** {High / Medium / Low}

**Resources needed:** {what's required}

---

### Principle {P2}: {Name}
(Same structure)

---

### Principle {P3}: {Name}
(Same structure)

---

### Principle {P4}: {Name}
(Same structure)

---

## 5. IFR (Ideal Final Result)

**IFR Statement:**
"{Object} by itself performs {useful function} without {harmful effects} and without {additional resources}."

**Example:**
"The development process by itself ensures quality without slowing delivery and without extra budget."

**Comparison to solutions:**

| Solution | IFR Achievement | Gap |
|----------|----------------|-----|
| Using P1 | {%} | {what's missing from ideal} |
| Using P2 | {%} | {what's missing from ideal} |
| Using P3 | {%} | {what's missing from ideal} |

---

## 6. Resource Analysis (VPR)

**Available resources in the system:**

**Internal resources:**
- {Resource 1}: {description}
- {Resource 2}: {description}

**External resources (environment):**
- {Resource 3}: {description}
- {Resource 4}: {description}

**Cheap/free resources:**
- {Resource 5}: {why cheap/free}
- {Resource 6}: {why cheap/free}

**How to use resources to implement solution:**
{Plan for resource utilization}

---

## 7. Best Solution Selection

**Solutions generated:**
1. {Solution from P1}: {brief description}
2. {Solution from P2}: {brief description}
3. {Solution from P3}: {brief description}

**Evaluation Matrix:**

| Solution | IFR % | Feasibility | Resources | Total |
|----------|-------|-------------|-----------|-------|
| 1 | {%} | {1-10} | {1-10} | {sum} |
| 2 | {%} | {1-10} | {1-10} | {sum} |
| 3 | {%} | {1-10} | {1-10} | {sum} |

**Winner:** Solution {N} - Total: {score}

**Rationale:**
{Why this solution is best}

---

## 8. Implementation Plan

**Solution:** {Winning solution description}

**Principle(s) used:** {P1, P2}

**Implementation phases:**

**Phase 1: Design (Week 1-2)**
- [ ] {Task 1}
- [ ] {Task 2}
- Deliverable: {prototype/design}

**Phase 2: Build (Week 3-5)**
- [ ] {Task 1}
- [ ] {Task 2}
- Deliverable: {working solution}

**Phase 3: Validate (Week 6)**
- [ ] {Task 1}
- [ ] {Task 2}
- Deliverable: {validated solution}

---

## 9. Success Metrics

**Contradiction resolution metrics:**

**{X} metric:**
- Baseline: {value}
- Target: {value}
- Measurement: {how to measure}

**{Y} metric:**
- Baseline: {value}
- Target: {maintain or improve}
- Measurement: {how to measure}

**Contradiction resolved if:**
{X} improves by ≥{%} AND {Y} does not worsen by >{%}

**Measurement schedule:**
- Week 3: First check
- Week 6: Final assessment

---

## 10. Append to Workflow Plan

**Executive summary for workflow-plan.md:**

```markdown
## TRIZ Structured Analysis

**Contradiction:** {X} ⇄ {Y}
**Matrix Recommendations:** P{1}, P{2}, P{3}, P{4}
**Solution:** {Winning solution name}
**Principles Used:** {P1, P2}
**IFR Achievement:** {%}

**Implementation:**
- Phase 1 (Week 1-2): {summary}
- Phase 2 (Week 3-5): {summary}
- Phase 3 (Week 6): {summary}

**Success Metrics:**
- {X}: {baseline} → {target}
- {Y}: {maintain at baseline}

**Next Review:** Week 3
```

---

## 11. Memory Storage

**Store in Claude Flow Memory:**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:methods:triz:structured:{project_id}:{date}" \
  --content "{
    mode: 'Structured',
    contradiction: '{X} ⇄ {Y}',
    principles_recommended: ['{P1}', '{P2}', '{P3}', '{P4}'],
    principles_used: ['{P1}', '{P2}'],
    solution: '{name}',
    ifr_achievement: {%},
    implementation_timeline: '{weeks}',
    domain: '{Business|Finance|Health|Personal}',
    effectiveness: '{to be rated post-implementation}',
    full_document: '{link to triz-structured-analysis.md}'
  }"
```

---

**Return to:** {Step 4/5/8} with resolved contradiction

**Template Version:** 1.0
**Time Investment:** 30-60 minutes
