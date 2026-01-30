---
description: Choose merge strategy and structure
name: step-c-06b-merge-strategy
nextStepFile: ./c-06c-generate.md
type: decision
---

# CREATE C-06: Merge Posts - Define Merge Strategy

## STEP GOAL:

User chooses how to combine selected posts (structure, order, format).

## EXECUTION RULES

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**

---

## EXECUTION:

### 1. Load Selected Posts

Load content of 2+ selected posts from previous step.
Show preview of each post's structure.

### 2. Display Merge Strategies

Load merge strategies from: `../../data/comparison-matrices/merge-strategies-matrix.md`

Display selected posts summary:
```
Selected posts ({count}):
  [1] "{post_1_title}" ({post_1_size})
  [2] "{post_2_title}" ({post_2_size})
  [N] "{post_n_title}" ({post_n_size})
```

Present merge strategy options with menu:
```
═══════════════════════════════════════════════════════════════

  🔗 MERGE STRATEGY: Choose How to Combine

─────────────────────────────────────────────────────────────

[1] LINEAR CONCATENATION
[2] THEMATIC CLUSTERING
[3] COMPARATIVE ANALYSIS
[4] HIERARCHICAL
[5] CUSTOM STRUCTURE

[?] PREVIEW — Show how each strategy would look
[M] Back to MENU — Вернуться в меню

═════════════════════════════════════════════════════════════════
```

User selects strategy (1-5) or ? or M.

### 3. Handle Strategy Selection

#### IF [1] LINEAR CONCATENATION:

```
Выбрана стратегия: Linear Concatenation

Порядок постов в слиянии:
  [1st] "{post_1_title}"
  [2nd] "{post_2_title}"
  [3rd] "{post_3_title}"

ПЕРЕУПОРЯДОЧИТЬ ПОСТЫ?

Current order: {current_order}
New order (type): _____________________

Рекомендуемый порядок:
  • По хронологии: oldest to newest
  • По популярности: most to least popular
  • По темам: general to specific

[C] CONFIRM & CONTINUE
[B] BACK — Select another strategy
```

If [C]: Load and execute `./step-c-06c-generate.md`

#### IF [2] THEMATIC CLUSTERING:

```
Выбрана стратегия: Thematic Clustering

System automatically reorganizes posts by detected themes:

Detected Themes:
─────────────────────────────────────────────────────────────

Theme 1: "{theme_title}" ({percent}% of content)
  └─ From: {post_list}

Theme 2: "{theme_title}" ({percent}% of content)
  └─ From: {post_list}

Theme 3: "{theme_title}" ({percent}% of content)
  └─ From: {post_list}

─────────────────────────────────────────────────────────────

REORGANIZE THEMES?

[E] EDIT THEMES — Отредактировать категории
[R] REANALYZE — Пересчитать автоматически
[C] CONFIRM & CONTINUE — Подтвердить
```

If [C]: Load and execute `./step-c-06c-generate.md`

#### IF [3] COMPARATIVE ANALYSIS:

```
Выбрана стратегия: Comparative Analysis

Methods detected in content:

Post 1: "{title}"
  Method: {detected_method}
  Key points: {key_points}

Post 2: "{title}"
  Method: {detected_method}
  Key points: {key_points}

Post N: "{title}"
  Method: {detected_method}
  Key points: {key_points}

─────────────────────────────────────────────────────────────

Will create comparison table:
  Columns: {column_list}
  Rows: {method_list}

[E] EDIT COMPARISON CRITERIA
[C] CONFIRM & CONTINUE
```

If [C]: Load and execute `./step-c-06c-generate.md`

#### IF [4] HIERARCHICAL:

```
Выбрана стратегия: Hierarchical Structure

Main Post (Core Content):
─────────────────────────────────────────────────────────────

POST 1: "{title}"
  Reason: {reason_why_main}
  Role: Main topic, primary content

Supporting Posts (Deep Dives):
─────────────────────────────────────────────────────────────

POST 2: "{title}"
  Role: {supporting_role}

POST N: "{title}"
  Role: {supporting_role}

─────────────────────────────────────────────────────────────

CHANGE MAIN POST?

[1] Use Post 1 (current)
[2] Use Post 2 instead
[N] Use Post N instead

[C] CONFIRM & CONTINUE
```

If [C]: Load and execute `./step-c-06c-generate.md`

#### IF [5] CUSTOM STRUCTURE:

```
═══════════════════════════════════════════════════════════════

  DEFINE CUSTOM MERGE STRUCTURE

─────────────────────────────────────────────────────────────

Create your own organization:

OUTLINE EDITOR:

# [MERGED TITLE]

## Introduction

## Section 1: [Your heading]
Content from: [Post 1/2/N] _______

## Section 2: [Your heading]
Content from: [Post 1/2/N] _______

## Conclusion

─────────────────────────────────────────────────────────────

AVAILABLE CONTENT:
{available_posts_list}

─────────────────────────────────────────────────────────────

[S] SAVE STRUCTURE
[T] TEMPLATE — Use predefined template
[C] CONFIRM & CONTINUE
```

If [C]: Load and execute `./step-c-06c-generate.md`

#### IF [?] PREVIEW:

```
═══════════════════════════════════════════════════════════════

  STRATEGY PREVIEW

SELECTED STRATEGY: {strategy_name}

RESULTING STRUCTURE:

# {merged_title}

## Introduction
{intro_preview}

## Section 1: {post_title}
{content_preview_200chars}

## Section 2: {post_title}
{content_preview_200chars}

## Conclusion
{conclusion_preview}

─────────────────────────────────────────────────────────────

METRICS:
  • Total length: {word_count}K words
  • Estimated read time: {read_time} minutes
  • Quality score: {quality}/5

─────────────────────────────────────────────────────────────

[<] Back to Strategy Selection
[C] CONFIRM & USE THIS
```

#### IF [M] Back to MENU:

Load `./c-00-menu.md`

---

## NEXT STEP

When strategy selected and confirmed: Load and execute `./step-c-06c-generate.md`

---

## EXECUTION RULE

ALWAYS halt and wait for user input after presenting menu.
ONLY proceed when user makes explicit selection (1-5, ?, M, or confirmation option).
