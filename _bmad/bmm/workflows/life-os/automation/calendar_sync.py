#!/usr/bin/env python3
"""
Calendar Sync Integration System
Synchronizes Life OS TODO time blocks with Google Calendar, Outlook, and iCal

Usage:
    python calendar_sync.py --sync                          # One-time sync
    python calendar_sync.py --sync --dry-run               # Preview changes
    python calendar_sync.py --daemon                       # Start background sync
    python calendar_sync.py --weekly-view                  # Generate weekly view
    python calendar_sync.py --setup google                 # Initial OAuth setup
"""

import argparse
import logging
import sys
import yaml
import pickle
import os
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import time
import hashlib

# Calendar provider imports
try:
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False
    logging.warning("Google Calendar dependencies not installed. Run: pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib")

try:
    from O365 import Account
    OUTLOOK_AVAILABLE = True
except ImportError:
    OUTLOOK_AVAILABLE = False
    logging.warning("Outlook dependencies not installed. Run: pip install O365")

try:
    from icalendar import Calendar, Event as ICalEvent
    ICAL_AVAILABLE = True
except ImportError:
    ICAL_AVAILABLE = False
    logging.warning("iCal dependencies not installed. Run: pip install icalendar")

# Constants
SCOPES_GOOGLE = ['https://www.googleapis.com/auth/calendar']
SCOPES_OUTLOOK = ['Calendars.ReadWrite']

@dataclass
class TimeBlock:
    """Represents a parsed TODO time block"""
    title: str
    start_time: datetime
    end_time: datetime
    domain: str
    priority: str
    goal_id: str
    description: str
    tasks: List[str]
    expected_outcomes: List[str]
    source_file: str
    line_number: int
    hash: str = ""

    def __post_init__(self):
        """Generate hash for change detection"""
        if not self.hash:
            content = f"{self.title}|{self.start_time}|{self.end_time}|{self.domain}|{self.description}"
            self.hash = hashlib.md5(content.encode()).hexdigest()

@dataclass
class CalendarEvent:
    """Represents a calendar event"""
    event_id: str
    title: str
    start_time: datetime
    end_time: datetime
    description: str
    color: str
    metadata: Dict
    provider: str  # 'google', 'outlook', 'ical'
    last_modified: datetime
    hash: str = ""

    def __post_init__(self):
        """Generate hash for change detection"""
        if not self.hash:
            content = f"{self.title}|{self.start_time}|{self.end_time}|{self.description}"
            self.hash = hashlib.md5(content.encode()).hexdigest()

@dataclass
class SyncConflict:
    """Represents a sync conflict between TODO and calendar"""
    conflict_id: str
    goal_id: str
    todo_version: TimeBlock
    calendar_version: CalendarEvent
    detected_at: datetime
    resolved: bool = False
    resolution: Optional[str] = None

class ColorMapper:
    """Maps domains to calendar colors"""

    DEFAULT_COLORS = {
        'finance': '#0B8043',    # Green
        'business': '#039BE5',   # Blue
        'health': '#D50000',     # Red
        'personal': '#F4B400',   # Yellow
        'learning': '#7986CB',   # Purple
        'default': '#616161'     # Gray
    }

    def __init__(self, custom_colors: Optional[Dict] = None):
        self.colors = {**self.DEFAULT_COLORS}
        if custom_colors:
            self.colors.update(custom_colors)

    def get_color(self, domain: str) -> str:
        """Get color hex code for domain"""
        return self.colors.get(domain.lower(), self.colors['default'])

    def get_google_color_id(self, domain: str) -> str:
        """Map domain to Google Calendar color ID"""
        color_mapping = {
            'finance': '10',    # Green
            'business': '9',    # Blue
            'health': '11',     # Red
            'personal': '5',    # Yellow
            'learning': '3',    # Purple
            'default': '8'      # Gray
        }
        return color_mapping.get(domain.lower(), color_mapping['default'])

class TODOParser:
    """Parse Life OS TODO files to extract time blocks"""

    def __init__(self, config: Dict):
        self.config = config
        self.time_block_pattern = re.compile(
            r'###\s+(\d{2}:\d{2})-(\d{2}:\d{2})\s*\|\s*(.+?)\s*\[goal_id:\s*([a-z0-9-]+)\]'
        )
        self.domain_pattern = re.compile(r'\*\*Domain:\*\*\s+(\w+)')
        self.priority_pattern = re.compile(r'\*\*Priority:\*\*\s+(\w+)')

    def parse_file(self, file_path: Path, date: datetime) -> List[TimeBlock]:
        """Parse a TODO file and extract time blocks"""
        time_blocks = []

        if not file_path.exists():
            logging.warning(f"TODO file not found: {file_path}")
            return time_blocks

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find time blocks section
            time_blocks_section = self._extract_time_blocks_section(content)
            if not time_blocks_section:
                logging.info(f"No time blocks section found in {file_path}")
                return time_blocks

            # Split into individual blocks
            blocks = time_blocks_section.split('---')

            for block_idx, block in enumerate(blocks):
                block = block.strip()
                if not block:
                    continue

                time_block = self._parse_time_block(block, file_path, date, block_idx)
                if time_block:
                    time_blocks.append(time_block)

        except Exception as e:
            logging.error(f"Error parsing TODO file {file_path}: {e}")

        return time_blocks

    def _extract_time_blocks_section(self, content: str) -> Optional[str]:
        """Extract the time blocks section from TODO content"""
        marker = self.config.get('todo', {}).get('time_block_marker', '## Time Blocks')

        if marker not in content:
            return None

        # Get content after marker
        parts = content.split(marker, 1)
        if len(parts) < 2:
            return None

        # Get content until next ## section or end
        time_blocks_content = parts[1]
        next_section = re.search(r'\n##[^#]', time_blocks_content)
        if next_section:
            time_blocks_content = time_blocks_content[:next_section.start()]

        return time_blocks_content

    def _parse_time_block(self, block: str, file_path: Path, date: datetime, line_offset: int) -> Optional[TimeBlock]:
        """Parse individual time block"""
        try:
            # Extract header (time and title)
            match = self.time_block_pattern.search(block)
            if not match:
                logging.debug(f"Could not parse time block header in {file_path}")
                return None

            start_time_str, end_time_str, title, goal_id = match.groups()

            # Parse times
            start_time = self._parse_time(date, start_time_str)
            end_time = self._parse_time(date, end_time_str)

            # Extract domain and priority
            domain_match = self.domain_pattern.search(block)
            domain = domain_match.group(1) if domain_match else 'default'

            priority_match = self.priority_pattern.search(block)
            priority = priority_match.group(1) if priority_match else 'medium'

            # Extract tasks
            tasks = self._extract_list_items(block, before_marker='**Expected Outcomes:**')

            # Extract expected outcomes
            outcomes = self._extract_list_items(block, after_marker='**Expected Outcomes:**')

            return TimeBlock(
                title=title.strip(),
                start_time=start_time,
                end_time=end_time,
                domain=domain,
                priority=priority,
                goal_id=goal_id,
                description=block,
                tasks=tasks,
                expected_outcomes=outcomes,
                source_file=str(file_path),
                line_number=line_offset
            )

        except Exception as e:
            logging.error(f"Error parsing time block: {e}")
            return None

    def _parse_time(self, date: datetime, time_str: str) -> datetime:
        """Parse time string (HH:MM) and combine with date"""
        hours, minutes = map(int, time_str.split(':'))
        return date.replace(hour=hours, minute=minutes, second=0, microsecond=0)

    def _extract_list_items(self, text: str, before_marker: Optional[str] = None,
                           after_marker: Optional[str] = None) -> List[str]:
        """Extract bullet point items from text"""
        # Constrain text to section if markers provided
        if after_marker and after_marker in text:
            text = text.split(after_marker, 1)[1]
        if before_marker and before_marker in text:
            text = text.split(before_marker, 1)[0]

        # Extract list items
        items = []
        for line in text.split('\n'):
            line = line.strip()
            if line.startswith('- ') or line.startswith('* '):
                items.append(line[2:].strip())

        return items

class CalendarProvider:
    """Base class for calendar providers"""

    def authenticate(self):
        """Authenticate with calendar service"""
        raise NotImplementedError

    def list_events(self, start_date: datetime, end_date: datetime) -> List[CalendarEvent]:
        """List events in date range"""
        raise NotImplementedError

    def create_event(self, time_block: TimeBlock, color: str) -> CalendarEvent:
        """Create calendar event from time block"""
        raise NotImplementedError

    def update_event(self, event: CalendarEvent, time_block: TimeBlock, color: str) -> CalendarEvent:
        """Update existing calendar event"""
        raise NotImplementedError

    def delete_event(self, event_id: str):
        """Delete calendar event"""
        raise NotImplementedError

class GoogleCalendarProvider(CalendarProvider):
    """Google Calendar integration"""

    def __init__(self, credentials_file: str, token_file: str, calendar_id: str = 'primary'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.calendar_id = calendar_id
        self.service = None
        self.color_mapper = ColorMapper()

    def authenticate(self):
        """Authenticate with Google Calendar API"""
        if not GOOGLE_AVAILABLE:
            raise RuntimeError("Google Calendar dependencies not installed")

        creds = None

        # Load token if exists
        if os.path.exists(self.token_file):
            with open(self.token_file, 'rb') as token:
                creds = pickle.load(token)

        # Refresh or get new credentials
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES_GOOGLE)
                creds = flow.run_local_server(port=0)

            # Save credentials
            with open(self.token_file, 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)
        logging.info("Google Calendar authenticated successfully")

    def list_events(self, start_date: datetime, end_date: datetime) -> List[CalendarEvent]:
        """List Google Calendar events"""
        if not self.service:
            self.authenticate()

        events_result = self.service.events().list(
            calendarId=self.calendar_id,
            timeMin=start_date.isoformat() + 'Z',
            timeMax=end_date.isoformat() + 'Z',
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = []
        for item in events_result.get('items', []):
            # Only sync events with Life OS metadata
            extended_props = item.get('extendedProperties', {}).get('private', {})
            if extended_props.get('sync_source') != 'life-os':
                continue

            events.append(self._convert_to_calendar_event(item))

        return events

    def create_event(self, time_block: TimeBlock, color: str) -> CalendarEvent:
        """Create Google Calendar event"""
        if not self.service:
            self.authenticate()

        event_body = {
            'summary': time_block.title,
            'description': time_block.description,
            'start': {'dateTime': time_block.start_time.isoformat(), 'timeZone': 'UTC'},
            'end': {'dateTime': time_block.end_time.isoformat(), 'timeZone': 'UTC'},
            'colorId': self.color_mapper.get_google_color_id(time_block.domain),
            'extendedProperties': {
                'private': {
                    'sync_source': 'life-os',
                    'goal_id': time_block.goal_id,
                    'domain': time_block.domain,
                    'priority': time_block.priority,
                    'sync_timestamp': datetime.utcnow().isoformat(),
                    'hash': time_block.hash
                }
            }
        }

        event = self.service.events().insert(
            calendarId=self.calendar_id,
            body=event_body
        ).execute()

        logging.info(f"Created Google Calendar event: {event['id']} - {time_block.title}")
        return self._convert_to_calendar_event(event)

    def update_event(self, event: CalendarEvent, time_block: TimeBlock, color: str) -> CalendarEvent:
        """Update Google Calendar event"""
        if not self.service:
            self.authenticate()

        event_body = {
            'summary': time_block.title,
            'description': time_block.description,
            'start': {'dateTime': time_block.start_time.isoformat(), 'timeZone': 'UTC'},
            'end': {'dateTime': time_block.end_time.isoformat(), 'timeZone': 'UTC'},
            'colorId': self.color_mapper.get_google_color_id(time_block.domain),
            'extendedProperties': {
                'private': {
                    **event.metadata,
                    'sync_timestamp': datetime.utcnow().isoformat(),
                    'hash': time_block.hash
                }
            }
        }

        updated_event = self.service.events().update(
            calendarId=self.calendar_id,
            eventId=event.event_id,
            body=event_body
        ).execute()

        logging.info(f"Updated Google Calendar event: {event.event_id} - {time_block.title}")
        return self._convert_to_calendar_event(updated_event)

    def delete_event(self, event_id: str):
        """Delete Google Calendar event"""
        if not self.service:
            self.authenticate()

        self.service.events().delete(
            calendarId=self.calendar_id,
            eventId=event_id
        ).execute()

        logging.info(f"Deleted Google Calendar event: {event_id}")

    def _convert_to_calendar_event(self, google_event: Dict) -> CalendarEvent:
        """Convert Google Calendar event to CalendarEvent"""
        extended_props = google_event.get('extendedProperties', {}).get('private', {})

        start = google_event['start'].get('dateTime', google_event['start'].get('date'))
        end = google_event['end'].get('dateTime', google_event['end'].get('date'))

        return CalendarEvent(
            event_id=google_event['id'],
            title=google_event.get('summary', ''),
            start_time=datetime.fromisoformat(start.replace('Z', '+00:00')),
            end_time=datetime.fromisoformat(end.replace('Z', '+00:00')),
            description=google_event.get('description', ''),
            color=google_event.get('colorId', '8'),
            metadata=extended_props,
            provider='google',
            last_modified=datetime.fromisoformat(google_event['updated'].replace('Z', '+00:00'))
        )

class OutlookCalendarProvider(CalendarProvider):
    """Microsoft Outlook/Office 365 integration"""

    def __init__(self, credentials_file: str, calendar_id: str = 'Calendar'):
        self.credentials_file = credentials_file
        self.calendar_id = calendar_id
        self.account = None
        self.color_mapper = ColorMapper()

    def authenticate(self):
        """Authenticate with Microsoft Graph API"""
        if not OUTLOOK_AVAILABLE:
            raise RuntimeError("Outlook dependencies not installed")

        # Load credentials
        with open(self.credentials_file, 'r') as f:
            creds = json.load(f)

        credentials = (creds['client_id'], creds['client_secret'])

        self.account = Account(credentials, auth_flow_type='credentials', tenant_id=creds['tenant_id'])

        if not self.account.is_authenticated:
            if self.account.authenticate(scopes=SCOPES_OUTLOOK):
                logging.info("Outlook authenticated successfully")
            else:
                raise RuntimeError("Outlook authentication failed")

    def list_events(self, start_date: datetime, end_date: datetime) -> List[CalendarEvent]:
        """List Outlook calendar events"""
        if not self.account or not self.account.is_authenticated:
            self.authenticate()

        schedule = self.account.schedule()
        calendar = schedule.get_calendar(calendar_name=self.calendar_id)

        query = calendar.new_query('start').greater_equal(start_date)
        query.chain('and').on_attribute('end').less_equal(end_date)

        events = []
        for event in calendar.get_events(query=query, include_recurring=False):
            # Only sync events with Life OS metadata
            if event.categories and 'life-os' in event.categories:
                events.append(self._convert_to_calendar_event(event))

        return events

    def create_event(self, time_block: TimeBlock, color: str) -> CalendarEvent:
        """Create Outlook calendar event"""
        if not self.account or not self.account.is_authenticated:
            self.authenticate()

        schedule = self.account.schedule()
        calendar = schedule.get_calendar(calendar_name=self.calendar_id)

        event = calendar.new_event()
        event.subject = time_block.title
        event.body = time_block.description
        event.start = time_block.start_time
        event.end = time_block.end_time
        event.categories = ['life-os', time_block.domain, time_block.priority]

        # Store metadata in body (Outlook has limited custom properties)
        metadata_json = json.dumps({
            'goal_id': time_block.goal_id,
            'domain': time_block.domain,
            'priority': time_block.priority,
            'sync_timestamp': datetime.utcnow().isoformat(),
            'hash': time_block.hash
        })
        event.body = f"{time_block.description}\n\n<!-- metadata: {metadata_json} -->"

        event.save()

        logging.info(f"Created Outlook event: {event.object_id} - {time_block.title}")
        return self._convert_to_calendar_event(event)

    def update_event(self, event: CalendarEvent, time_block: TimeBlock, color: str) -> CalendarEvent:
        """Update Outlook calendar event"""
        # Implementation similar to create_event
        pass

    def delete_event(self, event_id: str):
        """Delete Outlook calendar event"""
        # Implementation for Outlook delete
        pass

    def _convert_to_calendar_event(self, outlook_event) -> CalendarEvent:
        """Convert Outlook event to CalendarEvent"""
        # Extract metadata from body
        metadata = {}
        if '<!-- metadata:' in outlook_event.body:
            metadata_str = outlook_event.body.split('<!-- metadata:')[1].split('-->')[0].strip()
            try:
                metadata = json.loads(metadata_str)
            except json.JSONDecodeError:
                pass

        return CalendarEvent(
            event_id=outlook_event.object_id,
            title=outlook_event.subject,
            start_time=outlook_event.start,
            end_time=outlook_event.end,
            description=outlook_event.body.split('<!-- metadata:')[0].strip(),
            color='',  # Outlook doesn't have colors
            metadata=metadata,
            provider='outlook',
            last_modified=outlook_event.modified
        )

class CalendarSyncManager:
    """Main orchestrator for calendar synchronization"""

    def __init__(self, config_path: str = 'calendar-sync-config.yaml'):
        self.config = self._load_config(config_path)
        self.color_mapper = ColorMapper(self.config.get('colors', {}))
        self.todo_parser = TODOParser(self.config)
        self.providers = self._initialize_providers()
        self.conflicts = []

        self._setup_logging()

    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file"""
        config_file = Path(config_path)
        if not config_file.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_file, 'r') as f:
            return yaml.safe_load(f)

    def _setup_logging(self):
        """Setup logging based on config"""
        log_config = self.config.get('logging', {})
        log_level = getattr(logging, log_config.get('level', 'INFO'))
        log_file = log_config.get('file', 'logs/calendar-sync.log')

        # Create log directory if needed
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)

        handlers = []

        # File handler
        handlers.append(logging.FileHandler(log_file))

        # Console handler
        if log_config.get('console', True):
            handlers.append(logging.StreamHandler(sys.stdout))

        logging.basicConfig(
            level=log_level,
            format='%(asctime)s %(levelname)s %(message)s',
            handlers=handlers
        )

    def _initialize_providers(self) -> Dict[str, CalendarProvider]:
        """Initialize enabled calendar providers"""
        providers = {}
        provider_config = self.config.get('providers', {})

        # Google Calendar
        if provider_config.get('google', {}).get('enabled'):
            google_config = provider_config['google']
            providers['google'] = GoogleCalendarProvider(
                credentials_file=google_config['credentials_file'],
                token_file=google_config['token_file'],
                calendar_id=google_config.get('calendar_id', 'primary')
            )
            logging.info("Google Calendar provider initialized")

        # Outlook Calendar
        if provider_config.get('outlook', {}).get('enabled'):
            outlook_config = provider_config['outlook']
            providers['outlook'] = OutlookCalendarProvider(
                credentials_file=outlook_config['credentials_file'],
                calendar_id=outlook_config.get('calendar_id', 'Calendar')
            )
            logging.info("Outlook Calendar provider initialized")

        return providers

    def sync(self, dry_run: bool = False, force: bool = False,
             start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
        """Perform synchronization"""
        logging.info("Starting sync operation")

        if dry_run:
            logging.info("DRY RUN MODE - No changes will be applied")

        # Default to today
        if not start_date:
            start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        if not end_date:
            end_date = start_date + timedelta(days=1)

        # Backup if configured
        if self.config.get('sync', {}).get('backup_before_sync') and not dry_run:
            self._create_backup()

        # Get TODO time blocks
        time_blocks = self._get_time_blocks(start_date, end_date)
        logging.info(f"Parsed {len(time_blocks)} time blocks from TODO files")

        # Get calendar events
        calendar_events = self._get_calendar_events(start_date, end_date)
        logging.info(f"Retrieved {len(calendar_events)} calendar events")

        # Sync TODO → Calendar
        created, updated, deleted = self._sync_todo_to_calendar(
            time_blocks, calendar_events, dry_run, force
        )

        # Sync Calendar → TODO (if enabled)
        if self.config.get('sync', {}).get('bidirectional', True):
            self._sync_calendar_to_todo(calendar_events, time_blocks, dry_run)

        # Handle conflicts
        if self.conflicts:
            logging.warning(f"Detected {len(self.conflicts)} conflicts requiring resolution")
            self._handle_conflicts(dry_run)

        logging.info(f"Sync completed: {created} created, {updated} updated, {deleted} deleted")

    def _get_time_blocks(self, start_date: datetime, end_date: datetime) -> List[TimeBlock]:
        """Get time blocks from TODO files"""
        time_blocks = []

        # Get file pattern from config
        file_pattern = self.config.get('todo', {}).get('file_pattern', '../../steps-e/daily-todo-*.md')
        base_path = Path(__file__).parent

        # Iterate through date range
        current_date = start_date
        while current_date < end_date:
            date_str = current_date.strftime('%Y-%m-%d')
            file_path = base_path / file_pattern.replace('*', date_str)

            blocks = self.todo_parser.parse_file(file_path, current_date)
            time_blocks.extend(blocks)

            current_date += timedelta(days=1)

        return time_blocks

    def _get_calendar_events(self, start_date: datetime, end_date: datetime) -> List[CalendarEvent]:
        """Get events from all enabled providers"""
        all_events = []

        for provider_name, provider in self.providers.items():
            try:
                events = provider.list_events(start_date, end_date)
                all_events.extend(events)
                logging.info(f"Retrieved {len(events)} events from {provider_name}")
            except Exception as e:
                logging.error(f"Error retrieving events from {provider_name}: {e}")

        return all_events

    def _sync_todo_to_calendar(self, time_blocks: List[TimeBlock],
                               calendar_events: List[CalendarEvent],
                               dry_run: bool, force: bool) -> Tuple[int, int, int]:
        """Sync TODO time blocks to calendar"""
        created = 0
        updated = 0
        deleted = 0

        # Build event lookup by goal_id
        event_map = {
            event.metadata.get('goal_id'): event
            for event in calendar_events
            if event.metadata.get('goal_id')
        }

        # Process time blocks
        for block in time_blocks:
            existing_event = event_map.get(block.goal_id)

            if not existing_event:
                # Create new event
                if not dry_run:
                    for provider in self.providers.values():
                        color = self.color_mapper.get_color(block.domain)
                        provider.create_event(block, color)
                created += 1
                logging.info(f"[CREATE] {block.title} ({block.goal_id})")

            elif force or existing_event.hash != block.hash:
                # Update existing event if changed
                if self._detect_conflict(existing_event, block):
                    self.conflicts.append(SyncConflict(
                        conflict_id=f"conflict-{len(self.conflicts)}",
                        goal_id=block.goal_id,
                        todo_version=block,
                        calendar_version=existing_event,
                        detected_at=datetime.now()
                    ))
                else:
                    if not dry_run:
                        provider = self.providers.get(existing_event.provider)
                        if provider:
                            color = self.color_mapper.get_color(block.domain)
                            provider.update_event(existing_event, block, color)
                    updated += 1
                    logging.info(f"[UPDATE] {block.title} ({block.goal_id})")

            # Remove from map
            event_map.pop(block.goal_id, None)

        # Delete events not in TODO (cancelled blocks)
        for goal_id, event in event_map.items():
            if not dry_run:
                provider = self.providers.get(event.provider)
                if provider:
                    provider.delete_event(event.event_id)
            deleted += 1
            logging.info(f"[DELETE] {event.title} ({goal_id})")

        return created, updated, deleted

    def _sync_calendar_to_todo(self, calendar_events: List[CalendarEvent],
                               time_blocks: List[TimeBlock], dry_run: bool):
        """Sync calendar changes back to TODO (placeholder)"""
        # This would require TODO file modification logic
        # For now, just log what would be done
        logging.info("Calendar → TODO sync not yet implemented")

    def _detect_conflict(self, calendar_event: CalendarEvent, time_block: TimeBlock) -> bool:
        """Detect if there's a sync conflict"""
        # Check if both were modified after last sync
        sync_timestamp_str = calendar_event.metadata.get('sync_timestamp')
        if not sync_timestamp_str:
            return False

        sync_timestamp = datetime.fromisoformat(sync_timestamp_str)

        # If calendar was modified after sync and hashes differ, it's a conflict
        if calendar_event.last_modified > sync_timestamp and calendar_event.hash != time_block.hash:
            return True

        return False

    def _handle_conflicts(self, dry_run: bool):
        """Handle conflicts based on resolution strategy"""
        strategy = self.config.get('sync', {}).get('conflict_resolution', 'manual-review')

        if strategy == 'manual-review':
            logging.info(f"Conflicts require manual resolution. Run: python calendar_sync.py --conflicts")
            return

        for conflict in self.conflicts:
            if strategy == 'calendar-wins':
                # Use calendar version
                logging.info(f"Resolving conflict {conflict.conflict_id}: Using calendar version")
                # Would update TODO here
            elif strategy == 'todo-wins':
                # Use TODO version
                logging.info(f"Resolving conflict {conflict.conflict_id}: Using TODO version")
                # Would update calendar here

    def _create_backup(self):
        """Create backup before sync"""
        backup_dir = Path('backups')
        backup_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = backup_dir / f'backup_{timestamp}.json'

        # Save current state (simplified)
        backup_data = {
            'timestamp': timestamp,
            'conflicts': [asdict(c) for c in self.conflicts]
        }

        with open(backup_path, 'w') as f:
            json.dump(backup_data, f, indent=2, default=str)

        logging.info(f"Backup created: {backup_path}")

        # Clean old backups
        max_backups = self.config.get('sync', {}).get('max_backups', 10)
        backups = sorted(backup_dir.glob('backup_*.json'))
        if len(backups) > max_backups:
            for old_backup in backups[:-max_backups]:
                old_backup.unlink()
                logging.info(f"Deleted old backup: {old_backup}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Life OS Calendar Sync')
    parser.add_argument('--sync', action='store_true', help='Perform sync operation')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without applying')
    parser.add_argument('--force', action='store_true', help='Force full resync')
    parser.add_argument('--setup', choices=['google', 'outlook'], help='Run OAuth setup')
    parser.add_argument('--daemon', action='store_true', help='Start sync daemon')
    parser.add_argument('--status', action='store_true', help='Check daemon status')
    parser.add_argument('--conflicts', action='store_true', help='List pending conflicts')
    parser.add_argument('--weekly-view', action='store_true', help='Generate weekly view')
    parser.add_argument('--config', default='calendar-sync-config.yaml', help='Config file path')

    args = parser.parse_args()

    try:
        manager = CalendarSyncManager(config_path=args.config)

        if args.setup:
            # Run OAuth setup
            if args.setup == 'google' and 'google' in manager.providers:
                manager.providers['google'].authenticate()
                print("Google Calendar setup complete!")
            elif args.setup == 'outlook' and 'outlook' in manager.providers:
                manager.providers['outlook'].authenticate()
                print("Outlook Calendar setup complete!")

        elif args.sync:
            manager.sync(dry_run=args.dry_run, force=args.force)

        elif args.conflicts:
            if manager.conflicts:
                print(f"\nPending Conflicts: {len(manager.conflicts)}\n")
                for conflict in manager.conflicts:
                    print(f"ID: {conflict.conflict_id}")
                    print(f"Goal: {conflict.goal_id}")
                    print(f"TODO: {conflict.todo_version.title}")
                    print(f"Calendar: {conflict.calendar_version.title}")
                    print("---")
            else:
                print("No pending conflicts")

        elif args.weekly_view:
            print("Weekly view generation not yet implemented")

        else:
            parser.print_help()

    except Exception as e:
        logging.error(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
