---
name: 'step-05a1-criteria-validation'
description: 'Validate solution against success criteria and assess risk-adjusted value'

nextStepFile: './step-05b-decision-validation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
solutionSelectionTemplates: '../data/solution-selection-templates.md'
---

# Step 5a1: Criteria Validation & Risk Assessment

---

## ANTI-VIOLATION GUARDS

**❌ VIOLATION #2: Simulating Work (EXPANDED)**

FORBIDDEN PHRASES - YOU MUST NEVER USE THESE:

Category 1: Conditional/Hypothetical
- ❌ "I would analyze..."
- ❌ "I would document..."
- ❌ "We could..."
- ❌ "Based on user input, I would..."
- ❌ "This will be done..."
- ❌ "Assessment complete"

REQUIRED REPLACEMENTS:
Instead of: "I would analyze..."
Use: "I am analyzing... [show actual analysis results]"

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

---

## EXECUTION PROTOCOLS:

- 🎯 [protocol 1]
- 💾 [protocol 2]
- 📖 [protocol 3]
- 🚫 **FORBIDDEN: Generic Examples** - Do not use "[user_problem]", "[example]", "[placeholder]"
- ✅ **REQUIRED: Problem-Specific Data** - Use actual data from user's real problem

---

## CRITICAL GAPS CHECK

**🚨 BEFORE PROCEEDING - VERIFY NO CRITICAL GAPS**
(*см. паттерн проблемы №24*)

- Каждый незаполненный/абстрактный кусок данных, не отвечающий must-have требованиям, считается critical gap.
- Если крит. gap не может быть устранён — STOP, объяснить что требуется, получить у пользователя данные.

---

## 🔒 MANDATORY SELF-VALIDATION PROTOCOL

**🚨 YOU MUST EXECUTE THIS - NOT JUST READ IT**
(*см. паттерн проблемы №30 — полный чеклист!*)

### VALIDATION CATEGORY 1: Work Completion
- [ ] Все mandatory sequence steps выполнены?
- [ ] Нет ли симуляции (только реальные действия)?
- [ ] Используются реальные пользовательские данные?
- [ ] Все user-input запросы отработаны и задокументированы?

### VALIDATION CATEGORY 2: Output Documentation
- [ ] Результаты анализа реально сохранены?
- [ ] Frontmatter обновлён полностью по формату
- [ ] Ничего не пропущено?

### VALIDATION CATEGORY 3: Menu Interaction
- [ ] Меню реально показано
- [ ] Ждём ответа пользователя по меню
- [ ] Обработка опций, возврат в меню, если не 'C'

### VALIDATION CATEGORY 4: Next Step Prep (if 'C')
- [ ] nextStep файл существует, будет загружен полностью
- [ ] Чтение цели, структуры, полной последовательности следующего файла

### VALIDATION CATEGORY 5: Quality Checks
- [ ] Нет ли критических дыр
- [ ] Достаточен ли confidence
- [ ] MCP tools вызваны (если применимо)
- [ ] Evidence-based (если применимо)

Если хоть один пункт fail — ОСТАНОВИТЬСЯ И ИСПРАВИТЬ!


## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative validation, not unilateral assessment
- ✅ You bring evaluation frameworks and risk methodologies
- ✅ User brings solution understanding and criteria preferences
- ✅ Together we establish quantitative evaluation foundation

### Step-Specific Rules:

- 🎯 Focus only on validation and risk assessment (not quality validation)
- 🚫 FORBIDDEN to perform decision quality validation yet
- 💬 Approach: Systematic criteria compliance and risk analysis
- 📋 Document validation results and risk calculations

## EXECUTION PROTOCOLS:

- 🎯 Validate against all success criteria dimensions
- 💾 Perform comprehensive risk-adjusted value calculation
- 📖 Prepare quantitative foundation for decision validation
- 🚫 Only validation - quality assessment comes next

## CONTEXT BOUNDARIES:

- Available context: Applicability matrix results from step-4
- Focus: Success criteria validation and risk-adjusted value assessment
- Limits: Do not perform decision quality validation or alternative analysis
- Dependencies: Matrix evaluation and recommendation framework established

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Success Criteria

"**Загружаю success criteria из предыдущих шагов...**"

Load success criteria established in step-1 and refined in step-2:

**Must-Have Criteria:**
- [List critical requirements from step-1]

**Should-Have Criteria:**
- [List important requirements from step-1]

**Nice-to-Have Criteria:**
- [List enhancement opportunities from step-1]

### X. MANDATORY CONFLICT DETECTION

🚨 YOU MUST CHECK FOR CRITERION CONFLICTS

Conflict Detection Process:

Step 1: Create Conflict Matrix
For each pair of criteria, ask: "Can both be maximized simultaneously?"

Conflict Matrix:
              | Cost | Quality | Speed | Security |
            Cost      |  -   |   ❌    |   ❌  |    ✓     |
            Quality   |  ❌  |    -    |   ❌  |    ✓     |
            Speed     |  ❌  |   ❌    |   -   |    ❌    |
            Security  |  ✓   |    ✓    |   ❌  |    -     |

Legend:
✓ = No conflict (can optimize both)
❌ = Conflict exists (tradeoff required)

Step 2: For Each Conflict (❌), Document:
Conflict: [Criterion A] vs [Criterion B]
Nature of Conflict:
- [Explain why they conflict]
- [Example of the tradeoff]

Which Takes Priority?
- User's stated priority: [A/B/Equal]
- Justification: [why]

Resolution Strategy:
- [How we'll handle this conflict in scoring]

Step 3: Verify Priorities Resolve Conflicts
- [ ] All conflicts have stated priority
- [ ] Priorities are consistent (no circular conflicts: A>B, B>C, C>A)
- [ ] User explicitly approved priority order
- [ ] Scoring will reflect these priorities

FORBIDDEN:
- Ignoring conflicts
- Assuming no conflicts exist
- Not asking user to resolve conflicts
- Proceeding with inconsistent priorities

### 2. Validate Against Success Criteria

"**Валидирую primary recommendation против success criteria...**"

Compare the top-ranked solution from matrix evaluation against success criteria:

**Must-Have Compliance Check (HARD GATE):**
- [ ] Critical requirements met
- [ ] Deal-breaker constraints satisfied
- [ ] Minimum viable solution achieved

### MANDATORY SEQUENCE - 2. Validate Against Success Criteria

HARD GATE - Critical requirements met

CRITICAL VALIDATION RULE:
IF any Must-Have requirement scores < 4.0/5 THEN
├─ BLOCK this recommendation
├─ FLAG as NON-COMPLIANT
├─ REQUIRE alternative solution or mitigation plan
└─ DO NOT proceed to final documentation
ELSE
└─ PASS GATE - Proceed to risk-adjusted value assessment

**Should-Have Assessment:**
- [ ] Important requirements addressed
- [ ] Value-adding features included
- [ ] Competitive advantages maintained

**Nice-to-Have Optimization:**
- [ ] Enhancement opportunities identified
- [ ] Future-proofing considerations
- [ ] Scalability and adaptability factors

**Compliance Scoring:**
- Must-Have: [X]/[Y] requirements met ([percentage]%)
- Should-Have: [X]/[Y] requirements met ([percentage]%)
- Nice-to-Have: [X]/[Y] enhancements available ([percentage]%)

**Hard Gate Enforcement:**
```
IF must_have_compliance < 100% THEN
  STOP ANALYSIS
  RECOMMENDATION: NON-COMPLIANT - Review alternative options
  REASON: [List failed must-have requirements]
  NEXT ACTION: Return to step-04a to evaluate alternative solutions
ELSE
  PASS GATE - Proceed to risk-adjusted value assessment
```

### 3. Assess Risk-Adjusted Value

"**Оцениваю risk-adjusted value of recommendation...**"

Load risk-adjusted value framework from {solutionSelectionTemplates}:

**Expected Value Assessment:**
- **Quantitative Benefits:** [financial/monetary/value_metrics]
- **Qualitative Benefits:** [strategic/operational/capability_gains]
- **Total Expected Value:** [quantitative_assessment]

**Risk Impact Assessment:**
- **Implementation Risk:** [probability] × [impact] = [risk_value]
- **Operational Risk:** [probability] × [impact] = [risk_value]
- **Opportunity Risk:** [probability] × [impact] = [risk_value]
- **Total Risk Exposure:** [aggregate_risk]

Risk-Adjusted Value Assessment:

Expected Value Assessment:
- Quantitative Benefits [financial/monetary/value metrics]
- Qualitative Benefits [strategic/operational/capability gains]
- Total Expected Value [quantitative assessment]

Risk Impact Assessment:
- Implementation Risk [probability × impact = risk-value]
- Operational Risk [probability × impact = risk-value]
- Opportunity Risk [probability × impact = risk-value]
- Total Risk Exposure [aggregate risk]

Risk-Adjusted Final Value:
RiskAdjustedValue = ExpectedValue × (1 - RiskImpact) × ConfidenceLevel

Risk-Adjusted Value Rating: [High/Medium/Low] value proposition

### 4. Document Validation Results

"**Документирую validation results в consilium report...**"

Update {outputFile} with validation analysis:

```markdown
## Solution Validation Results

### Success Criteria Compliance

#### Must-Have Requirements (Critical - 100% Required)
- ✅ **[Requirement 1]:** [compliance_status] - [evidence/justification]
- ✅ **[Requirement 2]:** [compliance_status] - [evidence/justification]
- ✅ **[Requirement 3]:** [compliance_status] - [evidence/justification]

**Overall Must-Have Compliance:** [percentage]% ([status])

#### Should-Have Requirements (Important - 80%+ Recommended)
- ✅ **[Requirement 1]:** [compliance_status] - [evidence/justification]
- ⏳ **[Requirement 2]:** [compliance_status] - [evidence/justification]
- ❌ **[Requirement 3]:** [compliance_status] - [evidence/justification]

**Overall Should-Have Compliance:** [percentage]% ([status])

#### Nice-to-Have Requirements (Optional - Enhancements)
- ⭐ **[Enhancement 1]:** [availability_status] - [value_add]
- ⭐ **[Enhancement 2]:** [availability_status] - [value_add]

### Risk-Adjusted Value Analysis

#### Expected Value Assessment
- **Quantitative Benefits:** [financial/monetary/value_metrics]
- **Qualitative Benefits:** [strategic/operational/capability_gains]
- **Total Expected Value:** [quantitative_assessment]

#### Risk Impact Assessment
- **Implementation Risk:** [probability] × [impact] = [risk_value]
- **Operational Risk:** [probability] × [impact] = [risk_value]
- **Opportunity Risk:** [probability] × [impact] = [risk_value]
- **Total Risk Exposure:** [aggregate_risk]

#### Risk-Adjusted Final Value
```
Risk_Adjusted_Value = [expected_value] × (1 - [risk_impact]) × [confidence]
= [calculation_result]
```

**Risk-Adjusted Value Rating:** [High/Medium/Low] value proposition
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

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Decision Validation"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper validation analysis
- IF P: Execute {partyModeWorkflow} to discuss validation results with other agents
- IF C: Save validation results to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#6-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and validation results are saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin decision validation.

### MANDATORY SEQUENCE - 7. Criteria Validation as Learning System

🚨 THIS IS NOT OPTIONAL
🚨 THIS IS HOW THE VALIDATION FRAMEWORK IMPROVES OVER TIME

Master Rule:
Criteria validation is what transforms EMBER Consilium from
static methodology to adaptive learning system.
Skip this step and all other improvements mean nothing.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Solution validated against all success criteria dimensions
- Risk-adjusted value calculation properly performed with all components
- Compliance scoring completed for all criteria categories
- Validation results comprehensively documented
- Progress updated to 65% with validation foundation established

### ❌ SYSTEM FAILURE:

- Success criteria validation incomplete or missing
- Risk-adjusted analysis inadequate or incorrect
- Compliance scoring not performed systematically
- **Must-Have hard gate not enforced - non-compliant solution recommended**
- **Sensitivity analysis not performed on compliance thresholds**
- Validation documentation inadequate or missing

**Master Rule:** Criteria validation establishes compliance foundation - all assessments must be comprehensive and evidence-based.
