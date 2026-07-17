# Consolidated Output Specification

**Workflow:** idea-to-post-pipeline
**Version:** 1.0
**Date:** 2026-01-28
**Purpose:** Single reference document for all output formats and specifications

---

## 1. POST FILE FORMAT

### File Naming Convention
```
/posts/YYYY-MM-DD_idea-{id}_angle-{angle_id}_v{version}.md
```

**Examples:**
- `2026-01-27_idea-1_angle-3_v1.md`
- `2026-01-28_idea-2_angle-1_v2.md` (version 2 after edit)

### File Structure: YAML Frontmatter + Markdown Content

```markdown
---
id: post_001
date: 2026-01-27
idea_id: 1
angle: angle_3
topic: automation
target_persona: agency_owner
platform: telegram
views: 550
ctr: 5.82%
comments: 12
reposts: 4
status: published
version: 1
---

# 🚀 ИИ заменит твоего помощника

[Full post content with emoji + formatting]
```

### YAML Frontmatter Fields

| Field | Type | Format | Required | Notes |
|-------|------|--------|----------|-------|
| id | string | post_NNN | Yes | Unique post identifier |
| date | string | YYYY-MM-DD | Yes | Creation date |
| idea_id | integer | 1-9999 | Yes | Reference to original idea |
| angle | string | angle_X | Yes | Angle variant used |
| topic | string | category | Yes | Content category (e.g., automation, pricing, psychology) |
| target_persona | string | enum | Yes | Audience (founder, marketer, agency_owner) |
| platform | string | enum | Yes | Distribution platform (telegram, instagram, linkedin) |
| views | integer | 0-999999 | Optional | Performance metric (after publishing) |
| ctr | float | 0-10% | Optional | Click-through rate (after publishing) |
| comments | integer | 0-999999 | Optional | Engagement count (after publishing) |
| reposts | integer | 0-999999 | Optional | Share count (after publishing) |
| status | string | enum | Yes | draft, published, archived, needs_review |
| version | integer | 1-999 | Yes | Version number (increments on edit) |

### Content Structure

All posts must follow this structure:

```
[Hook] - Attention-grabbing first line (10-15 words)
[Problem] - Describe the pain point (2-3 sentences)
[Solution] - Present the solution (2-3 sentences)
[Trigger] - Social proof or emotional trigger (1-2 sentences)
[CTA] - Call-to-action (1 line)
```

### Content Variants

Three versions required per post:
- **500-character version:** Full detail with emoji and formatting
- **250-character version:** Condensed with key points
- **100-character version:** Ultra-short with just hook + CTA

**Character counting:** Includes spaces and emoji

### Example Post

```markdown
---
id: post_001
date: 2026-01-27
idea_id: 1
angle: angle_1
topic: automation
target_persona: agency_owner
platform: telegram
views: 550
ctr: 5.82%
comments: 12
reposts: 4
status: published
version: 1
---

# 🚀 3 часа вместо недели: как ИИ подтягивает контент

Писать контент вручную — это 8 часов в день и ноль роста.
Я покажу как ИИ сжимает цикл в 3 часа.

Вот чем отличается процесс:
• Исследование: 30 мин (вместо 2 часов)
• Написание: 1 час (вместо 4 часов)
• Редактирование: 90 мин (вместо 2 часов)

Результат: посты, которые конвертят 4-5% и работают из коробки.

👉 Хочешь попробовать? Я помогу настроить твой workflow.
```

---

## 2. CSV FILE SPECIFICATIONS

### 2.1 ideas_inbox.csv

**Purpose:** Capture new ideas for research

**Columns:**

| Column | Type | Format | Required | Constraints | Example |
|--------|------|--------|----------|-------------|---------|
| id | integer | 1-9999 | Yes | Auto-increment | 1 |
| date_added | string | YYYY-MM-DD | Yes | Current date | 2026-01-27 |
| source | string | enum | Yes | brainstorm, conversation, research, internal, inspiration | brainstorm |
| raw_idea | string | text | Yes | Max 500 chars | ИИ контент за 3 часа |
| category | string | enum | Yes | automation, tech, market, methodology, psychology, other | automation |
| status | string | enum | Yes | active, pending, archived | active |
| notes | string | text | Optional | Max 1000 chars | Интересная идея про ускорение контента |

**Sample Data:**

```csv
id,date_added,source,raw_idea,category,status,notes
1,2026-01-27,brainstorm,ИИ контент за 3 часа,automation,active,Интересная идея про ускорение контента
2,2026-01-27,conversation,Speech-to-text для постов,tech,active,Подсказал пользователь на встрече
3,2026-01-27,research,Масштабирование личного бренда,market,pending,Найдено в статье Medium
4,2026-01-26,internal,A/B тестирование hooks,methodology,active,Собственное наблюдение из аналитики
5,2026-01-25,inspiration,Психология urgency в CTR,psychology,archived,Хорошая идея но неактуальна сейчас
```

---

### 2.2 ideas_research.csv

**Purpose:** Store researched ideas with angle variants

**Columns:**

| Column | Type | Format | Required | Constraints | Example |
|--------|------|--------|----------|-------------|---------|
| id | integer | 1-9999 | Yes | Auto-increment | 1 |
| original_idea_id | integer | 1-9999 | Yes | FK to ideas_inbox | 1 |
| research_date | string | YYYY-MM-DD | Yes | Date researched | 2026-01-27 |
| main_angle | string | text | Yes | Primary angle (max 100 chars) | ИИ экономит время |
| sub_angles_count | integer | 1-20 | Yes | Number of variants | 8 |
| best_angle_id | string | angle_X | Yes | Highest-scoring variant | angle_1 |
| angles_list | string | text | Yes | Pipe-separated list | Экономия времени\|Масштабирование\|Качество\|... |
| sources_count | integer | 1-20 | Yes | Number of research sources | 7 |
| avg_relevance | integer | 0-100 | Yes | Average relevance score | 84 |

**Sample Data:**

```csv
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance
1,1,2026-01-27,ИИ экономит время,8,angle_1,Экономия времени|Масштабирование|Качество|Стоимость|Обучение|Интеграция|ROI|Психология,7,84
2,2,2026-01-27,Speech-to-text workflow,7,angle_2,Скорость записи|Точность|Отсутствие ошибок|Интеграция с ИИ|Мобильность|Удобство|Экономия труда,6,79
3,3,2026-01-27,Масштабирование личного бренда,9,angle_3,Контентная стратегия|Аудитория|Монетизация|Системы|Делегирование|Партнёрства|Экспертность|Социальная сеть|Продажи,8,82
```

---

### 2.3 posts_content.csv

**Purpose:** Index of all created posts with quality metrics

**Columns:**

| Column | Type | Format | Required | Constraints | Notes |
|--------|------|--------|----------|-------------|-------|
| id | string | post_NNN | Yes | Unique | Auto-generated |
| research_id | integer | 1-9999 | Yes | FK to ideas_research | Links to research |
| angle_used | string | angle_X | Yes | Must match research | Which angle variant |
| publish_date | string | YYYY-MM-DD | Optional | After publishing | NULL if draft |
| platform | string | enum | Yes | telegram, instagram, linkedin | Distribution platform |
| post_title_short | string | text | Yes | Max 100 chars | Brief title |
| content_500_chars | string | text | Yes | Exactly 500 chars | Full-length variant |
| content_250_chars | string | text | Yes | Exactly 250 chars | Medium variant |
| content_100_chars | string | text | Yes | Exactly 100 chars | Short variant |
| quality_score | integer | 0-100 | Yes | Calculated | After validation |
| ctr_potential | float | 0-10 | Yes | Calculated | Estimated click rate |
| engagement_score | float | 0-5 | Yes | Calculated | Engagement prediction |
| status | string | enum | Yes | draft, ready, published, needs_review, needs_rewrite | Current status |
| notes | string | text | Optional | Max 500 chars | Additional info |

**Status Values:**
- `draft` - Work in progress
- `ready` - Ready to publish
- `published` - Live on platform
- `needs_review` - Requires manual review before publish
- `needs_rewrite` - Quality too low, requires rewrite

**Sample Data:**

```csv
id,research_id,angle_used,publish_date,platform,post_title_short,content_500_chars,content_250_chars,content_100_chars,quality_score,ctr_potential,engagement_score,status,notes
post_001,1,angle_1,2026-01-28,telegram,3 часа вместо недели,"3 часа вместо недели: как ИИ подтягивает контент...","3 часа вместо недели — вот что ИИ даёт контенту","Как ИИ ускоряет контент",92,4.5,4.8,ready,Отличный пост для публикации
post_002,1,angle_2,,telegram,ИИ + качество контента,"Качество контента может быть выше при использовании ИИ...","ИИ контент часто качественнее, чем думают","ИИ и качество",86,3.8,4.2,draft,Нужна доработка CTA
post_003,2,angle_2,2026-01-29,telegram,Speech-to-text спасает время,"Speech-to-text + ИИ = идеальный дуэт для быстрого контента...","Voice to posts за 5 минут вместо часа","Speech-to-text спасает время",91,4.2,4.5,ready,Хороший пост для аудитории
```

---

### 2.4 metrics_tracking.csv

**Purpose:** Track post performance over time

**Columns:**

| Column | Type | Format | Required | Constraints | Formula/Notes |
|--------|------|--------|----------|-------------|----------------|
| post_id | string | post_NNN | Yes | FK to posts_content | Which post |
| publish_date | string | YYYY-MM-DD | Yes | Date published | When posted |
| day_number | integer | 1-999 | Yes | Days since publish | Day 1, 2, 3... |
| views | integer | 0-999999 | Yes | View count | Total views |
| clicks | integer | 0-999999 | Yes | Click count | Total clicks |
| ctr_percent | float | 0-10 | Yes | Calculated | clicks/views*100 |
| comments | integer | 0-999999 | Yes | Comment count | Direct comments |
| shares | integer | 0-999999 | Yes | Share/repost count | Reposts/shares |
| saves | integer | 0-999999 | Yes | Save count | Bookmarks/saves |
| engagement_rate | float | 0-100 | Yes | Calculated | (comments+shares+saves)/views*100 |
| sentiment | string | enum | Yes | positive, neutral, negative | Audience sentiment |
| notes | string | text | Optional | Max 500 chars | Observations |

**Sample Data:**

```csv
post_id,publish_date,day_number,views,clicks,ctr_percent,comments,shares,saves,engagement_rate,sentiment,notes
post_001,2026-01-28,1,245,11,4.5,2,1,3,2.4,positive,Отличный старт
post_001,2026-01-29,2,412,19,4.6,5,3,7,3.7,positive,Растёт интерес
post_001,2026-01-30,3,680,31,4.6,12,7,15,4.2,positive,Пост набирает обороты
post_001,2026-01-31,4,945,43,4.5,18,11,22,5.1,positive,Стабильный рост
```

---

### 2.5 angles_library.csv

**Purpose:** Reference library of angle templates for reuse

**Columns:**

| Column | Type | Format | Required | Constraints | Example |
|--------|------|--------|----------|-------------|---------|
| id | integer | 1-9999 | Yes | Auto-increment | 1 |
| original_idea_id | integer | 1-9999 | Yes | FK to ideas_inbox | 1 |
| research_date | string | YYYY-MM-DD | Yes | Date researched | 2026-01-27 |
| main_angle | string | text | Yes | Primary theme (max 100 chars) | ИИ экономит время |
| sub_angles_count | integer | 1-20 | Yes | Number of variants | 8 |
| best_angle_id | string | angle_X | Yes | Highest-performing variant | angle_1 |
| angles_list | string | text | Yes | Pipe-separated angles | Экономия\|Масштабирование\|... |
| sources_count | integer | 1-20 | Yes | Number of sources | 7 |
| avg_relevance | integer | 0-100 | Yes | Relevance score | 84 |

---

## 3. WORKFLOW STATE FILE

### workflow_state.json

**Purpose:** Track session state for multi-session continuability

**Location:** Workflow root directory (alongside workflow.md)

**Format:** JSON

**Structure:**

```json
{
  "workflow_id": "idea-to-post-pipeline",
  "session_id": "2026-01-27-v1",
  "currentMode": "CREATE",
  "currentStep": "step-c-03c-draft",
  "stepsCompleted": [
    "step-01-init",
    "step-01b-continue",
    "step-00-menu",
    "step-c-01-add-idea",
    "step-c-02a-load",
    "step-c-02b-select",
    "step-c-02c-research",
    "step-c-02d-results",
    "step-c-03a-select-idea",
    "step-c-03b-select-angle"
  ],
  "lastUpdated": "2026-01-27T21:30:00Z",
  "sessionDuration": 45,
  "context": {
    "selectedIdea": 1,
    "selectedAngle": "angle_3",
    "draftVersion": 1,
    "draftFeedback": [
      "add examples",
      "improve CTA"
    ]
  }
}
```

**Fields:**

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| workflow_id | string | Yes | Always "idea-to-post-pipeline" |
| session_id | string | Yes | Format: YYYY-MM-DD-vX (e.g., 2026-01-27-v1) |
| currentMode | string | Yes | CREATE, EDIT, VALIDATE, or YOLO |
| currentStep | string | Yes | Current step filename |
| stepsCompleted | array | Yes | List of completed step filenames |
| lastUpdated | string | Yes | ISO 8601 datetime |
| sessionDuration | integer | Yes | Minutes elapsed in session |
| context | object | Optional | Custom context per mode |

---

## 4. QUALITY METRICS REFERENCE

### Quality Score (0-100)

**Scoring Criteria:**
- Hook strength (20 points): Does it grab attention?
- Problem clarity (20 points): Is the problem clear?
- Solution relevance (20 points): Is the solution appropriate?
- CTA clarity (20 points): Is the call-to-action explicit?
- Tone consistency (20 points): Is the tone authentic and consistent?

**Quality Thresholds:**
- 85-100: EXCELLENT (ready to publish)
- 75-84: GOOD (minor improvements)
- 65-74: ACCEPTABLE (needs review)
- <65: POOR (rewrite required)

### CTR Potential (0-10%)

**Scoring Criteria:**
- Hook appeal (relevance to audience)
- Problem resonance (emotional connection)
- Solution credibility (believability)
- Trigger strength (psychological impact)
- CTA effectiveness (conversion potential)

**CTR Benchmarks:**
- 4.0%+: EXCELLENT (top 10%)
- 3.0-3.9%: GOOD (top 25%)
- 2.0-2.9%: ACCEPTABLE (average)
- <2.0%: POOR (below average)

### Engagement Score (0-5.0)

**Scoring Criteria:**
- Comment-worthiness (discussion potential)
- Share-worthiness (repost potential)
- Save-worthiness (bookmark potential)
- Emotional trigger strength
- Community resonance

**Engagement Benchmarks:**
- 4.5-5.0: EXCELLENT (highly shareable)
- 4.0-4.4: VERY GOOD (shareable)
- 3.0-3.9: GOOD (moderately shareable)
- 2.0-2.9: ACCEPTABLE (some engagement)
- <2.0: POOR (low engagement)

---

## 5. BACKUP AND RECOVERY

### Backup Locations

```
/backup/
├── posts_backup_YYYY-MM-DD.csv
├── ideas_inbox_backup_YYYY-MM-DD.csv
├── ideas_research_backup_YYYY-MM-DD.csv
├── metrics_tracking_backup_YYYY-MM-DD.csv
└── angles_library_backup_YYYY-MM-DD.csv
```

### Backup Schedule

- **Automated:** Daily at midnight
- **Manual:** After each major operation (mode completion)
- **Retention:** 30 days (automatic cleanup)

### Recovery Procedures

1. **Corrupted CSV:** Auto-repair on load, fallback to most recent backup
2. **Lost session state:** Reconstruct from stepsCompleted array
3. **Post file corruption:** Recover from posts_content.csv version
4. **Complete data loss:** Restore from /backup/ folder

---

## 6. VALIDATION CHECKLIST

When saving any output, verify:

- [x] File location follows naming convention
- [x] YAML frontmatter complete (if markdown)
- [x] CSV column count matches specification
- [x] CSV column types correct
- [x] CSV status values valid
- [x] Quality scores in valid range
- [x] CTR potential in valid range
- [x] Engagement score in valid range
- [x] Timestamps in ISO 8601 format
- [x] Version number incremented (if edit)
- [x] workflow_state.json updated

---

## 7. EXAMPLES

### Example 1: Create New Post

**Steps:**
1. Research idea → ideas_research.csv entry
2. Write post content (3 variants)
3. Validate quality (score, CTR, engagement)
4. Save to posts_content.csv
5. Create individual post markdown file
6. Update workflow_state.json

**Output Files:**
- `/posts/2026-01-28_idea-1_angle-1_v1.md`
- posts_content.csv (new row)
- workflow_state.json (updated)

### Example 2: Edit Existing Post

**Steps:**
1. Load post from posts_content.csv
2. Increment version number (v1 → v2)
3. Edit content in markdown file
4. Revalidate quality
5. Update posts_content.csv version field
6. Save new file as v2

**Output Files:**
- `/posts/2026-01-28_idea-1_angle-1_v2.md`
- posts_content.csv (version field updated)

### Example 3: Track Metrics

**Steps:**
1. Publish post to Telegram
2. Record daily metrics (views, clicks, engagement)
3. Append to metrics_tracking.csv
4. Calculate CTR and engagement rate
5. Monitor trends

**Output File:**
- metrics_tracking.csv (new rows)

---

## 8. CHARACTER LENGTH VERIFICATION

### Content Variant Specifications

**500-character version:**
- Includes spaces and emoji
- Full detail with examples
- Complete story arc (hook → problem → solution → trigger → CTA)

**250-character version:**
- Includes spaces and emoji
- Condensed key points
- Hook → solution → CTA

**100-character version:**
- Includes spaces and emoji
- Ultra-short: hook + CTA only
- Maximum impact in minimal space

**Character counting tool:**
```
Use standard UTF-8 character counting
Include: letters, numbers, spaces, emoji, punctuation
Exclude: nothing (count everything)
```

---

## 9. REFERENCE LINKS

- **Main workflow:** workflow.md
- **Template examples:** /data/csv-templates/
- **Quality checklists:** /data/checklist-templates/
- **Reference guides:** /data/reference/
- **Step files:** /steps/

---

## Document Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-28 | Initial consolidated specification |

---

**Last Updated:** 2026-01-28
**Status:** APPROVED FOR PRODUCTION
