---
name: 'step-01-edit'
description: 'Initialize Brownfield Documenter edit mode - select target and setup editing environment'

nextStepFile: './step-02-modify.md'
outputFile: '{bmb_creations_output_folder}/brownfield-documenter-edited-{project_name}-{datetime}.md'
---

# Step 1: Brownfield Documenter Edit Initialization

## STEP GOAL:

Initialize Brownfield Documenter edit mode by selecting documentation target and setting up editing environment with EMBER integration.

## EDIT MODE SELECTION: Choose Edit Target

**Select your edit target:**
- **📝 Edit Generated Documentation** - Modify existing generated documentation files
- **🔧 Edit Workflow Configuration** - Modify workflow settings and parameters
- **🎨 Edit EMBER Integration** - Adjust EMBER interaction patterns and prompts
- **⚙️ Edit Project Structure** - Modify project scanning and analysis settings

## EXECUTION SEQUENCE

### 1. Select Edit Target

**For Edit Generated Documentation:**
- Display target benefits: "Modify existing documentation outputs"
- Ask user: "Select documentation file to edit:"
- Set {{edit_target}} = "documentation"

**For Edit Workflow Configuration:**
- Display target benefits: "Customize workflow behavior and settings"
- Ask user: "Select configuration aspect to edit:"
- Set {{edit_target}} = "configuration"

**For Edit EMBER Integration:**
- Display target benefits: "Fine-tune AI assistance patterns"
- Ask user: "Select EMBER integration to modify:"
- Set {{edit_target}} = "ember"

**For Edit Project Structure:**
- Display target benefits: "Adjust project analysis settings"
- Ask user: "Select structure element to edit:"
- Set {{edit_target}} = "structure"

### 2. Load Current State

Based on {{edit_target}}:
- Load existing documentation files
- Load current workflow configuration
- Load EMBER integration settings
- Load project structure definitions

### 3. Initialize Edit Environment

**EMBED Assisted Editing:**
- Load EMBER edit workflow integration
- Initialize context preservation for editing
- Set up EMBER suggestion templates for modifications

**Manual Editing:**
- Load traditional editing patterns
- Initialize manual input tracking for changes

### 4. Validate Edit Permissions

- Check file write permissions for target files
- Verify backup creation capabilities
- Confirm EMBER integration availability (for Assisted mode)

### 5. Create Edit Session

Initialize edit session with:
- edit_target: {{edit_target}}
- edit_mode: "assisted" or "manual"
- backup_location: {bmb_creations_output_folder}/backups/
- session_id: Generated unique identifier

### 6. Proceed to Modification

**EMBED Assisted:** Proceed with EMBER-guided editing
**Manual:** Proceed with direct file editing

---

## SUCCESS METRICS

- Edit target selected and validated
- Edit environment initialized successfully
- File permissions confirmed
- Edit session created with proper backups
- Correctly proceeded to modification step based on mode

## EDIT MODE INITIALIZED ✅
