# Calendar Sync Integration System

## Overview

The Calendar Sync system provides two-way synchronization between Life OS daily TODO time blocks and external calendar systems (Google Calendar, Microsoft Outlook, iCal). This enables seamless integration with existing productivity tools while maintaining the Life OS as the source of truth for goal-oriented task planning.

## Features

### Core Capabilities

1. **Bidirectional Synchronization**
   - Parse daily TODO time blocks from Life OS markdown files
   - Create/update calendar events with goal metadata
   - Sync changes from calendar back to TODO files
   - Preserve goal_id and domain information in event metadata

2. **Multi-Platform Support**
   - Google Calendar API (primary)
   - Microsoft Outlook API (via Microsoft Graph)
   - iCal export/import (fallback)

3. **Intelligent Conflict Resolution**
   - Detect conflicts when events are modified in both systems
   - Configurable resolution strategies (calendar-wins, todo-wins, manual-review)
   - Timestamp-based last-write-wins with user override

4. **Visual Organization**
   - Color coding by domain:
     - Finance: Green (#0B8043)
     - Business: Blue (#039BE5)
     - Health: Red (#D50000)
     - Personal: Yellow (#F4B400)
     - Learning: Purple (#7986CB)
   - Weekly view generation with domain breakdown

5. **Safety Features**
   - Dry-run mode for testing
   - Backup creation before sync operations
   - Detailed logging and audit trail
   - Rollback capability

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Calendar Sync Manager                     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ TODO Parser  │  │   Conflict   │  │ Color Mapper │     │
│  │              │  │   Resolver   │  │              │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Google Calendar │  │ Outlook Calendar│  │  iCal Provider  │
│    Provider     │  │    Provider     │  │                 │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Access to Google/Microsoft developer console for API credentials

### Install Dependencies

```bash
cd _bmad/bmm/workflows/life-os/automation
pip install -r requirements.txt
```

Required packages:
- `google-api-python-client` (Google Calendar)
- `google-auth-httplib2`
- `google-auth-oauthlib`
- `O365` (Microsoft Outlook)
- `icalendar` (iCal support)
- `pyyaml` (configuration)
- `python-dateutil` (datetime parsing)

## Configuration

### 1. Create Configuration File

Copy the template:
```bash
cp calendar-sync-config.template.yaml calendar-sync-config.yaml
```

### 2. Configure Calendar Providers

Edit `calendar-sync-config.yaml`:

```yaml
# Calendar provider settings
providers:
  google:
    enabled: true
    calendar_id: "primary"  # or specific calendar ID
    credentials_file: "credentials/google_credentials.json"
    token_file: "credentials/google_token.pickle"

  outlook:
    enabled: false
    calendar_id: "Calendar"
    credentials_file: "credentials/outlook_credentials.json"

  ical:
    enabled: true
    export_path: "exports/life-os-calendar.ics"

# Sync settings
sync:
  frequency: "15min"  # How often to sync (5min, 15min, 30min, 1hour, manual)
  conflict_resolution: "manual-review"  # calendar-wins, todo-wins, manual-review
  backup_before_sync: true
  max_backups: 10

# TODO parsing
todo:
  file_pattern: "../../steps-e/daily-todo-*.md"
  time_block_marker: "## Time Blocks"
  goal_id_pattern: "\\[goal_id: ([a-z0-9-]+)\\]"

# Domain color mapping
colors:
  finance: "#0B8043"      # Green
  business: "#039BE5"     # Blue
  health: "#D50000"       # Red
  personal: "#F4B400"     # Yellow
  learning: "#7986CB"     # Purple
  default: "#616161"      # Gray

# Logging
logging:
  level: "INFO"  # DEBUG, INFO, WARNING, ERROR
  file: "logs/calendar-sync.log"
  console: true
```

### 3. Set Up OAuth Authentication

#### Google Calendar

1. **Create Google Cloud Project**
   ```bash
   # Run the OAuth setup helper
   python scripts/setup_google_oauth.py
   ```

   Or manually:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create new project or select existing
   - Enable Google Calendar API
   - Create OAuth 2.0 credentials (Desktop app)
   - Download credentials JSON file

2. **Save Credentials**
   ```bash
   mkdir -p credentials
   mv ~/Downloads/credentials.json credentials/google_credentials.json
   ```

3. **Initial Authentication**
   ```bash
   python calendar_sync.py --setup google
   ```

   This will:
   - Open browser for Google sign-in
   - Request calendar access permissions
   - Save refresh token to `google_token.pickle`

#### Microsoft Outlook

1. **Register Azure AD Application**
   ```bash
   python scripts/setup_outlook_oauth.py
   ```

   Or manually:
   - Go to [Azure Portal](https://portal.azure.com/)
   - Navigate to Azure Active Directory > App registrations
   - Create new registration
   - Add permissions: `Calendars.ReadWrite`
   - Create client secret
   - Note Application (client) ID and Directory (tenant) ID

2. **Save Credentials**

   Create `credentials/outlook_credentials.json`:
   ```json
   {
     "client_id": "your-application-id",
     "client_secret": "your-client-secret",
     "tenant_id": "your-tenant-id"
   }
   ```

3. **Initial Authentication**
   ```bash
   python calendar_sync.py --setup outlook
   ```

## Usage

### Basic Sync Operations

```bash
# Perform one-time sync
python calendar_sync.py --sync

# Dry-run mode (preview changes without applying)
python calendar_sync.py --sync --dry-run

# Sync specific date range
python calendar_sync.py --sync --start-date 2024-02-01 --end-date 2024-02-07

# Force full resync (ignore timestamps)
python calendar_sync.py --sync --force
```

### Continuous Monitoring

```bash
# Start sync daemon (runs in background)
python calendar_sync.py --daemon

# Check daemon status
python calendar_sync.py --status

# Stop daemon
python calendar_sync.py --stop
```

### Conflict Resolution

When conflicts are detected with `manual-review` mode:

```bash
# List pending conflicts
python calendar_sync.py --conflicts

# Resolve specific conflict
python calendar_sync.py --resolve <conflict_id> --choose calendar
python calendar_sync.py --resolve <conflict_id> --choose todo
python calendar_sync.py --resolve <conflict_id> --merge
```

### Weekly View Generation

```bash
# Generate weekly calendar view
python calendar_sync.py --weekly-view

# Export to HTML
python calendar_sync.py --weekly-view --format html --output weekly-calendar.html

# Export to PDF
python calendar_sync.py --weekly-view --format pdf --output weekly-calendar.pdf
```

### Backup and Restore

```bash
# Create manual backup
python calendar_sync.py --backup

# List available backups
python calendar_sync.py --list-backups

# Restore from backup
python calendar_sync.py --restore <backup_id>

# Rollback last sync
python calendar_sync.py --rollback
```

## TODO Time Block Format

The sync system parses TODO files with this structure:

```markdown
# Daily TODO - 2024-02-05

## Time Blocks

### 09:00-10:30 | Strategic Planning [goal_id: finance-q1-review]
**Domain:** finance
**Priority:** high

- Review Q1 financial reports
- Identify cost optimization opportunities
- Prepare presentation for board meeting

**Expected Outcomes:**
- Financial analysis completed
- 3-5 actionable recommendations documented

---

### 11:00-12:00 | Client Meeting - Acme Corp [goal_id: business-acme-contract]
**Domain:** business
**Priority:** critical

- Present proposal for new contract
- Negotiate terms and pricing
- Close deal if possible

**Expected Outcomes:**
- Contract signed or clear next steps identified

---

### 14:00-15:30 | Gym Session [goal_id: health-fitness-routine]
**Domain:** health
**Priority:** medium

- Strength training (upper body)
- 20 min cardio
- Stretching

**Expected Outcomes:**
- Workout completed according to plan
```

### Parsed Event Details

Each time block is converted to:
- **Title:** "Strategic Planning" (prefix removed)
- **Start:** 2024-02-05 09:00
- **End:** 2024-02-05 10:30
- **Description:** Full markdown content including tasks and outcomes
- **Color:** Green (finance domain)
- **Metadata:**
  - `goal_id`: finance-q1-review
  - `domain`: finance
  - `priority`: high
  - `sync_source`: life-os
  - `sync_timestamp`: 2024-02-05T08:00:00Z

## Two-Way Sync Behavior

### TODO → Calendar

When a TODO time block is created or modified:

1. **New Event:** Create calendar event with all metadata
2. **Updated Event:** Update existing calendar event if `goal_id` matches
3. **Deleted Block:** Mark calendar event as "CANCELLED" (not deleted, for audit)

### Calendar → TODO

When a calendar event is modified externally:

1. **Time Changed:** Update time block in TODO file
2. **Title Changed:** Update time block header
3. **Event Deleted:** Add strikethrough to TODO time block
4. **Event Created:** Add new time block to TODO (if has `sync_source: life-os` metadata)

**Note:** Only events with Life OS metadata are synced back to prevent pollution from unrelated calendar events.

## Conflict Resolution Strategies

### calendar-wins

- Changes in calendar always override TODO
- Fast, automatic
- Risk: Lose TODO updates if calendar modified simultaneously

### todo-wins

- Changes in TODO always override calendar
- Preserves Life OS as authoritative source
- Risk: Lose external calendar updates

### manual-review (Default)

- Conflicts are logged for manual resolution
- User chooses which version to keep or merges both
- Safest option, requires user intervention

### Example Conflict

```
CONFLICT DETECTED: Event ID cal-123 / goal_id finance-q1-review

Calendar Version:
  Time: 09:00-10:00 (changed from 09:00-10:30)
  Title: "Strategic Planning Session" (added "Session")
  Modified: 2024-02-05 08:45:00

TODO Version:
  Time: 09:00-10:30 (original)
  Title: "Strategic Planning"
  Modified: 2024-02-05 08:50:00

Choose resolution:
[C] Use Calendar version
[T] Use TODO version
[M] Merge (use TODO title, Calendar time)
[S] Skip (resolve later)
```

## Color Coding System

Events are automatically color-coded based on domain:

| Domain | Color | Hex | Purpose |
|--------|-------|-----|---------|
| Finance | Green | #0B8043 | Financial planning, budgeting, investments |
| Business | Blue | #039BE5 | Work projects, meetings, client interactions |
| Health | Red | #D50000 | Exercise, medical appointments, wellness |
| Personal | Yellow | #F4B400 | Family time, hobbies, personal development |
| Learning | Purple | #7986CB | Study, courses, skill development |
| Default | Gray | #616161 | Unclassified or mixed domain |

Colors are applied during event creation and updated if domain changes.

## Weekly View

The weekly view generator creates a visual summary:

```bash
python calendar_sync.py --weekly-view --format html
```

**Output includes:**
- Calendar grid with color-coded events
- Domain breakdown (time spent per domain)
- Goal progress indicators
- Unscheduled vs scheduled time
- Conflict warnings

**Example HTML Output:**

```html
<!DOCTYPE html>
<html>
<head><title>Life OS Weekly Calendar</title></head>
<body>
  <h1>Week of February 5-11, 2024</h1>

  <div class="calendar-grid">
    <!-- Interactive calendar view -->
  </div>

  <div class="domain-breakdown">
    <h2>Time by Domain</h2>
    <ul>
      <li>Finance: 12.5 hours (25%)</li>
      <li>Business: 20.0 hours (40%)</li>
      <li>Health: 7.5 hours (15%)</li>
      <li>Personal: 5.0 hours (10%)</li>
      <li>Learning: 5.0 hours (10%)</li>
    </ul>
  </div>

  <div class="goal-progress">
    <!-- Goal completion indicators -->
  </div>
</body>
</html>
```

## Error Handling

### Common Errors

**Authentication Errors:**
```
ERROR: Google Calendar authentication failed
Solution: Re-run 'python calendar_sync.py --setup google'
```

**Rate Limiting:**
```
WARNING: Google Calendar API rate limit exceeded. Retry in 60 seconds.
Solution: Reduce sync frequency in config or wait for quota reset
```

**Malformed TODO:**
```
ERROR: Could not parse time block in daily-todo-2024-02-05.md line 45
Solution: Check time format (HH:MM-HH:MM) and goal_id syntax
```

### Logging

All operations are logged to `logs/calendar-sync.log`:

```
2024-02-05 09:00:15 INFO Starting sync operation
2024-02-05 09:00:16 INFO Parsed 12 time blocks from daily-todo-2024-02-05.md
2024-02-05 09:00:17 INFO Created 3 new calendar events
2024-02-05 09:00:18 INFO Updated 8 existing events
2024-02-05 09:00:19 WARNING Conflict detected for goal_id: finance-q1-review
2024-02-05 09:00:20 INFO Sync completed successfully
```

Enable debug logging for troubleshooting:
```yaml
logging:
  level: "DEBUG"
```

## Security Best Practices

1. **Credential Storage**
   - Never commit credentials to version control
   - Add to `.gitignore`:
     ```
     credentials/
     *.pickle
     calendar-sync-config.yaml
     ```

2. **OAuth Tokens**
   - Tokens are stored encrypted
   - Automatic refresh before expiration
   - Revoke access from Google/Microsoft console if compromised

3. **Sensitive Data**
   - Event descriptions may contain sensitive information
   - Ensure calendar permissions are properly configured
   - Use private calendars for personal data

4. **API Keys**
   - Rotate API keys periodically
   - Use separate credentials for development/production
   - Monitor API usage for anomalies

## Troubleshooting

### Sync Not Working

1. Check daemon status: `python calendar_sync.py --status`
2. Verify credentials: `python calendar_sync.py --test-auth`
3. Review logs: `tail -f logs/calendar-sync.log`
4. Test with dry-run: `python calendar_sync.py --sync --dry-run`

### Events Not Appearing

1. Verify calendar_id in config matches target calendar
2. Check if events have required metadata (goal_id)
3. Ensure time blocks follow correct format
4. Check for parsing errors in logs

### Conflicts Not Resolving

1. Check conflict resolution strategy in config
2. List pending conflicts: `python calendar_sync.py --conflicts`
3. Manually resolve: `python calendar_sync.py --resolve <id> --choose todo`

### Performance Issues

1. Reduce sync frequency in config
2. Limit date range: `--start-date` and `--end-date`
3. Enable caching (experimental): `sync.enable_cache: true`
4. Use incremental sync: `--incremental` (only changes since last sync)

## Advanced Features

### Custom Parsers

Extend TODO parsing for custom formats:

```python
# In calendar_sync.py
from parsers import CustomTODOParser

sync_manager.register_parser(CustomTODOParser)
```

### Webhook Integration

Receive real-time updates from calendar:

```bash
# Start webhook server
python calendar_sync.py --webhook --port 8080

# Configure Google Calendar push notifications
# (See scripts/setup_webhook.py for details)
```

### Batch Operations

Sync multiple TODO files at once:

```bash
python calendar_sync.py --batch --pattern "steps-e/daily-todo-2024-02-*.md"
```

### Custom Color Schemes

Override default colors in config:

```yaml
colors:
  finance: "#00FF00"  # Bright green
  business: "#0000FF"  # Pure blue
  custom_domain: "#FF00FF"  # Magenta
```

## API Reference

### CalendarSyncManager

Main orchestrator class:

```python
from calendar_sync import CalendarSyncManager

manager = CalendarSyncManager(config_path="calendar-sync-config.yaml")

# Sync operations
manager.sync(dry_run=False, force=False)
manager.sync_date_range(start_date, end_date)

# Conflict resolution
conflicts = manager.get_conflicts()
manager.resolve_conflict(conflict_id, strategy="todo-wins")

# Weekly view
weekly_html = manager.generate_weekly_view(format="html")
```

### Providers

```python
from providers import GoogleCalendarProvider, OutlookCalendarProvider

# Google Calendar
google = GoogleCalendarProvider(credentials_file, token_file)
events = google.list_events(start_date, end_date)
google.create_event(event_data)

# Outlook Calendar
outlook = OutlookCalendarProvider(credentials_file)
events = outlook.list_events(start_date, end_date)
outlook.update_event(event_id, updated_data)
```

## Roadmap

### Planned Features

- [ ] Mobile app integration (iOS/Android)
- [ ] Slack notifications for conflicts
- [ ] AI-powered time block suggestions
- [ ] Multi-user sync (family/team calendars)
- [ ] Timezone-aware scheduling
- [ ] Recurring event support
- [ ] Natural language parsing ("tomorrow at 3pm")
- [ ] Integration with task management tools (Todoist, Asana)

### Version History

- **v1.0.0** (Current) - Initial release
  - Google Calendar and Outlook support
  - Two-way sync with conflict resolution
  - Color coding by domain
  - Weekly view generation

## Support

For issues, questions, or feature requests:

1. Check existing documentation
2. Review logs for error details
3. Search GitHub issues
4. Create new issue with:
   - System information (OS, Python version)
   - Config file (redact sensitive data)
   - Relevant log entries
   - Steps to reproduce

## License

This Calendar Sync integration is part of the Life OS workflow system.
See main project license for terms and conditions.

---

**Last Updated:** 2024-02-05
**Maintained By:** Life OS Development Team
**Version:** 1.0.0
