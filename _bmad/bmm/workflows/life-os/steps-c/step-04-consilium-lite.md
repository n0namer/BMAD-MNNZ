---
name: 'step-04-consilium-lite'
description: 'Consilium Lite: Fast specialist consultation for Quick Track (2-3 perspectives, 5-10 min)'
nextStepFile: './step-05-scoring.md'
workflowPlanFile: '{bmb_creations_output_folder}/life-os/workflow-plan-life-os.md'
trackType: 'quick'
estimatedTime: '5-10 minutes'
specialists: '1-2'
perspectives: '3'
---

# Step 4 Lite: Consilium Lite

## STEP GOAL

Assemble a lightweight specialist consilium (Quick Track only), capture 3 perspectives, deliver quick recommendation.

**Quality Standards:** 200-300 words total output, 2-3 bullets per perspective

## MANDATORY EXECUTION RULES (READ FIRST)

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', read entire file
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Step-Specific Rules:
- 🎯 LITE MODE ONLY: 3 perspectives (Facts / Risks / Opportunities)
- 👥 Use 1-2 specialists maximum
- ⏱️ Keep to 5-10 minutes total
- 🚫 FORBIDDEN: Six Hats methodology (use Full Consilium instead)
- 🚫 FORBIDDEN: Multi-round discussion
- 💬 Confirm specialist input before moving on
- ✅ Use subprocess for consilium reference files if needed

---

## EXECUTION PROTOCOLS

### Search Orchestrator Protocol (If user asks for advice)
- Follow data/mcp_search_system_prompt_xml.md
- Execute: CLI memory search → local MD → web/MCP
- Summarize findings and cite sources

---

## MANDATORY SEQUENCE

### 1. Load Specialist List

Open {workflowPlanFile}, locate "Specialist Matching" section.

Summarize to user:
```
Based on your idea, I've selected these specialists:

Specialist 1: {name} ({role})
Specialist 2: {name} ({role}) [if applicable]

They'll provide 3 quick perspectives on your idea.
Ready to proceed?
```

### 2. Gather 3 Perspectives (Lite Mode)

**Question the specialists on these 3 perspectives:**

#### ⚪ **FACTS** - What do we know?
Ask: "What are the key facts, data points, and constraints we should consider?"
- 2-3 bullets max
- Keep it grounded

#### ⚫ **RISKS** - What could go wrong?
Ask: "What are the biggest risks or potential blockers?"
- 2-3 bullets max
- Focus on critical risks only

#### 🟢 **OPPORTUNITIES** - What's the upside?
Ask: "What opportunities or innovations could amplify this idea's potential?"
- 2-3 bullets max
- Think creative solutions

### 3. Synthesize Quick Recommendation

After gathering input from specialists, synthesize into 2-3 sentence recommendation:

**Format:**
```
✅ **Consilium Lite Recommendation**

[1-2 sentence summary of specialist consensus]

Key Insight: [1 critical insight from specialists]

Next: [Proceed to scoring]
```

### 4. Append to Workflow Plan

Append:
```markdown
## Consilium Lite (Quick Track)

**Date:** {date}
**Specialists:** {names}
**Track:** Quick

### Perspectives

**Facts:**
- {fact 1}
- {fact 2}

**Risks:**
- {risk 1}
- {risk 2}

**Opportunities:**
- {opportunity 1}
- {opportunity 2}

### Recommendation
{Quick recommendation text}
```

### 5. Present Menu Options

Display: "**Select:** [C] Continue to Scoring"

#### Menu Handling Logic:
- IF C: Save to {workflowPlanFile}, update frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user respond, then redisplay menu

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Specialists identified
- 3 perspectives captured (2-3 bullets each)
- Quick recommendation synthesized
- Total time ≤10 minutes

### ❌ SYSTEM FAILURE:
- Generating without specialist input
- Using Six Hats or multi-round discussion
- Exceeding 10 minutes
- Skipping documentation

**Master Rule:** Keep it fast, lightweight, and facilitator-driven.

---

## NOTES

**When to Upgrade to Full Consilium:**
- If Lite reveals >50% disagreement → Offer to upgrade to Deep Track
- If contradictions emerge → Offer Deep Track with TRIZ
- If user requests more depth → Escalate to Step 04 (Full Consilium)

**Quick Track Success:**
- Lite mode completes in 5-10 minutes
- Low cognitive load for specialists
- Sufficient input for scoring step
- User retains control over depth
