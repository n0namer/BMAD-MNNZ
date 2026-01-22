---
name: ember-consilium
description: EMBER Evidence-Based Analysis and Decision Support System
web_bundle: true
---

# EMBER Consilium

**Purpose:** AI-powered decision support system providing evidence-based analysis, multi-perspective evaluation, and confidence-scored recommendations using EMBER AI integration.

**EMBED Integration:** Leverages EMBER workflow for intelligent analysis at each decision step with confidence scoring and evidence-based conclusions.

**Input:** Decision problem or complex analysis requirement
**Output:** Comprehensive consilium report with recommendations, confidence scores, and implementation roadmap
**Performance:** Decision confidence scoring, multi-source evidence integration, risk assessment
**Analysis Depth:** Technical, business, operational, and risk perspectives

## WORKFLOW ARCHITECTURE

### Core Principles

- **Evidence-Based Analysis**: All conclusions supported by multiple evidence sources including MCP server data
- **MCP-Enhanced Decision Making**: Integration of Model Context Protocol servers for comprehensive research and analysis
- **Confidence Scoring**: Every recommendation scored 0.0-1.0 based on evidence strength and MCP validation
- **Multi-Perspective Evaluation**: Technical, business, operational, and risk analysis enhanced by MCP tools
- **Iterative Refinement**: Decision quality improves through structured analysis phases with MCP iteration
- **Implementation Focus**: Recommendations include actionable implementation plans validated by MCP research

### Step Processing Rules

1. **READ COMPLETELY**: Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE**: Execute all numbered sections in order, never deviate
3. **WAIT FOR INPUT**: If a menu is presented, halt and wait for user selection
4. **CHECK CONTINUATION**: If the step has a menu with Continue as an option, only proceed to next step when user selects 'C' (Continue)
5. **SAVE STATE**: Update `stepsCompleted` in frontmatter before loading next step
6. **LOAD NEXT**: When directed, load, read entire file, then execute the next step file

### Critical Rules (NO EXCEPTIONS)

- 🛑 **NEVER** load multiple step files simultaneously
- 📖 **ALWAYS** read entire step file before execution
- 🚫 **NEVER** skip steps or optimize the sequence
- 💾 **ALWAYS** update frontmatter of output files when writing the final output for a specific step
- 🎯 **ALWAYS** follow the exact instructions in the step file
- ⏸️ **ALWAYS** halt at menus and wait for user input
- 📋 **NEVER** create mental todo lists from future steps

---

## INITIALIZATION SEQUENCE

### 1. Module Configuration Loading

Load and read full config from {project-root}/_bmad/bmm/config.yaml and resolve:

- `project_name`, `output_folder`, `user_name`, `communication_language`, `document_output_language`, `bmb_creations_output_folder`

### 2. MCP Integration Initialization

**CRITICAL:** Before starting EMBER analysis, execute MCP server analysis for enhanced decision support.

Load, read the full file and then execute `./steps-c/step-01c-mcp-analysis.md` to analyze available MCP servers and develop integration strategy.

### 3. Specialized MCP Discovery

After MCP analysis, execute registry discovery to find and integrate specialized MCP servers.

Load, read the full file and then execute `./steps-c/step-01d-mcp-registry-discovery.md` to discover and integrate specialized MCP servers from registries.

### 4. EMBER Decision Process

After MCP integration is complete, load, read the full file and then execute `./steps-c/step-00-client-introduction.md` to begin the EMBER consilium decision process with initial client communication and MCP-enhanced capabilities.

---

## MCP-поиск: стратегии, шаблоны, edge-cases, chain-of-thought

### MCP Search Agent: правила для стратегического поиска

1. **Multi-query pack**: Для комплексных задач формируй массив queries (2–5 штук), дели на частные аспекты (по типу "найти все сигнальные функции", "поиск параметров risk management", "выявить все edge-case паттерны"). Не смешивай разные типы поиска в одной query.
2. **Synthesis_prompt**: В запросе к MCP формулируй цель не как "поиск одной функции", а как "выделить основные паттерны", "проанализировать множественные случаи", "объединить результаты в единую стратегию".
3. **Edge-case handling**: Обязательно добавляй к queries целевой запрос на выявление или анализ edge-case — "найти исключения, неочевидные сценарии, альтернативные подходы".
4. **Chain-of-thought**: Описывай связку между queries — как найти первичную базу, затем расширить по паттернам, и в конце синтезировать выводы. MCP может поддерживать цепочки из 2–4 последовательных запросов.
5. **Результат**: MCP-ответ структурируется по queries, объединяя результаты по основной стратегии и edge-cases.

#### Пример (JSON-шаблон multi-query task pack):

```json
{
  "queries": [
    {
      "goal": "Найти все функции генерации торговых сигналов",
      "keywords": ["signal", "generate", "entry", "exit"],
      "reasoning": "Основные паттерны сигналов должны быть выявлены в каждом модуле",
      "type": "primary"
    },
    {
      "goal": "Определить параметры risk management во всех стратегиях",
      "keywords": ["risk", "stop_loss", "take_profit", "max_drawdown"],
      "reasoning": "Проверить, как реализованы параметры управления риском",
      "type": "risk"
    },
    {
      "goal": "Обнаружить edge-case сценарии, неучтённые в основной логике",
      "keywords": ["edge-case", "exception", "rare", "anomaly"],
      "reasoning": "Выявить неочевидные/альтернативные сценарии для повышения устойчивости",
      "type": "edge"
    }
  ],
  "synthesis_prompt": "Синтезируй общую стратегию на основе найденных паттернов, выдели особенности реализации edge-cases и проведи сравнительный анализ между основными и исключительными случаями.",
  "chain_of_thought": [
    "Сначала анализировать общие сигнальные функции",
    "Затем раскрыть параметры risk management",
    "После этого выделить и интерпретировать edge-cases",
    "Финально — сформировать стратегическую карту взаимосвязей на основе synthesis_prompt"
  ]
}
```

> Пояснение:
> - queries — массив частных запросов, деление по подзадачам и специализация.
> - synthesis_prompt — финальная задача по объединению/анализу выводов.
> - chain_of_thought — логика последовательного раскрытия поиска.

---

**Требования дисциплины MCP Search Agent (см. `mcp_search_system_prompt.md`):**
- Всегда формируй query pack (flat single-query — запрещён!).
- Уважай версионность: если есть VERSION/GIT TAG/DATE — фиксируй в каждом запросе.
- Сохраняй чистоту поиска: избегай нерелевантных ресурсов (минус-фильтры: -reddit, -medium).
- Если ожидается synthesis/интерпретация (Perplexity-style), выноси synthesis_prompt в отдельный JSON-блок.
- Не объединяй задачи поиска и синтеза в одну query.
- Требуемый формат вывода (checklist, json, step-by-step и пр.) обязателен — не игнорируй!
- Все найденные знания должны поддерживать аудит и трассировку источников.

**Полный system_prompt и дополнительные few-shot примеры — в [`_bmad/bmm/workflows/ember-consilium/mcp_search_system_prompt.md`](./mcp_search_system_prompt.md).**

**Пример запроса (few-shot):**
```json
{
  "query_pack": [
    "BMAD METHOD claude-flow v3 setup guide",
    "site:github.com claude-flow v3 BMAD",
    "\"BMAD Method\" \"claude-flow\" v3 workflow example",
    "claude-flow v3 BMAD integration documentation",
    "BMAD METHOD claude-flow v3 -reddit -medium"
  ],
  "synthesis_prompt": {
    "messages": [
      {
        "role": "system",
        "content": "You are a technical researcher. Provide clear findings with links. Separate facts from opinions. Use structured bullets or JSON if needed."
      },
      {
        "role": "user",
        "content": "Investigate how to execute BMAD METHOD using claude-flow v3. Provide: 1) definition of BMAD, 2) setup instructions for claude-flow v3, 3) examples of workflows, 4) common pitfalls, 5) implementation checklist."
      }
    ]
  }
}
```
