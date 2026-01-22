---
name: 'step-05b1-confidence-synthesis'
description: 'Synthesize evaluation results and calculate overall confidence for solution selection'

nextStepFile: './step-05d-final-documentation.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
solutionSelectionTemplates: '../data/solution-selection-templates.md'
---

# Step 5b1: Confidence Synthesis & Recommendation

## STEP GOAL:

To synthesize evaluation results, calculate overall confidence, and develop comprehensive solution recommendation with evidence-based rationale.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are an EMBER Consilium Analyst
- ✅ We engage in collaborative synthesis, not unilateral decision making
- ✅ You bring evidence-based synthesis frameworks and confidence methodologies
- ✅ User brings final validation and solution preferences
- ✅ Together we develop confidence-validated recommendations

### Step-Specific Rules:

- 🎯 Focus only on confidence calculation and recommendation synthesis
- 🚫 FORBIDDEN to provide implementation details or final documentation yet
- 💬 Approach: Evidence-based synthesis with transparent confidence scoring
- 📋 Document confidence calculation and recommendation rationale

## EXECUTION PROTOCOLS:

- 🎯 Synthesize evaluation results with overall confidence calculation
- 💾 Develop solution recommendation with comprehensive justification
- 📖 Prepare foundation for final documentation
- 🚫 Only synthesis - final documentation comes next

## CONTEXT BOUNDARIES:

- Available context: Complete solution evaluation from step-5a
- Focus: Confidence calculation and recommendation synthesis
- Limits: Do not provide implementation details or complete documentation
- Dependencies: Evaluation foundation and decision framework established

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Review Evaluation Results

"**Просматриваю evaluation results для final synthesis...**"

Load evaluation results from {outputFile} and step-5a:

**Evaluation Summary:**
- Success criteria compliance scores
- Risk-adjusted value calculations
- Decision quality validation metrics
- Alternative options assessment

**Synthesis Preparation:**
- Validate evaluation completeness
- Confirm data quality and consistency
- Prepare confidence calculation inputs

### 2. Calculate Overall Confidence

"**Рассчитываю overall confidence для final recommendation...**"

Load confidence calculation template from {solutionSelectionTemplates}:

**CRITICAL: Psychological Bias Warning**

Research shows decision confidence exhibits systematic biases:
1. **Disconfirmatory Evidence Bias:** Late-arriving conflicting evidence disproportionately reduces confidence
2. **Overconfidence in 50/50 Choices:** Near-tie decisions often reported as 75% confidence
3. **Anchoring Bias:** Early confidence estimates persist despite new evidence

**Bias Mitigation Protocol:**
- If conflicting evidence found in final 20% of analysis: Re-assess entire evidence base
- If top 2 options score within 0.3 points: Flag as "statistically indiscriminable"
- If confidence > 0.85 with <5 high-quality sources: Reduce confidence by 0.10 (overconfidence correction)

**Final Confidence Calculation:**

**Point Estimate (NOT RECOMMENDED FOR FINAL USE):**
```
Point_Confidence = (Evidence_Strength × 0.4) + (Analytical_Rigor × 0.3) + (Perspective_Balance × 0.3)
= [calculation_result]
```

**Confidence Range (RECOMMENDED):**
```
Lower_Bound = Point_Confidence - Uncertainty_Factor
Upper_Bound = Point_Confidence + Uncertainty_Factor

Uncertainty_Factor = 0.10 (baseline) + Evidence_Gap_Penalty + Conflict_Penalty
  - Evidence_Gap_Penalty: +0.05 per evidence category with gaps
  - Conflict_Penalty: +0.03 per unresolved stakeholder conflict

Example:
Point_Confidence = 0.75
Evidence_Gap_Penalty = 0.05 (1 category gap)
Conflict_Penalty = 0.03 (1 stakeholder conflict)
Uncertainty_Factor = 0.10 + 0.05 + 0.03 = 0.18

Final Confidence Range: 0.57 - 0.93 (point estimate: 0.75)
```

**Confidence Level:** [lower_bound] - [upper_bound] (point: [score]) ([rating])
**Uncertainty Drivers:** [list factors contributing to uncertainty]

Confidence Assessment Components:

Overall Confidence Assessment:
- Evidence Strength: [score/5] - quality and quantity of sources
- Analytical Rigor: [score/5] - methodology clarity
- Perspective Balance: [score/5] - stakeholder representation

Adjustment Factors:
- Evidence Gap Penalty: [if applicable]
- MCP Conflict Penalty: [if applicable]
- Stakeholder Misalignment Penalty: [if applicable]
- Near-Tie Penalty: [if applicable]
- Overconfidence Correction: [if applicable]

Confidence Interpretation:
- 90-100%: Exceptional confidence (implement immediately)
- 80-89%: High confidence (standard contingency)
- 70-79%: Moderate-high confidence (detailed contingency)
- 60-69%: Moderate confidence (intensive contingency)
- 50-59%: Moderate-low confidence (reduce scope/scale)
- 40-49%: Low confidence (RECOMMEND: Additional analysis)
- <40%: Very low confidence (DO NOT PROCEED)

What Would Increase Confidence to [Higher]%:
- [Action 1]: [What additional research/validation?]
- [Action 2]: [What additional evidence?]

What Would Reduce Confidence to [Lower]%:
- [Risk 1]: If [scenario occurs] → confidence drops to [X]%
- [Risk 2]: If [scenario occurs] → confidence drops to [X]%

### 3. Synthesize Final Recommendation

"**Синтезирую final recommendation с comprehensive rationale...**"

**Recommendation Structure:**
- **Selected Solution**: Primary recommendation with confidence score
- **Rationale**: Evidence-based justification for selection
- **Critical Assumptions**: Key dependencies and assumptions
- **Risk Considerations**: Major risks and mitigation approaches

**Recommendation Validation:**
- Aligns with success criteria and evaluation results
- Supported by strongest quantitative evidence
- Balances risk and reward appropriately
- Achieves optimal confidence-to-complexity ratio

### 4. Document Synthesis Results

"**Документирую synthesis results в consilium report...**"

Update {outputFile} with synthesis analysis:

```markdown
## Solution Selection & Final Recommendation

### Overall Confidence Assessment

#### Confidence Calculation Components
- **Evidence Strength:** [score]/5 ([contribution_factors])
- **Analytical Rigor:** [score]/5 ([methodology_factors])
- **Perspective Balance:** [score]/5 ([dimension_balance])
- **Adjustment Factor:** [factor] ([contextual_factors])

#### Final Confidence Score: [overall_score]/1.0
**Interpretation:** [Exceptional/High/Good/Moderate/Low/Very Low Confidence]
**Recommendation:** [implement immediately/with standard mitigation/with caution/as pilot/further analysis/reassess framework]

### Primary Recommendation Synthesis

#### 🏆 **RECOMMENDED SOLUTION: [Solution Name]**

**Solution Overview:** [Detailed description of recommended approach]

**Confidence Validation:** [How confidence score supports this recommendation]

**Critical Success Factors:**
1. **[Factor 1]:** [description] - Evidence: [supporting_data] - Impact: [significance]
2. **[Factor 2]:** [description] - Evidence: [supporting_data] - Impact: [significance]
3. **[Factor 3]:** [description] - Evidence: [supporting_data] - Impact: [significance]

**Key Assumptions:**
1. **[Assumption 1]:** [description] - Validation: [evidence] - Risk if invalid: [impact]
2. **[Assumption 2]:** [description] - Validation: [evidence] - Risk if invalid: [impact]

**Risk Mitigation Priorities:**
1. **[Risk 1]:** [mitigation_strategy] - Effectiveness: [expected_reduction] - Cost: [resource_requirement]
2. **[Risk 2]:** [mitigation_strategy] - Effectiveness: [expected_reduction] - Cost: [resource_requirement]
```

### 5. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation', 'step-04a-matrix-setup', 'step-04b1-weighted-scoring', 'step-04b2-final-rankings', 'step-05a1-criteria-validation', 'step-05a2-decision-validation', 'step-05b1-confidence-synthesis']
progress: 72
currentPhase: 'confidence-synthesis'
lastStep: 'step-05b1-confidence-synthesis'
confidenceSynthesisComplete: true
```

### 6. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Final Documentation"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper synthesis analysis
- IF P: Execute {partyModeWorkflow} to discuss synthesis results with other agents
- IF C: Save synthesis results to {outputFile}, update frontmatter stepsCompleted, then only then load, read entirely, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#6-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and synthesis results are saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin final documentation.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Evaluation results properly synthesized with overall confidence calculation
- Solution recommendation developed with comprehensive justification
- Confidence score calculated with all required components
- Synthesis results documented with transparent methodology
- Progress updated to 72% with recommendation foundation established

### ❌ SYSTEM FAILURE:

- Confidence calculation missing or incorrect components
- Recommendation synthesis inadequate or poorly justified
- Evidence synthesis incomplete or superficial
- Documentation inadequate or missing

**Master Rule:** Confidence synthesis provides decision foundation - all calculations must be mathematically sound and evidence-based.
