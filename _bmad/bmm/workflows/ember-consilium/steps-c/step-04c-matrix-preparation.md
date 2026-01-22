---
name: 'step-04a2b-matrix-preparation'
description: 'Prepare matrix structure and document evaluation framework (ENFORCEMENT VERSION)'

nextStepFile: './step-04d-scoring-application.md'
outputFile: '{output_folder}/ember-consilium-{user_name}-{date}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data references
decisionFrameworks: '../data/decision-frameworks.md'
evaluationCriteria: '../data/evaluation-criteria.md'
---

# Step 4a2b: Matrix Preparation & Framework Documentation (ENFORCEMENT VERSION)

## STEP GOAL:

Prepare and document the matrix structure and evaluation framework with strict enforcement of self-validation, anti-violation, GAP/FAIL-fast and confidence protocols. No aspect may be left ambiguous — success/failure logic must be explicit.

## MANDATORY ENFORCEMENT RULES

### ANTI-VIOLATION / CRITICAL GATES

- 🛑 NEVER proceed unless all matrix elements (options, factors, criteria) are explicitly defined and validated.
- ⚠️ For every gap in options/factors/criteria template, you MUST flag and annotate GAP/FAIL and reduce framework confidence.
- DUALLY LOG every skipped or partially-filled section as explicit ENFORCEMENT FAILURE.
- 📋 YOU ARE AN ENFORCEMENT AGENT — Facilitation is secondary; primary duty is completeness, traceability, and self-audit.

### SELF-VALIDATION CHECKLIST

- [ ] All solution options explicitly listed (no placeholders, no "TBD")
- [ ] All context factors fully named and categorized, no empty entries
- [ ] Every evaluation criterion (scale, weight, confidence) specified
- [ ] Matrix template includes row for rationale and GAP/FAIL flags
- [ ] "Framework Confidence" explicitly scored; reductions must be tallied (at least -20% for 1+ critical GAPs)
- [ ] Scoring is OFF in this step; preparation only

---

## EXECUTION PROTOCOLS:

- 🎯 Prepare matrix structure with templates and methodology
- 💾 Document complete evaluation framework in consilium report
- 📖 Complete matrix setup phase and prepare for scoring
- 🚫 Only preparation and documentation - scoring comes next

## CONTEXT BOUNDARIES:

- Available context: Factors and criteria established in step-4a2a
- Focus: Matrix structure preparation and framework documentation
- Limits: Do not perform scoring or provide recommendations
- Dependencies: Factors and criteria foundation established

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Factors and Criteria

"**Загружаю factors and criteria из предыдущего шага...**"

Load factors and criteria from {outputFile}:
- Context factors identified and categorized
- Evaluation criteria established with weights
- Measurement approaches defined

### 2. Prepare Matrix Structure

"**Подготавливаю matrix structure для evaluation...**"

**Matrix Structure Definition:**
```
Factors (Rows) × Solutions (Columns)
Each cell: Score (1-5) + Confidence (0.0–1.0) + Rationale
Rows: All factors; Columns: All solution options; Last row: GAP/FAIL flag per column; "Framework Confidence": explicit value/adjustment.
```

**ENFORCEMENT Matrix Preparation Checklist:**
- [ ] Solution options enumerated with NO blanks or TBA entries
- [ ] Context factors fully categorized with 0 empty fields
- [ ] All criteria (scales, weights, confidence processes) defined
- [ ] For each missing, ambiguous, or placeholder item: GAP/FAIL flag (see table)
- [ ] Framework Confidence annotated: penalties applied for all gaps
- [ ] Matrix template readies for scoring, but no scores are entered now

**Matrix Template (ENFORCEMENT-READY):**
```markdown
## Applicability Matrix Structure (ENFORCEMENT VERSION)

### Solution Options Evaluated
1. **Option A:** [Description] - [Key characteristics] *(GAP/FAIL: [Y/N]; Reason if Y)*
2. **Option B:** [Description] - [Key characteristics] *(GAP/FAIL: [Y/N]; Reason if Y)*
3. **Option C:** [Description] - [Key characteristics] *(GAP/FAIL: [Y/N]; Reason if Y)*

### Context Factors Assessed
**Total Factors:** [count]; **GAP/FAIL Flags Present:** [Y/N]
**Categories:** Technical ([count]), Business ([count]), Operational ([count]), Risk ([count]) (list gaps or missing)

### Evaluation Criteria Enforcement
**Scoring Scale:** 1–5 (Not Applicable to Excellent Fit) (any scale not defined = GAP/FAIL)
**Weight Range:** 1–5 (Supporting to Critical)
**Confidence Scale:** 0.0–1.0 (No Confidence to Extremely High) (missing scale ⇒ -20% confidence)

### ENFORCEMENT Matrix Table

| Factor                | Weight | Option A      | Option B      | Option C      | GAP/FAIL Flag | Rationale/Gap Note      |
|-----------------------|--------|---------------|---------------|---------------|---------------|------------------------|
| Technical Complexity  | [w]    | [ ] ([ ])     | [ ] ([ ])     | [ ] ([ ])     | [Y/N]         | [if Y: specify reason] |
| Scalability           | [w]    | [ ] ([ ])     | [ ] ([ ])     | [ ] ([ ])     | [Y/N]         | [if Y: specify reason] |
| [More factors...]     |        |               |               |               |               |                        |
| **GAP/FAIL Summary**  |        |               |               |               | [count]       | [enumerate all]        |
| **Framework Confidence** |      |               |               |               |               | [100%-(penalties)]     |
```

### 3. Document Framework in Report

"**Документирую evaluation framework в consilium report...**"

Update {outputFile} with matrix setup information (ENFORCEMENT FORMAT):

```markdown
## Applicability Matrix Framework (ENFORCEMENT VERSION)

### Solution Options — Enforcement

**Total Options:** [count]  
**Blank, placeholder, or unclear options?** [Y/N]  
**GAP/FAIL flags:** [list if any]

#### Option Details (GAP/FAIL must be annotated for incomplete or ambiguous)

1. **[Option Name]**
    - **Category:** [type]
    - **Description:** [detailed description] (GAP: [Y/N])
    - **Key Characteristics:** [list] (specify gaps)
    - **Rationale:** [why this option; GAP-comment if unclear]

2. **[Option Name]** *(repeat for all)*

### Context Factors — Enforcement

**Total Factors:** [count]  
**Empty/missing factors?** [Y/N]  
**GAP/FAIL flags:** [list where incomplete]

#### Factor Catalog & GAP Audit

- **Technical Factors:** [list or GAP-comment]
- **Business Factors:** [list or GAP-comment]
- **Operational Factors:** [list or GAP-comment]
- **Risk Factors:** [list or GAP-comment]

### Evaluation Criteria — Enforcement

**Scoring Methodology:** Explicit, full scales only (missing scale = GAP/FAIL)  
**Weight Distribution:** All weights assigned (missing = GAP/FAIL)  
**Assessment Approach:** Gaps summarized

### Matrix Preparation Status [STRICT ENFORCEMENT TABLE]

| Requirement                        | Satisfied [Y/N] | GAP/FAIL Notes             |
|-------------------------------------|-----------------|----------------------------|
| Solution Options (No blanks/TBD)    |                 |                            |
| All Factors Categorized             |                 |                            |
| Criteria (Scales/Weights/Conf)      |                 |                            |
| Matrix Structure Populated          |                 |                            |
| Framework Confidence Adjusted       |                 | [specify % penalty]        |

**Framework confidence after penalties:** [100% - (# GAPs × 20%)]%

✅ *Mark checked when fully satisfied; else note all gaps (reason & impact).*

### GAP/FAIL SUMMARY

- List every missing/uncertain input; annotate consequence (cannot proceed to scoring if any gaps in options/factors/criteria; confidence drop of -20% per critical fail).

### Enforcement Declaration

**YOU MAY ONLY PROCEED TO SCORING IF:**  
- All enforcement checklist items are certified complete  
- GAP/FAIL summary is empty  
- Framework confidence is at 100% (no deductions)

```

### 4. Update Consilium Progress

Update {outputFile} frontmatter:
```yaml
stepsCompleted: ['step-01-problem-analysis', 'step-02-decision-block-v2', 'step-03a-evidence-collection', 'step-03b-evidence-validation', 'step-04a1-solution-options', 'step-04a2a-factors-establishment', 'step-04a2b-matrix-preparation']
progress: 50
currentPhase: 'matrix-setup'
lastStep: 'step-04a2b-matrix-preparation'
matrixSetupComplete: true
enforcementAudit: true
lastMatrixEnforcement: true
frameworkConfidence: '[current % after penalties]'
gapFailSummary: '[only "none" allows next step]'
```

### 5. Present MENU OPTIONS

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Scoring Application"

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper framework refinement
- IF P: Execute {partyModeWorkflow} to discuss matrix setup with other agents
- IF C: Save matrix setup to {outputFile}, update frontmatter stepsCompleted, then only then load, read entire file, then execute {nextStepFile}
- IF Any other comments or queries: help user respond then [Redisplay Menu Options](#5-present-menu-options)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and then end with display again of the menu options

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN C is selected and matrix setup is saved to {outputFile} will you then load and read fully {nextStepFile} to execute and begin scoring application.

## NEAR-TIE DETECTION PROTOCOL

**After matrix scoring completed in subsequent steps, validate:**
```
IF (top_option_score - second_option_score < 0.3) THEN
  FLAG: "Options are statistically indiscriminable"
  WARNING: "Difference within measurement error margin"
  RECOMMENDATION:
    - Acquire additional differentiating evidence
    - Establish new evaluation criteria specific to these options
    - Consider hybrid solution combining strengths
    - Escalate to stakeholder decision override
  CONFIDENCE REDUCTION: -20% due to near-tie uncertainty
ELSE
  PASS: Clear differentiation between options
```

**Near-Tie Threshold Justification:**
0.3 point difference on 1-5 scale = 6% variation, within typical scoring subjectivity

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Matrix structure prepared with complete templates and methodology
- Evaluation framework comprehensively documented in consilium report
- Matrix preparation checklist completed with all requirements
- Framework properly documented with clear evaluation approach
- Progress updated to 50% with matrix setup finalized

### ❌ SYSTEM FAILURE:

- Matrix structure not prepared with complete templates
- Framework documentation inadequate or missing critical elements
- Preparation checklist not completed or requirements missing
- Evaluation approach not clearly documented
- Setup not properly finalized for scoring phase

**Master Rule:**  
Matrix preparation completes the evaluation foundation — all structures must be prepared, frameworks fully documented, and enforcement self-validation declared.  
If ANY critical element is missing:  
- Mark enforcement failure, confidence drops by at least -20%,  
- Do NOT proceed, repeat/correct until self-audit checklist passes and GAP/FAIL log is empty.
