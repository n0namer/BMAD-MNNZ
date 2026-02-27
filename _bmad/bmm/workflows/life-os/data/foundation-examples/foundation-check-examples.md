# Foundation Check Examples & Scenarios

## Scenario Walkthroughs

### Scenario A: First Run (No Existing Data)

**Initial State:**
- No foundation files exist (0/4)
- User starts workflow in "create" mode
- System needs to collect all foundation data

**User Experience:**
```
🆕 **Первый запуск - фундаментальные данные не найдены**

Перед началом работы нужно собрать базовые данные:

**Step 0.5:** Стадия проекта (Точка А)
  → Что уже готово? На какой стадии?
  → ~3-5 минут

**Step 0.6:** Ресурсы
  → Какие инструменты доступны? (LLM, команда)
  → ~2-3 минуты

**Step 0.7:** Оптимизация
  → Как быстрее всего реализовать?
  → ~2-3 минуты

**Step 00:** Долгосрочные цели
  → Цели на 1/3/5-10 лет (4 области)
  → ~10-15 минут

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Общее время: ~20-25 минут (один раз)

**Зачем это нужно?**
- ✅ Таймлайны будут учитывать ваш Speed Multiplier (LLM 10x-50x)
- ✅ Scoring будет учитывать ваши цели
- ✅ Рекомендации будут оптимальными для ваших ресурсов

[C]ontinue - Начать сбор данных
[Q]uit - Выйти (данные не будут собраны)
```

**Flow:**
```
User: [C]
  → System loads step-00.5-project-stage.md
  → Collects project stage data
  → Saves to project-stage-assessment.md
  → Auto-advances to step-00.6-resource-assessment.md
  → Collects resources
  → Auto-advances to step-00.7-optimization-intelligence.md
  → Collects optimization preferences
  → Auto-advances to step-00-goals-discovery.md
  → Collects goals
  → All 4/4 files created
  → Returns to step-01-collect-ideas.md
```

**Time Investment:** ~20-25 minutes (one-time setup)

---

### Scenario B: Subsequent Run (All Data Exists)

**Initial State:**
- All 4 foundation files exist
- Data last updated 15 days ago
- User starts workflow in "create" mode again

**User Experience:**
```
✅ **Фундаментальные данные уже заполнены!**

Найдены следующие данные:

┌─────────────────────────────────────────────────────────────┐
│ 📊 ВАШИ ЦЕЛИ (goals.yaml)                                   │
├─────────────────────────────────────────────────────────────┤
│ Финансы (1 год):  Increase ARR to $500K                     │
│ Бизнес (1 год):   Launch 3 new features                     │
│ Здоровье (1 год): Run 3x/week consistently                  │
│ Личное (1 год):   Learn Spanish (B1 level)                  │
│                                                              │
│ (+ цели на 3 года и 5-10 лет)                               │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 🔍 СТАДИЯ ПРОЕКТА (project-stage)                           │
├─────────────────────────────────────────────────────────────┤
│ Стадия:         D2 - Beta Testing                           │
│ Готовность:     65%                                         │
│ Главный блокер: Need 100 beta users for feedback            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ ⚡ РЕСУРСЫ (resource-assessment)                            │
├─────────────────────────────────────────────────────────────┤
│ Метод разработки: LLM + Cursor AI                           │
│ Speed Multiplier: 15x                                       │
│ Команда:          Solo founder + 2 contractors              │
│ Ограничения:      20h/week, $5k/month budget                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 🚀 ОПТИМИЗАЦИЯ (optimization-suggestions)                   │
├─────────────────────────────────────────────────────────────┤
│ Домен:          SaaS product for small businesses           │
│ Рекомендация:   Next.js + Supabase (18x speed)              │
│ Tech Stack:     React, TypeScript, Tailwind, Stripe         │
└─────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 **Что дальше?**

[S]kip - Пропустить (использовать существующие данные)
[U]pdate - Обновить часть данных (выбор, что именно)
[R]e-enter - Заново заполнить все (сброс и повтор Steps 0.5-0.7)
```

**Flow (User chooses [S]):**
```
User: [S]
  → System: "✅ Использую существующие данные."
  → System: "Переходим к сбору новой идеи..."
  → System loads step-01-collect-ideas.md
```

**Time Saved:** 20-25 minutes (entire foundation sequence skipped)

---

### Scenario C: Partial Update (Some Data Stale)

**Initial State:**
- All 4 files exist
- Resources data updated 95 days ago (stale threshold: 90 days)
- User wants to update just resources

**User Experience:**
```
✅ **Фундаментальные данные уже заполнены!**

[Summary shown as above]

ℹ️ Ваши данные о ресурсах обновлены 95 дней назад.
Возможно, что-то изменилось (новые инструменты, команда, бюджет)?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 **Что дальше?**

[S]kip - Пропустить (использовать существующие данные)
[U]pdate - Обновить часть данных (выбор, что именно)
[R]e-enter - Заново заполнить все
```

**Flow (User chooses [U]):**
```
User: [U]

System shows:
Что нужно обновить?

[1] Цели (1/3/5-10 лет) - последнее обновление: 15 дней назад ✅
[2] Стадия проекта (Точка А) - последнее обновление: 15 дней назад ✅
[3] Ресурсы (команда, LLM, бюджет) - последнее обновление: 95 дней назад ⚠️
[4] Оптимизация (tech stack, подход) - последнее обновление: 15 дней назад ✅
[A]ll - Всё заново

Выберите номера через запятую (например: 1,3) или [A]ll:

User: 3
  → System loads step-00.6-resource-assessment.md
  → User updates resources (new team member, upgraded to Claude Opus)
  → System saves updated resource-assessment.md
  → System: "✅ Ресурсы обновлены. Возвращаемся к workflow..."
  → System loads step-01-collect-ideas.md
```

**Time Saved:** ~15 minutes (only updated 1 section instead of all 4)

---

### Scenario D: Quick Update Mid-Workflow

**Initial State:**
- User is at Step 04 (Consilium)
- Realizes project stage has changed (reached D3 from D2)
- Wants to update without restarting workflow

**User Experience:**
```
[User is in Step 04]

User types: /update-foundation

System shows:
🛠️ **Быстрое обновление фундаментальных данных**

Текущие данные:
1. ✅ Цели: обновлено 20 дней назад
2. ✅ Стадия проекта: обновлено 20 дней назад
3. ✅ Ресурсы: обновлено 5 дней назад
4. ✅ Оптимизация: обновлено 20 дней назад

Что обновить?

[1] Цели (1/3/5-10 лет)
[2] Стадия проекта (Точка А)
[3] Ресурсы (команда, LLM, бюджет)
[4] Оптимизация (tech stack, подход)
[A]ll - Всё заново
[C]ancel - Отмена

User: 2
  → System loads step-00.5-project-stage.md
  → User updates: D2 → D3, 65% → 75%, new blocker
  → System saves
  → System: "✅ Стадия проекта обновлена. Возвращаемся к Step 04..."
  → System loads step-04-consilium.md (continues where left off)
```

**Time Saved:** Seamless update without losing workflow context

---

### Scenario E: Missing Data Detection

**Initial State:**
- 3/4 files exist (goals, stage, optimization)
- Resources file missing (deleted or corrupted)
- User starts workflow

**User Experience:**
```
⚠️ **Неполные фундаментальные данные**

Найдено: 3/4 файлов

✅ Заполнено:
  - goals.yaml (обновлено 15 дней назад)
  - project-stage-assessment.md (обновлено 15 дней назад)
  - optimization-suggestions.md (обновлено 15 дней назад)

❌ Отсутствует:
  - resource-assessment.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 **Что дальше?**

[C]omplete - Заполнить недостающие данные (только отсутствующие шаги)
[R]e-enter - Заново заполнить всё (сброс и полный повтор)
[S]kip - Продолжить без полных данных (⚠️ не рекомендуется)

User: [C]
  → System loads step-00.6-resource-assessment.md
  → User completes resources section
  → System saves resource-assessment.md
  → System: "✅ Все данные собраны (4/4). Продолжаем..."
  → System loads step-01-collect-ideas.md
```

**Time Saved:** ~17-20 minutes (skipped 3 existing steps)

---

## Staleness Detection Logic

### Thresholds by Data Type

| Data Type | Staleness Threshold | Reason |
|-----------|---------------------|--------|
| **Goals** | 180 days (6 months) | Long-term goals change slowly |
| **Project Stage** | 30 days (1 month) | Project stage can progress quickly |
| **Resources** | 90 days (3 months) | Team/tools change moderately |
| **Optimization** | 90 days (3 months) | New tools/frameworks appear frequently |

### Warning Messages

**For 30-60 days old (Yellow Zone):**
```
ℹ️ Данные о {section} обновлены {N} дней назад.
Проверьте актуальность, если что-то изменилось.

[R]eview - Просмотреть и обновить
[K]eep - Оставить как есть
```

**For 60-90 days old (Orange Zone):**
```
⚠️ Данные о {section} обновлены {N} дней назад.
Рекомендуем проверить актуальность.

[R]eview - Просмотреть и обновить (рекомендуется)
[K]eep - Оставить как есть
[L]ater - Напомнить через 30 дней
```

**For 90+ days old (Red Zone):**
```
🚨 Данные о {section} обновлены {N} дней назад!
Данные могли устареть, обновите для точных результатов.

[R]eview - Просмотреть и обновить (настоятельно рекомендуется)
[K]eep - Оставить как есть (⚠️ может повлиять на точность)
```

### Implementation Details

**Check staleness on every foundation-check run:**
```bash
# Calculate days since last update
FILE_TIMESTAMP=$(stat -f %m "{file}")
CURRENT_TIMESTAMP=$(date +%s)
DAYS_OLD=$(( (CURRENT_TIMESTAMP - FILE_TIMESTAMP) / 86400 ))

# Check thresholds
if [ $DAYS_OLD -gt 180 ] && [ "$FILE" == "goals.yaml" ]; then
  STALENESS="RED"
elif [ $DAYS_OLD -gt 90 ] && [ "$FILE" == "resource-assessment.md" ]; then
  STALENESS="RED"
elif [ $DAYS_OLD -gt 30 ] && [ "$FILE" == "project-stage-assessment.md" ]; then
  STALENESS="YELLOW"
fi
```

**Store staleness check in memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:staleness:{file}:last-check" \
  --content "{timestamp}|{days_old}|{user_action}"
```

---

## User Action Tracking

### Memory Storage Format

```yaml
life-os:foundation-check:history:
  - timestamp: "2026-02-01T10:30:00Z"
    action: "skip"
    files_exist: 4
    staleness: [15, 15, 5, 15]  # days old for each file

  - timestamp: "2026-01-15T14:20:00Z"
    action: "update"
    sections_updated: [3]  # Resources
    time_saved_minutes: 17

  - timestamp: "2025-12-20T09:00:00Z"
    action: "re-enter"
    reason: "major project pivot"
    time_invested_minutes: 22
```

### Usage Analytics

**Track patterns:**
- How often user skips vs updates
- Which sections updated most frequently
- Average time between updates per section
- Most common update combinations (e.g., always update stage+resources together)

**Use for:**
- Intelligent defaults (if user always skips, auto-skip with notification)
- Predictive staleness warnings
- Workflow optimization suggestions

---

## Integration with Workflow Routing

### Old Routing (Before Foundation Check)

```yaml
mode == create:
  → step-00.5-project-stage.md  # Always forced user through all steps
  → step-00.6-resource-assessment.md
  → step-00.7-optimization-intelligence.md
  → step-00-goals-discovery.md
  → step-01-collect-ideas.md
```

**Problem:** User forced to re-enter data every time (20-25 min waste)

### New Routing (With Foundation Check)

```yaml
mode == create:
  → step-00-foundation-check.md
      │
      ├─ All 4/4 exist + [Skip]
      │   → step-01-collect-ideas.md (0 min overhead)
      │
      ├─ All 4/4 exist + [Update: 3]
      │   → step-00.6-resource-assessment.md (3 min)
      │   → step-01-collect-ideas.md
      │
      ├─ Some 2/4 exist + [Complete]
      │   → step-00.6-resource-assessment.md (3 min)
      │   → step-00-goals-discovery.md (10 min)
      │   → step-01-collect-ideas.md
      │
      └─ None 0/4 exist + [Continue]
          → step-00.5-project-stage.md
          → step-00.6-resource-assessment.md
          → step-00.7-optimization-intelligence.md
          → step-00-goals-discovery.md
          → step-01-collect-ideas.md (full 22 min sequence)
```

**Benefit:** Intelligent routing saves 0-20 minutes depending on what exists

---

## Quick Reference Card

### File Locations
```
{bmb_creations_output_folder}/life-os/
├── goals.yaml                         # Step 00 output
├── project-stage-assessment.md        # Step 0.5 output
├── resource-assessment.md             # Step 0.6 output
└── optimization-suggestions.md        # Step 0.7 output
```

### Menu Options Quick Guide

| Option | When Shown | Action | Time Impact |
|--------|------------|--------|-------------|
| `[S]kip` | All data exists | Use existing data, skip to Step 01 | Saves 20-25 min |
| `[U]pdate` | All data exists | Choose specific sections to update | Saves 5-20 min |
| `[R]e-enter` | Any data exists | Reset all, start from scratch | Full 22 min sequence |
| `[C]omplete` | Some data missing | Fill only missing sections | Saves 3-19 min |
| `[C]ontinue` | No data exists | Collect all foundation data | Full 22 min (required) |
| `[Q]uit` | No data exists | Exit without collecting | N/A |

### Global Command

**`/update-foundation`** - Available at ANY step in workflow
- Access quick update menu
- Update any foundation section
- Return to original step after update
- No context loss

---

## Error Recovery Scenarios

### File Corrupted or Invalid YAML

```
⚠️ **Проблема с файлом данных**

Файл {filename} существует, но содержит ошибки:
- {error_details}

[F]ix - Попытаться автоматически исправить
[R]e-enter - Заново заполнить этот раздел
[I]gnore - Продолжить (⚠️ может вызвать ошибки дальше)

Выбор: [F] / [R] / [I]
```

### File Access Permissions Issue

```
🚨 **Ошибка доступа к файлу**

Не удается прочитать {filename}
Причина: {permission_error}

[R]etry - Повторить попытку
[S]kip - Пропустить этот файл
[A]bort - Прервать и выйти

Выбор: [R] / [S] / [A]
```

### Conflicting Data Between Files

```
⚠️ **Обнаружены несоответствия в данных**

- goals.yaml указывает timeline: 6 месяцев
- project-stage-assessment.md указывает completion: 65%
- Эти данные не согласуются (65% за 6 мес = слишком медленно)

[U]pdate - Обновить несогласованные разделы
[I]gnore - Продолжить как есть
[E]xplain - Объяснить подробнее

Выбор: [U] / [I] / [E]
```

---

**End of Foundation Check Examples**
