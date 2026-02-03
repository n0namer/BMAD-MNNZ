---
validationDate: 2026-02-01
completionDate: 2026-02-01
workflowName: life-os
workflowPath: d:\\Users\\NIKITA\\Documents\\DEV\\katana-vectorbt\\_bmad\\bmm\\workflows\\life-os
validationStatus: COMPLETE
---

# Validation Report: life-os

**Validation Started:** 2026-02-01
**Validator:** BMAD Workflow Validation System
**Standards Version:** BMAD Workflow Standards

- [File Structure & Size](#file-structure--size)
- [Frontmatter Validation](#frontmatter-validation)
- [Path Violations](#path-violations)
- [Menu Validation](#menu-validation)
- [Step Type Validation](#step-type-validation)
- [Output Format Validation](#output-format-validation)
- [Validation Design Check](#validation-design-check)
- [Instruction Style Check](#instruction-style-check)
- [Collaborative Experience Check](#collaborative-experience-check)
- [Subprocess Optimization Check](#subprocess-optimization-check)
- [Cohesive Review](#cohesive-review)

## File Structure & Size

### Итог
Статус: WARNINGS

### Структура папок
- workflow.md присутствует.
- Папки steps-c/, steps-e/, steps-v/ присутствуют и содержат step-файлы.
- Папки data/ и templates/ присутствуют.
- Доп. файл: GAPS-RESOLUTION-REPORT.md (документ/отчет) — допустимо.

### Проверка наличия workflow-plan.md
- Ожидаемый файл: workflow-plan.md — НЕ НАЙДЕН.
- Следствие: невозможно сверить шаги с дизайн‑планом (требуется восстановить/создать план, либо обновить проверку).

### Размеры step-файлов (лимит <200 рекоменд., 250 макс.)
**steps-c/**
- step-01-collect-ideas.md — 122 строк (✅ Good)
- step-02-specialist-match.md — 91 строк (✅ Good)
- step-03-consilium.md — 70 строк (✅ Good)
- step-04-scoring.md — 76 строк (✅ Good)
- step-05-integration.md — 92 строк (✅ Good)
- step-06-calendar-sync.md — 77 строк (✅ Good)

**steps-e/**
- step-01-update-project.md — 68 строк (✅ Good)
- step-02-rescoring.md — 70 строк (✅ Good)
- step-03-kill-project.md — 63 строк (✅ Good)

**steps-v/**
- step-01-daily-review.md — 54 строк (✅ Good)
- step-02-weekly-review.md — 54 строк (✅ Good)
- step-03-monthly-review.md — 49 строк (✅ Good)

### Размеры reference/data файлов
- dfvc-criteria-rubric.md — 811 строк (⚠️ очень большой файл; лучше шардировать/индексировать)
- five-forces-template.md — 453 строк (⚠️ большой файл; рассмотреть разбиение)
- mcda-methodology.md — 617 строк (⚠️ большой файл; рассмотреть разбиение)
- real-options-guide.md — 666 строк (⚠️ большой файл; рассмотреть разбиение)
- stage-gate-mapping.md — 656 строк (⚠️ большой файл; рассмотреть разбиение)
- unit-economics-calculator.md — 326 строк (⚠️ большой файл; рассмотреть разбиение)
- Остальные data-файлы — небольшие (✅)

### Дополнительно
- workflow.md — 292 строки (⚠️ крупный корневой файл; не step‑файл, но стоит мониторить размер).

### Рекомендации
- Восстановить/создать workflow-plan.md для сверки шагов и полноты структуры.
- Рассмотреть шардирование крупных data‑файлов (>300 строк) на тематические части.

**File Structure & Size validation complete.**


## Frontmatter Validation

### Итог
Статус: PASS

### Проверенные файлы
steps-c:
- step-01-collect-ideas.md — PASS
- step-02-specialist-match.md — PASS
- step-03-consilium.md — PASS
- step-04-scoring.md — PASS
- step-05-integration.md — PASS
- step-06-calendar-sync.md — PASS

steps-e:
- step-01-update-project.md — PASS
- step-02-rescoring.md — PASS
- step-03-kill-project.md — PASS

steps-v:
- step-01-daily-review.md — PASS
- step-02-weekly-review.md — PASS
- step-03-monthly-review.md — PASS

### Нарушения
- Не обнаружены: нет неиспользуемых переменных, нет запрещенных `workflow_path`, `thisStepFile`, `workflowFile`, все `nextStepFile` используют формат `./step-*.md`.

**Frontmatter validation complete.** Proceeding to Menu Handling Validation...


## Path Violations

### Config Variables (Exceptions)
Из workflow.md извлечены переменные конфигурации:
- user_name
- communication_language
- document_output_language
- bmb_creations_output_folder

### Content Path Violations
- Не обнаружены: `{project-root}/` в теле step‑файлов не найден.

### Dead Links
- Не обнаружены: все относительные ссылки на step/data файлы существуют.
- Выходные пути с `{bmb_creations_output_folder}` корректно пропущены как ожидаемые output‑файлы.

### Module Awareness
- Не обнаружено bmb‑специфичных путей в модуле bmm.

### Summary
- **CRITICAL:** 0
- **HIGH:** 0
- **MEDIUM:** 0

**Status:** ✅ PASS - No violations


## Menu Validation

### Итог
Статус: WARN

### Проверенные файлы (steps-c/)
- step-01-collect-ideas.md — MENU present (C-only) — ⚠️ замечание
- step-02-specialist-match.md — MENU present (C-only) — PASS
- step-03-consilium.md — MENU present (C-only) — PASS
- step-04-scoring.md — MENU present (C-only) — PASS
- step-05-integration.md — MENU present (C-only) — PASS
- step-06-calendar-sync.md — MENU отсутствует (финальный шаг) — PASS

### Нарушения / замечания
- step-01-collect-ideas.md: в ветке **IF C** отсутствует явный шаг `update frontmatter` перед загрузкой {nextStepFile}. Стандарт требует последовательность Save → update frontmatter → load next step.

### Общая оценка
- Меню в шагах 02–05 оформлены корректно (Display + Handler + EXECUTION RULES, halt/wait, redisplay).
- В шагах без меню (step-06) — допустимо для финала.

**Menu Handling validation complete.** Proceeding to Step Type Validation...


## Step Type Validation

### Итог
Статус: WARN

### Результаты по шагам (steps-c/)
- step-01-collect-ideas.md
  - Ожидаемый тип: **Init (Non‑Continuable)** (шаг 01)
  - Фактический тип: **Middle (Simple)** (C-only menu)
  - Замечание: init‑шаг по стандарту должен auto‑proceed без меню и чаще создавать выход из шаблона. Здесь есть C‑меню и нет auto‑proceed → несоответствие паттерну.

- step-02-specialist-match.md — Ожидаемый тип: Middle (Simple) — PASS
- step-03-consilium.md — Ожидаемый тип: Middle (Simple) — PASS
- step-04-scoring.md — Ожидаемый тип: Middle (Simple) — PASS
- step-05-integration.md — Ожидаемый тип: Middle (Simple) — PASS
- step-06-calendar-sync.md — Ожидаемый тип: Final — PASS (нет nextStepFile, есть completion message)

### Нарушения
- step-01-collect-ideas.md: несоответствие паттерну Init (Non‑Continuable).
  - Рекомендация: либо сделать auto‑proceed без меню, либо официально описать шаг 01 как Middle (Simple) в design/plan.

**Step Type validation complete.** Proceeding to Output Format Validation...


## Output Format Validation

### Документообразование
- Workflow производит **workflow plan** (workflowPlanFile) и **project file** (outputProjectFile) → паттерн близок к Plan‑then‑Build.
- Дизайн‑файл `{workflow_folder_path}/workflow-plan.md` отсутствует, поэтому тип шаблона формально не подтвержден.

### Template Assessment
- Найден шаблон `templates/workflow-plan.template.md` (структурированный каркас).
- Ни один шаг не ссылается на этот шаблон; step‑02 создает план «с нуля» через минимальный header.
- Рекомендация: либо использовать шаблон при создании плана, либо удалить/обновить шаблон, чтобы не вводить в заблуждение.

### Final Polish Step
- Для плана отсутствует отдельный «polish» шаг. Если план предполагается как free‑form документ, это ⚠️; если structured, может быть допустимо.

### Step-to-Output Mapping
- step-01-collect-ideas.md → пишет idea файл в `{ideasFolder}` (OK), но **в C‑ветке нет update frontmatter**.
- step-02-specialist-match.md → пишет в `{workflowPlanFile}` перед переходом (OK).
- step-03-consilium.md → пишет в `{workflowPlanFile}` перед переходом (OK).
- step-04-scoring.md → пишет в `{workflowPlanFile}` перед переходом (OK).
- step-05-integration.md → пишет в `{workflowPlanFile}` и `{decisionsLog}` (OK).
- step-06-calendar-sync.md → пишет `{outputProjectFile}` и аппендит в `{workflowPlanFile}` (финальный шаг, OK).

### Subprocess Analysis Summary
- Шагов проанализировано: 6
- Шагов с выходом в документ: 6
- Шагов с корректным сохранением перед переходом: 5
- Шагов с проблемами: 1 (step-01, отсутствие update frontmatter)

### Итог
Статус: WARN

**Output Format validation complete.** Proceeding to Validation Design Check...


## Validation Design Check

### Нужна ли валидация?
- По домену: Life/Business OS — **не критично** (не compliance/medical/legal). Валидаторы скорее являются review‑процессом.
- workflow-plan.md отсутствует, поэтому решение основано на содержимом workflow.md.

### Найденные validation‑шаги
- steps-v/step-01-daily-review.md
- steps-v/step-02-weekly-review.md
- steps-v/step-03-monthly-review.md

### Оценка качества validation‑шагов
- Шаги являются review‑процедурами, а не строгими проверками качества/комплаенса.
- Нормально для не‑критичного workflow; строгие требования (data‑driven валидация, anti‑lazy language) не обязательны.

### Validation Data Files
- Специальных validation‑data файлов не обнаружено (data/ содержит методики/справочники). Это допустимо для не‑критичного review‑флоу.

### Итог
Статус: N/A (Validation not critical)

**Validation Design check complete.** Proceeding to Instruction Style Check...


## Instruction Style Check

### Оценка домена
- Домен: личное/бизнес‑планирование, фасилитация → **intent‑based** предпочтителен.

### Классификация стиля по шагам
**steps-c/**
- step-01-collect-ideas.md — Mixed (есть intent‑фрейм, но много точных формулировок/скриптов)
- step-02-specialist-match.md — Mixed/Prescriptive (точные вопросы и формулировки)
- step-03-consilium.md — Mixed (структурированные вопросы, но с гибкостью)
- step-04-scoring.md — Mixed/Prescriptive (конкретные списки вопросов/форматов)
- step-05-integration.md — Mixed (детальная структура шагов)
- step-06-calendar-sync.md — Mixed (конкретные вопросы и форматы)

**steps-e/**
- step-01-update-project.md — Mixed/Prescriptive
- step-02-rescoring.md — Mixed/Prescriptive
- step-03-kill-project.md — Mixed/Prescriptive

**steps-v/**
- step-01-daily-review.md — Mixed/Prescriptive
- step-02-weekly-review.md — Mixed/Prescriptive
- step-03-monthly-review.md — Mixed/Prescriptive

### Замечания
- В большинстве шагов присутствуют точные формулировки («Ask: ...», готовые тексты). Для данного домена предпочтительнее intent‑based стиль с целями и принципами, позволяющий адаптировать диалог.
- При этом структура шагов ясна и консистентна — это плюс.

### Итог
Статус: WARN (стиль слегка излишне предписывающий для intent‑домена)

**Instruction Style check complete.** Proceeding to Collaborative Experience Check...


## Collaborative Experience Check

### Collaborative Experience Check Results

**Overall Facilitation Quality:** Fair (сильная структура, но местами похоже на анкетирование)

**Step-by-Step Analysis:**

**step-01-collect-ideas.md:**
- Question style: смешанный (есть “ask 1–2”, но большой список полей)
- Conversation flow: умеренно естественный
- Role clarity: ✅
- Status: ⚠️ NEEDS IMPROVEMENT

**step-02-specialist-match.md:**
- Question style: прогрессивный, но есть скриптованные фразы
- Conversation flow: нормальный
- Role clarity: ✅
- Status: ✅ PASS

**step-03-consilium.md:**
- Question style: прогрессивный (по специалисту)
- Conversation flow: естественный
- Role clarity: ✅
- Status: ✅ PASS

**step-04-scoring.md:**
- Question style: список из 5 критериев (форм‑подобно)
- Conversation flow: жестковатый
- Role clarity: ✅
- Status: ⚠️ NEEDS IMPROVEMENT

**step-05-integration.md:**
- Question style: много подпроцедур и списков
- Conversation flow: скорее процедурный
- Role clarity: ✅
- Status: ⚠️ NEEDS IMPROVEMENT

**step-06-calendar-sync.md:**
- Question style: список параметров (даты/ёмкость/мильстоуны)
- Conversation flow: процедурный
- Role clarity: ✅
- Status: ⚠️ NEEDS IMPROVEMENT

**Edit steps (steps-e):**
- Вопросы структурированные, но часто «анкета» → ⚠️

**Validation steps (steps-v):**
- Краткие и последовательные, без меню → ✅

**Collaborative Strengths Found:**
- Ясные роли и ожидания
- Пошаговая логика с подтверждениями

**Collaborative Issues Found:**
- Laundry‑list вопросы в scoring/integration/calendar/edit
- Мало подсказок по «задавайте 1–2 вопроса» кроме step‑01
- Отсутствуют явные механизмы мягкого обработки неопределенности/ошибок ввода

**User Experience Assessment:**
- Ближе к «mix»: партнер + структурированная анкета

**Overall Collaborative Rating:** ⭐⭐⭐☆☆ (3/5)

**Status:** ⚠️ NEEDS IMPROVEMENT

**Collaborative Experience check complete.** Proceeding to Cohesive Review...


## Subprocess Optimization Check

## Subprocess Optimization Opportunities

**Total Opportunities:** 6 | **High Priority:** 2 | **Estimated Context Savings:** ~2000+ lines (data files + multi‑file scans)

### High-Priority Opportunities

**step-04-scoring.md / step-05-integration.md** — Pattern 3 (data ops)
- **Current:** Инструкции предлагают использовать крупные data‑файлы напрямую (mcda‑methodology, stage‑gate‑mapping, strategic‑buckets, portfolio‑health, integration‑patterns, workflow‑mapping, timeline‑allocation, wip‑enforcement).
- **Suggested:** Запускать subprocess, который загружает конкретный data‑файл и возвращает только релевантные выдержки/таблицы для текущего шага.
- **Impact:** Сильная экономия контекста (сотни строк на файл) и быстреее выполнение.
- **Example:** `subprocess: load ../data/mcda-methodology.md → return only criteria table`

**step-02-specialist-match.md** — Pattern 1 (grep/regex) + Pattern 4 (parallel)
- **Current:** Поиск последней идеи описан как ручное действие.
- **Suggested:** Subprocess на поиск последних файлов в ideasFolder и краткое резюме (Pattern 1), параллельно с загрузкой workflowPlanFile (Pattern 4).
- **Impact:** Сокращение времени и контекста, меньше ручного выбора.

### Moderate/Low-Priority Opportunities
- **step-01-collect-ideas.md** — Pattern 3 (data ops): параллельно сохранять в Markdown и Claude Flow (уже указано), но можно явно выделить subprocess на запись/подтверждение.
- **steps-v/*.md** — Pattern 1: быстрый grep/summary по metricsFile/portfolioFile вместо полного чтения.
- **steps-e/*.md** — Pattern 2: глубокий разбор project‑файла в subprocess и возврат краткого summary.
- **step-06-calendar-sync.md** — Pattern 3: генерация таймлайна в subprocess на основании параметров.

### Summary by Pattern
- **Pattern 1 (grep/regex):** 2 opportunities
- **Pattern 2 (per-file):** 1 opportunity
- **Pattern 3 (data ops):** 2 opportunities
- **Pattern 4 (parallel):** 1 opportunity

### Implementation Recommendations
**Quick Wins:** subprocess для выбора последней идеи и краткого summary; subprocess для загрузки одного data‑файла с извлечением релевантного раздела.
**Strategic:** стандартизировать использование data‑ops в шагах с крупными reference файлами.
**Future:** параллелизация загрузки справочников и plan/portfolio файлов.

**Status:** ⚠️ Review recommended

**Subprocess optimization analysis complete.** Identified 6 opportunities with potential context savings. Proceeding to Cohesive Review...


## Cohesive Review

### Cohesive Review Summary

**Overall Assessment:** Good → Needs work (minor structural fixes + UX/style improvements)

**Cohesiveness & Flow:**
- Шаги логично выстроены: идея → специалисты → консилиум → скоринг → интеграция → календарь.
- Edit и Validate потоки согласованы и независимы.
- Конец понятен (создание project file + сообщение о завершении).

**Strengths:**
- Четкая архитектура tri‑modal (steps‑c/e/v) и ясные цели по шагам.
- Полный «operating system» охват: scoring, portfolio health, WIP, интеграция.
- Сильные reference‑материалы в data/ (методологии и шаблоны).

**Weaknesses / Issues:**
- Отсутствует `{workflow_folder_path}/workflow-plan.md`, что ломает проверку дизайна и спецификаций.
- step-01 не соответствует init‑паттерну и в C‑ветке нет update frontmatter.
- Инструкции часто слишком прескриптивные для intent‑домена → ощущение «анкеты».
- Нет явного использования шаблона `templates/workflow-plan.template.md`.
- Крупные data‑файлы (>300 строк) требуют шардирования или subprocess‑data ops.

**User Experience Forecast:**
- Пользователь получит четкий путь, но может устать от длинных списков вопросов.
- Потребуется легкая донастройка диалога для более «коучингового» опыта.

**Recommendation:**
- **Needs work**: исправить init‑паттерн и фронтматтер‑обновления, синхронизировать план/шаблон, смягчить стиль вопросов.

**Cohesive Review complete.** Proceeding to finalize validation report...



## Summary

**Completion Date:** 2026-02-01
**Overall Status:** WARNINGS

**Validation Steps Completed:**
- File Structure & Size — WARNINGS
- Frontmatter Validation — PASS
- Path Violations — PASS
- Menu Validation — WARN
- Step Type Validation — WARN
- Output Format Validation — WARN
- Validation Design Check — N/A
- Instruction Style Check — WARN
- Collaborative Experience Check — NEEDS IMPROVEMENT
- Subprocess Optimization Check — REVIEW RECOMMENDED
- Cohesive Review — NEEDS WORK

**Critical Issues:** None

**Warnings / Improvements:**
- Отсутствует `workflow-plan.md` (невозможно сверить дизайн/план).
- step-01: нет `update frontmatter` в C‑ветке; не соответствует init‑паттерну.
- Шаблон `templates/workflow-plan.template.md` не используется.
- Инструкции слишком прескриптивные для intent‑домена; UX местами «анкета».
- Крупные data‑файлы (>300 строк) требуют шардирования/подхода data‑ops.

**Key Strengths:**
- Четкая tri‑modal структура (steps‑c/e/v).
- Логичный end‑to‑end поток и ясные цели.
- Богатые справочные материалы (data/).

**Overall Assessment:** Good → Needs work (minor structural fixes + UX/style tuning).

**Recommendation:** Needs tweaks before wide use.

**Suggested Next Steps:**
1. Восстановить/создать `workflow-plan.md` или обновить проверки, чтобы опираться на фактический дизайн.
2. Исправить step-01: добавить update frontmatter и определиться с типом шага (Init vs Middle).
3. Подключить `workflow-plan.template.md` в шаге создания плана.
4. Смягчить стиль вопросов (intent‑based), уменьшить «laundry list».
5. Разбить большие data‑файлы или использовать subprocess‑data ops.
