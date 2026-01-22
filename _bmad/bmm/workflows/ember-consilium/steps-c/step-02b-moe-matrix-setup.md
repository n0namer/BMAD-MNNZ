---
name: 'step-02b-moe-matrix-setup'
description: 'Establish MOE framework, matrix template, and confidence assessment'

nextStepFile: './step-03a-evidence-identification.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 2b: MOE Matrix Setup & Confidence Framework

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

To establish MOE analysis framework, create applicability matrix template, define confidence assessment framework, and document complete analysis methodology in consilium report.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative framework completion, not unilateral design
- ✅ You bring MOE methodology and matrix expertise
- ✅ User brings domain validation and framework refinement
- ✅ Together we complete comprehensive analysis framework

### Step-Specific Rules:

- 🎯 Focus only on MOE framework, matrix template, and confidence setup
- 🚫 FORBIDDEN to perform actual analysis or evaluation yet
- 💬 Approach: Systematic framework completion with user validation
- 📋 Document complete analysis methodology and templates

## EXECUTION PROTOCOLS:

- 🎯 Establish MOE dimensions and matrix structure
- 💾 Define confidence assessment framework
- 📖 Complete analysis methodology documentation
- 🚫 Only framework setup - evidence gathering comes next

## CONTEXT BOUNDARIES:

- Available context: Decision Block v2.0 phases 1-2 completed
- Focus: MOE framework establishment and matrix template creation
- Limits: Do not perform evidence gathering or solution evaluation
- Dependencies: Framework application foundation established

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 0. Assess Decision Complexity (NEW)

"**Оцениваю complexity решения для определения appropriate process...**"

**Decision Complexity Matrix:**

Calculate complexity score across 3 dimensions:
1. **Scope:** [Low: 2-3 options | Medium: 4-6 options | High: 7+ options]
2. **Uncertainty:** [Low: <3 unknown factors | Medium: 3-6 unknowns | High: 7+ unknowns]
3. **Stakeholders:** [Low: 1-3 people | Medium: 4-8 people | High: 9+ people]

**Complexity Classification:**
```
IF (Scope=Low AND Uncertainty=Low AND Stakeholders=Low) THEN
  Process: LIGHT (5 steps, 4 hours)
  Steps: 00, 01a, 03a, 04a, 05c

ELSE IF (Scope<=Medium AND Uncertainty<=Medium) THEN
  Process: STANDARD (15 steps, 2 days)
  Steps: 00, 01a-01c, 02a, 03a-03c, 04a-04c, 05a-05c

ELSE
  Process: COMPREHENSIVE (full 31 steps, 5-7 days)
  Steps: All steps 00 through 05d
```

**Selected Process:** [LIGHT / STANDARD / COMPREHENSIVE]
**Estimated Timeline:** [hours/days]
**Justification:** [why this complexity level]

### 1. Validate User Problem Against Generic Factors

"**Проверяю что factors соответствуют твоему specific problem...**"

🚨 CRITICAL GATE: NO GENERIC FACTORS

Before building matrix, verify:

Check 1: Are ALL factors tied to user's problem?
- Review each factor from step-02a
- For each factor: "Is this from the user's actual problem?" [Yes/No]
- If NO to any factor → STOP
- REMOVE generic factors
- ADD factors specific to this problem

Check 2: Do factors match user's constraints?
- [ ] Technical factors match user's tech stack
- [ ] Business factors match user's business model
- [ ] Timeline factors match user's schedule
- [ ] Resource factors match user's available resources
- [ ] Regulatory factors match user's jurisdiction

Check 3: Are solution options aligned to factors?
- For each solution option: "Is it relevant to this specific problem?" [Yes/No]
- If NO → REMOVE option
- If needed: ASK user for more aligned options

IF GATE FAILS (generic factors detected):
→ STOP immediately
→ Rebuild factor list using only problem-specific factors
→ Confirm with user before proceeding to matrix setup

Load framework application from {outputFile}:
- Problem definition refinement completed
- Evidence requirements established
- Methodology foundation confirmed

### 2. Establish MOE Analysis Framework

"**Устанавливаю MOE Analysis Framework для multi-dimensional evaluation...**"

**Define evaluation dimensions:**
- Technical feasibility dimension
- Business value dimension
- Operational impact dimension
- Risk profile dimension

**Establish evaluation criteria for each dimension:**
- Technical: complexity, scalability, integration, maintainability
- Business: ROI, time-to-value, strategic alignment, resource requirements
- Operational: process impact, training needs, support overhead, change management
- Risk: implementation risk, operational risk, security risk, compliance risk

### 3. Create Applicability Matrix Template

"**Создаю Applicability Matrix template для solution evaluation...**"

**Matrix structure:**
- Factor identification (technical, business, operational, risk)
- Scoring scale definition (1-5 with confidence levels)
- Weight assignment methodology
- Aggregation rules for final rankings

**Context factor catalog:**
- List all relevant factors from problem analysis
- Categorize factors by type and importance
- Define measurement approaches for each factor

### 4. Define Confidence Assessment Framework

"**Определяю Confidence Assessment Framework...**"

Load {evaluationCriteria} confidence framework:
- Confidence scale definition (0.0-1.0)
- Evidence strength assessment
- Analytical rigor evaluation
- Perspective balance calculation

**Confidence threshold establishment:**
- Exceptional confidence: >0.9
- High confidence: 0.8-0.9
- Moderate confidence: 0.6-0.7
- Low confidence: 0.4-0.5
- Very low confidence: <0.4

### 5. Document Analysis Framework in Report

"**Документирую complete analysis framework в consilium report...**"

Update {outputFile} with Decision Block v2.0 framework:

```markdown
## Decision Block v2.0 Analysis Framework

### Problem Definition Refinement
**Original Problem:** {from_step_1}
**Refined Scope:** {refined_scope}
**Decision Type:** {strategic/operational/tactical}

**Success Criteria Hierarchy:**
- **Must-Have (Critical):** {must_have_list}
- **Should-Have (Important):** {should_have_list}
- **Nice-to-Have (Optional):** {nice_to_have_list}

### Evidence Requirements
**Technical Evidence:** {technical_evidence_needs}
**Business Evidence:** {business_evidence_needs}
**Operational Evidence:** {operational_evidence_needs}
**Risk Evidence:** {risk_evidence_needs}

### MOE Analysis Dimensions

#### Technical Dimension
**Criteria:** Complexity, Scalability, Integration, Maintainability
**Weight:** {technical_weight}
**Measurement Approach:** {technical_measurement}

#### Business Dimension
**Criteria:** ROI, Time-to-Value, Strategic Alignment, Resources
**Weight:** {business_weight}
**Measurement Approach:** {business_measurement}

#### Operational Dimension
**Criteria:** Process Impact, Training, Support, Change Management
**Weight:** {operational_weight}
**Measurement Approach:** {operational_measurement}

#### Risk Dimension
**Criteria:** Implementation, Operational, Security, Compliance
**Weight:** {risk_weight}
**Measurement Approach:** {risk_measurement}

### Applicability Matrix Structure
**Evaluation Factors:** {factor_count} factors identified
**Scoring Scale:** 1-5 (Not Applicable to Excellent Fit)
**Confidence Levels:** 0.0-1.0 (No Confidence to Extremely High)

### Decision Quality Framework
**Overall Confidence Formula:**
```
Overall_Confidence = (Evidence_Strength × Analytical_Rigor × Perspective_Balance) ^ Adjustment_Factor
```

**Confidence Interpretation:**
- **>0.9:** Exceptional - Implement immediately
- **0.8-0.9:** High - Standard risk mitigation
- **0.7-0.8:** Good - Caution and monitoring
- **0.6-0.7:** Moderate - Pilot implementation
- **0.5-0.6:** Low - Further analysis required
- **<0.5:** Very Low - Reassess decision framework
```

### 6. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02a-decision-framework', 'step-02b-moe-matrix-setup']
progress: 35
currentPhase: 'decision-framework'
lastStep: 'step-02b-moe-matrix-setup'
decisionFrameworkEstablished: true
```

### 7. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Evidence Identification"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper framework refinement
- IF P: Execute {partyModeWorkflow} to discuss decision methodology with other agents
- IF C: Save complete framework to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#7-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and framework is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin evidence identification.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- MOE analysis framework established with all dimensions defined
- Applicability matrix template created with complete structure
- Confidence assessment framework defined with clear thresholds
- Complete analysis framework documented in consilium report
- Progress updated to 35% with established evaluation methodology

### ❌ SYSTEM FAILURE:

- MOE dimensions not fully defined or weighted incorrectly
- Applicability matrix template incomplete or structurally flawed
- Confidence framework not established with proper assessment methods
- Framework documentation missing critical components
- Methodology foundation inadequate for subsequent analysis

**Master Rule:** MOE matrix setup completes the analytical foundation - all evaluation dimensions must be properly established and documented.
