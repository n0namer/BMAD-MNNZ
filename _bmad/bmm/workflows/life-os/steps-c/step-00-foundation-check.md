---
name: 'step-00-foundation-check'
description: 'Check if foundation data exists, offer to skip or update'
nextStepFile: './step-01-collect-ideas.md'
nextStepIfMissing: './step-00.5-project-stage.md'
goalsFile: '{bmb_creations_output_folder}/life-os/goals.yaml'
stageAssessmentFile: '{bmb_creations_output_folder}/life-os/project-stage-assessment.md'
resourceAssessmentFile: '{bmb_creations_output_folder}/life-os/resource-assessment.md'
optimizationFile: '{bmb_creations_output_folder}/life-os/optimization-suggestions.md'
foundationCheckExamples: '../data/foundation-examples/foundation-check-examples.md'
---

# Step 00: Foundation Data Check

## STEP GOAL

Check if foundation data is filled (goals, resources, project stage). If yes - offer to skip or update. If no - collect data via Steps 0.5-0.7.

**Principle:** Don't waste user's time re-collecting already known data.

## MANDATORY EXECUTION RULES

### Universal Rules
- 🛑 NEVER force re-entry of existing data
- 📖 CRITICAL: Check files existence before asking questions
- 🎯 Show summary of existing data
- ✅ Always provide [Skip], [Update], [Re-enter] options
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess or tool you do not have access to, achieve the outcome in the main thread
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in Russian (`{communication_language}`)

## EXECUTION PROTOCOL

### 1. Check Foundation Files Existence

```bash
# Check if foundation data files exist (goals optional)
REQUIRED_FILES=(
  "{stageAssessmentFile}"
  "{resourceAssessmentFile}"
  "{optimizationFile}"
)

OPTIONAL_FILES=(
  "{goalsFile}"
)

REQUIRED_COUNT=0
for file in ${REQUIRED_FILES[@]}; do
  if [ -f "$file" ]; then
    REQUIRED_COUNT=$((REQUIRED_COUNT + 1))
  fi
done

GOALS_EXIST=false
if [ -f "{goalsFile}" ]; then
  GOALS_EXIST=true
fi
```

**If ALL 3 required files exist → Show Summary + Menu**
**If SOME required files missing → Offer to complete missing parts**
**If NO required files exist → Run full foundation sequence (Steps 0.5-0.7)**
**Goals file is OPTIONAL and shown separately**

---

### 2. Scenario A: All Required Foundation Data Exists (3/3 files)

**Display summary of existing data in formatted boxes:**
```
✅ **Фундаментальные данные заполнены!**
[Show 3 boxes: Stage, Resources, Optimization with key data]

⚠️ **Долгосрочные цели (Goals):** {
  IF GOALS_EXIST:
    "✅ Определены ({timestamp})"
  ELSE:
    "⏭️ Не определены (опционально, можно добавить позже)"
}

💡 **Что дальше?**
[S]kip - Пропустить (использовать существующие данные)
[U]pdate - Обновить часть данных
[R]e-enter - Заново заполнить все
{IF !GOALS_EXIST: "[G]oals - Определить долгосрочные цели (~10-15 мин)"}

Ваш выбор: [S] / [U] / [R] {IF !GOALS_EXIST: "/ [G]"}
```

**Action Routing:**
- `[S]` → Load `{nextStepFile}` (step-01-collect-ideas.md)
- `[U]` → Show update menu, load selected step(s)
- `[R]` → Confirm, then load `{nextStepIfMissing}` (step-00.5)
- `[G]` (if goals not defined) → Load step-00-goals-discovery.md, then return to Step 01

### Menu Handler (Scenario A)

**Available Options:**
- `[S]` - Skip - Use existing data (proceed to Step 01)
- `[U]` - Update - Selectively update sections
- `[R]` - Re-enter - Complete foundation sequence from Step 0.5
- `[G]` - Goals - Define long-term goals (if not defined)

**Execution Rules:**
1. Display menu options with existing data summary
2. **HALT and WAIT** for user input
3. If user selects `[S]` → Save state, update frontmatter, load and execute {nextStepFile}
4. If user selects `[U]` → Show update submenu (see Section 5), then wait again
5. If user selects `[R]` → Confirm warning, save state, load {nextStepIfMissing}
6. If user selects `[G]` → Save state, load step-00-goals-discovery.md, then return to Step 01
7. **Do NOT auto-proceed** - this is an interactive menu requiring user choice

---

### 3. Scenario B: Some Required Foundation Data Missing (1-2/3 files)

```
⚠️ **Неполные фундаментальные данные**
Найдено: {REQUIRED_COUNT}/3 обязательных файлов

✅ Заполнено: {list existing}
❌ Отсутствует: {list missing}
⏭️ Goals: {GOALS_EXIST ? "✅ Определены" : "Не определены (опционально)"}

💡 **Что дальше?**
[C]omplete - Заполнить недостающие обязательные
[R]e-enter - Заново всё
[S]kip - Продолжить (⚠️ не рекомендуется)
```

**Action Routing:**
- `[C]` → Load first missing required step
- `[R]` → Load `{nextStepIfMissing}` (step-00.5)
- `[S]` → Warn, then load `{nextStepFile}` if confirmed

### Menu Handler (Scenario B)

**Available Options:**
- `[C]` - Complete - Fill missing required sections
- `[R]` - Re-enter - Start full foundation sequence
- `[S]` - Skip - Continue anyway (not recommended)

**Execution Rules:**
1. Display menu with existing vs missing data
2. **HALT and WAIT** for user input
3. If user selects `[C]` → Determine first missing step file, save state, load that step
4. If user selects `[R]` → Save state, load {nextStepIfMissing} (step-00.5)
5. If user selects `[S]` → Display warning about risks, wait for confirmation, then load {nextStepFile}
6. **Do NOT auto-proceed** - this is an interactive menu requiring user choice

---

### 4. Scenario C: No Required Foundation Data (0/3 files)

```
🆕 **Первый запуск - фундаментальные данные не найдены**

Перед началом нужно собрать базовые данные:

**Обязательно (3 шага):**
- Step 0.5: Стадия проекта (~3-5 мин)
- Step 0.6: Ресурсы (~2-3 мин)
- Step 0.7: Оптимизация (~2-3 мин)

**Опционально (можно отложить):**
- Step 00: Долгосрочные цели (~10-15 мин)

Общее время: ~10-12 минут (обязательное), +10-15 минут (если с целями)

**Зачем?**
- ✅ Точные таймлайны (Speed Multiplier)
- ✅ Оптимальные рекомендации по стеку
- ⏭️ Цели улучшают scoring, но можно добавить позже

[C]ontinue - Начать сбор обязательных данных
[Q]uit - Выйти
```

**Action Routing:**
- `[C]` → Load `{nextStepIfMissing}` (step-00.5)
- `[Q]` → Exit workflow

### Menu Handler (Scenario C)

**Available Options:**
- `[C]` - Continue - Begin required foundation data collection
- `[Q]` - Quit - Exit workflow

**Execution Rules:**
1. Display menu with time estimates and benefits
2. **HALT and WAIT** for user input
3. If user selects `[C]` → Save state, update frontmatter, load and execute {nextStepIfMissing}
4. If user selects `[Q]` → Confirm exit, save session state, terminate workflow gracefully
5. **Do NOT auto-proceed** - this is an interactive menu requiring user choice

---

### 5. Quick Update Menu (Global Command)

**`/update-foundation` - Available at ANY step:**

```
🛠️ **Быстрое обновление фундаментальных данных**

Текущие данные:
1. ✅ Стадия проекта: {timestamp}
2. ✅ Ресурсы: {timestamp}
3. ✅ Оптимизация: {timestamp}
4. {GOALS_EXIST ? "✅ Цели: {timestamp}" : "⏭️ Цели: Не определены (опционально)"}

[1-4] - Обновить раздел | [A]ll - Всё | [C]ancel - Отмена
```

**Implementation:**
- Global command, works from any step
- After update, return to original step
- Confirmation: "✅ {section} обновлён. Возвращаемся..."
- If selecting #4 and goals don't exist → Offer to create them

---

### 6. Save Memory of User Choice

**After user makes choice, save to memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:foundation-check:last-action" \
  --content "{timestamp}|{action}|{user_choice}"
```

**Track:** Last check time, user action (skip/update/re-enter), section frequency
**Use for:** Intelligent defaults, staleness detection (>90 days), usage analytics

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- File existence checked correctly
- Existing data summarized clearly
- User offered appropriate choices
- Quick update menu available
- No forced re-entry of known data
- User time saved (skip when data exists)

### ❌ SYSTEM FAILURE
- Forcing user through steps when data exists
- Not showing summary of existing data
- No option to skip or update
- Making user re-enter everything every time
- Not tracking staleness or usage patterns

**Master Rule:** RESPECT USER'S TIME. If data exists, show it and offer to skip. Never force repetition.

---

## Quick Reference

### Three Main Scenarios
1. **All required data exists (3/3)** → [S]kip / [U]pdate / [R]e-enter / [G]oals (if not defined)
2. **Some required missing (1-2/3)** → [C]omplete / [R]e-enter / [S]kip
3. **None exists (0/3)** → [C]ontinue / [Q]uit

### Staleness Thresholds
- Goals: 180 days | Project Stage: 30 days | Resources: 90 days | Optimization: 90 days

### Time Impact
- Full skip (3/3 + goals): Saves 20-25 min
- Full skip (3/3, no goals): Saves 10-12 min
- Partial update: Saves 5-20 min
- Complete missing: Saves 3-19 min
- Full sequence (without goals): 10-12 min (required first run)
- Full sequence (with goals): 20-25 min (first run)

---

💡 **Reference:** For complete scenarios, flow walkthroughs, staleness detection details, and integration examples, load: `{foundationCheckExamples}`

---

**Status:** DESIGNED ✅
**Implementation:** Ready to integrate into workflow.md
**User Benefit:** Saves 20-25 minutes on subsequent runs, respects existing data
