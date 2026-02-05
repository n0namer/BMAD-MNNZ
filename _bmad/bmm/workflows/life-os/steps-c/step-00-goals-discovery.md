---
name: 'step-00-goals-discovery'
description: 'Discover and document user goals across 4 domains and 3 timeframes'
optional: true
nextStepFile: './step-01-collect-ideas.md'
goalsFile: '{bmb_creations_output_folder}/life-os/goals.yaml'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
goalsExamples: '../data/goals-examples/goals-examples.md'
goalsDomains: '../data/goals-examples/goals-4-domains-reference.md'
goalsSmartValidation: '../data/goals-examples/goals-smart-validation.md'
goalsTimeHorizons: '../data/goals-examples/goals-time-horizons.md'
goalsDomainTemplates: '../data/goals-domain-templates.md'
goalsYamlStructure: '../data/goals-yaml-structure.md'
goalsQuarterlyPlanning: '../data/goals-quarterly-planning.md'
---

# Step 0: Goals Discovery (Открытие Целей)

⚠️ **OPTIONAL STEP** - Can be deferred for Quick Track ideas (simple, low-stakes, exploration).

## STEP GOAL

Collect and document life goals across 4 domains (Finance, Business, Health, Personal) on 3 time horizons (1/3/5-10 years) for Strategic Alignment (Step 05).

## WHEN TO SKIP

- Quick Track ideas (simple, low-stakes)
- Exploring multiple ideas (define goals after selecting top idea)
- Time-sensitive idea evaluation

## MANDATORY EXECUTION RULES

- 🛑 NEVER generate goals without user input. You are a facilitator, not goal creator.
- 📖 CRITICAL: Read complete step before action
- ✅ Save all input to BOTH YAML AND Claude Flow memory
- ✅ SPEAK OUTPUT in Russian (`{communication_language}`)
- ✅ Max 2 questions at a time
- ✅ Validate SMART criteria (Specific, Measurable, Achievable)
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess/tool missing → achieve outcome in main thread

## EXECUTION PROTOCOL

### 0. Search Orchestrator Protocol (Required)
- Follow data/mcp_search_system_prompt_xml.md
- Execute: CLI memory search → local MD (rg) → web/MCP
- Convene consilium to rank 2-4 options with pros/cons
- Ask user to choose before proceeding

💡 **JIT Reference Files (load when needed):**
- `{goalsExamples}` - 3 complete scenarios
- `{goalsDomains}` - 4 domains with 20+ examples each
- `{goalsSmartValidation}` - SMART criteria + validation pairs
- `{goalsTimeHorizons}` - 1/3/5-10 year planning guide
- `{goalsDomainTemplates}` - Collection templates + examples
- `{goalsYamlStructure}` - YAML structure + memory save
- `{goalsQuarterlyPlanning}` - Review protocol + alignment scoring

### 1. Welcome User

```
🎯 **Life Operating System - Открытие Целей**

Добро пожаловать в систему управления жизнью!

Прежде чем начать работу с конкретными идеями и проектами,
давайте определим ваши главные цели на ближайшие годы.

Это поможет в Step 05 (Strategic Alignment) оценивать,
насколько каждый проект приближает вас к целям.

💡 **Почему это важно?**
- 85% проектов не завершаются из-за отсутствия связи с целями
- Четкие цели повышают фокус на 3x
- Стратегическое выравнивание снижает "шум" в портфеле на 60%

Мы пройдем через **4 области** (финансы, бизнес, здоровье, личное)
и **3 временных горизонта** (1 год, 3 года, 5-10 лет).

Займет ~10-15 минут.
```

### Step-Specific Subprocess Optimization Rules

- 🎯 Load ALL 7 JIT reference files in subprocesses (Pattern 3)
- 💬 Each subprocess returns ONLY relevant section for current phase
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess unavailable, achieve outcome in main context thread

### JIT Reference Loading (7 Subprocesses)

**For EACH reference file, launch a subprocess:**

1. **goals-domain-templates.md** - Returns template for selected domain only
2. **goals-smart-validation.md** - Returns SMART criteria checklist only
3. **goals-time-horizons.md** - Returns time horizon guide for selected period
4. **goals-okr-examples.md** - Returns 2-3 relevant examples, not all 50+
5. **goals-quarterly-planning.md** - Returns current quarter planning guide
6. **goals-structure.yaml** - Returns YAML structure template
7. **goals-yaml-structure.md** - Returns YAML syntax guide

Each subprocess:
- Loads its reference file
- Extracts ONLY applicable content for current collection phase
- Returns targeted extract to parent

**Total subprocess returns:** 400 lines (7 targeted extracts) instead of 3,000 lines (7 full files)

**Expected format from subprocess (example for domain templates):**
```markdown
## {Domain} Goals Template

**1-Year Goals Examples:**
- {example_1}
- {example_2}

**3-Year Goals Examples:**
- {example_1}
- {example_2}

**5-10 Year Goals Examples:**
- {example_1}
- {example_2}

**Collection Questions:**
1. {question_1yr}
2. {question_3yr}
3. {question_5-10yr}
```

**Graceful fallback:** If subprocess unavailable, load files progressively in main context.

---

### 2. Domain Collection

**Collect goals domain by domain (4 domains × 3 timeframes = 12 goals total).**

**Quick Reference:**
- **Finance:** Income, savings, investments, passive income, net worth
- **Business:** Revenue, products, customers, team, market position
- **Health:** Fitness, body composition, biomarkers, habits, longevity
- **Personal:** Skills, knowledge, relationships, experiences, contribution

**For EACH domain, ask 3 questions (1yr/3yr/5-10yr). Use template from `{goalsDomainTemplates}` with specific examples.**

💡 **JIT:** Load `{goalsDomainTemplates}` for complete collection template and examples by domain.


### 3. Validation & Refinement

After collecting all 12 goals:

```
✅ **Проверка целей**

Я собрал ваши цели. Давайте убедимся, что они конкретные и измеримые (SMART).

Для каждой цели проверю:
- **S**pecific (конкретная) - понятно, что именно нужно сделать?
- **M**easurable (измеримая) - есть числовой показатель?
- **A**chievable (достижимая) - реально ли это за данный срок?
```

**For EACH goal:** Check measurable outcome (₽500K, 10kg, 1000 клиентов) + specificity (английский до B2, not "выучить английский") + realistic timeframe.

**If vague:** Ask for concrete result, metrics, numbers. Example: "пассивный доход ₽50K/месяц" not "больше зарабатывать"

💡 **JIT:** Load `{goalsSmartValidation}` for detailed SMART criteria and 10 validation pairs. Load `{goalsDomainTemplates}` for refinement examples.

### 4. Save to YAML and Claude Flow Memory (Dual Storage - CRITICAL)

**Create `{goalsFile}` with structure from `{goalsYamlStructure}` (4 domains × 3 timeframes + alignmentWeights).**

**Run in parallel:**
1. Write YAML file
2. Save to Claude Flow memory: `life-os:goals:user` (full YAML content)
3. Save alignment weights: `life-os:scoring:alignment-weights` (1_year:0.5,3_years:0.3,5_10_years:0.2)

💡 **JIT:** Load `{goalsYamlStructure}` for complete YAML template and memory save commands.

### 5. Confirm Save

```
✅ **Цели сохранены!**

Saved to:
- 📄 YAML file: {goalsFile}
- 🧠 Claude Flow memory: life-os:goals:user
- 📊 Alignment weights: ready for Step 05

**Статистика:**
- {N}/12 целей соответствуют SMART
- Все 4 области охвачены
- Все 3 временных горизонта заполнены

💡 **Как это будет использоваться:**
В Step 05 (Strategic Alignment) каждая идея будет оцениваться
по формуле:

Strategic Alignment Score =
  (impact on 1-year goals × 0.5) +
  (impact on 3-year goals × 0.3) +
  (impact on 5-10-year goals × 0.2)

Готовы начать работу с идеями?
```

### 6. Proceed to Next Step (Auto-Proceed)

Display: "**Переходим к сбору идей...**"
Then load, read entire file, execute `{nextStepFile}`.

#### Menu Handling Logic:
- After completion, immediately save state, then load, read entire file, execute {nextStepFile}

#### EXECUTION RULES:
- **This is an auto-proceed step** (no menu displayed)
- **Do NOT wait** for user menu selection
- **Do NOT display** interactive options
- Save goals to dual storage (YAML file + Claude Flow memory)
- Save alignment weights for Step 05 scoring
- Update workflow plan frontmatter with completion status
- Immediately transition to Step 01 (collect ideas)

---

## SUCCESS METRICS

### ✅ SUCCESS
- All 12 goals collected (4 domains × 3 timeframes)
- 75%+ goals are SMART-compliant (9+/12)
- Saved to YAML file AND Claude Flow memory
- Alignment weights stored for Step 05
- User confirmed ready to proceed

### ❌ SYSTEM FAILURE
- Generating goals instead of collecting user input
- Not saving to BOTH storages (YAML + memory)
- Asking >2 questions at once
- Not validating SMART criteria
- Skipping confirmation

**Master Rule:** DISCOVERY not INVENTION. Listen, guide, validate, document, save.

---

## REFERENCE FILES (JIT Loading)

Load when needed:
- `{goalsDomainTemplates}` - Collection templates + domain examples
- `{goalsYamlStructure}` - YAML structure + memory save commands
- `{goalsQuarterlyPlanning}` - Review protocol + alignment scoring
- `{goalsExamples}` - 3 complete scenarios
- `{goalsDomains}` - 4 domains with 20+ examples
- `{goalsSmartValidation}` - SMART criteria + validation pairs
- `{goalsTimeHorizons}` - 1/3/5-10 year planning guide
