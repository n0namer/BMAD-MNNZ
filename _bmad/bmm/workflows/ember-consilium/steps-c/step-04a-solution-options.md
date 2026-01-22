---
name: 'step-04a1-solution-options'
description: 'Define and document solution options for matrix evaluation'

nextStepFile: './step-04b-factors-establishment.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
decisionFrameworks: '../data/decision-frameworks.md'
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 4a1: Solution Options Definition

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
- **FORBIDDEN:** Выводить "[user_problem]", "[example]", "[placeholder]", шаблонные фрагменты или любые non-specified stub/pseudo fields
- **REQUIRED:** Использовать только реально предоставленные пользователем данные. Если встречается placeholder, example, generic list/template — workflow обязан остановиться: сформировать STOP-branch, вернуть управление пользователю, запросить реальный problem-specific input. Любая попытка вывести generic (например, "[solution_option]") — жёсткий STOP и документирование причины нарушение.

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

**ENFORCEMENT:** STOP-branch обязателен при появлении любого generic/placeholder/неконкретного поля — дальнейшая обработка невозможна, документируется причина, требуется explicit user-specific контекст.

## 🚨 MCP PARAMETER ANTI-RESTRICTION RULES

**ENFORCEMENT:** Строго запрещается ограничивать MCP-запросы параметрами (extension, language, platform итд) без explicit user-input или подтверждённой доменной необходимости. Любое ограничение (например, extension: py, js, ts, etc; count < 10; freshness overly narrow) без явного требования пользователя или обоснования задачи — критическое нарушение, жёсткий STOP:

- ❌ DON'T: Ограничивать extension, language, platform если нет явного запроса или domain-specific обоснования (подтверждение в output)
- ❌ DON'T: Ставить небольшие лимиты (count < 10), если нет запроса на ресурсы/быстродействие
- ❌ DON'T: Применять freshness/time range без причины пользователя
- 🚫 FORBIDDEN: Любой MCP-запрос с ограничениями, не обоснованными ausdrücklich user-requirement/domain necessity → workflow немедленно STOP, запись причины, запрос на clarification/explanation от пользователя

**REQUIRED WORKFLOW:**
- Перед наложением ограничений MCP-запросов — проверить и записать явный user-input или domain necessity
- Документировать причину ограничения
- Если не выполнено — STOP и возврат управления и запроса к пользователю

**Примеры недопустимых запросов:**
octocode.searchCode({ query: "authentication", extension: "py" }) // Запрещено без user-input
brave.webSearch({ query: "best practices", count: 3 }) // Недопустимо маленький лимит

**Примеры допустимых:**
octocode.searchCode({ query: "authentication", limit: 12 }) // Хорошо по умолчанию

---

## PROBLEM-SPECIFIC DATA REQUIREMENTS

🚨 THIS STEP REQUIRES ACTUAL DATA FROM USER'S PROBLEM

**ENFORCEMENT:** Любое появление generic, placeholder, example data — абсолютно запрещено. Если хотя бы один из пунктов "Data Validation Before Proceeding" не проходит или обнаружен placeholder/template/incomplete input — workflow обязан сделать STOP: зафиксировать проблему (где/что именно невалидно), вернуть управление пользователю и запросить валидные problem-specific данные, никаких проходов дальше до получения корректных данных.

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
If too generic → STOP — redo with problem-specific data, workflow не продолжается!

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

To systematically define and document solution options based on problem analysis and evidence findings for applicability matrix evaluation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative option definition, not unilateral solution design
- ✅ You bring systematic option generation frameworks and categorization
- ✅ User brings domain expertise and solution preferences
- ✅ Together we establish comprehensive option foundation

### Step-Specific Rules:

- 🎯 Focus only on solution options definition (not factor identification)
- 🚫 FORBIDDEN to identify context factors or establish criteria yet
- 💬 Approach: Comprehensive option generation with clear categorization
- 📋 Document all options with characteristics and rationale

## EXECUTION PROTOCOLS:

- 🎯 [protocol 1] Generate solution options — ТОЛЬКО по реальной задаче пользователя!
- 💾 [protocol 2] Document options with comprehensive characteristics
- 📖 [protocol 3] Prepare options foundation for factor evaluation
- 🚫 **FORBIDDEN: Generic Examples** - Do not use "[user_problem]", "[example]", "[placeholder]"
- ✅ **REQUIRED: Problem-Specific Data** - Use actual data from user's real problem

## CONTEXT BOUNDARIES:

- Available context: Decision framework and evidence from previous steps
- Focus: Solution option generation and documentation
- Limits: Do not identify factors or establish evaluation criteria
- Dependencies: Evidence foundation established in step-3

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Define Solution Options

"**Defining solution options for evaluation...**"

**Generate Solution Options:** Based on problem analysis and evidence gathered, identify potential solution approaches:

**Option Generation Process:**
- Review problem decomposition from step-1
- Consider evidence findings from step-3
- Identify viable solution categories
- Define specific implementation approaches

**Typical Solution Categories:**
- Technology solutions (new systems, upgrades, integrations)
- Process solutions (workflow changes, procedure updates)
- Organizational solutions (team restructuring, training)
- Hybrid solutions (combination approaches)

**Solution Option Template:**
- **Option Name:** [Descriptive identifier]
- **Category:** [Technology/Process/Organizational/Hybrid]
- **Description:** [Key characteristics and approach]
- **Rationale:** [Why this option addresses the problem]
- **Key Differentiators:** [Unique aspects vs other options]

### 2. Document Options in Report

"**Documenting solution options in the consilium report...**"

Update {outputFile} with solution options:

```markdown
## Solution Options for Evaluation

### Option Generation Process
**Based on:** Problem analysis (Step 1) and evidence findings (Step 3)
**Categories Identified:** Technology, Process, Organizational, Hybrid
**Total Options Generated:** [count]

### Solution Option Details

#### Option 1: [Option Name]
**Category:** [Technology/Process/Organizational/Hybrid]
**Core Description:**
[Detailed description of the solution approach]

**Key Characteristics:**
- [Characteristic 1]: [description]
- [Characteristic 2]: [description]
- [Characteristic 3]: [description]

**Problem Addressed:**
[How this option addresses the core problem identified in Step 1]

**Evidence Support:**
[Supporting evidence from Step 3 findings]

**Key Differentiators:**
[What makes this option unique compared to alternatives]

#### Option 2: [Option Name]
[... same structure as Option 1 ...]

#### Option 3: [Option Name]
[... same structure as Option 1 ...]

#### [Additional options as needed...]

### Option Categories Summary

#### Technology Solutions ([count])
- **Primary Focus:** System capabilities, technical architecture
- **Key Considerations:** Integration, scalability, maintainability
- **Evidence Base:** Technical requirements and constraints

#### Process Solutions ([count])
- **Primary Focus:** Workflow optimization, procedure changes
- **Key Considerations:** Change management, adoption barriers
- **Evidence Base:** Process inefficiencies and improvement opportunities

#### Organizational Solutions ([count])
- **Primary Focus:** Team structure, skills development, culture
- **Key Considerations:** Change management, training requirements
- **Evidence Base:** Organizational capabilities and gaps

#### Hybrid Solutions ([count])
- **Primary Focus:** Multi-dimensional approaches combining elements
- **Key Considerations:** Integration complexity, coordination requirements
- **Evidence Base:** Systemic issues requiring comprehensive solutions

### Option Evaluation Readiness
✅ **Options Defined** - [count] solution options documented
✅ **Categories Established** - Options properly categorized
✅ **Characteristics Documented** - Key features and differentiators identified
✅ **Rationale Provided** - Problem-solution fit explained
✅ **Evidence Linked** - Options connected to supporting evidence
```

### 3. Update Consilium Progress

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

### 4. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Factor Criteria"

#### Menu Handling Logic:

- IF C: **EXECUTE TRANSITION PROTOCOL:**

  **Phase 1: Save Current Work**
  1. Save all work to outputFile
  2. Update frontmatter (see Update Consilium Progress section)
  3. Verify file write succeeded
  4. Verify frontmatter was updated
  5. Read back file to confirm

  **Phase 2: Validate Completion**
  1. Run self-validation checklist
  2. Verify all checkboxes checked
  3. If any fail → fix before proceeding

  **Phase 3: Load Next Step**
  1. Identify next step file path: {nextStepFile}
  2. Verify file exists and is accessible
  3. Load ENTIRE file content (not partial)
  4. Verify load succeeded (check file size > 0)
  5. Count sections in loaded file
  6. Verify you can see all sections

  **Phase 4: Read Before Executing**
  1. Read the COMPLETE file content
  2. Identify: STEP GOAL
  3. Identify: MANDATORY SEQUENCE steps
  4. Identify: What this step produces
  5. Verify you understand what to do

  **Phase 5: Execute Next Step**
  1. Begin execution from Section 1 of next step
  2. Follow MANDATORY SEQUENCE exactly
  3. Do not skip any sections

  **VERIFICATION CHECKPOINTS:**
  Before loading next step:
  ✓ Current work saved
  ✓ Frontmatter updated
  ✓ Self-validation passed

  After loading next step:
  ✓ Entire file loaded (file size: [X] bytes)
  ✓ Can see all sections (counted: [N] sections)
  ✓ Understood STEP GOAL
  ✓ Understood MANDATORY SEQUENCE

  Ready to execute: YES/NO

  IF ANY CHECKPOINT FAILS:
  - STOP
  - Fix the failure
  - Re-run checkpoint
  - Only proceed when ALL pass

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and solution options are saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin factor criteria establishment.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Solution options systematically generated from evidence
- Options comprehensively documented with characteristics
- Categories properly established and applied
- Rationale and differentiators clearly explained
- Options linked to supporting evidence foundation
- Progress updated to 45% with options foundation established

### ❌ SYSTEM FAILURE:

- Solution options not systematically generated or incomplete
- Option documentation inadequate or missing characteristics
- Categories not properly established or applied inconsistently
- Rationale and differentiators not clearly explained
- Evidence linkage missing or insufficient

**Master Rule:** Solution options establish the evaluation foundation - all options must be comprehensively defined and evidence-supported.
