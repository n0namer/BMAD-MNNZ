# Dimensional Report Sections Template

## DIMENSIONAL BREAKDOWN SECTIONS

Used by validation report steps (V-01 through V-07) to display detailed analysis.

### Section Format

Each dimensional section follows this format:

```
{DIMENSION_ID}: {DIMENSION_NAME} ({items_count} {item_type})
  Score: {score}% | Average: {average}/5 {status_indicator}
  Pass rate: {pass_rate}% of items meet standards
  Issues: {issue_count} items with gaps ({issue_percent}%)
  Critical: {critical_count} items failing checks ({critical_percent}%)
  Recommendation: {recommendation_text}
```

### Status Indicators

- ✅ = Excellent/Good (score >= 80%)
- ⚠️ = Acceptable but needs work (60-79%)
- 🔴 = Critical (< 60%)

### Data Template

```json
{
  "dimension": "{DIMENSION_ID}",
  "name": "{DIMENSION_NAME}",
  "items_count": 156,
  "items_type": "posts",
  "score": 81,
  "average": 4.77,
  "unit": "/5",
  "status_indicator": "✅",
  "pass_rate": 82,
  "issue_count": 28,
  "issue_percent": 18,
  "critical_count": 8,
  "critical_percent": 5,
  "recommendation": "Focus on hook strength and CTA clarity",
  "details": {
    "strong_areas": ["metric_1", "metric_2"],
    "weak_areas": ["metric_1", "metric_2"],
    "action_items": ["action_1", "action_2"]
  }
}
```

### Standard Dimensions

#### V-01: QUALITY CHECKLIST
```json
{
  "dimension": "V-01",
  "name": "QUALITY CHECKLIST",
  "items_type": "posts"
}
```
Measures: Hook strength, CTA clarity, structure, readability

#### V-02: PERFORMANCE AUDIT
```json
{
  "dimension": "V-02",
  "name": "PERFORMANCE AUDIT",
  "items_type": "published posts"
}
```
Measures: Click rate, engagement rate, share rate, conversion metrics

#### V-03: CONSISTENCY CHECK
```json
{
  "dimension": "V-03",
  "name": "CONSISTENCY CHECK",
  "items_type": "posts"
}
```
Measures: Tone consistency, audience alignment, messaging coherence, style

#### V-04: COPY AUDIT
```json
{
  "dimension": "V-04",
  "name": "COPY AUDIT",
  "items_type": "posts"
}
```
Measures: Grammar, action verbs, data usage, persuasiveness

#### V-05: ENGAGEMENT CHECK
```json
{
  "dimension": "V-05",
  "name": "ENGAGEMENT CHECK",
  "items_type": "posts + ideas"
}
```
Measures: Hook quality, discussion potential, social proof, uniqueness

#### V-06: BATCH VALIDATION
```json
{
  "dimension": "V-06",
  "name": "BATCH VALIDATION",
  "items_type": "items"
}
```
Measures: Composite score across all dimensions, prioritization

#### V-07: IDEA VALIDATION
```json
{
  "dimension": "V-07",
  "name": "IDEA VALIDATION",
  "items_type": "ideas"
}
```
Measures: Viability, research difficulty, audience fit, uniqueness

## Usage in Step Files

Replace dimensional breakdown sections with:

```markdown
### Dimensional Analysis

Load template from: `../../data/report-templates/dimensional-report-sections.md`

Display sections for V-01 through V-07 with actual score data:
- Load score from validation results
- Calculate issue counts from data
- Apply status indicators
- Include recommendations based on score thresholds
```

## Critical Issue Extraction

For files that list critical issues, separate this into:

File: `data/report-templates/critical-issues-template.md`

```markdown
## Critical Issues (Require Immediate Attention)

Posts failing multiple validations:

{critical_issues_list}

Where each issue is:
```
🔴 Post #{id}: "{title}"
   Failures: {failure_list}
   Severity: CRITICAL
   Fix time: {est_time}
   Status: {status}
```

Replace in-file lists with loading and rendering from JSON:
```json
{
  "critical_posts": [
    {
      "id": 3,
      "title": "Why Most People Fail at Fitness",
      "failures": ["Quality 3/5", "Copy 1/5", "Engagement 2 stars"],
      "severity": "CRITICAL",
      "fix_time": "30 min",
      "status": "REWRITE REQUIRED"
    }
  ]
}
```
