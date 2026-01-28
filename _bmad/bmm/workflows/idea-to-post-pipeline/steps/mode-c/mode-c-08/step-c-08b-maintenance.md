---
description: Run system maintenance and optimization checks
name: step-c-08b-maintenance
nextStepFile: ../../mode-c/mode-c-00-menu.md
type: management
---

# CREATE C-08: Manage Base - System Maintenance

## STEP GOAL:

Run comprehensive maintenance routines to ensure system health, optimize data storage, and identify potential issues.

## EXECUTION:
### EXECUTION RULES - HALT AND WAIT

**ALWAYS halt and wait for user input after presenting menu or asking for selection.**
**ONLY proceed to next step when user provides explicit input/selection.**


### 1. Display Maintenance Menu

```
═══════════════════════════════════════════════════════════════

  🛠️   SYSTEM MAINTENANCE

═════════════════════════════════════════════════════════════════

Workflow Status: HEALTHY
Last Maintenance: 2026-01-27 08:15
Maintenance Mode: STANDARD

SELECT MAINTENANCE OPERATION:

─────────────────────────────────────────────────────────────
```

### 2. Run Diagnostics

```
[1] RUN FULL DIAGNOSTICS
    Check all system components

    Includes:
    • Database integrity check
    • File system validation
    • Data consistency verification
    • Performance analysis
    • Backup verification

    Time: ~15 minutes
    Impact: Read-only (no data changes)

[2] OPTIMIZE DATABASE
    Defragment and optimize data storage

    Includes:
    • Defragment tables
    • Rebuild indexes
    • Cleanup deleted records
    • Optimize queries

    Time: ~10 minutes
    Impact: May pause operations briefly

[3] CLEAN UP TEMPORARY FILES
    Remove cache, temp files, old logs

    Includes:
    • Clear cache
    • Delete temp files
    • Archive old logs (>30 days)
    • Remove duplicates

    Time: ~5 minutes
    Impact: Frees disk space

[4] VERIFY DATA INTEGRITY
    Check for corrupted or missing files

    Includes:
    • Verify checksums
    • Check file permissions
    • Validate CSV structure
    • Test data access

    Time: ~8 minutes
    Impact: Read-only

[?] HELP - Learn about maintenance operations
```

### 3. Execute Selected Operation

```
RUNNING FULL DIAGNOSTICS...
═════════════════════════════════════════════════════════════════

[████████████████░░░░] 80%

Current Checks:
─────────────────────────────────────────────────────────────

✓ Database Tables: 23/23 validated
  └─ ideas_inbox: 47 records, 2.3MB
  └─ posts_published: 156 records, 28.5MB
  └─ posts_draft: 23 records, 5.2MB
  └─ posts_merged: 8 records, 3.1MB
  └─ kb_entries: 342 records, 6.2MB
  └─ metadata: 234 records, 4.1MB

✓ File System: 456 files validated
  └─ CSV files: OK
  └─ Markdown files: OK
  └─ Configuration: OK
  └─ Backups: OK

⏳ Data Consistency: Checking...
  └─ Cross-references: 892/892 valid
  └─ Missing files: 0
  └─ Orphaned records: 0

⏳ Performance Analysis: In progress...

═════════════════════════════════════════════════════════════════
```

### 4. Display Diagnostics Results

```
DIAGNOSTICS COMPLETE ✓
═════════════════════════════════════════════════════════════════

SYSTEM HEALTH: ✅ EXCELLENT

Overall Score: 98.7/100 (Very Healthy)

─────────────────────────────────────────────────────────────

DETAILED RESULTS:

Database Health: ✅ 100/100
  • No corrupted tables
  • All indexes operational
  • Data consistency: Perfect
  • Query performance: Optimal

File System: ✅ 98/100
  • Total files: 456
  • Integrity: 456/456 OK
  • Permissions: Correct
  • Storage: Healthy

Data Quality: ✅ 99/100
  • Cross-references: 892/892 valid
  • Missing data: 0
  • Orphaned records: 0
  • Duplicate detection: None found

Performance: ✅ 97/100
  • Average query time: 24ms
  • Backup restore time: 8m 34s
  • Data access speed: Optimal
  • System load: 12%

─────────────────────────────────────────────────────────────

RECOMMENDATIONS:

Optional Optimizations:
  1. Optimize database (saves ~2MB space)
  2. Archive logs older than 30 days (frees 150MB)
  3. Update search indexes (improves speed 5%)

No Critical Issues Found ✓

═════════════════════════════════════════════════════════════════
```

### 5. Optimization Options

```
MAINTENANCE OPTIONS:

[O] OPTIMIZE DATABASE
    Run optimization routine
    Estimated time: 10 minutes
    Benefit: 2MB saved, 5% faster queries

[C] CLEANUP FILES
    Remove temporary and old files
    Estimated time: 5 minutes
    Benefit: 150MB freed

[U] UPDATE INDEXES
    Rebuild search indexes
    Estimated time: 8 minutes
    Benefit: 5% faster searches

[S] SCHEDULE MAINTENANCE
    Set automatic maintenance schedule
    Options: Daily, Weekly, Monthly

[N] NEXT STEP
    Return to management menu

[M] BACK
    Back to previous menu

[?] HELP
    Learn more about maintenance
```

### 6. Execute Optimization

```
OPTIMIZATION IN PROGRESS...
═════════════════════════════════════════════════════════════════

[████████████████████] 100%

Operations Completed:
─────────────────────────────────────────────────────────────

✓ Database Optimization
  • Defragmentation: Complete
  • Space freed: 2.1MB
  • Query performance improvement: +5.2%
  • Time: 9m 23s

✓ File Cleanup
  • Temporary files deleted: 34
  • Old logs archived: 12
  • Space freed: 156MB
  • Time: 4m 12s

✓ Index Update
  • Indexes rebuilt: 8
  • Index size optimized: 23%
  • Search speed improvement: +4.8%
  • Time: 7m 45s

═════════════════════════════════════════════════════════════════

OPTIMIZATION COMPLETE ✓

Results:
─────────────────────────────────────────────────────────────
  • Total time: 21m 20s
  • Space freed: 158.1MB
  • Performance improved: +5.0%
  • System status: EXCELLENT

Available Storage:
  • Before: 343.6GB free
  • After: 501.7GB free
  • Improvement: +158.1GB (+46%)

═════════════════════════════════════════════════════════════════
```

### 7. Final Summary & Next Steps

```
MAINTENANCE SUMMARY:

Status: ✅ COMPLETE & SUCCESSFUL

System Performance:
  • Health Score: 98.7/100 (Excellent)
  • Storage Efficiency: Optimized (+158MB)
  • Query Speed: +5.2% improvement
  • Overall Status: All systems nominal

Next Maintenance: 2026-02-04 (automatic schedule)

═════════════════════════════════════════════════════════════════

WHAT'S NEXT?

[B] BACK TO MENU
    Return to CREATE mode menu

[M] MAIN WORKFLOW
    Go to main workflow menu

[A] ADDITIONAL TASKS
    • View system logs
    • Export reports
    • Configure backup schedule
    • Advanced settings

[?] HELP
    Learn about system features

═════════════════════════════════════════════════════════════════
```

## SUCCESS CRITERIA:

✓ All diagnostic checks completed
✓ System health status verified
✓ Optimizations applied successfully
✓ Performance improved
✓ Storage cleaned up
✓ Future maintenance scheduled

## MAINTENANCE SCHEDULE:

- Daily: Automatic log rotation
- Weekly: Index optimization
- Monthly: Full system diagnostics
- Quarterly: Database reorganization
- Yearly: Major system review

## SUPPORT:

For issues or questions: `help maintenance` or contact system administrator.
