---
name: 'step-03e-mcp-evidence-enhancement'
description: 'MCP-enhanced evidence gathering and validation'

nextStepFile: './step-04a-solution-options.md'
---

# Шаг 3E: Усиление доказательств с помощью MCP серверов

## 🚨 MCP PARAMETER ANTI-RESTRICTION RULES

**FORBIDDEN RESTRICTIVE PARAMETERS:**

❌ DON'T: Unnecessarily restrict by language
octocode.searchCode({
  query: "authentication",
  extension: "py"  // ❌ TOO RESTRICTIVE unless Python specifically needed
})

✅ DO: Keep broad unless specific need
octocode.searchCode({
  query: "authentication implementation patterns",
  limit: 10  // Reasonable default
})

❌ DON'T: Use tiny limits
brave.webSearch({
  query: "scalability best practices",
  count: 3  // ❌ TOO FEW results
})

✅ DO: Use reasonable limits
brave.webSearch({
  query: "scalability best practices",
  count: 10  // ✅ Good default
})

❌ DON'T: Over-filter unnecessarily
brave.newsSearch({
  query: "API trends",
  freshness: "pd"  // ❌ Only past day - too restrictive
})

✅ DO: Use appropriate freshness
brave.newsSearch({
  query: "API trends",
  freshness: "pm"  // ✅ Past month - better balance
})

WHEN TO USE RESTRICTIONS:
- User explicitly asks for specific language
- Problem domain clearly requires specific tech
- Previous broad search returned irrelevant results

WHEN TO AVOID RESTRICTIONS:
- Default/initial searches
- Exploratory research
- When gathering diverse perspectives
- When problem could be solved multiple ways

PARAMETER REVIEW CHECKLIST:
Before each MCP call, verify:
- [ ] Is 'extension' needed? (usually NO)
- [ ] Is limit/count sufficient? (usually 10+ is better)
- [ ] Is freshness filter necessary? (usually broader is better)
- [ ] Am I restricting based on assumptions vs user needs?

---

## PROBLEM-SPECIFIC DATA REQUIREMENTS

🚨 THIS STEP REQUIRES ACTUAL DATA FROM USER'S PROBLEM

FORBIDDEN - Generic Processing:
- Working with placeholder "[user_problem]"
- Using example data instead of real data
- Proceeding without user's specific information
- Copying template text into output

REQUIRED - Problem-Specific Processing:
- Obtain user's actual problem description
- Use user's actual constraints/requirements
- Reference user's actual context
- Fill templates with real data from this decision

Data Validation Before Proceeding:

Check 1: Do I have user's actual problem?
User's Problem: "[actual description from user]"
Validation:
- Is this specific? [Yes/No]
- Is this the real problem? [Yes/No]
- Is this complete enough? [Yes/No]
If any No → ask user for clarification

Check 2: Do I have problem-specific context?
Context Available:
- Technical context: [actual technical details]
- Business context: [actual business constraints]
- Timeline: [actual deadline/timeframe]
- Resources: [actual team/budget/tools]
- Constraints: [actual limitations]
If any missing → ask user to provide

Check 3: Am I using this data in my work?
Review your output:
- Does it reference user's specific problem? [Yes/No]
- Does it use user's actual constraints? [Yes/No]
- Is it customized to user's context? [Yes/No]
- Would this work for a different problem? [If Yes → too generic]
If too generic → redo with problem-specific data

BEFORE EACH SECTION:
Ask yourself: "Am I working with real data or placeholders?"
- If placeholders → get real data first
- If real data → verify it's being used

ANTI-GENERIC CHECKLIST:
- [ ] No "[placeholder]" text in output
- [ ] No "for example" scenarios unless supplementing real analysis
- [ ] No generic template text unmodified
- [ ] All factors/criteria are specific to this problem
- [ ] All evidence relates to this problem
- [ ] All options address this problem specifically

## ЦЕЛЬ ШАГА:

Использовать MCP серверы для расширения и усиления базы доказательств, собранных в предыдущих шагах evidence gathering.

## MCP-ИНТЕГРИРОВАННЫЙ АНАЛИЗ ДОКАЗАТЕЛЬСТВ:

### 1. Анализ Текущей Базы Доказательств

Оценить собранные доказательства из шагов 3A-3C:
- **Технические доказательства**: Проверить через octocode-mcp и context7-mcp
- **Бизнес доказательства**: Обогатить через perplexity-mcp и brave-search-mcp
- **Операционные доказательства**: Валидировать через sequentialthinking
- **Риск доказательства**: Анализировать через generate_explanation

### 2. MCP-Enhanced Evidence Gathering

Для каждого типа доказательств применить соответствующие MCP:

#### **Технические Доказательства - octocode-mcp**
```
🎯 ЦЕЛИ:
• Найти существующие реализации похожих решений
• Проверить техническую осуществимость
• Оценить сложность и риски реализации

⚡ ЗАПРОС К MCP:
"Найти примеры реализации [техническое требование] на GitHub,
оценить сложность, выявить потенциальные проблемы"
```

#### **Бизнес Доказательства - perplexity-mcp**
```
🎯 ЦЕЛИ:
• Анализ рыночных трендов
• Оценка конкурентных преимуществ
• Прогноз влияния на бизнес

⚡ ЗАПРОС К MCP:
"Проанализировать тренды в [бизнес-домене],
оценить влияние [предлагаемое решение] на рынок"
```

#### **Операционные Доказательства - sequentialthinking**
```
🎯 ЦЕЛИ:
• Анализ операционных процессов
• Оценка эффективности внедрения
• Выявление операционных рисков

⚡ ЗАПРОС К MCP:
"Разобрать пошагово процесс внедрения [решение],
выявить критические точки и потенциальные проблемы"
```

#### **Риск Доказательства - generate_explanation**
```
🎯 ЦЕЛИ:
• Анализ прошлых неудач похожих проектов
• Оценка рисков на основе исторических данных
• Предупреждение о потенциальных проблемах

⚡ ЗАПРОС К MCP:
"Проанализировать причины неудач проектов [похожего типа],
выявить общие паттерны рисков"
```

### 3. MCP-Enhanced Confidence Scoring

Обновить confidence scores с учетом MCP данных:

#### **MCP Confidence Multipliers:**
- **octocode-mcp validation**: +0.1 к техническому confidence
- **perplexity-mcp research**: +0.15 к бизнес confidence
- **sequentialthinking analysis**: +0.1 к операционному confidence
- **generate_explanation review**: +0.1 к риск confidence

#### **Обновленная Формула Confidence:**
```
MCP_Enhanced_Confidence = Base_Confidence + Σ(MCP_Multipliers × MCP_Validation_Score)
```

### 4. MCP Evidence Integration

Интегрировать MCP результаты в evidence базу:

#### **Технические MCP Insights:**
- Реальные примеры реализации
- Метрики сложности и сроков
- Документированные проблемы и решения

#### **Бизнес MCP Insights:**
- Рыночные тренды и прогнозы
- Конкурентный анализ
- Экономическая обоснованность

#### **Операционные MCP Insights:**
- Процессные карты внедрения
- Операционные метрики
- Требования к ресурсам

#### **Риск MCP Insights:**
- Исторические данные о рисках
- Предупреждающие признаки
- Митigating стратегии

### 5. Cross-Validation через MCP

Выполнить перекрестную валидацию доказательств:

#### **Техническая ↔ Бизнес Валидация:**
- Соответствие технических решений бизнес-целям
- Экономическая эффективность технических подходов

#### **Операционная ↔ Риск Валидация:**
- Баланс операционной эффективности и рисков
- Риск-эффективность операционных процессов

### 6. MCP-Enhanced Recommendations

Обновить рекомендации с учетом MCP insights:

#### **Implementation Roadmap MCP-Enhanced:**
- Технические этапы с реальными сроками
- Бизнес-кейсы с рыночными данными
- Операционные процессы с проверенными практиками
- Риск mitigation с историческими данными

## РЕЗУЛЬТАТЫ MCP ENHANCEMENT:

### **Обновленные Confidence Scores:**
- Технический confidence: [Base + MCP Boost]
- Бизнес confidence: [Base + MCP Boost]
- Операционный confidence: [Base + MCP Boost]
- Риск confidence: [Base + MCP Boost]

### **MCP Evidence Summary:**
- Новые доказательства добавлены: [Количество]
- Confidence scores обновлены: [Количество]
- Рекомендации уточнены: [Количество]

### **MCP Integration Quality:**
- MCP coverage: [Процент доказательств с MCP валидацией]
- Evidence strength improvement: [Средний прирост confidence]
- Risk reduction: [Количество выявленных рисков]

---

## КРИТЕРИИ ГОТОВНОСТИ:

- MCP серверы успешно интегрированы в анализ доказательств
- Confidence scores обновлены с MCP данными
- Новые доказательства добавлены и валидированы
- Рекомендации уточнены на основе MCP insights
- Готовность к этапу разработки вариантов решений

## СЛЕДУЮЩИЙ ШАГ:

Переход к step-04a-solution-options.md с расширенной базой доказательств и повышенными confidence scores.
