# Implementation Guide: CSV Schema & JSON Structure Updates

**Document Type:** Implementation Roadmap
**Priority Level:** CRITICAL - Blocks Content Machine Pipeline
**Estimated Time:** 7.5 hours
**Status:** Ready for Execution

---

## Overview

This guide provides step-by-step instructions for implementing the CSV schema updates and JSON structures required for the idea-to-post-pipeline Content Machine to function properly.

### What Needs to Be Done
1. Add `pain_points_json` to ideas_research.csv
2. Create `user_preferences/offer_filter.csv` (new file)
3. Create `.bmad/workflow_state.json` infrastructure
4. Add data type columns to posts_content.csv
5. Create and run validation scripts

### Impact
- Enables Content Machine pipeline (c-02c → c-03c)
- Supports offer generation and tracking
- Enables draft variant creation with embedded offers
- Supports workflow state persistence across steps

---

## STEP 1: Add pain_points_json to ideas_research.csv

### 1.1 Understanding the Structure

**What:** A JSON column storing pain points organized by angle
**Why:** Content Machine uses these to generate relevant offers
**When:** Populated during step c-02c (research)
**Used By:** Step c-03b2 (offer generation)

### 1.2 Expected Format

```json
{
  "angle_1": [
    "Медленная документация берёт 2-3 дня на большой объём",
    "Все процессы в голове у одного человека",
    "Нельщо масштабировать без найма новых специалистов",
    "Непроцессированная информация = нельзя продать бизнес"
  ],
  "angle_2": [
    "Качество документов зависит от того кто их написал",
    "Нет стандарта, каждый пишет по-своему",
    "Редактирование и проверка занимают много времени"
  ]
}
```

### 1.3 Implementation Steps

**Step 1.3a: Add Column Header**

File: `_bmad/bmm/workflows/idea-to-post-pipeline/templates/csv/ideas_research_template.csv`

```csv
# Current:
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance

# Change to:
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance,pain_points_json
```

**Step 1.3b: Update All Template Copies**

```bash
# Files to update:
_bmad/bmm/workflows/idea-to-post-pipeline/data/csv-templates/ideas_research_template.csv
_bmad/bmm/workflows/idea-to-post-pipeline/templates/csv/ideas_research_template.csv
```

Both should be identical. If different, consolidate and use one as source of truth.

**Step 1.3c: Create Migration Helper**

```python
# File: scripts/migrate_csv_schema.py

import csv
import json
from datetime import datetime

def add_pain_points_column():
    """Add pain_points_json column to ideas_research.csv with NULL defaults"""

    input_file = '_bmad/bmm/workflows/idea-to-post-pipeline/data/ideas_research.csv'
    output_file = input_file  # Overwrite original

    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        # Check if pain_points_json already exists
        if 'pain_points_json' in fieldnames:
            print("✅ Column already exists, skipping...")
            return

        # Add new column
        fieldnames = list(fieldnames) + ['pain_points_json']

        # Read all data and add NULL to new column
        for row in reader:
            row['pain_points_json'] = None  # Will be populated during research
            rows.append(row)

    # Write back with new column
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Added pain_points_json column to {len(rows)} rows")
    print(f"   File: {output_file}")

# Run migration
if __name__ == '__main__':
    add_pain_points_column()
```

**Step 1.3d: Run Migration**

```bash
cd _bmad/bmm/workflows/idea-to-post-pipeline
python ../../scripts/migrate_csv_schema.py
```

**Expected Output:**
```
✅ Added pain_points_json column to 5 rows
   File: _bmad/bmm/workflows/idea-to-post-pipeline/data/ideas_research.csv
```

### 1.4 Validation

**Check the file manually:**
```bash
# Should see new column at end:
head -1 data/ideas_research.csv
# Output: id,original_idea_id,...,avg_relevance,pain_points_json
```

**Verify data integrity:**
```python
import csv
with open('data/ideas_research.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # All rows should have pain_points_json = NULL initially
        assert row['pain_points_json'] == '' or row['pain_points_json'] is None
        print(f"Row {row['id']}: pain_points_json = {row['pain_points_json']} ✓")
```

---

## STEP 2: Create user_preferences Directory and offer_filter.csv

### 2.1 Directory Structure

```
idea-to-post-pipeline/
├── user_preferences/          # NEW
│   ├── offer_filter.csv       # NEW
│   └── .gitignore             # (add this file)
├── data/
├── templates/
├── steps-c/
└── ...
```

### 2.2 Create Directory

```bash
mkdir -p _bmad/bmm/workflows/idea-to-post-pipeline/user_preferences
```

### 2.3 Create offer_filter.csv

**File:** `user_preferences/offer_filter.csv`

```csv
offer_type,willing,notes
training,1,"Offer 1-on-1 coaching and mentoring sessions"
setup,1,"Can design processes and workflows for clients"
templates,1,"Have methodology templates and guides ready"
consulting,0,"May add later - time constraints now"
full_dev,0,"Cannot do full development at this stage"
```

**Why these values:**
- `offer_type`: 5 predefined types (don't add more)
- `willing`: 1=yes (will generate offers of this type), 0=no
- `notes`: Reason why included/excluded

### 2.4 Create .gitignore

**File:** `user_preferences/.gitignore`

```
# User preferences are personal config - don't version control
*.csv
*.json
.DS_Store
```

### 2.5 Add to Main .gitignore

**File:** `.gitignore` (at project root)

Add this line:
```
# User-specific preferences
user_preferences/offer_filter.csv
.bmad/workflow_state.json
```

### 2.6 Validation

```bash
# Check directory created:
ls -la user_preferences/
# Should show: offer_filter.csv and .gitignore

# Check CSV content:
cat user_preferences/offer_filter.csv
# Should match format above

# Check columns:
head -1 user_preferences/offer_filter.csv
# Output: offer_type,willing,notes
```

---

## STEP 3: Create workflow_state.json Infrastructure

### 3.1 Purpose

- **Temporary storage** of generated offers and draft variants
- **Bridges steps** c-03b2 (offer generation) → c-03c (draft creation)
- **Auto-deleted** after c-03e (finalization)

### 3.2 File Location and Structure

**File:** `.bmad/workflow_state.json`

```json
{
  "session_id": "session-2026-01-30-15-32-45",
  "current_step": "c-03b2",
  "timestamp_created": "2026-01-30T15:32:45Z",
  "content_type": "demo",
  "selected_idea_id": 1,
  "selected_angle": "angle_1",
  "generated_offers": [
    {
      "id": "offer-1",
      "type": "training",
      "title": "BMAD Documentation Workshop",
      "description": "Learn how to structure documents using BMAD framework",
      "cta": "Book your 2-hour session",
      "pain_solved": [
        "Все процессы в голове у одного человека",
        "Нельзя масштабировать без найма новых специалистов"
      ],
      "effort_level": "medium",
      "estimated_price_range": "$500-1000"
    }
  ],
  "draft_variants": [
    {
      "variant_id": "draft-1",
      "title": "Быстрая документация с BMAD",
      "hook": "80+ документов за 2 часа?",
      "body": "Вчера за 2 часа сгенерировал 80+ документов...",
      "cta": "Узнай как →",
      "selected": false
    }
  ],
  "stepsCompleted": {
    "c-03b1": true,
    "c-03b2": true,
    "c-03c": false
  }
}
```

### 3.3 Schema Validation Script

Create file: `scripts/validate_workflow_state.py`

```python
import json
from jsonschema import validate, ValidationError

WORKFLOW_STATE_SCHEMA = {
    "type": "object",
    "required": ["session_id", "current_step", "generated_offers", "stepsCompleted"],
    "properties": {
        "session_id": {"type": "string"},
        "current_step": {"type": "string"},
        "timestamp_created": {"type": "string"},
        "content_type": {"enum": ["demo", "evergreen", "topical"]},
        "selected_idea_id": {"type": "integer", "minimum": 1},
        "selected_angle": {"type": "string"},
        "generated_offers": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "type", "title", "cta", "pain_solved"],
                "properties": {
                    "id": {"type": "string"},
                    "type": {"enum": ["training", "setup", "templates", "consulting", "full_dev"]},
                    "title": {"type": "string", "minLength": 10, "maxLength": 80},
                    "description": {"type": "string"},
                    "cta": {"type": "string", "minLength": 5, "maxLength": 50},
                    "pain_solved": {
                        "type": "array",
                        "items": {"type": "string"},
                        "minItems": 1,
                        "maxItems": 5
                    },
                    "effort_level": {"enum": ["low", "medium", "high"]},
                    "estimated_price_range": {"type": "string"}
                }
            }
        },
        "draft_variants": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["variant_id", "title", "hook", "body", "cta"],
                "properties": {
                    "variant_id": {"type": "string"},
                    "title": {"type": "string", "minLength": 10, "maxLength": 80},
                    "hook": {"type": "string", "minLength": 5, "maxLength": 100},
                    "body": {"type": "string", "maxLength": 500},
                    "cta": {"type": "string", "minLength": 5, "maxLength": 50},
                    "selected": {"type": "boolean"}
                }
            }
        },
        "stepsCompleted": {"type": "object"}
    }
}

def validate_workflow_state(filepath):
    """Validate workflow_state.json against schema"""
    with open(filepath) as f:
        state = json.load(f)

    try:
        validate(instance=state, schema=WORKFLOW_STATE_SCHEMA)
        print(f"✅ {filepath} is valid")
        return True
    except ValidationError as e:
        print(f"❌ Validation error in {filepath}:")
        print(f"   {e.message}")
        return False
```

### 3.4 File Lifecycle

**Creation:** Step c-03b2
```python
# In c-03b2-offer-generation.md logic:
state = {
    "session_id": generate_session_id(),
    "current_step": "c-03b2",
    "generated_offers": [offers...],
    "stepsCompleted": {"c-03b1": True, "c-03b2": True, "c-03c": False}
}
save_json(".bmad/workflow_state.json", state)
```

**Update:** Step c-03c
```python
# In c-03c-draft.md logic:
state = load_json(".bmad/workflow_state.json")
state['current_step'] = "c-03c"
state['draft_variants'] = [variants...]
state['stepsCompleted']['c-03c'] = True
save_json(".bmad/workflow_state.json", state)
```

**Delete:** Step c-03e
```python
# In c-03e-finalize.md logic (after saving to posts_content.csv):
import os
if os.path.exists(".bmad/workflow_state.json"):
    os.remove(".bmad/workflow_state.json")
    print("✅ Cleaned up workflow state")
```

### 3.5 Add to .gitignore

**File:** `.gitignore`

```
# Temporary workflow state - don't version
.bmad/workflow_state.json
```

---

## STEP 4: Add Columns to posts_content.csv

### 4.1 New Columns Required

```csv
# Add these 4 columns:
1. last_posted_date (DATE, format: YYYY-MM-DD)
2. variant_of (STRING, nullable, format: "post-id" or NULL)
3. content_type (ENUM, values: evergreen, topical, tutorial, demo, etc.)
4. repost_count (INT, default: 0)
```

### 4.2 Migration Script

Create file: `scripts/migrate_posts_content.py`

```python
import csv
from datetime import datetime

def add_posts_content_columns():
    """Add new columns to posts_content.csv"""

    input_file = 'data/posts_content.csv'
    output_file = input_file

    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)

        # Check what columns exist
        has_last_posted = 'last_posted_date' in fieldnames
        has_variant = 'variant_of' in fieldnames
        has_type = 'content_type' in fieldnames
        has_repost = 'repost_count' in fieldnames

        # Add missing columns
        if not has_last_posted:
            fieldnames.append('last_posted_date')
        if not has_variant:
            fieldnames.append('variant_of')
        if not has_type:
            fieldnames.append('content_type')
        if not has_repost:
            fieldnames.append('repost_count')

        # Read and augment data
        for row in reader:
            # Set defaults for new columns
            if not has_last_posted:
                # Use publish_date if available, else today
                row['last_posted_date'] = row.get('publish_date',
                                                   datetime.now().strftime('%Y-%m-%d'))
            if not has_variant:
                row['variant_of'] = None
            if not has_type:
                # Set to demo or evergreen based on content
                row['content_type'] = 'demo' if 'demo' in row.get('notes', '').lower() else 'evergreen'
            if not has_repost:
                row['repost_count'] = 0

            rows.append(row)

    # Write back
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Updated posts_content.csv")
    print(f"   Added columns: {[c for c in fieldnames if c not in reader.fieldnames]}")
    print(f"   Total rows: {len(rows)}")

if __name__ == '__main__':
    add_posts_content_columns()
```

### 4.3 Run Migration

```bash
cd _bmad/bmm/workflows/idea-to-post-pipeline
python ../../scripts/migrate_posts_content.py
```

### 4.4 Verify

```bash
# Check headers:
head -1 data/posts_content.csv | tr ',' '\n'
# Should see new columns at end

# Check data:
head -2 data/posts_content.csv | tail -1 | awk -F',' '{print NF " columns"}'
# Should show correct column count
```

---

## STEP 5: Create Validation Scripts

### 5.1 CSV Structure Validator

Create file: `scripts/validate_csv_structure.py`

```python
import csv
import json
import os

def validate_csv_headers(filename, required_headers, optional_headers=[]):
    """Validate CSV has required headers"""
    with open(filename) as f:
        reader = csv.DictReader(f)
        actual = set(reader.fieldnames)

    required = set(required_headers)
    optional = set(optional_headers)

    # Check required
    missing = required - actual
    if missing:
        print(f"❌ {filename} missing required headers: {missing}")
        return False

    print(f"✅ {filename} headers valid")
    return True

def validate_csv_data_types(filename, field_validators):
    """Validate CSV data types"""
    issues = []

    with open(filename) as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, 1):
            for field, validator in field_validators.items():
                try:
                    validator(row[field])
                except Exception as e:
                    issues.append(f"Row {idx}, field {field}: {e}")

    if issues:
        print(f"❌ {filename} data type issues:")
        for issue in issues[:5]:  # Show first 5
            print(f"   {issue}")
        return False

    print(f"✅ {filename} data types valid")
    return True

def validate_json_field(filename, field_name, row_indices=None):
    """Validate JSON field in CSV"""
    issues = []

    with open(filename) as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, 1):
            if row_indices and idx not in row_indices:
                continue

            value = row.get(field_name)
            if not value or value == 'NULL':
                continue  # Skip nulls

            try:
                json.loads(value)
            except json.JSONDecodeError as e:
                issues.append(f"Row {idx}: {e}")

    if issues:
        print(f"❌ {filename} {field_name} JSON issues:")
        for issue in issues[:3]:
            print(f"   {issue}")
        return False

    print(f"✅ {filename} {field_name} JSON valid")
    return True

# Run all validations
def run_all_validations():
    """Run complete validation suite"""
    all_valid = True

    # ideas_inbox.csv
    all_valid &= validate_csv_headers(
        'data/ideas_inbox.csv',
        required=['id', 'date_added', 'source', 'raw_idea', 'category', 'status', 'notes'],
        optional=['idea_metadata', 'duplicate_count', 'related_ideas', 'content_type']
    )

    # ideas_research.csv
    all_valid &= validate_csv_headers(
        'data/ideas_research.csv',
        required=['id', 'original_idea_id', 'research_date', 'best_angle_id'],
        optional=['pain_points_json', 'related_ideas']
    )
    all_valid &= validate_json_field('data/ideas_research.csv', 'pain_points_json')

    # posts_content.csv
    all_valid &= validate_csv_headers(
        'data/posts_content.csv',
        required=['id', 'research_id', 'angle_used', 'quality_score'],
        optional=['last_posted_date', 'variant_of', 'content_type', 'repost_count']
    )

    # user_preferences/offer_filter.csv
    if os.path.exists('user_preferences/offer_filter.csv'):
        all_valid &= validate_csv_headers(
            'user_preferences/offer_filter.csv',
            required=['offer_type', 'willing', 'notes']
        )

    # workflow_state.json
    if os.path.exists('.bmad/workflow_state.json'):
        all_valid &= validate_json_field('.bmad/workflow_state.json', '')

    if all_valid:
        print("\n✅ ALL VALIDATIONS PASSED!")
    else:
        print("\n❌ Some validations failed - see above")

    return all_valid

if __name__ == '__main__':
    run_all_validations()
```

### 5.2 Run Validation

```bash
cd _bmad/bmm/workflows/idea-to-post-pipeline
python ../../scripts/validate_csv_structure.py
```

**Expected Output:**
```
✅ data/ideas_inbox.csv headers valid
✅ data/ideas_research.csv headers valid
✅ data/ideas_research.csv pain_points_json JSON valid
✅ data/posts_content.csv headers valid
✅ user_preferences/offer_filter.csv headers valid

✅ ALL VALIDATIONS PASSED!
```

---

## STEP 6: Integration Testing

### 6.1 Test pain_points_json Population

Create file: `scripts/test_pain_generation.py`

```python
import json
import csv

def test_pain_points_generation():
    """Test that pain_points_json can be populated correctly"""

    test_data = {
        "angle_1": [
            "Медленная документация берёт 2-3 дня на большой объём",
            "Все процессы в голове у одного человека",
            "Нельзя масштабировать без найма новых специалистов",
            "Непроцессированная информация = нельзя продать бизнес"
        ],
        "angle_2": [
            "Качество документов зависит от того кто их написал",
            "Нет стандарта, каждый пишет по-своему",
            "Редактирование и проверка занимают много времени"
        ]
    }

    # Serialize to CSV format
    json_str = json.dumps(test_data, ensure_ascii=False)
    print(f"JSON serialized: {json_str[:100]}...")

    # Deserialize from CSV format
    loaded_data = json.loads(json_str)
    assert loaded_data == test_data
    print("✅ pain_points_json serialization/deserialization works")

    # Verify structure
    for angle_id, pains in loaded_data.items():
        assert isinstance(pains, list), f"{angle_id} must be list"
        assert 3 <= len(pains) <= 5, f"{angle_id} must have 3-5 pains"
        assert all(isinstance(p, str) for p in pains), f"{angle_id} elements must be strings"
    print("✅ pain_points_json structure validation works")

if __name__ == '__main__':
    test_pain_points_generation()
```

### 6.2 Test offer_filter.csv Loading

Create file: `scripts/test_offer_filter.py`

```python
import csv

def test_offer_filter_loading():
    """Test that offer_filter.csv can be loaded and used"""

    willing_types = []

    with open('user_preferences/offer_filter.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['willing'] == '1':
                willing_types.append(row['offer_type'])

    print(f"Willing offer types: {willing_types}")
    assert len(willing_types) > 0, "Must have at least one willing offer type"
    assert all(t in ['training', 'setup', 'templates', 'consulting', 'full_dev']
               for t in willing_types), "Invalid offer types"
    print("✅ offer_filter.csv loading works")

if __name__ == '__main__':
    test_offer_filter_loading()
```

### 6.3 Run All Tests

```bash
cd _bmad/bmm/workflows/idea-to-post-pipeline
python ../../scripts/test_pain_generation.py
python ../../scripts/test_offer_filter.py
python ../../scripts/validate_csv_structure.py
```

---

## CHECKLIST: Implementation Complete

### Phase 1: CSV Schema (4 hours)
- [ ] Add pain_points_json to ideas_research.csv
  - [ ] Update template files
  - [ ] Run migration script
  - [ ] Verify column added
  - [ ] Validate no data loss

- [ ] Create user_preferences directory
  - [ ] Create offer_filter.csv
  - [ ] Create .gitignore
  - [ ] Add to main .gitignore

- [ ] Add columns to posts_content.csv
  - [ ] last_posted_date
  - [ ] variant_of
  - [ ] content_type
  - [ ] repost_count
  - [ ] Run migration
  - [ ] Verify columns added

### Phase 2: JSON Infrastructure (1.5 hours)
- [ ] Create workflow_state.json schema
- [ ] Create validation script
- [ ] Add to .gitignore
- [ ] Document file lifecycle

### Phase 3: Validation (2 hours)
- [ ] Create CSV validator script
- [ ] Create JSON validator script
- [ ] Create integration tests
- [ ] Run all validators
- [ ] Fix any issues
- [ ] Verify all tests pass

---

## Success Criteria

✅ All CSV files have required columns
✅ All new columns have appropriate defaults
✅ pain_points_json structure is valid JSON
✅ offer_filter.csv loads correctly
✅ workflow_state.json schema is defined
✅ All validation scripts pass
✅ No data was lost in migrations
✅ Backward compatibility maintained
✅ All tests pass
✅ Files properly added to .gitignore

---

## Quick Reference Commands

```bash
# Add columns to ideas_research.csv
python scripts/migrate_csv_schema.py

# Add columns to posts_content.csv
python scripts/migrate_posts_content.py

# Create user preferences directory
mkdir -p user_preferences

# Run all validations
python scripts/validate_csv_structure.py
python scripts/test_pain_generation.py
python scripts/test_offer_filter.py

# Check .gitignore
cat .gitignore | grep -E "pain_points|workflow_state|offer_filter"
```

---

**Document Version:** 1.0
**Created:** 2026-01-30
**Status:** Ready for Implementation
**Next Step:** Execute Phase 1 (CSV Schema)
