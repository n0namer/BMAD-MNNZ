# PDCA Review Reminders - Automated System

## Overview

Automated reminder system for PDCA reviews across 4 cadences:
- **Daily (EOD - 18:00)**: 5-min standup prompt
- **Weekly (Sunday 19:00)**: 30-min velocity review prompt
- **Monthly (Last Sunday 19:00)**: 1-hour trajectory analysis prompt
- **Quarterly (Last week of quarter)**: 2-hour strategic replanning prompt

## Features

- ✅ **Automatic detection** of review timing based on current date/time
- ✅ **Skip logic**: Won't prompt if review already completed
- ✅ **Priority-based**: Quarterly > Monthly > Weekly > Daily (shows highest priority only)
- ✅ **Memory integration**: Logs reminder delivery to Claude Flow memory
- ✅ **Cross-platform**: Bash (Linux/macOS) and PowerShell (Windows) versions
- ✅ **Cron/Task Scheduler ready**: Can run as scheduled job

## Files

| File | Purpose |
|------|---------|
| `scripts/review-reminders.sh` | Bash version (Linux/macOS) |
| `scripts/review-reminders.ps1` | PowerShell version (Windows) |
| `docs/REVIEW-REMINDERS.md` | This documentation |

## Usage

### Basic Usage

**Linux/macOS (Bash):**
```bash
cd /path/to/life-os
./scripts/review-reminders.sh
```

**Windows (PowerShell):**
```powershell
cd C:\path\to\life-os
.\scripts\review-reminders.ps1
```

### Check Mode (no prompt)

**Bash:**
```bash
./scripts/review-reminders.sh --check
```

**PowerShell:**
```powershell
.\scripts\review-reminders.ps1 -Check
```

### Force Specific Cadence

**Bash:**
```bash
./scripts/review-reminders.sh --force daily
./scripts/review-reminders.sh --force weekly
./scripts/review-reminders.sh --force monthly
./scripts/review-reminders.sh --force quarterly
```

**PowerShell:**
```powershell
.\scripts\review-reminders.ps1 -Force daily
.\scripts\review-reminders.ps1 -Force weekly
.\scripts\review-reminders.ps1 -Force monthly
.\scripts\review-reminders.ps1 -Force quarterly
```

## Automated Scheduling

### Linux/macOS (Cron)

Add to crontab (`crontab -e`):

```cron
# Run every hour
0 * * * * /path/to/life-os/scripts/review-reminders.sh >> /var/log/pdca-reminders.log 2>&1

# Or run at specific times (daily check at 18:00, weekly at 19:00 Sunday)
0 18 * * * /path/to/life-os/scripts/review-reminders.sh >> /var/log/pdca-reminders.log 2>&1
0 19 * * 0 /path/to/life-os/scripts/review-reminders.sh >> /var/log/pdca-reminders.log 2>&1
```

**Make script executable:**
```bash
chmod +x /path/to/life-os/scripts/review-reminders.sh
```

### Windows (Task Scheduler)

**Method 1: Using PowerShell (Recommended)**

```powershell
# Create scheduled task (run as current user)
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -File `"C:\path\to\life-os\scripts\review-reminders.ps1`""
$trigger = New-ScheduledTaskTrigger -Daily -At "12:00AM" -RepetitionInterval (New-TimeSpan -Hours 1) -RepetitionDuration (New-TimeSpan -Days 1)
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -RunOnlyIfNetworkAvailable $false
Register-ScheduledTask -TaskName "PDCA Review Reminders" -Action $action -Trigger $trigger -Settings $settings -Description "Automated PDCA review reminders for Life OS"
```

**Method 2: Using Task Scheduler GUI**

1. Open **Task Scheduler** (`taskschd.msc`)
2. Click **Create Task** (not "Create Basic Task")
3. **General** tab:
   - Name: `PDCA Review Reminders`
   - Description: `Automated PDCA review reminders for Life OS`
   - Configure for: Windows 10/11
4. **Triggers** tab:
   - New Trigger:
     - Begin the task: **On a schedule**
     - Settings: **Daily**
     - Start: **12:00:00 AM**
     - Repeat task every: **1 hour**
     - For a duration of: **1 day**
5. **Actions** tab:
   - New Action:
     - Action: **Start a program**
     - Program/script: `powershell.exe`
     - Arguments: `-ExecutionPolicy Bypass -File "C:\path\to\life-os\scripts\review-reminders.ps1"`
     - Start in: `C:\path\to\life-os\scripts`
6. **Conditions** tab:
   - Uncheck "Start the task only if the computer is on AC power"
7. **Settings** tab:
   - Check "Run task as soon as possible after a scheduled start is missed"
8. Click **OK**

## Review Cadence Logic

### Daily Review
- **Time**: 18:00 (6:00 PM) - 22:00 (10:00 PM)
- **Skip if**: Review file exists for today (`data/reviews/daily/YYYY-MM-DD.md`)
- **Prompt**: "Quick EOD standup: what done, what blocked, learnings"

### Weekly Review
- **Time**: Sunday at 19:00 (7:00 PM)
- **Skip if**: Review file exists for this week (`data/reviews/weekly/YYYY-Wxx.md`)
- **Prompt**: "Progress to weekly goals, velocity analysis, adjust next week"

### Monthly Review
- **Time**: Last Sunday of month at 19:00 (7:00 PM)
- **Condition**: Within last 7 days of month AND Sunday
- **Skip if**: Review file exists for this month (`data/reviews/monthly/YYYY-MM.md`)
- **Prompt**: "Trajectory to quarterly goals, trend analysis, goal adjustments"

### Quarterly Review
- **Time**: Last week of quarter (last 7 days of Mar/Jun/Sep/Dec)
- **Condition**: Last month of quarter (3/6/9/12) AND last 7 days
- **Skip if**: Review file exists for this quarter (`data/reviews/quarterly/QX-YYYY.md`)
- **Prompt**: "Quarter goal achievement, strategic replanning, set next quarter OKRs"

## Priority System

If multiple reviews are due at the same time, only the **highest priority** is shown:

**Priority Order (highest to lowest):**
1. Quarterly (most important, rare)
2. Monthly (high importance, monthly)
3. Weekly (medium importance, frequent)
4. Daily (low importance, daily)

**Example:**
- If it's the last Sunday of the last month of the quarter (e.g., Dec 24), and you haven't done any reviews:
  - System shows: **Quarterly review** (highest priority)
  - After completing quarterly → System shows: **Monthly review** (next priority)
  - After completing monthly → System shows: **Weekly review** (next priority)
  - After completing weekly → System shows: **Daily review** (lowest priority)

## Memory Integration

Each reminder delivery is logged to Claude Flow memory:

**Namespace:** `life-os:reviews`
**Key format:** `reminder:{cadence}:{date}`
**Content:** `Reminder delivered at {timestamp}`

**Example:**
```
Namespace: life-os:reviews
Key: reminder:daily:2026-02-06
Content: Reminder delivered at 2026-02-06T18:05:00Z
```

This allows tracking:
- How often reminders are delivered
- Which cadences are most/least used
- Reminder delivery patterns over time

## Example Output

### Daily Review Prompt
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ TIME FOR DAILY REVIEW!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Duration: 5 minutes
Purpose: Quick EOD standup: what done, what blocked, learnings

Run: step-07-pdca-review.md and select daily cadence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Weekly Review Prompt
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ TIME FOR WEEKLY REVIEW!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Duration: 30 minutes
Purpose: Progress to weekly goals, velocity analysis, adjust next week

Run: step-07-pdca-review.md and select weekly cadence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Monthly Review Prompt
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ TIME FOR MONTHLY REVIEW!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Duration: 1 hour
Purpose: Trajectory to quarterly goals, trend analysis, goal adjustments

Run: step-07-pdca-review.md and select monthly cadence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Quarterly Review Prompt
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ TIME FOR QUARTERLY REVIEW!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Duration: 2 hours
Purpose: Quarter goal achievement, strategic replanning, set next quarter OKRs

Run: step-07-pdca-review.md and select quarterly cadence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Troubleshooting

### Script doesn't run (permission denied)

**Linux/macOS:**
```bash
chmod +x /path/to/life-os/scripts/review-reminders.sh
```

**Windows:**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### Cron job not working

**Check cron logs:**
```bash
# Ubuntu/Debian
grep CRON /var/log/syslog

# CentOS/RHEL
grep CRON /var/log/cron

# Or check your custom log
tail -f /var/log/pdca-reminders.log
```

**Test manually first:**
```bash
/path/to/life-os/scripts/review-reminders.sh --force daily
```

### Task Scheduler not triggering

1. Open Task Scheduler
2. Right-click task → **Run**
3. Check **History** tab for errors
4. Verify **Triggers** configuration (repeat interval, duration)
5. Check **Conditions** (ensure "Start only if on AC power" is unchecked)

### Memory storage failing

**Check Claude Flow daemon status:**
```bash
npx claude-flow@v3alpha daemon status
```

**If daemon not running:**
```bash
npx claude-flow@v3alpha daemon start
```

**Verify memory backend:**
```bash
npx claude-flow@v3alpha memory status
```

## Advanced Configuration

### Customize Review Times

**Edit the script configuration section:**

**Bash (`review-reminders.sh`):**
```bash
# Review cadences configuration
DAILY_TIME="18:00"          # Change to your preferred time
WEEKLY_DAY="0"              # Sunday (0-6, 0=Sunday, 6=Saturday)
WEEKLY_TIME="19:00"         # Change to your preferred time
MONTHLY_DAY_OFFSET=7        # Days before end of month (7 = last week)
MONTHLY_TIME="19:00"        # Change to your preferred time
QUARTERLY_DAY_OFFSET=7      # Days before end of quarter
```

**PowerShell (`review-reminders.ps1`):**
```powershell
# Review cadences configuration
$DailyTime = [TimeSpan]::Parse("18:00")       # Change to your preferred time
$WeeklyDay = [DayOfWeek]::Sunday              # Change to your preferred day
$WeeklyTime = [TimeSpan]::Parse("19:00")      # Change to your preferred time
$MonthlyDayOffset = 7                          # Days before end of month
$MonthlyTime = [TimeSpan]::Parse("19:00")     # Change to your preferred time
$QuarterlyDayOffset = 7                        # Days before end of quarter
```

### Disable Specific Cadences

Comment out the cadence check in the main logic:

```bash
# if check_quarterly_review; then
#     ...
# fi

if check_monthly_review; then
    ...
fi
```

### Custom Notifications

Extend the script to send notifications via:
- Email (using `sendmail` or SMTP)
- Slack (using webhook)
- Desktop notification (using `notify-send` or Windows Toast)

**Example (Linux desktop notification):**
```bash
# Add to prompt_review() function
notify-send "PDCA Review Due" "$cadence review is due ($duration)"
```

**Example (Windows Toast notification):**
```powershell
# Add to Show-ReviewPrompt function
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
$template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
$toastXml = [xml] $template.GetXml()
$toastXml.GetElementsByTagName("text")[0].AppendChild($toastXml.CreateTextNode("PDCA Review Due")) | Out-Null
$toastXml.GetElementsByTagName("text")[1].AppendChild($toastXml.CreateTextNode("$Cadence review is due ($Duration)")) | Out-Null
$xml = New-Object Windows.Data.Xml.Dom.XmlDocument
$xml.LoadXml($toastXml.OuterXml)
$toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("PDCA Reminders").Show($toast)
```

## Integration with Life OS Workflow

### Workflow Connection

The reminder system integrates with **step-07-pdca-review.md**:

1. Reminder script detects due review
2. User runs `step-07-pdca-review.md`
3. User selects cadence from menu
4. Workflow creates review file in `data/reviews/{cadence}/`
5. Next time script runs, it detects existing review file and skips

### Automatic Detection

The script automatically detects completed reviews by checking:
- `data/reviews/daily/YYYY-MM-DD.md`
- `data/reviews/weekly/YYYY-Wxx.md`
- `data/reviews/monthly/YYYY-MM.md`
- `data/reviews/quarterly/QX-YYYY.md`

If the file exists, the review is considered complete for that period.

## Best Practices

### Recommended Setup

1. **Run hourly** (via cron/Task Scheduler) for consistent reminders
2. **Start with daily reviews** to build the habit
3. **Weekly is the most important** cadence (30 min well spent)
4. **Don't skip Act phase** - adjustments are the point of PDCA
5. **Review past reviews** before starting new one for context

### Anti-Patterns to Avoid

❌ **Snoozing reminders repeatedly** → Set realistic times
❌ **Completing review without user input** → AI-generated reviews are useless
❌ **Skipping Act phase** → Without adjustments, it's just documentation theater
❌ **Running multiple cadences at once** → Priority system exists for a reason
❌ **Ignoring chronic blockers** → Address them in Act phase

### Success Metrics

Track these in your metrics file:
- **Daily review completion rate** (target: 80%+)
- **Weekly review consistency** (target: every Sunday)
- **Monthly trajectory alignment** (actual vs expected)
- **Quarterly OKR achievement** (target: 70%+ avg)

## FAQ

**Q: What if I miss a review?**
A: The script will prompt you the next time it runs. Complete it as soon as possible to maintain continuity.

**Q: Can I run multiple cadences in one session?**
A: Yes, after completing the highest priority review, run the script again to see the next priority.

**Q: What if the script shows the wrong cadence?**
A: Use `--force` to manually select the cadence you want.

**Q: How do I disable reminders temporarily?**
A: Stop the cron job or Task Scheduler task. Re-enable when ready.

**Q: Can I customize the reminder times?**
A: Yes, edit the configuration section at the top of the script.

**Q: Does the script work offline?**
A: Yes, the script itself works offline. Memory storage requires Claude Flow daemon running (can be local).

**Q: What if I complete a review manually (not via script)?**
A: Create the review file manually in the correct location (e.g., `data/reviews/daily/2026-02-06.md`) and the script will detect it.

## Support

For issues or questions:
- Check this documentation first
- Review **step-07-pdca-review.md** for workflow details
- Check **data/pdca-integration-guide.md** for PDCA theory

## Version History

**v1.0.0** (2026-02-06):
- Initial release
- Support for all 4 cadences
- Cross-platform (Bash + PowerShell)
- Memory integration
- Cron/Task Scheduler ready
- Priority-based system
- Skip logic for completed reviews
