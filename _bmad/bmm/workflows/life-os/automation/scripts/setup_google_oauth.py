#!/usr/bin/env python3
"""
Google Calendar OAuth Setup Helper

This script guides you through setting up Google Calendar API access:
1. Creating a Google Cloud project
2. Enabling the Calendar API
3. Creating OAuth credentials
4. Downloading credentials file

Usage:
    python scripts/setup_google_oauth.py
"""

import sys
from pathlib import Path

def print_step(step_num: int, title: str, content: str):
    """Print formatted step"""
    print(f"\n{'='*70}")
    print(f"STEP {step_num}: {title}")
    print(f"{'='*70}\n")
    print(content)

def main():
    print("""
╔══════════════════════════════════════════════════════════════════╗
║         Google Calendar OAuth Setup - Interactive Guide          ║
╚══════════════════════════════════════════════════════════════════╝
""")

    print_step(1, "Go to Google Cloud Console",
        """Open your web browser and navigate to:
https://console.cloud.google.com/

Sign in with your Google account that you want to use for calendar access.
""")

    input("Press ENTER when you're ready to continue...")

    print_step(2, "Create a New Project (or select existing)",
        """1. Click on the project dropdown at the top of the page
2. Click "NEW PROJECT"
3. Enter project name: "Life-OS-Calendar-Sync" (or your preferred name)
4. Click "CREATE"
5. Wait for project creation (this may take a few seconds)
6. Select your new project from the dropdown
""")

    input("Press ENTER when you're ready to continue...")

    print_step(3, "Enable Google Calendar API",
        """1. In the left sidebar, click "APIs & Services" → "Library"
   (or navigate to: https://console.cloud.google.com/apis/library)

2. In the search box, type "Google Calendar API"

3. Click on "Google Calendar API" in the results

4. Click the "ENABLE" button

5. Wait for the API to be enabled
""")

    input("Press ENTER when you're ready to continue...")

    print_step(4, "Configure OAuth Consent Screen",
        """1. Go to "APIs & Services" → "OAuth consent screen"
   (or navigate to: https://console.cloud.google.com/apis/credentials/consent)

2. Select "External" user type (unless you have Google Workspace)

3. Click "CREATE"

4. Fill in the required fields:
   - App name: Life OS Calendar Sync
   - User support email: [your email]
   - Developer contact: [your email]

5. Click "SAVE AND CONTINUE"

6. On "Scopes" page, click "ADD OR REMOVE SCOPES"

7. Filter for "Google Calendar API" and select:
   - .../auth/calendar (See, edit, share, and permanently delete all calendars)

8. Click "UPDATE" then "SAVE AND CONTINUE"

9. On "Test users" page, add your email address

10. Click "SAVE AND CONTINUE"

11. Review and click "BACK TO DASHBOARD"
""")

    input("Press ENTER when you're ready to continue...")

    print_step(5, "Create OAuth Credentials",
        """1. Go to "APIs & Services" → "Credentials"
   (or navigate to: https://console.cloud.google.com/apis/credentials)

2. Click "+ CREATE CREDENTIALS" at the top

3. Select "OAuth client ID"

4. If prompted, configure the consent screen (you may have done this already)

5. For "Application type", select "Desktop app"

6. Enter name: "Life OS Calendar Sync Desktop"

7. Click "CREATE"

8. A dialog will show your Client ID and Client Secret
   (You don't need to copy these - they're in the JSON file)

9. Click "OK" to dismiss the dialog
""")

    input("Press ENTER when you're ready to continue...")

    print_step(6, "Download Credentials",
        """1. In the "OAuth 2.0 Client IDs" section, find your newly created credential

2. Click the download icon (⬇) on the right side of the credential row

3. This will download a file named something like:
   "client_secret_XXXXX.apps.googleusercontent.com.json"

4. The file will be in your Downloads folder
""")

    input("Press ENTER when you're ready to continue...")

    print_step(7, "Save Credentials File",
        """Now we'll move the downloaded credentials file to the correct location.

Please enter the full path to the downloaded JSON file:
(Usually in your Downloads folder, named client_secret_*.json)
""")

    # Get credentials file path from user
    credentials_path = input("Credentials file path: ").strip().strip('"').strip("'")

    if not credentials_path:
        print("\nNo path provided. Please manually copy the file to:")
        print("  automation/credentials/google_credentials.json")
        return

    credentials_file = Path(credentials_path)

    if not credentials_file.exists():
        print(f"\nError: File not found: {credentials_path}")
        print("\nPlease manually copy the file to:")
        print("  automation/credentials/google_credentials.json")
        return

    # Create credentials directory
    target_dir = Path(__file__).parent.parent / 'credentials'
    target_dir.mkdir(exist_ok=True)

    # Copy file
    target_file = target_dir / 'google_credentials.json'

    try:
        import shutil
        shutil.copy(credentials_file, target_file)
        print(f"\n✓ Credentials saved to: {target_file}")
    except Exception as e:
        print(f"\nError copying file: {e}")
        print(f"\nPlease manually copy:")
        print(f"  FROM: {credentials_file}")
        print(f"  TO:   {target_file}")
        return

    print_step(8, "Test Authentication",
        """The credentials are saved! Now test the authentication:

Run the following command from the automation directory:

    python calendar_sync.py --setup google

This will:
1. Open your web browser
2. Ask you to sign in to Google
3. Request permission to access your calendar
4. Save the access token

After successful authentication, you can start using calendar sync!
""")

    print("\n" + "="*70)
    print("Setup complete! Next steps:")
    print("="*70)
    print("""
1. Run authentication test:
   python calendar_sync.py --setup google

2. Copy and configure the config file:
   cp calendar-sync-config.template.yaml calendar-sync-config.yaml

3. Run your first sync:
   python calendar_sync.py --sync --dry-run

4. If dry-run looks good, do actual sync:
   python calendar_sync.py --sync
""")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(0)
