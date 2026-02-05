---
name: 'step-05-scoring'
description: 'Score the project using MCDA/RICE inputs and document rationale'
nextStepFile: './step-06-integration.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
goalsFile: '{bmb_creations_output_folder}/life-os/goals.yaml'
mcdaGuide: '../data/mcda-methodology.md'
stageGateMap: '../data/stage-gate-mapping.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 5: Scoring

## STEP GOAL:

Score the project using structured criteria and document the rationale.

💡 **Quality Reference:** See `../data/scoring-examples.md` for WRONG vs RIGHT scoring examples

**Minimum Quality Standards:**
- Every score justified with reasoning (not just numbers)
- Evidence provided (data, competitor analysis, interviews)
- "Why not higher?" ceiling explained
- Weighted calculation shown (MCDA)
- 600-800 words total output

## MANDATORY EXECUTION RULES (READ FIRST):

**Universal:** 🛑 Never generate content without user input | 📖 Read complete step file first | 🔄 When loading next step with 'C', read entire file | 📋 YOU ARE A FACILITATOR, not content generator | ✅ Always speak in `{communication_language}`

**Step-Specific:** 🎯 Focus ONLY on scoring and rationale | 🚫 FORBIDDEN to change scope or add features | 💬 Use {mcdaGuide} and {stageGateMap} as reference only | 🎯 Use subprocess for scoring criteria filtering by track (Pattern 3) | 💬 Return ONLY track-relevant criteria, not full MCDA encyclopedia

**Execution Protocols:** If subprocess available, load only relevant parts from {mcdaGuide}/{stageGateMap} | Use Search Orchestrator (data/mcp_search_system_prompt_xml.md) when unclear | 💾 Append scoring summary to {workflowPlanFile}

## MANDATORY SEQUENCE

### 1. Load References

Briefly reference {mcdaGuide} and {stageGateMap} for criteria alignment.

### 2. Check Goals Availability & Select Scoring Mode

**Check if {goalsFile} exists:**
- ✅ **Found:** Use 5 criteria (Impact, Confidence, Effort, Strategic Alignment, Risk)
- ❌ **Not found:** Use 4 criteria (no Strategic Alignment) → Offer: `[C]ontinue simplified | [D]efine Goals Now (Step 00, ~10-15 min)`

### 2.1. Select Scoring Approach

**[A]bsolute** - Independent scoring (0-5 scale) | Risk: grade inflation
**[C]omparative** - Rank against other ideas (recommended 2+ ideas) | Forced ranking prevents ties
**[B]atch** - Side-by-side matrix (3+ ideas) | Fastest for portfolios

➡️ **Your choice:** [A/C/B] | 📖 **Details:** data/comparative-ranking-protocol.md


### 3. Auto-Suggest: Domain-Specific Criteria (Intelligence Layer)

**Auto-add based on frameworks:** Business (Market Opportunity 0.10, Competitive Advantage 0.10) | Finance (Expected Value 0.15, Option Value 0.10) | Health (Readiness 0.10, Sustainability 0.10) | Personal Dev (Skill Impact 0.10, Time Commitment 0.10) | **Total weights = 1.0** | Confirm with user: `Adjust weights? [Y/n]`

### 4. Collect Scoring Inputs

📖 **Criteria Definitions:** data/mcda-criteria-detailed.md

#### Scoring Criteria Filtering (Subprocess - Pattern 3)

**Launch a subprocess that:**
1. Detects track: Quick / Standard / Deep (from workflow plan frontmatter or step-00)
2. Loads ONLY relevant criteria from `data/mcda-criteria-detailed.md`:
   - **Quick Track:** 3 criteria only (Impact, Confidence, Effort) + definitions (~50 lines)
   - **Standard Track:** 9 base criteria (Impact, Confidence, Effort, Strategic Alignment, Risk + 4 domain-specific auto-detected) + definitions (~150 lines)
   - **Deep Track:** 10+ criteria (all base + additional domain-specific + custom weight formulas) + definitions (~250 lines)
3. If user selected Comparative/Batch mode: Also filters `data/comparative-ranking-protocol.md` to matching section (~70 lines)
4. Returns ONLY track-appropriate criteria definitions + ranking protocol (if needed) (~100-300 lines instead of 1,000+ full MCDA guide)

**Subprocess returns:**
- Quick: ~50-120 lines (3 criteria + comparative protocol if selected)
- Standard: ~150-220 lines (9 criteria + protocol)
- Deep: ~250-320 lines (10+ criteria + protocol)

**Graceful fallback:** If subprocess unavailable, load full MCDA criteria file and manually filter by track in main context

**Context Savings:** ~1,000 lines (full MCDA guide + all criteria definitions + all ranking protocols) → ~100-320 lines (track-filtered subset) = ~680-900 lines saved

**ABSOLUTE MODE:** Ask user for values (1-5) + rationale for each criterion | Anchors: 1=низко, 3=средне, 5=высоко | If goals available: Include Strategic Alignment | If unsure: Use Search Orchestrator for scoring profiles

**COMPARATIVE/BATCH MODE:** 📖 **Protocol:** data/comparative-ranking-protocol.md | Execute forced differentiation logic

### 5. Calculate Summary

**ABSOLUTE MODE:** If goals available: weights = Impact (0.25), Confidence (0.15), Effort (-0.20), Strategic (0.25), Risk (-0.15) | If no goals: Impact (0.35), Confidence (0.20), Effort (-0.25), Risk (-0.20) | Confirm with user | If simplified scoring AND score ≥8.0: Suggest defining goals

**COMPARATIVE/BATCH MODE:** 📖 **Results:** data/comparative-ranking-protocol.md | Present normalized scores with differentiation metrics

### 6. Append to Workflow Plan

**If GOALS_AVAILABLE = true, append:**
```markdown
## Scoring Summary

**Criteria Scores (1–5):**
- Impact: {score} — {rationale}
- Confidence: {score} — {rationale}
- Effort: {score} — {rationale}
- Strategic Alignment: {score} — {rationale}
- Risk: {score} — {rationale}

**Overall Score:** {score}/10 (method: weighted with goals)

**Decision Rationale:**
- {bullet}
- {bullet}
```

**If GOALS_AVAILABLE = false, append:**
```markdown
## Scoring Summary (Simplified - Goals Not Defined)

**Criteria Scores (1–5):**
- Impact: {score} — {rationale}
- Confidence: {score} — {rationale}
- Effort: {score} — {rationale}
- Risk: {score} — {rationale}

⚠️ **Strategic Alignment:** Not scored (goals not defined yet)

**Overall Score:** {score}/10 (method: simplified without goal alignment)

**Decision Rationale:**
- {bullet}
- {bullet}

💡 **Tip:** Define goals (Step 00) later to improve scoring accuracy.
```

### 7. Stage Gate: Scoring DoD

Confirm readiness to proceed with planning:
- Scores are complete and justified
- Key risks are acknowledged
- Strategic alignment is acceptable
- User agrees to proceed

Ask the user to confirm Gate 1 (Proceed / Revise / Pause).

Append:
```markdown
## Stage Gate: Scoring

**Gate Decision:** {Proceed/Revise/Pause}
**DoD Checklist:** {met/not met}
**Notes:** {brief rationale}
```

### 8. Quality Self-Validation & Checkpoint

📖 **Quality Examples:** data/scoring-examples.md

**Checklist:** ☐ Scores justified with reasoning? ☐ Evidence provided? ☐ "Why not higher?" explained? ☐ Weighted calculation shown? ☐ Sensitivity analysis? ☐ Clear decision? ☐ 600-800 words?

**Quality Check:** [I]mprove | [A]ccept as-is (with warning) | [R]efer to examples | [C]ontinue

**Review Checkpoint:** [Y]es proceed | [N]o revise | [E]xplain criteria

### 9. Quick Feedback & Menu Options

**Feedback:** 👍 Helpful | 😐 OK | 👎 Frustrating → Save to memory: `npx claude-flow@v3alpha memory store --namespace "user-context" --key "feedback:step-05-scoring:{timestamp}"`

**Menu:** [T] TRIZ (resolve conflicts) | [S] Rescore | [A] Adjust Criteria | [C] Continue | 💡 Advanced: [A] Elicitation | [P] Party Mode

**Handling:** T=Step 4.5 TRIZ → return → re-checkpoint | S=restart 2.1 → re-checkpoint | A=modify weights → recalc → re-checkpoint | C=save → load/execute {nextStepFile} | ALWAYS wait for user input

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Scores collected with rationale
- Overall score confirmed
- Scoring written to {workflowPlanFile}

### ❌ SYSTEM FAILURE:
- Scoring without user input
- Missing rationale
- Skipping save/update before continuing

**Master Rule:** Scoring must be explicit, justified, and recorded.
