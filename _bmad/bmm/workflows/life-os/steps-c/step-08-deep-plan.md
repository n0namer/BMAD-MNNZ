---
name: 'step-08-deep-plan'
description: 'Build or deepen a multi-level plan (L1-L6) for project participation'
projectPlanFile: '{bmb_creations_output_folder}/life-os/plans/{project_id}-plan.md'
snapshotFile: '{bmb_creations_output_folder}/life-os/snapshots/{project_id}.md'
journalFile: '{bmb_creations_output_folder}/life-os/journal/{project_id}.md'
deepPlanTemplatesRef: '../data/deep-plan-templates.md'
l1l3TemplateRef: '../data/l1-l3-template.md'
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

💡 **Quality Reference:** `../data/validation-examples.md` | **Quality Gates:** `../data/deep-plan-quality-gates.md`

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

📖 **Reference:** `../data/deep-plan-auto-intelligence.md`

**Launch a subprocess that:**
1. Scans idea metadata for domain tags (Business, Health, Personal, etc.)
2. Loads auto-linking-engine.md with 50+ linking rules
3. Matches domain patterns to template structures:
   - Business → Finance/OKR nodes at L2
   - Health → Habit Loop at L5
   - Personal → Pomodoro/Time blocks at L5
4. Identifies cross-domain dependencies (e.g., Business goal needs Health energy)
5. Returns structured node suggestions with parent-child relationships

**Subprocess returns:** Concise node mapping (200-300 lines) instead of loading full auto-linking-engine.md (1300+ lines).

**Graceful fallback:** If subprocess unavailable, load `../data/deep-plan-auto-intelligence.md` and manually apply 3-5 highest-priority linking rules based on user's domain tags.

### 4. Generate Plan

📖 **Structure Guide:** `../data/deep-plan-l1-l6-guide.md`

**L1-L3 (Standard):** Load {l1l3TemplateRef}
- L1: Overview (what/why/how, 2-3 paragraphs)
- L2: Major phases (3-5 phases with duration, goal)
- L3: Milestones (5-8 with dates, criteria, deliverables)
- Output: Duration, critical path, top 3 risks

**L1-L6 (Deep):** Load {deepPlanTemplatesRef}
- L1: Role/mission | L2: Contribution areas (2-5) | L3: Work streams | L4: Stages | L5: Tasks | L6: Atomic actions
- Use scenario template: Tech Expert, Research, Ops, Product, Invited Role (fallback)
- Mixed Scenario if multiple match (merge unique nodes)
- Apply auto-linked nodes from subprocess (connections from Step 3)

### 5. Update Project Plan

Update "Deep Plan (L1-L6)" section in {projectPlanFile}. Add RACI for L2 nodes, 2-4 If-Then actions.

**Metrics:**
- Depth Covered = levels / 6
- Nodes Count = total L* lines
- RACI Coverage = (L2 with R+A) / total L2
- If-Then Coverage = count If-Then actions

**If TRIZ used:** Document principle, before/after resolution, add as L2 node if applicable.

### 6. Update Journal

Append: Date, what deepened, key decisions.

---

### 7. Quality Validation

📖 **Reference:** `../data/deep-plan-quality-gates.md`

**L1-L3 Checklist:** Structure clear? Phase timelines specific? 20-30 tasks? Top 3 risks? 800-1200 words?

**L1-L6 Checklist:** Full depth (not L1-L2)? Timelines specific? 100+ tasks? Dependencies mapped? 5-8 risks? Contingencies? 2000-3000 words?

**Quality Check:**
[I]mprove | [A]ccept as-is (risk acknowledged) | [R]efer to examples | [C]ontinue (standards met)

**Handle:** I=return to step 4 | A=warn + confirm | R=show validation-examples.md | C=proceed

**Review Checkpoint:**
```
L1: {Role/Mission}
L2: {Areas} | L3: {Streams} | L4: {Stages} | L5: {Tasks} | L6: {Actions}
RACI: {%} | If-Then: {count} | Template: {name} | Auto-linked: {count}
```

Plan meets expectations? [Y]es/[N]o/[E]xplain
- Y=proceed to menu | N=revise | E=show L1-L6 breakdown

---

### 8. Menu Options

```
[T] TRIZ - Resolve contradictions (if L2+ reveals conflicts)
[R] Revise Plan - Restructure levels
[Q] Quality Gate - Check completeness (L1-L4, RACI ≥70%, If-Then ≥2)
[C] Continue - Finalize plan

Choice: [T/R/Q/C]
```

**Menu Logic:**
- **T:** Identify contradictions → Step 4.5 TRIZ Analysis → Apply principle → Update L2 structure → Document TRIZ principle → Re-run quality check → Redisplay menu
- **R:** Revise levels → Restructure L1-L6 → Re-run quality check → Redisplay menu
- **Q:** Verify L1-L4, RACI ≥70%, If-Then ≥2 → Show results → Allow extension → Re-run quality check → Redisplay menu
- **C:** Save to {projectPlanFile} and {journalFile} → Update frontmatter → Execute {nextStepFile}

**RULES:** Wait for input. Complete only when C selected.

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
