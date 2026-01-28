---
description: Generate 3-4 alternative versions of each post using different angles (educational/emotional/social-proof/curiosity)
name: step-yolo-05-variants
nextStepFile: ./step-yolo-06-summary.md
type: variant-generation
---

# YOLO Step 5: Variant Generation

## STEP GOAL:

Generate 3-4 alternative versions per post using different psychological angles, giving user choice of best-performing variant.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Variant Generation Start

```
═══════════════════════════════════════════════════════════════

  ✨ GENERATING VARIANTS (3-4 per post)

  Создаю варианты каждого поста с разными углами...

═══════════════════════════════════════════════════════════════
```

### 2. Generate Variants by Angle

**For each post, create 3-4 versions:**

```
POST #1: "3 часа вместо недели: как ИИ подтягивает контент"

VARIANT 1A - EDUCATIONAL (Best: +15% CTR)
────────────────────────────────────────
"Пошагово: как настроить ИИ для контента (за 15 мин)"
[Technical, detailed, teaches a skill]
CTR Potential: 4.2%

VARIANT 1B - EMOTIONAL (Best for: conversion)
────────────────────────────────────────
"Устал писать посты 8 часов в день? ИИ спасает"
[Emotional pain point, relatable]
Engagement: 4.8/5 stars

VARIANT 1C - SOCIAL PROOF (Best for: credibility)
────────────────────────────────────────
"5 успешных фаундеров уже используют этот способ"
[Social proof, results-oriented]
CTR Potential: 3.9%

VARIANT 1D - CURIOSITY (Best for: click-through)
────────────────────────────────────────
"Вот чего ты не знаешь про ИИ и контент..."
[Mystery hook, pattern interrupt]
CTR Potential: 4.6%
```

### 3. Aggregate All Variants

```json
{
  "post_id": "post_001",
  "original_score": 92,
  "variants": [
    {
      "variant_id": "v1a",
      "angle": "educational",
      "content": "Пошагово: как настроить...",
      "ctr_potential": 4.2,
      "engagement_score": 4.1,
      "recommendation": "Best for: engagement & sharing"
    },
    {
      "variant_id": "v1b",
      "angle": "emotional",
      "content": "Устал писать посты...",
      "ctr_potential": 4.1,
      "engagement_score": 4.8,
      "recommendation": "Best for: conversions"
    },
    ...
  ]
}
```

### 4. Display Variants Summary

```
═══════════════════════════════════════════════════════════════

  ✨ VARIANT GENERATION COMPLETE:

  📊 Generated: 36 total variants (9 posts × 4 angles)
  🎯 Recommendations: Auto-selected best variant per post
  📈 CTR boost predicted: +10-25% with optimal angles

═══════════════════════════════════════════════════════════════

Готовим итоговый отчёт...
```

---

## NEXT STEP

Load, read entire file, then execute `./step-yolo-06-summary.md`
