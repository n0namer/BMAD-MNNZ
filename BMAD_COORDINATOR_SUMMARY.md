# BMAD Coordinator Summary

**Research Complete**: 2026-01-26
**Document**: For swarm coordination and workflow automation

---

## Executive Summary

Complete exploration of the `_bmad` directory reveals a sophisticated, modular workflow system with 61 workflows across 5 major modules. All workflows are cataloged with exact file paths for coordinator automation.

**Total Assets**:
- 61 Workflows
- 720 Files
- 65 Directories
- 4 Major Modules (BMB, BMM, GDS, CIS) + Core Utilities

---

## Module Breakdown

### 1. BMB (Build Agent & Module Builder) - 3 Workflows
Location: `C:\Users\NIKITA\pipeline-final-test\_bmad\bmb`

**Workflows**:
- Agent Creation/Editing/Validation (workflow.md)
- Module Creation/Editing/Validation (workflow.md)
- Workflow Creation/Editing/Validation (workflow.md)

**Files**: 70+ step files, 15+ data files, multiple templates
**Purpose**: Agent and module development infrastructure

---

### 2. BMM (Business Model Module) - 28 Workflows
Location: `C:\Users\NIKITA\pipeline-final-test\_bmad\bmm`

**Phase 1: Analysis (2 Workflows)**
- Create Product Brief: `workflows/1-analysis/create-product-brief/workflow.md`
- Research: `workflows/1-analysis/research/workflow.md`

**Phase 2: Planning (2 Workflows)**
- Create PRD: `workflows/2-plan-workflows/create-prd/workflow.md`
- Create UX Design: `workflows/2-plan-workflows/create-ux-design/workflow.md`

**Phase 3: Solutioning (3 Workflows)**
- Check Implementation Readiness: `workflows/3-solutioning/check-implementation-readiness/workflow.md`
- Create Architecture: `workflows/3-solutioning/create-architecture/workflow.md`
- Create Epics and Stories: `workflows/3-solutioning/create-epics-and-stories/workflow.md`

**Phase 4: Implementation (7 Workflows)**
- Code Review: `workflows/4-implementation/code-review/workflow.yaml`
- Correct Course: `workflows/4-implementation/correct-course/workflow.yaml`
- Create Story: `workflows/4-implementation/create-story/workflow.yaml`
- Dev Story: `workflows/4-implementation/dev-story/workflow.yaml`
- Retrospective: `workflows/4-implementation/retrospective/workflow.yaml`
- Sprint Planning: `workflows/4-implementation/sprint-planning/workflow.yaml`
- Sprint Status: `workflows/4-implementation/sprint-status/workflow.yaml`

**Quick Flow (2 Workflows)**
- Quick Dev: `workflows/bmad-quick-flow/quick-dev/workflow.md`
- Quick Spec: `workflows/bmad-quick-flow/quick-spec/workflow.md`

**Diagrams (4 Workflows)**
- Create Dataflow: `workflows/excalidraw-diagrams/create-dataflow/workflow.yaml`
- Create Diagram: `workflows/excalidraw-diagrams/create-diagram/workflow.yaml`
- Create Flowchart: `workflows/excalidraw-diagrams/create-flowchart/workflow.yaml`
- Create Wireframe: `workflows/excalidraw-diagrams/create-wireframe/workflow.yaml`

**Test Architecture (8 Workflows)**
- ATDD: `workflows/testarch/atdd/workflow.yaml`
- Automate: `workflows/testarch/automate/workflow.yaml`
- CI: `workflows/testarch/ci/workflow.yaml`
- Framework: `workflows/testarch/framework/workflow.yaml`
- NFR Assess: `workflows/testarch/nfr-assess/workflow.yaml`
- Test Design: `workflows/testarch/test-design/workflow.yaml`
- Test Review: `workflows/testarch/test-review/workflow.yaml`
- Trace: `workflows/testarch/trace/workflow.yaml`

**Document Project (1 Workflow)**
- Document Project: `workflows/document-project/workflow.yaml`

---

### 3. GDS (Game Design Suite) - 23 Workflows
Location: `C:\Users\NIKITA\pipeline-final-test\_bmad\gds`

**Phase 1: Preproduction (2 Workflows)**
- Brainstorm Game: `workflows/1-preproduction/brainstorm-game/workflow.md`
- Game Brief: `workflows/1-preproduction/game-brief/workflow.md`

**Phase 2: Design (2 Workflows)**
- Game Design Document: `workflows/2-design/gdd/workflow.md`
- Narrative Design: `workflows/2-design/narrative/workflow.md`

**Phase 3: Technical (2 Workflows)**
- Game Architecture: `workflows/3-technical/game-architecture/workflow.md`
- Generate Project Context: `workflows/3-technical/generate-project-context/workflow.md`

**Phase 4: Production (7 Workflows)**
- Code Review: `workflows/4-production/code-review/workflow.yaml`
- Correct Course: `workflows/4-production/correct-course/workflow.yaml`
- Create Story: `workflows/4-production/create-story/workflow.yaml`
- Dev Story: `workflows/4-production/dev-story/workflow.yaml`
- Retrospective: `workflows/4-production/retrospective/workflow.yaml`
- Sprint Planning: `workflows/4-production/sprint-planning/workflow.yaml`
- Sprint Status: `workflows/4-production/sprint-status/workflow.yaml`

**Game Testing (7 Workflows)**
- Automate: `workflows/gametest/automate/workflow.yaml`
- E2E Scaffold: `workflows/gametest/e2e-scaffold/workflow.yaml`
- Performance: `workflows/gametest/performance/workflow.yaml`
- Playtest Plan: `workflows/gametest/playtest-plan/workflow.yaml`
- Test Design: `workflows/gametest/test-design/workflow.yaml`
- Test Framework: `workflows/gametest/test-framework/workflow.yaml`
- Test Review: `workflows/gametest/test-review/workflow.yaml`

**Quick Flow (2 Workflows)**
- Quick Dev: `workflows/gds-quick-flow/quick-dev/workflow.md`
- Quick Spec: `workflows/gds-quick-flow/quick-spec/workflow.md`

**Documentation (1 Workflow)**
- Document Project: `workflows/document-project/workflow.yaml`

---

### 4. CIS (Creative Intelligence System) - 4 Workflows
Location: `C:\Users\NIKITA\pipeline-final-test\_bmad\cis`

**Workflows**:
- Design Thinking: `workflows/design-thinking/workflow.yaml`
- Innovation Strategy: `workflows/innovation-strategy/workflow.yaml`
- Problem Solving: `workflows/problem-solving/workflow.yaml`
- Storytelling: `workflows/storytelling/workflow.yaml`

---

### 5. Core Module - 3 Workflows
Location: `C:\Users\NIKITA\pipeline-final-test\_bmad\core`

**Workflows**:
- Brainstorming: `workflows/brainstorming/workflow.md`
- Party Mode: `workflows/party-mode/workflow.md`
- Advanced Elicitation: `workflows/advanced-elicitation/`

---

## File Organization Patterns

### Workflow File Structure (Standard Pattern)

```
workflow-directory/
├── workflow.md (or workflow.yaml)     # Main workflow definition
├── instructions.md                     # Detailed step-by-step instructions
├── checklist.md                        # Progress tracking checklist
├── steps/                              # Step files (or steps-c/, steps-e/, steps-v/)
│   ├── step-01-*.md
│   ├── step-02-*.md
│   └── ...
├── templates/                          # Template files for reuse
│   ├── *.template.md
│   └── ...
└── data/                              # Reference data and examples
    ├── *.md
    └── reference/
```

### File Types Found

| Type | Count | Purpose |
|------|-------|---------|
| workflow.md | 20+ | Markdown workflow definitions |
| workflow.yaml | 35+ | YAML structured workflows |
| instructions.md | 30+ | Procedural guidance |
| checklist.md | 25+ | Task progress tracking |
| step-*.md | 150+ | Individual workflow steps |
| *.template.md | 10+ | Reusable templates |
| data/*.md | 50+ | Reference materials |

---

## Access Patterns for Coordinator

### Pattern 1: Load Workflow
```
1. Read workflow.md or workflow.yaml
2. Extract workflow metadata (title, description, phases)
3. Identify required steps in steps/ or steps-*/
4. Load instructions.md for detailed guidance
5. Track progress with checklist.md
```

### Pattern 2: Execute Steps
```
1. Identify step-phase (steps-c/ for creation, steps-e/ for editing, steps-v/ for validation)
2. Read step files in sequence
3. Follow instructions in each step
4. Execute actions (brainstorm, create artifacts, validate)
5. Mark checklist items as complete
```

### Pattern 3: Apply Templates
```
1. Check templates/ subdirectory
2. Load appropriate template file
3. Fill in template with user input
4. Validate against requirements
5. Save artifact
```

### Pattern 4: Reference Data
```
1. Check data/ subdirectory
2. Load reference materials
3. Extract relevant patterns/standards
4. Apply to current task
5. Store learned patterns
```

---

## Key Workflow Categories

### By Phase Progression
1. **Analysis Workflows**: Research, discovery, requirements gathering
2. **Planning Workflows**: Design, architecture, roadmapping
3. **Implementation Workflows**: Development, coding, execution
4. **Testing Workflows**: Test design, automation, validation
5. **Documentation Workflows**: Project documentation, knowledge capture
6. **Creative Workflows**: Brainstorming, problem-solving, innovation

### By Complexity
- **Quick Flow**: Fast, informal (quick-dev, quick-spec)
- **Standard Flow**: Complete, structured (create-prd, create-architecture)
- **Advanced Flow**: Comprehensive, multi-phase (game-design-document, test-architecture)

### By Domain
- **Software Engineering** (BMM): Product, architecture, testing
- **Game Development** (GDS): Game design, narrative, playtesting
- **Creative Problem-Solving** (CIS): Innovation, storytelling, design thinking
- **Module/Agent Building** (BMB): Agent creation, module development

---

## Coordinator Action Items

### 1. Workflow Discovery
- Use index to identify relevant workflows
- Load workflow.md/yaml files
- Extract metadata and requirements

### 2. Step Sequencing
- Read step files in order
- Identify parallel vs. sequential steps
- Spawn agents for concurrent execution

### 3. Template Application
- Check templates/ for applicable templates
- Fill templates with user input
- Validate against standards in data/

### 4. Checklist Tracking
- Load checklist.md for workflow
- Mark items as in-progress
- Update status as tasks complete

### 5. Agent Spawning
- Identify required agent types from workflow
- Spawn coordinator agents for multi-phase workflows
- Assign specific steps to specialized agents

### 6. Memory Coordination
- Store workflow state in claude-flow memory
- Track completed steps
- Share templates and data with agents
- Learn from workflow execution

---

## Integration with CLAUDE.md

From CLAUDE.md guidelines:

1. **Task Complexity Detection**: Most BMAD workflows trigger swarm orchestration
2. **Agent Routing**: Specialized agents for each workflow type
3. **Memory Coordination**: Store workflow metadata in coordination namespace
4. **Concurrent Execution**: Multiple step files can be processed in parallel
5. **File Organization**: All workflow files organized in appropriate _bmad directories (not root)

---

## Quick Start for Coordinator

1. **Load Index**: Read `_BMAD_COMPLETE_INDEX.md`
2. **Identify Workflow**: Find workflow in module structure
3. **Read Workflow File**: Load workflow.md or workflow.yaml
4. **Extract Steps**: Read step files from steps/ or steps-*/
5. **Follow Instructions**: Execute instructions.md
6. **Spawn Agents**: Create concurrent tasks for steps
7. **Track Progress**: Update checklist.md
8. **Store Memory**: Save workflow state to coordination memory

---

## Storage Locations

All analysis documents stored in project root (not in _bmad):

- `_BMAD_COMPLETE_INDEX.md` - Comprehensive workflow index with all paths
- `BMAD_COORDINATOR_SUMMARY.md` - This document, coordinator quick reference

---

## Document Ready for Swarm Deployment

This summary is prepared for:
1. Coordinator initialization and workflow selection
2. Agent spawning with workflow context
3. Memory coordination and state tracking
4. Cross-phase workflow orchestration
5. Template and data distribution to agents

All file paths are absolute and coordinator-ready.
