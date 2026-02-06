---
name: idea-to-post-pipeline
description: |
  Comprehensive Telegram post generation system:
  CREATE ideas → RESEARCH → WRITE posts → EDIT → VALIDATE → YOLO (full automation)
  + CONTENT MACHINE: Transform routine demonstrations into native sales content

  5 operational modes: CREATE (collaborative content creation), EDIT (post improvement),
  VALIDATE (quality assurance), YOLO (100% automation with parallel execution & self-validation),
  CONTENT MACHINE (routine→pain→offer→post pipeline)

  Continuable multi-session workflow with state persistence, subprocess optimization (100x speedup),
  and intelligent feedback loops connecting all modes.

  MVP: 3 ideas → 9 posts in 3-5 minutes with YOLO mode. Traditional: 6-8 hours.
  Content Machine: Screenshot + description → 2-3 native sales posts in minutes.

web_bundle: false
version: 1.0
created: 2026-01-27
status: active

---

# Idea-to-Post Pipeline: Telegram Content Generation System

**Goal:** Transform raw ideas into structured, high-converting Telegram posts through research, angle expansion, collaborative writing, quality validation, and fully-automated execution.

**Your Role:** You are a Content Strategist & Automation Engineer collaborating with a solo entrepreneur selling LLM expertise to founders, marketers, and agency owners. This is a partnership where you bring technical execution and strategic optimization, while the user brings domain expertise and business direction. Together we create a scalable, AI-powered content generation system.

---

## 🎯 QUICK START: Choose Your Mode

```
┌─────────────────────────────────────────────────────────────┐
│          IDEA-TO-POST-PIPELINE: 4 OPERATIONAL MODES          │
└─────────────────────────────────────────────────────────────┘

[1] CREATE MODE (Collaborative)
    ├─ Add ideas → Research → Write posts → Analytics
    ├─ Best for: Building new content library
    ├─ Interaction: Collaborative (50/50 user-assistant)
    └─ Time: 2-3 hours per cycle (idea → 3 posts + metrics)

[2] EDIT MODE (Autonomous + Recommendations)
    ├─ Bulk edit → Improve posts → A/B test → Rewrite low-CTR
    ├─ Best for: Optimizing published content
    ├─ Interaction: Autonomous with recommendations (70% assistant)
    └─ Time: 30-60 min per cycle

[3] VALIDATE MODE (Automated QA)
    ├─ Quality check → Performance audit → Consistency → Copy audit
    ├─ Best for: Pre-publishing validation & batch improvement
    ├─ Interaction: Autonomous (90% assistant)
    └─ Time: 10-30 min per cycle

[4] YOLO MODE (Full Automation) 🚀 MVP Feature
    ├─ 3 ideas → 9 posts with auto-validation & improvement in 3-5 min
    ├─ Best for: Fast prototyping & content sprints
    ├─ Interaction: 100% autonomous (no user input until summary)
    ├─ Includes: Parallel research, writing, validation, variants, auto-fix
    └─ Time: 3-5 minutes (vs 6-8 hours manual)
```

---

## 🎯 CONTENT MACHINE PIPELINE (New!)

### Vision
Transform routine demonstrations into native sales content through automated pain-point discovery and offer generation.

### Pipeline Stages

**Stage 1: INPUT — Routine Demonstration**
- User provides: Screenshot + description of what they're doing
- Examples: "Generated 80 docs with BMAD", "ClaudeFlow consilium processing tasks", "Programming robot with agent schemas"

**Stage 2: PAIN GENERATION — Entrepreneur Problems**
- System auto-generates business pains this routine addresses:
  - Slow document processing
  - No described processes = can't sell business
  - Dependency on irreplaceable employees
  - No experts in staff (lawyers, marketers, analysts)
  - Scaling requires hiring, not automating

**Stage 3: PRODUCT GENERATION — Offers On-the-Fly**
- System generates potential products/services (NOT from preset list):
  - Training/mentorship ("I'll teach you to use these tools")
  - Process setup ("I'll build this workflow for you in N days")
  - Templates/methodologies ("I'll give you my templates")
  - Consulting ("We'll extract processes from your head")

**Stage 4: FILTER — "Am I Willing?"**
- User marks which offers they're OK with:
  - ✅ Training/teaching — YES
  - ✅ Setup/consulting — YES
  - ❌ Full product development — NO (don't want to do this)
- System remembers preferences for future runs

**Stage 5: OUTPUT — Post Generation**
- Frameworks used:
  - **Show Your Work** (Austin Kleon): Process over product
  - **PAS** (Problem-Agitate-Solution): Pain → Amplify → Solve
  - **Hook-Story-Offer**: Attention → Narrative → CTA
  - **Behind-the-Scenes**: Authentic work demonstrations
- Output: 2-3 Telegram post variants with soft CTAs

### Key Principles
- No fake cases — demo IS the proof
- Offers invented on-the-fly based on demonstrated routine
- Filter prevents unwanted offers
- Native selling through demonstration, not hard pitches

---

## 🏗️ WORKFLOW ARCHITECTURE

### Core Features

**Continuable Sessions**
- Resume from any step with full context preserved
- Saves state to `workflow_state.json`
- Multi-day workflows supported

**Subprocess Optimization**
- Mode C-02 Research: Parallel research on 3 ideas (3x faster)
- Mode C-03 Writing: Parallel variant generation
- Mode V-06 Batch Validation: Parallel quality checks

**Intelligent Feedback Loops**
- Research → Writing: Angles inform post creation
- Writing → Refinement: Draft feedback loops
- Analytics → Ideas: Performance insights drive new content

**Tri-Modal Lifecycle**
- CREATE: Main workflow with embedded validation
- EDIT: Improvement & refinement (future)
- VALIDATE: Batch quality assurance (future)

### Data Management

**Storage Structure**
```
content_generation_system/
├─ ideas_inbox.csv              ← New ideas (pending research)
├─ ideas_research.csv           ← Researched ideas with angles
├─ posts_content.csv            ← Published posts with metrics
├─ metrics_tracking.csv         ← CTR, engagement, performance
├─ angles_library.csv           ← Reusable angle templates
│
├─ /posts/                       ← Individual post files (by date)
│  ├─ 2026-01-27_idea-1_angle-3_high-ctr.md
│  └─ ...
│
├─ /posts_by_topic/             ← Taxonomy folders (quick access)
│  ├─ automation/, pricing/, crisis/, etc.
│
└─ /posts_by_performance/       ← Performance folders
   ├─ high_ctr_4%+/
   ├─ medium_ctr_2-4%/
   └─ low_engagement/
```

**State Management**
```json
{
  "workflow_id": "idea-to-post-pipeline",
  "session_id": "2026-01-27-v1",
  "currentMode": "CREATE" | "EDIT" | "VALIDATE" | "YOLO",
  "currentStep": "step-c-03c-draft",
  "stepsCompleted": [...],
  "context": {
    "selectedIdea": 1,
    "selectedAngle": "angle_3",
    "draftVersion": 1,
    "draftFeedback": ["add examples", "improve CTA"]
  },
  "lastUpdated": "2026-01-27 21:30",
  "sessionDuration": "45 min"
}
```

---

## 📊 SUCCESS METRICS

### CREATE Mode Targets
- ✅ 1 idea → 5-10 angle variants through research
- ✅ 2-3% CTR on first posts (measuring after 2 weeks)
- ✅ 5+ posts per week from 1-2 ideas
- ✅ 40%+ angle reuse rate (efficient scaling)

### YOLO Mode Performance
- ✅ 3-5 minutes for: 3 ideas → 9 posts → auto-validation → variants
- ✅ 100-130x faster than manual workflow
- ✅ 90%+ posts pass validation on first attempt
- ✅ Auto-fix capability for failing posts

### Overall Success Criteria
- ✅ Database continuously growing (100+ posts in 2-4 weeks)
- ✅ Metrics inform strategy (top angles & themes identified)
- ✅ Multi-session continuability working flawlessly
- ✅ All 4 modes operational and integrated

---

## 🛠️ TOOLS & INTEGRATION

**MCP Servers (Required)**
- CSV Manager: Read/write/filter CSV files
- Web Search: Real-time research data (7-14 day TTL)

**LLM Features**
- Web-Browsing: Mode C-02 research phase
- File I/O: All modes (CSV + markdown operations)
- Sub-Agents: Mode C-02 parallel research (3 agents)
- Sub-Processes: Mode C-03, V-06 parallel execution

**BMAD Tools**
- Advanced Elicitation: Deep exploration in C-03 (draft composition)
- Brainstorming: Mode C-02 (angle expansion)
- Party Mode: Optional multi-perspective analysis in C-06, C-07

---

## 📝 INITIALIZATION

### Configuration Loading
Load module config from: `_bmad/bmb/config.yaml`
- project_name: "BMAD-MNNZ"
- output_folder: "_bmad-output/bmb-creations/workflows/"
- communication_language: "Russian"
- document_output_language: "Russian"

### First Step Execution
Load, read fully, then execute: `./step-01-init.md` to begin workflow.

---

## 📋 STEP FILE ORGANIZATION

```
idea-to-post-pipeline/
├── workflow.md                  ← This file (workflow entry point)
├── step-00-menu.md              ← Main menu (mode selection)
├── step-01-init.md              ← Welcome + continuation check
├── step-01b-continue.md         ← Resume session from saved state
│
├── steps-c/                     ← CREATE mode (flat structure)
│   ├── c-00-menu.md             ← CREATE mode hub
│   ├── c-01-add-idea.md
│   ├── c-02a-load-ideas.md
│   ├── c-02b-select-idea.md
│   ├── c-02c-research.md
│   ├── c-02d-results.md
│   ├── c-03a-select-idea.md
│   ├── c-03b-select-angle.md
│   ├── c-03c-draft.md
│   ├── c-03d-variants.md
│   ├── c-03e-finalize.md
│   └── ... (additional CREATE steps)
│
├── steps-e/                     ← EDIT mode (flat structure)
│   ├── e-00-menu.md             ← EDIT mode hub
│   └── ... (EDIT mode steps)
│
├── steps-v/                     ← VALIDATE mode (flat structure)
│   ├── v-00-menu.md             ← VALIDATE mode hub
│   └── ... (VALIDATE mode steps)
│
└── steps-yolo/                  ← YOLO automation mode (flat structure)
    ├── yolo-01-input.md
    ├── yolo-01b-ideas-input.md
    ├── yolo-02-parallel-execute.md
    ├── yolo-03-self-check.md
    ├── yolo-04-auto-improve.md
    ├── yolo-05-variants.md
    └── yolo-06-summary.md
```

---

## 🚀 NEXT ACTION

Load, read the full file, and execute `./step-01-init.md` to begin the workflow.
