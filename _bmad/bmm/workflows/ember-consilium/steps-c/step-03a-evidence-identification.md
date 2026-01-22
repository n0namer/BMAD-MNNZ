---
name: 'step-03a1-evidence-identification'
description: 'Review evidence requirements and identify available sources'

nextStepFile: './step-03b-evidence-gathering.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 3a1: Evidence Requirements & Source Identification

## 🚨 ANTI-VIOLATION GUARDS (EXPANDED)

**Эти нарушения абсолютно запрещены:**

### ❌ VIOLATION #1: Skipping Menu Display
- **FORBIDDEN:** Пропуск меню перед переходом на следующий шаг
- **REQUIRED:** Меню всегда показывается, всегда ждет реального выбора пользователя

### ❌ VIOLATION #2: Simulating Work (EXPANDED)
**FORBIDDEN PHRASES - YOU MUST NEVER USE THESE:**
- ❌ "I would analyze...", "I would gather...", "I would document...", "One would need to...", "We could...", "It would be necessary to..."
- ❌ "Based on user input, I would...", "The analysis would show...", "Results would indicate...", "This would be documented as..."
- ❌ "I will analyze..." (если не насрочно), "This will be done...", "We will gather..."
- ❌ "Analysis complete" (без фактических результатов), "Evidence gathered" (без вывода данных), "Assessment done" (без результата)

**REQUIRED REPLACEMENTS:**
- Всегда используйте настоящее время: "Я анализирую...", "Результаты: ..."
- Фактически выполняйте все действия, ничего не симулируйте

**SIMULATION DETECTION:**
Если вы описываете, что бы сделали, а не что делаете сейчас, — ОСТАНОВИТЕСЬ. Вы должны реально делать работу, а не обещать её выполнить.

### ❌ VIOLATION #3: Generic Placeholders & Data
- **FORBIDDEN:** Выводить "[user_problem]", "[example]", "[placeholder]", шаблонные фрагменты, любые псевдонимы или variables
- **REQUIRED:** Используйте только реально предоставленные пользователем данные. Если встречается placeholder, generic template, example case или иная "заглушка" — workflow обязан немедленно остановиться: сформировать STOP-branch, зафиксировать проблему и запросить расширенный user input. Показывать хоть что-то generic (например, field "[problem]") — критическое нарушение enforcement, дальнейшее движение workflow невозможно до получения валидных данных.

### ❌ VIOLATION #4: Skipping MCP Calls
- **FORBIDDEN:** Не делать реальные вызовы к MCP tool'ам, если они требуются этим шагом
- **REQUIRED:** Реально вызывать MCP-тулы, документировать что вызвано, что недоступно

### ❌ VIOLATION #5: Partial File Loading
- **FORBIDDEN:** Грузить следующий step-файл только частично или запускать до полного чтения
- **REQUIRED:** Грузить и читать целиком, ДО выполнения

### ❌ VIOLATION #6: No User Input
- **FORBIDDEN:** Предполагать переход без явного выбора пользователя
- **REQUIRED:** Всегда ждать реального ввода с клавиатуры перед продолжением

### ❌ VIOLATION #7: Skipping Sequence Steps
- **FORBIDDEN:** Пропускать шаги в MANDATORY SEQUENCE
- **REQUIRED:** Следовать строго по порядку

### ❌ VIOLATION #8: Not Saving Work
- **FORBIDDEN:** Показывать результаты без сохранения их в {outputFile}
- **REQUIRED:** Всегда сохранять работу, обновлять frontmatter

---

**ENFORCEMENT:** Абсолютный STOP и возврат управления пользователю — при малейшей попытке workflow использовать generic field, placeholder, example (без explicit user input). Любое нарушение анти-generic — STOP, документировать причину, восстановление работы только после получения real, problem-specific input!

## 🚨 MCP PARAMETER ANTI-RESTRICTION RULES

**ENFORCEMENT:** Строго запрещается ограничивать параметры MCP-запросов (extension, language, platform, etc) без явного требования пользователя или подтверждённой доменной необходимости. Любое неявно навязанное ограничение — критическое нарушение:

- ❌ DON'T: Unnecessarily restrict by extension, language, version, platform (например, extension: py/js/ts/...), если только это не задано пользователем или не вытекает из валидированной проблемы.
- ❌ DON'T: Использовать малые лимиты (count < 10), если пользователь не указал ограничения/приоритет на скорость/ресурсы.
- ❌ DON'T: Применять freshness/time ограничение без пользовательской причины.
- 🚫 FORBIDDEN: Любой MCP-запрос c ограничениями по extension/language, если нет явного запроса → workflow обязан сделать STOP и запросить явную спецификацию у пользователя.

**REQUIRED WORKFLOW:** Перед любым ограничением MCP параметров:
- Подтверждаю, что пользователь либо:
  - (а) явно задал extension/language/platform/freshness
  - (б) задача не может быть решена иначе (critically domain-specific)
- Документирую причину ограничения (запрос/user spec/обоснование)
- Если не выполнено — STOP, вернуть управление пользователю, запросить clarification/explanation

**Примеры недопустимого запроса:**
octocode.searchCode({ query: "authentication", extension: "py" }) // Запрещено без user-input
brave.webSearch({ query: "best practices", count: 3 }) // Недопустимо маленький лимит

**Примеры допустимого:**
octocode.searchCode({ query: "authentication", limit: 12 }) // Хорошо по умолчанию

---


## PROBLEM-SPECIFIC DATA REQUIREMENTS

🚨 THIS STEP REQUIRES ACTUAL DATA FROM USER'S PROBLEM

**ENFORCEMENT:** Любое появление generic, placeholder, example data — абсолютно запрещено. Если хотя бы один из пунктов "Data Validation Before Proceeding" не проходит или обнаружен placeholder/template/incomplete input — workflow обязан сделать STOP: оставить подробную причину (где/что именно невалидно), вернуть управление пользователю и запросить валидные, полностью problem-specific данные.

FORBIDDEN - Generic Processing:
- Working with placeholder "[user_problem]"
- Using example data instead of real data
- Proceeding without user's specific information
- Copying template text into output

REQUIRED - Problem-Specific Processing:
- Obtain user's actual problem description
- Use user's actual constraints/requirements
- Reference user's actual context
- Fill templates with real data from this decision

Data Validation Before Proceeding:

Check 1: Do I have user's actual problem?
User's Problem: "[actual description from user]"
Validation:
- Is this specific? [Yes/No]
- Is this the real problem? [Yes/No]
- Is this complete enough? [Yes/No]
If any No → STOP — ask user for clarification, workflow не продолжается!

Check 2: Do I have problem-specific context?
Context Available:
- Technical context: [actual technical details]
- Business context: [actual business constraints]
- Timeline: [actual deadline/timeframe]
- Resources: [actual team/budget/tools]
- Constraints: [actual limitations]
If any missing → STOP — ask user to provide, workflow не продолжается!

Check 3: Am I using this data in my work?
Review your output:
- Does it reference user's specific problem? [Yes/No]
- Does it use user's actual constraints? [Yes/No]
- Is it customized to user's context? [Yes/No]
- Would this work for a different problem? [If Yes → too generic]
If too generic → STOP — redo with problem-specific data

BEFORE EACH SECTION:
Ask yourself: "Am I working with real data or placeholders?"
- If placeholders → STOP — get real data first
- If real data → verify it's being used

ANTI-GENERIC CHECKLIST:
- [ ] No "[placeholder]" text in output
- [ ] No "for example" scenarios unless supplementing real analysis
- [ ] No generic template text unmodified
- [ ] All factors/criteria are specific to this problem
- [ ] All evidence relates to this problem
- [ ] All options address this problem specifically

## STEP GOAL:

To review evidence requirements from the decision framework and systematically identify available sources across all requirement categories.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative evidence planning, not unilateral research design
- ✅ You bring systematic identification frameworks and source categorization
- ✅ User brings domain knowledge and source access insights
- ✅ Together we establish comprehensive evidence collection foundation

### Step-Specific Rules:

- 🎯 Focus only on requirements review and source identification (not collection)
- 🚫 FORBIDDEN to collect evidence or assess quality yet
- 💬 Approach: Systematic source identification with comprehensive coverage
- 📋 Document all requirements and potential sources

## EXECUTION PROTOCOLS:

- 🎯 [protocol 1] Review evidence requirements — ТОЛЬКО по реальной задаче пользователя!
- 💾 [protocol 2] Источники фиксируются с точной конкретикой, без placeholder!
- 📖 [protocol 3] Подготовить foundation ТОЛЬКО на базе данных из user input, MCP discovery и validated перечней
- 🚫 **FORBIDDEN: Generic Examples** - Do not use "[user_problem]", "[example]", "[placeholder]"
- ✅ **REQUIRED: Problem-Specific Data** - Use actual data from user's real problem

## CONTEXT BOUNDARIES:

- Available context: Decision framework established in step-2
- Focus: Requirements review and source identification
- Limits: Do not collect evidence or make quality assessments
- Dependencies: Evidence needs defined in decision framework

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 0. CRITICAL GATE: Problem-Specific Evidence Check

"**Проверяю что evidence categories реально соответствуют problem context...**"

🚨 MANDATORY BEFORE EVIDENCE GATHERING

**ENFORCEMENT:** Если среди evidence categories обнаружен placeholder, generic template, [evidence_type], [source_example] или хотя бы одна категория невалидно "универсальна" — workflow немедленно делает STOP: записывает проблему (вид и причину generic-детекции), возвращает управление пользователю для уточнения/документирования реальных evidence categories по данной задаче. Никаких проходов дальше до полной кастомизации категорий под задачу пользователя.

Evidence categories must be customized to this problem:

Check 1: How many evidence categories are generic templates?
- Count: [X] generic categories
- Count: [Y] problem-specific categories
- Target ratio: 0% generic, 100% problem-specific

Check 2: For each evidence category, verify:
- Is this category relevant to THIS problem? [Yes/No]
- Is this category required by THIS problem? [Yes/No]
- Would skipping this category harm decision? [Yes/No]

Check 3: Are missing categories?
- What problem aspects need evidence? [list]
- What evidence categories support these? [map]
- Are all necessary categories included? [Yes/No]

GATE RULES:
- Если >30% generic templates — STOP, невозможно продолжить, требуется перегенерация списков под задачу
- Если любой evidence category не привязана явно к специфике задачи — STOP
- Только после явного подтверждения от пользователя о кастомизации всех категорий возможен продолжение workflow

ANTI-GENERIC ENFORCEMENT:
- NO "[evidence_type]" placeholders in categories
- NO "[source_example]" without actual source identification
- NO generic lists - must be customized to this problem

### 1. MCP Tool Discovery

"**Запускаю определение MCP инструментов для evidence gathering...**"

**Phase 1.1: Available MCP Assessment (🚨 HARD ENFORCEMENT!)**
- Ты ОБЯЗАН реально проверить, какие MCP tools есть в текущем окружении
- Запрещено писать гипотетический список — только актуальный, реальный перечень
- Ты ДОЛЖЕН:
  1. Вызвать list_tools() или аналог MCP для каждого сервера
  2. Сформировать два списка:
     - "Available MCP tools: [фактические]"
     - "Desired but unavailable: [аналитика, почему, какой нужен]"
  3. Не выводи ни одной утилиты, не подтверждённой ping'ом/списком утилит
- MUST DOCUMENT:
  - Какие есть фактически
  - Какие нужны, но отсутствуют
  - Причины, насколько это блокирует задачу

🚫 FORBIDDEN:
- Упоминать несуществующие MCP-инструменты (не прошедших discovery)
- Продолжать работу без enforcement-документации
- Любая симуляция наличия инструмента — критический violation!

**ПРИМЕР (корректный):**
Available MCP tools: brave-search-mcp, perplexity-mcp, sequentialthinking
Desired but unavailable: octocode-mcp (нет соединения), context7-mcp (не установлен)

**Phase 1.2: Domain-Specific Tool Selection**
```javascript
// Выбор инструментов по типу проблемы
const problemDomain = classifyProblemDomain();
const selectedTools = selectMCPToolsForDomain(problemDomain, availableMCPs);
```

**Phase 1.3: Tool Readiness Check**
```javascript
// Проверка готовности выбранных инструментов
const readyTools = selectedTools.filter(tool => isToolReady(tool));
```

### 2. MCP-Enhanced Evidence Requirements Analysis

"**Анализирую evidence requirements с помощью адаптивного MCP стека...**"

**Load and enhance evidence requirements from {outputFile}:**
- Technical evidence needs (enhanced by active MCP tools)
- Business evidence needs (enhanced by active MCP tools)
- Operational evidence needs (enhanced by active MCP tools)
- Risk evidence needs (enhanced by active MCP tools)

**MCP-Enhanced Validation:**
- All requirement categories defined
- Source types identified by research
- Collection methods suggested by MCP analysis

### 2. Identify Evidence Sources

"**Определяю доступные evidence sources...**"

**Source Categories:**

**Internal Sources (SPECIFIC TO USER'S ORGANIZATION):**

**🚨 YOU MUST ASK USER ABOUT THEIR ACTUAL SOURCES**

Don't list generic source types. Instead:

**Task 1: Identify user's available internal sources (🚨 HARD ENFORCEMENT — NO GENERIC!)**
- Ты ОБЯЗАН запросить строго problem-specific данные:
  - "У вас есть конкретная документация по [problem area]? Как называется документ, где он хранится?"
  - "Есть ли у вас исторические данные по похожим ситуациям? Где они лежат? Какой объем?"
  - "Кто из вашей команды обладает экспертизой в [relevant domain]? ФИО, роль, что именно умеет?"
  - "Делались ли подобные проекты? Как назывались, каковы результаты/выводы?"

🚨 USER INPUT VALIDATION
- Каждый ответ должен быть максимально конкретен:
  - Название, путь/хранилище, ответственный человек
  - Нет общих ('что-то есть', 'кто-то знает') — эти ответы считаются невалидными!
- Если ответ расплывчат — ТРЕБУЙ ДЕТАЛИЗАЦИЮ (пример: "Какой именно документ? Кому он принадлежит?")

- ВАЖНО: После получения данных разбей всё по категориям:
  - Internal Sources Available:
    - Документ/отчёт: [название, путь, владелец]
    - Дата/данные: [описание, местоположение]
    - Эксперт: [ФИО, специализация, контакты]
    - Проект: [название, результат]

  - Internal Sources NOT Available:
    - [описать причину и критичность]

- На каждый пункт фиксируй, что есть/нет, критично/некритично, возможно ли создать substitute, требуется ли external research

🚫 FORBIDDEN:
- Любой generic ответ — это violation, требуется ручная доработка и уточнение у пользователя!

**External Sources:**
- Industry research and reports
- Competitor analysis
- Market data and trends
- Regulatory requirements

**Expert Sources:**
- Domain specialists
- Technical experts
- Industry consultants
- Academic research

**Data Sources:**
- Quantitative metrics and KPIs
- Qualitative assessments
- Benchmarking data
- Performance analytics

### 3. Map Sources to Categories

"**Сопоставляю sources с requirement categories...**"

**Technical Evidence Sources:**
- [List specific sources for technical requirements]

**Business Evidence Sources:**
- [List specific sources for business requirements]

**Operational Evidence Sources:**
- [List specific sources for operational requirements]

**Risk Evidence Sources:**
- [List specific sources for risk requirements]

### 4. Prepare Evidence Gathering Strategy

"**Подготавливаю evidence gathering strategy для identified categories...**"

### 5. Identify MCP Evidence Enhancement Opportunities

"**Определяю де MCP може enhance evidence gathering...**"

MCP AVAILABILITY CHECK:
[ ] Which MCPs are available for this evidence gathering?
[ ] What problem-specific intelligence can they provide?
[ ] Which evidence gaps can MCPs help fill?

FOR EACH EVIDENCE CATEGORY:
- Category: [name]
- Evidence Status: [complete/partial/gaps]
- MCP Capability Available: [Yes/No]
- MCP Enhancement Potential: [High/Medium/Low]
- MCP Query to Execute: [if available: actual query]

EXAMPLE FORMAT:
```
Category: "Market Size & Growth Trends"
Evidence Status: Partial (have general trends, need specific segment data)
MCP Available: Yes (Web Search + Market Research MCP)
Enhancement: High (can get current quarter data + projections)
MCP Query: "What is current market size for [specific_segment] and projected growth rate for [timeline]?"
```

MCP INTEGRATION RULE:
- Do NOT assume all MCPs are available
- DO VERIFY actual MCP capability for this problem
- DO execute queries for actual evidence enhancement
- DO document which MCPs were used and what evidence they provided

Evidence Gathering Plan:

### 6. Document Source Identification

"**Документирую source identification в consilium report...**"

Update {outputFile} with source identification:

```markdown
## Evidence Source Identification

### Evidence Requirements Review
**Framework:** Decision Block v2.0 established in Step 2
**Categories:** Technical, Business, Operational, Risk
**Requirements Validated:** [yes/no] - all categories properly defined

### Source Categories Identified

#### Internal Sources
- **Documentation:** Existing system docs, policies, procedures
- **Historical Data:** Past projects, performance metrics, incident reports
- **Team Knowledge:** Subject matter experts, operational experience
- **Current State:** Active systems, processes, capabilities

#### External Sources
- **Industry Research:** Market reports, analyst insights, trends
- **Competitive Intelligence:** Competitor analysis, benchmarking data
- **Regulatory Requirements:** Compliance standards, legal constraints
- **Market Data:** Economic indicators, industry statistics

#### Expert Sources
- **Technical Experts:** System architects, developers, IT specialists
- **Business Experts:** Financial analysts, strategic planners, executives
- **Operational Experts:** Process owners, department heads, managers
- **Risk Experts:** Compliance officers, auditors, security specialists

#### Data Sources
- **Quantitative:** KPIs, metrics, performance indicators, benchmarks
- **Qualitative:** Surveys, interviews, assessments, expert opinions
- **Transactional:** System logs, audit trails, usage statistics
- **Observational:** Process observations, user behavior analysis

### Category-Source Mapping

#### Technical Evidence Sources
- **Internal:** System documentation, architecture diagrams, technical specs
- **External:** Technology trends, vendor capabilities, industry standards
- **Expert:** IT architects, system administrators, developers
- **Data:** Performance metrics, system logs, capacity reports

#### Business Evidence Sources
- **Internal:** Business plans, financial reports, strategic objectives
- **External:** Market analysis, competitor intelligence, economic data
- **Expert:** Business analysts, executives, financial officers
- **Data:** ROI calculations, budget data, revenue projections

#### Operational Evidence Sources
- **Internal:** Process documentation, workflow diagrams, training materials
- **External:** Industry best practices, operational benchmarks
- **Expert:** Process owners, department managers, operations leads
- **Data:** Process metrics, efficiency reports, resource utilization

#### Risk Evidence Sources
- **Internal:** Risk registers, incident reports, compliance documentation
- **External:** Industry risk reports, regulatory changes, threat intelligence
- **Expert:** Risk managers, compliance officers, security specialists
- **Data:** Risk metrics, audit findings, incident statistics

### Source Readiness Assessment
✅ **Requirements Reviewed** - All categories properly defined
✅ **Sources Identified** - Comprehensive coverage across all types
✅ **Categories Mapped** - Clear linkage between sources and requirements
✅ **Readiness Confirmed** - Foundation established for evidence collection
```

### 5. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
---
# Document Identity
consiliumId: "EMB-CSL-[timestamp]"
title: "EMBER Consilium Report: [user's decision topic]"
created: "[ISO date when started]"
lastUpdated: "[ISO date now]"

# Workflow Progress
stepsCompleted:
  - 'step-[previous steps]'
  - '[current step name]'  # ADD THIS STEP
progress: [XX]  # Current progress percentage
currentPhase: '[current phase name]'
lastStep: '[current step name]'

# Phase Completion Flags
complexityAssessmentComplete: [true/false]
problemAnalysisComplete: [true/false]
decisionFrameworkApplicationComplete: [true/false]
evidenceCollectionComplete: [true/false]
evidenceValidationComplete: [true/false]
matrixSetupComplete: [true/false]
scoringApplicationComplete: [true/false]
[other phase flags as applicable]

# Decision Status
status: "[PHASE_NAME_COMPLETE]"
nextStep: "[next step file name]"

# Quality Metrics
overallConfidence: [0-100]
evidenceQuality: [0-100]
criticalGaps: [count]

# User Context
userName: "[user name]"
decisionDomain: "[technical/business/operational/etc]"
decisionComplexity: "[Light/Standard/Comprehensive]"
---

Frontmatter Validation Checklist:
- [ ] consiliumId exists and unique
- [ ] title reflects user's actual decision
- [ ] stepsCompleted array includes current step
- [ ] progress percentage updated correctly
- [ ] currentPhase matches current work
- [ ] lastStep is current step name
- [ ] Appropriate completion flag set to true
- [ ] status reflects current state
- [ ] nextStep points to correct file

IF ANY FIELD IS MISSING OR WRONG:
- Correct it before proceeding
- Verify against step requirements
- Do not skip fields
```

### 6. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Evidence Gathering"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper source identification
- IF P: Execute {partyModeWorkflow} to discuss evidence sources with other agents
- IF C: Save source identification to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#6-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

---

### X. CRITICAL GAPS CHECK

**🚨 BEFORE PROCEEDING - VERIFY NO CRITICAL GAPS**

Critical Gap Definition:
A gap is CRITICAL if:
- It affects must-have success criteria
- It prevents meaningful evaluation of options
- It creates unacceptable uncertainty in decision
- It could lead to fundamentally wrong decision

Gap Assessment:
Step 1: Review All Documented Gaps
- Evidence gaps from step-03
- Validation gaps from step-03d
- Analysis gaps from current step
- User input gaps (questions not answered)

Step 2: Classify Each Gap
Gap Classification:
[Gap description]
├─ Severity: [Critical / Important / Minor]
├─ Impact: [What decision aspect it affects]
├─ Can proceed without it? [Yes/No]
└─ Mitigation: [How we're handling it]

Step 3: Critical Gap Decision Tree (🚨 HARD ENFORCEMENT!)
- IF critical_gaps_exist AND cannot_proceed (нет способа преодолеть/заменить, must-have req отсутствует):
    - STOP => workflow должен остановиться до получения user input/документации
    - Document требуется input: что, откуда, кто ответственный, срок
    - WAIT: ни один следующий шаг не выполняется до устранения

- IF critical_gaps_exist AND can_mitigate:
    - MUST document mitigation (какая стратегия, какие substitute, что NOT ideal)
    - Confidence ∆ (снижение confidence процентно) — если ниже 30%, требуется explicit user approval (WAIT до получения)
    - Без approval — НЕ двигаться

- IF no_critical_gaps:
    - Сравнивай каждый must-have критерий с наличием источников
    - Confidence должен быть явно проставлен (concrete number)
    - FIX: если вдруг что-то стало недоступно в ходе выполнения — STOP и вернуться к получению данных

🚫 FORBIDDEN:
- Продвигаться дальше, если gap непреодолим или confidence < threshold без explicit user decision

YOU MUST DOCUMENT:
## Critical Gaps Assessment
- Critical Gaps Identified: [count]
- Can Proceed? [Yes/No/With Limitations]
- Mitigation Strategy: [if applicable]
- Confidence Reduction: -[X]%
- User Approval: [Obtained / Pending]

BLOCKING RULES:
- If any critical gap cannot be mitigated → MUST stop and get user input
- If confidence would drop below 30% due to gaps → MUST flag for user review
- If must-have criteria cannot be evaluated → MUST stop until gap filled

---

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and source identification is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin evidence gathering.

---

## 🔒 MANDATORY SELF-VALIDATION PROTOCOL

HOW TO USE THIS VALIDATION (🚨 HARD ENFORCEMENT):
1. Пройдите буквально каждый чек — визуально и вручную, НИ ОДНОГО ПРОПУЩЕННОГО
2. Любой сомнительный пункт обязан быть доработан до состояния "✅ выполнено"
3. Если какая-то галка не выставляется — ОСТАНОВИТЬ работу, не переходить к следующему шагу!
4. Если чеклист не полон — дополни, если не покрывает новый enforcement — расширь!

---

### VALIDATION CATEGORY 1: Work Completion

[ ] Check 1.1: All MANDATORY SEQUENCE steps completed
- Review: MANDATORY SEQUENCE section in this file
- Count: How many steps? [___]
- Verify: I completed step , step , ... step [N]

[ ] Check 1.2: No steps skipped
- Review: MANDATORY SEQUENCE again
- Confirm: I did not skip any steps

[ ] Check 1.3: Work was executed, not simulated
- Review: My output
- Confirm: I used present tense ("I analyzed..."), not conditional ("I would...")
- Confirm: I showed actual results, not placeholders

[ ] Check 1.4: User input obtained where required
- Review: All "Ask user:" prompts
- Confirm: I asked each question and got response

[ ] Check 1.5: Problem-specific data used
- Review: My output
- Confirm: It uses user's actual problem (not generic)
- Confirm: No "[placeholder]" text remains

---

### VALIDATION CATEGORY 2: Output Documentation

[ ] Check 2.1: Work saved to outputFile
- Open file, verify changes exist
- File size > [previous size]?

[ ] Check 2.2: Frontmatter updated correctly
- stepsCompleted, progress, currentPhase, lastStep current?
- If errors → fix!

[ ] Check 2.3: Content actually added
- All content in file, not just frontmatter

---

### VALIDATION CATEGORY 3: Menu Interaction

[ ] Check 3.1: Menu displayed to user
- Capture menu text from output

[ ] Check 3.2: User input received
- Waited for input (A/P/C/question)?

[ ] Check 3.3: Choice handled correctly
- If A: advanced elicitation executed?
- If P: party mode?
- If C: proceeding to next step?

[ ] Check 3.4: Return to menu if not C
- After A/P/question: menu redisplayed?

---

### VALIDATION CATEGORY 4: Next Step Preparation (if 'C' selected)

[ ] Check 4.1: Correct next step file path and existence
- nextStepFile: {nextStepFile}
- File actually exists?

[ ] Check 4.2: Complete file loading
- Plan to load entire file, not partial

[ ] Check 4.3: Read before executing
- Step goal understood
- MANDATORY SEQUENCE of next step studied

[ ] Check 4.4: Ready to execute
- Can describe next step purpose in own words?

---

### VALIDATION CATEGORY 5: Quality Checks

[ ] Check 5.1: No insurmountable critical gaps
- Compare with CRITICAL GAPS CHECK section

[ ] Check 5.2: Confidence level matches data
- At least 30%? Or user permission for lower confidence?

[ ] Check 5.3: MCP tools called as needed
- If MCP calls required → executed/documented

[ ] Check 5.4: Based on data, not assumptions
- Real sources, references, data used

---

### FINAL VALIDATION DECISION

Checked boxes count: [___] / [total]

IF ALL CHECKED:
✅ Validation PASSED
→ If 'C' selected → proceed to next step
→ If A/P/question → return to cycle

IF ANY UNCHECKED:
❌ Validation FAILED
- Fill gaps, fix violations
- Re-run validation

Violation Report (if any)
```
Unchecked items:
- [Check X.X]: [description]
...

What needs to be done:
1. [Fix what]
...
```

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS
### ✅ SUCCESS:

- Evidence requirements reviewed comprehensively
- Source categories identified systematically
- Requirements mapped to sources clearly
- Identification documented transparently
- Progress updated to 32% with identification foundation established

### ❌ SYSTEM FAILURE:

- Evidence requirements not reviewed comprehensively
- Source categories not identified systematically
- Requirements-source mapping incomplete or unclear
- Documentation inadequate or missing
- Foundation not properly established

**Master Rule:** Source identification establishes the collection framework - all categories must be systematically mapped to available sources.
