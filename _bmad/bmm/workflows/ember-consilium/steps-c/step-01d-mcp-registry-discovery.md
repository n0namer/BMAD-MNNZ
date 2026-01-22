---
name: 'step-01d-mcp-registry-discovery'
description: 'Automated discovery and integration of specialized MCP servers from registries'

nextStepFile: './step-01b-analysis-documentation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 1D: MCP Registry Discovery (ENFORCEMENT VERSION)

## STEP GOAL:

Automatically discover and validate specialized MCP servers from available registries according to strict enforcement and quality control criteria. Only servers passing critical gates may be added to the MCP stack.

## MANDATORY ENFORCEMENT RULES

### ANTI-VIOLATION / CRITICAL GATES

- 🛑 NEVER add any MCP server without passing all validation checkpoints.
- 🕹️ DO NOT skip failure handling or fallback protocols.
- ⚠️ For any registry or MCP service failure, you MUST document fallback strategy, confidence penalty, and GAP flags.
- ✔️ All suggested integrations must pass compatibility, relevance, reputation, and support criteria. Do not improvise, skip, or reorder steps.
- 📋 YOU ARE AN ENFORCEMENT AGENT — enforce all conditions explicitly.

### SELF-VALIDATION CHECKLIST

Before considering this step complete, you MUST:

- [ ] Confirm all MCP catalogs enumerated & queried according to procedure.
- [ ] Validate that each found MCP was checked for relevance, compatibility, and source reputation via explicit rating.
- [ ] Enforce fallback & penalty logic for each failed or low-reputation MCP.
- [ ] Summarize discovery results in a GAP/ENHANCEMENT section at the end.
- [ ] Update MCP stack and YAML progress ONLY if all above checks passed.

---

## 1. REGISTRY SOURCES

- **Official MCP Registry:** https://registry.modelcontextprotocol.io
- **GitHub MCP Servers Repo:** https://github.com/modelcontextprotocol/servers
- **MCP Server Finder:** https://www.mcpserverfinder.com
- **Awesome MCP Servers:** https://mcpservers.org

Documentation for each:    (domain, method, credibility, last-checked)

## 2. Verify MCP Availability

"**Verifying MCP servers availability for your problem-solving...**"

🚨 CRITICAL: MUST VERIFY ACTUAL MCP AVAILABILITY

Available MCPs for this session:
[ ] Check: Which MCP servers are actually available to me RIGHT NOW?
[ ] Check: What capabilities does each have?
[ ] Check: Are there any restrictions or limitations?
[ ] Check: Which MCPs are ACTUALLY relevant to this problem?

FOR EACH MCP LISTED:
- MCP Name: [name]
- Status: [Available / Not Available / Limited]
- Capabilities: [actual capabilities]
- Problem Relevance: [High/Medium/Low for this specific problem]
- Restrictions: [any limitations noted]

IF NO MCPs AVAILABLE FOR THIS PROBLEM:
- Flag: "MCP-dependent analysis not possible"
- Proceed with: "Manual research and analysis only"
- User notification: "Limited to [available resources]"

IF SOME MCPs AVAILABLE:
- Proceed with available only
- DO NOT assume restricted MCPs will work
- Document which MCPs actually used in analysis

**Available MCP Categories:**
- Web Search MCPs [VERIFY AVAILABLE]
- Market Research MCPs [VERIFY AVAILABLE]
- Technical Knowledge MCPs [VERIFY AVAILABLE]
- Business Intelligence MCPs [VERIFY AVAILABLE]

## MCP PARAMETER ANTI-RESTRICTION RULES

🚨 CRITICAL: MCP tools should NOT be artificially restricted

FORBIDDEN:
- ❌ Limiting MCP queries due to "safety concerns" if not genuine
- ❌ Arbitrarily restricting parameter ranges
- ❌ Assuming MCPs have limitations they don't have
- ❌ Pre-filtering MCP availability without checking
- ❌ Limiting searches due to perceived irrelevance (let MCP decide)

REQUIRED:
- ✅ Use full query capability of available MCPs
- ✅ Allow MCPs to process complex, multi-faceted queries
- ✅ Respect MCP design - don't add artificial constraints
- ✅ Document actual MCP limitations (not perceived ones)
- ✅ Verify restrictions with MCP documentation, not assumptions

RULE:
MCPs are designed to handle sophisticated queries.
If you think a query is "too complex" for an MCP,
check the actual MCP documentation first.
Do not arbitrarily restrict MCP usage.

---

## 3. DISCOVERY + VALIDATION PROTOCOL

### a) Problem Analysis Extraction

- Domain: [technical/business/operational/risk/financial]
- Capabilities needed: [list]
- Specialization: [general/specialized/domain-specific]
- Extract keywords using system metadata or context.

### b) Automated Search

- Query all sources using enforced structure.
- For any failed query: LOG failure, proceed to fallback, reduce confidence by 10% per critical failure.

### c) Validate Each MCP Candidate

- **Criteria (rate 1-5):**
    - Relevance to domain/problem (explicit score)
    - Reputation/trust (peer review, official/informal, community reviews)
    - Compatibility (protocol support, stack integration)
    - Availability (install/setup friction)
- For every MCP with score <3.5/5 in credibility or relevance: mark as SOFT FAILURE, reduce integration impact by 50%, document in summary.

### d) Fallback & GAP Tracking

- Maintain Fallback Log: [Registry/MCP, error, timestamp, attempted fallback, penalty]
- For missing coverage: add GAP Flag and annotate in summary.

## 3. DECISION: MCP Stack Expansion

- List validated MCPs with full explicit table (see next template).
- Propose only those SURVIVING all enforcement gates.

---

## INTEGRATION & GAP SUMMARY TEMPLATE

```
### MCP INTEGRATION SUMMARY

| MCP Name         | Registry/Source                | Relevance | Credibility | Compatibility | Status      | Confidence Adj. | Notes                    |
|------------------|-------------------------------|-----------|-------------|---------------|-------------|-----------------|--------------------------|
| Armor Crypto     | registry.modelcontext...       | 4.8       | 4.8         | 5             | ADDED       | 0%              | OK                       |
| MongoDB          | github.com/modelcontext...     | 4.6       | 4.2         | 5             | ADDED       | 0%              | Selected for DB tasks    |
| VendorX          | mcpserverfinder.com            | 2.8       | 2.7         | 3             | GAP         | -10%            | Reputation < threshold   |
| ...              | ...                            | ...       | ...         | ...           | ...         | ...             | ...                      |

**Total MCPs Queried:** [count]
**Added to Stack:** [count]
**Soft failures:** [count]
**GAP flags:** [count], Details: [list; cause; impact]

**CONFIDENCE ADJUSTMENT:**
- SUM total penalty due to GAP/FAIL: -[X]%
- MCP Stack coverage <100%? → Extra manual review required
```

---

## 4. PROGRESS REPORT & YAML UPDATE

When checklist satisfied, update {outputFile} frontmatter:

```yaml
stepsCompleted: ['step-01a-problem-definition', 'step-01b-analysis-documentation', 'step-01c-mcp-analysis', 'step-01d-mcp-registry-discovery']
progress: 18
currentPhase: 'mcp-registry-discovery'
lastStep: 'step-01d-mcp-registry-discovery'
mcpRegistryDiscoveryComplete: true
```

---

## 5. SELF-VALIDATION & STEP COMPLETION LOGIC

**BEFORE declaring this step complete you MUST:**  
- [x] Complete all self-validation checklist items above.  
- [x] Fill Integration Summary Table and GAP/FAIL protocol outcomes.  
- [x] Explicitly record all confidence adjustments with reasoning.

**If any checklist item is not fully satisfied:**
- Flag as system failure
- Do NOT proceed to next step; rerun missing parts

---

## CRITICAL SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All MCP registries queried and validated
- Every candidate checked on all criteria
- Fallbacks, penalties, and gaps documented
- Integration summary table present
- YAML/frontmatter updated in {outputFile}
- User presented only enforcement-passed MCPs

### ❌ SYSTEM FAILURE:

- ANY registry source skipped
- Any MCP added without explicit validation
- GAPs or failures not documented
- No confidence adjustment logged
- Progress/YAML not updated

---

## NEXT STEP

When all checks and enforcement logs are present AND the user confirms completion, proceed to step-01b-analysis-documentation.md.

## ОСНОВНЫЕ КАТАЛОГИ MCP СЕРВЕРОВ:

### 1. **Официальный MCP Registry**
```
URL: https://registry.modelcontextprotocol.io
Особенности:
- Авторитетный источник от Anthropic
- REST API: GET /v0/servers
- Верификация ownership
- Категории: database, cloud, devops, business
```

### 2. **MCP Servers Repository**
```
URL: https://github.com/modelcontextprotocol/servers
Особенности:
- Reference implementations
- Official integrations (GitHub, GitLab, Slack)
- Community серверы
- Категории по назначению
```

### 3. **MCP Server Finder**
```
URL: https://www.mcpserverfinder.com
Особенности:
- Comprehensive directory
- Implementation guides
- Compatibility matrix
- Community reviews
```

### 4. **Awesome MCP Servers**
```
URL: https://mcpservers.org
Особенности:
- Категоризированная коллекция
- Featured серверы
- Search по категориям
```

## ПРОЦЕДУРА ПОИСКА СПЕЦИАЛИЗИРОВАННЫХ MCP:

### 1. Анализ Текущей Проблемы

Извлечь ключевые характеристики проблемы:
- Домен: [technical/business/operational/risk/financial]
- Требуемые возможности: [search/analysis/database/cloud]
- Уровень специализации: [general/specialized/domain-specific]

### 2. Автоматизированный Поиск в Каталогах

**Поиск в официальном registry:**
```javascript
const registryResults = await fetch('https://registry.modelcontextprotocol.io/v0/servers', {
  method: 'GET',
  params: {
    search: problemKeywords,
    category: problemDomain
  }
});
```

**Поиск в MCP Servers Repository:**
```javascript
const repoResults = await searchGitHub({
  repo: 'modelcontextprotocol/servers',
  query: problemCapabilities,
  category: problemDomain
});
```

**Поиск в специализированных каталогах:**
```javascript
const finderResults = await searchMCPFinder({
  domain: problemDomain,
  capabilities: requiredCapabilities,
  useCase: problemType
});
```

**MCP Failure Handling Protocol:**

```
FOR each selected MCP:
  TRY:
    Execute MCP query
    Validate output quality
  CATCH (MCP_FAILURE):
    Log failure: [MCP name, error type, timestamp]

    Fallback Strategy:
    1. Attempt alternative MCP in same category
    2. If no alternative: Flag evidence gap for this category
    3. Reduce confidence by 10% per failed critical MCP
    4. Document manual investigation required
    5. Proceed with reduced evidence base

  QUALITY_CHECK:
    IF (mcp_output_credibility < 3.0) THEN
      Treat as soft failure
      Reduce weight of this MCP output by 50%
```

**MCP Execution Status:**
- Total MCPs attempted: [count]
- Successful executions: [count] ([percentage]%)
- Failed MCPs: [list with fallback actions]
- Confidence adjustment: -[X]% due to MCP failures

### 3. Оценка и Фильтрация Найденных MCP

**Критерии оценки:**
- **Релевантность**: Соответствие домену проблемы (0.0-1.0)
- **Надежность**: Репутация источника, отзывы сообщества
- **Совместимость**: Поддержка требуемых протоколов
- **Доступность**: Легкость установки и настройки

**Фильтрация результатов:**
- Удалить дубликаты
- Отсортировать по релевантности
- Выделить официальные интеграции

### 4. Предложение Специализированных MCP

**Категоризация найденных серверов:**

#### Финансовый домен:
- **Armor Crypto**: блокчейн, staking, DeFi, DCA, лимитные ордера
- **Bankless Onchain**: ERC20 токены, история транзакций, состояние смарт-контрактов
- **Paddle**: управление продуктами, биллинг, отчеты

#### Базы данных & Big Data:
- **Snowflake**: взаимодействие с Snowflake базами данных
- **MongoDB**: с инспекцией схем и безопасным доступом
- **Apache Doris/IoTDB/Pinot**: аналитика в реальном времени

#### Облачные платформы:
- **Alibaba Cloud**: (DataWorks, OpenSearch, RDS, OPS)
- **GitHub/GitLab**: управление репозиториями и issues
- **Kubernetes**: управление инфраструктурой

#### Бизнес-инструменты:
- **Amplitude**: аналитика продуктов и метрики
- **Chargebee**: управление подписками и биллингом
- **Linear**: управление проектами и задачами

### 5. Интерактивный Выбор и Интеграция

**Предложение пользователю:**
```
Найдено [N] потенциально полезных специализированных MCP:

1. [MCP Name] - [краткое описание] (релевантность: [score])
   Домен: [domain], Возможности: [capabilities]

2. [MCP Name] - [краткое описание] (релевантность: [score])
   ...

Хотите интегрировать какой-либо из этих MCP?
[Y]es - выбрать для интеграции
[N]o - продолжить без дополнительных MCP
[L]ist - показать полный список
```

### 6. Интеграция Выбранных MCP

**Для выбранных MCP:**
- Проверить совместимость
- Установить и настроить
- Добавить в активный MCP стек
- Обновить стратегию использования

### 7. Расширение MCP Стека

**Добавить к существующему стеку:**
```javascript
// Расширение текущего MCP стека специализированными серверами
const currentStack = getCurrentMCPStack(); // brave-search, perplexity, sequentialthinking, octocode
const specializedAdditions = selectedMCPs;

const enhancedStack = [...currentStack, ...specializedAdditions];

// Сохранить расширенный стек для следующих шагов
saveEnhancedMCPStack(enhancedStack);
```

**Обновление конфигурации:**
- Добавить специализированные MCP в активный стек
- Обновить domain mappings для будущих поисков
- Сохранить выбор пользователя для аналитики

## РЕЗУЛЬТАТЫ ПОИСКА:

**Текущий MCP стек:** brave-search-mcp, perplexity-mcp, sequentialthinking, octocode-mcp

**Добавленные специализированные MCP:** [список выбранных]

**Расширенный MCP стек:** [текущий + специализированные]

---

## КРИТЕРИИ ГОТОВНОСТИ:

- Каталоги MCP проанализированы
- Релевантные специализированные серверы найдены
- Оценка и фильтрация выполнена
- Пользовательские предпочтения учтены
- Интеграция завершенных MCP подтверждена

## СЛЕДУЮЩИЙ ШАГ:

Переход к step-01b-analysis-documentation.md с расширенным MCP стеком.
