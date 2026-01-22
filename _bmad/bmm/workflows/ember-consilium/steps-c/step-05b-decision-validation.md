---
name: 'step-05a2-decision-validation'
description: 'Perform decision quality validation and alternative options assessment'

nextStepFile: './step-05c-confidence-synthesis.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
solutionSelectionTemplates: '../data/solution-selection-templates.md'
---

# Step 5a2: Decision Quality Validation

## STEP GOAL:

To perform comprehensive decision quality validation, assess stakeholder alignment, and evaluate alternative options for final solution evaluation preparation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative quality assessment, not unilateral validation
- ✅ You bring decision quality frameworks and stakeholder analysis
- ✅ User brings domain insights and stakeholder perspectives
- ✅ Together we validate decision robustness and completeness

### Step-Specific Rules:

- 🎯 Focus only on decision quality validation and alternatives assessment
- 🚫 FORBIDDEN to make final solution selection yet
- 💬 Approach: Comprehensive quality assessment with stakeholder alignment
- 📋 Document validation metrics and alternative comparisons

## EXECUTION PROTOCOLS:

- 🎯 Perform comprehensive decision quality validation
- 💾 Assess stakeholder alignment and evidence strength
- 📖 Evaluate alternative options systematically
- 🚫 Only validation - final selection comes next

## CONTEXT BOUNDARIES:

- Available context: Criteria validation and risk assessment completed
- Focus: Decision quality validation and alternative options assessment
- Limits: Do not make final solution selection or recommendations
- Dependencies: Quantitative validation foundation established

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Validation Results

"**Загружаю validation results из предыдущего шага...**"

Load criteria validation and risk assessment results from {outputFile}:
- Success criteria compliance scores
- Risk-adjusted value calculations
- Validation foundation established

### 2. Perform Decision Quality Validation

"**Валидирую quality of decision-making process...**"

**Evidence Base Strength:**
- **Total Evidence Sources:** [count]
- **High-Quality Sources:** [count] ([percentage]%)
- **Supporting Citations:** [count] references
- **Cross-Validation:** [consistency_assessment]

**Analytical Rigor Assessment:**
- **Methodology Consistency:** [score]/5
- **Bias Mitigation:** [score]/5
- **Assumption Transparency:** [score]/5
- **Peer Review Potential:** [score]/5

**Stakeholder Alignment:**
- **Decision Sponsor:** [support_level] ([rationale])
- **Implementation Team:** [support_level] ([rationale])
- **End Users:** [support_level] ([rationale])
- **Overall Alignment:** [score]/5

### MANDATORY SEQUENCE - 2. Perform Decision Quality Validation

Stakeholder Conflict Resolution:

IF alignment-variance > 30% THEN
├─ CONFLICT DETECTED
├─ Conflict Resolution Protocol:
│  1. Identify decision authority: Who has final say?
│  2. Document disagreement points: List specific conflicts
│  3. Assess stakeholder influence: Weight by impact on success
│  4. Facilitate alignment meeting: Structured discussion required
│  5. Resolution strategy:
│     ├─ Consensus approach
│     ├─ Authority override (with dissent documented)
│     └─ Hybrid approach (accommodate some concerns)
│
└─ Document Resolution:
   - Conflicts detected: [count + severity]
   - Resolution approach: [method used]
   - Final decision authority: [role/person]
   - Dissenting stakeholders: [list with concerns]

ELSE
└─ ALIGNMENT SUFFICIENT - Proceed with recommendation

**Stakeholder Conflict Status:**
- Conflicts detected: [count] ([severity])
- Resolution approach: [method used]
- Final decision authority: [role/person]
- Dissenting stakeholders: [list with concerns]

### 3. Evaluate Alternative Options

"**Оцениваю alternative options для comparison...**"

Compare top 3 options from matrix evaluation:

Primary vs Secondary Comparison:
- Performance Gap: [score difference]
- Risk Differential: [risk comparison]
- Confidence Differential: [confidence comparison]
- Switching Considerations: [ease of change]
- Time Required: [days/weeks]
- Cost Impact: [budget impact]

Secondary vs Tertiary Comparison:
- Performance Gap: [score difference]
- Risk Differential: [risk comparison]
- Use Case Differentiation: [optimal scenarios]

Evaluation Summary:
- Primary Recommendation: [option name]
- Compliance Score: [X/5]
- Compliance Status: [%]
- Risk-Adjusted Value: [value rating]
- Calculation: [result]
- Confidence in Evaluation: [high/medium/low]
- Alternative Options: [count viable alternatives]
- Decision Readiness: [ready/not ready] for final selection

### 4. Document Evaluation Results

"**Документирую comprehensive evaluation results...**"

Update {outputFile} with complete evaluation analysis:

```markdown
## Solution Evaluation Results

### Decision Quality Validation

#### Evidence Base Strength
- **Total Evidence Sources:** [count]
- **High-Quality Sources:** [count] ([percentage]%)
- **Supporting Citations:** [count] references
- **Cross-Validation:** [consistency_assessment]

#### Analytical Rigor Assessment
- **Methodology Consistency:** [score]/5
- **Bias Mitigation:** [score]/5
- **Assumption Transparency:** [score]/5
- **Peer Review Potential:** [score]/5

#### Stakeholder Alignment
- **Decision Sponsor:** [support_level] ([rationale])
- **Implementation Team:** [support_level] ([rationale])
- **End Users:** [support_level] ([rationale])
- **Overall Alignment:** [score]/5

### Alternative Options Assessment

#### Primary vs Secondary Comparison
- **Performance Gap:** [score_difference]
- **Risk Differential:** [risk_comparison]
- **Confidence Differential:** [confidence_comparison]
- **Switching Considerations:** [ease_of_change] - [time_required] - [cost_impact]

#### Secondary vs Tertiary Comparison
- **Performance Gap:** [score_difference]
- **Risk Differential:** [risk_comparison]
- **Use Case Differentiation:** [optimal_scenarios]

### Evaluation Summary
- **Primary Recommendation:** [option_name] - [compliance_score]/5 compliance
- **Risk-Adjusted Value:** [value_rating] - [calculation_result]
- **Confidence in Evaluation:** [high/medium/low]
- **Alternative Options:** [count] viable alternatives identified
- **Decision Readiness:** [ready/not_ready] for final selection
```

### 5. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation', 'step-04a-matrix-setup', 'step-04b1-weighted-scoring', 'step-04b2-final-rankings', 'step-05a1-criteria-validation', 'step-05a2-decision-validation']
progress: 70
currentPhase: 'solution-evaluation'
lastStep: 'step-05a2-decision-validation'
solutionEvaluationComplete: true
```

### 6. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Solution Selection"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper evaluation analysis
- IF P: Execute {partyModeWorkflow} to discuss evaluation findings with other agents
- IF C: Save evaluation results to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#6-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and evaluation results are saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin final solution selection.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Decision quality validation completed across all dimensions
- Stakeholder alignment assessment performed comprehensively
- Alternative options evaluated and compared systematically
- Comprehensive evaluation results documented in consilium report
- Progress updated to 70% with evaluation foundation established

### ❌ SYSTEM FAILURE:

- Decision quality validation incomplete or missing
- Stakeholder alignment not assessed systematically
- Alternative comparison superficial or missing
- Evaluation documentation inadequate or missing

**Master Rule:** Decision validation provides quality assurance foundation - all assessments must be comprehensive and stakeholder-informed.
