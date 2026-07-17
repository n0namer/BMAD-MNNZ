# CONTENT MACHINE PIPELINE - TEST EXECUTION QUICK REFERENCE

**For QA Engineers and Testers**

---

## QUICK START: How to Run the Tests

### Setup
```bash
cd "D:\Users\NIKITA\Documents\DEV\BMAD-MNNZ\_bmad\bmm\workflows\idea-to-post-pipeline"

# Ensure directories exist:
mkdir -p content_generation_system
mkdir -p user_preferences
```

---

## TEST CASE 1: Full Demo Workflow (Mode [R])

### Input Data
```
Screenshot: Any BMAD/ClaudeFlow interface showing results
Description: "Generated 80+ high-quality documents in 2 hours using BMAD"
```

### Execution Steps
```
1. Navigate to step-00-menu.md
2. Choose [1] CREATE MODE
3. Choose [1a] Add Idea
4. Select [R] ROUTINE mode
5. Upload screenshot
6. Enter description
7. Continue through research (c-02c)
8. Continue through pain generation (auto at c-02c)
9. Continue through offer filter (c-03b1) — FIRST RUN: configure preferences
10. Continue through offer generation (c-03b2)
11. Continue through draft generation (c-03c)
12. Continue through variant generation (c-03d)
13. Export to CSV
```

### Validation Checkpoints
```
✓ Step c-01: ideas_inbox.csv has 1 record with content_type="demo"
✓ Step c-02c: pain_points generated in workflow_state.json
✓ Step c-03b1: offer_filter.csv created in user_preferences/
✓ Step c-03b2: generated_offers in workflow_state.json (2-4 per angle)
✓ Step c-03c: 3 drafts with quality scores 85-92
✓ Step c-03d: 3 variants generated (total 6 posts)
✓ Final: posts_content.csv has 6 new records
```

### Expected Results
```
Duration: <5 minutes
Pain points: 15-25 total (3-5 per angle)
Offers: 2-4 per angle, respecting filter
Posts: 6 (3 base + 3 variants)
Quality range: 85-92
CSV records: 6
State file: Valid JSON
```

**Pass Criteria:** All checkpoints ✓, all expected results met

---

## TEST CASE 2: Standard Text Workflow (Mode [T])

### Input Data
```
Text idea: "How to scale personal brand without hiring writers"
```

### Execution Steps
```
1. Navigate to step-00-menu.md
2. Choose [1] CREATE MODE
3. Choose [1a] Add Idea
4. Select [T] TEXT mode
5. Enter text idea
6. Continue through workflow
```

### Key Differences
```
✗ NO screenshot (text only)
✗ NO pain generation
✗ NO offer generation
✗ NO offer filter
✗ 3 posts (not 6)
```

### Validation Checkpoints
```
✓ ideas_inbox.csv has 1 record with content_type="text"
✓ workflow_state.json NOT created
✓ pain_points NOT generated
✓ generated_offers NOT generated
✓ 3 drafts generated (no offers embedded)
✓ posts_content.csv has 3 new records
```

**Pass Criteria:** Standard workflow without CM pipeline triggers

---

## TEST CASE 3: Error Scenarios

### Scenario 3.1: Missing CSV Files
```
Expected: System creates files automatically
Validation: files created with proper headers
Pass: automatic creation successful
```

### Scenario 3.2: Invalid Screenshot
```
Expected: Vision API fails, fallback to text
Validation: error logged, workflow continues
Pass: graceful degradation
```

### Scenario 3.3: No offer_filter.csv (first run)
```
Expected: First-run setup form displayed
Validation: filter created and reused
Pass: filter persists across sessions
```

### Scenario 3.4: Corrupted workflow_state.json
```
Expected: Error detected, backup created, recovery offered
Validation: .bak file exists, user can continue
Pass: error recovery working
```

### Scenario 3.5: All offers rejected in filter
```
Expected: Workflow continues without offers
Validation: drafts have offers_embedded=0
Pass: edge case handled gracefully
```

---

## DATA EXPORT VERIFICATION

### Check CSV Files

```bash
# Verify ideas_inbox.csv
# Should have: id, date_added, source, raw_idea, content_type, idea_metadata, category, status, notes
# For CM: content_type="demo", idea_metadata contains JSON with visual_context, tools_used, etc.

# Verify posts_content.csv
# Should have: 6 records for TC1, 3 records for TC2
# Quality scores: TC1 85-92, TC2 80-88
# offers_embedded: TC1 records 1-2 have 1-2, others have 0 or 1

# Verify user_preferences/offer_filter.csv
# Should have: 5 rows (one per offer type)
# willing column: yes/no values
# For TC1: should have 4 yes (training, setup, templates, consulting) and 1 no (full_dev)
```

---

## TIMING CHECKLIST

| Stage | Expected | Notes |
|-------|----------|-------|
| Input (c-01) | <30 sec | Vision API if Mode [R] |
| Pain generation (c-02c) | <3 sec | If content_type="demo" |
| Offer filter (c-03b1) | <1 min | User interaction |
| Offer generation (c-03b2) | <2 sec | LLM batch |
| Draft generation (c-03c) | <5 sec | 3 posts in sequence |
| Variant generation (c-03d) | <8 sec | 3 variants in sequence |
| **Total TC1** | **<5 min** | With user decisions |
| **Total TC2** | **<10 min** | Shorter pipeline |

---

## QUALITY METRICS QUICK CHECK

### Draft Quality Score (0-100)
```
Hook effectiveness (0-20)   ✓ Attention-grabbing, problem-clear
Structure (0-20)            ✓ Intro→Body→CTA, proper flow
Offer integration (0-20)    ✓ Natural, not forced (if present)
Language quality (0-20)     ✓ Native, Telegram-appropriate tone
CTA effectiveness (0-20)    ✓ Clear and soft (if present)

Range for CM posts: 85-92
Range for text posts: 80-88
```

### Offer Quality Check
```
✓ Specific to routine (not generic)
✓ Solves at least one pain
✓ Respects filter (no unwanted types)
✓ Soft CTA (not pushy)
✓ Effort level realistic
✓ Logically sound (not forced)
```

---

## WORKFLOW STATE STRUCTURE (workflow_state.json)

```json
{
  "workflow_id": "idea-to-post-pipeline",
  "session_id": "test-session-001",
  "currentMode": "CREATE",
  "content_type": "demo",  // or "text"
  "currentStep": "c-03d-variants",
  "context": {
    "demo_input": {
      "screenshot": "...",
      "description": "...",
      "tools_used": [...],
      "visual_context": "...",
      "demonstrated_result": "..."
    },
    "pain_points": {
      "angle_1": ["pain1", "pain2", ...],
      "angle_2": [...],
      ...
    },
    "generated_offers": {
      "angle_1": [
        {
          "offer_type": "training/setup/templates/consulting/full_dev",
          "title": "...",
          "description": "...",
          "cta": "...",
          "pain_solved": "...",
          "effort_level": "low/medium/high"
        }
      ]
    },
    "drafts": [
      {
        "variant": 1,
        "framework": "Hook-Story-Offer",
        "content": "...",
        "quality_score": 92,
        "ctr_potential": 4.5,
        "engagement_score": 4.8,
        "offers_embedded": 2
      },
      ...
    ]
  }
}
```

---

## COMMON ISSUES & QUICK FIXES

### Issue: CSV file not found
**Fix:** Create directory `content_generation_system/` and let system auto-create file

### Issue: Vision API timeout
**Fix:** Catch error, fall back to text description, continue workflow

### Issue: offer_filter.csv not found
**Fix:** User is running Content Machine first time - display form, create file

### Issue: workflow_state.json parse error
**Fix:** Offer to regenerate or start fresh - create .bak backup

### Issue: Duplicated offers in generated_offers
**Fix:** Dedup in offer generation prompt or post-process

### Issue: Quality scores all same value
**Fix:** Verify scoring logic is calculating correctly, not hardcoding

---

## SIGN-OFF TEMPLATE

```
╔══════════════════════════════════════════════════════════╗
║    CONTENT MACHINE PIPELINE - QA SIGN-OFF               ║
╚══════════════════════════════════════════════════════════╝

TEST CASE 1 (Full Demo):     [ ] PASS  [ ] FAIL
TEST CASE 2 (Text):         [ ] PASS  [ ] FAIL
TEST CASE 3 (Error Handling):[ ] PASS  [ ] FAIL

PERFORMANCE:                 [ ] PASS  [ ] FAIL
DATA QUALITY:               [ ] PASS  [ ] FAIL
FILE I/O:                   [ ] PASS  [ ] FAIL
CSV EXPORTS:                [ ] PASS  [ ] FAIL
STATE MANAGEMENT:           [ ] PASS  [ ] FAIL

═══════════════════════════════════════════════════════════

OVERALL RESULT:

[  ] ✅ READY FOR PRODUCTION
[  ] ⚠️  READY WITH NOTES (list below)
[  ] ❌ NOT READY - BLOCKERS (list below)

NOTES / BLOCKERS:
___________________________________________________________
___________________________________________________________
___________________________________________________________

TESTER: _________________________ DATE: _______________

APPROVAL: ________________________ DATE: _______________
```

---

## NEXT ACTIONS AFTER TESTING

1. **If All Pass:** Proceed to production deployment
2. **If Issues Found:**
   - Document in blockers list
   - Create fixes
   - Re-test affected areas
   - Get re-approval
3. **Performance Optimization:** Consider parallel execution for future
4. **Documentation:** Update user guides based on test findings

---

**Testing Framework Version:** 1.0
**Last Updated:** 2026-01-30
**Maintained By:** Claude Code QA
