# FAQ: Часто задаваемые вопросы

## WORKFLOW Questions

### Q: В каком режиме мне начать?
**A:** Это зависит от твоей ситуации:
- **Ты только начинаешь?** → CREATE MODE (collaborative learning)
- **У тебя уже есть контент?** → EDIT MODE (улучшение)
- **Нужно быстро много контента?** → YOLO MODE (full automation)
- **Нужна проверка качества?** → VALIDATE MODE (quality assurance)

### Q: Могу ли я переключаться между режимами?
**A:** Да! Это нормально:
- Создал посты в CREATE → Валидируй в VALIDATE
- Нашёл плохие посты → Улучшай в EDIT
- Нужно срочно много контента → YOLO MODE
- All modes save state, so you can pause and resume

### Q: Если я прерву процесс, смогу ли я продолжить?
**A:** Да! Все режимы сохраняют состояние в `workflow_state.json`:
- Можешь выйти в любой момент
- Вернись позже и выбери "Resume from last step"
- Полный контекст восстановится автоматически

### Q: Как долго обычно занимает создание контента?

**A:** Смотри [timing-sla.md](./timing-sla.md):
- **CREATE MODE:** 60-90 мин для 3 постов
- **EDIT MODE:** 30-60 мин для 10-20 постов
- **VALIDATE MODE:** 10-30 мин для проверки
- **YOLO MODE:** 45-55 мин для 9-15 постов (вместо 6-8 часов!)

---

## QUALITY Questions

### Q: Какой качество контента я должен ожидать?

**A:** Зависит от режима:
- **CREATE:** 85-95% качество (user-guided, высокое)
- **EDIT:** 80-90% качество (AI recommendations)
- **VALIDATE:** Identifies issues correctly 95%+ (but doesn't write)
- **YOLO:** 75-85% качество (MVP quality, fast)

Все посты проходят validation перед публикацией.

### Q: Что такое "quality score"?

**A:** Это average of 5 checks:
1. **Quality Checklist:** Hook/problem/solution/CTA/tone (0-100)
2. **CTR Potential:** (urgency + specificity + curiosity) / 3 (0-5%)
3. **Consistency:** Tone/format/length consistency (0-100)
4. **Copy Audit:** Strong verbs, specific numbers, clear benefits (0-100)
5. **Engagement:** Hook + social proof + CTA strength (1-5 stars)

Average these → quality_score (0-100)

### Q: Если пост не прошёл валидацию, что делать?

**A:** Зависит от score:
- **score >= 90%:** Ready to publish
- **70-90%:** NEEDS IMPROVEMENT (фиксим в EDIT MODE)
- **< 70%:** NEEDS REWRITE (полная переделка)

Check [edit-improvements-checklist.md](../checklist-templates/edit-improvements-checklist.md) for what to fix.

### Q: Как я узнаю если мой контент хороший?

**A:** Смотри метрики:
- **CTR (Click-Through Rate):** 3%+ хороший
- **Engagement Rate:** 2%+ хороший
- **Shares:** Люди переделятся постом
- **Comments:** Люди отвечают / задают вопросы
- **Quality Score:** 85%+ хороший

More in [success-criteria.md](./success-criteria.md).

---

## RESEARCH Questions

### Q: Как я выбираю идею для исследования?

**A:** Идея должна пройти [idea-validation-checklist.md](../checklist-templates/idea-validation-checklist.md):
- Специфичная (не общая)
- Исследуемая (5+ источников доступны)
- Аудитория понятна
- Не дубликат
- Вызывает интерес

### Q: Сколько времени занимает исследование?

**A:** 15-20 мин для 1 идеи (5-8 углов найдено)

Если дольше:
- Идея слишком узкая? → Выбери другую
- Нужно больше деталей? → Продай исследование
- Интернет медленный? → Проверь соединение

### Q: Что такое "угол" в исследовании?

**A:** Это разный способ преподнести одну идею:

Идея: "ИИ помогает с контентом"

Разные углы:
1. **Time:** "ИИ сокращает время на 70%"
2. **Quality:** "ИИ контент может быть качественнее"
3. **Cost:** "ИИ дешевле чем нанимать копирайтера"
4. **Scalability:** "ИИ позволяет масштабировать"
5. **Psychology:** "Почему urgency работает в CTR"

Каждый угол = новый пост для разных читателей

### Q: Сколько углов нужно найти?

**A:**
- Минимум: 5 углов
- Хорошо: 7-8 углов
- Отлично: 9-10 углов

Больше углов = больше вариантов = лучше покрытие аудитории

---

## WRITING Questions

### Q: Как написать хороший пост?

**A:** Используй структуру: Hook → Problem → Solution → Trigger → CTA

- **Hook:** Первое предложение привлекает внимание (urgency/curiosity/pattern-interrupt)
- **Problem:** Вторая часть описывает боль целевой аудитории
- **Solution:** Третья часть предлагает конкретное решение
- **Trigger:** Четвёртая часть добавляет social proof или цифры
- **CTA:** Конец призывает к действию (save/share/click)

Больше в [post-quality-checklist.md](../checklist-templates/post-quality-checklist.md).

### Q: Какая длина оптимальна для поста?

**A:** Зависит от платформы:
- **Telegram:** 100-500 characters (один скролл)
- **LinkedIn:** 300-500 characters (оптимум)
- **Twitter:** 280 characters max
- **Instagram:** 300-500 characters

Варианты:
- 500 chars: Полный пост с деталями
- 250 chars: Краткая версия
- 100 chars: Super short hook

### Q: Мне нужны все 3 варианта (500/250/100)?

**A:** Зависит:
- **CREATE MODE:** Да, I'll generate all 3
- **EDIT MODE:** Выбирай какие нужны
- **VALIDATE MODE:** No, validation only
- **YOLO MODE:** Yes, all 3 generated + variants

All variants saved in posts_content_template.csv

### Q: Что такое "variants" и когда они нужны?

**A:** Variants = 3-4 alternative versions of same post with different angles:

Original post (educational angle):
"Пошагово: как настроить ИИ для контента (за 15 мин)"

Variants:
1. **Emotional:** "Устал писать посты 8 часов? ИИ спасает"
2. **Social Proof:** "5 успешных фаундеров уже используют"
3. **Curiosity:** "Вот чего ты не знаешь про ИИ и контент..."

**When needed:**
- YOLO MODE: автоматически генерирует
- EDIT MODE: если хочешь A/B тестировать
- CREATE MODE: manually, if you want

---

## DATA Questions

### Q: Где хранится мой контент?

**A:** В CSV files (local storage):
- **ideas_inbox.csv:** Raw ideas
- **ideas_research.csv:** Research results
- **posts_content.csv:** Написанные посты
- **metrics_tracking.csv:** Метрики (views, CTR, engagement)
- **angles_library.csv:** Библиотека использованных углов

Files located: `/posts/` directory (local)

### Q: Как я могу увидеть мои посты?

**A:** Несколько способов:
1. **EDIT MODE:** Load posts and browse
2. **CSV files:** Открой в Excel/Google Sheets
3. **VALIDATE MODE:** Generate quality report

### Q: Могу ли я экспортировать мои данные?

**A:** Да!
- CSV files можно открыть в Excel
- Можно копировать в Google Sheets
- Можно экспортировать в JSON (special request)
- Backup автоматический (daily)

### Q: Что если я случайно удалил пост?

**A:** Есть автоматический backup:
- Daily backups в `/posts/.backup/`
- Can restore from any date
- Contact me for recovery

### Q: Сколько постов я могу хранить?

**A:** Нет лимита (technologically), но рекомендуется:
- Archive posts > 6 months old (для speed)
- Keep active posts < 1 year
- Use EDIT MODE to clean up

---

## PERFORMANCE Questions

### Q: Почему мои посты имеют низкий CTR?

**A:** Смотри [edit-improvements-checklist.md](../checklist-templates/edit-improvements-checklist.md):

**Common issues:**
- ❌ Hook слабый → Усилить urgency/curiosity
- ❌ Problem не ясна → Уточнить боль читателя
- ❌ CTA слабый → Сделать более явным
- ❌ Timing неудачный → Опубликовать в другое время

Use EDIT MODE to rewrite and improve.

### Q: Как мне улучшить мои метрики?

**A:** Strategy:
1. **Analyze:** Какие посты работают, какие нет
2. **Learn:** Что общего у успешных
3. **Improve:** Применить lessons к новым постам
4. **Iterate:** Repeat cycle

Use [success-criteria.md](./success-criteria.md) to track progress.

### Q: Какой средний CTR я должен ожидать?

**A:**
- Week 1: 2-2.5% (новый контент)
- Week 2-4: 3%+ (learning curve)
- Week 5+: 3.5-4%+ (опыт накапливается)

If stuck at <2% after month → review your topic/audience fit

---

## TECHNICAL Questions

### Q: Что если workflow.md завис?

**A:** Try:
1. Exit current session (Ctrl+C or close)
2. Open workflow.md again
3. Choose "Resume from last step"
4. Все контекст восстановится

If still stuck:
- Reset: Delete workflow_state.json (start fresh)
- Check: Internet connection, file permissions

### Q: Где я найду все файлы?

**A:** Directory structure:
```
_bmad-output/bmb-creations/workflows/idea-to-post-pipeline/
├── workflow.md (master entry point)
├── steps/ (все шаги для всех режимов)
├── data/
│   ├── csv-templates/ (templates for data)
│   ├── checklist-templates/ (quality checklists)
│   └── reference/ (guides like this FAQ)
└── posts/ (ваш создаваемый контент)
```

### Q: Могу ли я использовать workflow offline?

**A:** Да! Workflow полностью offline:
- No internet required
- No API calls
- All processing local
- Can work on flight

Just make sure CSV files accessible.

### Q: Как я делаю backup?

**A:** Automatic backups:
- Daily backup в `/posts/.backup/YYYY-MM-DD/`
- Manual: Copy `/posts/` folder to safe location
- Cloud: Upload CSV files to Google Drive / Dropbox

---

## CONTINUATION Questions

### Q: Я закрыл workflow, как вернуться?

**A:** Simple:
1. Open workflow.md again
2. It will ask: "Resume from last session?"
3. Click [Y] Yes
4. Вы вернётесь на последний шаг со всем контекстом

### Q: Я могу менять режимы без потери прогресса?

**A:** Да! Каждый режим сохраняет своё состояние:
- CREATE MODE: Сохранит какую идею ты исследовал
- EDIT MODE: Сохранит какие посты ты редактировал
- VALIDATE MODE: Сохранит какие посты ты проверял
- YOLO MODE: Сохранит progress до summary

Все accessible later via workflow_state.json

### Q: Можно ли работать на двух разных проектах одновременно?

**A:** Технически возможно, но не рекомендуется (может confuse context).

Better approach:
1. Finish project 1 (CREATE/EDIT/VALIDATE cycle)
2. Archive posts from project 1
3. Start fresh project 2

Each project gets own workflow_state.json

---

## HELP Questions

### Q: Где ещё я могу найти помощь?

**A:** Resources:
- **Checklists:** `/data/checklist-templates/` (quality guides)
- **Reference:** `/data/reference/` (this FAQ, SLAs, success criteria)
- **Templates:** `/data/csv-templates/` (data structure)

### Q: Что если мой вопрос не в FAQ?

**A:** Options:
1. Use Advanced Elicitation (Mode [A]) to explore
2. Use Party Mode (Mode [P]) to discuss with multiple perspectives
3. Ask me directly in any step (I'm listening)

### Q: Как я могу улучшить этот workflow?

**A:** Feedback welcome!
- Что работает хорошо?
- Что не работает?
- Что добавить?

Changes can be made dynamically during use.

---

## COMMON ISSUES & SOLUTIONS

| Issue | Cause | Solution |
|-------|-------|----------|
| Posts scoring low | Weak hook/CTA | Use edit-improvements-checklist |
| CTR not improving | Same angles repeatedly | Add new angles from angles_library |
| Workflow too slow | Small batches | Try YOLO MODE or batch operations |
| Data looks wrong | Typos in CSV | Recheck entries in source file |
| Can't resume | workflow_state.json missing | Start fresh from step-01-init |
| Too much content | Not archiving old posts | Use EDIT MODE to archive |

---

Last updated: 2026-01-27
Questions? Ask anytime during workflow!
