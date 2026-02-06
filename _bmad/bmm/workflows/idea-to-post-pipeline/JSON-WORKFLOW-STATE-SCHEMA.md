# JSON Workflow State Infrastructure

## Overview

This document defines the complete JSON schema and lifecycle for workflow state management in the idea-to-post pipeline. The workflow state file tracks session progress, data flow, and intermediate results across steps.

---

## File Location & Lifecycle

**File:** `.workflow_state.json` (root directory of project)

**Lifecycle:**
- **Created:** During step c-03b1 (offer profile setup)
- **Updated:** After each major phase (c-03b1, c-03b2, c-03c, etc.)
- **Expires:** 8 hours after creation (auto-cleanup)
- **Scope:** Single session (NOT persistent across sessions)

---

## Complete JSON Schema

```json
{
  "// METADATA": "=== SESSION & TRACKING INFO ===",
  "session_id": "workflow-2026-01-30T10-35-00Z",
  "session_start_at": "2026-01-30T10:30:00Z",
  "session_mode": "demo | normal",
  "workflow_name": "idea-to-post-pipeline",
  "workflow_version": "3.0.1",

  "// WORKFLOW PHASE": "=== CURRENT STEP TRACKING ===",
  "current_phase": "c-03b2-offer-generation",
  "phase_sequence": ["c-01", "c-02c", "c-03b", "c-03b1", "c-03b2", "c-03c"],
  "phases_completed": ["c-01", "c-02c", "c-03b", "c-03b1"],

  "// INPUT DATA": "=== DATA LOADED FROM PREVIOUS STEPS ===",
  "content_type": "demo",
  "selected_idea_id": "idea-123",
  "idea_text": "BMAD опросил и сгенерировал 80+ документов за 2 часа",
  "idea_metadata": {
    "visual_context": "Скриншот BMAD интерфейса с 80+ документами в списке",
    "tools_used": "BMAD, Claude",
    "demonstrated_result": "80+ документов за 2 часа"
  },
  "selected_angle": "Time Saving",
  "angle_description": "Экономия времени на документацию через BMAD",

  "// PAIN POINTS": "=== FROM c-02c ===",
  "pain_points": [
    "Документация занимает дни, а результат плохой",
    "Все в голове у одного сотрудника",
    "Нельзя масштабировать бизнес без процессов"
  ],
  "pain_points_json": {
    "Time Saving": [
      "Медленная обработка большого объёма документов",
      "Нет описанных процессов → бизнес не продать",
      "Всё в голове у фаундера → невозможно делегировать"
    ]
  },

  "// OFFER PROFILE": "=== FROM c-03b1 ===",
  "offer_filter_configured": true,
  "willing_offers": ["training", "setup", "templates", "consulting"],
  "unwilling_offers": ["full_dev"],
  "offer_filter_created_at": "2026-01-30T10:30:00Z",

  "// GENERATED OFFERS": "=== FROM c-03b2 ===",
  "generated_offers": [
    {
      "offer_id": "offer-1",
      "offer_type": "training",
      "title": "Обучение BMAD для Документации",
      "description": "Научу вас генерировать 80+ документов за 2 часа, как в демо. Вы получите готовый workflow, шаблоны и полное понимание процесса.",
      "cta": "Напишите в личку — обсудим формат обучения.",
      "pain_solved": "Медленная обработка большого объёма документов",
      "effort_level": "medium",
      "reasoning": "Рутина показывает реальный инструмент (BMAD), результат (80+ доков), боль (медленная документация). Обучение масштабируется и решает проблему.",
      "created_at": "2026-01-30T10:35:00Z"
    },
    {
      "offer_id": "offer-2",
      "offer_type": "setup",
      "title": "Setup BMAD-Процесса за 3 Дня",
      "description": "Спроектирую и разверну workflow, который будет генерировать вашу документацию с минимальным участием. Адаптация под вашу задачу.",
      "cta": "Дайте мне юзкейс вашей компании — покажу, как это может работать.",
      "pain_solved": "Нет описанных процессов → бизнес не продать",
      "effort_level": "high",
      "reasoning": "Setup решает две боли сразу: процессы документируются, люди могут заменяться.",
      "created_at": "2026-01-30T10:35:00Z"
    }
  ],
  "generated_offers_count": 2,
  "offers_generated_at": "2026-01-30T10:35:00Z",

  "// DRAFT DATA": "=== FROM c-03c ===",
  "selected_draft_id": "draft-1",
  "selected_draft_type": "DIRECT & PUNCHY",
  "selected_draft_quality_score": 89,
  "selected_draft_ctr_potential": "4.2%",
  "draft_variant_of": null,
  "draft_content_preview": "3 часа вместо недели...",
  "draft_full_text": "[full 600-800 char text]",
  "draft_created_at": "2026-01-30T10:40:00Z",

  "// DRAFT VARIANTS": "=== ADDITIONAL CM FRAMEWORKS (demo only) ===",
  "draft_variants_generated": 6,
  "draft_variants_config": {
    "base_variants": ["DIRECT & PUNCHY", "STORYTELLING", "DATA-DRIVEN"],
    "content_machine_variants": ["PAS", "Hook-Story-Offer", "Show Your Work"],
    "framework_inputs": {
      "pain_points_embedded": true,
      "offers_embedded": true,
      "visual_context_used": true
    }
  },

  "// TIMESTAMPS & EXPIRY": "=== STATE LIFECYCLE ===",
  "state_created_at": "2026-01-30T10:30:00Z",
  "state_last_updated_at": "2026-01-30T10:40:00Z",
  "state_expires_at": "2026-01-30T18:30:00Z",
  "state_file_path": "./.workflow_state.json",

  "// ERROR HANDLING": "=== TRACK ISSUES & RETRIES ===",
  "errors": [],
  "warnings": [],
  "retry_count": 0,
  "last_error": null,

  "// INTERNAL": "=== SYSTEM USE ONLY ===",
  "_schema_version": "1.0",
  "_metadata_only": false,
  "_debug_mode": false
}
```

---

## Phase-by-Phase Data Flow

### Phase: c-03b1 (Offer Filter Setup)

**Creates/Updates:**
```json
{
  "session_id": "workflow-{timestamp}",
  "current_phase": "c-03b1-offer-check",
  "offer_filter_configured": true,
  "willing_offers": ["training", "setup", "templates", "consulting"],
  "unwilling_offers": ["full_dev"],
  "offer_filter_created_at": "2026-01-30T10:30:00Z"
}
```

**Action:** User selects willing offer types, system saves to `.workflow_state.json`

---

### Phase: c-03b2 (Offer Generation)

**Loads:** Everything from c-03b1, plus:
- `idea_text` (from c-01)
- `pain_points` (from c-02c)
- `selected_angle` (from c-03b)

**Generates & Saves:**
```json
{
  "current_phase": "c-03b2-offer-generation",
  "generated_offers": [
    {offer data array}
  ],
  "generated_offers_count": 2,
  "offers_generated_at": "2026-01-30T10:35:00Z"
}
```

**Action:** System calls LLM, validates JSON, saves offers to state

---

### Phase: c-03c (Draft Generation)

**Loads:** Everything from c-03b2, plus:
- `willing_offers`
- `generated_offers`
- `pain_points`

**Generates & Saves:**
```json
{
  "current_phase": "c-03c-draft",
  "selected_draft_id": "draft-1",
  "selected_draft_type": "DIRECT & PUNCHY",
  "draft_variant_of": null,
  "draft_created_at": "2026-01-30T10:40:00Z",

  "draft_variants_generated": 6,
  "draft_variants_config": {
    "base_variants": [...],
    "content_machine_variants": [...],
    "framework_inputs": {...}
  }
}
```

**Action:** System generates 3-6 draft variations, embeds offers into CM frameworks, saves metadata

---

## Cleanup & Expiry

### Auto-Cleanup

- **Trigger:** 8 hours after `state_created_at`
- **Action:** Delete `.workflow_state.json`
- **Reason:** Each session should start fresh with new state

### Manual Cleanup

- **Trigger:** When user moves to new workflow/idea
- **Action:** Delete old `.workflow_state.json` before creating new one
- **Check:** If file exists and `current_phase` is from previous workflow, prompt user

### Persistent Data Storage

**NOT in workflow_state (ephemeral):**
- Offer profiles → Saved to `user_preferences/offer_filter.csv`
- Published posts → Saved to `posts_content.csv`
- Research notes → Saved to `ideas_research.csv`

---

## Error Handling

### JSON Parsing Failures

```json
{
  "errors": [
    {
      "phase": "c-03b2-offer-generation",
      "error_type": "JSON_PARSE_ERROR",
      "error_message": "Unexpected token } at position 234",
      "llm_response_preview": "[truncated response]",
      "retry_count": 1,
      "timestamp": "2026-01-30T10:35:15Z"
    }
  ]
}
```

**Recovery:** System retries LLM call (max 2 attempts)

### Validation Failures

```json
{
  "warnings": [
    {
      "phase": "c-03b2-offer-generation",
      "warning_type": "INVALID_OFFER_TYPE",
      "detail": "Offer 'full_dev' not in willing_offers",
      "action_taken": "Filtered out, LLM re-prompted",
      "timestamp": "2026-01-30T10:35:20Z"
    }
  ]
}
```

**Recovery:** Filter invalid offers, re-prompt LLM if too few valid offers

### Missing Data

```json
{
  "errors": [
    {
      "phase": "c-03c-draft",
      "error_type": "MISSING_DATA",
      "missing_field": "generated_offers",
      "fallback": "Using empty offers array, skipping CM frameworks",
      "timestamp": "2026-01-30T10:40:00Z"
    }
  ]
}
```

**Recovery:** Skip that feature, continue with graceful degradation

---

## Loading & Persistence Logic

### Check if State Exists

```python
if os.path.exists('.workflow_state.json'):
    with open('.workflow_state.json') as f:
        state = json.load(f)

    # Check expiry
    if datetime.fromisoformat(state['state_expires_at']) < datetime.now():
        os.remove('.workflow_state.json')
        state = {}  # Start fresh
    else:
        # Load existing state
        load_phase_data(state)
else:
    state = initialize_new_state()
```

### Update State

```python
state['current_phase'] = 'c-03c-draft'
state['state_last_updated_at'] = datetime.now().isoformat()

with open('.workflow_state.json', 'w') as f:
    json.dump(state, f, indent=2)
```

### Extract Data for LLM

```python
llm_input = {
    'routine': state['idea_text'],
    'pain_points': state['pain_points_json'][state['selected_angle']],
    'angle': state['selected_angle'],
    'willing_offers': state['willing_offers']
}
```

---

## Integration Points

### c-03b1 → c-03b2

**c-03b1 Output:**
- `offer_filter_configured`: true
- `willing_offers`: array
- `unwilling_offers`: array

**c-03b2 Input:**
- Loads `willing_offers` for filtering LLM output

---

### c-03b2 → c-03c

**c-03b2 Output:**
- `generated_offers`: array of 2-4 offers

**c-03c Input:**
- Loads `generated_offers`
- Embeds into DRAFT 4-6 (PAS, Hook-Story-Offer, Show Your Work)
- If missing, skips CM frameworks

---

### c-03c → c-03d (Variants)

**c-03c Output:**
- `selected_draft_id`: string
- `selected_draft_type`: string
- `draft_variant_of`: null or post_id

**c-03d Input:**
- Uses `selected_draft_id` to load draft text
- If `draft_variant_of` exists, modifies for variant

---

## Example: Complete Workflow Session

### Initial State (c-03b1)

```json
{
  "session_id": "workflow-2026-01-30T10-30-00Z",
  "current_phase": "c-03b1-offer-check",
  "content_type": "demo",
  "selected_idea_id": "idea-123",
  "offer_filter_configured": true,
  "willing_offers": ["training", "setup", "templates", "consulting"],
  "state_created_at": "2026-01-30T10:30:00Z"
}
```

### After c-03b2

```json
{
  "session_id": "workflow-2026-01-30T10-30-00Z",
  "current_phase": "c-03b2-offer-generation",
  "... (same as above)",
  "generated_offers": [
    {offer-1},
    {offer-2}
  ],
  "generated_offers_count": 2,
  "offers_generated_at": "2026-01-30T10:35:00Z",
  "state_last_updated_at": "2026-01-30T10:35:00Z"
}
```

### After c-03c

```json
{
  "session_id": "workflow-2026-01-30T10-30-00Z",
  "current_phase": "c-03c-draft",
  "... (all previous data)",
  "selected_draft_id": "draft-1",
  "selected_draft_type": "DIRECT & PUNCHY",
  "draft_created_at": "2026-01-30T10:40:00Z",
  "draft_variants_generated": 6,
  "state_last_updated_at": "2026-01-30T10:40:00Z"
}
```

---

## Key Design Principles

1. **Single Source of Truth:** `.workflow_state.json` holds all intermediate data
2. **Ephemeral:** State expires after 8 hours (prevents stale data)
3. **Graceful Degradation:** Missing data doesn't break flow
4. **Error Tracking:** All errors/warnings logged in state
5. **Clear Lineage:** Each offer/draft tracks its inputs and creation timestamp
6. **Audit Trail:** Every phase documents what data it loaded and created
7. **No Duplication:** Only stored once (not repeated in CSV)

---

## Validation Checklist

When saving state, verify:
- ✓ `session_id` is unique and ISO datetime
- ✓ `current_phase` matches actual step
- ✓ `state_expires_at` is 8 hours from creation
- ✓ All offer IDs are unique (`offer-1`, `offer-2`, etc.)
- ✓ All offers have `offer_type` in `willing_offers`
- ✓ No circular dependencies in phase sequence
- ✓ All timestamps are ISO format (YYYY-MM-DDTHH:MM:SSZ)
- ✓ Error array contains proper structure

---

## Migration & Versioning

**Current Schema Version:** 1.0

**Backward Compatibility:** When loading older versions:
1. Check `_schema_version`
2. If < 1.0, upgrade field names (if any schema changes in future)
3. Add missing fields with defaults
4. Save upgraded version back to disk

---

## Testing & Debugging

### Enable Debug Mode

```json
{
  "_debug_mode": true
}
```

When enabled:
- Print full state to console after each update
- Save backup copy as `.workflow_state.backup.json`
- Log all phase transitions

### Inspect State

```bash
# Pretty print state
cat .workflow_state.json | python -m json.tool

# Count offers
cat .workflow_state.json | python -c "import json, sys; data=json.load(sys.stdin); print(f'Offers: {len(data.get(\"generated_offers\", []))}')"

# Check expiry
cat .workflow_state.json | python -c "import json, sys, datetime; data=json.load(sys.stdin); exp=datetime.datetime.fromisoformat(data['state_expires_at']); print(f'Expires in: {(exp - datetime.datetime.now()).total_seconds()/3600:.1f} hours')"
```

---

## References

- Implemented in: c-03b2-offer-generation.md, c-03c-draft.md
- Persistent data: user_preferences/offer_filter.csv, posts_content.csv
- Session tracking: SESSION.md or equivalent
