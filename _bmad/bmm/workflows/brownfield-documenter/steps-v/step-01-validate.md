---
name: 'step-01-validate'
description: 'Initialize validation mode - select validation target and setup validation environment'

nextStepFile: './step-02-analyze.md'
outputFile: '{output_folder}/validation-session-{project_name}-{datetime}.md'
---

# Step 1: Brownfield Documenter Validation Initialization

## STEP GOAL:

Initialize validation mode by selecting validation target and setting up comprehensive validation environment.

## VALIDATION TARGET SELECTION: Choose Validation Scope

**Select your validation target:**
- **📋 Validate Generated Documentation** - Check documentation quality and completeness
- **🔧 Validate Workflow Configuration** - Verify workflow settings and parameters
- **🎨 Validate EMBER Integration** - Test EMBER interaction patterns and responses
- **⚙️ Validate Project Analysis** - Review project scanning and structure analysis
- **🏗️ Validate Complete Workflow** - Full end-to-end workflow validation

## EXECUTION SEQUENCE

### 1. Select Validation Target

**For Documentation Validation:**
- Display target benefits: "Ensure documentation quality and accuracy"
- Ask user: "Select documentation aspects to validate:"
- Set {{validation_target}} = "documentation"

**For Configuration Validation:**
- Display target benefits: "Verify workflow correctness and completeness"
- Ask user: "Select configuration elements to validate:"
- Set {{validation_target}} = "configuration"

**For EMBER Integration Validation:**
- Display target benefits: "Test AI assistance quality and reliability"
- Ask user: "Select EMBER integration to validate:"
- Set {{validation_target}} = "ember"

**For Project Analysis Validation:**
- Display target benefits: "Review project understanding accuracy"
- Ask user: "Select analysis aspects to validate:"
- Set {{validation_target}} = "analysis"

**For Complete Workflow Validation:**
- Display target benefits: "Comprehensive end-to-end validation"
- Ask user: "Confirm complete workflow validation:"
- Set {{validation_target}} = "complete"

### 2. Load Validation Frameworks

Based on {{validation_target}}:
- Load appropriate validation templates
- Initialize validation checklists
- Set up validation metrics and scoring
- Prepare validation environment

### 3. Initialize Validation Environment

**Automated Validation:**
- Load validation automation scripts
- Initialize test harnesses
- Set up validation data sets
- Configure validation parameters

**Interactive Validation:**
- Load validation checklists
- Initialize user-guided validation
- Set up validation tracking
- Prepare validation reports

### 4. Validate Prerequisites

- Check target availability and accessibility
- Verify validation tool dependencies
- Confirm test data availability
- Validate validation environment setup

### 5. Create Validation Session

Initialize validation session with:
- validation_target: {{validation_target}}
- validation_mode: "automated" or "interactive"
- session_id: Generated unique identifier
- validation_scope: Defined validation boundaries

### 6. Proceed to Analysis

**Automated:** Auto-proceed with validation execution
**Interactive:** Proceed with user-guided validation

---

## SUCCESS METRICS

- Validation target selected and validated
- Validation environment initialized successfully
- Prerequisites confirmed and available
- Validation session created with proper scope
- Correctly proceeded to analysis step based on mode

## VALIDATION INITIALIZED ✅
