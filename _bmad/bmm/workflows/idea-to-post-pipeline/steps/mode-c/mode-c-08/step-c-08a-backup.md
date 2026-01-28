---
description: Create and verify backup of all posts data
name: step-c-08a-backup
nextStepFile: ./step-c-08b-maintenance.md
type: management
---

# CREATE C-08: Manage Base - Create Backup

## STEP GOAL:

Create comprehensive backup of all posts, ideas, and knowledge base data for disaster recovery and version control.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Backup Initialization

```
═══════════════════════════════════════════════════════════════

  🔄  CREATE SYSTEM BACKUP

═════════════════════════════════════════════════════════════════

System Status: READY FOR BACKUP

Current Data Summary:
─────────────────────────────────────────────────────────────
  • Total Ideas: 47 (ideas_inbox.csv)
  • Published Posts: 156 (posts_published.csv)
  • Draft Posts: 23 (posts_draft.csv)
  • Merged Resources: 8 (posts_merged.csv)
  • Knowledge Base Entries: 342
  • Total File Size: ~45MB

Last Backup: 2026-01-27 08:15 (< 24 hours ago)
System Health: ✓ Normal

─────────────────────────────────────────────────────────────
```

### 2. Select Backup Type

```
CHOOSE BACKUP TYPE:

[1] QUICK BACKUP
    Only changed files since last backup
    Time: ~2 minutes
    Size: Varies (typically 1-5MB)

[2] FULL BACKUP
    Complete copy of all data
    Time: ~10 minutes
    Size: ~45MB

[3] SELECTIVE BACKUP
    Choose specific data types to backup
    Time: Varies
    Size: Varies

[?] HELP
    Learn about backup strategies
```

### 3. Execute Backup Process

```
BACKUP IN PROGRESS...
═════════════════════════════════════════════════════════════════

[████████░░░░░░░░░░] 45%

Backing up:
  ✓ ideas_inbox.csv (47 ideas - 2.3MB)
  ✓ posts_published.csv (156 posts - 28.5MB)
  ✓ posts_draft.csv (23 posts - 5.2MB)
  ✓ posts_merged.csv (8 resources - 3.1MB)
  ⏳ knowledge_base/ (342 entries - ~6MB)
  ⏳ metadata/ (various files)

Estimated time remaining: 5 minutes...

═════════════════════════════════════════════════════════════════
```

### 4. Create Backup Manifest

```
Generating backup manifest with:

Backup Details:
─────────────────────────────────────────────────────────────
  • Backup ID: bak-2026-01-28-14-45
  • Type: FULL BACKUP
  • Created: 2026-01-28 14:45:32 UTC
  • Total Files: 234
  • Total Size: 45.1MB
  • Compression: GZIP (.tar.gz)
  • Encryption: AES-256
  • Duration: 9 minutes 47 seconds

Files Included:
  ├─ CSV Data Files (4):
  │  ├─ ideas_inbox.csv
  │  ├─ posts_published.csv
  │  ├─ posts_draft.csv
  │  └─ posts_merged.csv
  ├─ Knowledge Base (342 entries)
  ├─ Metadata (156 files)
  ├─ Configuration (23 files)
  └─ Logs (5 files)

─────────────────────────────────────────────────────────────

Backup Verification:
  ✓ All files included
  ✓ Checksums verified (MD5, SHA256)
  ✓ Compression successful
  ✓ Encryption applied
  ✓ Backup integrity: CONFIRMED

═════════════════════════════════════════════════════════════════
```

### 5. Save Backup

```
SAVING BACKUP...

Location: /data/backups/bak-2026-01-28-14-45.tar.gz
Size: 12.3MB (compressed from 45.1MB)
Compression Ratio: 3.67:1

✓ Backup saved successfully

Backup File Details:
  • Full Path: D:\...\backups\bak-2026-01-28-14-45.tar.gz
  • Readable By: System administrator
  • Accessible From: Recovery console
  • Retention: 90 days (auto-delete policy)

═════════════════════════════════════════════════════════════════
```

### 6. Display Backup Summary

```
BACKUP COMPLETE ✓

Summary:
─────────────────────────────────────────────────────────────
  • Status: SUCCESS
  • Time Elapsed: 9m 47s
  • Files Backed Up: 234
  • Total Data: 45.1MB (12.3MB compressed)
  • Backup ID: bak-2026-01-28-14-45

Recovery Information:
  To restore this backup, use:
  $ restore-backup bak-2026-01-28-14-45

  Or from recovery console:
  > restore --backup-id bak-2026-01-28-14-45

─────────────────────────────────────────────────────────────

STORAGE STATUS:
  Backup Storage: 156.4GB / 500GB (31% used)
  Available: 343.6GB
  Retention: 90 days

═════════════════════════════════════════════════════════════════
```

### 7. Provide Next Steps

```
WHAT'S NEXT?

[V] VERIFY BACKUP
    Test restore functionality

[L] VIEW BACKUPS
    See all existing backups

[S] SCHEDULE BACKUP
    Set automatic backup schedule

[N] NEXT STEP
    Proceed to maintenance checks

[M] BACK
    Return to management menu

[?] HELP
    Learn about backup management
```

## SUCCESS CRITERIA:

✓ Backup created successfully
✓ All data files included
✓ Backup integrity verified
✓ File saved to correct location
✓ Recovery information provided

## RECOVERY NOTES:

- Restore full backup: `restore-backup [backup-id]`
- Restore specific files: `restore-backup [backup-id] --files [file-list]`
- Verify backup: `verify-backup [backup-id]`
- List all backups: `list-backups`
