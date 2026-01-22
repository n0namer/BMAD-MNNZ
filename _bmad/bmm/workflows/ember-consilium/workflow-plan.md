---
workflowName: ember-consilium
description: EMBER Evidence-Based Analysis and Decision Support System - Workflow Design Plan
version: 1.0.0
created: 2026-01-19
---

# EMBER Consilium Workflow Design Plan

## Overview

The EMBER Consilium workflow implements a comprehensive evidence-based decision support system using AI-powered analysis and structured analytical frameworks. The workflow follows BMAD tri-modal architecture with specialized create-mode steps.

## Workflow Architecture

### Tri-Modal Structure
- **Create Mode (steps-c/)**: 19 steps implementing full EMBER analysis workflow
- **Edit Mode (steps-e/)**: For modifying existing consilium reports
- **Validate Mode (steps-v/)**: For validating workflow compliance

### Step Organization
The workflow uses numbered steps with letter suffixes for sub-steps:
- **01a-01b**: Problem Definition & Initial Analysis
- **02a-02b**: Decision Framework Setup
- **03a-03c**: Evidence Gathering & Validation
- **04a-04h**: Solution Development & Evaluation
- **05a-05d**: Criteria Validation & Final Documentation

## Step Relationships & Flow

### Phase 1: Problem Analysis (Steps 01a-01b)
```
01a-problem-definition.md
    ↓ (user selects C)
01b-analysis-documentation.md
    ↓ (user selects C)
02a-decision-framework.md
```

### Phase 2: Framework Setup (Steps 02a-02b)
```
02a-decision-framework.md
    ↓ (user selects C)
02b-moe-matrix-setup.md
    ↓ (user selects C)
03a-evidence-identification.md
```

### Phase 3: Evidence Management (Steps 03a-03c)
```
03a-evidence-identification.md
    ↓ (user selects C)
03b-evidence-gathering.md
    ↓ (user selects C)
03c-evidence-validation.md
    ↓ (user selects C)
04a-solution-options.md
```

### Phase 4: Solution Development (Steps 04a-04h)
```
04a-solution-options.md
    ↓ (user selects C)
04b-factors-establishment.md
    ↓ (user selects C)
04c-matrix-preparation.md
    ↓ (user selects C)
04d-scoring-application.md
    ↓ (user selects C)
04e-scoring-validation.md
    ↓ (user selects C)
04f-ranking-calculation.md
    ↓ (user selects C)
04g-validation-assessment.md
    ↓ (user selects C)
04h-results-documentation.md
    ↓ (user selects C)
05a-criteria-validation.md
```

### Phase 5: Final Validation & Documentation (Steps 05a-05d)
```
05a-criteria-validation.md
    ↓ (user selects C)
05b-decision-validation.md
    ↓ (user selects C)
05c-confidence-synthesis.md
    ↓ (user selects C)
05d-final-documentation.md
    ↓ (END)
```

## Data Flow & Dependencies

### Input Data
- User decision problem statement
- Stakeholder information
- Constraints and requirements
- Available evidence sources

### Intermediate Outputs
- Problem decomposition analysis
- Decision frameworks
- Evidence collection
- MOE matrix setup
- Solution scoring and ranking

### Final Output
- Comprehensive EMBER consilium report
- Confidence-scored recommendations
- Implementation roadmap
- Risk assessment

## File Dependencies

### Data Files
- `decision-frameworks.md`: Decision making methodologies
- `evaluation-criteria.md`: Assessment standards
- `implementation-planning-templates.md`: Planning templates
- `solution-selection-templates.md`: Solution templates
- `validation-framework.md`: Validation standards
- `evidence-analysis-template.md`: Evidence analysis format

### Template Files
- `evidence-analysis-template.md`
- `executive-summary-template.md`
- `implementation-plan-template.md`
- `recommendation-template.md`

### External Dependencies
- `advanced-elicitation/workflow.xml`: For deep problem exploration
- `party-mode/workflow.md`: For collaborative analysis sessions

## Step Type Classification

| Step | Type | Purpose |
|------|------|---------|
| 01a | Init | Problem capture and initial decomposition |
| 01b | Continuation | EMBER analysis and documentation |
| 02a-05c | Middle (Collaborative) | Framework application, evidence management, solution development |
| 05d | Final | Report completion and delivery |

## Error Handling & Recovery

### Critical Path Checks
- All step files must exist and be accessible
- External workflow references must be valid
- Data files must be present for dependent steps
- Output files use config variables (validated at runtime)

### User Input Validation
- Mandatory fields checked at each step
- Progress tracking via output file frontmatter
- Ability to revisit previous steps if needed

## Performance Considerations

### File Size Limits
- All step files: < 200 lines (recommended), < 250 lines (maximum)
- Current sizes: All within limits (112-182 lines)

### Execution Flow
- Sequential step execution (no parallel processing in create mode)
- User interaction required at each collaborative step
- Progress saved incrementally to prevent data loss

## Compliance Standards

### BMAD Standards Compliance
- ✅ Tri-modal architecture implemented
- ✅ Step file size limits respected
- ✅ Frontmatter variables properly used
- ✅ Relative path formats followed
- ⚠️ Minor: Non-standard step numbering (intentional for sub-steps)

### EMBER Framework Integration
- Decision Block v2.0 methodology
- Confidence scoring for all recommendations
- Multi-perspective evidence analysis
- Systematic risk assessment

## Future Extensions

### Potential Edit Mode (steps-e/)
- Modify existing consilium reports
- Update evidence with new data
- Re-evaluate recommendations

### Potential Validate Mode (steps-v/)
- Compliance checking against EMBER standards
- Report quality assessment
- Recommendation validation

## Version History

- **v1.0.0** (2026-01-19): Initial workflow design implementation
  - Complete 19-step EMBER analysis workflow
  - BMAD tri-modal architecture
  - Evidence-based decision support system
