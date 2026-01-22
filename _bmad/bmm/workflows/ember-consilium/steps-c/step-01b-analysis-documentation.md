name: 'step-01b-analysis-documentation'
description: 'Perform EMBER analysis, identify gaps, and initialize consilium report'

nextStepFile: './step-02a-decision-framework.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

---

# Step 1b: EMBER Analysis & Documentation

## STEP GOAL:
Выполнить initial EMBER-аналитику, выявить все знания и пробелы, создать расширенное problem analysis резюме, и инициализировать foundation для EMBER consilium отчёта.

---

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
- **FORBIDDEN:** Выводить "[user_problem]", "[example]", "[placeholder]", шаблонные фрагменты
- **REQUIRED:** Использовать только реально предоставленные пользователем данные

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

## 🚨 MCP PARAMETER ANTI-RESTRICTION RULES

**FORBIDDEN RESTRICTIVE PARAMETERS:**
- ❌ Не ограничивайте параметры MCP без четкой причины (язык, лимиты, фильтры)
- Ограничивайте только если это явно указано пользователем или требуется проблемой

**PARAMETER REVIEW CHECKLIST:**
- [ ] extension — по умолчанию не указывать!
- [ ] limit/count — не менее 10
- [ ] freshness — не чрезмерно сужающий
- [ ] любые фильтры — только по необходимости

---

## EXECUTION PROTOCOLS (UPDATED):

- 🎯 Провести реальную EMBER-аналитику (не описывать, а делать)
- 💾 Выявить и ранжировать все реальные knowledge gaps
- 📖 Инициализировать consilium report с результатами анализа
- 🚫 Только анализировать, не переходить к оценке решений

- 🚫 **FORBIDDEN: Generic Examples** — нельзя использовать "[user_problem]", "[example]", "[placeholder]"
- ✅ **REQUIRED: Problem-Specific Data** — использовать только реальные пользовательские данные

---

## PROBLEM-SPECIFIC DATA REQUIREMENTS

**🚨 ОБЯЗАТЕЛЬНО: ВСЯ АНАЛИТИКА ДОЛЖНА БЫТЬ ПО РЕАЛЬНОЙ ПРОБЛЕМЕ ПОЛЬЗОВАТЕЛЯ**

- Запрещено использовать шаблоны, примеры, placeholder-сценарии
- Валидируйте, что у вас есть реальные данные, и что вы их используете (см. чеклисты пользователя)
- Запросите детализацию у пользователя, если данных недостаточно

---

## CONTEXT BOUNDARIES

- Доступен контекст: завершён problem definition (step-01a)
- Фокус: EMBER анализ, выявление пробелов, инициализация отчёта
- Запрещено: любые попытки перехода к генерации/оценке решений
- Все действия строго пошагово

---

## MANDATORY SEQUENCE

**СОБЛЮДАЙТЕ ЧЕТКО ВСЮ ПОСЛЕДОВАТЕЛЬНОСТЬ. НЕЛЬЗЯ ПРОПУСКАТЬ/ПЕРЕМЕЩАТЬ ШАГИ.**

### 1. Load Problem Definition

"**Загружаю problem definition из предыдущего шага...**"

Получить полный текст, исходники стейкхолдеров и начальный контекст из {outputFile}.

### 2. Perform Initial EMBER Analysis

"**Запускаю initial EMBER analysis для problem insights...**"

**🚨 NOTE: "EMBED Analysis" is a placeholder name. This means:**
- Use YOUR analytical capabilities to assess the problem
- Use available MCP tools (brave-search, perplexity, etc.) to gather insights
- Use systematic questioning to identify gaps
- Do NOT wait for a special "EMBED tool" that doesn't exist

**Analysis Tasks You MUST Complete:**

**Task 1: Problem Complexity Assessment**
- Ask user: "On scale 1-5, how complex do you consider this problem?"
- Analyze: Number of interconnected factors
- Analyze: Number of unknowns vs knowns
- Document complexity score with rationale

**🚨 USER INPUT VALIDATION**
After asking user:
- Validate: Ответ специфичен (не "не знаю", не "сложно сказать")
- Запросить пример — "Что именно делает проблему сложной/простой?"
- Если ответ расплывчатый, запросить детализацию (см. шаблон Problem #25)

**Task 2: Stakeholder Impact Analysis**
- Review stakeholders identified in step-01a
- For each stakeholder: assess impact level (high/medium/low)
- Identify potential conflicts between stakeholder interests
- Document impact assessment

**🚨 USER INPUT VALIDATION**
Проверьте, дал ли пользователь достаточно подробную разбивку по стейкхолдерам:
- Нет ли пропусков, нет ли слишком общих ответов ("все важны")
- Если не хватает конкретики — запросите детали, приведите пример

**Task 3: Critical Success Factor Identification**
- Ask user: "What would make this decision definitely successful?"
- Extract must-have requirements
- Prioritize factors by criticality
- Document top 3-5 critical success factors

**🚨 USER INPUT VALIDATION**
- Ответ пользователя должен содержать измеримые/ясные успех-факторы, а не шаблонные ("ну чтобы было хорошо")
- Если ответ неопределён, пример: "Что именно означает успех? [Например: performance X, стоимость Y, достижение Z]"
- Если недостаточно — повторно запросить детали

**Task 4: Initial Risk Identification**
- Ask user: "What are your main concerns about this decision?"
- Identify technical risks
- Identify business risks
- Identify timeline risks
- Document risk catalog

**🚨 USER INPUT VALIDATION**
- Ответ пользователя должен раскрывать спектр рисков (не просто "чтобы ошибок не было")
- Если мало/расплывчато — дать примеры ("Риск 1: нехватка экспертизы", "Риск 2: дедлайны", и т.д.)
- Пройтись по каждому risk category, пока не будет конкретики

### 3. Identify Knowledge Gaps

"**Определяю knowledge gaps для comprehensive analysis...**"

- Проверить, что отсутствует
- Ранжировать: критические, важные, второстепенные

### 4. Create Problem Analysis Summary

"**Формирую comprehensive problem analysis summary...**"

- Всё структурировать по: statement, core decision, stakeholders, criteria, контексту и т.д.

### 5. Initialize Consilium Report

- Создать {outputFile} по шаблону (см. ниже)
- Обеспечить корректный frontmatter

### 6. Update Consilium Progress (FRONTMATTER, ENFORCED)

### X. Update Consilium Progress

**🚨 MANDATORY FRONTMATTER UPDATE - COMPLETE FORMAT**

Обновить frontmatter {outputFile} ВСЕМИ полями:

```yaml
***
consiliumId: "EMB-CSL-[timestamp]"
title: "EMBER Consilium Report: [user's decision topic]"
created: "[ISO date when started]"
lastUpdated: "[ISO date now]"

stepsCompleted: 
  - 'step-01a-problem-definition'
  - 'step-01b-analysis-documentation'
progress: 20
currentPhase: 'problem-analysis'
lastStep: 'step-01b-analysis-documentation'

complexityAssessmentComplete: [true/false]
problemAnalysisComplete: [true/false]
decisionFrameworkApplicationComplete: [true/false]
evidenceCollectionComplete: [true/false]
evidenceValidationComplete: [true/false]
matrixSetupComplete: [true/false]
scoringApplicationComplete: [true/false]

status: "PROBLEM_ANALYSIS_COMPLETE"
nextStep: "step-02a-decision-framework.md"

overallConfidence: [0-100]
evidenceQuality: [0-100]
criticalGaps: [count]

userName: "[user name]"
decisionDomain: "[technical/business/operational/etc]"
decisionComplexity: "[Light/Standard/Comprehensive]"
***
```

**Frontmatter Validation Checklist:**
- [ ] consiliumId уникален
- [ ] title отражает суть задачи пользователя
- [ ] stepsCompleted содержит текущий шаг
- [ ] progress = 20
- [ ] currentPhase = 'problem-analysis'
- [ ] lastStep = этот шаг
- [ ] status = PROBLEM_ANALYSIS_COMPLETE
- [ ] nextStep = step-02a-decision-framework.md
- [ ] все флаги выставлены корректно
- [ ] присутствует вся пользовательская информация (userName, domain, и т.д.)

**AFTER UPDATE:**
- Прочесть файл, убедиться что всё сохранено и корректно

---

## CRITICAL GAPS CHECK

### X. CRITICAL GAPS CHECK

**🚨 BEFORE PROCEEDING - VERIFY NO CRITICAL GAPS**

- Опишите все выявленные critical/important gaps
- Классифицируйте каждый gap
- Если есть непреодолимые критические пробелы — ОСТАНОВИТЬ workflow до их устранения

---

## 🔒 MANDATORY SELF-VALIDATION PROTOCOL

**🚨 ВЫПОЛНЯТЬ ДО ПРОДОЛЖЕНИЯ (СМ. ЧЕКЛИСТ НИЖЕ)**

### VALIDATION CATEGORY 1: Work Completion

- [ ] Check 1.1: Все шаги выполнены (MANDATORY SEQUENCE)
- [ ] Check 1.2: Нет пропущенных шагов
- [ ] Check 1.3: Выполнена реальная работа, а не симуляция
- [ ] Check 1.4: Получен user input везде, где требуется
- [ ] Check 1.5: Использованы только данные реального кейса

### VALIDATION CATEGORY 2: Output Documentation

- [ ] Check 2.1: Работа сохранена в {outputFile}
- [ ] Check 2.2: Frontmatter обновлён по полной схеме
- [ ] Check 2.3: Контент реально присутствует в файле
- [ ] Check 2.4: Запись файла прошла корректно

### VALIDATION CATEGORY 3: Menu Interaction

- [ ] Check 3.1: Меню отображено пользователю
- [ ] Check 3.2: Получен и обработан ввод пользователя
- [ ] Check 3.3: Логика меню исполнена корректно
- [ ] Check 3.4: Меню возвращается, если требуется

### VALIDATION CATEGORY 4: Next Step Preparation

- [ ] Check 4.1: Корректно определён путь next step
- [ ] Check 4.2: Следующий step-файл будет загружен полностью
- [ ] Check 4.3: Прочитать и понять, что требуется (GOAL, SEQUENCE)
- [ ] Check 4.4: Полная готовность к запуску следующего шага

### VALIDATION CATEGORY 5: Quality Checks

- [ ] Check 5.1: Нет непреодолимых critical gaps
- [ ] Check 5.2: Текущий confidence >= 30% И обоснован
- [ ] Check 5.3: MCP tools вызваны, если требовались (добавьте таблицу вызова)
- [ ] Check 5.4: Использованы доказательства и реальные данные

---

### FINAL VALIDATION DECISION

- Если ВСЕ боксы отмечены — переходить к следующему шагу.
- Если хотя бы что-то не выполнено — ДАННЫЙ workflow БЛОКИРУЕТСЯ до устранения.
---

## MENU OPTIONS (UPDATED)

**Select an Option:**  
[A] Advanced Elicitation  
[P] Party Mode  
[C] Continue to Decision Block Analysis

---

#### 🚨 WAITING FOR USER INPUT - ENFORCEMENT

1. Показать меню
2. ЯВНО ОСТАНОВИТЬСЯ и ЖДАТЬ выбора  
3. НЕ ПРОДОЛЖАТЬ и не выбирать 'C' автоматически  
4. После выбора — чётко выполнить логику обработки

---

#### Menu Handling Logic (UPDATED):

- IF A: Выполнить {advancedElicitationTask}
- IF P: Выполнить {partyModeWorkflow}
- IF C: **EXECUTE TRANSITION PROTOCOL:**
  - Сохранить всё в {outputFile}
  - Полностью обновить frontmatter и проверить правильность
  - Провести self-validation checklist
  - Если всё ОК — находим файл {nextStepFile}, полностью грузим, проверяем структуру, читаем целиком до исполнения
  - Только после всего этого — начать следующий шаг
- IF любой другой вариант/вопрос: помочь, затем ВЕРНУТЬ МЕНЮ

**TRANSITION PROTOCOL (Detailed):**
- Phase 1: Сохранить всё, обновить frontmatter, проверить успех записи
- Phase 2: Self-validation checklist — ВСЁ ДОЛЖНО БЫТЬ ЗАКОНЧЕНО
- Phase 3: Загрузить и ПРОЧИТАТЬ СЛЕДУЮЩИЙ ФАЙЛ ПОЛНОСТЬЮ (проверить размер, секции)
- Phase 4: Прочитать GOAL, SEQUENCE, структурировать
- Phase 5: Только теперь — исполнять

**ВАЛИДАЦИОННЫЕ ТОЧКИ:**
- Перед загрузкой: всё сохранено, обновлено, валидация пройдена
- После загрузки: файл загружен полностью, секции прочитаны, GOAL понят

---

## RESULTS COMPLETION NOTE

- Только после выбора 'C' и ВЕРИФИКАЦИИ, вы читаете и переходите к step-02a-decision-framework.md

---

## SYSTEM SUCCESS/FAILURE METRICS

- Только РЕАЛЬНОЕ выполнение работы, полные данные, корректные файлы, строгая обработка пользовательского ввода
- Провален хотя бы один enforcement rule — FAILURE, workflow блокируется

---
