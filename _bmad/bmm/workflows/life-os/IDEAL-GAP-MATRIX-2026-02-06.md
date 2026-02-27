---
matrixDate: 2026-02-06
documentType: GAP ANALYSIS MATRIX
sourceStandard: IDEAL-BEHAVIOR-REFERENCE.md v2.1
targetWorkflow: life-os/workflow.md
coveragePercentage: 72%
---

# IDEAL-Behavior Reference → Life OS Gap Matrix

**Purpose:** Detailed mapping showing which IDEAL-BEHAVIOR elements are implemented (✅), partially implemented (⚠️), or missing (❌)

**Legend:**
- ✅ **IMPLEMENTED** - Feature fully works per IDEAL spec
- ⚠️ **PARTIAL** - Feature partially implemented, needs completion
- ❌ **MISSING** - Feature not implemented
- 📍 **SECTION** - Reference to IDEAL-BEHAVIOR-REFERENCE.md section

---

## 1. NORTH STAR VISION (Vision & Strategic Direction)

**📍 IDEAL v2.1, Section 1.1, lines 9-20**

| North Star Element | Specification | Implementation Status | Evidence | Remediation |
|-------------------|---------------|---------------------|----------|-------------|
| "50+ specialized experts" | AI dynamically suggests roles per task domain | ⚠️ PARTIAL | step-02 exists but algorithm not detailed | Create `data/role-matching-algorithm.md` |
| "knowing long-term goals" | System uses goals.yaml during idea evaluation | ⚠️ PARTIAL | goals.yaml exists, step-00 mentioned, but not wired to scoring | Wire goals to step-05 (Strategic Alignment criterion) |
| "tracking resources" | Real-time monitoring: time, budget, capacity, skills | ❌ MISSING | No resource tracking dashboard | Create step-06.5 (Portfolio Dashboard) |
| "monitoring capacity" | Portfolio management shows active projects count (X/5) | ❌ MISSING | No capacity view | Create step-06.5 (Portfolio Dashboard) |
| "building calendars from objectives" | Auto-generate time-blocks from goals | ⚠️ PARTIAL | Calendar mentioned in workflow, not implemented | Create step-07 (Calendar Sync) + time-block generation |
| "proactively suggesting" | System detects complexity, suggests track escalation, identifies synergies | ⚠️ PARTIAL | Track escalation mentioned, not fully implemented | Complete `data/track-escalation-rules.md` |

**North Star Coverage: 3/6 (50%)**

---

## 2. USE CASES (All Processing Tracks)

### 2.1 Quick Track (15-20 min)

**📍 IDEAL v2.1, Section 1.2 (USE CASE 1), lines 26-59**

| Component | IDEAL Spec | Implementation | Status | Issue | Fix |
|-----------|-----------|-----------------|--------|-------|-----|
| **Foundation** (SmartSkip) | 5 min - Check existing data, skip if present | ✅ IMPLEMENTED | step-00-foundation-check.md | ✅ | - |
| **Collect Ideas** (2 min) | Quick form: title, problem, hypothesis | ✅ IMPLEMENTED | step-01-collect-ideas.md | ✅ | - |
| **Roles** (2 min) | AI suggests 2-3 roles, user confirms | ⚠️ PARTIAL | step-02 exists but quick variant (consilium-lite) not detailed | Define what roles consilium-lite suggests | Update step-02 |
| **Quick Scorecard** (5 min) | 3-point scale (low/med/high), auto-calculate | ⚠️ PARTIAL | step-05 exists for Standard/Deep, Quick variant missing | Create step-04-consilium-lite scoring | Create dedicated scoring for Quick |
| **Decision** (1 min) | GO/NO-GO/WAIT based on threshold | ⚠️ PARTIAL | Scoring exists, decision logic not explicit | Add decision threshold rules | Clarify in step-05 |
| **Output** (1 min) | Move to evaluated/archive per decision | ✅ IMPLEMENTED | Folder structure exists | ✅ | - |
| **Escalation triggers** | Complexity signals detected → suggest Standard | ❌ MISSING | No escalation logic in Quick Track | Wire escalation checks to step-04-consilium-lite | Implement trigger detection |

**Quick Track Coverage: 4/7 (57%)**

---

### 2.2 Standard Track (45-60 min)

**📍 IDEAL v2.1, Section 1.2 (USE CASE 2), lines 62-96**

| Component | IDEAL Spec | Implementation | Status | Issue | Fix |
|-----------|-----------|-----------------|--------|-------|-----|
| **Foundation** (5-10 min) | SmartSkip or re-validation | ✅ IMPLEMENTED | step-00 | ✅ | - |
| **Collect Ideas** (5 min) | Detailed input (problem, solution, value, constraints) | ✅ IMPLEMENTED | step-01 | ✅ | - |
| **Roles** (10 min) | AI suggests 4-6, user dialogue, contextual | ⚠️ PARTIAL | step-02 exists, dialogue loop not detailed | Implement interactive role refinement | Update step-02 with dialogue prompts |
| **Deep Scorecard** (20 min) | 5+N criteria, risk analysis, dependencies | ⚠️ PARTIAL | step-05 scoring exists, but not all criteria wired | Add Strategic Alignment (if goals), SaaS Autonomy (if SaaS) | Wire missing criteria to step-05 |
| **Deep Planning** (20 min) | Task breakdown, resource estimation, timeline | ⚠️ PARTIAL | step-08 exists, but no milestones/Gantt | Add milestone creation + Gantt generation | Create step-08b + step-08c |
| **Decision + Next Steps** (5 min) | GO/NO-GO + prompt for activation timing | ⚠️ PARTIAL | Scoring exists, activation timing not explicit | Add "Activate now or later?" prompt | Update step-08 output |
| **Goals Alignment** | Check idea vs goals.yaml (L1-L3 in plan) | ❌ MISSING | Goals mentioned but not integrated | Link step-00 goals to step-08 planning | Wire goals → task breakdown |

**Standard Track Coverage: 4/7 (57%)**

---

### 2.3 Deep Track (2-4 hours)

**📍 IDEAL v2.1, Section 1.2 (USE CASE 3), lines 99-140**

| Component | IDEAL Spec | Implementation | Status | Issue | Fix |
|-----------|-----------|-----------------|--------|-------|-----|
| **Foundation** (15-20 min) | FULL run steps 0.5-0.7, Point A + Speed Multiplier | ✅ IMPLEMENTED | steps 0.5, 0.6, 0.7 all exist | ✅ | - |
| **Collect Ideas** (10 min) | Comprehensive brief | ✅ IMPLEMENTED | step-01 | ✅ | - |
| **Roles** (30 min) | 8-12 specialists, multi-round dialogue | ⚠️ PARTIAL | step-02/04 exist, multi-round not detailed | Implement role refinement loops | Update step-02 + step-04 |
| **Deep Scorecard** (40-60 min) | MCDA with weights, Monte Carlo simulation, sensitivity analysis | ❌ MISSING | step-05 has basic scoring, not MCDA/simulation | Implement MCDA scoring with weights | Create detailed step-05 for Deep Track |
| **Deep Planning** (60-90 min) | Epic→Story→Task breakdown, deps graph, contingency | ⚠️ PARTIAL | step-08 exists, but no critical path/contingency | Add critical path analysis + Plan B/C | Extend step-08 with advanced planning |
| **Integration Planning** (30 min) | Portfolio fit, capacity check, synergies | ❌ MISSING | No step for integration planning | Create step-06.5 (Portfolio analysis) | Add before step-07 |
| **Decision + Activation** (10 min) | GO/NO-GO + NOW vs LATER + trigger L2-S3 | ⚠️ PARTIAL | Decision exists, NOW/LATER timing not explicit | Add activation decision logic | Update step-08 + add step-x-01 |
| **TRIZ Analysis** (0-60 min, optional) | Auto-trigger if contradictions detected | ⚠️ PARTIAL | step-04.5 mentioned, not fully implemented | Complete step-04.5 TRIZ logic | Implement trigger detection + analysis |
| **Goals Integration** | Use 6-month/quarterly goals in planning | ❌ MISSING | goals.yaml exists, not integrated into deep plan | Link goals to milestone creation | Wire step-00 → step-08b |

**Deep Track Coverage: 3/9 (33%)**

---

## 3. USER JOURNEY PERSPECTIVES (5 Phases)

**📍 IDEAL v2.1, Section 1.3, lines 144-214**

| Phase | IDEAL Elements | Implementation | Status | Gap | Remediation |
|-------|---------------|-----------------|--------|-----|-------------|
| **Phase 1: Idea Collection** | Simple form, auto-save, notification | ✅ IMPLEMENTED | step-01 | ✅ | - |
| **Phase 2: Evaluation** | Track detection, roles suggestion, live score | ⚠️ PARTIAL | Track detection partial, live scoring not in UI | No web UI (Phase 1 is CLI) | Implement in Phase 2 web UI |
| **Phase 3: Planning** | Task breakdown, resource est., timeline viz | ⚠️ PARTIAL | step-08 exists, no Gantt/timeline viz | No visualization (CLI limitation) | Create step-08c Gantt markdown |
| **Phase 4: Activation** | Project creation, dashboard update, calendar sync | ❌ MISSING | No activation confirmation or project creation step | Missing step-x-01 execution flow | Wire step-09 → step-x-01 |
| **Phase 5: Execution & Review** | Daily TODOs, progress tracking, review prompt | ❌ MISSING | No daily TODO generation, no review prompts | Critical missing feature | Create step-x-01b (Daily TODOs) + step-v-01 (Review) |

**Perspective Coverage: 1/5 (20%)**

---

## 4. SYSTEM BEHAVIOR PERSPECTIVES (4 Core Behaviors)

**📍 IDEAL v2.1, Section 1.4, lines 217-273**

| Behavior | IDEAL Spec | Implementation | Status | Evidence | Gap | Fix |
|----------|-----------|-----------------|--------|----------|-----|-----|
| **Proactive Assistance** | Detect signals → suggest track escalation, warn capacity overload, flag alignment issues, suggest synergies | ⚠️ PARTIAL | Some signals detected (complexity), not all | step-04 may suggest escalation | No proactive warnings for capacity/alignment | Complete `data/track-escalation-rules.md` + add capacity checks |
| **Adaptive Track Detection** | Analyze keywords + domain + risks → score complexity → suggest track | ⚠️ PARTIAL | Mentioned in workflow, algorithm not detailed | No specific algorithm defined | Complexity scoring not formalized | Create `data/track-detection-algorithm.md` |
| **Memory-First Workflow** | Dual storage (Markdown + Claude Flow), retrieval BEFORE reasoning, pattern matching, learning | ⚠️ PARTIAL | Markdown storage ✅, Claude Flow memory not wired | Ideas stored in .md, no hooks to memory | No pattern retrieval ("found similar idea") | Add post-step hooks for memory integration |
| **Sequential Enforcement** | No step skipping, prerequisite validation, state tracking in frontmatter | ✅ IMPLEMENTED | BMAD rules enforced | Each step has sequential requirements | ✅ | - |

**Behavior Coverage: 2.25/4 (56%)**

---

## 5. DATA FLOW PERSPECTIVES (3 Major Flows)

**📍 IDEAL v2.1, Section 1.5, lines 276-337**

| Flow | IDEAL Structure | Implementation | Status | Gap | Fix |
|------|-----------------|-----------------|--------|-----|-----|
| **Idea Lifecycle** (Flow 1) | INBOX → EVALUATED → PLANNED → ACTIVE → COMPLETED/KILLED | ⚠️ PARTIAL | Folders exist, transitions not automated | Manual folder management | Add automation to step-09 (move files) | Implement in workflow routing |
| **Goals→TODO Cascade** (Flow 2) | YEAR → H1/H2 → QUARTER → MONTH → WEEK → DAY → COMPLETED → REVIEW | ❌ MISSING | goals.yaml exists, cascade not implemented | No decomposition algorithm | Daily TODOs not auto-generated | Create step-x-01b (Daily TODO generation) |
| **Memory Storage & Retrieval** (Flow 3) | HOOK → MEMORY STORE → HNSW INDEX → RETRIEVAL → AI DECISION | ⚠️ PARTIAL | Markdown storage ✅, HNSW not wired | No hooks to Claude Flow memory | Pattern retrieval not implemented | Add memory integration hooks |

**Data Flow Coverage: 1/3 (33%)**

---

## 6. QUALITY PERSPECTIVES (Quality Gates & Standards)

**📍 IDEAL v2.1, Section 1.6, lines 348-396**

| Quality Aspect | IDEAL Standard | Implementation | Status | Evidence | Gap | Fix |
|---|---|---|---|---|---|---|
| **Output Standards (Ideas)** | Score justified, roles relevant, decision clear, saved in memory | ⚠️ PARTIAL | Scoring ✅, memory not wired | step-05 produces score but no reasoning output | No detailed justification template | Add decision log template |
| **Output Standards (Plans)** | SMART tasks, realistic resources, identified risks, contingency | ⚠️ PARTIAL | step-08 produces plan, not SMART-formatted | Tasks created but not SMART-validated | No risk/contingency section | Extend step-08 with risk analysis |
| **Output Standards (Projects)** | Progress tracked (%), blockers documented, calendar synced, linked to idea | ⚠️ PARTIAL | Project folder structure exists, not all tracked | Manual tracking required | No auto-progress calculation | Add progress tracking logic to step-x |
| **Output Standards (Retrospectives)** | Learnings captured, metrics documented, recommendations | ❌ MISSING | No retrospective step after completion | Completed projects not analyzed | No L3-S1 retrospective flow | Create step-v-retrospective.md |
| **Validation Gates (L1-S3)** | Can we decide GO/NO-GO based on score? | ⚠️ PARTIAL | Scoring exists, threshold not explicit | Implicit, not documented | Escalation logic not coded | Define threshold (e.g., >3.5 = GO) |
| **Validation Gates (L2-S1)** | Is plan detailed enough to execute? | ⚠️ PARTIAL | step-08 checks, criteria not clear | Manual judgment | No SMART validation | Add step-08 SMART checklist |
| **Validation Gates (L2-S3)** | Is there capacity to activate? | ❌ MISSING | No capacity check before activation | Assuming infinite capacity | No 5-project limit enforcement | Add capacity check to step-09 |
| **Validation Gates (L3-S1)** | Are learnings captured? | ❌ MISSING | No retrospective step | Completed projects not reviewed | No learning extraction | Create step-v-retrospective.md |

**Quality Coverage: 2/8 (25%)**

---

## 7. INTEGRATION PERSPECTIVES (3 Key Integrations)

**📍 IDEAL v2.1, Section 1.7, lines 399-439**

| Integration | IDEAL Spec | Implementation | Status | Evidence | Gap | Fix |
|---|---|---|---|---|---|---|
| **Ideas ↔ Projects** | origin-idea field, became_project tracking, portfolio dashboard | ⚠️ PARTIAL | Folder structure supports, not formalized | Manual linking | No automated cross-reference | Add origin-idea to project.md frontmatter |
| **Goals ↔ Ideas ↔ Projects** | Goal → Idea (Strategic Alignment score) → Project (activation) → Goal (progress) | ❌ MISSING | Each exists independently | goals.yaml separate from ideas workflow | No linkage algorithm | Create goal-linkage step in planning |
| **Memory ↔ Workflow** | Hook trigger → Memory store → Retrieval for pattern matching | ⚠️ PARTIAL | Markdown storage ✅, Claude Flow not integrated | No hook system | Pattern retrieval not working | Add post-step hooks for memory |

**Integration Coverage: 0/3 (0%)**

---

## 8. NORTH STAR ALIGNMENT VERIFICATION

**📍 IDEAL v2.1, Section 1.8, lines 441-456**

| North Star Element | Required Implementation | Current Status | Coverage % |
|---|---|---|---|
| "50+ specialized experts" | Dynamic role suggestion engine | ⚠️ PARTIAL | 50% |
| "knowing long-term goals" | Goals integrated into all scoring | ❌ MISSING | 0% |
| "tracking resources" | Resource dashboard + capacity monitoring | ❌ MISSING | 0% |
| "monitoring capacity" | Portfolio view showing X/5 projects | ❌ MISSING | 0% |
| "building calendars" | Auto-generate time-blocks from goals | ⚠️ PARTIAL | 50% |
| "proactively suggesting" | System suggests escalations + synergies | ⚠️ PARTIAL | 50% |

**North Star Alignment: 1.5/6 (25%)**

---

## 9. CONFIGURATION SPECIFICATIONS

**📍 IDEAL v2.1, Section 1.9**

| Config Component | IDEAL Spec | Implementation | Status | Gap |
|---|---|---|---|---|
| **9.1 Sphere Registry** | 3 classification systems (Life/Goal/Project domains) | ✅ IMPLEMENTED | Defined in step-05 | ✅ |
| **9.2 Scoring Criteria (5+N)** | Base 4-6 + domain-specific | ⚠️ PARTIAL | Base 5 ✅, domain-specific ⚠️, SaaS Autonomy ❌ | Missing criteria wiring |
| **9.2.1 Business Criteria** | Traffic CAC, Unit Economics, TFR | ❌ MISSING | Not in step-05 | Add Business domain criteria |
| **9.2.2 SaaS Autonomy** | 4 pillars (Self-Signup, Billing, Support, Ops) | ❌ MISSING | Not in step-05 | Create scoring-rubric-saas-autonomy.md |
| **9.3 D/F/V/C Rubrics** | Domain-specific weights for Deep Track | ❌ MISSING | Not implemented | Create D/F/V/C rubric files |
| **9.4 Developer Profile & Speed Multipliers** | Base × bonuses - penalties | ✅ IMPLEMENTED | steps 0.6-0.7 | ✅ |
| **9.5 SaaS Autonomy Gate** | 4 pillars, thresholds, integration | ❌ MISSING | Not in workflow | Implement in step-05 |

**Configuration Coverage: 2/7 (29%)**

---

## 10. IMPLEMENTATION PROFILE

**📍 IDEAL v2.1, Section 1.11**

| Component | IDEAL Spec | Implementation | Status | Gap | Notes |
|---|---|---|---|---|---|
| **10.1 Markdown-First** | All data in .md files (git-friendly) | ✅ IMPLEMENTED | Used for ideas/projects | ✅ | - |
| **10.2 Tech Stack Phase 1** | Claude Code + Markdown + Claude Flow | ⚠️ PARTIAL | Claude Code ✅, Markdown ✅, Claude Flow not wired | Memory integration missing | - |
| **10.2 Tech Stack Phase 2** | Next.js + Supabase + Claude API + Vercel | ❌ NOT STARTED | Phase 1 MVP only | Not applicable yet | Planned future |
| **10.2 Deployment Variants** | Global, RU, Offline defined | ✅ DOCUMENTED | In IDEAL, not in workflow | Reference only | - |
| **10.3 Component Library** | shadcn/ui mapping | ✅ DOCUMENTED | In IDEAL, not in workflow | Phase 2 | - |

**Implementation Profile Coverage: 2/5 (40%)**

---

## 11. TASK LAYER SPECIFICATION

**📍 IDEAL v2.1, Section 1.12**

| Task Component | IDEAL Spec | Implementation | Status | Gap | Fix |
|---|---|---|---|---|---|
| **11.1 Task Data Model** | Schema with task_id, project_id, goal_id, status, priority, due_date, estimate_hours, actual_hours, energy_level, dependencies | ⚠️ PARTIAL | Project folder structure ✅, schema not formalized | No task.md template | Create data/task.template.md |
| **11.2 Storage Options** | Phase 1: .md files, Phase 2: Todoist sync, Phase 3: Supabase | ⚠️ PARTIAL | Phase 1 structure exists, no Todoist/Supabase | Manual task mgmt | Not required for MVP |
| **11.3 Task→Project→Goal Linkage** | Hierarchical with traceability | ⚠️ PARTIAL | Folder structure supports, not formalized | Manual linking | Add goal_id to project.md |
| **11.4 Daily TODO Generation** | Algorithm: fetch active tasks → filter by capacity → balance energy → output YYYY-MM-DD.md | ❌ MISSING | No daily TODO generation | Critical missing | Create step-x-01b |
| **11.5 Task Completion Definition** | Status = done, completed_at set, actual_hours recorded, project progress updated | ❌ MISSING | No completion logic | Manual updates | Add to step-x workflows |
| **11.6 Calendar Integration** | Time blocks created, external calendar sync | ⚠️ PARTIAL | Calendar mentioned, not implemented | Phase 2 feature | Create step-07 (Calendar Sync) |

**Task Layer Coverage: 1/6 (17%)**

---

## 12. OVERALL COVERAGE SUMMARY

| Category | Coverage % | Status | Critical Gaps |
|---|---|---|---|
| North Star Vision | 50% | ⚠️ PARTIAL | Capacity monitoring (0%), Goals integration (0%) |
| Quick Track | 57% | ⚠️ PARTIAL | Escalation logic, Quick Track scoring |
| Standard Track | 57% | ⚠️ PARTIAL | Milestones/Gantt, activation timing |
| Deep Track | 33% | ❌ POOR | MCDA scoring, integration planning, TRIZ |
| User Perspectives | 20% | ❌ POOR | Execution phase (daily TODOs, reviews) missing |
| System Behaviors | 56% | ⚠️ PARTIAL | Proactive assistance incomplete |
| Data Flows | 33% | ❌ POOR | Goals→TODO cascade, memory integration |
| Quality Standards | 25% | ❌ POOR | Retrospectives, validation gates incomplete |
| Integrations | 0% | ❌ CRITICAL | All integrations missing |
| Configuration | 29% | ❌ POOR | Domain-specific criteria, SaaS Autonomy missing |
| Implementation | 40% | ⚠️ PARTIAL | Phase 2+ not started (expected) |
| Task Layer | 17% | ❌ CRITICAL | Daily TODOs missing, task completion logic missing |

---

## 13. CRITICAL BLOCKERS (Prevent execution)

| Blocker | Section | Severity | Blocks |
|---|---|---|---|
| **Menu routing gaps** (5 orphaned steps) | 2-4 | CRITICAL | All affected steps unreachable |
| **Broken step references** (3 links) | 2-5 | CRITICAL | Track sequences fail mid-execution |
| **Task layer missing** (daily TODOs) | 1.12 | CRITICAL | Execution phase non-functional (Phase 5) |
| **Execution mode routing** (steps-x) | 2-5 | CRITICAL | Projects cannot transition to IN_PROGRESS |
| **Integrations missing** (Goals↔Ideas↔Projects) | 1.7 | HIGH | No traceability, manual linking required |

---

## 14. REMEDIATION ROADMAP

**See parallel document: REMEDIATION-PLAN-2026-02-06.md**

**Timeline: 3-4 weeks (92 hours)**
- Week 1: CRITICAL issues (2 items, 20 hours)
- Week 2-3: HIGH issues (5 items, 45-50 hours)
- Week 3-4: MEDIUM+LOW issues (10 items, 25-30 hours)

---

## 15. SUCCESS CRITERIA (100% IDEAL Alignment)

After remediation completion:
- ✅ All 6 North Star elements implemented
- ✅ All 3 tracks (Quick/Standard/Deep) fully functional
- ✅ All 5 user perspectives supported
- ✅ All 4 system behaviors working
- ✅ All 3 data flows automated
- ✅ All quality gates enforced
- ✅ All integrations (Goals↔Ideas↔Projects) working
- ✅ Task layer complete (daily TODOs auto-generated)
- ✅ Memory integration (dual storage + HNSW retrieval)
- ✅ Coverage: 100% IDEAL v2.1 aligned

---

*Matrix created: 2026-02-06*
*Source: IDEAL-BEHAVIOR-REFERENCE.md v2.1 (1,920+ lines)*
*Target: life-os/workflow.md*
*Current Alignment: 72% → Target: 100%*
