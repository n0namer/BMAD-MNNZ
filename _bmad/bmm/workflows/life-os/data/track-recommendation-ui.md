---
name: 'track-recommendation-ui'
version: '1.0'
purpose: 'UI templates for presenting track recommendations to users'
consumedBy:
  - step-01-collect-ideas.md
---

# Track Recommendation UI Templates

## Template 1: High/Medium Confidence (≥75%)

Use when the algorithm has a clear recommendation.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 TRACK RECOMMENDATION

Based on your idea "{title}":

  Recommended track: {QUICK / STANDARD / DEEP}
  Confidence: {percentage}% ({HIGH / MEDIUM / LOW})
  Estimated time: {15-20 min / 45-60 min / 2-4 hours}

  Key factors:
  - Domain: {domain} ({contributes to X track})
  - Complexity: {complexity_signal} ({contributes to X track})
  - Resources: {resource_level} ({contributes to X track})
  {If relevant: - Budget: {budget_range} ({contributes to X track})}
  {If relevant: - Stakeholders: {stakeholder_count} ({contributes to X track})}
  {If relevant: - Novelty: {novelty} ({contributes to X track})}

  Score: {total_score} / 20.0

  What's included in each track:

  [Q] Quick Track (15-20 min)
      ✓ Fast consilium (2-3 specialists, no Six Hats)
      ✓ Simplified scoring (3 criteria only)
      ✗ No portfolio integration
      ✗ No deep plan

  [S] Standard Track (45-60 min) {← RECOMMENDED if this is the choice}
      ✓ Full consilium (4-6 specialists, Six Hats)
      ✓ Full scoring (9 criteria + domain-specific)
      ✓ Portfolio integration
      ✗ No calendar sync
      ✗ No deep plan

  [D] Deep Track (2-4 hours)
      ✓ Goals alignment check
      ✓ Deep consilium (6-8 specialists, multi-round)
      ✓ Optional TRIZ analysis
      ✓ Full scoring + portfolio integration
      ✓ Calendar sync
      ✓ L1-L6 deep plan with auto-intelligence

  Your choice: [Q/S/D]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Template 2: Low Confidence (<75%)

Use when signals are ambiguous and user must choose.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ TRACK SELECTION NEEDED

I couldn't confidently recommend a track based on the information provided.
Confidence: {percentage}% (LOW)

Here are your options:

[Q] Quick Track (15-20 min)
    Best for: Simple ideas, low stakes, proven models
    Gets you: Fast go/no-go decision + 2-3 key risks

[S] Standard Track (45-60 min)
    Best for: Medium complexity, moderate stakes
    Gets you: Full specialist analysis + scoring + portfolio fit

[D] Deep Track (2-4 hours)
    Best for: High stakes, complex projects, strategic decisions
    Gets you: Full strategic plan + goals alignment + calendar sync

Which track feels right for your idea?
Your choice: [Q/S/D]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Template 3: User Override Warning (Lighter Track)

Use when user chooses a lighter track than recommended.

```
⚠️ Note: You chose {chosen_track} but {recommended_track} was recommended.

{Track name} skips:
{List of skipped steps based on track comparison}

Proceed with {chosen_track}? [Y/N]
```

### Skip Lists by Override Type

**Standard → Quick skips:**
- Roles discovery (Step 02)
- Specialist matching (Step 03)
- Full Six Hats consilium (Step 04 becomes Lite)
- Portfolio integration (Step 06)
- Domain-specific scoring criteria (Step 05 simplified)

**Deep → Standard skips:**
- Goals alignment check (Step 00)
- Calendar sync (Step 07)
- Deep plan L1-L6 (Step 08)
- TRIZ analysis (Step 04.5)
- Advanced plan polish (Step 08.5)

**Deep → Quick skips:**
- Goals alignment check (Step 00)
- Roles discovery (Step 02)
- Specialist matching (Step 03)
- Full consilium (Step 04 becomes Lite)
- Portfolio integration (Step 06)
- Calendar sync (Step 07)
- Deep plan (Step 08)
- TRIZ analysis (Step 04.5)

## Template 4: No Warning (Heavier Track)

Use when user chooses a heavier track than recommended.

No warning needed. Simply proceed with:

```
✅ {chosen_track} track selected. Proceeding to {next_step_name}...
```

## Presentation Rules

1. **Always show all three tracks** in the menu, regardless of recommendation
2. **Mark recommended track** with an arrow `{← RECOMMENDED}` if confidence ≥75%
3. **Include score breakdown** only if confidence is MEDIUM or LOW (helps user understand)
4. **Keep factor list to 3-4 items max** (most impactful factors only)
5. **Show time estimates** for all three tracks (helps user make informed choice)
6. **Use emoji sparingly** (📊 for recommendation header, ⚠️ for warnings only)

## Color/Formatting Guidelines

- Use horizontal rules `━━━━━━` to separate recommendation blocks
- Indent track options with 2 spaces
- Indent track details with 4 spaces
- Use `✓` for included features, `✗` for excluded features
- Bold track names and key labels
- Use brackets `[Q/S/D]` for menu options

## Integration

This file is referenced in:
- **step-01-collect-ideas.md** Step 9.6 (Present Track Recommendation)
- **step-01-collect-ideas.md** Step 9.7 (Handle User Override)
