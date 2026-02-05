---
name: 'design-thinking-empathy'
version: '1.0'
purpose: 'Design Thinking Empathy Check protocol for idea validation'
consumedBy:
  - step-01-collect-ideas.md
  - step-02-roles-discovery.md
---

# Design Thinking: Empathy Check

## Goal

Frame new ideas with user-centric thinking by understanding the human context before proceeding with technical analysis.

## Protocol

Ask the user 2-3 empathy questions to understand who benefits and what problem is being solved.

### Question 1: Who benefits?

- "Кто получит пользу от этого проекта?"
- "Для кого это решает проблему?"

### Question 2: What pain does this solve?

- "Какую боль или проблему это устраняет?"
- "Что произойдёт, если эту проблему НЕ решить?"

### Question 3 (optional): Why now?

- "Почему это важно сейчас?"
- "Что изменилось, что делает это актуальным?"

## Guidance for Unclear Answers

- If user says "not sure yet" → That's OK! Mark as "to be explored" and continue
- If user struggles → Offer examples: "Например: клиенты, команда, личная продуктивность?"
- Don't block progress → Empathy questions are guidance, not gates

## Design Thinking Tip

💡 If you can't clearly answer "who benefits?" and "what pain?", the idea may need refinement. Consider pausing to gather more user insights.

## Output Format

Append to workflow plan:

```markdown
## Design Thinking: Empathy Framing

**Who Benefits:** {user answer or "to be explored"}
**Pain/Problem Solved:** {user answer or "to be explored"}
**Why Now:** {user answer or "not specified"}
```

## Integration Points

This protocol is executed in:
- **Step 01 (Collect Ideas)**: After basic idea capture, before clarifying questions
- **Step 02 (Roles Discovery)**: Referenced when defining stakeholder roles
