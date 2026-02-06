# CSV Schema Specifications & Implementation Guide

## Overview
This document specifies the schema, parsing logic, and usage patterns for the new CSV columns and offer_filter configuration.

---

## 1. idea_metadata Column (ideas_inbox.csv)

### Schema Definition
```json
{
  "type": "object",
  "optional": true,
  "nullable": true,
  "properties": {
    "visual_context": {
      "type": "string",
      "description": "Visual or contextual reference for the idea",
      "examples": [
        "Screenshot from case study",
        "Screenshot from LinkedIn post",
        "Photo of whiteboard sketch"
      ]
    },
    "tools_used": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Tools or platforms mentioned in the idea",
      "examples": [
        ["ChatGPT", "Midjourney"],
        ["Figma", "Slack"],
        ["Linear", "GitHub"]
      ]
    },
    "demonstrated_result": {
      "type": "string",
      "description": "Specific result or outcome demonstrated by the idea",
      "examples": [
        "Generated 500 words in 3 minutes",
        "Increased conversion rate by 23%",
        "Saved 5 hours per week"
      ]
    }
  }
}
```

### CSV Format
```csv
id,date_added,source,raw_idea,category,status,notes,idea_metadata
1,2026-01-27,brainstorm,"ИИ контент за 3 часа",automation,active,"Интересная идея",
2,2026-01-27,screenshot,"Tool demo",tech,active,"Скриншот с LinkedIn","{""visual_context"":""LinkedIn post 2026-01-27"",""tools_used"":[""Claude"",""Figma""],""demonstrated_result"":""Generated in 3 hours""}"
```

### Parsing Logic
```python
import json
from typing import Optional, Dict, List, Any

def parse_idea_metadata(raw_metadata: str) -> Optional[Dict[str, Any]]:
    """
    Parse idea_metadata JSON column from CSV.

    Args:
        raw_metadata: Raw string from CSV (may be empty, NULL, or JSON)

    Returns:
        Parsed dict or None if empty/invalid
    """
    if not raw_metadata or raw_metadata.upper() == "NULL":
        return None

    try:
        return json.loads(raw_metadata)
    except json.JSONDecodeError:
        return None

def validate_idea_metadata(metadata: Dict[str, Any]) -> bool:
    """
    Validate idea_metadata structure.

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(metadata, dict):
        return False

    # All fields optional, but if present must be correct type
    if "visual_context" in metadata and not isinstance(metadata["visual_context"], str):
        return False
    if "tools_used" in metadata and not isinstance(metadata["tools_used"], list):
        return False
    if "demonstrated_result" in metadata and not isinstance(metadata["demonstrated_result"], str):
        return False

    return True
```

### Usage in [R]outine Mode
When processing ideas for content generation:
```python
# Load idea with metadata
idea = load_idea_from_csv(idea_id)
metadata = parse_idea_metadata(idea['idea_metadata'])

if metadata:
    # Use visual context to enhance research
    if metadata.get('visual_context'):
        sources.append({
            'type': 'visual',
            'context': metadata['visual_context']
        })

    # Map tools to relevant angles
    tools_used = set(metadata.get('tools_used', []))
    relevant_angles = angles.filter_by_tools(tools_used)

    # Use demonstrated result as social proof
    if metadata.get('demonstrated_result'):
        proof_points.append(metadata['demonstrated_result'])
```

---

## 2. pain_points_json Column (ideas_research.csv)

### Schema Definition
```json
{
  "type": "object",
  "optional": true,
  "nullable": true,
  "description": "Pain points mapped to each angle",
  "additionalProperties": {
    "type": "object",
    "properties": {
      "pains": {
        "type": "array",
        "items": {"type": "string"},
        "description": "List of pain points relevant to this angle"
      },
      "impact": {
        "type": "string",
        "enum": ["high", "medium", "low"],
        "description": "Impact level of these pain points"
      }
    }
  }
}
```

### CSV Format
```csv
id,original_idea_id,research_date,main_angle,sub_angles_count,best_angle_id,angles_list,sources_count,avg_relevance,pain_points_json
1,1,2026-01-27,"ИИ экономит время",8,"angle_1","Экономия времени|Масштабирование|...",7,84,
2,2,2026-01-27,"Speech-to-text workflow",7,"angle_2","Скорость записи|Точность|...",6,79,"{""angle_2"":{""pains"":[""Time spent recording"",""Transcription errors""],""impact"":""high""},""angle_3"":{""pains"":[""Integration complexity""],""impact"":""medium""}}"
```

### Parsing Logic
```python
def parse_pain_points(raw_json: str) -> Optional[Dict[str, Dict[str, Any]]]:
    """
    Parse pain_points_json column.

    Args:
        raw_json: Raw string from CSV

    Returns:
        Dict mapping angle_id to pain_points object, or None
    """
    if not raw_json or raw_json.upper() == "NULL":
        return None

    try:
        pain_data = json.loads(raw_json)
        # Validate structure
        for angle_id, angle_pains in pain_data.items():
            if not isinstance(angle_pains, dict) or "pains" not in angle_pains:
                return None
            if not isinstance(angle_pains["pains"], list):
                return None
        return pain_data
    except (json.JSONDecodeError, TypeError):
        return None

def extract_pains_for_angle(pain_points: Dict, angle_id: str) -> List[str]:
    """
    Extract pain points for specific angle.

    Returns:
        List of pain points, empty list if angle not found
    """
    if not pain_points or angle_id not in pain_points:
        return []

    angle_data = pain_points[angle_id]
    return angle_data.get("pains", [])
```

### Usage in Content Generation
When generating posts from research:
```python
# Load research with pain points
research = load_research_from_csv(research_id)
pain_points = parse_pain_points(research['pain_points_json'])

# Select angle for post
selected_angle = research['best_angle_id']

# Get pain points for this angle
relevant_pains = extract_pains_for_angle(pain_points, selected_angle)

# Use pains in post copy
if relevant_pains:
    copy_hooks = [
        f"Tired of {pain}?" for pain in relevant_pains
    ]

    # Map pains to emotional triggers
    emotional_angles = copy_framework.map_pains_to_emotions(relevant_pains)
```

---

## 3. offer_filter.csv (USER PREFERENCES)

### Schema Definition
```csv
offer_type,willing,notes
```

| Column | Type | Description |
|--------|------|-------------|
| `offer_type` | string | Type of service/product offering (training, setup, templates, consulting, full_dev) |
| `willing` | boolean | User's willingness (true/false) to offer this type |
| `notes` | string | Optional notes explaining the preference |

### Offer Types Reference
```
training    - Training materials, courses, workshops
setup       - Setup services, configuration, deployment help
templates   - Template packages, reusable code/configs
consulting  - Consulting/advisory services, coaching
full_dev    - Full development services, custom builds
```

### CSV Format
```csv
offer_type,willing,notes
training,true,Training materials accepted
setup,true,Setup services accepted
templates,true,Template packages accepted
consulting,false,Consulting not offered
full_dev,false,Full development not offered
```

### Parsing Logic
```python
def load_offer_filter(filepath: str) -> Dict[str, bool]:
    """
    Load offer filter preferences.

    Returns:
        Dict mapping offer_type to boolean willingness
    """
    preferences = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            offer_type = row['offer_type'].strip()
            willing = row['willing'].lower() == 'true'
            preferences[offer_type] = willing

    return preferences

def is_offer_acceptable(preferences: Dict[str, bool], offer_type: str) -> bool:
    """
    Check if offer type is acceptable based on user preferences.

    Returns:
        True if acceptable, False if not
    """
    return preferences.get(offer_type.lower(), False)
```

### Usage in Recommendation Filtering
```python
# Load user preferences
offer_prefs = load_offer_filter('data/user_preferences/offer_filter.csv')

# Filter recommendations by acceptable offers
def filter_recommendations(recommendations):
    filtered = []
    for rec in recommendations:
        offer_type = rec.get('offer_type')
        if is_offer_acceptable(offer_prefs, offer_type):
            filtered.append(rec)
    return filtered

# Example usage in Mode R (Routine)
routine_recommendations = filter_recommendations(all_recommendations)
# Only recommendations with willing=true will be included
```

---

## Data Integration Points

### Workflow Integration
1. **Mode C (Create):**
   - Step C-01: When adding idea, capture idea_metadata
   - Step C-02: When researching, populate pain_points_json
   - Step C-03: When filtering recommendations, check offer_filter.csv

2. **Mode R (Routine):**
   - Automatically uses idea_metadata for visual context
   - Filters angles by pain_points relevance
   - Only suggests offers where willing=true

3. **Mode E (Edit):**
   - Can update pain_points_json based on new research
   - Can add idea_metadata to previously created ideas

### Database Considerations
- All new columns are optional (NULL-able)
- JSON columns should be indexed for performance
- Offer filter is read-only (user preferences)

---

## Migration Strategy

### For Existing Data
1. **No migration required** - all new columns are optional
2. **Backward compatible** - existing parsers work unchanged
3. **Gradual population** - fill columns as data becomes available
4. **No data loss** - NULL values preserve original functionality

### Testing Checklist
```
[ ] CSV files parse correctly with Python csv module
[ ] JSON columns parse when present
[ ] NULL/empty values handled gracefully
[ ] offer_filter.csv loaded correctly
[ ] Filtering logic works for recommendations
[ ] Pain point mapping works for all angles
[ ] idea_metadata optional for all ideas
[ ] No errors with existing blank columns
[ ] Performance acceptable with large datasets
[ ] UTF-8 encoding preserved (Cyrillic text)
```

---

## Examples

### Example 1: Complete Idea with Metadata
```csv
1,2026-01-27,brainstorm,"ИИ контент за 3 часа",automation,active,"Интересная идея","{""visual_context"":""ChatGPT screenshot"",""tools_used"":[""ChatGPT"",""Notion""],""demonstrated_result"":""3 hours vs 8 hours""}"
```

### Example 2: Research with Pain Points
```csv
1,1,2026-01-27,"ИИ экономит время",8,"angle_1","Экономия времени|Масштабирование|...",7,84,"{""angle_1"":{""pains"":[""Time pressure"",""Deadline stress""],""impact"":""high""}}"
```

### Example 3: Offer Filter (Complete File)
```csv
offer_type,willing,notes
training,true,Training materials accepted
setup,true,Setup services accepted
templates,true,Template packages accepted
consulting,false,Consulting not offered
full_dev,false,Full development not offered
```

---

## Error Handling

```python
def safe_parse_idea_metadata(raw_metadata: str) -> Optional[Dict]:
    """Parse with comprehensive error handling."""
    if not raw_metadata:
        return None

    try:
        data = json.loads(raw_metadata)
        if validate_idea_metadata(data):
            return data
        else:
            logger.warning(f"Invalid metadata structure: {raw_metadata}")
            return None
    except json.JSONDecodeError as e:
        logger.warning(f"Failed to parse metadata JSON: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error parsing metadata: {e}")
        return None
```

---

## Performance Optimization

1. **Index JSON columns** in database for faster queries
2. **Cache offer_filter.csv** in memory (small file, read-only)
3. **Lazy load** idea_metadata and pain_points (optional fields)
4. **Batch validation** when processing multiple rows

---

## Version History
- **2026-01-30:** Initial schema specification and implementation
- **Status:** Ready for production implementation
