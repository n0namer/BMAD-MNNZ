# CSV Schema Updates for Diversity & Deduplication

## Overview

This document describes schema updates needed for the idea-to-post pipeline to support:
- Content diversity tracking and repost management
- Duplicate idea detection and consolidation
- Content type classification and filtering
- Relationship mapping between similar ideas

---

## 1. posts_content.csv - Schema Updates

### New Columns

| Column | Type | Format | Nullable | Default | Description |
|--------|------|--------|----------|---------|-------------|
| `last_posted_date` | DATE | ISO 8601 (YYYY-MM-DD) | No | CURRENT_DATE | When this post was last published to social media |
| `variant_of` | STRING | UUID/ID format | Yes | NULL | Post ID if this is a variant or repost of another post |
| `content_type` | ENUM | See values below | No | evergreen | Classification of content type for filtering and selection |
| `repost_count` | INT | Non-negative integer | No | 0 | Number of times this post has been reposted or republished |

### Content Type Enumeration

```csv
evergreen         # Timeless content, no date dependency
topical          # Time-sensitive, references current events
seasonal         # Calendar-based, holidays/seasons
philosophical    # Opinion/perspective pieces
tutorial         # Step-by-step how-to content
demo            # Live examples, showcases
case_study      # Real-world examples with results
listicle        # Numbered/bulleted list content
```

### Migration Path

**Step 1: Add columns to existing CSV**
```bash
# Before (example row):
id,title,content,angles_used,posted_count,created_date
001,Title Here,Content here,"angle1,angle2",2,2024-01-15

# After (example row):
id,title,content,angles_used,posted_count,created_date,last_posted_date,variant_of,content_type,repost_count
001,Title Here,Content here,"angle1,angle2",2,2024-01-15,2024-01-20,NULL,evergreen,2
```

**Step 2: Set default values**
- `last_posted_date`: Use `posted_date` if available, else current date
- `variant_of`: NULL (no variants in existing data)
- `content_type`: Set to `evergreen` for all existing posts
- `repost_count`: Use existing `posted_count` value

**Step 3: Update tracking**
- Set `last_posted_date` = last date from posting history if available
- Calculate `repost_count` from posting history metrics

### Example Updated Row

```csv
id,title,content,angles_used,posted_count,created_date,last_posted_date,variant_of,content_type,repost_count
p-001,"10 Ways to Optimize Python Performance","Content about Python optimization...","Performance,Optimization",5,2024-01-10,2024-02-20,NULL,tutorial,5
p-002,"Why Python Matters in 2024","Opinion piece about Python adoption...","Opinion,Trends",3,2024-01-15,2024-02-15,p-001,topical,3
```

---

## 2. ideas_inbox.csv - Schema Updates

### New Columns

| Column | Type | Format | Nullable | Default | Description |
|--------|------|--------|----------|---------|-------------|
| `duplicate_count` | INT | Non-negative integer | No | 0 | Number of times this idea (or similar) was submitted |
| `related_ideas` | JSON ARRAY | Valid JSON array of IDs | Yes | NULL | Array of idea IDs that explore the same topic from different angles |
| `content_type` | ENUM | See values below | No | evergreen | Suggested content type for posts derived from this idea |

### Content Type Enumeration

Same as posts_content.csv (see above)

### Related Ideas Format

```json
// Example: Single related idea
"related_ideas": ["idea-123"]

// Example: Multiple related ideas
"related_ideas": ["idea-123", "idea-456", "idea-789"]

// Example: Empty (no related ideas)
"related_ideas": null
```

### Duplicate Detection Logic

Duplicate detection should be triggered during **idea submission** (step C-01) and **idea selection** (step C-02a):

```
IF new_idea submitted THEN
  1. Search existing ideas for duplicate title/content match
  2. IF match found (>85% similarity) THEN
     - Increment `duplicate_count` on existing idea
     - Show user: "Similar idea exists (submitted X times)"
     - Offer: "Add your angle to existing?" or "Submit as new angle?"
  3. IF user confirms duplicate THEN
     - Link as related idea
     - DO NOT create new inbox entry
  4. ELSE (new angle) THEN
     - Create new inbox entry
     - Set `related_ideas` = [ID of similar idea]
     - Increment `duplicate_count` on original
END
```

### Migration Path

**Step 1: Add columns**
```bash
# Before:
id,title,description,source,date_added,status
i-001,Idea Title,Description...,User,2024-01-10,inbox

# After:
id,title,description,source,date_added,status,duplicate_count,related_ideas,content_type
i-001,Idea Title,Description...,User,2024-01-10,inbox,0,NULL,evergreen
```

**Step 2: Set default values**
- `duplicate_count`: 0 (no duplicates in existing data)
- `related_ideas`: NULL (will be populated during research/selection)
- `content_type`: evergreen (default assumption)

**Step 3: Analyze for relationships**
- Run similarity analysis on existing ideas
- If similar ideas found (>80% title similarity):
  - Link them via `related_ideas`
  - Set `duplicate_count` = number of submissions with that theme

### Example Updated Rows

```csv
id,title,description,source,date_added,status,duplicate_count,related_ideas,content_type
i-001,"Python Performance Tips","How to optimize Python code...","User1",2024-01-10,inbox,0,NULL,tutorial
i-002,"Python Optimization Techniques","Different ways to speed up Python...","User2",2024-01-12,inbox,1,"[""i-001""]",tutorial
i-003,"Timeless Python Patterns","Design patterns in Python...","User3",2024-01-15,inbox,0,"[""i-001"",""i-002""]",philosophical
i-004,"Python Performance (duplicate)","Same as i-001 but worded differently","User1",2024-01-18,inbox,2,"[""i-001""]",tutorial
```

---

## 3. ideas_research.csv - Schema Updates

### New Columns

| Column | Type | Format | Nullable | Default | Description |
|--------|------|--------|----------|---------|-------------|
| `related_ideas` | JSON ARRAY | Valid JSON array of IDs | Yes | NULL | Links to related ideas from inbox that inform this research |

### Related Ideas Format

```json
// Research informed by one idea
"related_ideas": ["i-001"]

// Research that synthesizes multiple ideas
"related_ideas": ["i-001", "i-002", "i-003"]

// No specific linked ideas
"related_ideas": null
```

### Migration Path

**Step 1: Add column**
```bash
# Before:
id,idea_id,research_content,sources,date_researched,quality_score
r-001,i-001,"Research findings...","Source1, Source2",2024-01-10,85

# After:
id,idea_id,research_content,sources,date_researched,quality_score,related_ideas
r-001,i-001,"Research findings...","Source1, Source2",2024-01-10,85,NULL
```

**Step 2: Link to inbox**
- `related_ideas`: Manually map research to source ideas (automated during step C-02c)

### Example Updated Row

```csv
id,idea_id,research_content,sources,date_researched,quality_score,related_ideas
r-001,i-001,"Comprehensive research on Python performance optimization techniques...","PythonDocs, RealPython, StackOverflow",2024-01-10,85,"[""i-001"",""i-002"",""i-003""]"
```

---

## 4. angles_library.csv - Schema Enhancements

### No New Columns, But Enhanced Usage

The existing `angles_library.csv` should be cross-referenced with the new `content_type` field:

**Enhancement:** Add a `recommended_content_types` column to angles

| Column | Type | Description |
|--------|------|-------------|
| `recommended_content_types` | JSON ARRAY | Content types that work well with this angle |

Example:
```csv
angle_id,angle_name,description,usage_count,recommended_content_types
a-001,Performance,"Focus on speed and efficiency...",15,"[""tutorial"",""demo"",""case_study""]"
a-002,Opinion,"Share perspective on trends...",22,"[""philosophical"",""topical""]"
```

---

## 5. metrics_tracking.csv - New Metrics

### Add Diversity Tracking Columns

| Column | Type | Description |
|--------|------|-------------|
| `content_type_distribution` | JSON OBJECT | Count of posts by content type |
| `duplicate_ideas_found` | INT | Number of duplicate ideas detected this period |
| `variant_posts_created` | INT | Number of post variants created |
| `repost_frequency` | DECIMAL | Average reposts per post (content_reuse_rate) |

### Example Metrics Row

```csv
date,total_ideas,total_posts,avg_research_time,content_type_distribution,duplicate_ideas_found,variant_posts_created,repost_frequency
2024-01-20,42,18,"{""evergreen"":8,""topical"":4,""tutorial"":3,""philosophical"":2,""demo"":1}",3,5,2.4
```

---

## 6. Data Validation Rules

### posts_content.csv Validation

```
Rule 1: last_posted_date must be <= current date
Rule 2: variant_of (if not NULL) must reference existing post ID
Rule 3: content_type must be in approved enumeration
Rule 4: repost_count must be >= 0
Rule 5: If variant_of is set, repost_count should typically match or exceed original
```

### ideas_inbox.csv Validation

```
Rule 1: duplicate_count must be >= 0
Rule 2: related_ideas (if not NULL) must be valid JSON array
Rule 3: All IDs in related_ideas must reference existing ideas
Rule 4: An idea cannot be related to itself
Rule 5: If duplicate_count > 0, related_ideas should be populated
Rule 6: content_type must be in approved enumeration
```

### ideas_research.csv Validation

```
Rule 1: related_ideas (if not NULL) must be valid JSON array
Rule 2: All IDs in related_ideas must reference ideas from ideas_inbox.csv
Rule 3: related_ideas should match idea_id and any variations
```

---

## 7. Migration Script Pseudocode

```python
def migrate_csv_schema():
    """
    Complete migration of CSV schema to include new columns.
    """

    # Step 1: Migrate posts_content.csv
    posts = read_csv('posts_content.csv')
    posts['last_posted_date'] = posts.get('posted_date', today())
    posts['variant_of'] = None
    posts['content_type'] = 'evergreen'  # Default for all
    posts['repost_count'] = posts.get('posted_count', 0)
    write_csv('posts_content.csv', posts)

    # Step 2: Migrate ideas_inbox.csv
    ideas = read_csv('ideas_inbox.csv')
    ideas['duplicate_count'] = 0
    ideas['related_ideas'] = None
    ideas['content_type'] = 'evergreen'  # Default for all

    # Detect duplicates
    for idx, idea in ideas.iterrows():
        similar = find_similar_ideas(idea['title'], ideas, threshold=0.85)
        if similar:
            ideas.loc[idx, 'duplicate_count'] = len(similar)
            ideas.loc[idx, 'related_ideas'] = json.dumps(similar)

    write_csv('ideas_inbox.csv', ideas)

    # Step 3: Migrate ideas_research.csv
    research = read_csv('ideas_research.csv')
    research['related_ideas'] = research['idea_id'].apply(
        lambda x: json.dumps([x])  # Link each research to its source idea
    )
    write_csv('ideas_research.csv', research)

    # Step 4: Enhance angles_library.csv
    angles = read_csv('angles_library.csv')
    angles['recommended_content_types'] = angles['angle_name'].apply(
        get_recommended_types
    )
    write_csv('angles_library.csv', angles)

    # Step 5: Initialize metrics_tracking.csv row
    new_metrics = {
        'date': today(),
        'total_ideas': len(ideas),
        'total_posts': len(posts),
        'avg_research_time': calculate_avg_research_time(),
        'content_type_distribution': count_by_type(posts),
        'duplicate_ideas_found': sum(ideas['duplicate_count'] > 0),
        'variant_posts_created': sum(posts['variant_of'].notna()),
        'repost_frequency': posts['repost_count'].mean()
    }
    append_csv('metrics_tracking.csv', new_metrics)

def find_similar_ideas(title, ideas_df, threshold=0.85):
    """Find ideas with similar titles using string similarity."""
    similar = []
    for idx, other in ideas_df.iterrows():
        similarity = string_similarity(title, other['title'])
        if similarity >= threshold and other['id'] != title:
            similar.append(other['id'])
    return similar

def get_recommended_types(angle_name):
    """Map angle name to recommended content types."""
    mapping = {
        'Performance': ['tutorial', 'demo', 'case_study'],
        'Opinion': ['philosophical', 'topical'],
        'Educational': ['tutorial', 'demo', 'listicle'],
        'News': ['topical', 'news'],
        'Showcase': ['demo', 'case_study'],
    }
    return mapping.get(angle_name, ['evergreen'])
```

---

## 8. Workflow Integration Points

### Where New Fields Are Populated

**Step C-01 (Add Idea):**
- Check `ideas_inbox.csv` for duplicates
- Populate `duplicate_count` if match found
- Set `related_ideas` array

**Step C-02b (Select Idea):**
- Display `duplicate_count` to user
- Show `related_ideas` for context
- Suggest content type based on theme

**Step C-02c (Research):**
- Populate research's `related_ideas`
- Link to source ideas

**Step C-03c (Draft):**
- Assign `content_type` to new post
- Default based on idea's suggested type

**Step C-03d (Variants):**
- Create post with `variant_of` = original post ID
- Increment `repost_count` on original

**Step C-04 (Search & Analytics):**
- Use `content_type_distribution` for diversity metrics
- Use `repost_frequency` for content reuse analysis
- Use `duplicate_count` for suggestion quality

**Step C-06 (Merge):**
- Use `related_ideas` to find posts to merge
- Update `variant_of` if merging variants

**Step C-07 (Analytics Dashboard):**
- Display diversity breakdown by `content_type`
- Show repost/variant analytics
- Show duplicate detection effectiveness

---

## 9. Backward Compatibility

### Handling Legacy Data

All new columns are optional (nullable or have defaults):
- Existing CSV files will continue to work
- New code will populate defaults
- Migration can happen gradually per workflow execution

### Read Legacy Format

```python
def read_csv_safe(filepath):
    """Read CSV and add missing columns with defaults."""
    df = pd.read_csv(filepath)

    # posts_content.csv defaults
    if 'last_posted_date' not in df.columns:
        df['last_posted_date'] = df.get('posted_date', today())
    if 'variant_of' not in df.columns:
        df['variant_of'] = None
    if 'content_type' not in df.columns:
        df['content_type'] = 'evergreen'
    if 'repost_count' not in df.columns:
        df['repost_count'] = df.get('posted_count', 0)

    # ideas_inbox.csv defaults
    if 'duplicate_count' not in df.columns:
        df['duplicate_count'] = 0
    if 'related_ideas' not in df.columns:
        df['related_ideas'] = None

    return df
```

---

## 10. Testing Strategy

### Unit Tests

```python
def test_schema_migration():
    """Test CSV schema migration."""

    # Load original CSV
    original = read_csv('posts_content.csv')
    original_rows = len(original)

    # Run migration
    migrate_csv_schema()

    # Verify migration
    migrated = read_csv('posts_content.csv')

    assert len(migrated) == original_rows, "Row count must match"
    assert 'last_posted_date' in migrated.columns
    assert 'variant_of' in migrated.columns
    assert 'content_type' in migrated.columns
    assert 'repost_count' in migrated.columns
    assert migrated['content_type'].notna().all(), "No NULL content types"
    assert migrated['repost_count'].ge(0).all(), "Repost count >= 0"

def test_duplicate_detection():
    """Test duplicate idea detection."""
    ideas = read_csv('ideas_inbox.csv')

    # Verify no idea is related to itself
    for idx, idea in ideas.iterrows():
        if idea['related_ideas']:
            related = json.loads(idea['related_ideas'])
            assert idea['id'] not in related, "Idea cannot relate to itself"

def test_variant_tracking():
    """Test post variant tracking."""
    posts = read_csv('posts_content.csv')

    # Verify all variant_of references exist
    for idx, post in posts.iterrows():
        if post['variant_of']:
            assert post['variant_of'] in posts['id'].values, \
                f"Variant reference {post['variant_of']} not found"
```

---

## 11. Rollout Plan

### Phase 1: Schema Extension (Week 1)
- [ ] Add columns to CSV files with defaults
- [ ] Update read/write functions
- [ ] Deploy to test environment

### Phase 2: Migration (Week 2)
- [ ] Run migration script on all CSV files
- [ ] Validate data integrity
- [ ] Test backward compatibility

### Phase 3: Workflow Integration (Week 3)
- [ ] Update steps C-01, C-02, C-03, C-04 to use new fields
- [ ] Implement duplicate detection
- [ ] Implement variant tracking

### Phase 4: Analytics (Week 4)
- [ ] Update dashboard to display new metrics
- [ ] Add diversity reports
- [ ] Track effectiveness of deduplication

---

## 12. Troubleshooting

### Issue: JSON parsing errors in related_ideas

**Solution:** Ensure JSON is properly escaped in CSV:
```csv
# Wrong:
related_ideas: ["id-1", "id-2"]

# Correct:
related_ideas: "[""id-1"",""id-2""]"
```

### Issue: NULL vs empty string vs empty JSON array

**Standard:**
- No related ideas: `NULL` (not `""` or `[]`)
- Empty variant: `NULL` (not `""`)
- Default content type: `evergreen` (not `NULL`)

### Issue: Duplicate detection false positives

**Tuning:**
- Adjust similarity threshold (default: 0.85)
- Exclude common words from comparison
- Use semantic similarity for better accuracy

---

## 13. Configuration Reference

### Content Type Weights (for selection algorithm)

```json
{
  "evergreen": {"weight": 1.0, "reuse_friendly": true},
  "topical": {"weight": 0.8, "reuse_friendly": false},
  "seasonal": {"weight": 0.6, "reuse_friendly": true},
  "philosophical": {"weight": 1.0, "reuse_friendly": true},
  "tutorial": {"weight": 0.9, "reuse_friendly": true},
  "demo": {"weight": 0.7, "reuse_friendly": false},
  "case_study": {"weight": 0.9, "reuse_friendly": true},
  "listicle": {"weight": 0.8, "reuse_friendly": true}
}
```

### Duplicate Detection Thresholds

```json
{
  "title_similarity": 0.85,
  "content_similarity": 0.75,
  "keyword_match": 0.90,
  "action_threshold": 0.80
}
```

---

## 14. Document History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2024-01-30 | Initial schema design | Claude Code |
| - | - | - | - |

---

## 15. Related Documentation

- `CONVERSION-SUMMARY.md` - How old workflow maps to new schema
- `workflow.md` - Updated workflow steps using new fields
- `validation-guide.md` - Data validation rules and tests
- Steps: `step-c-01-add-idea.md`, `step-c-02b-select-idea.md`, etc.

---

**Status:** Ready for Phase 1 implementation

**Next Steps:**
1. Review schema with team
2. Validate backward compatibility
3. Create migration script
4. Test on staging environment
