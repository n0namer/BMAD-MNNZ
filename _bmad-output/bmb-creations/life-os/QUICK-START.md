---
created: 2026-02-05
type: quick-start-guide
audience: Nikita
time: 5 минут
---

# PDCA + Goals - Quick Start (5 минут)

## ⚡ Шаг 1: Определи цели (2 минуты)

```bash
# Запусти Goals Discovery
cd D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\life-os

# Открой step-00 в Claude Code и следуй инструкциям:
# steps-c/step-00-goals-discovery.md
```

**Что заполнить:**
- 📅 **2026 цели** (год): Katana 2 Scaled-Live, Автоответчик $50k MRR, минус 5 кг, английский C1
- 📆 **Q1 2026** (квартал): Epic L complete, Автоответчик MVP + 100 clients
- 📍 **Feb 2026** (месяц): Epic L, funding $36.5k, минус 2 кг

**Сохранится в:** `bmb-creations/life-os/goals.yaml`

---

## ⚡ Шаг 2: Генерируй TODO (1 минута)

```bash
cd automation

# Установи зависимости (если нужно)
pip install pyyaml

# Генерируй Week 1 TODO (Mon-Fri)
bash generate-daily-todo.sh
```

**Результат:**
```
output/todos/
├── 2026-02-10-mon.md  ← Katana Story 2, Funding research
├── 2026-02-11-tue.md  ← Story 2 tests, Pitch deck
├── 2026-02-12-wed.md  ← Innovation Sprint setup
├── 2026-02-13-thu.md  ← AutoML research
└── 2026-02-14-fri.md  ← Weekly review
```

---

## ⚡ Шаг 3: Синхронизируй календарь (2 минуты)

### Вариант A: Быстрый (iCal export)

```bash
# Уже готов! Файлы в output/todos/ics/
# Импортируй в Google Calendar:
# Settings → Import & Export → Import → Выбери .ics файл
```

### Вариант B: Автоматический (Google Calendar API)

```bash
# OAuth setup (один раз)
python scripts/setup_google_oauth.py  # Следуй инструкциям

# Настройка
cp calendar-sync-config.template.yaml calendar-sync-config.yaml
# Редактируй: enabled: true, calendar_id: "твой_id"

# Первая синхронизация
python calendar_sync.py --sync --dry-run  # Проверка
python calendar_sync.py --sync            # Применить
```

---

## ✅ Готово! Теперь работай:

**Утро (08:00):**
- 📖 Открой сегодняшний TODO (например, `2026-02-10-mon.md`)
- 📅 Проверь календарь (time blocks уже там)
- 🎯 Начни с High Priority задач

**День:**
- ✅ Отмечай выполненные задачи в TODO файле
- ⏱️ Обнови Calendar если изменились планы

**Вечер (18:00):**
- 📝 Daily Review (5 минут):
  ```markdown
  ## ✅ Completed
  - Katana Story 2 coding ✅
  - Funding research ✅

  ## ⏸️ Not Done
  - Story 2 tests → Tomorrow

  ## 🚧 Blockers
  - None

  ## 📝 Learnings
  - Data integration faster than expected

  ## ⏭️ Tomorrow
  - Finish Story 2 tests
  - Create pitch deck
  ```

**Воскресенье (19:00):**
- 📊 Weekly Review (30 минут) - используй `templates/reviews/weekly-review.template.md`
- 🔄 Генерируй TODO на следующую неделю: `bash generate-daily-todo.sh`

---

## 📊 Метрики (опционально, но полезно):

```bash
cd ../metrics

# Собери данные за неделю
python collect_metrics.py

# Посчитай метрики
python calculate_metrics.py

# Покажи dashboard
python generate_dashboard.py --format cli
```

**7 метрик:**
1. Completion Rate (сколько задач выполнено)
2. Velocity (задач в день)
3. Focus Time (часов глубокой работы)
4. Goal Progress (% к целям)
5. Alignment Score (% задач aligned с целями)
6. Burnout Risk (индикатор перегрузки)
7. Domain Balance (распределение времени)

---

## 🚨 Если что-то не работает:

**TODO не генерируется:**
```bash
# Проверь goals.yaml
cat ../data/goals.yaml

# Убедись что есть week_focus и tasks
```

**Calendar sync не работает:**
```bash
# Проверь конфиг
cat calendar-sync-config.yaml

# Используй fallback (iCal export)
ls output/todos/ics/*.ics
```

**Метрики показывают 0%:**
```bash
# Убедись что TODO файлы в todos/archive/
ls ../output/todos/archive/

# Daily review сохранён в reviews/daily/
ls ../reviews/daily/
```

---

## 📖 Полная документация:

- **PDCA-INTEGRATION-GUIDE.md** - Полное руководство (941 строка)
- **automation/README.md** - TODO generation docs
- **automation/calendar-sync.md** - Calendar sync docs
- **metrics/dashboard.md** - Metrics docs

---

## 🎯 Week 1 Example (Nikita):

**Goals (Q1 2026):**
```yaml
finance: "Katana Epic L complete + Paper Trading, Автоответчик funding + MVP"
business: "2 projects validated, PMF confirmed"
```

**Week 1 Focus:** "Katana Epic L completion + Автоответчик funding"

**Daily TODOs:**
- **Mon**: Katana Story 2 coding (2h), Funding research (1h)
- **Tue**: Story 2 tests (2h), Pitch deck (2h)
- **Wed**: Story 3 start (2h), Investor outreach (1h)
- **Thu**: Story 3 coding (3h), F&F meeting (1h)
- **Fri**: Weekly review (1h), Plan Week 2 (30min)

**Results (End of Week):**
- ✅ Epic L: 2/11 stories complete (18% progress)
- ✅ Автоответчик: $20k funding confirmed (55% of $36.5k goal)
- 📊 Completion Rate: 85%
- ⚡ Burnout Risk: 15% (healthy)

---

**⏰ Total Setup Time:** 5 minutes
**Daily Time:** 5-10 minutes (morning review + evening update)
**Weekly Time:** 30 minutes (Sunday review)

**ROI:** ~300% (30 минут инвестиций → 2 часа экономии за неделю)

---

**🚀 START NOW: Open `steps-c/step-00-goals-discovery.md`**
