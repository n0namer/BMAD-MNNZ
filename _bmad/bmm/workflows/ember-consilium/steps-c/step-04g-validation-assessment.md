---
name: 'step-04b2b1-validation-assessment'
description: 'Validate matrix results with quality metrics and stability assessment'

nextStepFile: './step-04h-results-documentation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
decisionFrameworks: '../data/decision-frameworks.md'
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 4b2b1: Matrix Validation Assessment

## STEP GOAL:

To validate matrix evaluation results with comprehensive quality metrics and perform ranking stability assessment.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative validation assessment, not unilateral verification
- ✅ You bring validation methodologies and quality assessment frameworks
- ✅ User brings validation insights and quality assessment preferences
- ✅ Together we ensure evaluation integrity and reliability

### Step-Specific Rules:

- 🎯 Focus only on validation assessment and quality metrics
- 🚫 FORBIDDEN to perform documentation or final reporting yet
- 💬 Approach: Systematic validation with comprehensive quality assessment
- 📋 Document all validation metrics and stability assessments

## EXECUTION PROTOCOLS:

- 🎯 Validate matrix results with quality metrics
- 💾 Perform ranking stability assessment
- 📖 Prepare validation foundation for documentation
- 🚫 Only validation - documentation comes next

---

## MCP INTEGRATION CHECKLIST REQUIREMENTS – AUDIT TRAIL & TRACEABILITY

**Любые изменения scoring, weighting, confidence или penalty на этапе валидации/оценки качества должны соответствовать этим требованиям:**

- Для ЛЮБОГО adjustment в calculable weights, confidence или penalties:
  - [ ] Жёстко сохранять ссылку на source-MCP, источник данных и rationale adjustment-а.
  - [ ] Формировать audit trail для всех изменений: причина, источник (автомат/эксперт/алгоритм), финальное значение, временная метка, ответственные лица/агенты.
  - [ ] Логировать как manual, так и automated adjustment-и с критериями, логикой и подтверждающими данными.
  - [ ] Обязательно фиксировать, являются ли эти изменения обратимыми, и как осуществляется возврат.
  - [ ] Все штрафы (penalties) и снижение confidence должны быть привязаны к конкретному фактору, расчету или допущению, с объяснением.
  - [ ] Для каждой финальной scoring/validation/factor analysis матрицы сохранять полный provenance chain: исходные веса, все adjustments, penalties, confident/uncertain решения.
  - [ ] В случае ручной корректировки — отдельный audit entry c идентификацией персон/группы и объяснением оснований.
  - [ ] Нарушение этого чеклиста приводит к автоматической остановке процесса validation и требует незамедлительного исправления traceability/audit log!

---

## CONTEXT BOUNDARIES:

- Available context: Rankings calculated and factor analysis completed
- Focus: Result validation and quality assessment
- Limits: Do not perform documentation or final reporting
- Dependencies: Ranking foundation and factor analysis established

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Ranking Results

"**Загружаю ranking results из предыдущего шага...**"

Load ranking data from {outputFile}:
- Final rankings calculated
- Factor analysis completed
- Analytical insights generated

### 2. Validate Matrix Results

"**Валидирую matrix evaluation results...**"

**Evaluation Quality Metrics:**
- **Factors with High Confidence (>0.8):** [count]/[total] ([percentage]%)
- **Factors with Medium Confidence (0.6-0.8):** [count]/[total] ([percentage]%)
- **Factors with Low Confidence (<0.6):** [count]/[total] ([percentage]%)

**Ranking Stability Assessment:**
- **Primary Recommendation Confidence:** [high/medium/low]
- **Gap Between Top Two Options:** [score_difference]
- **Sensitivity to Weight Changes:** [stable/moderate/sensitive]

### 3. Document Validation Assessment

"**Документирую validation assessment results...**"

Create intermediate validation documentation:

**Validation Assessment Summary:**
- **Quality Metrics Applied:** [list of metrics used]
- **Confidence Distribution:** High: [count], Medium: [count], Low: [count]
- **Ranking Stability:** [assessment] - [key indicators]
- **Validation Completeness:** [percentage]% of factors validated

**Assessment Results:**
- **Overall Evaluation Quality:** [high/medium/low]
- **Ranking Confidence Level:** [score]/1.0
- **Stability Indicators:** [list key stability metrics]
- **Quality Assurance:** [validation checks performed]

### 4. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation', 'step-04a-matrix-setup', 'step-04b1-weighted-scoring', 'step-04b2a-ranking-calculation', 'step-04b2b1-validation-assessment']
progress: 58
currentPhase: 'validation-assessment'
lastStep: 'step-04b2b1-validation-assessment'
validationAssessmentComplete: true
```

### 5. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Results Documentation"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper validation analysis
- IF P: Execute {partyModeWorkflow} to discuss validation assessment with other agents
- IF C: Save validation assessment to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#5-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and validation assessment is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin results documentation.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Matrix results validated with comprehensive quality metrics
- Ranking stability assessment completed systematically
- Validation assessment documented with clear results
- Quality assurance performed with integrity checks
- Progress updated to 58% with validation foundation established

### ❌ SYSTEM FAILURE:

- Validation incomplete or quality metrics inadequate
- Ranking stability not assessed systematically
- Assessment documentation inadequate or missing
- Quality assurance not performed or insufficient
- Foundation not properly established for documentation

**Master Rule:** Validation assessment ensures evaluation integrity - all results must be systematically validated and quality-assured.
