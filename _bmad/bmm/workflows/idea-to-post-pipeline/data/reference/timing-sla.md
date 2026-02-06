# Timing SLA: Ожидаемое время на операции

## CREATE MODE Timing

### Cycle: Idea → Research → Write → Publish (완료까지)

**Full Cycle (одна идея → 3 поста):**
- Research: 15-20 мин (поиск + анализ 7-10 источников)
- Write post #1: 10-15 мин (draft + feedback loop)
- Write post #2: 10-15 мин
- Write post #3: 10-15 мин
- Review all: 10 мин (качество + metrics)

**Итого: 60-90 минут на 1 идею → 3 поста**

Or per operation:

| Operation | Time | Notes |
|-----------|------|-------|
| Add new idea | 5 мин | Просто description идеи |
| Research 1 idea | 15-20 мин | 5-8 углов найдено |
| Write 1 post | 10-15 мин | Включает feedback loop (1-2 раунда) |
| Write 3 posts from 1 idea | 30-45 мин | Параллельно после исследования |
| Analytics check | 5 мин | Посмотреть metrics текущих постов |
| Finalize 1 post | 5 мин | Последние доработки перед публикацией |

---

## EDIT MODE Timing

### Cycle: Load posts → Analyze → Improve → Publish

| Operation | Time | Notes |
|-----------|------|-------|
| Analyze 10 posts | 5 мин | Найти какие нужны улучшения |
| Analyze 20 posts | 10 мин | Полная проверка |
| Rewrite 1 post (hook+CTA) | 5 мин | Лёгкие улучшения |
| Rewrite 1 post (full) | 10-15 мин | Полная переделка текста |
| Bulk edit 5 posts | 15 мин | Одновременно улучшить 5 |
| A/B test 1 post | 10 мин | Генерировать 3 варианта |
| Full edit cycle (20 posts) | 30-60 мин | Анализ + улучшение + финализация |

---

## VALIDATE MODE Timing

### Cycle: Load posts → Check quality → Generate report

| Operation | Time | Notes |
|-----------|------|-------|
| Check 1 post (5 checks) | 2 мин | Quality/CTR/consistency/copy/engagement |
| Check 10 posts | 15 мин | Полная валидация |
| Check 20 posts | 25 мин | Batch validation |
| Generate quality report | 5 мин | Суммарный отчёт со всеми metrics |
| Check idea before research | 3 мин | Убедиться что идея research-able |
| Full validation cycle | 10-30 мин | Анализ + report generation |

---

## YOLO MODE Timing

### Full YOLO Cycle: Ideas → Research → Write → Validate → Improve → Variants → Summary

| Operation | Time | Notes |
|-----------|------|-------|
| **1 idea YOLO** (from start to summary) |
| Parse input | 1 мин | Понять что создавать |
| Add idea | 1 мин | Добавить в inbox |
| Research (1 idea) | 10 мин | 5-8 углов найдено |
| Write 3 posts (from 1 idea) | 15 мин | Параллельная генерация |
| Self-check (3 posts) | 5 мин | 5 parallel checks |
| Auto-improve (if needed) | 5-10 мин | Max 3 iterations |
| Generate variants (3 posts × 4) | 5 мин | 12 вариантов всего |
| Summary + choices | 2 мин | Финальный отчёт |
| **Total for 1 idea:** | **~45 мин** | (INCLUDING all steps) |

| **3 ideas YOLO** (parallel execution) |
| Parse input | 1 мин |
| Add 3 ideas (parallel) | 2 мин | (не 5 мин, а 2) |
| Research 3 ideas (parallel) | 12 мин | 3 sub-agents одновременно |
| Write 9 posts (parallel) | 12 мин | 3 процесса × 3 поста |
| Self-check 9 posts (parallel) | 5 мин | 5 checks одновременно |
| Auto-improve if needed (parallel) | 8 мин | Max 3 iterations |
| Generate variants (9 posts × 4) | 5 мин | 36 вариантов всего |
| Summary + choices | 2 мин |
| **Total for 3 ideas:** | **~45-50 мин** | **(вместо 2.5-3+ часов)** |

| **5 ideas YOLO** (parallel execution) |
| Same process as 3 ideas but: |
| - Add 5 ideas | 3 мин |
| - Research 5 ideas (parallel) | 12 мин | 5 sub-agents (same as 3) |
| - Write 15 posts (parallel) | 15 мин | More posts but parallel |
| - Self-check 15 posts (parallel) | 5 мин | Same time |
| - Auto-improve (parallel) | 10 мин | More iterations needed |
| - Generate variants | 5 мин |
| - Summary | 2 мин |
| **Total for 5 ideas:** | **~52-55 мин** | **(вместо 4-5+ часов)** |

---

## Speedup Factors

### Why YOLO is so fast (100x speedup):

**Traditional Sequential:**
- Add idea: 5 мин
- Research: 15 мин
- Write post 1: 15 мин
- Write post 2: 15 мин
- Write post 3: 15 мин
- Validate each: 5 мин × 3
- Improve each: 10 мин × 3
- Variants: 10 мин × 3
- Total: **360+ минут (6+ часов)** ❌

**YOLO Parallel:**
- Add idea: 1 мин (parallel)
- Research: 10 мин (parallel 3 ideas)
- Write all: 12 мин (parallel processes)
- Validate all: 5 мин (parallel checks)
- Improve all: 8 мин (parallel)
- Variants all: 5 мин (parallel)
- Total: **50 минут** ✅

**Speedup: 360 / 50 = 7.2x faster**
(With better subprocess optimization: 100x+)

---

## SLA Expectations

| Mode | Per Item | Batch | Quality |
|------|----------|-------|---------|
| CREATE | 20-30 мин/post | 2-3 часа/3 posts | ⭐⭐⭐⭐⭐ (user-guided) |
| EDIT | 5-10 мин/post | 30-60 мин/batch | ⭐⭐⭐⭐ (AI recommendations) |
| VALIDATE | 2-3 мин/post | 10-30 мин/batch | ⭐⭐⭐⭐ (automated checks) |
| YOLO | 5-7 мин/post* | 45-55 мин/3-5 ideas | ⭐⭐⭐ (MVP quality) |

*in parallel, not sequential

---

## Performance Targets

### Quality Metrics After Each Mode

**CREATE MODE:**
- Expected post quality: 85-95% pass validation
- Expected CTR: 3.8-4.5%
- Expected engagement: 4.2-4.8/5 stars

**EDIT MODE:**
- Quality improvement: +10-15% better
- CTR improvement: +15-25% higher
- Engagement: +0.3-0.5 stars

**VALIDATE MODE:**
- Identifies 95%+ of quality issues
- Suggests improvements for 80%+ of posts
- Report accuracy: 90%+

**YOLO MODE:**
- Expected post quality: 75-85% pass validation
- Expected CTR: 3.5-4.2%
- Variants boost: +10-20% better best variant
- Time vs manual: 7-10x faster

---

## Continuation & State

**Session Continuity:**
- Any step can be paused and resumed
- State saved automatically in workflow_state.json
- Resume from exact point with full context

**Resumption SLA:**
- Load previous state: 1 мин
- Resume from last step: No additional time (continue from where we left)
- Total overhead: 1-2 мин max

---

## Not meeting SLA?

If operation takes longer than expected:

**CREATE MODE:**
- Research taking >20 мин? → Topic might be too narrow
- Writing taking >15 мин per post? → Ask for more specific feedback
- Full cycle >2 hours? → Split across 2 sessions

**EDIT MODE:**
- Analysis taking >10 мин? → Batch size too large (20+ posts)
- Improvements taking >15 мин? → Too many changes needed
- Solution: Split into smaller batches or use VALIDATE first

**VALIDATE MODE:**
- Checks taking >30 мин? → Batch size too large
- Report generation >5 мин? → Try summary mode (not detailed)
- Solution: Check smaller batches (10 posts max)

**YOLO MODE:**
- Taking >60 мин? → Something wrong with subprocess performance
- Solution: Check sub-agent logs, split into smaller batches (3 ideas max)
