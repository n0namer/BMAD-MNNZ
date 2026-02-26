# LIFE OS WORKFLOW - DETAILED ISSUES & FIXES

**Дата:** 6 февраля 2026
**Статус:** ISSUES FOUND & SOLUTIONS PROVIDED

---

## НАЙДЕННЫЕ ПРОБЛЕМЫ

### 1. CRITICAL ISSUE: step-x-01-kickoff.md nextStepFile Reference

**Файл:** `steps-x/step-x-01-kickoff.md`
**Проблема:**
```yaml
nextStepFile: './step-x-02-tracking.md'  # ❌ НЕПРАВИЛЬНО
```

**Реальный файл:**
```
steps-x/step-x-02-weekly-pulse.md  # ✓ ПРАВИЛЬНОЕ имя
```

**Статус:** CRITICAL - Routing сломается

**Решение:**
```yaml
# ✅ ИСПРАВИТЬ НА:
nextStepFile: './step-x-02-weekly-pulse.md'
```

**Команда для исправления:**
```bash
# В файле steps-x/step-x-01-kickoff.md строка 4:
# Изменить:
nextStepFile: './step-x-02-tracking.md'
# На:
nextStepFile: './step-x-02-weekly-pulse.md'
```

---

### 2. MINOR ISSUE: step-00.1-portfolio-intake.md Missing nextStepFile

**Файл:** `steps-c/step-00.1-portfolio-intake.md`
**Проблема:**
```yaml
# Нет поля nextStepFile!
# Вместо этого только:
routing: step-01 (with track pre-selection)
```

**Статус:** MINOR - Документирует где идти (step-01), но нет стандартного frontmatter

**Решение:** Добавить стандартный nextStepFile в frontmatter
```yaml
nextStepFile: './step-01-collect-ideas.md'
```

**Команда для исправления:**
```bash
# В файле steps-c/step-00.1-portfolio-intake.md добавить в frontmatter (после line 17):
nextStepFile: './step-01-collect-ideas.md'
```

---

### 3. MINOR ISSUE: step-04.5-triz-analysis.md Missing nextStepFile

**Файл:** `steps-c/step-04.5-triz-analysis.md`
**Проблема:**
```yaml
# Нет поля nextStepFile!
# TRIZ может быть вызван из step-04, step-05 или step-08
# Но не ясно где вернуться после TRIZ
```

**Статус:** MINOR - TRIZ опциональный и может быть вызван из разных точек

**Решение:** Добавить условный nextStepFile и документировать поведение
```yaml
# OPTION 1: Back to step-05 (most common path)
nextStepFile: './step-05-scoring.md'

# ИЛИ OPTION 2: Документировать что TRIZ вернёт управление к step-05
calledFrom: [step-04, step-05, step-08]
returnTo: 'call origin (step-05 most common)'
```

**Рекомендация:** Добавить документацию:
```yaml
nextStepFile: './step-05-scoring.md'  # Default return path
# TRIZ может быть вызван из step-04 (→ возвращает в step-05)
#                        step-05 (→ возвращает в step-05)
#                        step-08 (→ возвращает в step-08)
# Фактический return path определяется контекстом вызова
```

---

### 4. DOCUMENTATION ISSUE: Step 08 Track-Specific Output Length

**Файл:** `steps-c/step-08-deep-plan.md`
**Проблема:**
```yaml
# Нет явной документации как выход меняется по track:
# - Quick Track: SKIPPED
# - Standard Track: L1-L3 (10-15 min)
# - Deep Track: L1-L6 (20-60 min)
```

**Статус:** MINOR - Функционирует но не задокументировано

**Решение:** Добавить в frontmatter:
```yaml
name: 'step-08-deep-plan'
trackVariants:
  quick:
    status: 'SKIPPED'
    reason: 'Too detailed for quick track validation'
    duration: '0 min'
  standard:
    status: 'L1-L3 (high-level plan)'
    duration: '10-15 min'
  deep:
    status: 'L1-L6 (comprehensive plan)'
    duration: '20-60 min with scenarios'
```

---

### 5. DOCUMENTATION ISSUE: Foundation Sequence nextStepFile Chain

**Файлы:**
- `step-00-foundation-check.md` → `step-01-collect-ideas.md` ✓
- `step-00.5-project-stage.md` → `step-00.6-resource-assessment.md` ✓
- `step-00.6-resource-assessment.md` → `step-00.7-optimization-intelligence.md` ✓
- `step-00.7-optimization-intelligence.md` → `step-00-goals-discovery.md` ✓
- `step-00-goals-discovery.md` → `step-01-collect-ideas.md` ✓

**Проблема:** Логика правильная но может быть непонятна:
- Если goals пропущены: `step-00.7` → `step-01` (пропустить goals)
- Если goals выбраны: `step-00.7` → `step-00-goals` → `step-01`

**Статус:** MINOR - Требует уточнения в step-00.7

**Решение:** Добавить в step-00.7-optimization-intelligence.md условное документирование:
```yaml
nextStepFile: './step-00-goals-discovery.md'
nextStepIfSkipped: './step-01-collect-ideas.md'
condition: 'User chooses [S]kip Goals Discovery → Jump to step-01'
```

---

## ВЕРИФИЦИРОВАННЫЕ ПУТИ (ОК)

### Foundation Sequence ✓
```
Step 00: Foundation Check
  IF all data exists → [Skip]/[Update]/[Re-enter]
  ELSE → Run foundation sequence:

Step 00.5: Project Stage Discovery
  → Step 00.6: Resource Assessment ✓ (nextStepFile указан)
  → Step 00.6: Resource Assessment
  → Step 00.7: Optimization Intelligence ✓ (nextStepFile указан)
  → Step 00.7: Optimization Intelligence
  → Step 00-Goals Discovery (optional) ✓ (nextStepFile указан)
  → Step 00-Goals Discovery (optional)
  → Step 01: Collect Ideas ✓ (nextStepFile указан)
```

### Quick Track ✓
```
Step 01: Collect Ideas
  → Step 04-consilium-lite ✓ (confirmed file exists)
  → Step 05: Scoring ✓ (nextStepFile = './step-06-integration.md')
  ❌ ОШИБКА: Step 05 указывает на step-06, но Quick Track должен идти в step-09

Issue: Step 05-scoring.md имеет hardcoded:
  nextStepFile: './step-06-integration.md'
Но для Quick Track должно быть: './step-09-complete.md'
```

---

## НАЙДЕННАЯ ВЛОЖЕННАЯ ПРОБЛЕМА: Quick Track Step 05 Routing

**Файл:** `steps-c/step-05-scoring.md`
**Проблема:**
```yaml
nextStepFile: './step-06-integration.md'  # ✓ Правильно для Standard/Deep
# Но для Quick Track это будет неправильно!
# Quick Track должен идти: 01 → 04-consilium-lite → 05 → 09
```

**Статус:** CRITICAL для Quick Track

**Текущее поведение:**
- Standard Track: 05 → 06 ✓
- Deep Track: 05 → 06 ✓
- Quick Track: 05 → 06 ❌ (должно быть 05 → 09)

**Решение:** Добавить conditional logic в step-05 или в workflow.md step-routing:

**Option 1: В workflow.md явно указать routing**
```yaml
quickTrackFlow:
  - step-01-collect-ideas.md
  - step-04-consilium-lite.md
  - step-05-scoring.md
  # Next step AFTER 05 is step-09 for Quick Track (override default)
```

**Option 2: В step-05-scoring.md добавить track-aware logic**
```yaml
nextStepFile: './step-06-integration.md'  # Default for Standard/Deep
nextStepIfQuickTrack: './step-09-complete.md'
```

---

## ИТОГОВЫЙ СПИСОК FIXES

### 🔴 CRITICAL (Must Fix)

| № | Файл | Проблема | Решение | Приоритет |
|---|------|----------|---------|-----------|
| 1 | steps-x/step-x-01-kickoff.md | nextStepFile: './step-x-02-tracking.md' (неправильно) | Изменить на './step-x-02-weekly-pulse.md' | **P0** |
| 2 | steps-c/step-05-scoring.md | Quick Track routing не работает | Добавить conditional next step для Quick Track | **P0** |

### 🟡 MINOR (Should Fix)

| № | Файл | Проблема | Решение | Приоритет |
|---|------|----------|---------|-----------|
| 3 | steps-c/step-00.1-portfolio-intake.md | Нет nextStepFile | Добавить: nextStepFile: './step-01-collect-ideas.md' | **P1** |
| 4 | steps-c/step-04.5-triz-analysis.md | Нет явного nextStepFile | Добавить: nextStepFile: './step-05-scoring.md' + документация | **P1** |
| 5 | steps-c/step-08-deep-plan.md | Нет track-specific documentation | Добавить trackVariants в frontmatter | **P2** |
| 6 | steps-c/step-00.7-optimization-intelligence.md | Условное routing не документировано | Добавить nextStepIfSkipped | **P2** |

---

## ИСПРАВЛЕНИЯ (STEP-BY-STEP)

### FIX #1: step-x-01-kickoff.md

**Текущая строка 4:**
```yaml
nextStepFile: './step-x-02-tracking.md'
```

**Изменить на:**
```yaml
nextStepFile: './step-x-02-weekly-pulse.md'
```

---

### FIX #2: step-05-scoring.md Routing Logic

**Добавить в frontmatter:**
```yaml
---
name: 'step-05-scoring'
description: 'MCDA scoring and decision gate'
nextStepFile: './step-06-integration.md'  # Standard/Deep default
trackVariants:
  quick:
    nextStepFile: './step-09-complete.md'  # Quick → Complete
  standard:
    nextStepFile: './step-06-integration.md'  # Standard → Integration
  deep:
    nextStepFile: './step-06-integration.md'  # Deep → Integration
---
```

**В теле step добавить logic:**
```markdown
## NEXT STEP ROUTING

Based on selected track:
- **Quick Track:** [Continue] → Step 09 (Complete)
- **Standard/Deep Track:** [Continue] → Step 06 (Portfolio Integration)
```

---

### FIX #3: step-00.1-portfolio-intake.md

**Добавить в frontmatter (после line 17):**
```yaml
nextStepFile: './step-01-collect-ideas.md'
```

---

### FIX #4: step-04.5-triz-analysis.md

**Добавить в frontmatter:**
```yaml
nextStepFile: './step-05-scoring.md'  # Default return path
calledFrom:
  - step-04-consilium.md  # → returns to step-05
  - step-05-scoring.md    # → returns to step-05
  - step-08-deep-plan.md  # → returns to step-08
returnBehavior: 'Returns to step-05 by default, or to calling step if override'
```

---

### FIX #5: step-08-deep-plan.md

**Добавить в frontmatter:**
```yaml
trackVariants:
  quick:
    status: 'SKIPPED (too detailed)'
    duration: '0 min'
    rationale: 'Quick track uses go/no-go decision, not detailed plan'
  standard:
    status: 'L1-L3 (high-level plan)'
    duration: '10-15 min'
    deliverable: 'Phase-level planning, resource allocation outline'
  deep:
    status: 'L1-L6 (comprehensive plan)'
    duration: '20-60 min (up to 3h with refinement)'
    deliverable: 'Full detail with scenarios, task decomposition, dependency mapping'
```

---

### FIX #6: step-00.7-optimization-intelligence.md

**Уточнить в frontmatter:**
```yaml
nextStepFile: './step-00-goals-discovery.md'
nextStepIfSkipped: './step-01-collect-ideas.md'

userChoice:
  '[C]ontinue with Goals Discovery': 'Load step-00-goals-discovery.md'
  '[S]kip Goals - Evaluate idea first': 'Jump directly to step-01-collect-ideas.md'
```

---

## ДОПОЛНИТЕЛЬНЫЕ РЕКОМЕНДАЦИИ

### 1. Обновить workflow.md Section "Track-Based Routing"

**Добавить уточнение для Step 05:**
```markdown
### Quick Track Step 05 Special Handling

Step 05 (Scoring) adjusts next step based on track:
- **Quick Track:** After scoring → Step 09 (Complete)
  - No portfolio integration, no planning
  - User gets decision recommendation and moves on
- **Standard/Deep:** After scoring → Step 06 (Integration)
  - Portfolio impact analysis, resource planning
```

---

### 2. Добавить Issue Tracker для отслеживания

**Создать файл:** `_bmad/_output/ISSUES-TRACKER.yaml`

```yaml
issues:
  - id: 'ROUTING-001'
    title: 'step-x-01-kickoff nextStepFile reference incorrect'
    severity: 'critical'
    file: 'steps-x/step-x-01-kickoff.md'
    status: 'open'
    fix: 'Change ./step-x-02-tracking.md to ./step-x-02-weekly-pulse.md'

  - id: 'ROUTING-002'
    title: 'Quick Track Step 05 routing broken'
    severity: 'critical'
    file: 'steps-c/step-05-scoring.md'
    status: 'open'
    fix: 'Add track-conditional nextStepFile logic'

  - id: 'DOCS-001'
    title: 'Missing nextStepFile in portfolio-intake'
    severity: 'minor'
    file: 'steps-c/step-00.1-portfolio-intake.md'
    status: 'open'
    fix: 'Add nextStepFile: ./step-01-collect-ideas.md'
```

---

## ВАЛИДАЦИЯ ПОСЛЕ ИСПРАВЛЕНИЙ

### Проверка 1: Все nextStepFile references
```bash
# Должно быть 0 неправильных ссылок:
grep -r "nextStepFile:" steps-*/ | grep -v "step-01\|step-02\|step-03\|step-04\|step-05\|step-06\|step-07\|step-08\|step-09\|step-x-0" | wc -l
# Результат должен быть 0
```

### Проверка 2: Quick Track путь работает
```
01 → 04-consilium-lite → 05 → 09  ✓
```

### Проверка 3: Standard Track путь работает
```
01 → 02 → 03 → 04 → 05 → 06 → 08 → 09  ✓
```

### Проверка 4: Deep Track путь работает
```
00 → 01 → 02 → 03 → 04 → 04.5 → 05 → 06 → 07 → 08 → 08.5 → X-01 → 09  ✓
```

---

## ЗАКЛЮЧЕНИЕ

**Найдено:** 6 issues (2 critical, 4 minor)

**Статус Валидации:**
- ✓ Категоризация типов: PASS
- ✓ Отсутствие смешивания: PASS
- ✓ Foundation steps: PASS
- ❌ Frontmatter routing: FAIL (2 critical, 4 minor)

**Рекомендация:** Исправить CRITICAL issues до использования workflow

**Время на исправление:** ~15-20 минут

---

*Подготовлено: 6 февраля 2026*
*Статус: Ready for fix execution*
