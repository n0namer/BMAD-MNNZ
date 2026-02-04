---
name: 'step-01-init'
description: 'Initialize Brownfield Documenter - select mode and setup project'

nextStepFile: './step-02-scan.md'
outputFile: '{bmb_creations_output_folder}/brownfield-documenter-{project_name}-{datetime}.md'
---

# Step 1: Brownfield Documenter Initialization

## STEP GOAL:

Initialize Brownfield Documenter by selecting interaction mode and setting up project path with EMBER integration.

## MODE SELECTION: Choose Interaction Level

**Select your preferred interaction mode:**
- **🌟 EMBER Assisted** (Recommended) - EMBER suggests, you control each step
- **⚡ EMBER Auto-Pilot** - Full autonomy, EMBER handles everything
- **✏️ Manual Mode** - Traditional workflow, you answer all questions

## EXECUTION SEQUENCE

### 1. Select Interaction Mode

**For EMBER Assisted Mode:**
- Display mode benefits: "EMBED suggestions with your oversight"
- Ask user: "Confirm EMBER Assisted mode? [Y/n]"
- Set {{interaction_mode}} = "assisted"

**For EMBER Auto-Pilot Mode:**
- Display mode benefits: "Full autonomy, fastest results"
- Ask user: "Confirm EMBER Auto-Pilot mode? [Y/n]"
- Set {{interaction_mode}} = "auto-pilot"

**For Manual Mode:**
- Display mode benefits: "Traditional workflow, full control"
- Ask user: "Confirm Manual mode? [Y/n]"
- Set {{interaction_mode}} = "manual"

### 2. Get Project Path

Ask user: "Enter the root path of the brownfield project to document:"

Store as {{project_root_path}}

### 3. Validate Project Access

- Check if path exists and is readable
- For EMBER modes: Verify EMBER workflow availability
- Log: "Project validated for {{interaction_mode}} mode: {{project_root_path}}"

### 4. Initialize Mode-Specific Setup

**EMBED Assisted/Auto-Pilot:**
- Load EMBER workflow integration
- Initialize context preservation
- Set up EMBER prompt templates

**Manual Mode:**
- Load traditional workflow patterns
- Initialize manual input tracking

### 5. Initialize Output Structure

Create output folder: {bmb_creations_output_folder}/brownfield-documenter-{project_name}-{datetime}/

Initialize state file with mode settings:
- interaction_mode: {{interaction_mode}}
- ember_enabled: true/false
- auto_proceed: true/false

### 6. Proceed Based on Mode

**EMBED Auto-Pilot:** Auto-proceed to next step
**EMBED Assisted/Manual:** Proceed with user confirmation

---

## SUCCESS METRICS

- Interaction mode selected and confirmed
- Project path obtained and validated
- EMBER integration initialized (for Assisted/Auto-Pilot modes)
- Output folder created with mode-specific naming
- State file initialized with mode settings
- Correctly proceeded based on selected mode (auto/manual)
