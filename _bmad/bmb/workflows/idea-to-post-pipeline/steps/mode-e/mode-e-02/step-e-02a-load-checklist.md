---
description: Load edit-improvements-checklist.md and display all improvement categories
name: step-e-02a-load-checklist
nextStepFile: ./step-e-02b-evaluate.md
type: load-checklist
---

# EDIT E-02a: Load Improvement Checklist

## STEP GOAL:

Load the standardized edit-improvements-checklist.md and present all categories for systematic post improvement.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Checklist Loading

```
═══════════════════════════════════════════════════════════════

  ✅ CHECKLIST EDIT: Систематическое улучшение

  Загружаю чек-лист улучшений...

═══════════════════════════════════════════════════════════════
```

### 2. Load Checklist

Load from: `data/checklist-templates/edit-improvements-checklist.md`

```
Чек-лист успешно загружен!

📋 EDIT IMPROVEMENTS CHECKLIST (v2.1)

Категории улучшений:

✅ HOOK (ПРИВЛЕЧЕНИЕ ВНИМАНИЯ) — 8 пунктов
   • Заголовок захватывает внимание
   • Обещание результата ясно
   • Интрига или вопрос привлекает
   • Эмоция включена в начало
   • Цифры/факты поддерживают хук
   • Длина оптимальна (не дольше 10-12 слов)
   • Уникальность (не дубликат других постов)
   • Срочность или FOMO добавлены

✅ PROBLEM (ОПРЕДЕЛЕНИЕ ПРОБЛЕМЫ) — 7 пунктов
   • Боль аудитории понятна
   • Проблема конкретизирована
   • Читатель себя видит в описании
   • Стоимость проблемы показана
   • Эмоция к проблеме добавлена
   • Контекст объяснен (когда/где возникает)
   • Социальное доказательство (другие тоже страдают)

✅ SOLUTION (РЕШЕНИЕ) — 8 пунктов
   • Решение ясно и понятно
   • Практические шаги перечислены
   • Примеры даны (mini case study)
   • До-после показано
   • Инструменты/ресурсы перечислены
   • Время внедрения указано
   • Легкость реализации показана
   • Результаты подтверждены

✅ CTA (ПРИЗЫВ К ДЕЙСТВИЮ) — 6 пунктов
   • CTA ясна и конкретна
   • Не более 1-2 вариантов действия
   • Результат действия объяснен
   • Срочность добавлена (делай прямо сейчас)
   • Ссылка/контакт легко найти
   • Возражения предусмотрены (FAQ)

✅ ENGAGEMENT (ВОВЛЕЧЁННОСТЬ) — 7 пунктов
   • Диалог с читателем поддерживается
   • Вопросы к читателю включены
   • Личный опыт/история добавлены
   • Уязвимость/честность показана
   • Юмор уместен (если есть)
   • Длина оптимальна (не слишком длинно)
   • Читаемость хорошая (абзацы, маркеры)

═══════════════════════════════════════════════════════════════
```

### 3. Present Checklist Overview

```
📊 ОБЩАЯ ИНФОРМАЦИЯ:

Всего пунктов в чек-листе: 36
Категорий: 5 (Hook, Problem, Solution, CTA, Engagement)

📝 КАК РАБОТАЕТ:

1. Я загру́жу посты из твоей базы
2. Проверю каждый пост по чек-листу
3. Покажу какие пункты PASSED, какие FAILED
4. Рекомендую что улучшать
5. Применю улучшения (с твоим одобрением)

⏱️  ВРЕМЯ ПРОВЕРКИ:
   • 1 пост: ~2-3 минуты
   • 5 постов: ~10-15 минут
   • 10+ постов: ~20-30 минут
```

### 4. Present Next Options

```
═══════════════════════════════════════════════════════════════

ДАЛЬШЕ?

[A] ALL POSTS — Проверить все посты в базе
    Загружу все опубликованные посты (N шт)

[S] SPECIFIC — Выбрать конкретные посты
    Ты выберешь какие посты проверить

[F] FILTER — Проверить по критериям
    Например: посты за последний месяц
    или посты с CTR < 2%

[C] CUSTOM — Загрузить другой чек-лист
    Есть ли свой чек-лист который использовать?

[B] BACK — Вернуться в EDIT меню

═══════════════════════════════════════════════════════════════
```

Wait for user selection.

---

## CHECKLIST STRUCTURE

The loaded checklist includes:

**HOOK** (8 items)
- Attention-grabbing headline
- Clear promise of result
- Intrigue or question
- Emotional element
- Supporting facts/numbers
- Optimal length
- Uniqueness
- Urgency/FOMO

**PROBLEM** (7 items)
- Audience pain is clear
- Problem is concrete
- Reader sees themselves
- Cost of problem shown
- Emotion added
- Context explained
- Social proof included

**SOLUTION** (8 items)
- Solution is clear
- Practical steps listed
- Examples given
- Before-after shown
- Tools/resources listed
- Implementation time stated
- Ease of implementation
- Results confirmed

**CTA** (6 items)
- CTA is clear
- 1-2 action options max
- Result of action explained
- Urgency added
- Link/contact easy to find
- Objections addressed

**ENGAGEMENT** (7 items)
- Dialogue maintained
- Questions included
- Personal story shared
- Vulnerability shown
- Humor appropriate
- Optimal length
- Good readability

---

## SUCCESS CRITERIA

- ✅ Checklist loaded successfully
- ✅ All 5 categories presented
- ✅ All 36 items explained
- ✅ User understands checklist structure
- ✅ User knows what to check next

---

## NEXT STEP

Handle user selection:
- [A] → Load all posts → Execute `./step-e-02b-evaluate.md`
- [S] → Let user select posts → Execute `./step-e-02b-evaluate.md`
- [F] → Apply filter → Execute `./step-e-02b-evaluate.md`
- [C] → Allow custom checklist upload
- [B] → Return to `../mode-e-00-menu.md`
