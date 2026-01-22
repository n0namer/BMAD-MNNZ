---
name: 'step-02a-decision-framework'
description: 'Load frameworks and apply Decision Block v2.0 phases 1-2'

nextStepFile: './step-02b-moe-matrix-setup.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
decisionFrameworks: '../data/decision-frameworks.md'
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 2a: Decision Framework Application

---

## ANTI-VIOLATION GUARDS

- 🚨 STRICTLY FORBIDDEN:
  - Симуляция, генерация placeholder'ов, допущения без основания — запрещены.
  - Любая абстракция, generic-ответы, использование временных или шаблонных данных строго блокируются.
- 🚨 Все действия — только по специфике текущей задачи/кейса, document/case placeholders запрещены.
- 🚨 Любые MCP workflow transition разрешены только по однозначному валидированному user input.
- 🚨 Все вызовы MCP-функций обязаны соблюдать anti-restrictiveness rule, запрещено ограничение валидного участия пользователя.

## PROBLEM-SPECIFIC DATA REQUIREMENTS

- Все критерии, evidence и аналитика должны быть релевантны только текущему кейсу.
- Обязателен контроль отсутствия "generic", универсальных или не-кейс-специфичных элементов.
- Перед каждым шагом проводится верификация специфики данных, подтверждение текущей реальной задачи.

## EXTENDED EXECUTION PROTOCOLS

- Четко фиксируется последовательность: только строго по утверждённой схеме, автоматический переход невозможен.
- Перед каждым действием — enforce self-check и блокировку "по умолчанию".
- На каждом этапе — user input enforcement: пользователь подтверждает каждый переход или действие.
- Вставка или редактирование frontmatter только с именной меткой шага и временем.

## CRITICAL GAPS CHECK & SELF-VALIDATION

**Чеклист критических пробелов перед переходом:**
- [ ] Вся аналитика и критерии соответствуют только описываемому кейсу.
- [ ] Нет использования placeholder'ов, симуляций, template-ответов.
- [ ] Каждая запрограммированная секция (criteria, evidence, gaps) валидирована на специфичность и полноту.
- [ ] Перед переходом к MENU — ручная self-validation.

**Таблица валидации критериев для explicit проверки:**

| Критерий              | Проверка специфичности | Проверка измеримости | Конфликты/Пересечения | Валидировано ✔️ |
|-----------------------|-----------------------|---------------------|-----------------------|-----------------|
| Must-have             |                       |                     |                       |                 |
| Should-have           |                       |                     |                       |                 |
| Nice-to-have          |                       |                     |                       |                 |

Перед подтверждением перехода заполнить и зафиксировать таблицу выше. 

## MENU ENFORCEMENT & WAITING FOR USER INPUT

- Каждый возможный вариант меню дословно декларируется, автоматизация вибора или перехода запрещена.
- После каждого действия — await explicit user menu choice, только после — продолжение.
- При любой ошибке — возвращение к MENU без выполнения автоматических сценариев.

## FRONTMATTER UPDATE ENFORCEMENT

- Все изменения frontmatter фиксируются в едином формате yaml, с шагами и контрольной меткой времени/шага.
- Запрещено изменение других данных файла вне фронтматтер-блока.

---

## STEP GOAL:

To load decision frameworks and apply Decision Block v2.0 phases 1-2 for problem definition refinement and evidence requirements establishment.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative framework application, not unilateral methodology design
- ✅ You bring Decision Block v2.0 expertise and systematic application
- ✅ User brings domain knowledge and framework validation
- ✅ Together we establish robust decision methodology foundation

### Step-Specific Rules:

- 🎯 Focus only on framework loading and phases 1-2 application
- 🚫 FORBIDDEN to establish MOE framework or matrix templates yet
- 💬 Approach: Systematic methodology application with user validation
- 📋 Document framework application and initial findings

## EXECUTION PROTOCOLS:

- 🎯 Load and apply Decision Block v2.0 phases systematically
- 💾 Establish evidence requirements foundation
- 📖 Prepare for MOE and matrix framework establishment
- 🚫 Only phases 1-2 - MOE comes next

## DECISION FRAMEWORK CUSTOMIZATION RULES

🚨 CRITICAL: Framework MUST be customized to user's problem

UNIVERSAL RULES FOR ALL FRAMEWORKS:

Rule 1: Problem Specificity
- [ ] Framework constraints tied to user's actual problem context
- [ ] Not templated from generic decision frameworks
- [ ] All stakeholders identified are REAL stakeholders for THIS problem
- [ ] Timeline reflects ACTUAL project timeline

Rule 2: Constraint Accuracy
- [ ] Technical constraints are specific to user's tech stack
- [ ] Business constraints are specific to user's organization
- [ ] Resource constraints are specific to user's available resources
- [ ] Regulatory constraints are specific to user's jurisdiction/industry

Rule 3: Decision Authority
- [ ] Decision maker clearly identified (not generic "stakeholder")
- [ ] Decision criteria reflect this specific decision maker's priorities
- [ ] Success criteria are specific to this user's definition of success

VIOLATION = STOP AND REBUILD:
If framework appears to be generic template without customization:
→ STOP immediately
→ Identify missing problem-specific details
→ ASK USER for specifics before proceeding
→ REBUILD framework using actual problem data

---

## CONTEXT BOUNDARIES:

- Available context: Problem analysis completed in step-01
- Focus: Framework loading and phases 1-2 application
- Limits: Do not establish MOE dimensions or matrix templates
- Dependencies: Complete problem analysis foundation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Decision Frameworks

"**Загружаю Decision Block v2.0 и MOE frameworks...**"

Load {decisionFrameworks} to access:
- Decision Block v2.0 methodology
- MOE analysis framework
- Applicability matrix concepts
- Implementation planning framework

### 2. Apply Decision Block v2.0 Phase 1: Problem Definition Refinement

"**Применяю Phase 1 Decision Block v2.0: Problem Definition Refinement...**"

**Refine problem statement:**
- Validate original problem decomposition
- Identify any missed elements
- Clarify decision scope and boundaries
- Confirm stakeholder analysis completeness

**Success criteria validation:**
- Review must-have/should-have/nice-to-have
- Validate measurability of criteria
- Identify potential conflicts between criteria
- Establish relative importance weights

### 3. Apply Decision Block v2.0 Phase 2: Evidence Requirements Definition

"**Применяю Phase 2: Evidence Requirements Definition...**"

**Define evidence needs:**
- Technical evidence requirements
- Business case evidence needs
- Operational feasibility evidence
- Risk assessment evidence requirements

**Evidence source identification:**
- Internal data sources
- External research requirements
- Expert consultation needs
- Benchmarking opportunities

### 4. Document Framework Application

"**Документирую framework application results...**"

Create intermediate documentation:

**Problem Definition Refinement:**
- Original problem: [from_step_1]
- Refined scope: [refined_scope]
- Decision type: [strategic/operational/tactical]

**Success Criteria Validation:**
- Must-have (critical): [must_have_list]
- Should-have (important): [should_have_list]
- Nice-to-have (optional): [nice_to_have_list]

**Evidence Requirements Defined:**
- Technical evidence: [technical_evidence_needs]
- Business evidence: [business_evidence_needs]
- Operational evidence: [operational_evidence_needs]
- Risk evidence: [risk_evidence_needs]

### 5. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02a-decision-framework']
progress: 30
currentPhase: 'decision-framework-application'
lastStep: 'step-02a-decision-framework'
decisionFrameworkApplicationComplete: true
```

### 6. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to MOE Matrix Setup"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper framework refinement
- IF P: Execute {partyModeWorkflow} to discuss framework application with other agents
- IF C: Save framework application to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#6-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and framework application is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin MOE matrix setup.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Decision frameworks properly loaded and accessed
- Decision Block v2.0 Phase 1 completed with problem refinement
- Phase 2 completed with evidence requirements defined
- Framework application documented with clear results
- Progress updated to 30% with methodology foundation established

### ❌ SYSTEM FAILURE:

- Decision frameworks not loaded or accessed
- Phase 1 not completed or problem refinement inadequate
- Phase 2 not completed or evidence requirements incomplete
- Application documentation missing or unclear
- Foundation not properly established

**Master Rule:** Framework application establishes the methodology foundation - all subsequent analysis depends on proper Decision Block v2.0 implementation.
