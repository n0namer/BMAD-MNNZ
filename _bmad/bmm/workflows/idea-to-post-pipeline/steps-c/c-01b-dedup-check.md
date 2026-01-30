---
description: Check if new idea is duplicate of existing ideas before adding to database
name: step-c-01b-dedup-check
nextStepFile: ./c-00-menu.md
type: validation-deduplication
---

# CREATE C-01B: Deduplication Check

## STEP GOAL:

Check if new idea is a duplicate of existing ideas. If potential duplicate found, help user decide: same idea, different angle, or entirely new idea.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting duplicate check results.**
**ONLY proceed when user confirms they understand the results.**

---

## PROCESS OVERVIEW

```
1. Normalize input (lowercase, remove stopwords, extract keywords)
2. Search ideas_inbox.csv + ideas_research.csv for similar ideas
3. Calculate word overlap percentage for each potential match
4. If matches found with >60% overlap → Present to user
5. User decides: Same idea / Different angle / Completely new
```

---

## EXECUTION STEPS

### 1. Display Check Starting

```
═══════════════════════════════════════════════════════════════

  🔍 DEDUPLICATION CHECK

  Проверяю, не похожа ли эта идея на уже существующие...

═══════════════════════════════════════════════════════════════
```

### 2. Normalize & Extract Keywords

From user's new idea:
- Convert to lowercase
- Remove Russian stopwords (и, или, что, это, для, с, по, etc.)
- Extract key terms (3-5 main concepts)
- Extract category keywords

**Example normalization:**
```
Input: "ИИ контент за 3 часа с помощью нейросетей"
Keywords: [ИИ, контент, нейросети, час]
```

### 3. Search Existing Ideas

Search in:
- `ideas_inbox.csv` - raw ideas awaiting research
- `ideas_research.csv` - researched ideas with angles

For EACH existing idea, calculate:
- **Word Overlap**: Common keywords / total unique keywords
- **Semantic Similarity**: Similar categories, related topics
- **Match Score**: (Word Overlap × 70%) + (Category Similarity × 30%)

### 4a. NO MATCHES FOUND (Score < 60%)

```
✅ Проверка завершена

Хорошие новости - это оригинальная идея!
Не найдено похожих идей в базе.

Можно добавлять. 👍

[Y] Добавить в ideas_inbox
[N] Вернуться к меню
```

**[Y] - Add to Inbox:**
Return to step c-01, save the idea to ideas_inbox.csv with:
- `duplicate_check: "passed - original"`
- `dedup_score: "0%"`
- `dedup_date: [today]`

**[N] - Back to Menu:**
Load `./c-00-menu.md`

---

### 4b. MATCHES FOUND (Score 60-100%)

```
═══════════════════════════════════════════════════════════════

  ⚠️  ПОХОЖИЕ ИДЕИ НАЙДЕНЫ

  Твоя идея похожа на [N] существующ(ую/ые):

═══════════════════════════════════════════════════════════════

MATCH #1 (84% similarity)
├─ Идея: "ИИ для создания контента"
├─ Статус: researched (5 углов найдено)
├─ Добавлено: 2026-01-25
├─ Категория: automation
└─ Общее: ИИ, контент, создание

MATCH #2 (71% similarity)
├─ Идея: "Автоматизация постов нейросетями"
├─ Статус: inbox
├─ Добавлено: 2026-01-24
├─ Категория: automation
└─ Общее: ИИ, посты, автоматизация

─────────────────────────────────────────────────────────────

Что это:

[1] ДУБЛИКАТ — Это та же идея, не добавлять
[2] ДРУГОЙ УГОЛ — Похожая тема, но новая идея/подход
[3] ДРУГОЕ — Это совсем другая идея, дубликата нет

═════════════════════════════════════════════════════════════
```

#### OPTION [1] - DUPLICATE

```
Понял, это дубликат.

❌ Идея НЕ добавлена в inbox

Рекомендация:
→ Используй найденную идею (#[N])
→ Добавь свой угол в angles_library (если новый подход)
→ Или выбери совсем другую идею

[R] RESEARCH — Исследуй найденную идею вместо
[A] ADD NEW — Добавь совсем другую идею
[M] Back to MENU — Другие операции
```

**[R] - Research:**
Load found idea and execute `./c-02c-research.md`

**[A] - Add New:**
Return to step c-01 (request new idea)

**[M] - Back to Menu:**
Load `./c-00-menu.md`

**Log duplicate attempt:**
```csv
# In ideas_inbox.csv (optional duplicate_log field):
id,date_added,source,raw_idea,category,status,duplicate_check,duplicate_matched_id
[NEW],today,user_input,"[idea]",[cat],rejected,true,[MATCHED_ID]
```

---

#### OPTION [2] - DIFFERENT ANGLE

```
Понял, это новый угол на похожую тему.

✅ Добавляю как NEW IDEA + связываю с найденной

Твоя идея будет:
├─ Статус: active (в inbox)
├─ Связь с идеей #[N]: related_idea
└─ Пометка: "Новый угол на тему: [original]"

Плюсы:
• Больше углов на одну тему = больше контента
• Можно написать несколько постов на одну идею
• Кросс-ссылки в контенте
```

**Save idea with:**
- `status: "active"` (to ideas_inbox.csv)
- `duplicate_check: "passed - new_angle"`
- `dedup_score: "[similarity]%"`
- `dedup_date: [today]`
- `related_idea_id: [MATCHED_ID]` (link to similar idea)

**Add to angles_library.csv:**
```csv
idea_id,angle_name,perspective,related_idea,created_date
[NEW_ID],"[Your angle]","[Description]",[MATCHED_ID],[today]
```

**Display:**
```
✅ Идея добавлена как новый угол!

Теперь можно:
[R] RESEARCH — Исследуй эту идею
[A] ADD MORE — Добавь ещё идею
[M] Back to MENU — Другие операции
```

**[R] - Research:**
Load, read entire file, then execute `./c-02a-load-ideas.md`

**[A] - Add More:**
Return to step c-01 (request new idea)

**[M] - Back to Menu:**
Load `./c-00-menu.md`

---

#### OPTION [3] - COMPLETELY DIFFERENT

```
Понял, это совсем другая идея.

Просмотри найденные идеи еще раз?

⚠️  Проверка показала >60% совпадение ключевых слов.
    Но может быть это совпадение только в словах?

Сравни:

Твоя идея: "[Your idea]"
Похожая: "[Found idea]"

Реально ли это разные идеи? [Y/N]
```

**[Y] - Confirm Different:**
```
ОК, добавляю как новую идею.

✅ Идея добавлена несмотря на сходство слов
   (ты подтвердил что идеи разные)

Теперь:
[R] RESEARCH — Исследуй эту идею
[A] ADD MORE — Добавь ещё идею
[M] Back to MENU — Другие операции
```

**Save idea with:**
- `status: "active"` (to ideas_inbox.csv)
- `duplicate_check: "passed - user_override"`
- `dedup_score: "[similarity]%"`
- `dedup_date: [today]`
- `dedup_note: "User confirmed different despite word overlap"`

**[N] - Go Back to Review:**
Return to option selection (show matches again)

---

## DATA OPERATIONS

### Input Data
- User's new idea text (from step c-01)
- ideas_inbox.csv (existing raw ideas)
- ideas_research.csv (researched ideas)

### Output Data

**On completion, update:**

1. **ideas_inbox.csv** - Add new idea with dedup metadata:
```csv
id,date_added,source,raw_idea,category,status,duplicate_check,dedup_score,dedup_date,related_idea_id,notes
[NEW],today,user_input,"[idea]",[cat],active/rejected,passed/rejected,[score]%,[today],[ID if exists],"[notes]"
```

2. **angles_library.csv** (if new_angle selected):
```csv
idea_id,angle_name,perspective,related_idea,created_date,status
[NEW_ID],"[Angle name]","[Description]",[MATCHED_ID],[today],active
```

3. **Deduplication log** (optional, for analytics):
```csv
check_date,new_idea,matched_ideas,highest_score,user_decision
[today],"[idea]","[#N, #M, ...]",[score]%,[decision]
```

---

## ALGORITHM: Word Overlap Calculation

```
Pseudocode:

1. NORMALIZE(new_idea_text):
   - lowercase
   - remove stopwords
   - extract keywords
   - Result: keyword_set_new

2. FOR EACH existing_idea IN [inbox + research]:
   - NORMALIZE(existing_idea_text)
   - Result: keyword_set_existing

   - overlap = COUNT(keyword_set_new ∩ keyword_set_existing)
   - total = COUNT(keyword_set_new ∪ keyword_set_existing)
   - word_overlap_pct = (overlap / total) × 100

   - category_match = 1 if same_category else 0.5

   - SCORE = (word_overlap_pct × 0.7) + (category_match × 100 × 0.3)

   IF SCORE >= 60:
     Add to potential_matches with SCORE

3. SORT potential_matches by SCORE DESC

4. DISPLAY top 2-3 matches to user
```

---

## ERROR HANDLING

**No data files found:**
```
⚠️  Ошибка: не найдены файлы идей

Возможные причины:
• Файлы ideas_inbox.csv / ideas_research.csv отсутствуют
• Путь к файлам не правильный

Действие:
→ Инициализируем файлы
→ Идея добавляется как первая
```

**Corrupted CSV:**
```
⚠️  Ошибка: некорректные данные в файлах идей

Действие:
→ Используется резервная копия
→ Идея добавляется безопасно
→ Рекомендуется проверить файлы
```

**User timeout (no response 2+ minutes):**
```
⏱️  Истекло время на выбор

Сохраняю твою идею для проверки позже.
Можешь вернуться к ней через меню.

[M] Back to MENU — Другие операции
```

---

## VALIDATION RULES

| Check | Condition | Result |
|-------|-----------|--------|
| Similar ideas found | Score 60-100% | Present options |
| No similar ideas | Score < 60% | Accept as new |
| Perfect duplicate | Score 95%+ | Strongly recommend reject |
| Related content | Score 70-85% + user says "angle" | Accept with link |
| User override | User confirms different | Accept anyway |

---

## HINTS & TIPS

**For Claude/Agent executing this step:**

1. **Keyword Extraction:** Focus on nouns and action verbs, ignore articles and prepositions
2. **Category Matching:** Check against known categories (automation, market, tech, methodology, growth, etc.)
3. **Semantic Understanding:** If keywords are same but meaning different, respect user's judgment (option 3)
4. **Related Ideas:** Create links in data for future cross-referencing (e.g., "5 ways to discuss ИИ контент")

**For User:**

- If unsure about "duplicate vs angle", think: "Can I write a completely different post about this?"
  - YES → It's a different angle (option 2)
  - NO → It's a duplicate (option 1)

---

## NEXT STEPS

Based on user choice:

- **[1] DUPLICATE** → c-02c (research matched idea) OR c-00 (menu)
- **[2] NEW ANGLE** → c-02a (research this idea) OR c-01 (add more)
- **[3] DIFFERENT** → c-02a (research this idea) OR c-01 (add more)
- **[Y] ALL PATHS BACK** → c-00-menu.md

---

## TECHNICAL NOTES

**Dependencies:**
- Python/Node.js CSV library for parsing ideas_inbox.csv
- Stopwords list (Russian language)
- Text similarity algorithm (Jaccard index for keywords)

**Files to read/modify:**
- `content_generation_system/ideas_inbox.csv` - READ + APPEND
- `content_generation_system/ideas_research.csv` - READ (search)
- `content_generation_system/angles_library.csv` - APPEND (if new angle)

**Optional tracking:**
- Create `_logs/dedup-checks.csv` for analytics
- Track: date, idea text, matches found, user decision, result
