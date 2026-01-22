---
name: 'step-04b2b2-results-documentation'
description: 'Document comprehensive evaluation outcomes and complete matrix evaluation'

nextStepFile: './step-05a-criteria-validation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
decisionFrameworks: '../data/decision-frameworks.md'
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 4b2b2: Results Documentation & Completion

## STEP GOAL:

To document comprehensive evaluation outcomes in the consilium report and complete the matrix evaluation phase.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative documentation completion, not unilateral finalization
- ✅ You bring documentation frameworks and completion methodologies
- ✅ User brings documentation preferences and completion validation
- ✅ Together we finalize comprehensive evaluation documentation

### Step-Specific Rules:

- 🎯 Focus only on documentation and phase completion (not new analysis)
- 🚫 FORBIDDEN to perform additional validation or new calculations
- 💬 Approach: Comprehensive documentation with transparent completion
- 📋 Document evaluation outcomes and complete matrix phase

## EXECUTION PROTOCOLS:

- 🎯 Document comprehensive evaluation outcomes
- 💾 Complete matrix evaluation phase
- 📖 Finalize evaluation documentation
- 🚫 Only documentation - new phases come next

## CONTEXT BOUNDARIES:

- Available context: Validation assessment completed
- Focus: Documentation completion and phase finalization
- Limits: Do not perform new validation or analysis
- Dependencies: Validation foundation established

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Validation Assessment

"**Загружаю validation assessment из предыдущего шага...**"

Load validation data from {outputFile}:
- Quality metrics calculated
- Stability assessment completed
- Validation foundation confirmed

### 2. Document Matrix Results

"**Документирую comprehensive matrix evaluation results в consilium report...**"

Update {outputFile} with complete applicability matrix analysis:

```markdown
## Applicability Matrix Evaluation Results

### Solution Options Evaluated
1. **Option A:** [Description] - [Key characteristics]
2. **Option B:** [Description] - [Key characteristics]
3. **Option C:** [Description] - [Key characteristics]

### Context Factors Assessed
**Total Factors:** [count]
**Factor Categories:** Technical ([count]), Business ([count]), Operational ([count]), Risk ([count])

### Evaluation Criteria Applied
**Scoring Scale:** 1-5 (Not Applicable to Excellent Fit)
**Weight Range:** 1-5 (Supporting to Critical)
**Confidence Scale:** 0.0-1.0 (No Confidence to Extremely High)

### Applicability Matrix Results

| Factor | Weight | Option A | Option B | Option C |
|--------|--------|----------|----------|----------|
| **Technical Complexity** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |
| **Scalability Requirements** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |
| **Integration Compatibility** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |
| **Business ROI** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |
| **Time-to-Value** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |
| **Strategic Alignment** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |
| **Process Impact** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |
| **Training Requirements** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |
| **Implementation Risk** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |
| **Operational Risk** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |
| **Security Risk** | [weight] | [score] ([confidence]) | [score] ([confidence]) | [score] ([confidence]) |

**Notes:**
- Scores in parentheses indicate confidence levels (0.0-1.0)
- Higher scores indicate better fit for the factor
- Confidence levels adjust final rankings

### Weighted Score Calculations

#### Base Weighted Scores (before confidence adjustment)
- **Option A:** [weighted_score] (Rank: [position])
- **Option B:** [weighted_score] (Rank: [position])
- **Option C:** [weighted_score] (Rank: [position])

#### Confidence-Adjusted Scores
- **Option A:** [adjusted_score] (Confidence: [average_confidence])
- **Option B:** [adjusted_score] (Confidence: [average_confidence])
- **Option C:** [adjusted_score] (Confidence: [average_confidence])

### Final Rankings

#### 🥇 Primary Ranking: Option [A/B/C]
**Adjusted Score:** [score]
**Average Confidence:** [confidence]
**Key Strengths:**
- [Strength 1 with factor correlation]
- [Strength 2 with factor correlation]
- [Strength 3 with factor correlation]

**Critical Success Factors:**
- [Factor 1]: [performance_level] - [impact_on_success]
- [Factor 2]: [performance_level] - [impact_on_success]

#### 🥈 Secondary Ranking: Option [A/B/C]
**Adjusted Score:** [score]
**Average Confidence:** [confidence]
**Key Differentiators:**
- [Advantage over primary]
- [Advantage over primary]

#### 🥉 Tertiary Ranking: Option [A/B/C]
**Adjusted Score:** [score]
**Average Confidence:** [confidence]
**Consideration Factors:**
- [Situations where this might be preferred]

### Factor Performance Analysis

#### Best Performing Factors
1. **[Factor Name]:** [top_scorer] (Score: [score])
   - Rationale: [why this factor scored highly]
   - Impact: [influence on overall ranking]

#### Most Discriminating Factors
1. **[Factor Name]:** Separated winners from others
   - Winner Score: [score], Others Average: [average]
   - Weight: [weight] (Critical/Important/Supporting)

#### Areas of Lowest Confidence
1. **[Factor Name]:** Average confidence [level]
   - Sources of uncertainty: [reasons]
   - Potential impact on ranking: [assessment]

### Matrix Validation Summary

#### Evaluation Quality Metrics
- **Factors with High Confidence (>0.8):** [count]/[total] ([percentage]%))
- **Factors with Medium Confidence (0.6-0.8):** [count]/[total] ([percentage]%))
- **Factors with Low Confidence (<0.6):** [count]/[total] ([percentage]%)))

#### Ranking Stability Assessment
- **Primary Ranking Confidence:** [high/medium/low]
- **Gap Between Top Two Options:** [score_difference]
- **Sensitivity to Weight Changes:** [stable/moderate/sensitive]

### Recommendations for Next Steps
- **Immediate:** [actions based on matrix results]
- **Further Analysis:** [areas needing additional evaluation]
- **Decision Timeline:** [recommended timeframe for final selection]
```

### 3. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation', 'step-04a-matrix-setup', 'step-04b1-weighted-scoring', 'step-04b2a-ranking-calculation', 'step-04b2b1-validation-assessment', 'step-04b2b2-results-documentation']
progress: 60
currentPhase: 'matrix-evaluation'
lastStep: 'step-04b2b2-results-documentation'
matrixEvaluationComplete: true
```

### 4. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Criteria Validation"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper matrix analysis
- IF P: Execute {partyModeWorkflow} to discuss evaluation results with other agents
- IF C: Save matrix evaluation to {outputFile}, update frontmatter stepsCompleted, then only then load, read entirely {nextStepFile} to execute and begin criteria validation
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#4-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and matrix evaluation is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin criteria validation.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Evaluation outcomes documented with complete transparency
- Matrix evaluation phase completed comprehensively
- Documentation finalized with all evaluation results
- Progress updated to 60% with matrix evaluation finalized

### ❌ SYSTEM FAILURE:

- Documentation incomplete or lacking transparency
- Evaluation outcomes not comprehensively documented
- Phase completion inadequate or missing components
- Results documentation inadequate or insufficient

**Master Rule:** Results documentation provides complete evaluation record - all outcomes must be transparently documented and phase properly completed.

