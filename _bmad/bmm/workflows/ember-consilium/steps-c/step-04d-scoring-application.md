---
name: 'step-04b1a-scoring-application'
description: 'Apply weighted scoring formulas and confidence adjustments to solutions'

nextStepFile: './step-04e-scoring-validation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
decisionFrameworks: '../data/decision-frameworks.md'
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 4b1a: Scoring Application & Adjustments

## STEP GOAL:

To apply weighted scoring formulas and confidence adjustments to solution evaluations for quantitative assessment foundation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative quantitative application, not unilateral calculations
- ✅ You bring scoring formulas and confidence adjustment frameworks
- ✅ User brings scoring judgments and confidence assessments
- ✅ Together we produce transparent quantitative foundation

### Step-Specific Rules:

- 🎯 Focus only on scoring formula application and confidence adjustments
- 🚫 FORBIDDEN to perform validation or documentation yet
- 💬 Approach: Systematic mathematical application with clear rationale
- 📋 Document all formulas, inputs, and adjustment rationales

## EXECUTION PROTOCOLS:

- 🎯 Apply weighted scoring formulas to all solutions
- 💾 Calculate confidence adjustments with documented rationale
- 📖 Prepare quantitative results for validation phase
- 🚫 Only calculations - validation comes next

## CONTEXT BOUNDARIES:

- Available context: Matrix framework established in step-4a
- Focus: Mathematical formula application and confidence calibration
- Limits: Do not perform validation or provide documentation
- Dependencies: Matrix setup completed with evaluation criteria defined

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Matrix Framework

"**Загружаю matrix framework из предыдущего шага...**"

Load matrix setup data from {outputFile}:
- Solution options defined
- Context factors established
- Evaluation criteria confirmed
- Weight assignments validated

**Framework Validation:**
- All required elements present
- Structure matches expectations
- Data quality sufficient for evaluation

### 2. Apply Weighted Scoring

"**Применяю weighted scoring к matrix results...**"

**Weighted Score Calculation:**
For each solution, calculate:
```
Weighted_Score = Σ(Factor_Score × Factor_Weight) / Σ(Weights)
```

**Weight Categories Applied:**
- **Critical Factors** (weight: 3-5): Business alignment, risk impact, success criteria
- **Important Factors** (weight: 2-3): Technical feasibility, resource requirements
- **Supporting Factors** (weight: 1-2): Operational preferences, minor considerations

**Scoring Process:**
- Evaluate each solution against every factor
- Apply appropriate weights to each factor score
- Calculate weighted averages for each solution
- Document scoring rationale for transparency

**Calculation Template:**
```
Solution [X] Weighted Score:
= (Factor1_Score × Factor1_Weight) + (Factor2_Score × Factor2_Weight) + ... + (FactorN_Score × FactorN_Weight)
÷ (Factor1_Weight + Factor2_Weight + ... + FactorN_Weight)
= [numerator] ÷ [denominator] = [weighted_score]
```

### 3. Apply Confidence Adjustments

"**Применяю confidence adjustments к scores...**"

Load confidence framework from {evaluationCriteria}:

**Confidence Adjustment Formula:**
```
Adjusted_Score = Base_Score × Confidence_Level
```

**Confidence Levels Applied:**
- **High (0.8-1.0)**: Strong evidence, reliable assessment
- **Medium (0.6-0.8)**: Reasonable evidence, some uncertainty
- **Low (0.4-0.6)**: Limited evidence, significant uncertainty

**Adjustment Application:**
- Reduce scores for low-confidence evaluations
- Increase scores for high-confidence validations
- Document confidence rationale for each adjustment
- Maintain audit trail of all confidence judgments

**Adjustment Template:**
```
Solution [X] Confidence Adjustment:
Base_Weighted_Score: [score]
Confidence_Level: [level] ([rationale])
Adjusted_Score = [base_score] × [confidence] = [adjusted_score]
Adjustment_Impact: [increase/decrease] of [percentage]%
```

### 4. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation', 'step-04a-matrix-setup', 'step-04b1a-scoring-application']
progress: 52
currentPhase: 'scoring-application'
lastStep: 'step-04b1a-scoring-application'
scoringApplicationComplete: true
```

### 5. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Scoring Validation"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper scoring analysis
- IF P: Execute {partyModeWorkflow} to discuss scoring applications with other agents
- IF C: Save scoring application to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#5-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and scoring application is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin scoring validation.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Weighted scoring formulas applied systematically to all solutions
- Confidence adjustments calculated with clear rationale for all evaluations
- Mathematical accuracy maintained throughout calculations
- Audit trails established for all scoring applications
- Progress updated to 52% with quantitative foundation established

### ❌ SYSTEM FAILURE:

- Weighted scoring not applied correctly or incomplete
- Confidence adjustments missing rationale or incorrectly calculated
- Mathematical errors in formula application
- Audit trails not maintained or insufficient
- Calculation transparency inadequate

**Master Rule:** Scoring application provides mathematical foundation - all formulas must be correctly applied and transparently documented.

