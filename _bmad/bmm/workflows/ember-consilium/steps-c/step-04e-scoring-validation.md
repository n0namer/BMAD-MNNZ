---
name: 'step-04b1b-scoring-validation'
description: 'Validate scoring calculations and document quantitative results'

nextStepFile: './step-04f-ranking-calculation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
decisionFrameworks: '../data/decision-frameworks.md'
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 4b1b: Scoring Validation & Documentation

## STEP GOAL:

To validate scoring calculations for accuracy and document comprehensive quantitative results for evaluation foundation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative validation and documentation, not unilateral verification
- ✅ You bring validation frameworks and documentation methodologies
- ✅ User brings validation insights and documentation preferences
- ✅ Together we complete transparent quantitative foundation

### Step-Specific Rules:

- 🎯 Focus only on validation and documentation of scoring results
- 🚫 FORBIDDEN to perform new calculations or ranking yet
- 💬 Approach: Comprehensive validation with transparent documentation
- 📋 Document all validation metrics and quantitative outcomes

## EXECUTION PROTOCOLS:

- 🎯 Validate scoring calculations for mathematical accuracy
- 💾 Document comprehensive quantitative results
- 📖 Complete scoring phase and prepare for ranking
- 🚫 Only validation - rankings come next

## CONTEXT BOUNDARIES:

- Available context: Scoring formulas applied and confidence adjustments calculated
- Focus: Calculation validation and comprehensive documentation
- Limits: Do not perform new calculations or ranking analysis
- Dependencies: Scoring application completed with quantitative results

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Scoring Results

"**Загружаю scoring results из предыдущего шага...**"

Load scoring application data from {outputFile}:
- Weighted scores calculated
- Confidence adjustments applied
- Mathematical accuracy verified
- Audit trails maintained

### 2. Validate Scoring Calculations

"**Валидирую scoring calculations для accuracy...**"

**Calculation Validation:**
- Verify all factors included in scoring
- Confirm weight assignments applied correctly
- Validate mathematical accuracy of calculations
- Cross-check confidence adjustment applications

**Audit Trail Requirements:**
- All formulas documented with inputs
- Intermediate calculations preserved
- Rationale for confidence adjustments recorded
- Source data traceability maintained

### 3. Document Scoring Results

"**Документирую weighted scoring results...**"

Update {outputFile} with scoring calculations:

```markdown
## Weighted Scoring & Confidence Adjustments

### Scoring Methodology Applied

#### Weighted Score Formula
```
Weighted_Score = Σ(Factor_Score × Factor_Weight) / Σ(Weights)
```

#### Confidence Adjustment Formula
```
Adjusted_Score = Base_Score × Confidence_Level
```

### Weight Categories Applied
- **Critical Factors** (weight: 3-5): [list factors]
- **Important Factors** (weight: 2-3): [list factors]
- **Supporting Factors** (weight: 1-2): [list factors]

### Solution Scoring Calculations

#### Option A: [Solution Name]
**Base Weighted Score Calculation:**
```
= (Factor1: [score] × [weight]) + (Factor2: [score] × [weight]) + ... + (FactorN: [score] × [weight])
÷ ([weight1] + [weight2] + ... + [weightN])
= [numerator] ÷ [denominator] = [weighted_score]
```

**Confidence Adjustment:**
```
Base Score: [weighted_score]
Confidence Level: [level] ([rationale])
Adjusted Score = [base_score] × [confidence] = [adjusted_score]
```

#### Option B: [Solution Name]
[... same calculation structure ...]

#### Option C: [Solution Name]
[... same calculation structure ...]

### Scoring Validation Summary
- **Total Factors Evaluated:** [count]
- **Weight Sum Validation:** [expected vs actual]
- **Confidence Range Check:** All values within 0.0-1.0 range
- **Mathematical Accuracy:** [verified/not verified]
- **Audit Trail:** [complete/incomplete]

### Confidence Adjustment Summary
- **High Confidence Adjustments (>0.8):** [count] applications
- **Medium Confidence Adjustments (0.6-0.8):** [count] applications
- **Low Confidence Adjustments (<0.6):** [count] applications
- **Average Confidence Level:** [score]/1.0
- **Most Impactful Adjustment:** [solution] - [impact_percentage]% change
```

### 4. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation', 'step-04a-matrix-setup', 'step-04b1a-scoring-application', 'step-04b1b-scoring-validation']
progress: 55
currentPhase: 'weighted-scoring'
lastStep: 'step-04b1b-scoring-validation'
weightedScoringComplete: true
```

### 5. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Ranking Calculation"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper scoring validation
- IF P: Execute {partyModeWorkflow} to discuss scoring validation with other agents
- IF C: Save scoring validation to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#5-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and scoring validation is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin ranking calculations.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Scoring calculations validated for mathematical accuracy
- Audit trails verified for completeness and traceability
- Quantitative results comprehensively documented
- Validation completed with transparent methodology
- Progress updated to 55% with validated scoring foundation

### ❌ SYSTEM FAILURE:

- Calculation validation incomplete or inadequate
- Audit trails not verified or insufficient
- Documentation incomplete or lacking transparency
- Validation methodology not properly applied
- Results documentation inadequate

**Master Rule:** Scoring validation ensures quantitative integrity - all calculations must be verified and transparently documented.

