---
description: Save merged post to knowledge base
name: step-c-06d-save
nextStepFile: ../../mode-c/mode-c-00-menu.md
type: confirmation
---

# CREATE C-06: Merge Posts - Save Merged Content

## STEP GOAL:

Save generated merged post to posts_published.csv and update knowledge base with new resource.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Save Confirmation

```
═══════════════════════════════════════════════════════════════

  💾  SAVE MERGED POST

═════════════════════════════════════════════════════════════════

MERGED POST SUMMARY:

Title: [Generated or user-edited title]
Type: Merged Resource
Source Posts: 3 (Posts #1, #2, #4)
Word Count: 5,847
Reading Time: 18 minutes
Quality: ★★★★★ 8.6/10

─────────────────────────────────────────────────────────────

SAVE LOCATION: posts_published.csv

Entry Details:
  • Post ID: [Auto-generated]
  • Publication Status: DRAFT
  • Created: 2026-01-28
  • Last Modified: 2026-01-28
  • Source Merge: [Posts 1, 2, 4]
  • Format: blog-post

─────────────────────────────────────────────────────────────
```

### 2. Create Post Entry

```
Creating CSV entry with:

Column 1 (Post ID): post-merged-[timestamp]
Column 2 (Title): [Full title]
Column 3 (Content): [Full merged content]
Column 4 (Meta Description): [Generated summary]
Column 5 (Word Count): 5847
Column 6 (Reading Time): 18 min
Column 7 (Status): draft
Column 8 (Category): merged-resource
Column 9 (Source Posts): post-1, post-2, post-4
Column 10 (Created): 2026-01-28T14:35:00Z
Column 11 (Quality Score): 8.6
Column 12 (Last Modified): 2026-01-28T14:35:00Z

═════════════════════════════════════════════════════════════════
```

### 3. Create Backup Entry

```
Auto-backup version created:

File: posts_merged_backup_[timestamp].csv
Contains: Full merged post details + metadata
Location: /data/backups/
Retention: 30 days

✓ Backup created successfully
```

### 4. Update Knowledge Base

```
Updating knowledge base with:

Entry: merged-post-[id]
├─ Type: merged-resource
├─ Source Posts: [1, 2, 4]
├─ Themes: [Extracted themes]
├─ Quality: 8.6/10
├─ Last Updated: 2026-01-28
└─ Status: ACTIVE

Relationships:
  • Links to Post #1: [Yes]
  • Links to Post #2: [Yes]
  • Links to Post #4: [Yes]
  • Cross-references: [Count] posts

═════════════════════════════════════════════════════════════════
```

### 5. Display Save Status

```
SAVE STATUS:
─────────────────────────────────────────────────────────────

✓ Post entry saved to posts_published.csv
✓ Backup created successfully
✓ Knowledge base updated
✓ Cross-references established

SUCCESS: Merged post saved! 🎉

Post ID: post-merged-[id]
Status: DRAFT (ready for publishing)

Next Steps:
  • Publish post (in EDIT mode > Publish)
  • Share on social media
  • Monitor engagement metrics
  • Create variants (in VALIDATE mode)

─────────────────────────────────────────────────────────────
```

### 6. Return to Main Menu

```
WHAT'S NEXT?

[C] CREATE MORE
    Go back to CREATE menu to generate new posts

[E] EDIT
    Switch to EDIT mode to refine this post

[V] VALIDATE
    Switch to VALIDATE mode to check quality

[Y] YOLO MODE
    Generate multiple posts quickly

[M] MAIN MENU
    Return to main workflow menu

[?] HELP
    Learn about available options
```

## SUCCESS CRITERIA:

✓ Merged post saved to posts_published.csv
✓ All metadata stored correctly
✓ Backup created successfully
✓ Knowledge base updated
✓ Navigation options presented clearly

## OUTPUT:

Merged post saved and ready for publishing. User directed to next workflow step.

## INTEGRATION:

- Files saved to: `data/posts_published.csv`
- Backup location: `data/backups/`
- Knowledge base: Updated with merged resource entry
- Next steps: Available in main menu navigation
