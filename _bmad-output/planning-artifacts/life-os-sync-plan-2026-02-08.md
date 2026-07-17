# Plan: Синхронизация Life OS Workflow с Ideal Behavior (additive)

**Date:** 2026-02-08  
**Project:** BMAD-MNNZ  
**Source of truth:**
- d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\workflow.md
- d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\docs\IDEAL-BEHAVIOR-REFERENCE.md

## Goal
Синхронизировать life-os/workflow.md с IDEAL-BEHAVIOR-REFERENCE.md так, чтобы **IDEAL-BEHAVIOR только дополнял**, а не переписывал существующий workflow. Сохранить структуру, логику и порядок шагов. Добавить недостающие поведенческие требования, правила, формулировки и системные ожидания.

## Priority Autopilot Checklist ([]/[x])
При словах-триггерах (`дальше`, `продолжай`, `continue`) **и фразах с тем же смыслом** выполняй первый незакрытый пункт.

- [x] WB-E Edit Workflow (/bmad-bmb-workflow в Edit Mode) - 2026-02-08: additive sync edits applied to `d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\workflow.md`
- [x] WB-V Validate Workflow (/bmad-bmb-workflow в Validate Mode) - 2026-02-08: PASS (additive alignment confirmed, no conflicts, structure preserved)
- [x] WB-E2 Edit Workflow (strict coverage addenda) - 2026-02-08: SmartSkip + thresholds + retrieval-before-reasoning + stage fields + activation prompt added
- [x] WB-V2 Validate Workflow (strict coverage) - 2026-02-08: PASS (strict coverage confirmed, additive integrity preserved)

## Absolute Paths (использовать в каждом промпте)
- WORKFLOW_LIFE_OS: d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\workflow.md
- IDEAL_BEHAVIOR: d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\docs\IDEAL-BEHAVIOR-REFERENCE.md
- WORKFLOW_BUILDER_FLOW: d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmb\workflows\workflow\workflow.md
- PLAN_THIS_FILE: d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad-output\planning-artifacts\life-os-sync-plan-2026-02-08.md

## BMAD Workflows To Include (из .codex/prompts)
1. WB-E Edit Workflow (/bmad-bmb-workflow в Edit Mode)
2. WB-V Validate Workflow (/bmad-bmb-workflow в Validate Mode)

## Post-Step Remediation Map (обязательное правило)
- Если WB-E не смог внести правки полностью → повторить WB-E с уточнением недостающих секций.
- Если WB-V выявил критические проблемы → вернуться в WB-E и исправить, затем снова WB-V.
**Итерационный цикл (обязателен):** `WB-E -> WB-V -> WB-E -> WB-V` повторять до статуса `PASS`.  
Любой `NEEDS FIX` автоматически возвращает на `WB-E` с точечными исправлениями, затем повторная `WB-V`.

## Detailed Workflow Intents (что запускать и каким текстом)

### 1) WB-E Edit Workflow (/bmad-bmb-workflow в Edit Mode)
**Goal:** Добавить в life-os/workflow.md все недостающие правила/поведения из IDEAL-BEHAVIOR-REFERENCE.md, не переписывая существующий текст.

**Launch text (copy/paste):**
```text
Запусти workflow builder в режиме EDIT.

Файл для правок:
- d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\workflow.md

Источник для синхронизации:
- d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\docs\IDEAL-BEHAVIOR-REFERENCE.md

Задача:
Синхронизировать workflow с IDEAL-BEHAVIOR так, чтобы IDEAL-BEHAVIOR ДОПОЛНЯЛ, а не переписывал существующий workflow.

Правила:
1) Сохрани текущую структуру, порядок шагов и логические секции.
2) Добавляй недостающие требования как расширения (bullet/подразделы/под-секции), а не как замену.
3) Никаких удалений без явной необходимости. Если конфликт — добавь поясняющую сноску/примечание, а не удаление.
4) Все добавления должны быть явно трассируемы к IDEAL-BEHAVIOR (можно короткие ссылки: "см. IDEAL BEHAVIOR: секция 1.2" и т.п.).
5) Не менять смысл уже описанных правил/алгоритмов, если нет прямого противоречия.
6) Если предлагается новое правило — добавь его в максимально релевантную существующую секцию, не создавая лишних новых разделов.
7) В конце добавь краткий блок "IDEAL BEHAVIOR ALIGNMENT" с перечнем ключевых добавлений (3-7 пунктов).

Ожидаемый результат:
- Обновлённый workflow.md с additive-синхронизацией
- Короткий список добавленных/уточнённых пунктов
```

### 2) WB-V Validate Workflow (/bmad-bmb-workflow в Validate Mode)
**Goal:** Проверить, что новые правки не ломают структуру и корректно дополняют workflow, без переписывания исходной логики.

**Launch text (copy/paste):**
```text
Запусти workflow builder в режиме VALIDATE.

Проверь файл:
- d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\workflow.md

Сверь с:
- d:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os\docs\IDEAL-BEHAVIOR-REFERENCE.md

Критерии:
1) IDEAL-BEHAVIOR дополняет, а не переписывает workflow.
2) Нет удаления ключевых секций и нет поломки последовательности.
3) Добавления трассируемы к IDEAL-BEHAVIOR.
4) Нет логических конфликтов между новым и старым текстом.

Выход:
- Краткий validation report: PASS / NEEDS FIX
- Если NEEDS FIX — список точечных правок
```

## Definition of Done
- life-os/workflow.md синхронизирован с IDEAL-BEHAVIOR (additive).
- Validation report: PASS.
- Все правки трассируемы к IDEAL-BEHAVIOR.
