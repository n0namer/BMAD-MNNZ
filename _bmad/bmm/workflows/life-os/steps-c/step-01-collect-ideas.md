---
name: 'step-01-collect-ideas'
description: 'Collect new idea or project from user'
nextStepFile: './step-02-roles-discovery.md'
ideasFolder: '{bmb_creations_output_folder}/life-os/ideas'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
workflowPlanTemplate: '../templates/workflow-plan.template.md'
---

# Step 1: Collect Ideas

## STEP GOAL

To capture a new idea or project from the user and understand its core intent,
context, and constraints.

## MANDATORY EXECUTION RULES

### Universal Rules
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read complete step before action
- 🎯 You are a facilitator, not an ideator
- ✅ Save all input to BOTH Markdown AND Claude Flow memory
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess or tool you do not have access to, achieve the outcome in the main thread
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role
You are a thoughtful listener and idea clarifier. Your job is to:
- Listen carefully to what user shares
- Ask 1-2 clarifying questions
- Document the idea completely
- Save to dual storage (Markdown + Claude Flow)

## EXECUTION PROTOCOL

### Search Orchestrator Protocol (Required)
- Follow data/mcp_search_system_prompt_xml.md.
- Execute: CLI memory search -> local MD (rg) -> web/MCP.
- Convene consilium to rank 2–4 options with pros/cons and recommendation.
- Ask user to choose before proceeding.

### Semantic Decision Support
If a decision or prioritization remains unclear, use Search Orchestrator to rank 2–3 options.

### 1. Welcome User

Display welcome message explaining Life OS (50+ AI specialists, portfolio organization, Stage-Gate/MCDA/RICE tracking).

### 2. Collect the Idea

Ask: "Tell me about your new idea or project. What are you thinking?"

Document essentials (1-2 questions at a time): Title, Description, Why Now, Timeline, Domain, Resources.

If vague, guide with hints about product/service/goal, concrete results, success criteria.

### 3. Design Thinking: Empathy Check

📖 **Protocol:** data/design-thinking-empathy.md

Ask 2-3 empathy questions (who benefits, what pain, why now). Append framing to workflow plan.

### 4. Clarifying Questions (1-2 Max)

Ask about: biggest risk, relation to existing projects, success definition, time allocation.

If unclear, offer examples (MVP launch, process improvement, metric growth, personal goal).

### 5. Save Idea File

Create `{ideasFolder}/{IDEA_ID}.md` with frontmatter (id, title, created, domain, status, user_input) and sections: Brief Description, Motivation, Design Thinking Framing, Stakeholders, Initial Thoughts, Timeline, Resources, Clarifying Q&A, Memory Note.

### 6. Update Workflow Plan

Create {workflowPlanFile} from template if not exists. Append Idea Summary and Design Thinking Framing. Update frontmatter `stepsCompleted`.

### 7. Save to Claude Flow Memory

If possible, run the Markdown save and Claude Flow save in parallel and confirm both completed.

Save the idea to Claude Flow memory with:
```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:ideas:{IDEA_ID}" \
  --content "{markdown_content}"
```

### 8. Confirm Save

"✅ **Idea captured!** Saved both to files and memory.

Now let me analyze the complexity and recommend the optimal track..."

---

### Step-Specific Subprocess Optimization Rules

- 🎯 Run track detection in subprocess (Pattern 3)
- 💬 Return recommended track only, not full algorithm
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess unavailable, achieve outcome in main context thread

### Track Detection Algorithm (Subprocess)

**Launch a subprocess that:**
1. Loads data/track-detection-algorithm.md
2. Extracts 6 parameters from idea:
   - Complexity signals
   - Stakes/budget
   - Timeline pressure
   - Stakeholder count
   - Uncertainty level
   - Strategic importance
3. Applies decision tree + scoring matrix
4. Returns recommended track + confidence + breakdown

**Subprocess returns:**
```json
{
  "recommended_track": "Standard",
  "confidence": "85%",
  "complexity_score": 6.2,
  "reasoning": "Moderate complexity, 2-3 stakeholders, medium stakes",
  "alternative_tracks": {
    "Quick": "possible if scope reduced",
    "Deep": "consider if budget >100K or strategic pivot"
  },
  "parameters": {
    "domain": "software",
    "complexity_signal": "standard-analysis",
    "resource_level": "small-team",
    "budget_range": "medium",
    "stakeholder_count": "2-3",
    "novelty": "adaptation"
  }
}
```

**Context savings:** 1,000 lines (full algorithm) → 100 lines (result)

**Graceful fallback:** If subprocess unavailable, load algorithm in main context.

---

### 9. Track Detection & Recommendation

📖 **Algorithm:** data/track-detection-algorithm.md
📖 **UI Templates:** data/track-recommendation-ui.md

#### Step 9.1: Extract Parameters

Extract 6 parameters from the collected idea:
- `domain` (personal/hobby/freelance/small-business/software/saas/ai-ml/franchise/enterprise)
- `complexity_signal` (quick-evaluation/standard-analysis/deep-analysis)
- `resource_level` (solo-spare-time/solo-focused/small-team/funded-team)
- `budget_range` (zero/low/medium/high/investment-round)
- `stakeholder_count` (1/2-3/4+)
- `novelty` (proven-model/adaptation/new-in-domain/breakthrough)

See data/track-detection-algorithm.md for complete inference rules.

#### Step 9.2-9.4: Apply Decision Tree and Scoring

1. Check deterministic rules (6 rules in algorithm)
2. If no match, apply scoring matrix (weighted 0-20 points)
3. Determine recommended track and confidence level

#### Step 9.5-9.6: Present Recommendation

Use templates from data/track-recommendation-ui.md:
- Template 1 if confidence ≥75%
- Template 2 if confidence <75%

#### Step 9.7: Handle Override

Use Template 3 if user chooses lighter track than recommended. No warning for heavier track.

#### Step 9.8: Save Track Selection

Append track selection summary to {workflowPlanFile} with scoring breakdown, steps included, and estimated time.

Update idea file frontmatter with track metadata (track, track_score, track_confidence, track_override).

#### Step 9.9: Save to Memory

```bash
npx claude-flow@v3alpha memory store \
  --namespace "shared-knowledge" \
  --key "life-os:track-selection:{IDEA_ID}" \
  --content "{idea_id, recommended_track, selected_track, confidence, score, parameters, timestamp}"
```

---

### 10. Route to Next Step

| Track | Next Step | Notes |
|-------|-----------|-------|
| Quick | step-04-consilium.md | Add flag: `track=quick` for Consilium Lite |
| Standard | step-02-roles-discovery.md | Normal flow |
| Deep | step-00-goals-discovery.md OR step-02-roles-discovery.md | Check if goals.yaml exists first |

### Menu Handler (Track Selection)

**Available Options (presented after recommendation in Step 9.5):**
- Accept recommended track
- Override to lighter/heavier track
- View track comparison details

**Execution Rules:**
1. Present track recommendation with confidence level (from Step 9.5)
2. **HALT and WAIT** for user selection
3. If user accepts recommendation → Save track metadata to idea file and memory, then route based on track table above
4. If user overrides to lighter track → Show Template 3 warning (Step 9.7), wait for confirmation, then save and route
5. If user overrides to heavier track → No warning, save metadata, route to appropriate next step
6. **Track routing logic:**
   - **Quick track** → Save track flag, load and execute step-04-consilium.md with `track=quick` parameter
   - **Standard track** → Save track metadata, load and execute step-02-roles-discovery.md
   - **Deep track** → Check if {goalsFile} exists. If yes → load step-02-roles-discovery.md. If no → load step-00-goals-discovery.md first
7. **Do NOT auto-proceed** - this is an interactive decision requiring user confirmation

---

## 📊 Quick Feedback (Optional)

Ask: 👍 Helpful | 😐 OK | 👎 Frustrating

Save response to memory:
```bash
npx claude-flow@v3alpha memory store \
  --namespace "user-context" \
  --key "feedback:step-01-collect-ideas:{timestamp}" \
  --content "{step, rating, comment, track, timestamp}"
```

Display: "**Proceeding to {next_step_name}...**"
Then load and execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- Idea clearly documented (title, description, why, timeline, domain)
- Both clarifying questions asked and answered
- Saved to Markdown file
- Saved to Claude Flow memory
- User confident in progression

### ❌ SYSTEM FAILURE
- Generating ideas instead of collecting user input
- Not saving to both storages
- Asking too many questions (max 2)
- Not confirming save to memory
- Not waiting for user menu selection

**Master Rule:** This step is about CAPTURE not CREATION. Listen, clarify, document, save.



