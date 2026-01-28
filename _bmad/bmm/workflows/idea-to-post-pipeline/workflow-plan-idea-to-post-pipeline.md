---
stepsCompleted: ['step-01-discovery', 'step-02-classification', 'step-03-requirements', 'step-04-tools', 'step-05-plan-review', 'step-06-design-validated']
created: 2026-01-27
reviewedDate: 2026-01-27
approvedDate: 2026-01-27
designedDate: 2026-01-27
validatedDate: 2026-01-27
status: DESIGN_VALIDATED_READY_FOR_FOUNDATION
workflowName: idea-to-post-pipeline
targetPath: standalone_custom
reviewMethod: party-mode-5-experts
designApproach: single-main-menu-8-modes-validated-optimized
totalStepFiles: 35-40
---

# Workflow Creation Plan: idea-to-post-pipeline

## Discovery Notes

**User's Vision:**
Create a system that transforms raw ideas into structured, high-converting Telegram posts through research, angle expansion, and selective development.

**Who It's For:**
Solo entrepreneur/marketer (God) selling LLM expertise to founders, marketers, and agency owners.

**What It Produces:**
Finished Telegram posts (text + emoji + formatting) with 3 variants (500/250/100 symbols), structured as: hook → problem → solution → trigger → CTA

**Key Insights:**
- One raw idea → 5-10 angle variants through research (validated by relevance + data availability + audience fit)
- Scalable content calendar (one idea = week of posts)
- Based on fresh data (TTL 7-14 days), best practices, market trends
- MVP with CSV files for idea accumulation + local editing
- Tracks post performance (CTR, engagement) to optimize future posts
- **Feedback loops:** Analytics insights → generate recommendations → suggest new ideas
- **Idea validation:** Quality gates before research (specific? researchable? audience clear? not duplicate?)
- **Offline mode:** Graceful fallback to cached research if internet unavailable
- **Export ready:** Posts can be exported to Telegram/Instagram/other platforms
- **Auto-backup:** Daily automated backups with recovery capability

---

## Classification Decisions

**Workflow Name:** `idea-to-post-pipeline`
**Target Path:** Standalone custom (local only)

### 4 Key Structural Decisions:

1. **Document Output:** `true`
   - Creates persistent post documents
   - Output format: markdown text with emoji + formatting
   - Stored in `posts_content.csv` and individual post files

2. **Module Affiliation:** `standalone` (Local-first, Cloud-ready)
   - Not part of BMB, BMM, CIS, or BMGD
   - Custom location for this user
   - Standard variables only
   - **Note:** MVP = local CSV files, but architecture supports future migration to cloud (cloud-ready DB models)

3. **Session Type:** `continuable` ✅ **MULTI-SESSION**
   - Session 1: Idea capture + research initiation
   - Session 2: Research completion + angle expansion
   - Session 3: Angle selection + post creation
   - Session 4: Post review + refinement
   - Can span multiple days between sessions
   - State tracking: stepsCompleted + lastStep + activeIdea context

4. **Lifecycle Support:** `tri-modal with versioning`
   - **Create (steps-c/):** Idea → research → expand → create post
   - **Edit (steps-e/):** Modify existing posts, refactor angles
   - **Validate (steps-v/):** Quality check posts, ensure CTR potential, compliance
   - **Versioning:** All posts maintain full edit history (v1, v2, v3, etc.)
   - **Archival:** Old/underperforming posts can be archived (preserved for reference)

---

## Structural Implications

### Step Files Required:

**CREATE MODE (steps-c/):**
- `step-01-init.md` → Spark the idea (raw thought capture)
- `step-01b-continue.md` → Resume from previous session
- `step-02-research.md` → Deep dive research (web + MCP)
- `step-03-angles.md` → Expand into 5-10 angle variants
- `step-04-selection.md` → User picks one angle to develop
- `step-05-structure.md` → Apply post structure (hook/problem/solution/trigger/CTA)
- `step-06-write.md` → Compose full post
- `step-07-variants.md` → Create 3 length variants (500/250/100)
- `step-08-polish.md` → Final quality pass

**EDIT MODE (steps-e/):**
- `step-e-01-load.md` → Load existing post/idea
- `step-e-02-choose-edit.md` → What to modify
- `step-e-03-apply.md` → Apply changes
- `step-e-04-review.md` → Review edits

**VALIDATE MODE (steps-v/):**
- `step-v-01-load.md` → Load post to validate
- `step-v-02-structure-check.md` → Hook/problem/solution/trigger/CTA present?
- `step-v-03-quality.md` → Tone, emoji, formatting intact?
- `step-v-04-ctr-potential.md` → Likely to get 2-5% CTR?
- `step-v-05-report.md` → Generate validation report

### Data/Support Files:
- `data/post-template.md` — Template for post structure
- `data/angles-library.csv` — Reference library of angle types
- `data/personas.csv` — Target personas (Founder, Marketer, Agency Owner)
- `data/triggers.csv` — Marketing triggers reference
- `data/cta-templates.csv` — CTA examples by stage (ToFu/MoFu/BoFu)

### Output Structure:

**Workflow Files:**
```
_bmad-output/
└── bmb-creations/
    └── workflows/
        └── idea-to-post-pipeline/
            ├── workflow.md (main definition)
            ├── data/ (shared resources)
            ├── steps-c/ (create steps)
            ├── steps-e/ (edit steps)
            └── steps-v/ (validate steps)
```

**Content Base (alongside workflow):**
```
content_generation_system/
│
├─ posts_index.csv              ← CSV index for search/filtering
│
├─ /posts/                       ← MAIN POST LIBRARY (by date)
│  ├─ 2026-01-27_idea-1_angle-3_high-ctr.md
│  ├─ 2026-01-28_idea-2_angle-1_medium.md
│  └─ ...
│
├─ /posts_by_topic/             ← TAXONOMY folders (quick access)
│  ├─ automation/
│  ├─ pricing/
│  ├─ crisis/
│  └─ ...
│
└─ /posts_by_performance/       ← PERFORMANCE folders
   ├─ high_ctr_4%+/
   ├─ medium_ctr_2-4%/
   └─ low_engagement/
```

**Post File Format:**
```markdown
---
id: post_001
date: 2026-01-27
idea_id: 1
angle: angle_3
topic: automation
target_persona: agency_owner
platform: telegram
views: 550
ctr: 5.82%
comments: 12
reposts: 4
status: published
version: 1
---

# 🚀 ИИ заменит твоего помощника

[Full post content with emoji + formatting]
```

### Session Management:
- Uses `stepsCompleted` tracking in plan frontmatter
- Each step appends itself to completed list
- `step-01b-continue.md` checks for prior progress
- User can pause after any step and resume later

### Continuable Features:
- Saves research findings between sessions
- Preserves angle list for later selection
- Can return to same idea 3+ times to create multiple posts
- Maintains post version history

---

## Requirements

### Flow Structure & Loops

**Pattern:** Multi-looping with branching (8 modes + 3 main feedback loops)

**Core Loops:**
- **Loop 1 (Research → Creation):** [2] Research idea → identify 5-10 angles → [3] Write post → test → publish
- **Loop 2 (Refinement):** [3] Write → feedback → [5] Edit → improve → finalize
- **Loop 3 (Metrics → Ideas):** [7] Analytics → insights → [7b] Recommendations → [1] New ideas

### Workflow Modes (8 Operations):

**[1] Добавить новую идею**
- User interaction: COLLABORATIVE (80% user, 20% assistant)
- SLA: 5 minutes
- Flow:
  - User provides raw idea
  - I ask clarifying questions: source, target persona, pain type, category
  - I validate idea (concrete? researchable? audience clear? not duplicate?)
  - Store in `ideas_inbox.csv` with full metadata
  - Ask: add another idea? → Loop enabled
- Validation rules:
  - Idea must be specific (not too broad)
  - Must have available data for research
  - Target audience must be clear
  - No duplicate with existing ideas

**[2] Выбрать и исследовать идею**
- User interaction: AUTONOMOUS (10% user, 90% assistant)
- SLA: 45 min for 1 idea, 90 min for batch of 3 (with sub-agents)
- Flow:
  - Show ideas with "new" status (optionally filtered)
  - User selects one or multiple
  - For each: conduct web research (5-7 sources) → identify 5-10 semantic angle variants
  - Evaluate angles by: relevance score, data availability, audience fit
  - Save to `ideas_research.csv` + research notes
  - Show variant list with descriptions & scores
  - Ask: research another idea? → Loop enabled
- Data freshness: TTL = 7-14 days for cached research
- Parallel processing: Sub-agents for batch research

**[3] Превратить идею в пост**
- User interaction: COLLABORATIVE (50% user, 50% assistant)
- SLA: 30 min for 1 post, 60 min for batch of 3 (with sub-processes)
- Flow:
  - Show list of research variants with scores
  - User selects one angle
  - Ask clarifying questions: tone, trigger type, target persona (Advanced Elicitation)
  - Write draft (500 chars) → post structure: hook → problem → solution → trigger → CTA
  - Get user feedback/approval
  - Write final + 2 variants (500/250/100 chars) in parallel
  - Quality validation check (emoji, formatting, CTR potential)
  - Save to post file + `posts_index.csv`
  - Ask: develop another variant from same idea? → Loop enabled

**[4] Выбрать пост из базы**
- User interaction: AUTONOMOUS (20% user, 80% assistant)
- SLA: 2 minutes
- Flow:
  - Quick search or advanced filters (by date/idea/theme/CTR/status/semantic similarity)
  - Show filtered list with metadata
  - User selects post
  - Display: full text + all metadata + performance metrics + related posts
  - Ask: next action (edit/merge/archive/back) → branching

**[5] Редактировать пост**
- User interaction: COLLABORATIVE (40% user, 60% assistant)
- SLA: 15 minutes per edit iteration
- Flow:
  - Load post with version history
  - Present improvement checklist: hook appeal, problem clarity, solution quality, trigger strength, CTA effectiveness, emoji placement, formatting
  - User selects improvements needed
  - I rework those sections
  - Iterate until satisfied
  - Save as new version (preserve history)

**[6] Объединить несколько постов**
- User interaction: COLLABORATIVE (50% user, 50% assistant)
- SLA: 20 minutes
- Flow:
  - Show post list
  - User selects 2-3 posts
  - Display side-by-side with key components highlighted (Party Mode for multi-perspective analysis)
  - I analyze and propose optimal combination (which hook/problem/solution/CTA from which post)
  - User agrees or modifies
  - I create hybrid post
  - Save with source references

**[7] Посмотреть статистику**
- User interaction: AUTONOMOUS + Recommendations (70% assistant, 30% user feedback)
- SLA: 10 minutes
- Flow:
  - Show dashboard: top posts by CTR, top ideas, top themes, top triggers, trending angles
  - Provide analysis: which content types work best, actionable recommendations
  - Ask for deeper dive: by period/persona/theme
  - Show detailed metrics + competitive insights

**[7b] Recommendations (Feedback Loop Integration)**
- Based on analytics insights
- Flow:
  - Analytics identifies top-performing angle (e.g., "Scaling" = 5.8% CTR)
  - Recommendation: "Create more posts on scaling"
  - I propose: "Add 3 new ideas on scaling topic?"
  - If yes: batch suggest ideas + auto-add to inbox

**[8] Управление базой**
- User interaction: AUTONOMOUS (5% user, 95% assistant)
- SLA: 5 minutes
- Flow:
  - Automated daily backups to `/backup/` folder
  - CSV validation & repair
  - Archive old posts
  - Organize by topic/performance
  - Export posts (to Telegram/social platform)

### Branching Logic
From any mode [1-8]:
- User can return to **Main Menu**
- Select different mode
- Or continue with Loop (if enabled)

### Interaction Style:

**Overall:** HIGHLY COLLABORATIVE + MOSTLY AUTONOMOUS

**Per-Mode Breakdown:**
| Mode | Collaboration % | Role |
|------|-----------------|------|
| [1] Add | 80/20 | You speak, I add |
| [2] Research | 10/90 | I execute autonomously |
| [3] Write | 50/50 | Back-and-forth refinement |
| [4] Search | 20/80 | I find, you select |
| [5] Edit | 40/60 | You request, I execute |
| [6] Merge | 50/50 | Joint synthesis |
| [7] Analytics | 30/70 | I analyze, you ask questions |
| [8] Manage | 5/95 | Fully automated |

### Input Requirements:

- Raw ideas (voice, text, spontaneous thoughts)
- User selections from lists (id-based)
- User feedback/approvals on drafts
- Performance data (views, clicks, comments) for stats
- Validation of idea quality before research

### Output Specifications:

- **Posts:** Markdown files with YAML frontmatter + formatted text with emoji
- **Location:** `/posts/YYYY-MM-DD_idea-X_angle-Y_v{version}.md`
- **CSV indices:** `posts_index.csv`, `ideas_research.csv`, `ideas_inbox.csv`
- **Format:** Free-form markdown (minimal structure, content-driven)
- **Version tracking:** Full history preserved in post file (version numbers + timestamps)

### Success Criteria:

- **Quality Target:** 2-3% CTR on first posts (measuring after 2 weeks)
- **Volume Target:** 5+ posts per week from 1-2 ideas
- **Reuse Rate:** 40%+ of angles developed (not always new)
- **Timeline:** Reach targets within 4 weeks from start
- **Posts match tone:** Raw, direct, authentic (like real person)
- **Base accumulation:** Posts stored for analysis & future reference
- **Metrics inform strategy:** Top-performing angles drive future ideas

### Interaction Style:

**Overall:** HIGHLY COLLABORATIVE + MOSTLY AUTONOMOUS
- [1-2]: User selects/decides, I execute
- [3,6]: Conversational with my analysis + user refinement
- [5]: Structured checklist approach
- [7]: Advisory (I recommend, user can explore deeper)

### Input Requirements:

- Raw ideas (voice, text, spontaneous thoughts)
- User selections from lists (id-based)
- User feedback/approvals on drafts
- Performance data (views, clicks, comments) for stats

### Output Specifications:

- **Posts:** Markdown files with YAML frontmatter + formatted text with emoji
- **Location:** `/posts/YYYY-MM-DD_idea-X_variant-Y.md`
- **CSV indices:** `posts_index.csv`, `ideas_research.csv`, `ideas_inbox.csv`
- **Format:** Free-form markdown (minimal structure, content-driven)

### Success Criteria:

- Workflow creates production-ready posts (2-5% CTR potential)
- Base accumulates posts for reuse/analysis
- Statistics inform future content strategy
- User can rapidly generate multiple posts from one idea
- Posts match tone (raw, direct, like real person) with proper emoji + formatting

### Instruction Style:

- **Intent-based** with collaborative elements
- Conversational (not interrogative)
- Provide recommendations when user asks
- Respect user's final decisions
- Ask clarifying questions (1-2 at a time)

---

---

## Tools Configuration

### Core BMAD Workflows (Optional Deep-Dive Modes)
- **Party Mode:** ✅ INCLUDED (optional for heavy analysis)
  - Integration point: Mode 6 (semantic post merging analysis) + Mode 7 (multi-perspective stats analysis)
  - Purpose: Collaborative analysis from multiple expert perspectives
  - Note: Can be skipped for lightweight workflows, engaged for critical decisions

- **Advanced Elicitation:** ✅ INCLUDED
  - Integration points: Mode 3 (post composition clarification), Mode 2 (research validation)
  - Purpose: Deep exploration through Socratic questioning, counterfactual analysis
  - Use case: Ensure post clarity and maximum impact

- **Brainstorming:** ✅ INCLUDED
  - Integration point: Mode 2 (semantic angle expansion from research findings)
  - Purpose: Divergent thinking to generate 5-10 development variants
  - Trigger: When research yields initial data but angles not clear

### LLM Features
- **Web-Browsing:** ✅ INCLUDED (Core)
  - Use case: Mode 2 research phase - real-time data, trends, best practices, statistics
  - Scope: 5-7 sources per idea for fresh, current information
  - Fallback: Cached research if internet unavailable (TTL 7-14 days)
  - Error handling: Graceful degradation if search fails

- **File I/O:** ✅ INCLUDED (Core)
  - Operations: Read/write CSV files (ideas_inbox, ideas_research, posts_index), markdown post files
  - Scope: All modes require persistent file operations
  - Backup: Automated daily backups to `/backup/` folder
  - Recovery: Automatic CSV validation & repair on load

- **Sub-Agents:** ✅ INCLUDED (Optional for Batch)
  - Use case: Mode 2 - parallel research on multiple ideas simultaneously
  - Architecture:
    - Sub-Agent 1: Web Research (search_web + scrape tools)
    - Sub-Agent 2: Data Analysis (aggregation + scoring)
    - Sub-Agent 3: Recommendation (insight generation)
  - Benefit: Faster research completion for batch operations (3 ideas in 90 min vs 135 min sequential)

- **Sub-Processes:** ✅ INCLUDED (Optional for Parallel)
  - Use case: Mode 3 variant generation (500/250/100 char variants in parallel), Mode 7 aggregating stats
  - Benefit: Non-blocking composition and data aggregation
  - Scope: Parallel execution of independent tasks

### Memory Systems
- **Sidecar-file (Session Continuity):** ✅ INCLUDED (Core)
  - Type: Persistent workflow state
  - Tracking: stepsCompleted array, lastStep, activeIdea, activeResearch, session context
  - Purpose: Resume multi-session workflows without losing progress
  - Implementation: Frontmatter in workflow-plan + session context file

- **Vector-Database (Semantic Search):** ✅ INCLUDED (Optional for Advanced)
  - Tool: Chroma or Qdrant vector DB
  - Use case: Mode 4 intelligent post retrieval by semantic similarity
  - Benefit: Find related posts by meaning, not just keywords (e.g., "automation" finds "efficiency" posts)
  - Scope: Embeddings for posts, ideas, angles for intelligent recommendations
  - Integration: Auto-embed posts after creation, queryable by semantic search
  - Note: Optional for MVP, enables smart recommendations in future

### MCP Server Configuration (Required for Advanced Features)

**MVP (Minimum Viable Product):**
- ✅ CSV Manager (built-in file I/O)
- ✅ Web Search (real-time research)

**Enhanced Features (Optional):**
- ✅ Analytics Engine - Aggregate metrics, generate reports
  - Tools: aggregate_metrics, top_performers, trend_analysis
  - Transport: Stdio

- ✅ Vector Search - Semantic post similarity
  - Tools: semantic_search, similarity_score, recommend_similar
  - Transport: Stdio

### CSV Operations
- **Core Files:** ideas_inbox.csv, ideas_research.csv, posts_index.csv
- **Operations:**
  - read_csv: Load data with filters
  - write_csv: Create new entries
  - append_csv: Add to existing data
  - filter_csv: Query by multiple criteria
  - aggregate_csv: Calculate metrics (CTR, avg engagement)
  - sort_csv: Top performers, recent posts
- **Error Handling:**
  - Corrupted file detection
  - Automatic repair attempt
  - Fallback to backup on failure

### External Integrations (Optional)
- **Platform Export:** Mode 8 export to Telegram/Instagram/LinkedIn
  - Requires: Platform API keys (user-provided)
  - Format: Post + metadata → platform-specific format
  - Status: Ready for future implementation

### Installation & Dependencies

**MVP Setup (Zero Additional Dependencies):**
- Standard Python 3.8+ with built-in file I/O
- Web search via built-in tools
- No additional packages required
- Ready to deploy immediately

**Enhanced Setup (Optional Integrations):**
- Chroma or Qdrant for vector search: `pip install chroma-db` or similar
- Platform APIs: Telegram Bot API, Instagram Graph API (user configures)
- MCP servers: Use included MCP transport layer

**Scalability Notes:**
- Local-first MVP (CSV files = portable, no DB required)
- Cloud-ready architecture (can migrate to PostgreSQL + Pinecone later)
- Batch processing support (handle 10+ posts without bottleneck)

---

## Party Mode Review Summary (Step 05 ✅ COMPLETE)

### 5-Expert Consilium Analysis
**Experts:** Архитектор UX | Pragmatist Engineer | Growth Lead | Perfectionista | Devil's Advocate

### ✅ What Stayed (Validated):
- 8-mode structure (logical, complete, addresses all use cases)
- Continuable sessions (excellent for multi-day workflows)
- Tri-modal lifecycle (Create/Edit/Validate)
- Success Criteria (2-3% CTR, 5+ posts/week, 4-week ramp)
- Core tools selection (Party Mode, Advanced Elicitation, Brainstorming)

### ⚠️ What Was Enhanced:
1. **Requirements:** Added SLA for each mode (5 min to 90 min)
2. **Requirements:** Added interaction % breakdown per mode (10/90 to 80/20)
3. **Requirements:** Defined 3 main loops (Research→Creation, Write→Refinement, Analytics→Ideas)
4. **Requirements:** Added branching logic (return to menu from any mode)
5. **Discovery:** Added validation criteria, TTL, feedback loops, export, offline mode, auto-backup
6. **Classification:** Clarified "Local-first, Cloud-ready" + versioning strategy
7. **Tools:** Explicitly mapped MCP servers (CSV Manager, Web Search, Analytics Engine, Vector DB)
8. **Tools:** Detailed Sub-Agents architecture (3 agents for parallel research)
9. **Tools:** Added error handling (corrupted files, failed searches, graceful fallback)
10. **Tools:** Clarified MVP vs Enhanced features (optional advanced tools)

### 🚨 Risks Identified & Mitigated:
| Risk | Mitigation |
|------|-----------|
| Cognitive overload (8 modes) | Logical grouping + branching to menu keeps it manageable |
| Data quality depends on idea quality | Added validation gates before research |
| Web search dependency | Offline mode with 7-14 day cached data |
| Success criteria too optimistic | Adjusted to 2-3% CTR (realistic for first batch) |
| "ZERO DEPENDENCIES" misleading | Clarified: MVP = zero, Enhanced = optional integrations |
| Party Mode/Advanced Elicitation OVERKILL | Marked as optional deep-dive modes, not required for MVP |

### 📋 Plan Status: APPROVED FOR DESIGN ✅
All sections reviewed, feedback incorporated, ready for Step 06.

---

## Workflow Structure Design (STEP-06 ✅ COMPLETE + VALIDATED & OPTIMIZED)

### Design Decisions (Validated by User + Enhanced)

**Approach:** Single Main Menu Workflow + 8 Self-Contained Modes

**Architecture with Explicit Sub-Steps:**
```
workflow.md (entry)
  ↓
step-01-init.md (welcome + continuation check)
  ↓
step-01b-continue.md (resume from workflow_state.json if needed)
  ↓
step-00-menu.md (MAIN MENU — central hub)
  ├─ [1] Add idea → step-01-add-idea.md → LOOP or BACK
  ├─ [2] Research → step-02a-load → 02b-select → 02c-research → 02d-results → LOOP or BACK
  ├─ [3] Write post → step-03a-select-idea → 03b-select-angle → 03c-draft (with feedback LOOP) → 03d-variants → 03e-finalize → LOOP or BACK
  ├─ [4] Search → step-04a-search → 04b-results → 04c-actions → BACK
  ├─ [5] Edit → step-05a-load → 05b-select → 05c-edit (with iteration LOOP) → 05d-review → BACK
  ├─ [6] Merge → step-06a-select → 06b-analyze → 06c-suggest → 06d-create → BACK
  ├─ [7] Analytics → step-07a-dashboard → 07b-deep-dive → 07c-recommendations (optional jump to [1]) → BACK
  └─ [8] Manage → step-08a-options → 08b-execute → BACK
```

**Session Support:** ✅ Continuable (multi-session with workflow_state.json sidecar)
**State Management:**
```json
{
  "workflow_id": "idea-to-post-pipeline",
  "session_id": "2026-01-27-v1",
  "stepsCompleted": ["step-01-init", "step-01-add-idea (x3)", "step-02c-research"],
  "currentStep": "step-02d-results",
  "lastUpdated": "2026-01-27 21:30",
  "context": {
    "selectedIdea": 1,
    "selectedAngle": "angle_3",
    "draftVersion": 1
  }
}
```

**Lifecycle:** ✅ Tri-modal
- CREATE (steps-c/): Main workflow with embedded validation
- EDIT (steps-e/): Future — standalone edit mode
- VALIDATE (steps-v/): Future — batch quality validation

**Subprocess Optimization:**
- **Mode [2] Research:** Pattern 3+4 (parallel research on 3 ideas simultaneously)
  - Sub-process 1-3: Web search in parallel → 3x faster (45 min vs 135 min)
- **Mode [3] Write:** Pattern 4 (parallel variant generation + feedback loop)
  - Sub-process: Draft revision loop → iterative refinement
  - Sub-process: 3 variants generated in parallel
- **Mode [7] Analytics:** Pattern 3 (data loading + aggregation)
  - Sub-process 1-3: Load CSV files in parallel → fast dashboard

**Feedback Loops (Cross-Mode Connectivity):**
- **Loop 1:** [2] Research → [3] Write (angles → posts)
- **Loop 2:** [3] Draft → feedback → revise (iterative refinement)
- **Loop 3:** [7] Analytics → recommendations → [1] Add idea (insights → new ideas)

**Total Step Files:** ~35-40 files (organized by mode)

**Optimized File Structure:**
```
workflows/idea-to-post-pipeline/
├── workflow.md (main entry + overview)
│
├── data/
│   ├── csv-templates/
│   │   ├── ideas_inbox_template.csv
│   │   ├── ideas_research_template.csv
│   │   ├── posts_content_template.csv
│   │   ├── metrics_tracking_template.csv
│   │   └── angles_library_template.csv
│   ├── checklist-templates/
│   │   ├── idea-validation-checklist.md
│   │   ├── post-quality-checklist.md
│   │   └── edit-improvements-checklist.md
│   └── reference/
│       ├── interaction-styles.md
│       ├── timing-sla.md
│       ├── success-criteria.md
│       └── faq.md
│
├── steps/
│   ├── step-00-menu.md (Main Menu hub)
│   ├── step-01-init.md (Welcome + continuation check)
│   ├── step-01b-continue.md (Resume session)
│   │
│   ├── mode-01-add-idea/
│   │   └── step-01-add-idea.md
│   │
│   ├── mode-02-research/
│   │   ├── step-02a-load.md
│   │   ├── step-02b-select.md
│   │   ├── step-02c-research.md (with subprocess optimization)
│   │   └── step-02d-results.md
│   │
│   ├── mode-03-write-post/
│   │   ├── step-03a-select-idea.md
│   │   ├── step-03b-select-angle.md
│   │   ├── step-03c-draft.md (with feedback loop)
│   │   ├── step-03d-variants.md (with subprocess parallel generation)
│   │   └── step-03e-finalize.md
│   │
│   ├── mode-04-search-post/
│   │   ├── step-04a-search.md
│   │   ├── step-04b-results.md
│   │   └── step-04c-actions.md
│   │
│   ├── mode-05-edit-post/
│   │   ├── step-05a-load.md
│   │   ├── step-05b-select.md
│   │   ├── step-05c-edit.md (with iteration loop)
│   │   └── step-05d-review.md
│   │
│   ├── mode-06-merge-posts/
│   │   ├── step-06a-select.md
│   │   ├── step-06b-analyze.md
│   │   ├── step-06c-suggest.md
│   │   └── step-06d-create.md
│   │
│   ├── mode-07-analytics/
│   │   ├── step-07a-dashboard.md (with subprocess aggregation)
│   │   ├── step-07b-deep-dive.md
│   │   └── step-07c-recommendations.md
│   │
│   └── mode-08-manage/
│       ├── step-08a-options.md
│       └── step-08b-execute.md
│
├── subprocesses/ (optional — for Pattern 3+4 optimization)
│   ├── subprocess-parallel-research.md
│   ├── subprocess-draft-feedback-loop.md
│   └── subprocess-aggregate-metrics.md
│
└── DESIGN_NOTES.md (design decisions + rationale)
```

### Key Design Decisions Documented

1. **Architecture:** Single workflow (not 8 separate) → better state management, feedback loops
2. **Session Support:** Continuable with workflow_state.json → pause/resume capability
3. **Lifecycle:** Tri-modal (CREATE now, EDIT + VALIDATE future)
4. **Subprocesses:** Parallel execution in modes 2, 3, 7 → 3x speed improvement
5. **Feedback Loops:** Research→Write, Draft→Refine, Analytics→Ideas
6. **State Management:** stepsCompleted + context object → full continuity
7. **File Organization:** By mode (mode-01, mode-02...) → easier navigation
8. **Error Handling:** Validation at each step + graceful fallbacks

## STEP-07: FOUNDATION (✅ IN PROGRESS)

### Phase 1: Core Foundation Files ✅ COMPLETE (4/4)
- ✅ `workflow.md` — Master entry point with 4-mode routing
- ✅ `step-01-init.md` — Welcome + continuation detection
- ✅ `step-01b-continue.md` — Session resumption with state loading
- ✅ `step-00-menu.md` — Main menu hub (4 modes)

**Status**: Foundation ready for step file generation

### Phase 2: Priority 1 Files (IN PROGRESS)
- **CREATE Mode Core** (8 sub-modes, ~26 files):
  - [ ] Mode C-01: Add idea (1 file)
  - [ ] Mode C-02: Research (4 files) — with subprocess optimization
  - [ ] Mode C-03: Write post (5 files) — with feedback loops
  - [ ] Mode C-07: Analytics (3 files) — with metrics aggregation
  - [ ] Modes C-04, C-05, C-06, C-08 (defer to Phase 3)

- **YOLO Mode** (6 files) — MVP showcase feature:
  - [ ] step-yolo-01-input.md — Specification parser
  - [ ] step-yolo-02-parallel-execute.md — Parallel engine
  - [ ] step-yolo-03-self-check.md — Auto-validation (5 checks)
  - [ ] step-yolo-04-auto-improve.md — Auto-fix engine
  - [ ] step-yolo-05-variants.md — Variant generator
  - [ ] step-yolo-06-summary.md — Results presentation

### Phase 3: Data & Templates (IN PROGRESS)
- [ ] CSV templates (5 files): ideas_inbox, ideas_research, posts_content, metrics_tracking, angles_library
- [ ] Checklist templates (5 files)
- [ ] Reference files (4 files)

### Phase 4: EDIT Mode (Defer to later)
- 24 files organized by operation type

### Phase 5: VALIDATE Mode (Defer to later)
- 24 files organized by validation type

### Phase 6: Subprocesses (Defer to later)
- 7 optimization files

## Execution Strategy

**Sequential Batching** (optimize context usage):
1. Foundation files (DONE) ✅
2. YOLO mode (NEXT — 6 files)
3. CREATE core modes (NEXT — 13 files minimum)
4. Data templates (NEXT — 14 files)
5. Complete CREATE (C-04-C-08: 17 files)
6. EDIT mode (24 files)
7. VALIDATE mode (24 files)
8. Subprocesses (7 files)

**Estimated Timeline**:
- Phase 1: 5 min ✅
- Phase 2-4: 30-45 min (aggressive batch generation)
- Phase 5-8: 30-60 min (remaining modes)
- **Total: 60-120 minutes for all 105+ files**

