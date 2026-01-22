---
name: 'step-01a-problem-definition'
description: 'Capture decision problem, perform decomposition, and gather initial context'

nextStepFile: './step-01b-analysis-documentation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'


---

# Step 1a: Problem Definition & Decomposition

## STEP GOAL:

To capture the decision problem statement, perform systematic problem decomposition using Decision Block v2.0, and gather initial comprehensive context for evidence-based decision making foundation.

## MANDATORY EXECUTION RULES (READ FIRST):

## 🚨 ANTI-VIOLATION GUARDS

**These are common violations that you MUST NOT commit:**

### ❌ VIOLATION #1: Skipping Menu Display
**FORBIDDEN:** Proceeding to next step without showing menu to user
**REQUIRED:** Always display menu, always wait for user input 'C'

### ❌ VIOLATION #2: Simulating Work
**FORBIDDEN:** Using phrases like "I would analyze...", "Based on this, I would..."
**REQUIRED:** Actually do the work: "I am analyzing...", then show actual results

### ❌ VIOLATION #3: Generic Placeholders
**FORBIDDEN:** Outputting "[user_problem]", "[to_be_filled]", "[example]", или любые поля-заполнители
**REQUIRED:** Используется только реальный problem-specific user-input без placeholder/шаблонов. Любое появление placeholder, generic template, или невалидного user-provided data (например, "[problem]", "example context" и подобное) — это критический STOP: прекращайте workflow, фиксируйте причину и требуйте валидное описание от пользователя.

### ❌ VIOLATION #4: Skipping MCP Calls
**FORBIDDEN:** Not calling available MCP tools, or saying "I would call X"
**REQUIRED:** Actually call available MCP tools, document results

### ❌ VIOLATION #5: Partial File Loading
**FORBIDDEN:** Loading next step file partially or not reading it before execution
**REQUIRED:** Load ENTIRE file, read ALL content, then execute

### ❌ VIOLATION #6: No User Input
**FORBIDDEN:** Assuming user wants to continue, auto-proceeding without input
**REQUIRED:** Explicitly wait for user to type their choice

### ❌ VIOLATION #7: Skipping Sequence Steps
**FORBIDDEN:** Jumping ahead in MANDATORY SEQUENCE, skipping steps
**REQUIRED:** Follow sequence exactly in order, complete each step

### ❌ VIOLATION #8: Not Saving Work
**FORBIDDEN:** Displaying work to user but not saving to {outputFile}
**REQUIRED:** Save ALL work to {outputFile}, update frontmatter

**ENFORCEMENT:** При малейшем появлении generic, placeholder или незаполненного user-input работа останавливается, формируется подробный STOP-branch с фиксацией проблемы и запросом на корректный контекст пользователя. Вся дальнейшая обработка невозможна — workflow возвращает управление пользователю.

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You bring structured analytical frameworks and Decision Block v2.0 methodology
- ✅ User brings the specific decision problem and context
- ✅ Together we establish clear problem understanding foundation

### Step-Specific Rules:

- 🎯 Focus only on problem definition and initial context gathering
- 🚫 FORBIDDEN to perform full EMBER analysis or create reports yet
- 💬 Approach: Systematic decomposition with user collaboration
- 📋 Document problem elements and context comprehensively

### Anti-Simulation Enforcement

**FORBIDDEN PHRASES - YOU MUST NEVER USE THESE:**
- ❌ "I would analyze..."
- ❌ "I would document..."
- ❌ "We could..."
- ❌ "Based on user input, I would..."
- ❌ "This will be done..."
- ❌ "Assessment complete"

REQUIRED REPLACEMENTS:
Instead of: "I would analyze..."
Use: "I am analyzing... [show actual analysis results]"

## EXECUTION PROTOCOLS:

- 🎯 Use Decision Block v2.0 for systematic decomposition
- 💾 Document the complete user problem context
- 📖 Prepare the foundation for EMBER analysis
- 🚫 Do not go beyond problem definition at this step

- 🚫 **FORBIDDEN: Generic Examples** - Do not use "[user_problem]", "[example]", "[placeholder]"
- ✅ **REQUIRED: Problem-Specific Data** - Use only actual data from the user's real problem

---


## PROBLEM-SPECIFIC DATA REQUIREMENTS

🚨 THIS STEP REQUIRES ACTUAL DATA FROM USER'S PROBLEM

NO generic templates, NO "[user_problem]" placeholders!

DATA VALIDATION BEFORE PROCEEDING:

Check 1: Do I have user's actual problem?
- [ ] User described a SPECIFIC problem (not general category)
- [ ] Problem is REAL (not hypothetical/example)
- [ ] Problem description is COMPLETE enough to work with
- [ ] Problem is NOT a template placeholder

Check 2: Do I understand the problem context?
- [ ] WHO is affected by this problem? [actual stakeholders]
- [ ] WHAT exactly is happening? [specific symptoms]
- [ ] WHEN does this occur? [actual timing]
- [ ] WHERE in the system/process? [specific location]
- [ ] WHY is it a problem? [actual business impact]

Check 3: Can I proceed with this problem?
- [ ] Problem is specific enough to analyze [Yes/No]
- [ ] I have sufficient context [Yes/No]
- [ ] I can customize analysis to THIS problem [Yes/No]

ANTI-GENERIC ENFORCEMENT:
- [ ] No "[placeholder]" text in output
- [ ] No generic examples unmodified
- [ ] All factors/criteria are specific to this problem

IF ANY CHECK FAILS:
→ STOP here
→ Ask user for specific problem details
→ DO NOT proceed with generic template

---
name: 'step-01a-problem-definition'
description: 'Capture decision problem, perform decomposition, and gather initial context'

nextStepFile: './step-01b-analysis-documentation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

stepsCompleted:
  - 'step-01a-problem-definition'
progress: 15
currentPhase: 'problem-definition'
lastStep: 'step-01a-problem-definition'
problemDefinitionComplete: true

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

---
**Gap Assessment:**
- Review User Problem Statement, context, stakeholders, constraints
- Если что-то отсутствует/гипотетично: CLASSIFY → [Critical/Important/Minor], IMPACT → "Problem statement незаполнен" и др.
- Если cannot_proceed ⇒ STOP, запроси у пользователя

**YOU MUST DOCUMENT:**
```
## Critical Gaps Assessment

Critical Gaps Identified: [count]
[If > 0: list each with severity and impact]

Can Proceed? [Yes/No/With Limitations]

[If Yes with limitations]:
Mitigation Strategy: [описать]
Confidence Reduction: -[X]%
User Approval: [Obtained / Pending]

[If No]:
Required Information: [что нужно]
Who Can Provide: [user / external research / expert]
```

BLOCKING RULES:
- Если критический gap не устранён — STOP, запроси у пользователя
- Если confidence падает ниже 30% — ПОКАЗАТЬ пользователю эту проблему и ждать решения

---

## CONTEXT BOUNDARIES:

- Available context: Decision problem provided by user
- Focus: Problem understanding, stakeholder analysis, initial context
- Limits: Do not perform EMBER analysis or implementation evaluation
- Dependencies: Clear decision problem statement from user

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 0. Broad Research & Intelligence Gathering

"**EMBED Consilium запущен! Начинаю автономный сбор информации для evidence-based анализа.**"

**Phase 0.1: Initial Problem Capture**
```
User Problem Statement: [capture from previous context]
Analysis Scope: Автономный сбор данных без предвзятых предположений
```

**Phase 0.2: Broad Intelligence Gathering**
```
🔍 Активация разведочного поиска:

brave-search-mcp: Поиск "[user problem keywords]" - широкая разведка
perplexity-mcp: Анализ трендов и взаимосвязей технологий
sequentialthinking: Структурный анализ проблемы
```

**Phase 0.3: Information Synthesis**
```
Анализ результатов разведки:
- Ключевые технологии и понятия
- Существующие решения и подходы
- Тренды и best practices
- Потенциальные точки интеграции
```

### 0.5. Topic Classification & Problem Typing

"**Классифицирую тип проблемы на основе собранных данных...**"

**Classification Framework:**
```
Тип проблемы: [methodology/integration/tool-adoption/technical-implementation]
Сложность: [low/medium/high/critical]
Требуемые компетенции: [research/coding/analysis/integration]
Временные рамки: [quick/standard/deep]
```

**MCP Tool Selection Logic:**
```
ЕСЛИ проблема в методологии → perplexity-mcp + sequentialthinking
ЕСЛИ проблема в инструментах → octocode-mcp + brave-search-mcp
ЕСЛИ проблема в интеграции → sequentialthinking + context7-mcp (только если есть конкретная документация)
ЕСЛИ проблема в реализации → octocode-mcp + generate_explanation
```

### 1. Selective MCP Activation & Deep Analysis

"**Активирую оптимальный набор MCP инструментов на основе классификации...**"

**Phase 1.1: Tool Activation**
```
На основе классификации активирую:
[Список выбранных MCP с обоснованием]
```

**Phase 1.2: Deep Evidence Gathering**
```
Сбор evidence из выбранных источников:
- Технические спецификации
- Примеры реализации
- Сравнение альтернатив
- Оценка рисков и преимуществ
```

**Phase 1.3: Stakeholder & Context Analysis**
```
Анализ на основе собранных данных:
- Затронутые стороны и их интересы
- Технические ограничения и возможности
- Бизнес-контекст и требования
- Риски и факторы успеха
```

### 2. Evidence-Based Problem Formulation

"**Формирую problem definition на основе собранных evidence...**"

**Problem Statement Construction:**
```
Original Problem: [user input]
Evidence-Based Understanding: [synthesized from research]
Core Decision Elements: [identified from analysis]
Success Criteria: [derived from research and best practices]
```

**Decision Block v2.0 Application:**
```
Scope & Boundaries: [defined from research]
Stakeholder Impact: [analyzed from evidence]
Constraints: [identified from technical analysis]
Risk Assessment: [based on research findings]
```

### 3. Interactive Validation & Refinement

"**Валидирую понимание проблемы с пользователем...**"

**Validation Questions:**
```
На основе моего исследования, я понимаю проблему как: [formulation]
Верно ли это понимание? [Y]es / [N]o / [C]larify

Если нужно уточнение: Какие аспекты я понял неправильно?
Какая дополнительная информация важна для вас?
```

### 5. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01a-problem-definition']
progress: 15
currentPhase: 'problem-definition'
lastStep: 'step-01a-problem-definition'
problemDefinitionComplete: true
```

### 6. Present MENU OPTIONS (HARD ENFORCEMENT)

**Select an Option:** [C] Continue to Analysis Documentation

**Menu Handling Logic:**
- IF C: Сохраняется problem definition в {outputFile}, обновляется frontmatter stepsCompleted, ТОЛЬКО ПОСЛЕ ЭТОГО полностью загружается следующий файл, читается весь контент, начинается выполнение {nextStepFile}
- IF любой другой вопрос/комментарий: ответить пользователю → затем снова вывести меню (menu redisplay REQUIRED)

**HARD ENFORCEMENT GATES:**

**CRITICAL GATE 1 Menu Display is MANDATORY**
- Меню обязательно должно быть показано пользователю
- Нужно дождаться явного input пользователя
- Запрещено переходить дальше без меню
- Запрещено предполагать, что user хочет продолжить
- Нарушение: если меню не было показано → НЕГОДЯЩЕЕ выполнение

**CRITICAL GATE 2 User Input is MANDATORY**
- ВСЕГДА остановить выполнение и ждать ввода пользователя после меню
- Ввод пользователя должен быть явно: [C] или вопрос
- Продолжать дальше ТОЛЬКО если был ввод C
- Любой другой input — ответить, снова показать меню
- Нарушение: если продолжаешь без обязательного ввода пользователя — ОШИБКА В ПРОЦЕССЕ

**CRITICAL GATE 3 Menu Return Gate**
- При любом обработанном вопросе — обязательно вернуть menu
- Пропуск возвращения меню — критическая ошибка

**CRITICAL GATE 4 Verification Gate**
- При выборе [C], ВЕРИФИЦИРУЙ:
    1. Файл с problem definition сохранён (outputFile)
    2. stepsCompleted обновлён (frontmatter)
    3. Путь к следующему шагу корректен
    4. Следующий файл полностью загружается (не частично!)
    5. Файл читается до запуска любого кода

- Нарушение любой из этих gate — workflow FAILURE.

**CRITICAL GATE 5 YOU MUST VERIFY BEFORE PROCEEDING**
- НЕ ПРОДОЛЖАТЬ, если не пройдён весь self-validation checklist

**MANDATORY SELF-VALIDATION CHECKLIST:**  
(Заполнить ВСЕ ПУНКТЫ, иначе workflow violation!)

**Work Completion Verification:**
- [ ] Я выполнил ВСЕ шаги MANDATORY SEQUENCE
- [ ] НЕ пропустил ни одного шага
- [ ] НЕ симулировал работу (реальные действия, никакого "я бы...")
- [ ] Получил input пользователя там, где требуется — строго по проблеме
- [ ] Зафиксировал весь output сугубо problem-specific

**Output Documentation Verification:**
- [ ] Сохранил работу в {outputFile}
- [ ] stepsCompleted array обновлён и включает текущий шаг
- [ ] Проверил, что файл успешно сохранился
- [ ] В output отсутствуют шаблоны/placeholder/пример
- [ ] Все обязательные разделы присутствуют

**Menu Interaction Verification:**
- [ ] Показываю меню
- [ ] Жду ввода пользователя
- [ ] Получаю явный выбор (C/вопрос)
- [ ] В случае вопроса — корректно обрабатываю и возвращаю меню
- [ ] В случае C — начинаю следующий шаг

**Next Step Preparation Verification:**
- [ ] Проверяю корректный путь (nextStepFile)
- [ ] Загружаю ВСЮ информацию из файла
- [ ] Читаю файл ПОЛНОСТЬЮ перед выполнением
- [ ] Файл проверен на существование и доступность
- [ ] Знаю, что делать на следующем шаге

**VIOLATION DETECTION:**
- Если хоть один пункт не выполнен — workflow violation!
- Остановить выполнение, вернуться и исправить, перепроверить чеклист


## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and problem definition is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin analysis documentation.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Decision problem clearly captured and understood
- Problem systematically decomposed using Decision Block v2.0
- Initial context gathered across all dimensions
- Problem elements properly documented
- Progress updated to 15% with clear foundation established

### ❌ SYSTEM FAILURE:

- Problem statement not clearly captured or incomplete
- Decomposition not performed or inadequate
- Critical context missing from initial gathering
- Documentation incomplete or unclear
- Foundation not properly established
- **CRITICAL:** Menu not presented to user before proceeding
- **CRITICAL:** User input not received before continuing
- **CRITICAL:** Next step loaded without reading file completely
- **CRITICAL:** Work simulated instead of executed (e.g., "I would analyze..." instead of analyzing)
- **CRITICAL:** Generic placeholders used instead of problem-specific data

**Master Rule:** Problem definition establishes the foundation for all subsequent consilium work - it must be thorough and systematic.

## 🚨 ANTI-SIMULATION ENFORCEMENT

YOU ARE FORBIDDEN FROM:
- Использовать фразы "Я бы анализировал...", "Я бы собрал...", "Я бы задокументировал..."
- Говорить "Основываясь на вводе пользователя, я бы..." при отсутствии реального ввода
- Создавать generic examples вместо реального анализа
- Пропускать шаги и говорить "Это обычно делается..."
- Показывать placeholder/text или "to-be-filled" в выводе

YOU MUST INSTEAD:
- Выполнить работу — "Я анализирую...", затем показать реальные результаты
- Ждать input от пользователя перед переходом к следующим шагам
- Создавать полностью problem-specific контент по реальной задаче
- Заполнить весь output реальными данными, исключая шаблоны
