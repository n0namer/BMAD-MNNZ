---
name: 'step-04a2a-factors-establishment'
description: 'Identify context factors and establish evaluation criteria'

nextStepFile: './step-04c-matrix-preparation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
decisionFrameworks: '../data/decision-frameworks.md'
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 4a2a: Factors Establishment & Criteria Definition

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

To identify context factors comprehensively and establish evaluation criteria for systematic solution assessment.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative factor establishment, not unilateral categorization
- ✅ You bring systematic factor identification and criteria frameworks
- ✅ User brings domain insights and evaluation preferences
- ✅ Together we establish comprehensive evaluation foundation

### Step-Specific Rules:

- 🎯 Focus only on factor identification and criteria establishment
- 🚫 FORBIDDEN to prepare matrix structure or documentation yet
- 💬 Approach: Systematic factor discovery with clear evaluation criteria
- 📋 Document all factors and criteria comprehensively

## EXECUTION PROTOCOLS:

- 🎯 Identify context factors across all categories
- 💾 Establish evaluation criteria and weighting methodology
- 📖 Prepare foundation for matrix structure preparation
- 🚫 Only factors and criteria - matrix comes next

## CONTEXT BOUNDARIES:

- Available context: Solution options defined in step-4a1
- Focus: Factor identification and criteria establishment
- Limits: Do not prepare matrix structure or provide documentation
- Dependencies: Solution options foundation established

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Solution Options

"**Loading solution options from previous step...**"

Load solution options from {outputFile}:
- Options defined and categorized
- Characteristics and rationale documented
- Evaluation readiness confirmed

### 2. Identify Context Factors

"**Identifying context factors for matrix evaluation...**"

Load applicability matrix factors from {decisionFrameworks}:

**Technical Factors:**
- Complexity and technical risk
- Scalability and performance requirements
- Integration compatibility
- Maintainability and supportability

**Business Factors:**
- ROI and financial impact
- Time-to-value and implementation speed
- Strategic alignment
- Resource requirements

**Operational Factors:**
- Process impact and change management
- Training and adoption requirements
- Support overhead and maintenance
- Workflow disruption

**Risk Factors:**
- Implementation risk and challenges
- Operational risk and business continuity
- Security and compliance risk
- Financial and budgetary risk

**Factor Definition Template:**
- **Factor Name:** [Clear identifier]
- **Category:** [Technical/Business/Operational/Risk]
- **Description:** [What this factor measures]
- **Measurement Approach:** [How to assess this factor]
- **Importance Rationale:** [Why this matters for decision]

### 3. Establish Evaluation Criteria

"**Establishing evaluation criteria for each factor...**"

**Weight Bias Auditing Protocol:**
Before finalizing weights, perform validation:
1. **Independent Expert Validation:** Request 3-5 domain experts to assign weights independently
2. **Sensitivity Analysis:** Test if recommendation changes with ±15% weight variation
3. **Stakeholder Alignment Check:** Compare analyst weights with stakeholder priorities
4. **Conflict Documentation:** If weights differ >20% between experts, document reasoning

**Scoring Scale Definition:**
- **5: Excellent Fit** - Perfect alignment, optimal solution
- **4: Good Fit** - Strong alignment, minor optimizations needed
- **3: Acceptable Fit** - Moderate fit, some adjustments required
- **2: Poor Fit** - Significant challenges, major changes needed
- **1: Not Applicable** - Incompatible, not feasible

**Weight Assignment Methodology:**
- Strategic factors: Higher weights (business alignment, risk impact)
- Operational factors: Medium weights (process impact, resource needs)
- Technical factors: Context-dependent weights based on problem type

**Criteria Establishment Process:**
1. **Factor Importance Assessment:** Rate each factor's importance to success
2. **Weight Calculation:** Assign relative weights based on importance
3. **Scale Calibration:** Ensure consistent interpretation across factors
4. **Validation Check:** Verify weights sum appropriately and reflect priorities

### 4. Document Factors and Criteria

"**Documenting factors and criteria establishment...**"

Create intermediate documentation:

**Context Factors Established:**
- **Technical Factors:** [list with descriptions and measurement approaches]
- **Business Factors:** [list with descriptions and measurement approaches]
- **Operational Factors:** [list with descriptions and measurement approaches]
- **Risk Factors:** [list with descriptions and measurement approaches]

**Evaluation Criteria Defined:**
- **Scoring Scale:** 1-5 (Not Applicable to Excellent Fit)
- **Weight Assignment:** [methodology and ranges]
- **Factor Weights:** [list factors with assigned weights]
- **Validation Status:** [weights validated and priorities reflected]

### 5. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation', 'step-04a1-solution-options', 'step-04a2a-factors-establishment']
progress: 47
currentPhase: 'factors-establishment'
lastStep: 'step-04a2a-factors-establishment'
factorsEstablishmentComplete: true
```

### 6. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Matrix Preparation"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper factor exploration
- IF P: Execute {partyModeWorkflow} to discuss factors and criteria with other agents
- IF C: Save factors and criteria to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#6-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and factors/criteria are saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin matrix preparation.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Context factors comprehensively identified across all categories
- Evaluation criteria established with clear scoring methodology
- Weight assignments completed and priorities reflected
- Factors and criteria documented with measurement approaches
- Progress updated to 47% with evaluation foundation established

### ❌ SYSTEM FAILURE:

- Context factors not comprehensively identified or categorized
- Evaluation criteria not established with clear scales or methodology
- Weight assignments missing or not reflecting priorities
- Documentation inadequate or missing critical elements
- Foundation not properly established for matrix preparation

**Master Rule:** Factors establishment creates the evaluation framework - all factors must be clearly identified and criteria properly defined.
