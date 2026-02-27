#!/usr/bin/env python3
"""
Microsoft Outlook OAuth Setup Helper

This script guides you through setting up Microsoft Graph API access:
1. Registering an Azure AD application
2. Configuring API permissions
3. Creating client secret
4. Saving credentials

Usage:
    python scripts/setup_outlook_oauth.py
"""

import sys
import json
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
║        Microsoft Outlook OAuth Setup - Interactive Guide         ║
╚══════════════════════════════════════════════════════════════════╝
""")

    print_step(1, "Go to Azure Portal",
        """Open your web browser and navigate to:
https://portal.azure.com/

Sign in with your Microsoft account (personal or work/school).
""")

    input("Press ENTER when you're ready to continue...")

    print_step(2, "Navigate to Azure Active Directory",
        """1. In the Azure Portal, search for "Azure Active Directory" in the top search bar

2. Click on "Azure Active Directory" in the results

3. You should now be on the Azure AD Overview page
""")

    input("Press ENTER when you're ready to continue...")

    print_step(3, "Register a New Application",
        """1. In the left sidebar, click "App registrations"

2. Click "+ New registration" at the top

3. Fill in the registration form:
   - Name: Life OS Calendar Sync
   - Supported account types: Select one of:
     * "Accounts in any organizational directory and personal Microsoft accounts"
       (for personal Outlook/Microsoft 365)
     * "Accounts in this organizational directory only"
       (for work/school accounts)

   - Redirect URI: Leave blank for now (we'll use device code flow)

4. Click "Register"

5. You'll be taken to the app's Overview page
""")

    input("Press ENTER when you're ready to continue...")

    print_step(4, "Note Application IDs",
        """On the app Overview page, you'll see important information:

1. Copy and save these values (we'll need them later):
   - Application (client) ID: [a GUID like 12345678-1234-1234-1234-123456789abc]
   - Directory (tenant) ID: [another GUID]

Keep these safe - you'll enter them in a moment.
""")

    print("\nPlease enter the IDs you copied:")
    client_id = input("Application (client) ID: ").strip()
    tenant_id = input("Directory (tenant) ID: ").strip()

    if not client_id or not tenant_id:
        print("\nError: Both IDs are required. Please re-run the script.")
        return

    input("\nPress ENTER when you're ready to continue...")

    print_step(5, "Configure API Permissions",
        """1. In the left sidebar of your app, click "API permissions"

2. Click "+ Add a permission"

3. In the "Request API permissions" panel:
   - Click "Microsoft Graph"
   - Select "Delegated permissions"

4. Search for "Calendar" and expand the Calendars section

5. Check these permissions:
   ☑ Calendars.Read
   ☑ Calendars.ReadWrite

6. Click "Add permissions" at the bottom

7. Back on the API permissions page, click "Grant admin consent for [your organization]"
   (If this button is not available, you may need admin approval)

8. Confirm by clicking "Yes"

9. Wait for the status to show green checkmarks (✓ Granted for...)
""")

    input("Press ENTER when you're ready to continue...")

    print_step(6, "Create Client Secret",
        """1. In the left sidebar, click "Certificates & secrets"

2. Under "Client secrets" tab, click "+ New client secret"

3. Enter a description:
   - Description: Life OS Calendar Sync Secret

4. Select expiration:
   - Recommended: 24 months (you'll need to rotate it later)
   - Or: Custom date

5. Click "Add"

6. ⚠️ IMPORTANT: Copy the "Value" immediately!
   - This is your client secret
   - It will only be shown ONCE
   - You cannot retrieve it later (you'd have to create a new one)
""")

    print("\nPlease enter your client secret:")
    client_secret = input("Client secret (Value): ").strip()

    if not client_secret:
        print("\nError: Client secret is required. Please re-run the script.")
        return

    input("\nPress ENTER when you're ready to continue...")

    print_step(7, "Configure Authentication",
        """1. In the left sidebar, click "Authentication"

2. Under "Advanced settings", find "Allow public client flows"

3. Toggle "Enable the following mobile and desktop flows" to YES

4. Click "Save" at the top

This enables device code flow which is needed for desktop apps.
""")

    input("Press ENTER when you're ready to continue...")

    print_step(8, "Save Credentials",
        """Now we'll save your credentials to a configuration file.
""")

    # Create credentials directory
    target_dir = Path(__file__).parent.parent / 'credentials'
    target_dir.mkdir(exist_ok=True)

    # Create credentials file
    credentials = {
        "client_id": client_id,
        "client_secret": client_secret,
        "tenant_id": tenant_id,
        "authority": f"https://login.microsoftonline.com/{tenant_id}",
        "scopes": ["Calendars.ReadWrite"]
    }

    target_file = target_dir / 'outlook_credentials.json'

    try:
        with open(target_file, 'w') as f:
            json.dump(credentials, f, indent=2)
        print(f"\n✓ Credentials saved to: {target_file}")
    except Exception as e:
        print(f"\nError saving credentials: {e}")
        print("\nPlease manually create the file:")
        print(f"  Location: {target_file}")
        print(f"  Content:\n{json.dumps(credentials, indent=2)}")
        return

    print_step(9, "Test Authentication",
        """The credentials are saved! Now test the authentication:

First, make sure Outlook is enabled in your config:

1. Edit calendar-sync-config.yaml:
   providers:
     outlook:
       enabled: true  # Change this to true

2. Run authentication test:
   python calendar_sync.py --setup outlook

This will:
1. Prompt you to visit a URL and enter a device code
2. Sign in to your Microsoft account
3. Grant permissions
4. Save the access token

After successful authentication, you can start using calendar sync!
""")

    print("\n" + "="*70)
    print("Setup complete! Next steps:")
    print("="*70)
    print("""
1. Enable Outlook in config:
   Edit calendar-sync-config.yaml and set providers.outlook.enabled: true

2. Run authentication test:
   python calendar_sync.py --setup outlook

3. Run your first sync:
   python calendar_sync.py --sync --dry-run

4. If dry-run looks good, do actual sync:
   python calendar_sync.py --sync

⚠️ IMPORTANT SECURITY NOTES:
- Never commit outlook_credentials.json to version control
- Add it to .gitignore
- Rotate client secret every 24 months
- If secret is compromised, revoke it immediately in Azure Portal
""")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user.")
        sys.exit(0)
