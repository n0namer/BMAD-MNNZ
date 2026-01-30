# Data Validation Checklist for Idea-to-Post-Pipeline

**Purpose:** Quick reference guide for validating CSV data structure, JSON formats, and output consistency
**Last Updated:** 2026-01-30
**Status:** Ready for Implementation

---

## CSV HEADER VALIDATION

### ✅ ideas_inbox.csv
```
Current headers:
id,date_added,source,raw_idea,category,status,notes

To add:
□ idea_metadata (JSON, nullable) - for demo mode visual/tool context
□ duplicate_count (INT, default=0) - deduplication tracking
□ related_ideas (JSON array, nullable) - relationship links
□ content_type (ENUM, default="evergreen") - content classification

Validation:
□ All current data preserved
□ New columns have NULL/default values
□ No data loss during migration
□ Date format consistent (YYYY-MM-DD)
□ Status values valid: [active, pending, archived]
```

### ✅ ideas_research.csv
```
Current headers:
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance

To add:
□ pain_points_json (JSON object, nullable) - [CRITICAL] pain by angle
□ related_ideas (JSON array, nullable) - research relationships

CRITICAL: pain_points_json structure validation
  Format: {"angle_1": ["pain1", "pain2", ...], "angle_2": [...]}
  □ Valid JSON (must parse)
  □ Keys match research angles
  □ Values are arrays of strings
  □ Each angle has 3-5 pain points
  □ Pain points are business-focused (not technical)

Validation:
□ All angle_id references exist in angles_library.csv
□ avg_relevance in range 70-95
□ sources_count >= 3
□ research_date <= today
□ sub_angles_count <= length(angles_list)
```

### ✅ posts_content.csv
```
Current headers:
id,research_id,angle_used,publish_date,platform,post_title_short,
content_500_chars,content_250_chars,content_100_chars,quality_score,
ctr_potential,engagement_score,status,notes

To add:
□ last_posted_date (DATE, default=publish_date) - last publication
□ variant_of (STRING, nullable) - parent post reference
□ content_type (ENUM, default="evergreen") - content classification
□ repost_count (INT, default=0) - republication count

Validation:
□ All research_id references exist
□ All angle_used references exist in angles_library
□ content_*_chars fields within size limits:
  - content_100_chars: ≤100 chars
  - content_250_chars: ≤250 chars
  - content_500_chars: ≤500 chars
□ quality_score in range 45-94
□ ctr_potential in range 2.1-4.8
□ engagement_score in range 1.6-5.2
□ publish_date <= last_posted_date <= today
□ variant_of (if not null) references valid post id
□ status valid: [draft, needs_review, needs_rewrite, ready]
□ platform valid: [telegram, other platforms]
```

### ✅ angles_library.csv
```
Current headers:
id,angle_name,category,description,hook_type,psychology,ctr_potential,
difficulty,use_frequency,effectiveness_score,best_for

Enhancement (optional):
□ recommended_content_types (JSON array) - content types that work

Validation:
□ All angle ids unique
□ angle_name descriptive (20-50 chars)
□ category valid: [value, growth, tradeoff, psychology, credibility, engagement, emotional, trust, results, bold]
□ hook_type valid: [urgency, curiosity, pattern-interrupt, educational, social-proof, mystery, emotional, logical, results]
□ psychology matches hook_type (semantically)
□ ctr_potential in range 3.7-4.8
□ difficulty valid: [easy, medium, hard]
□ use_frequency valid: [low, medium, high]
□ effectiveness_score in range 80-95
□ best_for describes target audience
□ No duplicate angle_names
```

### ✅ metrics_tracking.csv
```
Current headers:
post_id,publish_date,day_number,views,clicks,ctr_percent,comments,
shares,saves,engagement_rate,sentiment,notes

To add (optional):
□ content_type_distribution (JSON) - {type: count}
□ duplicate_ideas_found (INT)
□ variant_posts_created (INT)
□ repost_frequency (DECIMAL)

Validation:
□ post_id exists in posts_content.csv
□ publish_date <= today
□ day_number > 0 and sequential per post
□ views >= 0
□ clicks >= 0 and <= views
□ ctr_percent = (clicks / views) * 100
□ comments >= 0
□ shares >= 0
□ saves >= 0
□ engagement_rate = (comments + shares + saves) / views * 100
□ sentiment valid: [positive, neutral, negative]
□ Time series data grouped by post_id
```

---

## JSON STRUCTURE VALIDATION

### pain_points_json (NEW - IN ideas_research.csv)

**Location:** ideas_research.csv column (when added)

**Schema:**
```json
{
  "angle_1": [
    "Pain description 1",
    "Pain description 2",
    "Pain description 3"
  ],
  "angle_2": [
    "Pain description 1",
    "Pain description 2"
  ]
}
```

**Validation Checklist:**
```
□ Valid JSON (no syntax errors)
□ Top-level object (not array)
□ All keys are angle identifiers (angle_1, angle_2, etc.)
□ All keys match angles from research
□ All values are arrays
□ All array elements are strings
□ No empty arrays
□ 3-5 pain points per angle minimum
□ No duplicate pain descriptions within same angle
□ Pain descriptions are:
  □ Business-focused (not technical jargon)
  □ Entrepreneur-oriented (not individual contributor)
  □ Specific and actionable (not vague)
  □ Under 100 characters each
  □ In same language as content (Russian in this case)

Example validation:
{
  "angle_1": [
    "Медленная документация берёт 2-3 дня на большой объём",  ✓ ≤100 chars
    "Все процессы в голове у одного человека",                ✓ ≤100 chars
    "Нельзя масштабировать без найма новых специалистов",     ✓ ≤100 chars
    "Непроцессированная информация = нельзя продать бизнес"   ✓ ≤100 chars
  ]
}
```

---

### related_ideas (NEW - IN ideas_inbox.csv, ideas_research.csv)

**Location:** ideas_inbox.csv and ideas_research.csv (when added)

**Schema:**
```json
null  // or
["idea-1", "idea-2", "idea-3"]
```

**Validation Checklist:**
```
□ Either null or valid JSON array
□ All array elements are valid idea IDs
□ All referenced ideas exist in ideas_inbox.csv
□ No self-references (idea cannot relate to itself)
□ No duplicates within same array
□ Maximum 5 related ideas per entry
□ Related ideas are truly related (semantic check)

Example valid values:
null
["i-001"]
["i-001", "i-002"]
["i-001", "i-002", "i-003"]
```

---

### offer_filter.csv Structure (NEW FILE)

**Location:** user_preferences/offer_filter.csv

**Schema:**
```csv
offer_type,willing,notes
training,1,"1=yes, 0=no"
setup,1,"1=yes, 0=no"
templates,1,"1=yes, 0=no"
consulting,0,"1=yes, 0=no"
full_dev,0,"1=yes, 0=no"
```

**Validation Checklist:**
```
□ Exactly 5 rows (one per offer type)
□ offer_type values: [training, setup, templates, consulting, full_dev]
□ All offer_types present
□ No duplicate offer_types
□ willing column: 0 or 1 (not null)
□ notes column populated (reason for inclusion/exclusion)
□ File format: UTF-8
□ Line endings: LF (not CRLF)

Example:
offer_type,willing,notes
training,1,"Want to offer 1-on-1 coaching"
setup,1,"Can design workflows for clients"
templates,1,"Have document templates ready"
consulting,0,"Too time-consuming at this stage"
full_dev,0,"Don't have capacity for full projects"
```

---

### workflow_state.json Structure (NEW FILE)

**Location:** .bmad/workflow_state.json (temporary, auto-created)

**Schema:**
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
      "title": "Workshop Title",
      "description": "Short description",
      "cta": "Call to action",
      "pain_solved": ["pain1", "pain2"],
      "effort_level": "medium",
      "estimated_price_range": "$500-1000"
    }
  ],
  "draft_variants": [
    {
      "variant_id": "draft-1",
      "title": "Post title",
      "hook": "Opening hook",
      "body": "Content...",
      "cta": "CTA...",
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

**Validation Checklist:**
```
Core fields:
□ session_id: valid UUID or timestamp-based
□ current_step: matches actual step (c-03b2, c-03c, etc.)
□ timestamp_created: ISO 8601 format
□ content_type: valid ["demo", "other"]
□ selected_idea_id: references existing idea
□ selected_angle: valid angle identifier

generated_offers array:
□ Each offer has id, type, title, description, cta
□ offer.type in willing offers (from offer_filter.csv)
□ offer.title: 20-80 chars
□ offer.description: 1-2 sentences
□ offer.cta: clear call-to-action (5-20 words)
□ offer.pain_solved: array of valid pain points from pain_points_json
□ offer.effort_level: [low, medium, high]
□ offer.estimated_price_range: valid format "$X-$Y"
□ All ids unique within array

draft_variants array:
□ Each variant has variant_id, title, hook, body, cta, selected
□ variant.title: 20-80 chars
□ variant.hook: 5-20 words
□ variant.body: ≤500 chars
□ variant.cta: 5-20 words
□ variant.selected: boolean (true or false)
□ Only one variant should have selected=true at a time
□ Variants embed offers naturally in body/cta

stepsCompleted object:
□ All values are boolean
□ Keys match actual steps
□ True for completed steps
□ False for incomplete/future steps
□ At least one step marked complete
```

---

## OUTPUT FORMAT VALIDATION

### Pain Points Display (From step c-02c)

**Format:**
```
ANGLE {number}: {Angle Name} {Emoji}
Боли, которые эта рутина решает:
├─ 🔴 Pain point 1
├─ 🔴 Pain point 2
├─ 🔴 Pain point 3
└─ 🔴 Pain point 4
```

**Validation:**
```
□ Emoji present (🔴 for pain points)
□ Tree structure correct (├─ for non-last, └─ for last)
□ 3-5 pain points per angle
□ Pain text under 100 chars
□ Language consistent (Russian)
□ No formatting issues (extra spaces, broken lines)
□ Proper indentation (2 spaces)
□ All angles covered
```

---

### Offer Display (From step c-03b2)

**Format:**
```
OFFER 1: {Title}
├─ Type: {type}
├─ Solves: {pain list}
├─ Effort: {level}
└─ CTA: {action}
```

**Validation:**
```
□ Title descriptive (20-80 chars)
□ Type valid: [training, setup, templates, consulting, full_dev]
□ Solves: all pains reference pain_points_json
□ Effort: [low, medium, high]
□ CTA: clear and actionable
□ 2-4 offers total
□ No duplicate offers
□ Proper formatting and structure
□ Tree structure correct
```

---

### Draft Variants Display (From step c-03c)

**Format:**
```
VARIANT {number}:
HOOK: {Hook text}
BODY: {Content}
CTA: {Call-to-action}
Embedded offers: [offers list]
```

**Validation:**
```
□ 3 variants generated
□ Hook: 5-20 words, engaging
□ Body: formatted correctly, ≤500 chars shown
□ CTA: clear, actionable, 5-20 words
□ Offers embedded naturally (not forced)
□ Variants differ meaningfully:
  □ Different hooks
  □ Different angles highlighted
  □ Different CTA focus
□ Layout consistent across variants
□ No overlapping/duplicate variants
```

---

## BACKWARD COMPATIBILITY CHECKLIST

```
CSV Migration:
□ All new columns optional (NULL/default values)
□ Existing data not modified
□ No column reordering
□ Read logic handles missing columns
□ Legacy CSVs work with new code

File Structure:
□ user_preferences/ directory creation doesn't break anything
□ .bmad/workflow_state.json auto-cleanup after step completion
□ No conflicts with existing .gitignore rules
□ Old workflows still run without new files

Data Integrity:
□ Test with original test data (5 ideas, 10 posts)
□ Verify all IDs still reference correctly
□ Check JSON parsing doesn't break CSV reads
□ Validate output format with old and new data
```

---

## COMMON VALIDATION ERRORS

### ❌ JSON Parsing Failures

**Issue:** `pain_points_json` with unescaped quotes
```
WRONG:  {"angle_1": ["Pain with "quotes" inside"]}
RIGHT:  {"angle_1": ["Pain with \"quotes\" inside"]}
```

**Fix:**
```
In CSV: escape internal quotes with \"
When loading: use json.loads() with proper handling
When saving: use json.dumps() for proper escaping
```

---

### ❌ NULL vs Empty String vs Empty Array

**Standard:**
```
No related ideas: NULL (not "" or "[]")
Empty variant: NULL (not "" or "null")
No pain points for angle: Not allowed (must have 3-5)
Default content type: "evergreen" (not NULL)
```

**Validation:**
```
□ Use NULL for missing optional data
□ Use "" only for deliberately empty strings
□ Never use "NULL" string (use actual null)
□ Never use empty JSON arrays [] for null values
```

---

### ❌ Date Format Inconsistency

**Issue:** Mixed date formats
```
WRONG:  2026-01-30, 01/30/2026, 30.01.2026 (mixed)
RIGHT:  2026-01-30 (consistent ISO 8601)
```

**Validation:**
```
□ All dates: YYYY-MM-DD
□ All timestamps: ISO 8601 (2026-01-30T15:32:45Z)
□ No timezone abbreviations (use Z for UTC)
□ Parse and re-format if inconsistent
```

---

### ❌ Numeric Type Errors

**Issue:** String numbers instead of numeric
```
WRONG:  "45" (string), "4.5" (for decimal)
RIGHT:  45 (integer), 4.5 (float)
```

**Validation:**
```
□ Parse numeric strings to actual numbers
□ Validate range (views >= 0, score 0-100, etc.)
□ Check precision (decimals where needed)
□ Round/truncate appropriately
```

---

## VALIDATION SCRIPT PSEUDO-CODE

```python
def validate_csv_structure():
    """Validate all CSV files have required headers and data types"""

    # Check each CSV
    files = {
        'ideas_inbox.csv': ['id', 'date_added', 'source', ...],
        'ideas_research.csv': ['id', 'original_idea_id', ...],
        'posts_content.csv': ['id', 'research_id', ...],
    }

    for filename, required_headers in files.items():
        df = read_csv(filename)

        # Check headers
        assert all(h in df.columns for h in required_headers), \
            f"Missing headers in {filename}"

        # Check new optional headers
        optional = ['pain_points_json', 'variant_of', 'content_type']
        for col in optional:
            if col in df.columns:
                if col == 'pain_points_json':
                    validate_pain_points_json(df[col])

def validate_pain_points_json(column):
    """Validate pain_points_json structure"""
    for idx, value in column.items():
        if value is None:  # Skip null values
            continue

        try:
            data = json.loads(value)
        except:
            raise ValueError(f"Invalid JSON at row {idx}: {value}")

        # Validate structure
        assert isinstance(data, dict), "Must be JSON object"

        for angle_id, pains in data.items():
            assert isinstance(pains, list), f"{angle_id} must be array"
            assert 3 <= len(pains) <= 5, f"{angle_id} needs 3-5 pains"
            assert all(isinstance(p, str) for p in pains), \
                f"{angle_id} values must be strings"

def validate_offer_filter():
    """Validate user_preferences/offer_filter.csv structure"""
    df = read_csv('user_preferences/offer_filter.csv')

    assert len(df) == 5, "Must have exactly 5 offer types"
    assert df['willing'].isin([0, 1]).all(), "willing must be 0 or 1"
    assert set(df['offer_type']) == \
        {'training', 'setup', 'templates', 'consulting', 'full_dev'}, \
        "Missing or extra offer types"

def validate_workflow_state():
    """Validate workflow_state.json structure"""
    with open('.bmad/workflow_state.json') as f:
        state = json.load(f)

    # Check required fields
    required = ['session_id', 'current_step', 'generated_offers',
                'stepsCompleted']
    assert all(k in state for k in required), "Missing required fields"

    # Validate offers
    for offer in state['generated_offers']:
        assert offer['type'] in ['training', 'setup', 'templates', ...], \
            "Invalid offer type"
        assert isinstance(offer['pain_solved'], list), \
            "pain_solved must be array"

# Run all validations
validate_csv_structure()
validate_offer_filter()
validate_workflow_state()
print("✅ All validations passed!")
```

---

## QUICK REFERENCE TABLE

| File | Status | Critical Fields | New Columns | Priority |
|------|--------|---|---|---|
| ideas_inbox.csv | ✅ Current | id, status | idea_metadata, duplicate_count | High |
| ideas_research.csv | ✅ Current | id, best_angle_id | **pain_points_json**, related_ideas | CRITICAL |
| posts_content.csv | ✅ Current | id, quality_score | content_type, variant_of | High |
| angles_library.csv | ✅ Current | id, effectiveness_score | recommended_content_types | Low |
| metrics_tracking.csv | ✅ Current | post_id, ctr_percent | type_distribution | Low |
| offer_filter.csv | ❌ NEW | offer_type, willing | - | CRITICAL |
| workflow_state.json | ❌ NEW | generated_offers | - | CRITICAL |

---

**Last Updated:** 2026-01-30
**Validation Status:** Ready for Implementation
**Next Step:** Execute CSV migrations and create new files
