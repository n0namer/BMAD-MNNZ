---
name: 'step-08-deep-plan'
description: 'Build or deepen a multi-level plan (L1-L6) for project participation'
projectPlanFile: '{bmb_creations_output_folder}/life-os/plans/{project_id}-plan.md'
snapshotFile: '{bmb_creations_output_folder}/life-os/snapshots/{project_id}.md'
journalFile: '{bmb_creations_output_folder}/life-os/journal/{project_id}.md'
deepPlanTemplatesRef: '../data/deep-plan-templates.md'
l1l3TemplateRef: '../data/l1-l3-template.md'
qualityGatesRef: '../data/deep-plan-quality-gates.md'
autoIntelligenceRef: '../data/deep-plan-auto-intelligence.md'
goalLinkageRef: '../data/goal-linkage-traceability.md'
nextStepFile: './step-08.5-final-polish.md'
track_defaults:
  quick:
    default_action: skip
    recommended_depth: none
    message: "Quick Track ideas don't need Deep Plan. Proceed to completion."
  standard:
    default_action: l1_l3
    recommended_depth: [L1, L2, L3]
    message: "Standard Track: L1-L3 provides sufficient detail. L4-L6 optional."
  deep:
    default_action: l1_l6
    recommended_depth: [L1, L2, L3, L4, L5, L6]
    message: "Deep Track: Full L1-L6 plan recommended for comprehensive analysis."
---

# Step 8: Deep Plan Builder

## STEP GOAL

Create multi-level plan (L1-L6) for effective project contribution.

💡 **Quality Reference:** `../data/validation-examples.md` | **Quality Gates:** `{qualityGatesRef}`

**Quality Standards:**
- **Deep Track (L1-L6):** Full depth, 100+ tasks, dependencies, 5-8 risks, 2000-3000 words
- **Standard Track (L1-L3):** Clear structure, 20-30 tasks, top 3 risks, 800-1200 words

## TRACK-BASED DEFAULTS

**Quick Track:** SKIP (not needed) | **Standard Track:** L1-L3 (10-15 min) | **Deep Track:** L1-L6 (20-60 min)

## EXECUTION RULES

- 🛑 Facilitator role only - no auto-generation
- 📖 Read complete step file first
- 💬 Ask 1-2 questions at a time, confirm each level
- 📊 Default to track-appropriate depth
- ✅ Use `{communication_language}` for all output
- 🎯 Use subprocess for auto-linking-engine.md (Pattern 3 + Pattern 4: Data Operations + Parallel)
- 💬 Return structured L2-L5 node connections only

## EXECUTION PROTOCOLS

Load {projectPlanFile}, {snapshotFile}, {journalFile}. Update Deep Plan section and journal. Follow Search Orchestrator protocol (CLI memory → local MD → web/MCP) for decisions.

---

## MANDATORY SEQUENCE

### 1. Load Context & Detect Track

Open {projectPlanFile}, {snapshotFile}, {journalFile}. Extract `track` from workflow plan frontmatter. Summarize goal, status, next step.

### 2. Depth Selection Menu

Present options based on track:
```
DEEP PLAN DEPTH SELECTION
Your idea: {TRACK} TRACK | Recommended: {track_defaults[track].message}

[A]ccept {recommended} ({time_estimate} min)
[F]ull L1-L6 (20-60 min)
{if quick_track}[S]kip Deep Plan{/if}

Choice: [A/F/S]
```

**Warnings:**
- **Standard→[F]:** "⚠️ Adds 40-50 min. L1-L3 sufficient. Proceed? [Y/N]"
- **Quick→[A/F]:** "⚠️ Quick Track = 15-20 min total. Deep Plan adds 10-60 min. Continue? [Y/N]"

**Route:**
- [A]: Quick=skip | Standard=L1-L3 | Deep=L1-L6
- [F]: L1-L6 (set `deep_plan_depth: L1-L6` in plan)
- [S]: Mark `deep_plan_skipped: true`, proceed to next step

### 3. Auto-Intelligence Check & Auto-Linking (Subprocess)

📖 **Reference:** `{autoIntelligenceRef}`

**Subprocess:** Scans domain tags → Loads auto-linking-engine.md (50+ rules) → Matches patterns (Business→Finance/OKR, Health→Habit Loop, Personal→Pomodoro) → Returns node mapping (200-300 lines).

**Fallback:** Load `{autoIntelligenceRef}` and apply 3-5 top-priority rules manually.

### 4. Generate Plan

📖 **Structure Guide:** `../data/deep-plan-l1-l6-guide.md`

**L1-L3 (Standard):** {l1l3TemplateRef} → L1: Overview | L2: Phases (3-5) | L3: Milestones (5-8) → Output: duration, critical path, top 3 risks.

**L1-L6 (Deep):** {deepPlanTemplatesRef} → L1: Role | L2: Areas (2-5) | L3: Streams | L4: Stages | L5: Tasks | L6: Actions. Use scenario template (Tech/Research/Ops/Product/Invited). Apply auto-linked nodes from Step 3.

### 5. Update Project Plan

Update "Deep Plan (L1-L6)" section in {projectPlanFile}. Add RACI for L2 nodes, 2-4 If-Then actions.

**Metrics:**
- Depth Covered = levels / 6
- Nodes Count = total L* lines
- RACI Coverage = (L2 with R+A) / total L2
- If-Then Coverage = count If-Then actions
- Goal Linkage Coverage = (milestones with goal_id) / total milestones

**If TRIZ used:** Document principle, before/after resolution, add as L2 node if applicable.

### 5.5. Link Milestones to Goals (Traceability)

📖 **Full Process:** `{goalLinkageRef}`

**Process:** Check goals.yaml → Match milestones (domain/timeframe/semantic) → Confirm with user → Update plan + metrics.

**Risk Flags:** Single-Goal Focus (>70%), Short-Term Bias (>80% 1-year), No Goal Linkage (<50%).

**Output:** Traceability matrix + coverage + risk flags → project plan + shared-knowledge memory.

### 6. Update Journal

Append: Date, what deepened, key decisions.

### 7. Quality Validation

📖 **Reference:** `{qualityGatesRef}`

**Checklists:** L1-L3: structure/tasks(20-30)/risks(3)/800-1200 words | L1-L6: depth/tasks(100+)/dependencies/risks(5-8)/2000-3000 words

**Quality Check:** [I]mprove | [A]ccept | [R]efer examples | [C]ontinue → Handle: I=step 4 | A=warn | R=examples | C=proceed

**Review:** Show L1-L6 summary, RACI%, If-Then count, template, auto-linked nodes. Confirm: [Y]es/[N]o/[E]xplain

### 7.5. Save Planning Patterns to Memory

Store planning patterns, task estimates, and TRIZ integration (if applied) to shared-knowledge namespace for learning and calibration.

### 8. Menu Options

```
[T] TRIZ - Resolve contradictions (if L2+ reveals conflicts)
[R] Revise Plan - Restructure levels
[Q] Quality Gate - Check completeness (L1-L4, RACI ≥70%, If-Then ≥2)
[C] Continue - Finalize plan

Choice: [T/R/Q/C]
```

## Menu Handling Logic:

### EXECUTION RULES:

**ALWAYS halt and wait for user input. Complete only when [C] selected.**

**Per-choice logic:**

- **[T] - TRIZ Analysis:**
  1. Identify contradictions from L2+ structure
  2. Execute Step 4.5 TRIZ Analysis subprocess
  3. Apply resolved principle to L2 structure
  4. Document principle, before/after, L2 update in plan
  5. Re-run quality check (section 7)
  6. Redisplay menu

- **[R] - Revise Plan:**
  1. Restructure L1-L6 levels based on user feedback
  2. Update milestone timelines and tasks
  3. Recalculate RACI coverage and If-Then actions
  4. Re-run quality check (section 7)
  5. Redisplay menu

- **[Q] - Quality Gate:**
  1. Verify L1-L4 complete (not just L1-L2)
  2. Check RACI coverage ≥70% on L2 nodes
  3. Verify If-Then actions ≥2
  4. Show validation results
  5. Allow user to request improvements or confirm
  6. Re-run quality check if improvements made
  7. Redisplay menu

- **[C] - Continue (Finalize):**
  1. Save plan to {projectPlanFile}
  2. Save updates to {journalFile}
  3. Update frontmatter with completion timestamp
  4. Execute next step: {nextStepFile}

---

## Quick Feedback

How was this step? 👍 Helpful | 😐 OK | 👎 Frustrating

[Type feedback or Enter to skip]

**Save to memory:**
```bash
npx claude-flow@v3alpha memory store --namespace "user-context" --key "feedback:step-08-deep-plan:{timestamp}" --content "{\"step\":\"step-08-deep-plan\",\"rating\":\"{rating}\",\"comment\":\"{comment}\",\"plan_mode\":\"{mode}\",\"timestamp\":\"{ISO_datetime}\"}"
```

---

## SUCCESS/FAILURE METRICS

**✅ SUCCESS:** Deep plan created/expanded, updates saved to plan and journal

**❌ FAILURE:** Skipping confirmation, not saving updates

**Master Rule:** Depth explicit, confirmed, documented.
