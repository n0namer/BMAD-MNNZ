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

```
🎯 **Life Operating System**

Welcome to your Life Operating System!

This is where new ideas and projects are evaluated with the help of
50+ AI specialists, organized into your portfolio, and tracked with
academic rigor (Stage-Gate, MCDA scoring, RICE methodology).

Let's start by capturing your new idea.
```

### 2. Collect the Idea (Ask, Listen, Document)

Say: **"Tell me about your new idea or project. What are you thinking?"**

As user speaks, document the essentials. Cover these topics progressively
(1–2 questions at a time, adapting to the user’s answers):
- **Project Title** (what is it)
- **Brief Description** (2-3 sentences)
- **Why Now** (motivation, opportunity)
- **Timeline Expectation** (days/weeks/months)
- **Domain** (software, finance, personal, business, health, etc.)
- **Resources Needed** (rough estimate)

If the idea is vague or unclear, guide with one short hint at a time:
- "Это больше про продукт, сервис или личную цель?"
- "Какой конкретный результат вы хотите получить через 4–6 недель?"
- "Что будет считаться успехом?"

### 3. Design Thinking: Empathy Check (Universal Method - Embedded)

**Goal:** Frame this idea with user-centric thinking.

Ask the user 2-3 empathy questions to understand the human context:

**Question 1: Who benefits?**
- "Кто получит пользу от этого проекта?"
- "Для кого это решает проблему?"

**Question 2: What pain does this solve?**
- "Какую боль или проблему это устраняет?"
- "Что произойдёт, если эту проблему НЕ решить?"

**Question 3 (optional): Why now?**
- "Почему это важно сейчас?"
- "Что изменилось, что делает это актуальным?"

💡 **Design Thinking Tip:** If you can't clearly answer "who benefits?" and "what pain?", the idea may need refinement. Consider pausing to gather more user insights.

**Guidance for Unclear Answers:**
- If user says "not sure yet" → That's OK! Mark as "to be explored" and continue
- If user struggles → Offer examples: "Например: клиенты, команда, личная продуктивность?"
- Don't block progress → Empathy questions are guidance, not gates

**Append to workflow plan:**
```markdown
## Design Thinking: Empathy Framing

**Who Benefits:** {user answer or "to be explored"}
**Pain/Problem Solved:** {user answer or "to be explored"}
**Why Now:** {user answer or "not specified"}
```

### 4. Clarifying Questions (Ask 1-2 Max)

Based on what they said, ask 1-2 clarifying questions:

**Example Question Set:**
- "What's the biggest risk or challenge you see?"
- "Does this relate to any existing project in your portfolio?"
- "What success looks like for you?"
- "How much time can you allocate to this?"

If the user can't answer, offer examples and let them pick:
- "Могу предложить варианты: запуск MVP, улучшение процесса, рост метрики, личная цель. Что ближе?"

### 5. Save to Memory (Dual Storage - CRITICAL)

Create file: `{ideasFolder}/{IDEA_ID}.md`

```markdown
---
id: {IDEA_ID}
title: {Project Title}
created: {today's date}
domain: {domain}
status: INBOX
user_input: {direct quote from user}
---

# {Project Title}

## Brief Description
{2-3 sentence description}

## Motivation
{Why now? What problem/opportunity?)

## Design Thinking: Empathy Framing
**Who Benefits:** {user answer or "to be explored"}
**Pain/Problem Solved:** {user answer or "to be explored"}
**Why Now:** {user answer or "not specified"}

## Stakeholders
- {Who's involved}
- {Who benefits}

## Initial Thoughts
{What user said about approach}

## Timeline Expectation
{Days/weeks/months}

## Resource Estimate
{Rough resource needs}

## Clarifying Questions Asked
- Q1: {question} → A: {answer}
- Q2: {question} → A: {answer}

## Memory Note
[Conversation date/time. Key insights. Next step trigger.]
```

### 6. Update Workflow Plan

If {workflowPlanFile} does not exist, create it from {workflowPlanTemplate}.

Append:
```markdown
## Idea Summary
- Title: {Project Title}
- Domain: {domain}
- Motivation: {why now}
- Timeline: {timeline}
- Resources: {resources}

## Design Thinking: Empathy Framing
**Who Benefits:** {user answer or "to be explored"}
**Pain/Problem Solved:** {user answer or "to be explored"}
**Why Now:** {user answer or "not specified"}
```

Update frontmatter in {workflowPlanFile} to append this step to
`stepsCompleted` (add `step-01-collect-ideas`).

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

Now let me find the right specialists to help evaluate this..."

---

### 9. Proceed to Next Step (Auto-Proceed)

Display: "**Proceeding to specialist matching...**"
Then load, read entire file, then execute {nextStepFile}.

#### Menu Handling Logic:
- After completion, immediately load, read entire file, then execute {nextStepFile}

#### EXECUTION RULES:
- This is an auto-proceed step (no menu)
- Do not wait for user menu selection

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



