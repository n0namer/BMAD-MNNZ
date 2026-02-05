# User Validation Framework

## Per-Step Feedback Collection

### When to Collect
- ✅ After every step completion (before "Continue" menu)
- ✅ After workflow completion (overall satisfaction)
- ✅ When user cancels mid-workflow (exit reason)

### Feedback Types

**1. Quick Rating (Required)**
- 👍 Helpful (4-5/5)
- 😐 OK (3/5)
- 👎 Frustrating (1-2/5)

**2. Comment (Optional)**
- Free text input
- Common categories: Clarity, Speed, Value, Difficulty

**3. Metadata (Auto-captured)**
- Step ID
- Duration (time spent on step)
- Track (Quick/Standard/Deep)
- Timestamp
- Idea context

### Quality Thresholds

**Green (Healthy):**
- 80%+ 👍 Helpful ratings
- <10% 👎 Frustrating ratings
- Average duration within ±20% of estimated

**Yellow (Needs Attention):**
- 60-79% 👍 Helpful
- 10-20% 👎 Frustrating
- Duration variance 20-50%

**Red (Critical Issue):**
- <60% 👍 Helpful
- >20% 👎 Frustrating
- Duration variance >50%

### Analytics Queries

**Most problematic step:**
```bash
npx claude-flow@v3alpha memory search -q "feedback rating:frustrating"
```

**Step duration analysis:**
```bash
npx claude-flow@v3alpha memory search -q "feedback step:04-consilium duration"
```

**Track-specific issues:**
```bash
npx claude-flow@v3alpha memory search -q "feedback track:quick rating:frustrating"
```

### Response Protocol

**If step receives 3+ frustrating ratings:**
1. Review step instructions for clarity
2. Check if examples needed
3. Consider breaking into smaller steps
4. Add "Common Issues" section

**If duration consistently 2x+ estimate:**
1. Re-estimate duration
2. Check if step scope too broad
3. Consider splitting or simplifying

### Workflow Completion Feedback

After Step 09 (Complete):
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 Workflow Complete!

Overall experience?

⭐⭐⭐⭐⭐ Excellent - Would recommend
⭐⭐⭐⭐   Good - Minor issues
⭐⭐⭐     OK - Several issues
⭐⭐       Poor - Many problems
⭐         Bad - Needs major improvement

[Rating] {user input}

💬 **What could be better?** (optional)
[Type your thoughts or press Enter to skip]

Would you use this workflow again? [Y/N]
```

### Exit Feedback (If User Cancels)

If user exits mid-workflow:
```markdown
⏸️ Workflow paused at Step {N}

Why are you stopping?

[T] Taking too long
[C] Too confusing
[N] Not what I needed
[L] Will continue later
[O] Other reason

💬 **Specific reason?** (optional, helps us improve)
[Type your thoughts or press Enter to skip]
```

### Memory Storage Format

**Per-Step Feedback:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "user-context" \
  --key "feedback:step-{step-id}:{timestamp}" \
  --content "{
    \"step\": \"step-01-collect-ideas\",
    \"rating\": \"helpful\",
    \"comment\": \"Clear instructions\",
    \"duration\": \"5min\",
    \"track\": \"standard\",
    \"timestamp\": \"{ISO_datetime}\",
    \"idea_id\": \"{IDEA_ID}\"
  }"
```

**Workflow Completion Feedback:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "user-context" \
  --key "feedback:workflow-complete:{timestamp}" \
  --content "{
    \"overall_rating\": 5,
    \"comment\": \"Excellent workflow\",
    \"would_use_again\": true,
    \"track\": \"standard\",
    \"duration_total\": \"45min\",
    \"steps_completed\": 9,
    \"timestamp\": \"{ISO_datetime}\",
    \"idea_id\": \"{IDEA_ID}\"
  }"
```

**Exit Feedback:**
```bash
npx claude-flow@v3alpha memory store \
  --namespace "user-context" \
  --key "feedback:exit:{timestamp}" \
  --content "{
    \"exit_step\": \"step-04-consilium\",
    \"reason\": \"taking-too-long\",
    \"comment\": \"Too many specialists\",
    \"track\": \"deep\",
    \"timestamp\": \"{ISO_datetime}\",
    \"idea_id\": \"{IDEA_ID}\"
  }"
```

### Analytics Dashboard Command

**Create `/feedback` command that shows:**

```markdown
# Workflow Feedback Summary

## Overall Health: 🟢 GREEN

**Last 30 Days:**
- Total workflows: 42
- Completion rate: 85% (36/42 completed)
- Average rating: 4.2/5 ⭐⭐⭐⭐

## Step Performance

| Step | Rating | 👍 | 😐 | 👎 | Avg Duration | Issues |
|------|--------|----|----|----|--------------|---------|
| 01 Collect | 4.5/5 | 90% | 8% | 2% | 8 min | ✅ None |
| 02 Roles | 3.8/5 | 65% | 25% | 10% | 6 min | ⚠️ Clarity |
| 03 Specialist | 4.2/5 | 82% | 15% | 3% | 5 min | ✅ None |
| 04 Consilium | 3.5/5 | 58% | 30% | 12% | 25 min | 🔴 Too long |
| 05 Scoring | 4.0/5 | 75% | 20% | 5% | 12 min | ✅ None |

## Top Issues (Last 30 Days)

1. **Step 04 (Consilium) - 12% frustrating**
   - "Takes too long" (5 mentions)
   - "Too many specialists" (3 mentions)
   - **Action:** Consider Consilium Lite for more ideas

2. **Step 02 (Roles) - 10% frustrating**
   - "Not clear which roles to pick" (4 mentions)
   - **Action:** Add more examples

3. **Duration variance**
   - Step 04: 25 min actual vs 15 min estimated (+67%)
   - **Action:** Update estimates

## Recommendations

✅ Step 01: Keep doing what works (90% helpful)
⚠️ Step 04: Reduce time or improve clarity (58% helpful)
⚠️ Step 02: Add examples (65% helpful)
```

### Integration with Hooks

**Update post-task hook:**
```javascript
// After step completion
if (stepCompleted) {
  saveStepFeedback({
    step: stepId,
    duration: actualDuration,
    rating: userRating, // from feedback prompt
    comment: userComment,
    track: currentTrack
  });

  // Check thresholds
  const stepHealth = analyzeStepHealth(stepId);
  if (stepHealth === 'red') {
    notifyDevelopers(`Step ${stepId} has critical feedback issues`);
  }
}
```

### User Experience Design

**Feedback takes 5-10 seconds (optional):**
- User can skip by pressing Enter
- Doesn't interrupt workflow flow
- Provides value to future users
- Non-intrusive UI placement

**Feedback block format (< 10 lines per step file):**
```markdown
---

## 📊 Quick Feedback (Optional)

This step: 👍 Helpful | 😐 OK | 👎 Frustrating

[Type feedback or press Enter to skip]

---
```

### Success Criteria

- ✅ Feedback collected after every step
- ✅ Memory stores all feedback with metadata
- ✅ Analytics available via `/feedback` command
- ✅ Quality thresholds defined (green/yellow/red)
- ✅ Response protocol for problematic steps
- ✅ Non-intrusive (optional, quick)

### BMAD Compliance

- Feedback block < 10 lines per step file
- Doesn't disrupt workflow flow
- Optional (user can skip with Enter)
- Provides continuous improvement data
- Enables data-driven workflow optimization
