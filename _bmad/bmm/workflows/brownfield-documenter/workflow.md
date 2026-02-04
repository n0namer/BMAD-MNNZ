---
name: brownfield-documenter
description: "Brownfield Documenter - EMBER-powered documentation generation for existing projects with flexible interaction modes"
version: "1.0.0"
author: "Workflow Builder Master"
---

# Brownfield Documenter

**Purpose:** Intelligent documentation generation for brownfield projects using EMBER AI orchestration with three interaction modes.

**EMBED Integration:** Leverages EMBER workflow for intelligent analysis and automated responses based on selected interaction mode, with EMBER consilium integration for complex decisions.

**Input:** Project root path + interaction mode selection
**Output:** Complete BMAD documentation package (index.md + supporting files)
**Performance:**
- EMBER Auto-Pilot: 5-15 minutes (fully autonomous)
- EMBER Assisted: 15-45 minutes (with human oversight)
- Manual: 30-120 minutes (traditional workflow)

## Architecture

**EMBED Orchestration Pattern:**
- **Core Engine:** document-project/full-scan-instructions.md
- **BMM Workflow Integration:** 32-step BMM workflow orchestration from ember-orchestration-system
- **EMBED Consilium Integration:** Decision support calls to EMBER consilium workflow
- **EMBED Integration:** Intelligent responses based on selected mode
- **Mode-Aware Execution:** Different behavior per interaction mode
- **Output Format:** BMAD documentation structure + BMM workflow execution

## Integration Points

- EMBER workflow for intelligent analysis (Assisted/Auto-Pilot modes)
- document-project workflow as scanning foundation
- BMAD menu system integration
- Multi-mode user experience
- Context preservation across workflow steps

## Execution Flow

### 🌟 EMBER Assisted Mode (Recommended):
1. **Mode Selection** - User chooses Assisted mode
2. **Project Setup** - User provides project path
3. **BMM Workflow Selection** - Choose from 32 available BMM workflows
4. **Interactive Execution** - EMBER orchestrates workflow with user oversight
5. **EMBED Consilium Integration** - Automatic calls for complex decisions
6. **Documentation Generation** - User oversees final output
7. **Quality Assurance** - User validates recommendations

### ⚡ EMBER Auto-Pilot Mode:
1. **Mode Selection** - User chooses Auto-Pilot mode
2. **Project Setup** - User provides project path
3. **BMM Workflow Selection** - Choose from 32 available workflows
4. **Autonomous Orchestration** - EMBER handles all workflow execution
5. **EMBED Consilium Integration** - Automatic decision support calls
6. **Fast Generation** - Complete execution without pauses
7. **Direct Output** - Final deliverables delivered

### ✏️ Manual Mode:
1. **Mode Selection** - User chooses Manual mode
2. **Traditional Workflow** - User executes workflows manually
3. **Standard Process** - Follows original BMAD workflow patterns
4. **Full Control** - Maximum user oversight and customization
5. **Optional EMBER Support** - Manual EMBER consilium calls if needed

### 🔧 BMM Workflow Orchestration:

**Available Workflows (32 total):**

#### **1-Analysis Phase (7 workflows):**
- `research` - Market and competitive analysis
- `create-product-brief` - Product vision and requirements
- Additional analysis workflows...

#### **2-Plan-Workflows Phase (3 workflows):**
- `create-ux-design` - User experience design
- `prd` - Product requirements documentation
- Additional planning workflows...

#### **3-Solutioning Phase (3 workflows):**
- `check-implementation-readiness` - Technical readiness assessment
- `create-architecture` - System architecture design
- `create-epics-and-stories` - Agile planning and breakdown

**EMBED Consilium Integration:**
- **Automatic Triggers:** Complex strategic/technical/business decisions
- **Workflow Calls:** Seamless integration with EMBER consilium workflow
- **Confidence Scoring:** All recommendations include confidence levels (0.0-1.0)
- **Result Injection:** Recommendations integrated back into workflow execution

## Key Features

- **Flexible Interaction** - Three distinct usage modes
- **EMBED Intelligence** - AI-powered analysis when desired
- **Backward Compatible** - Works with existing BMAD infrastructure
- **Context Aware** - Maintains state across workflow steps
- **Quality Options** - From draft speed to detailed control

## Mode Selection

**Choose your interaction level:**

### 🌟 EMBER Assisted (Recommended)
- EMBER provides suggestions, you control each step
- Best for learning + quality assurance
- Time: 15-45 minutes

### ⚡ EMBER Auto-Pilot
- Full autonomy, EMBER handles everything
- Fastest option for draft documentation
- Time: 5-15 minutes

### ✏️ Manual Mode
- Traditional workflow, you answer all questions
- Maximum control, slowest pace
- Time: 30-120 minutes

## Usage

```bash
# Through BMM Analyst agent
[BD] Brownfield Documenter - EMBER-powered documentation

# Direct execution
exec: {project-root}/_bmad/bmm/workflows/brownfield-documenter/workflow.md
```

## INITIALIZATION SEQUENCE

### 1. Module Configuration Loading

Load and read full config from {project-root}/_bmad/bmb/config.yaml and resolve:

- `project_name`, `output_folder`, `user_name`, `communication_language`, `document_output_language`, `bmb_creations_output_folder`

### 2. EMBER Documenter Process

After configuration loading, load, read the full file and then execute `./steps-c/step-00-client-introduction-brownfield.md` to begin the Brownfield Documenter process with initial client communication and mode selection.

## Dependencies

- BMAD Core system
- document-project workflow
- EMBER workflow (for Assisted/Auto-Pilot modes)
- File system access
- BMM module variables
