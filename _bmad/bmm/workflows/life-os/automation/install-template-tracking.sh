#!/bin/bash
#
# Template Usage Tracking Installation Script
#
# Installs template usage tracking into claude-flow hooks
#
# Usage:
#   bash install-template-tracking.sh [--dry-run]
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOOKS_DIR="$HOME/.claude-flow/hooks"
DRY_RUN=false

# Parse arguments
if [[ "$1" == "--dry-run" ]]; then
  DRY_RUN=true
  echo "🔍 DRY RUN MODE - No changes will be made"
fi

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo ""
echo "======================================================================"
echo "  Template Usage Tracking Installation"
echo "======================================================================"
echo ""

# Step 1: Check prerequisites
echo "📋 Step 1: Checking prerequisites..."

if ! command -v node &> /dev/null; then
  echo -e "${RED}❌ Node.js not found. Please install Node.js v20+${NC}"
  exit 1
fi
echo -e "${GREEN}✓${NC} Node.js found: $(node --version)"

if ! command -v npx &> /dev/null; then
  echo -e "${RED}❌ npx not found. Please install npm${NC}"
  exit 1
fi
echo -e "${GREEN}✓${NC} npx found"

# Check claude-flow installation
if ! npx claude-flow@v3alpha --version &> /dev/null; then
  echo -e "${YELLOW}⚠️${NC}  claude-flow not found. Will be installed on first use"
else
  echo -e "${GREEN}✓${NC} claude-flow found: $(npx claude-flow@v3alpha --version 2>&1 | head -n1)"
fi

echo ""

# Step 2: Create hooks directory if needed
echo "📂 Step 2: Setting up hooks directory..."

if [ ! -d "$HOOKS_DIR" ]; then
  if [ "$DRY_RUN" = false ]; then
    mkdir -p "$HOOKS_DIR"
    echo -e "${GREEN}✓${NC} Created hooks directory: $HOOKS_DIR"
  else
    echo -e "${YELLOW}[DRY RUN]${NC} Would create: $HOOKS_DIR"
  fi
else
  echo -e "${GREEN}✓${NC} Hooks directory exists: $HOOKS_DIR"
fi

echo ""

# Step 3: Copy integration script
echo "📦 Step 3: Installing hook integration script..."

SOURCE_INTEGRATION="$SCRIPT_DIR/hooks-template-integration.js"
DEST_INTEGRATION="$HOOKS_DIR/hooks-template-integration.js"

if [ ! -f "$SOURCE_INTEGRATION" ]; then
  echo -e "${RED}❌ Integration script not found: $SOURCE_INTEGRATION${NC}"
  exit 1
fi

if [ "$DRY_RUN" = false ]; then
  cp "$SOURCE_INTEGRATION" "$DEST_INTEGRATION"
  echo -e "${GREEN}✓${NC} Copied integration script to: $DEST_INTEGRATION"
else
  echo -e "${YELLOW}[DRY RUN]${NC} Would copy: $SOURCE_INTEGRATION → $DEST_INTEGRATION"
fi

echo ""

# Step 4: Copy tracker script
echo "📦 Step 4: Installing template tracker..."

SOURCE_TRACKER="$SCRIPT_DIR/template-tracker.js"
DEST_TRACKER="$HOOKS_DIR/template-tracker.js"

if [ ! -f "$SOURCE_TRACKER" ]; then
  echo -e "${RED}❌ Tracker script not found: $SOURCE_TRACKER${NC}"
  exit 1
fi

if [ "$DRY_RUN" = false ]; then
  cp "$SOURCE_TRACKER" "$DEST_TRACKER"
  chmod +x "$DEST_TRACKER"
  echo -e "${GREEN}✓${NC} Copied tracker script to: $DEST_TRACKER"
else
  echo -e "${YELLOW}[DRY RUN]${NC} Would copy: $SOURCE_TRACKER → $DEST_TRACKER"
fi

echo ""

# Step 5: Update or create post-edit hook
echo "🪝 Step 5: Configuring post-edit hook..."

POST_EDIT_HOOK="$HOOKS_DIR/post-edit.js"

POST_EDIT_CONTENT='#!/usr/bin/env node
/**
 * Post-Edit Hook
 * Triggered after file edits by Claude Code
 */

const { autoDetectAndTrack } = require("./hooks-template-integration.js");

module.exports = async (hookData) => {
  // Template usage tracking
  try {
    await autoDetectAndTrack("post-edit", hookData);
  } catch (error) {
    console.error("Template tracking error:", error.message);
  }

  // Add other post-edit logic here...
};
'

if [ -f "$POST_EDIT_HOOK" ]; then
  echo -e "${YELLOW}⚠️${NC}  Post-edit hook already exists"
  echo "   Manual integration required - add this to $POST_EDIT_HOOK:"
  echo ""
  echo "   const { autoDetectAndTrack } = require('./hooks-template-integration.js');"
  echo "   await autoDetectAndTrack('post-edit', hookData);"
  echo ""
else
  if [ "$DRY_RUN" = false ]; then
    echo "$POST_EDIT_CONTENT" > "$POST_EDIT_HOOK"
    chmod +x "$POST_EDIT_HOOK"
    echo -e "${GREEN}✓${NC} Created post-edit hook: $POST_EDIT_HOOK"
  else
    echo -e "${YELLOW}[DRY RUN]${NC} Would create: $POST_EDIT_HOOK"
  fi
fi

echo ""

# Step 6: Update or create post-task hook
echo "🪝 Step 6: Configuring post-task hook..."

POST_TASK_HOOK="$HOOKS_DIR/post-task.js"

POST_TASK_CONTENT='#!/usr/bin/env node
/**
 * Post-Task Hook
 * Triggered after tasks complete
 */

const { autoDetectAndTrack } = require("./hooks-template-integration.js");

module.exports = async (hookData) => {
  // Template usage tracking
  try {
    await autoDetectAndTrack("post-task", hookData);
  } catch (error) {
    console.error("Template tracking error:", error.message);
  }

  // Add other post-task logic here...
};
'

if [ -f "$POST_TASK_HOOK" ]; then
  echo -e "${YELLOW}⚠️${NC}  Post-task hook already exists"
  echo "   Manual integration required - add this to $POST_TASK_HOOK:"
  echo ""
  echo "   const { autoDetectAndTrack } = require('./hooks-template-integration.js');"
  echo "   await autoDetectAndTrack('post-task', hookData);"
  echo ""
else
  if [ "$DRY_RUN" = false ]; then
    echo "$POST_TASK_CONTENT" > "$POST_TASK_HOOK"
    chmod +x "$POST_TASK_HOOK"
    echo -e "${GREEN}✓${NC} Created post-task hook: $POST_TASK_HOOK"
  else
    echo -e "${YELLOW}[DRY RUN]${NC} Would create: $POST_TASK_HOOK"
  fi
fi

echo ""

# Step 7: Verify installation
echo "✅ Step 7: Verifying installation..."

if [ "$DRY_RUN" = false ]; then
  if [ -f "$DEST_INTEGRATION" ] && [ -f "$DEST_TRACKER" ]; then
    echo -e "${GREEN}✓${NC} All files installed successfully"

    # Test tracker
    if node "$DEST_TRACKER" --help &> /dev/null; then
      echo -e "${GREEN}✓${NC} Template tracker is executable"
    else
      echo -e "${YELLOW}⚠️${NC}  Template tracker test failed - check dependencies"
    fi
  else
    echo -e "${RED}❌ Installation incomplete${NC}"
    exit 1
  fi
else
  echo -e "${YELLOW}[DRY RUN]${NC} Skipping verification"
fi

echo ""
echo "======================================================================"
echo "  Installation Complete!"
echo "======================================================================"
echo ""
echo "📖 Next Steps:"
echo ""
echo "1. Test the tracker:"
echo "   node ~/.claude-flow/hooks/template-tracker.js --help"
echo ""
echo "2. View usage stats:"
echo "   node ~/.claude-flow/hooks/template-tracker.js --stats"
echo ""
echo "3. List unused templates:"
echo "   node ~/.claude-flow/hooks/template-tracker.js --list-unused"
echo ""
echo "4. Manual tracking (if needed):"
echo "   node ~/.claude-flow/hooks/template-tracker.js \\"
echo "     --template lean-canvas --action fill"
echo ""
echo "📚 Documentation:"
echo "   $SCRIPT_DIR/../docs/template-usage-tracking.md"
echo ""
echo "======================================================================"
echo ""

if [ "$DRY_RUN" = false ]; then
  echo -e "${GREEN}✨ Template usage tracking is now active!${NC}"
else
  echo -e "${YELLOW}🔍 DRY RUN COMPLETE - No changes were made${NC}"
  echo "   Run without --dry-run to install"
fi

echo ""
