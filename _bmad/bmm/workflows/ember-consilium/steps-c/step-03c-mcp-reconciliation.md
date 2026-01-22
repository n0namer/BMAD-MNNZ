---
name: 'step-03c-mcp-reconciliation'
description: 'Reconcile conflicting MCP outputs and assess resolution strategy'

nextStepFile: './step-03d-evidence-validation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 3c: MCP Output Reconciliation

## 🚨 ANTI-VIOLATION GUARDS (EXPANDED)

**Эти нарушения абсолютно запрещены:**

### ❌ VIOLATION #1: Skipping Menu Display
- **FORBIDDEN:** Пропуск меню перед переходом на следующий шаг
- **REQUIRED:** Меню всегда показывается, всегда ждет реального выбора пользователя

### ❌ VIOLATION #2: Simulating Work (EXPANDED)
**FORBIDDEN PHRASES - YOU MUST NEVER USE THESE:**
- ❌ "I would analyze...", "I would gather...", "I would document...", "One would need to...", "We could...", "It would be necessary to..."
- ❌ "Based on user input, I would...", "The analysis would show...", "Results would indicate...", "This would be documented as..."
- ❌ "I will analyze..." (если не насрочно), "This will be done...", "We will gather..."
- ❌ "Analysis complete" (без фактических результатов), "Evidence gathered" (без вывода данных), "Assessment done" (без результата)

**REQUIRED REPLACEMENTS:**
- Всегда используйте настоящее время: "Я анализирую...", "Результаты: ..."
- Фактически выполняйте все действия, ничего не симулируйте

**SIMULATION DETECTION:**
Если вы описываете, что бы сделали, а не что делаете сейчас, — ОСТАНОВИТЕСЬ. Вы должны реально делать работу, а не обещать её выполнить.

### ❌ VIOLATION #3: Generic Placeholders & Data
- **FORBIDDEN:** Выводить "[user_problem]", "[example]", "[placeholder]", шаблонные фрагменты
- **REQUIRED:** Использовать только реально предоставленные пользователем данные

### ❌ VIOLATION #4: Skipping MCP Calls
- **FORBIDDEN:** Не делать реальные вызовы к MCP tool'ам, если они требуются этим шагом
- **REQUIRED:** Реально вызывать MCP-тулы, документировать что вызвано, что недоступно

### ❌ VIOLATION #5: Partial File Loading
- **FORBIDDEN:** Грузить следующий step-файл только частично или запускать до полного чтения
- **REQUIRED:** Грузить и читать целиком, ДО выполнения

### ❌ VIOLATION #6: No User Input
- **FORBIDDEN:** Предполагать переход без явного выбора пользователя
- **REQUIRED:** Всегда ждать реального ввода с клавиатуры перед продолжением

### ❌ VIOLATION #7: Skipping Sequence Steps
- **FORBIDDEN:** Пропускать шаги в MANDATORY SEQUENCE
- **REQUIRED:** Следовать строго по порядку

### ❌ VIOLATION #8: Not Saving Work
- **FORBIDDEN:** Показывать результаты без сохранения их в {outputFile}
- **REQUIRED:** Всегда сохранять работу, обновлять frontmatter

---

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

## STEP GOAL:

To reconcile conflicting outputs from parallel MCP executions, establish resolution strategy, and determine confidence adjustments based on conflict severity.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative conflict resolution, not unilateral reconciliation
- ✅ You bring conflict assessment frameworks and resolution methodologies
- ✅ User brings contextual understanding and domain judgment
- ✅ Together we establish clear resolution strategy

### Step-Specific Rules:

- 🎯 Focus only on MCP output conflicts and resolution
- 🚫 FORBIDDEN to dismiss conflicts or ignore disagreements
- 💬 Approach: Systematic conflict identification and transparent resolution
- 📋 Document all conflicts and resolution approaches

## EXECUTION PROTOCOLS:

- 🎯 [protocol 1] Identify all MCP output conflicts
- 💾 [protocol 2] Assess conflict type and severity
- 📖 [protocol 3] Determine resolution strategy
- 🚫 **FORBIDDEN: Generic Examples** - Do not use "[user_problem]", "[example]", "[placeholder]"
- ✅ **REQUIRED: Problem-Specific Data** - Use actual data from user's real problem

## CONTEXT BOUNDARIES:

- Available context: MCP outputs from step-03b
- Focus: Conflict detection, assessment, and resolution
- Limits: Do not perform evidence validation yet
- Dependencies: MCP outputs gathered and documented

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### X. CONTRADICTORY EVIDENCE DETECTION & RESOLUTION

🚨 YOU MUST ACTIVELY LOOK FOR CONTRADICTIONS

Contradiction Detection Process:

Step 1: Cross-Reference All Evidence
For the same factor/question, what do different sources say?

Example:
Question: "Is technology X scalable for our use case?"

Source 1 (perplexity-mcp): "Yes, highly scalable"
Source 2 (brave-search result): "Known scalability issues at high load"
Source 3 (octocode examples): "Mixed - works for some, not others"

CONTRADICTION DETECTED ✓

Step 2: Document Each Contradiction
Contradiction #[N]:
- Question: [What we're trying to answer]
- Conflicting Evidence:
  1. [Source A]: Says [X]
     - Credibility: [score]
     - Date: [date]
     - Context: [context]
  
  2. [Source B]: Says [opposite of X]
     - Credibility: [score]
     - Date: [date]
     - Context: [context]

- Analysis:
  - Why might they disagree? [possible explanations]
  - Which is more credible? [rationale]
  - Which is more relevant to our context? [rationale]

Step 3: Resolution Strategy

Option A: One source clearly more credible
Resolution: Trust [Source A]
Reason: [Higher credibility score / More recent / More relevant context]
Confidence: [Medium - noting the contradiction exists]

Option B: Both equally credible
Resolution: Flag as UNRESOLVED CONTRADICTION
Action Required:
- Seek additional evidence to break tie
- Ask user for domain expertise input
- Proceed with BOTH scenarios considered
Confidence: [Low - due to unresolved contradiction]

Option C: Context-dependent
Resolution: BOTH may be correct in different contexts
Our Context: [our specific situation]
Therefore: [which applies to us]
Confidence: [Medium - context-specific]

Step 4: Impact on Decision
Impact of Contradiction #[N]:
- Affects: [which solution options / factors]
- Severity: [High/Medium/Low]
- If unresolved: [how we're handling uncertainty]
- Confidence reduction: -[X]%

YOU MUST DOCUMENT:
## Evidence Reconciliation Report
- Total Evidence Items: [count]
- Contradictions Detected: [count]
- Contradiction Details: [List each with full analysis]
- Resolution Summary:
  - Resolved: [count] contradictions
  - Unresolved: [count] contradictions
  - Confidence impact: -[total]%
- Actions Required: [List any evidence gaps to fill]

FORBIDDEN:
- Ignoring contradictory evidence
- Cherry-picking evidence that supports preferred option
- Not documenting contradictions
- Proceeding as if contradictions don't exist

### 1. Load MCP Execution Results

"**Загружаю MCP outputs из step-03b для анализа конфликтов...**"

Load all MCP results from {outputFile}:
- brave-search findings
- perplexity synthesis
- octocode technical examples
- software-planning insights
- sequentialthinking analysis

**Document each MCP's outputs with:**
- MCP name and execution time
- Key findings (3-5 main points)
- Data sources cited
- Confidence level in output (analyst assessment)

### 2. Identify MCP Output Conflicts

"**Идентифицирую conflicts между MCP outputs...**"

**Conflict Detection Checklist:**

For each pair of MCP outputs, assess:
```
CONFLICT TYPE MATRIX:

1. CONTRADICTORY CLAIMS (direct opposition)
   Example:
   brave-search: "Option A is market leader, 45% share"
   perplexity: "Option A market share declining, now 32%"
   → Clear contradiction on factual claim

2. TEMPORAL DIVERGENCE (different timeframes)
   Example:
   octocode: "Option B had 5000 GitHub stars in 2023"
   brave-search: "Option B has 8000 GitHub stars in 2025"
   → Same metric, different time periods (not necessarily conflict)

3. DIFFERENT METRICS (incomparable dimensions)
   Example:
   brave-search: "Option A is popular (market penetration: 35%)"
   octocode: "Option A has poor code documentation (GitHub rating: 2.3/5)"
   → Different dimensions, not contradictory

4. INTERPRETATION DIVERGENCE (different conclusions from same data)
   Example:
   perplexity: "Option A's declining user growth indicates market saturation—
                    RECOMMENDATION: Avoid, market is mature"
   sequentialthinking: "Option A's declining growth rate is normal for mature product—
                            RECOMMENDATION: Accept, stable market position"
   → Same data, different interpretation

5. CREDIBILITY DIVERGENCE (different source quality)
   Example:
   MCP-A (brave-search): "McKinsey consulting report ranks Option A as top choice"
                      [Tier 1 source: peer-reviewed, large sample, institutional]
   MCP-B (perplexity): "Reddit community consensus favors Option B"
                    [Tier 3 source: anecdotal, self-selected, unverified]
   → Different source types with different reliability
```

**MCP Conflict Summary:**
- Total MCP pairs analyzed: [count]
- Conflicting pairs detected: [count]
- Conflict types: [list which types found]
- Unresolved conflicts: [count]

### 3. Assess Conflict Severity and Resolution Strategy

"**Оцениваю severity каждого конфликта и определяю resolution strategy...**"

**For each identified conflict:**

**STEP 1: Determine Conflict Type**
```
Classify as: [Contradictory / Temporal / Different Metrics / Interpretation / Credibility]
```

**STEP 2: Assess MCP Credibility**

Rate each conflicting MCP output on:
- Output Quality (1-5): How well-reasoned and detailed?
- Source Reliability (1-5): How credible are cited sources?
- Methodology Transparency (1-5): How clear is reasoning?
- Recency (1-5): How current is information?

```
MCP_Credibility_Score = (Quality × 0.3) + (Reliability × 0.3) + (Transparency × 0.2) + (Recency × 0.2)
```

**STEP 3: Apply Resolution Strategy by Conflict Type**

```
IF Conflict_Type = CONTRADICTORY CLAIMS:
  Resolution Strategy:
  1. Verify sources for both claims (cite specific publications)
  2. Assess which has higher credibility score
  3. Check publication dates (prefer newer if high quality)
  4. Conduct manual investigation if disagreement substantial
  5. IF manual investigation inconclusive:
     - Report both claims in evidence
     - Reduce confidence by 10% for this factor
     - Mark as "UNRESOLVED - REQUIRES DECISION OVERRIDE"

IF Conflict_Type = TEMPORAL DIVERGENCE:
  Resolution Strategy:
  1. Establish timeline of measurements
  2. Assess rate of change
  3. Use most recent data IF credible
  4. Document trend IF significant
  5. No confidence penalty

IF Conflict_Type = DIFFERENT METRICS:
  Resolution Strategy:
  1. Recognize as complementary, not contradictory
  2. Include both metrics in evaluation factors
  3. Add evaluation factor if missing
  4. No conflict resolution needed
  5. No confidence penalty

IF Conflict_Type = INTERPRETATION DIVERGENCE:
  Resolution Strategy:
  1. Extract common underlying data
  2. Assess reasoning quality for each interpretation
  3. Evaluate interpretation credibility
  4. Document both interpretations as "valid perspectives"
  5. Confidence penalty: -2% per interpretation divergence

IF Conflict_Type = CREDIBILITY DIVERGENCE:
  Resolution Strategy:
  1. Assess credibility of each source
  2. Weight MCP outputs by credibility score
  3. Accept higher-credibility source for that dimension
  4. Document lower-credibility source as "alternative view"
  5. No confidence penalty if credibility difference clear
```

### 4. Document MCP Reconciliation Results

"**Документирую MCP reconciliation strategy и resolution approach...**"

Update {outputFile} with MCP Conflict Resolution Report:

```markdown
## MCP Output Reconciliation Report

### Conflict Summary
- **Total Conflicts Identified:** [count]
- **Conflict Types:** [list distribution across types]
- **Resolved Conflicts:** [count] ([resolution method])
- **Unresolved Conflicts:** [count] ([impact on decision])

### Detailed Conflict Analysis

#### Conflict 1: [Clear descriptive title]
**Involved MCPs:** [MCP1 vs MCP2]
**Conflict Type:** [Contradictory / Temporal / Different Metrics / Interpretation / Credibility]

**Claim A (MCP1):** [Exact quote from output]
- Source: [cited publication/data]
- Date: [publication date]
- Credibility Score: [X]/5

**Claim B (MCP2):** [Exact quote from output]
- Source: [cited publication/data]
- Date: [publication date]
- Credibility Score: [X]/5

**Resolution Strategy:** [Applied strategy from STEP 3]
**Resolution Result:** [How conflict resolved or why unresolved]
**Confidence Adjustment:** -[X]% due to this conflict

#### Conflict 2: [Next conflict with same structure]
...continue for all conflicts...

### Confidence Adjustment Due to MCP Conflicts

**Base Confidence (from evidence):** [X.XX]
**Conflict Penalties:**
- Unresolved contradictory claims: -[X]% per conflict
- Unresolved interpretation divergence: -[X]% per conflict
- Credibility mismatches: -[X]% per conflict

**Adjusted Confidence:** [X.XX - Y%] = [NEW SCORE]
**Total Confidence Reduction:** [X]%

### Unresolved Conflicts Requiring Manual Investigation

1. **[Conflict title]**
   - Issue: [why unresolved]
   - Recommendation: [additional research or expert consultation needed]
   - Timeline: [when must this be resolved]
   - Decision Impact: [consequence if not resolved]

### MCP Weighting for Matrix Evaluation

Based on reconciliation analysis:
```
brave-search weight: [X]% (credibility score: [X.X]/5)
perplexity weight: [X]% (credibility score: [X.X]/5)
octocode weight: [X]% (credibility score: [X.X]/5)
[other MCPs with weights]
```

All MCP outputs weighted by credibility in matrix evaluation rather than equally.
```

### 5. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
---
# Document Identity
consiliumId: "EMB-CSL-[timestamp]"
title: "EMBER Consilium Report: [user's decision topic]"
created: "[ISO date when started]"
lastUpdated: "[ISO date now]"

# Workflow Progress
stepsCompleted:
  - 'step-[previous steps]'
  - '[current step name]'  # ADD THIS STEP
progress: [XX]  # Current progress percentage
currentPhase: '[current phase name]'
lastStep: '[current step name]'

# Phase Completion Flags
complexityAssessmentComplete: [true/false]
problemAnalysisComplete: [true/false]
decisionFrameworkApplicationComplete: [true/false]
evidenceCollectionComplete: [true/false]
evidenceValidationComplete: [true/false]
matrixSetupComplete: [true/false]
scoringApplicationComplete: [true/false]
[other phase flags as applicable]

# Decision Status
status: "[PHASE_NAME_COMPLETE]"
nextStep: "[next step file name]"

# Quality Metrics
overallConfidence: [0-100]
evidenceQuality: [0-100]
criticalGaps: [count]

# User Context
userName: "[user name]"
decisionDomain: "[technical/business/operational/etc]"
decisionComplexity: "[Light/Standard/Comprehensive]"
---

Frontmatter Validation Checklist:
- [ ] consiliumId exists and unique
- [ ] title reflects user's actual decision
- [ ] stepsCompleted array includes current step
- [ ] progress percentage updated correctly
- [ ] currentPhase matches current work
- [ ] lastStep is current step name
- [ ] Appropriate completion flag set to true
- [ ] status reflects current state
- [ ] nextStep points to correct file

IF ANY FIELD IS MISSING OR WRONG:
- Correct it before proceeding
- Verify against step requirements
- Do not skip fields
```

### 6. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Evidence Validation"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper conflict analysis
- IF P: Execute {partyModeWorkflow} to discuss conflicts with other agents
- IF C: Save reconciliation results to {outputFile}, update frontmatter, then load and read {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#6-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and display menu again

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and reconciliation results are saved to {outputFile} will you then load and read fully {nextStepFile} to execute evidence validation with MCP conflict penalties incorporated.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All MCP output conflicts identified systematically
- Conflict types classified correctly
- Resolution strategy applied to each conflict
- Unresolved conflicts explicitly documented
- Confidence adjustments calculated for conflicts
- MCP weighting established for matrix evaluation
- Progress updated to 38% with reconciliation completed

### ❌ SYSTEM FAILURE:

- MCP conflicts not identified or glossed over
- Conflict types misclassified
- Resolution strategy not applied
- Unresolved conflicts ignored
- Confidence penalties not calculated
- Conflicts affecting matrix evaluation not documented

**Master Rule:** MCP reconciliation ensures quality of intelligence gathering - unresolved conflicts that become hidden create systematic bias in final recommendation.
