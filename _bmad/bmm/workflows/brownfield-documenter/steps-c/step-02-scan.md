---
name: 'step-02-scan'
description: 'Execute project scanning based on selected interaction mode'

nextStepFile: './step-03-generate.md'
---

# Step 2: Brownfield Project Scan

## STEP GOAL:

Execute project scanning using mode-appropriate analysis method - EMBER-enhanced or traditional document-project workflow.

## MODE-AWARE SCANNING: EMBER vs Manual Analysis

**EMBED Assisted/Auto-Pilot:** Enhanced scanning with EMBER intelligence
**Manual Mode:** Traditional document-project workflow execution

## EXECUTION SEQUENCE

### 1. Determine Scan Approach Based on Mode

**EMBED Auto-Pilot Mode:**
- Set scan_level: "quick" (fastest autonomous mode)
- Enable EMBER intelligence overlay
- Set auto_proceed: true, skip_interactive: true
- Configure EMBER to automatically answer all scan-related questions

**EMBED Assisted Mode:**
- Set scan_level: "standard" (balanced analysis)
- Enable EMBER suggestion mode
- Set auto_proceed: false, skip_interactive: false
- Configure EMBER to provide suggestions for user review/approval

**Manual Mode:**
- Set scan_level: "comprehensive" (detailed manual analysis)
- Disable EMBER integration
- Set auto_proceed: false, skip_interactive: false
- Use traditional document-project workflow

### 2. Execute Mode-Appropriate Scanning

**For EMBER Auto-Pilot:**
- Invoke EMBER-enhanced document-project workflow
- Parameters: project_root_path, scan_level: "quick", ember_auto_respond: true
- Monitor EMBER decision-making process

**For EMBER Assisted:**
- Invoke document-project with EMBER suggestions
- Parameters: project_root_path, scan_level: "standard", ember_suggestions: true
- Present EMBER suggestions to user for approval

**For Manual Mode:**
- Invoke standard document-project workflow
- Parameters: project_root_path, scan_level: "comprehensive", ember_disabled: true
- User answers all questions manually

### 3. Monitor Execution by Mode

**EMBED Auto-Pilot:**
- Track EMBER decision confidence scores
- Auto-proceed through all steps
- Log EMBER reasoning for transparency

**EMBED Assisted:**
- Present EMBER suggestions at each decision point
- Wait for user approval before proceeding
- Allow user to modify EMBER suggestions

**Manual Mode:**
- Follow standard document-project workflow
- User provides all inputs manually
- No EMBER intervention

### 4. Collect Scan Results

Gather all generated documentation files:
- index.md (project overview)
- architecture.md (system design)
- data-models.md (data structures)
- api-contracts.md (interfaces)
- development-guide.md (implementation)
- source-tree.md (code organization)

### 5. Proceed to Generation

**EMBED Auto-Pilot:** Auto-proceed immediately
**EMBED Assisted:** Proceed after user confirmation
**Manual Mode:** Proceed after user confirmation

---

## SUCCESS METRICS

- Project scanning executed successfully in selected mode
- EMBER integration worked correctly (for Assisted/Auto-Pilot modes)
- All scan-related questions answered appropriately based on mode
- Documentation files generated with expected quality
- Correctly proceeded to generation step based on mode settings
