# TRIZ Modes Execution - Detailed Instructions

**Purpose:** Complete execution protocols for 3 TRIZ modes

**Reference from:** step-04.5-triz-analysis.md

---

## Quick Mode (5-10 min)

1. **Classify contradiction** (use data/triz-quick-patterns.md)
2. **Suggest top-3 principles** based on contradiction type
3. **Brainstorm:** User provides 1-2 ideas per principle
4. **Select** 1-2 best solutions
5. **Document** using triz-quick.template.md
6. **Return** to calling step

---

## Structured Mode (30-60 min)

1. **Define technical contradiction:** Improving X worsens Y
2. **Contradiction Matrix:** Find 2-4 principles
3. **Define physical contradiction** (if applicable)
4. **Formulate IFR** (Ideal Final Result)
5. **Apply principles:** Document 2-3 concrete solutions each
6. **Evaluate** solutions (IFR%, feasibility, cost, time, risk)
7. **Document** using triz-structured.template.md

---

## Full ARIZ (2-4 hours)

**9 Parts of ARIZ-85V:**

**Part 1:** Problem Analysis (mini-task, maxi-task, IFR-1)
**Part 2:** Model Analysis (operative zone, time, resources)
**Part 3:** Information Fund (patents, analogs, transfer)
**Part 4:** Resource Utilization (space, time, fields)
**Part 5:** Knowledge Base (76 standard solutions)
**Part 6:** Problem Change (reformulation, inversion)
**Part 7:** System Transitions (bi-system, macro/micro)
**Part 8:** Psychological Inertia Removal (fantasy, constraints)
**Part 9:** Solution Organization (best choice, IFR check)

**Integration with Deep Plan:**
- ARIZ solution becomes L2 structure
- 9 parts map to L3-L4 levels

---

## Mode Selection Guide

| Time Available | Contradiction Type | Recommended Mode |
|----------------|-------------------|------------------|
| <15 min | Any | Quick |
| 15-60 min | Simple | Quick |
| 15-60 min | Complex/Strategic | Structured |
| >60 min | Medium complexity | Structured |
| >60 min | Fundamental | Full ARIZ |

---

## Return Integration

**From Step 4 (Consilium):**
- Present TRIZ solution to experts
- Measure new consensus % (expect >80%)
- Update Consilium Recommendations section

**From Step 5 (Scoring):**
- Recalculate MCDA with TRIZ-adjusted approach
- Expect improved scores (Confidence, Risk)
- Update Stage Gate decision

**From Step 8 (Deep Plan):**
- Integrate TRIZ solution into L2 structure
- Map implementation phases to L3-L4
- Update Quality Gate criteria

---

## Output Format Template

**Add to workflow-plan.md after completion:**

```markdown
## TRIZ: Разрешение противоречия

**Дата:** {дата}
**Режим:** {Quick / Structured / Full ARIZ}
**Вызван из:** Шаг {4/5/8}

**Противоречие:**
- Улучшаемое: {X}
- Ухудшаемое: {Y}

**Решение:** {краткое описание}
**Принципы ТРИЗ:** {N1} - {Название}, {N2} - {Название}
**ИКР достижение:** {%}

**План реализации:**
- {пункт 1}
- {пункт 2}

**Критерии успеха:**
- {метрика 1}: цель = {значение}
- {метрика 2}: цель = {значение}

**Статус противоречия:** {Разрешено / Частично / Не разрешено}
```

---

## Memory Storage Protocol

**Auto-save via CLI (global memory):**

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:methods:triz:{project_id}:{date}" \
  --content "{
    mode: '{Quick|Structured|Full}',
    contradiction: '{описание}',
    principles_used: ['{P1}', '{P2}'],
    solution: '{резюме}',
    effectiveness: '{оценка 1-5}',
    project_domain: '{Business|Finance|Health|Personal}',
    ifr_achievement: '{%}',
    called_from: 'step-{4|5|8}'
  }"
```

**Benefits of storage:**
- Future projects find similar contradictions already resolved
- Cross-domain pattern reuse
- Learning: which principles work best for which contradiction types

---

For complete detailed instructions, see: data/triz-modes-execution.md
