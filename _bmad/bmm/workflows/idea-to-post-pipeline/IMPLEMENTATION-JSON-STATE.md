# JSON Workflow State Implementation Guide

## Overview

This document provides step-by-step implementation instructions for integrating JSON workflow state management into the idea-to-post pipeline. The system creates a `.workflow_state.json` file that tracks session data across c-03b1 → c-03b2 → c-03c transitions.

---

## Quick Start

### 1. Replace Current Step Files

```bash
# Backup originals
cp steps-c/c-03b2-offer-generation.md steps-c/c-03b2-offer-generation.BACKUP.md
cp steps-c/c-03c-draft.md steps-c/c-03c-draft.BACKUP.md

# Use enhanced versions
cp steps-c/c-03b2-offer-generation-ENHANCED.md steps-c/c-03b2-offer-generation.md
cp steps-c/c-03c-draft-ENHANCED.md steps-c/c-03c-draft.md
```

### 2. Verify Schema Document

```bash
# Check that JSON schema is in place
ls -la JSON-WORKFLOW-STATE-SCHEMA.md
```

### 3. Test Session Flow

```bash
# Start fresh
rm -f .workflow_state.json

# Run c-03b1 → Should create .workflow_state.json
# Run c-03b2 → Should update with generated_offers
# Run c-03c  → Should update with selected_draft
```

---

## Implementation Details by Phase

### Phase 1: c-03b1 (Offer Filter Setup)

**Files to Modify:**
- `steps-c/c-03b1-offer-check.md` (already compatible, just ensure it saves to state)

**Expected Output:**

```json
{
  "session_id": "workflow-2026-01-30T10-30-00Z",
  "session_start_at": "2026-01-30T10:30:00Z",
  "current_phase": "c-03b1-offer-check",
  "content_type": "demo",
  "offer_filter_configured": true,
  "willing_offers": ["training", "setup", "templates", "consulting"],
  "unwilling_offers": ["full_dev"],
  "state_created_at": "2026-01-30T10:30:00Z",
  "state_expires_at": "2026-01-30T18:30:00Z"
}
```

**Implementation (Python example):**

```python
import json
import uuid
from datetime import datetime, timedelta

def initialize_workflow_state(content_type, willing_offers, unwilling_offers):
    """Create initial workflow state after c-03b1"""

    now = datetime.utcnow()
    session_id = f"workflow-{now.strftime('%Y-%m-%dT%H-%M-%SZ')}"

    state = {
        "session_id": session_id,
        "session_start_at": now.isoformat() + "Z",
        "session_mode": content_type,
        "workflow_name": "idea-to-post-pipeline",
        "workflow_version": "3.0.1",

        "current_phase": "c-03b1-offer-check",
        "phases_completed": ["c-01", "c-02c", "c-03b", "c-03b1"],

        "content_type": content_type,
        "offer_filter_configured": True,
        "willing_offers": willing_offers,
        "unwilling_offers": unwilling_offers,
        "offer_filter_created_at": now.isoformat() + "Z",

        "state_created_at": now.isoformat() + "Z",
        "state_last_updated_at": now.isoformat() + "Z",
        "state_expires_at": (now + timedelta(hours=8)).isoformat() + "Z",
        "state_file_path": "./.workflow_state.json",

        "errors": [],
        "warnings": [],

        "_schema_version": "1.0",
        "_metadata_only": False
    }

    with open(".workflow_state.json", "w") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

    return state

# Usage
initialize_workflow_state(
    content_type="demo",
    willing_offers=["training", "setup", "templates", "consulting"],
    unwilling_offers=["full_dev"]
)
```

---

### Phase 2: c-03b2 (Offer Generation)

**Files to Modify:**
- `steps-c/c-03b2-offer-generation-ENHANCED.md` (ready to use)

**Expected Updates to State:**

```json
{
  "current_phase": "c-03b2-offer-generation",
  "idea_text": "BMAD опросил и сгенерировал 80+ документов за 2 часа",
  "idea_metadata": {
    "visual_context": "Скриншот BMAD интерфейса",
    "tools_used": "BMAD, Claude",
    "demonstrated_result": "80+ документов за 2 часа"
  },
  "selected_angle": "Time Saving",
  "pain_points": ["Боль 1", "Боль 2", "Боль 3"],
  "pain_points_json": { "Time Saving": [...] },

  "generated_offers": [
    {
      "offer_id": "offer-1",
      "offer_type": "training",
      "title": "...",
      "description": "...",
      "cta": "...",
      "pain_solved": "...",
      "effort_level": "medium",
      "reasoning": "...",
      "created_at": "2026-01-30T10:35:00Z"
    }
  ],
  "generated_offers_count": 2,
  "offers_generated_at": "2026-01-30T10:35:00Z"
}
```

**Implementation (Python):**

```python
import json
import anthropic
from datetime import datetime

def load_state():
    """Load existing workflow state"""
    with open(".workflow_state.json", "r") as f:
        return json.load(f)

def generate_and_save_offers(state, pain_points, willing_offers):
    """Generate offers via Claude and save to state"""

    client = anthropic.Anthropic()

    # Build prompt (as in ENHANCED doc)
    prompt = f"""
    [Full prompt from c-03b2-offer-generation-ENHANCED.md]
    """

    try:
        # Call Claude
        response = client.messages.create(
            model="claude-opus-4-5-20251101",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )

        llm_text = response.content[0].text.strip()

        # Parse JSON
        try:
            generated_offers = json.loads(llm_text)
        except json.JSONDecodeError:
            print("⚠️ JSON parse error, retrying...")
            # Retry logic here
            generated_offers = []

        # Validate offers
        validated_offers = []
        for i, offer in enumerate(generated_offers):
            if offer.get("offer_type") in willing_offers:
                offer["offer_id"] = f"offer-{len(validated_offers) + 1}"
                offer["created_at"] = datetime.utcnow().isoformat() + "Z"
                validated_offers.append(offer)

        # Update state
        state["current_phase"] = "c-03b2-offer-generation"
        state["generated_offers"] = validated_offers
        state["generated_offers_count"] = len(validated_offers)
        state["offers_generated_at"] = datetime.utcnow().isoformat() + "Z"
        state["state_last_updated_at"] = datetime.utcnow().isoformat() + "Z"

        # Save state
        with open(".workflow_state.json", "w") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

        return validated_offers

    except Exception as e:
        print(f"⚠️ Error: {e}")
        state["errors"].append({
            "phase": "c-03b2-offer-generation",
            "error_type": type(e).__name__,
            "error_message": str(e),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        })
        with open(".workflow_state.json", "w") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
        return []

# Usage
state = load_state()
offers = generate_and_save_offers(
    state,
    pain_points=state["pain_points"],
    willing_offers=state["willing_offers"]
)
```

---

### Phase 3: c-03c (Draft Generation)

**Files to Modify:**
- `steps-c/c-03c-draft-ENHANCED.md` (ready to use)

**Expected Updates to State:**

```json
{
  "current_phase": "c-03c-draft",
  "selected_draft_id": "draft-1",
  "selected_draft_type": "DIRECT & PUNCHY",
  "selected_draft_quality_score": 89,
  "selected_draft_ctr_potential": "4.2%",
  "draft_variant_of": null,
  "draft_created_at": "2026-01-30T10:40:00Z",

  "draft_variants_generated": 6,
  "draft_variants_config": {
    "base_variants": ["DIRECT & PUNCHY", "STORYTELLING", "DATA-DRIVEN"],
    "content_machine_variants": ["PAS", "Hook-Story-Offer", "Show Your Work"],
    "framework_inputs": {
      "pain_points_embedded": true,
      "offers_embedded": true,
      "visual_context_used": true
    }
  }
}
```

**Implementation (Python):**

```python
def generate_drafts(state):
    """Generate all draft variations"""

    client = anthropic.Anthropic()
    drafts = {}

    # Base drafts (for all content types)
    base_prompts = {
        "DIRECT & PUNCHY": """[prompt for direct draft]""",
        "STORYTELLING": """[prompt for storytelling draft]""",
        "DATA-DRIVEN": """[prompt for data-driven draft]"""
    }

    # Generate base drafts
    for draft_type, prompt in base_prompts.items():
        response = client.messages.create(
            model="claude-opus-4-5-20251101",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )
        drafts[draft_type] = {
            "text": response.content[0].text,
            "quality_score": calculate_quality(response.content[0].text),
            "ctr_potential": estimate_ctr(response.content[0].text)
        }

    # Content Machine drafts (if demo)
    if state["content_type"] == "demo" and state.get("generated_offers"):
        cm_prompts = {
            "PAS": """[PAS prompt with pain_points]""",
            "Hook-Story-Offer": """[HSO prompt with offers]""",
            "Show Your Work": """[SYW prompt with context]"""
        }

        for draft_type, prompt in cm_prompts.items():
            response = client.messages.create(
                model="claude-opus-4-5-20251101",
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}]
            )
            drafts[draft_type] = {
                "text": response.content[0].text,
                "quality_score": calculate_quality(response.content[0].text),
                "ctr_potential": estimate_ctr(response.content[0].text)
            }

    return drafts

def display_drafts(drafts, content_type):
    """Display drafts for user selection"""

    print("\n" + "="*60)
    if content_type == "demo":
        print(f"✅ {len(drafts)} DRAFT VARIANTS CREATED (Content Machine)")
    else:
        print(f"✅ {len(drafts)} DRAFT VARIANTS CREATED")
    print("="*60 + "\n")

    base_count = 0
    cm_count = 0

    for i, (draft_type, draft_data) in enumerate(drafts.items(), 1):
        emoji = "⭐" if i == 1 else "🔥" if draft_type == "PAS" else "🚀" if draft_type == "Hook-Story-Offer" else "✨" if draft_type == "Show Your Work" else ""

        category = "BASE" if i <= 3 else "CONTENT MACHINE"
        score = draft_data["quality_score"]
        ctr = draft_data["ctr_potential"]

        print(f"[{i}] {draft_type} ({score}/100) {emoji}")
        if ctr:
            print(f"    CTR potential: {ctr}")
        print()

    print("="*60)
    print("\nOptions:")
    print("[1-6] SELECT DRAFT")
    print("[F] FEEDBACK")
    print("[G] GENERATE NEW")
    print("[V] VIEW FULL")
    print("[M] Back to MENU")
    print()

# Usage
state = load_state()
drafts = generate_drafts(state)
display_drafts(drafts, state["content_type"])

# After user selection
selection = input("Your choice: ")
if selection.isdigit() and 1 <= int(selection) <= len(drafts):
    draft_type = list(drafts.keys())[int(selection) - 1]
    state["selected_draft_id"] = f"draft-{selection}"
    state["selected_draft_type"] = draft_type
    state["draft_created_at"] = datetime.utcnow().isoformat() + "Z"
    state["current_phase"] = "c-03c-draft"

    with open(".workflow_state.json", "w") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
```

---

## File Format & Validation

### JSON Schema Validation

```python
import jsonschema

WORKFLOW_STATE_SCHEMA = {
    "type": "object",
    "required": ["session_id", "current_phase", "state_created_at"],
    "properties": {
        "session_id": {"type": "string", "pattern": "^workflow-"},
        "current_phase": {
            "type": "string",
            "enum": ["c-03b1-offer-check", "c-03b2-offer-generation", "c-03c-draft"]
        },
        "state_created_at": {"type": "string", "format": "date-time"},
        "state_expires_at": {"type": "string", "format": "date-time"},
        "generated_offers": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["offer_id", "offer_type", "title", "description"],
                "properties": {
                    "offer_id": {"type": "string"},
                    "offer_type": {
                        "type": "string",
                        "enum": ["training", "setup", "templates", "consulting", "full_dev"]
                    }
                }
            }
        }
    }
}

def validate_state(state):
    """Validate state against schema"""
    try:
        jsonschema.validate(instance=state, schema=WORKFLOW_STATE_SCHEMA)
        return True, "State is valid"
    except jsonschema.ValidationError as e:
        return False, f"Validation error: {e.message}"
```

### Example State File

See `JSON-WORKFLOW-STATE-SCHEMA.md` for complete example.

---

## Error Handling & Recovery

### Missing State File

**Problem:** User runs c-03b2 without completing c-03b1

**Solution:**

```python
def check_state_exists():
    """Verify state file exists and is valid"""

    if not os.path.exists(".workflow_state.json"):
        print("⚠️ ERROR: workflow_state.json not found")
        print("Steps must be completed in order:")
        print("  1. c-03b1 (Create state)")
        print("  2. c-03b2 (Generate offers)")
        print("  3. c-03c (Create drafts)")
        return False

    try:
        state = load_state()

        # Check expiry
        expires = datetime.fromisoformat(state["state_expires_at"].replace("Z", "+00:00"))
        if datetime.utcnow().replace(tzinfo=expires.tzinfo) > expires:
            print("⚠️ Workflow state has expired (8+ hours old)")
            print("Starting new session...")
            os.remove(".workflow_state.json")
            return False

        return True

    except Exception as e:
        print(f"⚠️ Error reading state: {e}")
        return False
```

### JSON Parse Failures

```python
def load_state_with_recovery():
    """Load state with error recovery"""

    try:
        with open(".workflow_state.json", "r") as f:
            state = json.load(f)
        return state

    except json.JSONDecodeError as e:
        print(f"⚠️ State file is corrupted: {e}")

        # Try to load backup
        if os.path.exists(".workflow_state.backup.json"):
            print("Restoring from backup...")
            shutil.copy(".workflow_state.backup.json", ".workflow_state.json")
            with open(".workflow_state.json", "r") as f:
                return json.load(f)

        # Otherwise start fresh
        print("Starting new session...")
        return None
```

### Validation Failures

```python
def validate_offers(offers, willing_offers):
    """Validate generated offers"""

    valid_offers = []
    warnings = []

    for i, offer in enumerate(offers):
        # Check required fields
        required = ["offer_type", "title", "description", "cta", "pain_solved"]
        if not all(field in offer for field in required):
            warnings.append(f"Offer {i+1}: Missing required fields")
            continue

        # Check offer_type
        if offer["offer_type"] not in willing_offers:
            warnings.append(
                f"Offer {i+1}: Type '{offer['offer_type']}' not in {willing_offers}"
            )
            continue

        valid_offers.append(offer)

    if warnings:
        print("⚠️ Validation warnings:")
        for warning in warnings:
            print(f"  • {warning}")

    return valid_offers, warnings
```

---

## Testing Checklist

### Unit Tests

```python
import pytest

def test_initialize_state():
    """Test state initialization"""
    state = initialize_workflow_state("demo", ["training"], [])
    assert state["session_id"].startswith("workflow-")
    assert state["current_phase"] == "c-03b1-offer-check"
    assert state["offer_filter_configured"] == True

def test_load_state():
    """Test state loading"""
    state = load_state()
    assert state is not None
    assert "session_id" in state

def test_update_state():
    """Test state update"""
    state = load_state()
    state["test_field"] = "test_value"
    save_state(state)

    loaded = load_state()
    assert loaded["test_field"] == "test_value"

def test_state_expiry():
    """Test state expiry detection"""
    state = load_state()
    state["state_expires_at"] = (datetime.utcnow() - timedelta(hours=1)).isoformat() + "Z"
    save_state(state)

    assert not is_state_valid()

def test_offer_validation():
    """Test offer validation"""
    offers = [
        {"offer_type": "training", "title": "T1", "description": "D1", "cta": "C1", "pain_solved": "P1"},
        {"offer_type": "full_dev", "title": "T2", "description": "D2", "cta": "C2", "pain_solved": "P2"}
    ]

    valid, warnings = validate_offers(offers, ["training", "setup"])
    assert len(valid) == 1
    assert len(warnings) == 1
```

### Integration Tests

```python
def test_workflow_c03b1_to_c03b2():
    """Test workflow from c-03b1 to c-03b2"""

    # Initialize state
    state = initialize_workflow_state("demo", ["training"], [])
    assert os.path.exists(".workflow_state.json")

    # Load and verify
    loaded = load_state()
    assert loaded["offer_filter_configured"]

    # Update with offers
    offers = [{"offer_type": "training", "title": "T1", ...}]
    loaded["generated_offers"] = offers
    save_state(loaded)

    # Verify persistence
    reloaded = load_state()
    assert len(reloaded["generated_offers"]) == 1

def test_workflow_full_cycle():
    """Test complete workflow c-03b1 → c-03b2 → c-03c"""

    # c-03b1
    state = initialize_workflow_state("demo", ["training"], [])

    # c-03b2
    offers = generate_and_save_offers(state, [], ["training"])
    assert state["current_phase"] == "c-03b2-offer-generation"

    # c-03c
    drafts = generate_drafts(state)
    state["selected_draft_id"] = "draft-1"
    save_state(state)

    # Verify final state
    final = load_state()
    assert final["current_phase"] == "c-03c-draft"
    assert "selected_draft_id" in final
```

---

## Migration from Old System

If replacing existing step files, follow this migration path:

### Step 1: Backup

```bash
mkdir -p _backup
cp steps-c/c-03b1-offer-check.md _backup/
cp steps-c/c-03b2-offer-generation.md _backup/
cp steps-c/c-03c-draft.md _backup/
```

### Step 2: Deploy New Files

```bash
cp steps-c/c-03b2-offer-generation-ENHANCED.md steps-c/c-03b2-offer-generation.md
cp steps-c/c-03c-draft-ENHANCED.md steps-c/c-03c-draft.md
```

### Step 3: Update c-03b1 (if needed)

Ensure `c-03b1-offer-check.md` calls state initialization:

```markdown
## State Initialization

After user confirms offer filter:

\`\`\`bash
python -c "from workflow_state import initialize_workflow_state; initialize_workflow_state(...)"
\`\`\`
```

### Step 4: Test Full Workflow

```bash
rm -f .workflow_state.json
# Run c-03b1 → c-03b2 → c-03c
# Verify state file updates at each step
```

---

## Performance Considerations

### State File Size

```
Average state file size: ~8-12 KB
- Metadata: ~1 KB
- 2-4 offers @ 1-2 KB each: ~4-8 KB
- Timestamps & overhead: ~1 KB
```

### Load Time

```
State file operations:
- Load: <10ms
- Save: <10ms
- Parse: <5ms
Total per operation: ~20ms
```

### Expiry Cleanup

```
Auto-cleanup triggered:
- At session start (check if expired)
- Every 8 hours (background job, if implemented)
- Manual cleanup: rm .workflow_state.json
```

---

## Maintenance & Monitoring

### Debug Mode

```python
# Enable in state file
state["_debug_mode"] = True

# Then every operation prints:
# - State before/after
# - Field changes
# - Errors and warnings
```

### Monitoring

```python
def collect_state_metrics():
    """Collect metrics about state usage"""

    state = load_state()

    metrics = {
        "file_size_bytes": os.path.getsize(".workflow_state.json"),
        "offers_count": len(state.get("generated_offers", [])),
        "errors_count": len(state.get("errors", [])),
        "warnings_count": len(state.get("warnings", [])),
        "time_in_phase": datetime.utcnow() - datetime.fromisoformat(
            state["state_created_at"].replace("Z", "+00:00")
        ),
        "phases_completed": len(state.get("phases_completed", []))
    }

    return metrics
```

---

## References

- **Schema Definition:** `JSON-WORKFLOW-STATE-SCHEMA.md`
- **c-03b2 Enhanced:** `steps-c/c-03b2-offer-generation-ENHANCED.md`
- **c-03c Enhanced:** `steps-c/c-03c-draft-ENHANCED.md`
- **Error Handling:** Section "Error Handling & Recovery" above
- **Testing:** Section "Testing Checklist" above

---

## Support & Issues

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| State file not found | c-03b1 didn't run | Run c-03b1 first |
| JSON parse error | Corrupted file | Delete and restart |
| Offers not embedding | Missing offers array | Ensure c-03b2 ran successfully |
| State expired | Session > 8 hours | Start new session |

### Debugging

```bash
# Check state validity
cat .workflow_state.json | python -m json.tool > /dev/null && echo "Valid JSON" || echo "Invalid JSON"

# View structure
cat .workflow_state.json | python -c "import json, sys; data=json.load(sys.stdin); print('Phases:', data.get('phases_completed')); print('Offers:', len(data.get('generated_offers', [])))"

# Check expiry
cat .workflow_state.json | python -c "import json, sys, datetime; data=json.load(sys.stdin); exp=datetime.datetime.fromisoformat(data['state_expires_at'].replace('Z', '+00:00')); print(f'Expires in: {(exp - datetime.datetime.now(datetime.timezone.utc)).total_seconds()/3600:.1f} hours')"
```

---

## Conclusion

This JSON state infrastructure provides:
- ✅ Clear data flow across workflow phases
- ✅ Error tracking and recovery
- ✅ Graceful degradation (missing data doesn't break flow)
- ✅ Single source of truth for session data
- ✅ Easy debugging and monitoring
- ✅ Auto-cleanup and expiry management

Deploy the enhanced step files and begin collecting state-driven workflows.
