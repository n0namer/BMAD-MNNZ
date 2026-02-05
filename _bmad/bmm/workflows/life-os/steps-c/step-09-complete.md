---
name: 'step-09-complete'
description: 'Finalize the create flow and confirm completion'
---

# Step 9: Complete

## STEP GOAL:

Confirm that the create flow finished successfully and provide a clear completion message.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

## EXECUTION PROTOCOLS:

- 🎯 Summarize what was created (plan + project artifacts)
- 💾 Confirm that the workflow is complete

## MANDATORY SEQUENCE

### 1. Confirm Completion

Say:
"✅ **Проект создан и сохранен.**  
Вы можете вернуться к редактированию или обзору в любой момент."

---

## 📊 Workflow Complete - Overall Feedback

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 Workflow Complete!

Overall experience?

⭐⭐⭐⭐⭐ Excellent - Would recommend
⭐⭐⭐⭐   Good - Minor issues
⭐⭐⭐     OK - Several issues
⭐⭐       Poor - Many problems
⭐         Bad - Needs major improvement

[Rating 1-5]

💬 **What could be better?** (optional)
[Type your thoughts or press Enter to skip]

Would you use this workflow again? [Y/N]

**After user responds, save to memory:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "user-context" \
  --key "feedback:workflow-complete:{timestamp}" \
  --content "{\"overall_rating\": {1-5}, \"comment\": \"{user_comment}\", \"would_use_again\": {true/false}, \"track\": \"{track}\", \"timestamp\": \"{ISO_datetime}\"}"
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---

## 📦 Archive This Idea

Idea complete! Archive for future reference and pattern learning?

**Archiving benefits:**
- Systematic storage in quarterly folder
- Pattern mining for similar ideas
- Calibrate estimates over time
- Cross-reference past successes

Options:
- **[A]** - Archive Now (recommended - includes retrospective)
- **[L]** - Later - Archive during quarterly review
- **[S]** - Skip - Don't archive

**If [A] selected:**
```bash
# Windows
cd scripts
.\archive-idea.ps1 -IdeaId "{idea-id}" -Status "completed"

# macOS/Linux
cd scripts
./archive-idea.sh {idea-id} completed
```

After archival completes:
```
✅ Idea archived to: output/archive/completed/{quarter}/
💾 Saved to global memory for pattern mining
```

---

## 📊 Retrospective (Optional)

This idea is complete! Help improve future estimates?

**Quick retrospective:** (5-10 minutes)
- Compare planned vs actual timeline
- Identify what went well / what could improve
- Calibrate Speed Multiplier for future ideas

Options:
- **[R]** - Run Retrospective Now (recommended)
- **[L]** - Later - Reminder in quarterly review
- **[S]** - Skip - Complete without retrospective

**Note:** If you archived above, retrospective is automatically included in archive.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS
- Completion message delivered
- User understands workflow is complete
- Retrospective option offered

### ❌ SYSTEM FAILURE
- No clear completion confirmation
- Retrospective not mentioned

**Master Rule:** End with a clear completion message and offer retrospective.
