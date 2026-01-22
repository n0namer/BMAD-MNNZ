---
name: 'step-04b2a-ranking-calculation'
description: 'Calculate final rankings and perform factor analysis'

nextStepFile: './step-04g-validation-assessment.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
decisionFrameworks: '../data/decision-frameworks.md'
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 4b2a: Ranking Calculation & Factor Analysis

## STEP GOAL:

To calculate final solution rankings using established methodology and perform comprehensive factor analysis for decision insights.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative ranking synthesis, not unilateral calculations
- ✅ You bring quantitative ranking methodology and factor analysis frameworks
- ✅ User brings ranking preferences and factor interpretation insights
- ✅ Together we produce transparent ranking foundation

### Step-Specific Rules:

- 🎯 Focus only on ranking calculations and factor analysis
- 🚫 FORBIDDEN to perform validation or documentation yet
- 💬 Approach: Systematic quantitative ranking with analytical insights
- 📋 Document all calculations, rankings, and factor analyses

## EXECUTION PROTOCOLS:

- 🎯 Calculate final rankings using established methodology
- 💾 Perform comprehensive factor analysis for insights
- 📖 Prepare analytical foundation for validation phase
- 🚫 Only calculations - validation comes next

---

## MCP INTEGRATION CHECKLIST REQUIREMENTS – AUDIT TRAIL & TRACEABILITY

**Любые изменения scoring, weighting, confidence или penalty на этапе ранжирования/факторного анализа должны соответствовать этим требованиям:**

- Для ЛЮБОГО adjustment в calculable weights, confidence или penalties:
  - [ ] Жёстко сохранять ссылку на source-MCP, источник данных и rationale adjustment-а.
  - [ ] Формировать audit trail для всех изменений: причина, источник (автомат/эксперт/алгоритм), финальное значение, временная метка, ответственные лица/агенты.
  - [ ] Логировать как manual, так и automated adjustment-и с критериями, логикой и подтверждающими данными.
  - [ ] Обязательно фиксировать, являются ли эти изменения обратимыми, и как осуществляется возврат.
  - [ ] Все штрафы (penalties) и снижение confidence должны быть привязаны к конкретному фактору, расчету или допущению, с объяснением.
  - [ ] Для каждой финальной scoring/ranking/factor analysis матрицы сохранять полный provenance chain: исходные веса, все adjustments, penalties, confident/uncertain решения.
  - [ ] В случае ручной корректировки — отдельный audit entry c идентификацией персон/группы и объяснением оснований.
  - [ ] Нарушение этого чеклиста приводит к автоматической остановке процесса ranking и требует незамедлительного исправления traceability/audit log!

---

## CONTEXT BOUNDARIES:

- Available context: Weighted scoring and confidence adjustments completed
- Focus: Ranking calculation and factor analysis execution
- Limits: Do not perform validation or provide final documentation
- Dependencies: Quantitative scoring foundation established

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Scoring Results

"**Загружаю weighted scoring results из предыдущего шага...**"

Load scoring data from {outputFile}:
- Base weighted scores calculated
- Confidence adjustments applied
- Adjusted scores validated
- Calculation audit trails maintained

### 2. Calculate Final Rankings

"**Рассчитываю final rankings всех solution options...**"

**Ranking Methodology Applied:**
1. **Primary Rank**: Highest adjusted weighted score
2. **Secondary Rank**: Strongest performance on critical factors
3. **Tertiary Rank**: Highest overall confidence level

**Ranking Calculations:**
- Sort solutions by adjusted weighted scores
- Apply tie-breaking rules for equal scores
- Validate ranking stability and sensitivity
- Document ranking methodology and assumptions

### 3. Perform Factor Analysis

"**Выполняю factor analysis для insights...**"

**Best Performing Factors Analysis:**
1. Identify factors with highest average scores
2. Determine which factors most influence rankings
3. Assess factor importance vs actual performance

**Most Discriminating Factors:**
1. Factors that create largest score gaps between options
2. Critical differentiators for decision making
3. Factors requiring further investigation

**Areas of Lowest Confidence:**
1. Factors with lowest average confidence scores
2. Evaluations needing additional evidence
3. Potential sources of ranking uncertainty

### 4. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation', 'step-04a-matrix-setup', 'step-04b1-weighted-scoring', 'step-04b2a-ranking-calculation']
progress: 57
currentPhase: 'ranking-calculation'
lastStep: 'step-04b2a-ranking-calculation'
rankingCalculationComplete: true
```

### 5. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Validation Documentation"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper ranking analysis
- IF P: Execute {partyModeWorkflow} to discuss ranking calculations with other agents
- IF C: Save ranking calculations to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#5-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and ranking calculations are saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin validation documentation.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Final rankings calculated using established methodology
- Factor analysis performed with comprehensive insights
- Ranking calculations documented with transparency
- Progress updated to 57% with ranking foundation established

### ❌ SYSTEM FAILURE:

- Rankings not calculated or methodology unclear
- Factor analysis missing or superficial
- Ranking calculations not properly documented
- Audit trails not maintained or insufficient

**Master Rule:** Ranking calculations provide quantitative decision foundation - all methodologies must be systematic and analytically sound.
