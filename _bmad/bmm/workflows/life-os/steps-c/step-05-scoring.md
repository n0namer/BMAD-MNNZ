---
name: 'step-05-scoring'
description: 'Score the project using MCDA/RICE inputs and document rationale'
nextStepFile: './step-06-integration.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
goalsFile: '{bmb_creations_output_folder}/life-os/goals.yaml'
mcdaGuide: '../data/mcda-methodology.md'
criteriaRubric: '../data/dfvc-criteria-rubric.md'
scoringCalculator: '../data/scoring-calculator.md'
comparativeExamples: '../data/comparative-ranking-examples.md'
stageGateMap: '../data/stage-gate-mapping.md'
trackEscalationRules: '../data/track-escalation-rules.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 5: Scoring

## STEP GOAL

Score the project using structured criteria and document the rationale. After scoring, write a short PDCA note that connects the current score to the upcoming weekly review (IDEAL 1.5) and store the score+reasoning in Claude memory so the review track knows the decision context.

💡 **Quality Reference:** See `../data/scoring-examples.md` for WRONG vs RIGHT scoring examples

**Minimum Quality Standards:**
- Every score justified with reasoning (not just numbers)
- Evidence provided (data, competitor analysis, interviews)
- "Why not higher?" ceiling explained
- Weighted calculation shown (MCDA)
- 600-800 words total output

## MANDATORY EXECUTION RULES (READ FIRST)

**Universal:** 🛑 Never generate content without user input | 📖 Read complete step file first | 🔄 When loading next step with 'C', read entire file | 📋 YOU ARE A FACILITATOR, not content generator | ✅ Always speak in `{communication_language}`

**Step-Specific:** 🎯 Focus ONLY on scoring and rationale | 🚫 FORBIDDEN to change scope or add features | 💬 Use references as guides only | 🎯 Use subprocess for scoring criteria filtering by track (Pattern 3) | 💬 Return ONLY track-relevant criteria, not full MCDA encyclopedia

**Execution Protocols:** If subprocess available, load only relevant parts from references | Use Search Orchestrator when unclear | 💾 Append scoring summary to {workflowPlanFile}

Before concluding, run a memory search for similar ideas and note the patterns in `shared-knowledge` (IDEAL 1.4) so future reviews can reuse the scoring rationale.

**🎯 5+N Dynamic Criteria System:**
- **Base 5 criteria** (always): Impact, Feasibility, Alignment, Urgency, Resources
- **+N conditional criteria** (context-dependent):
  - If SaaS idea → Add "Autonomy Readiness" (from SaaS Gate)
  - If high complexity (>15) → Add "Technical Risk", "Team Capability"
  - If high budget (>$10K) → Add "ROI Projection", "Payback Period"
- **JIT Loading:** Only load relevant criteria (saves cognitive load + context)

## MANDATORY SEQUENCE

### 1. Load References

Briefly reference {mcdaGuide} for methodology and {criteriaRubric} for criteria definitions.

📖 **Core References:**
- **Methodology:** `{mcdaGuide}` - MCDA approach, weight structure, calculation formulas
- **Criteria Rubric:** `{criteriaRubric}` - Detailed scoring anchors for all criteria
- **Calculator Protocol:** `{scoringCalculator}` - Step-by-step calculation procedures
- **Comparative Examples:** `{comparativeExamples}` - Ranking protocol and examples

### 2. Check Goals Availability & Select Scoring Mode

**Check if {goalsFile} exists:**
```bash
# Check for goals.yaml in output folder
if [ -f "{goalsFile}" ]; then
    echo "✅ Goals found - Strategic Alignment enabled"
    GOALS_AVAILABLE=true
else
    echo "⚠️ Goals not defined - Strategic Alignment disabled"
    GOALS_AVAILABLE=false
fi
```

**Scoring Mode Selection:**
- ✅ **Goals Found:** Use 5 criteria (Impact, Confidence, Effort, Strategic Alignment, Risk)
  - Load goals from `{goalsFile}` (YAML structure)
  - Enable Strategic Alignment scoring
- ❌ **Goals Not Found:** Use 4 criteria (no Strategic Alignment)
  - Offer: `[C]ontinue simplified | [D]efine Goals Now (Step 00, ~10-15 min)`
  - Skip Strategic Alignment section entirely

### 2.1. Select Scoring Approach

**[A]bsolute** - Independent scoring (0-5 scale) | Risk: grade inflation
**[C]omparative** - Rank against other ideas (recommended 2+ ideas) | Forced ranking prevents ties
**[B]atch** - Side-by-side matrix (3+ ideas) | Fastest for portfolios

➡️ **Your choice:** [A/C/B] | 📖 **Details:** `{comparativeExamples}`

### 3. Auto-Suggest: Domain-Specific Criteria (Intelligence Layer)

**Auto-add based on frameworks:** Business (Market Opportunity 0.10, Competitive Advantage 0.10) | Finance (Expected Value 0.15, Option Value 0.10) | Health (Readiness 0.10, Sustainability 0.10) | Personal Dev (Skill Impact 0.10, Time Commitment 0.10) | **Total weights = 1.0** | Confirm with user: `Adjust weights? [Y/n]`

### 4. Collect Scoring Inputs

📖 **Criteria Definitions:** `{criteriaRubric}`
📖 **Scoring Calculator:** `{scoringCalculator}`

#### Scoring Criteria Filtering (Subprocess - Pattern 3)

**Launch a subprocess that:**
1. Detects track: Quick / Standard / Deep (from workflow plan frontmatter or step-00)
2. Loads ONLY relevant criteria from `{criteriaRubric}`:
   - **Quick Track:** 3 criteria only (Impact, Confidence, Effort) + definitions (~50 lines)
   - **Standard Track:** 9 base criteria (Impact, Confidence, Effort, Strategic Alignment, Risk + 4 domain-specific auto-detected) + definitions (~150 lines)
   - **Deep Track:** 10+ criteria (all base + additional domain-specific + custom weight formulas) + definitions (~250 lines)
3. If user selected Comparative/Batch mode: Also filters `{comparativeExamples}` to matching section (~70 lines)
4. Returns ONLY track-appropriate criteria definitions + ranking protocol (if needed) (~100-300 lines instead of 1,000+ full guide)

**Context Savings:** ~1,000 lines (full MCDA guide + all criteria definitions + all protocols) → ~100-320 lines (track-filtered subset) = ~680-900 lines saved

**Graceful fallback:** If subprocess unavailable, load full criteria file and manually filter by track in main context

**ABSOLUTE MODE:** Ask user for values (1-5) + rationale for each criterion | Anchors: 1=низко, 3=средне, 5=высоко | If goals available: Include Strategic Alignment | If unsure: Use Search Orchestrator for scoring profiles

**COMPARATIVE/BATCH MODE:** 📖 **Protocol:** `{comparativeExamples}` | Execute forced differentiation logic

### 4.5. SaaS Autonomy Gate (Conditional - 6th Criterion)

**Purpose:** Evaluate SaaS products on autonomous operation capability (ONLY for SaaS/software domains).

**Trigger Detection:**
- Check `domain` field from Step 01 or workflow plan
- Apply if `domain = 'saas'` OR `domain = 'software'`
- Skip entirely for non-SaaS projects

**When to Apply:**
```bash
if [[ "$IDEA_DOMAIN" == "saas" || "$IDEA_DOMAIN" == "software" ]]; then
    echo "🛡️ SaaS Autonomy Gate triggered - evaluating 4 pillars..."
    # Proceed with autonomy scoring
else
    echo "ℹ️ Non-SaaS project - skipping autonomy gate"
    # Skip to section 4.7 (Strategic Alignment)
fi
```

**4 Autonomy Pillars (Full rubric in `{criteriaRubric}` section 6):**

| Pillar | Weight | What It Measures | Scale |
|--------|--------|------------------|-------|
| **Self-Signup** | 0.25 | Can users sign up without sales calls? | 1 (enterprise sales) → 5 (1-click OAuth) |
| **Self-Billing** | 0.30 | Automated payment and provisioning? | 1 (manual invoicing) → 5 (usage-based + dunning) |
| **Self-Service Support** | 0.30 | Can users solve problems without human agents? | 1 (dedicated CSM) → 5 (AI support, <1% contact) |
| **Autonomous Operation** | 0.15 | Can product run without manual team intervention? | 1 (daily manual work) → 5 (fully automated, 99.9% uptime) |

**User Interaction:** Present pillar-by-pillar scoring prompt (see `{scoringCalculator}` for detailed template)

**Calculate SaaS Autonomy Score:**
```
SaaS_Autonomy_Score = (Self_Signup × 0.25) + (Self_Billing × 0.30) +
                      (Self_Service_Support × 0.30) + (Autonomous_Operation × 0.15)

Result: 1.0-5.0 scale (consistent with other MCDA criteria)
```

**Classification:**

| Score Range | Classification | Team Size | Business Model | Passive Income Potential |
|-------------|---------------|-----------|----------------|-------------------------|
| 4.5-5.0 | Highly Autonomous | Solo founder feasible | Product-led growth | ✅ High |
| 3.5-4.4 | Moderately Autonomous | 2-5 team | Hybrid PLG + light touch | ⚠️ Medium |
| 2.5-3.4 | Limited Autonomy | 5-10 team | Sales-assisted | ❌ Low |
| 1.0-2.4 | Low Autonomy | 10+ team | High-touch enterprise | ❌ None |

**Risk Flags (auto-trigger):**
- ⚠️ `SaaS_Autonomy < 3.0` → High Support Load Risk
- ⚠️ `Autonomous_Operation < 2.5` → Manual Operations Bottleneck
- ⚠️ `SaaS_Autonomy < 2.0` → Consider Enterprise Model Instead

**Integration:** Add as 6th base criterion with 0.15 weight (see `{scoringCalculator}` for weight normalization)

### 4.7. Strategic Alignment (Conditional - 5th/6th Criterion)

**Purpose:** Evaluate how well this idea/project aligns with user's defined life goals (ONLY if goals.yaml exists).

**Trigger Detection:**
```bash
# Check if goals.yaml exists
if [ -f "{goalsFile}" ]; then
    echo "✅ Strategic Alignment enabled"
    GOALS_AVAILABLE=true
else
    echo "ℹ️ Goals not defined - skipping Strategic Alignment"
    GOALS_AVAILABLE=false
    # Skip to section 5 (Calculate Summary)
fi
```

**Scoring Method (if goals available):**
1. Load 12 goals from `{goalsFile}` (4 domains × 3 timeframes)
2. Score alignment with each goal (1-5 scale)
3. Calculate domain averages using timeframe weights (1yr: 0.5, 3yr: 0.3, 5-10yr: 0.2)
4. Average across 4 domains

**Scoring Anchors:**

| Score | Level | Description | Example |
|-------|-------|-------------|---------|
| **5** | Perfect Match | Directly achieves this goal | Idea: "Launch SaaS" → Goal: "Generate $10K MRR by year-end" |
| **4** | Strong Alignment | Significant progress toward goal | Idea: "Build MVP" → Goal: "Launch first product" |
| **3** | Moderate Alignment | Indirectly supports goal | Idea: "Learn React" → Goal: "Build profitable SaaS" |
| **2** | Weak Alignment | Tangential connection | Idea: "Write blog" → Goal: "Increase income" |
| **1** | No Alignment | Unrelated or contradictory | Idea: "Gaming hobby" → Goal: "Increase savings" |

**User Interaction:** Present domain-by-domain scoring prompt (see `{scoringCalculator}` for detailed template)

**Risk Flags (auto-trigger):**
- ⚠️ `Strategic_Alignment_Score < 2.5` → Strategic Misalignment Risk
- ⚠️ Single domain ≥4.5, all others <2.0 → Single-Domain Focus
- ⚠️ 1yr scores ≥4.0, 3yr + 5-10yr <2.0 → Short-Term Only

**Integration:** Add as 5th criterion with 0.25 weight (see `{scoringCalculator}` for weight normalization)

### 5. Calculate Summary

📖 **Calculator Protocol:** `{scoringCalculator}`

**ABSOLUTE MODE:** If goals available: weights = Impact (0.25), Confidence (0.15), Effort (-0.20), Strategic (0.25), Risk (-0.15) | If no goals: Impact (0.35), Confidence (0.20), Effort (-0.25), Risk (-0.20) | Confirm with user | If simplified scoring AND score ≥8.0: Suggest defining goals

**COMPARATIVE/BATCH MODE:** 📖 **Results:** `{comparativeExamples}` | Present normalized scores with differentiation metrics

**Formula:**
```
Overall_Score = Σ(Criterion_Score × Normalized_Weight)
Result: -3.0 to +7.0 scale (raw)
Normalized: 0-10 scale (presentation)
```

### 5.5. Track Escalation Check

💡 **Reference:** See `{trackEscalationRules}` for complete escalation algorithm

**After calculating summary, check for track escalation triggers:**

**TRIGGER 2: Scoring Contradiction** (opposing dimensions ≥4)
- Check Impact vs Effort: If both ≥4 → contradiction
- Check Impact vs Risk: If both ≥4 → contradiction
- Check Impact vs Feasibility: If Impact ≥4 AND Feasibility ≤2 → contradiction
- If ≥2 contradictions detected → Suggest track escalation

**TRIGGER 5: Budget Revelation** (>$1M or investment round)
- If budget >$1M revealed AND current track != Deep → Suggest Deep Track

**Escalation Prompt Template:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ TRACK ESCALATION NOTICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Scoring reveals {N} contradictions.

  Trigger: {Scoring Contradiction / Budget Revelation}
  Current track: {Quick / Standard / Deep}
  Suggested upgrade: {Standard / Deep} Track

  What changes:
  + {benefit 1}
  + {benefit 2}
  + Additional {time} minutes

  [U] Upgrade to {suggested} Track
  [K] Keep {current} Track (I understand the limits)
```

### 5.6. TRIZ Auto-Trigger Check (Contradiction Detection)

**After escalation checks, evaluate individual contradictions for TRIZ:**

**Check for:**
- High Impact + High Effort (≥4 both)
- High Impact + High Risk (≥4 both)
- High Quality + High Speed (if domain-specific criteria present)

**If contradiction detected:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ CONTRADICTION DETECTED: {Type}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Scoring reveals a contradiction:
- {Criterion A}: {score}/5 ({description})
- {Criterion B}: {score}/5 ({description})

This is a classic TRIZ contradiction. TRIZ can help find a path
that {resolves the contradiction}.

[T] Trigger TRIZ analysis
[S] Skip - Accept trade-off
[L] Learn more
```

**If user selects [T]:** Load and execute `./step-04.5-triz-analysis.md`, then return to scoring menu (Section 9)

**If no contradictions detected:** Skip TRIZ check, proceed to section 6

### 6. Append to Workflow Plan

**Append scoring summary to {workflowPlanFile} based on configuration:**

**If GOALS_AVAILABLE = true AND domain = 'saas'/'software':**
```markdown
## Scoring Summary

**Criteria Scores (1–5):**
- Impact: {score} — {rationale}
- Confidence: {score} — {rationale}
- Effort: {score} — {rationale}
- Strategic Alignment: {score} — {rationale}
- Risk: {score} — {rationale}
- **SaaS Autonomy:** {score}/5.0 — {classification}

**Overall Score:** {score}/10 (method: weighted with goals + SaaS autonomy)

**Decision Rationale:**
- {bullet}
- {bullet}

**SaaS Business Implications:**
- Team Size Needed: {solo / 2-5 / 5-10 / 10+}
- Business Model Fit: {PLG / Hybrid / Sales-assisted / High-touch}
- Passive Income Potential: {High / Medium / Low / None}

{If risk flags}
⚠️ **Risk Flags:** {flags}
```

**Other configurations:** See lines 914-1022 in original file for template variations

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

📖 **Quality Examples:** `../data/scoring-examples.md`

**Checklist:** ☐ Scores justified with reasoning? ☐ Evidence provided? ☐ "Why not higher?" explained? ☐ Weighted calculation shown? ☐ Sensitivity analysis? ☐ Clear decision? ☐ 600-800 words?

**Quality Check:** [I]mprove | [A]ccept as-is (with warning) | [R]efer to examples | [C]ontinue

**Review Checkpoint:** [Y]es proceed | [N]o revise | [E]xplain criteria

### 9. Quick Feedback & Menu Options

**Feedback:** 👍 Helpful | 😐 OK | 👎 Frustrating → Save to memory: `npx claude-flow@v3alpha memory store --namespace "user-context" --key "feedback:step-05-scoring:{timestamp}"`

#### Display:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 SCORING COMPLETE - NEXT STEP?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[T] TRIZ Analysis (resolve High Impact/Effort conflicts)
[S] Rescore (restart from Section 2.1)
[A] Adjust Criteria (modify weights and recalculate)
[C] Continue (save and load next step)

💡 Advanced Options:
[E] Advanced Elicitation (deepen scoring inputs)
[P] Party Mode (collaborative scoring session)

Your choice: [T/S/A/C/E/P]
```

#### Menu Handling Logic:

**IF [T] TRIZ Analysis selected:**
- Load and execute `./step-04.5-triz-analysis.md`
- Return to Section 8 (Quality Self-Validation & Checkpoint)
- Redisplay menu (Section 9)

**IF [S] Rescore selected:**
- Return to Section 2.1 (Select Scoring Approach)
- Clear previous scores
- After completion, return to Section 8
- Redisplay menu (Section 9)

**IF [A] Adjust Criteria selected:**
- Modify criterion weights
- Recalculate overall score
- Return to Section 8
- Redisplay menu (Section 9)

**IF [C] Continue selected:**
- Save current scoring to {workflowPlanFile}
- Load {nextStepFile}
- **DO NOT redisplay menu** - proceed to next step

**IF [E] Advanced Elicitation selected:**
- Load {advancedElicitationTask}
- Execute advanced elicitation subprocess
- Return to Section 8
- Redisplay menu (Section 9)

**IF [P] Party Mode selected:**
- Load {partyModeWorkflow}
- Execute collaborative scoring session
- Return to Section 8
- Redisplay menu (Section 9)

#### EXECUTION RULES:

**🚨 ALWAYS halt and wait after displaying menu**
- Do NOT proceed automatically
- Do NOT assume user wants [C]
- Do NOT skip checkpoint before menu display
- Wait explicitly for user input

**🔄 Redisplay menu for non-[C] options:**
- After [T] TRIZ completes → redisplay menu
- After [S] Rescore completes → redisplay menu
- After [A] Adjust completes → redisplay menu
- After [E] Elicitation completes → redisplay menu
- After [P] Party Mode completes → redisplay menu
- Only [C] exits the menu loop

**📋 Before menu display (MANDATORY):**
- Section 8 Quality Self-Validation MUST be complete
- User must confirm checkpoint ([Y]es or [N]o revise)
- If [N]o revise selected, complete revisions BEFORE displaying menu
- Only show menu after user confirms [Y]es to checkpoint

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
