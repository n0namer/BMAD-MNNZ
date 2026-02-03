## Subprocess Optimization Opportunities

**Total Opportunities:** 4 | **High Priority:** 1 | **Estimated Context Savings:** ~1000+ lines

### High-Priority Opportunities

**steps-c/step-04-scoring.md & step-05-integration.md** — Pattern 3 (data ops)
- **Current:** Data‑файлы шардированы, но нет явного subprocess‑поиска релевантных частей.
- **Suggested:** Подгружать только нужные part‑файлы через subprocess и возвращать краткие выдержки.
- **Impact:** Стабильное снижение контекста и ускорение.

### Moderate/Low-Priority Opportunities
- steps-v/*.md — Pattern 1: быстрый grep/summary по metricsFile/portfolioFile.
- steps-e/*.md — Pattern 2: анализ project‑файла в subprocess и возврат summary.
- step-01 — Pattern 4: параллельное сохранение в Markdown и Claude Flow.

### Summary by Pattern
- **Pattern 1 (grep/regex):** 1
- **Pattern 2 (per-file):** 1
- **Pattern 3 (data ops):** 1
- **Pattern 4 (parallel):** 1

### Implementation Recommendations
**Quick Wins:** добавить subprocess‑поиск релевантных part‑файлов в scoring/integration.
**Future:** стандартизировать pattern‑usage в review/edit шагах.

**Status:** ⚠️ Review recommended

**Subprocess optimization analysis complete.** Identified 4 opportunities with potential context savings. Proceeding to Cohesive Review...
