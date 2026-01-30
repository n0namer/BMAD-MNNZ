# Data Collection Implementation Guide
**Step-by-Step Setup for Style Preset Effectiveness Tracking**

Date: 2026-01-30
Version: 1.0
Audience: Data Analyst + Content Team

---

## QUICK START: 5-STEP SETUP (Week 1)

### Step 1: Define Your Style Presets (30 minutes)

Before tracking anything, you need to define exactly what each preset means.

**Example Preset Definition:**

```
PRESET #1: STORY-DRIVEN
├─ Hook Type: Narrative curiosity + personal relevance
├─ Structure: Setup → Problem → Personal experience → Transformation → CTA
├─ Tone: Warm, vulnerable, inspiring
├─ Language: Conversational, specific examples, emotional words
├─ CTA Style: Question-based ("What would you do?") or inspiring action
├─ Emotional Appeals: Empathy, hope, relatability
├─ Specificity: High (personal details, specific numbers)
├─ Length: 200-500 characters (Telegram optimized)
├─ Example: "I spent 6 months trying to scale my business... until I realized..."
└─ Best for: Insight posts, personal brand, emotional connection

PRESET #2: PROFESSIONAL
├─ Hook Type: Credibility + logical urgency
├─ Structure: Problem → Data/Evidence → Solution → Social proof → CTA
├─ Tone: Confident, authoritative, trustworthy
├─ Language: Formal but accessible, statistics, proven methods
├─ CTA Style: Direct action ("Click here to learn more")
├─ Emotional Appeals: Trust, authority, risk mitigation
├─ Specificity: Very high (data, metrics, case studies)
├─ Length: 200-400 characters
├─ Example: "Studies show 73% of entrepreneurs fail due to poor systems..."
└─ Best for: B2B content, credibility-building, How-To posts

[Continue for 4-6 presets based on your needs]
```

**Task 1.1: Define Presets**
- [ ] List 4-6 presets your team actually uses
- [ ] Describe each using template above
- [ ] Get team agreement on definitions
- [ ] Create reference document for team

---

### Step 2: Set Up Tracking Tables (1 hour)

Create a master CSV file with all data fields you'll collect.

**Core Tracking Table: posts_tracking.csv**

```csv
post_id,date_published,research_id,angle_used,style_preset,
style_variant,selection_method,confidence_score,platform,
content_type,target_audience,industry,length_chars,
hour_1_ctr,hour_6_ctr,hour_24_ctr,final_ctr,views_total,
clicks_total,comments_24h,shares_24h,saves_24h,engagement_rate,
sentiment_score,humanness_score,quality_score,status,notes
```

**Minimal Version (Start Here):**

```csv
post_id,date,style_preset,platform,hour_24_ctr,final_ctr,comments,
engagement_rate,quality_score,status
1,2026-01-28,story-driven,telegram,3.2%,4.5%,8,4.2%,92,published
2,2026-01-28,professional,linkedin,1.8%,2.1%,3,1.5%,78,published
3,2026-01-29,conversational,twitter,4.1%,4.8%,12,5.1%,85,published
```

**Task 2.1: Create Tracking File**
- [ ] Create `/data/analytics/posts_tracking.csv`
- [ ] Add header row with all fields
- [ ] Backfill data from 10-20 recent posts
- [ ] Calculate sample metrics

---

### Step 3: Create Post Metadata Template (30 minutes)

Every post should have metadata about which style was used.

**Add to your post creation workflow:**

```yaml
---
# Post Metadata
post_id: 8
date_created: 2026-01-30
date_published: 2026-01-30T14:30:00Z

# Content Info
research_id: research_3
idea_title: "How to scale without burning out"
angle_used: emotional_pain
content_type: story
target_audience: solopreneurs
industry: content_creation

# Style Preset
style_preset: story-driven
style_variant: emotional_transformation
selection_method: ai_recommendation
selection_confidence: 0.85

# Alternative Presets Considered
alternatives:
  - name: conversational
    confidence: 0.72
  - name: professional
    confidence: 0.64

# Platform & Technical
platform: telegram
post_length_chars: 412
has_emoji: true
has_link: true
optimal_publish_time: 14:30 UTC

# Tags for Analysis
tags: [transformation, personal-journey, vulnerability, actionable]
---

[Post content starts here...]
```

**Task 3.1: Add Metadata**
- [ ] Create template file in your workflow
- [ ] Update post creation process to capture these fields
- [ ] Use template for next 5 posts
- [ ] Verify all fields populated correctly

---

### Step 4: Set Up Daily Data Collection (30 minutes)

Decide how to pull engagement metrics daily.

**Option A: Manual (Simplest - Start Here)**

Every day at 9am:
1. Open platform analytics (Telegram, LinkedIn, etc.)
2. Record metrics for posts published in last 24h
3. Enter into tracking CSV
4. Takes: 5-10 minutes

**Option B: Semi-Automated (Better)**

Use Zapier or Make to:
1. Pull metrics from platform API automatically
2. Format into CSV
3. Append to tracking file daily
4. Takes: 10 minutes setup, then automatic

**Option C: Fully Automated (Advanced)**

Custom script that:
1. Queries all platform APIs
2. Matches with post_id metadata
3. Updates tracking file hourly
4. Triggers alerts if needed
5. Takes: 2-3 hours setup, then fully automatic

**For Week 1: Use Option A (Manual)**

```
DAILY DATA COLLECTION CHECKLIST (9am UTC)

□ Open Telegram Analytics
  - List all posts published in last 24 hours
  - For each post, record:
    * Views count
    * Click count (CTR = clicks/views)
    * Comments count
    * Shares count
    * Saves count
  - Engagement Rate = (comments + shares + saves) / views × 100

□ Open LinkedIn Analytics (if applicable)
  - Similar metrics to Telegram

□ Update posts_tracking.csv
  - Find each post_id
  - Enter hour_24_ctr and engagement_rate
  - Mark as "tracking"

□ Backup tracking file
  - Save copy to Google Drive
  - Version with date: posts_tracking_2026-01-30.csv

□ Note anomalies
  - Any posts with unusual metrics?
  - Add notes for later analysis
```

**Task 4.1: Set Up Daily Routine**
- [ ] Choose collection time (suggest 9am UTC)
- [ ] Add to calendar as recurring daily task
- [ ] Complete first full day of collection
- [ ] Verify metrics are reasonable

---

### Step 5: Create Weekly Summary Report (1 hour)

Every Friday, create a summary of the week's data.

**Simple Weekly Report Template:**

```markdown
# Weekly Performance Report
**Week of:** January 28 - February 3, 2026

## Summary Stats
- Posts published: 8
- Average CTR: 3.8%
- Average engagement: 3.2%
- Quality pass rate: 87%

## By Style Preset
| Preset | Posts | Avg CTR | Avg Eng | Best Post |
|--------|-------|---------|---------|-----------|
| Story-Driven | 4 | 4.5% | 4.1% | Post #8 (4.8%) |
| Professional | 2 | 3.1% | 2.1% | Post #5 (3.5%) |
| Conversational | 2 | 3.4% | 2.8% | Post #3 (4.1%) |

## Performance Insights
- Story-Driven outperforming other presets
- Post #8 (Story-Driven) was top performer this week
- Professional preset underperforming, consider reducing

## Recommendations
- Use Story-Driven for next 50% of posts
- Experiment with more emotional hooks
- Review why Professional posts underperforming

## Action Items
- [ ] Try 3 more Story-Driven posts next week
- [ ] Review Professional preset approach
- [ ] Test Conversational for Twitter posts
```

**Task 5.1: Create Weekly Report**
- [ ] Create template in Google Docs
- [ ] Generate first weekly report on Friday
- [ ] Share with team
- [ ] Capture 1-2 key insights

---

## DETAILED COLLECTION PROTOCOLS

### Collection Protocol 1: Engagement Metrics

**When:** Daily at 9am UTC (24 hours post-publication)

**Where:** Platform analytics

**What to collect:**

```csv
post_id,platform,hour_24_ctr,hour_24_comments,hour_24_shares,
hour_24_saves,hour_24_views,hour_24_engagement_rate
```

**How to calculate:**

```
CTR (Click-Through Rate):
  = (Total clicks) / (Total views) × 100
  = 31 clicks / 680 views × 100
  = 4.6%

Engagement Rate:
  = (comments + shares + saves) / views × 100
  = (12 + 7 + 15) / 680 × 100
  = 34 / 680 × 100
  = 5.0%

Save Rate:
  = saves / views × 100
  = 15 / 680 × 100
  = 2.2%

Share Rate:
  = shares / views × 100
  = 7 / 680 × 100
  = 1.0%
```

**Validation Checks:**
- CTR should be 1-8% (if <1% or >10%, verify data)
- Engagement should be 1-6% (if >8%, possible bot activity)
- Comments should be 1-50% of views (if >50%, verify)
- Saves usually 2-5% of views

---

### Collection Protocol 2: Sentiment & Comments

**When:** Daily at 9am UTC + manually during week

**Where:** Comments section on post

**What to collect:**

```csv
post_id,comment_count,positive_comments,negative_comments,
neutral_comments,dominant_emotion,confusion_flags,
positive_ratio
```

**How to analyze comments:**

```
Sample Comments:
1. "Exactly what I needed!" → POSITIVE, Grateful
2. "This is confusing, can you clarify?" → NEGATIVE, Confused
3. "Great tip" → POSITIVE, Appreciative
4. "How much does this cost?" → NEUTRAL, Questioning

Count:
- Positive: 2 (66%)
- Negative: 1 (33%)
- Neutral: 1 (33%)

Dominant Emotion: POSITIVE (grateful)
Confusion Flags: 1 (person didn't understand)
```

**Automated Option:**
Use Python VADER sentiment analysis:

```python
from vader_sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

for comment in post.comments:
    scores = analyzer.polarity_scores(comment.text)
    sentiment = scores['compound']  # -1 to +1

    if sentiment > 0.05:
        emotion = "POSITIVE"
    elif sentiment < -0.05:
        emotion = "NEGATIVE"
    else:
        emotion = "NEUTRAL"

    log_sentiment(post_id, sentiment, emotion)
```

---

### Collection Protocol 3: Quality Metrics (Weekly)

**When:** Every Friday

**Where:** Manual expert review of sample posts (10%)

**What to collect:**

```csv
post_id,humanness_score,readability_score,authenticity_score,
hook_quality,problem_clarity,solution_relevance,cta_clarity,
copy_strength,quality_score
```

**Scoring Rubric:**

Each metric scored 1-10:

| Score | Humanness | Readability | Authenticity |
|-------|-----------|-------------|--------------|
| 9-10 | Feels entirely human, personal quirks | Very easy, perfect pacing | Completely genuine, transparent |
| 7-8 | Mostly human with minor AI hints | Easy, good flow | Mostly authentic, minor polish |
| 5-6 | Detectable AI but edited | Average, some awkward phrasing | Some polish, mostly real |
| 3-4 | Clearly AI-generated | Difficult, clunky | Feels manufactured |
| 1-2 | Obviously AI, no editing | Very hard to read | Completely inauthentic |

**Calculation:**

```
Overall Quality Score = Average of:
- Humanness (25% weight)
- Readability (20% weight)
- Authenticity (20% weight)
- Hook Quality (15% weight)
- CTA Clarity (20% weight)

Example:
Humanness: 8/10 × 25% = 2.0
Readability: 7/10 × 20% = 1.4
Authenticity: 8/10 × 20% = 1.6
Hook Quality: 7/10 × 15% = 1.05
CTA: 8/10 × 20% = 1.6

Quality Score = 7.65/10 = 76.5%
```

---

### Collection Protocol 4: Style Preset Tagging

**When:** At time of post creation/selection

**How to capture:**

```
In post creation form, add:

[ ] Which style preset are you using?
    ○ Story-Driven
    ○ Professional
    ○ Conversational
    ○ Data-Focused
    ○ Other: _________

[ ] How confident are you in this choice?
    [1 - Not sure] ───────────────── [10 - Very confident]

[ ] Why did you choose this style?
    ___________________________________

[ ] Did you consider any alternatives?
    ☐ Style A (confidence: ___)
    ☐ Style B (confidence: ___)
    ☐ Style C (confidence: ___)
```

---

### Collection Protocol 5: Historical Data Recovery

**For existing posts (backfilling):**

**Step 1: Identify writing style**

Read post and classify into one of your presets:

```
Questions to ask:
1. What's the hook? (urgency? curiosity? story?)
2. What's the structure? (problem → solution? narrative arc?)
3. What's the tone? (formal? casual? emotional?)
4. What emotions does it appeal to?
5. How specific are the examples?

Example Analysis:
Post: "Here's how I scaled my content from 0 to 100k in 6 months.
       The secret wasn't better writing, it was better systems..."

Analysis:
- Hook: Personal story + curiosity gap
- Structure: Before → insight → lesson → CTA
- Tone: Conversational, personal
- Emotions: Aspiration, relatability
- Specificity: Numbers (100k, 6 months)

Classification: Story-Driven (confidence: 85%)
```

**Step 2: Look up historical metrics**

```
Go to platform analytics:
1. Find post in archive
2. Record all-time metrics:
   - Total views
   - Total clicks (CTR)
   - Total comments
   - Total shares
3. Note publish date (to find daily breakdowns)
```

**Step 3: Update tracking file**

```csv
post_id,date,style_preset,inference_confidence,
all_time_views,all_time_ctr,all_time_comments
```

**Task 5.2: Backfill Data**
- [ ] Identify 10-20 recent posts
- [ ] Classify each into preset
- [ ] Look up historical metrics
- [ ] Enter into tracking file

---

## DATA VALIDATION CHECKLIST

**Before analyzing data, validate it:**

```
□ No blank cells in critical fields
  (post_id, date, platform, ctr, engagement_rate)

□ Data types correct
  - Dates in YYYY-MM-DD format
  - Numbers without % symbol (3.5 not 3.5%)
  - Preset names match your definitions exactly

□ Ranges reasonable
  - CTR between 0.5% and 10%
  - Engagement between 0% and 8%
  - Quality score between 1 and 100
  - Humanness between 1 and 10

□ No duplicates
  - No post_id appears twice for same date
  - Each row represents unique post

□ Calculations verified
  - Random sample of 5 posts
  - Recalculate engagement rate manually
  - Verify matches CSV

□ Trends make sense
  - CTR not wildly fluctuating (except for viral posts)
  - Sentiment not swinging from +0.9 to -0.9
  - No sudden drops (except platform changes)
```

---

## COMMON COLLECTION MISTAKES TO AVOID

| Mistake | Problem | Solution |
|---------|---------|----------|
| Collecting at different times | Metrics not comparable | Set fixed time (9am UTC daily) |
| Incorrect CTR calculation | Analytics wrong | Use: clicks÷views×100 |
| Mixing platforms | Different benchmarks | Track separately |
| Tagging style too late | Forget what you chose | Tag immediately at creation |
| Not validating data | Analysis on bad data | Run validation check weekly |
| Collecting too many metrics | Overwhelm, inconsistency | Start minimal, add gradually |
| Manual entry errors | Human mistakes accumulate | Double-check sample weekly |
| Not backing up | Data loss | Save copy to cloud daily |

---

## SCALING UP: WEEKS 2-4

### Week 2: Add Sentiment Analysis

```
Add to daily collection:
□ Read top 5 comments on each post
□ Classify: positive, negative, neutral
□ Log dominant emotion detected
□ Note any confusion/questions
```

### Week 3: Add Quality Scoring

```
Add weekly (Friday):
□ Review random 2-3 posts
□ Score on humanness (1-10)
□ Score on readability (1-10)
□ Calculate quality index
```

### Week 4: Add Performance Matrices

```
Build analysis:
□ Create Content Type × Style matrix
□ Create Audience × Style matrix
□ Calculate average CTR for each combo
□ Identify patterns
```

---

## TOOLS & TEMPLATES SUMMARY

### Spreadsheet Setup

**Option 1: Google Sheets (Recommended)**
- Free, cloud-based, automatic backup
- Real-time collaboration
- Built-in formulas
- Easy sharing

**Option 2: Excel**
- Powerful formulas
- Works offline
- Need to manually backup

**Option 3: Airtable**
- Database-like structure
- More flexible
- Integration possibilities
- Learning curve

### Templates Needed

1. **posts_tracking.csv** - Main data file
2. **weekly_report.md** - Summary template
3. **post_metadata.yaml** - Per-post template
4. **quality_scoring_rubric.md** - Scoring guide
5. **data_validation_checklist.txt** - Validation list

---

## TIMELINE: YOUR FIRST MONTH

```
WEEK 1 (Jan 28 - Feb 3)
Mon: Define presets, create tracking file, backfill 10 posts
Tue: Start daily collection (manual)
Wed-Fri: Daily collection continues, test workflow
Fri: Create first weekly report

WEEK 2 (Feb 4 - 10)
Mon: Review Week 1 data, identify issues
Tue: Add sentiment analysis protocol
Wed-Fri: Daily collection + sentiment analysis
Fri: Second weekly report (identify first patterns)

WEEK 3 (Feb 11 - 17)
Mon: Analyze 2-week trends
Tue: Add quality scoring protocol
Wed-Fri: Full collection (metrics + sentiment + quality)
Fri: Third weekly report (with quality scores)

WEEK 4 (Feb 18 - 24)
Mon: Build performance matrices
Tue-Fri: Complete collection + analysis
Fri: Fourth weekly report + first insights
     "Story-Driven showing 21% above baseline"
```

---

## SUCCESS CRITERIA FOR DATA COLLECTION

**By end of Week 1:**
- [ ] Presets defined and team agrees
- [ ] Tracking file created and populated
- [ ] 5+ days of data collected
- [ ] First weekly report generated

**By end of Week 2:**
- [ ] 14 days of clean data
- [ ] Sentiment analysis working
- [ ] No data validation errors
- [ ] 2 weekly reports shared

**By end of Week 4:**
- [ ] 28 days of complete data
- [ ] All collection protocols working
- [ ] Quality metrics integrated
- [ ] First actionable insights identified

---

## TROUBLESHOOTING COMMON ISSUES

### Issue: CTR seems too high (>8%)

**Possible causes:**
- Different platform (Twitter has higher CTR)
- Link formatting (shortened links may have inflated metrics)
- Recent post (still collecting data)

**Solution:**
- Check platform consistency
- Look at post date
- Compare with similar posts from past

### Issue: Missing data in tracking file

**Possible causes:**
- Post published outside collection window
- Platform analytics not updated yet
- Metric not available for platform

**Solution:**
- Extend collection to 48 hours for more complete data
- Check platform analytics directly
- Skip post and mark as "pending"

### Issue: Team not consistently tagging presets

**Possible causes:**
- Template too complicated
- Unclear preset definitions
- Not part of workflow yet

**Solution:**
- Simplify tagging process
- Create quick reference guide
- Make tagging required before publishing
- Weekly checkin with team

---

## NEXT PHASE: AUTOMATION

Once manual collection is working (Week 3-4), consider:

1. **API Integration**
   - Connect platform APIs to auto-pull metrics
   - Reduces manual work by 80%
   - Requires technical setup

2. **Automated Reporting**
   - Scripts that generate weekly reports
   - Triggered automatically Friday
   - Sent to team via Slack

3. **ML Analysis**
   - Auto-classification of sentiment
   - Style auto-detection
   - Performance prediction

---

## CONCLUSION

Start simple with manual data collection this week. By Week 4, you'll have a working analytics system that tells you exactly which styles are performing best and why. This foundation enables everything else (recommendations, predictions, optimization).

The key: **Start collecting consistently before adding complexity.**

Good luck with your style preset effectiveness analysis!
