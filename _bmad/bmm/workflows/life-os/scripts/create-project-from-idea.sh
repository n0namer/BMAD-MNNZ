#!/bin/bash
# Create project from planned idea (PLANNED → ACTIVE)

# Usage: ./create-project-from-idea.sh {idea-file-path}
# Example: ./create-project-from-idea.sh ../ideas-bank/planned/idea-001-finance-katana-vectorbt.md

IDEA_FILE=$1
ISO_DATE=$(date +%Y-%m-%d)

# Validate input
if [ -z "$IDEA_FILE" ]; then
    echo "❌ Usage: ./create-project-from-idea.sh {idea-file-path}"
    echo "Example: ./create-project-from-idea.sh ../ideas-bank/planned/idea-001-finance-katana.md"
    exit 1
fi

if [ ! -f "$IDEA_FILE" ]; then
    echo "❌ Error: Idea file not found: $IDEA_FILE"
    exit 1
fi

# Extract filename and parse components
FILENAME=$(basename "$IDEA_FILE" .md)

# Parse: idea-XXX-sphere-name
if [[ $FILENAME =~ ^idea-([0-9]+)-([^-]+)-(.+)$ ]]; then
    IDEA_ID="${BASH_REMATCH[1]}"
    SPHERE="${BASH_REMATCH[2]}"
    IDEA_NAME="${BASH_REMATCH[3]}"
else
    echo "❌ Error: Invalid filename format. Expected: idea-XXX-sphere-name.md"
    echo "Got: $FILENAME"
    exit 1
fi

PROJECT_ID="project-$IDEA_ID"
PROJECT_NAME="$IDEA_NAME"
PROJECT_FOLDER="../projects-bank/active/$PROJECT_ID-$PROJECT_NAME"

echo "🚀 Creating project from idea..."
echo "   Idea: idea-$IDEA_ID ($SPHERE)"
echo "   Name: $IDEA_NAME"
echo "   Project: $PROJECT_ID-$PROJECT_NAME"
echo ""

# Create project directory structure
echo "📁 Creating project structure..."
mkdir -p "$PROJECT_FOLDER/tasks"
mkdir -p "$PROJECT_FOLDER/artifacts"
mkdir -p "$PROJECT_FOLDER/logs"

if [ $? -ne 0 ]; then
    echo "❌ Failed to create project folders"
    exit 1
fi

# Extract track from idea frontmatter (if present)
TRACK=$(grep "^track:" "$IDEA_FILE" | head -1 | sed 's/^track:\s*//' | xargs)
if [ -z "$TRACK" ]; then
    TRACK="untracked"
fi

# Extract plan section from idea (everything after "## Plan" or "## Implementation Plan")
echo "📋 Extracting plan from idea..."
PLAN_CONTENT=$(sed -n '/^## \(Implementation \)\?Plan/,$p' "$IDEA_FILE")

if [ -z "$PLAN_CONTENT" ]; then
    PLAN_CONTENT="# Implementation Plan

No detailed plan found in original idea.
Please create implementation steps here.
"
fi

# Create plan.md
cat > "$PROJECT_FOLDER/plan.md" <<EOF
$PLAN_CONTENT
EOF

echo "✅ Created plan.md"

# Create project.md with metadata
echo "📝 Creating project metadata..."
cat > "$PROJECT_FOLDER/project.md" <<EOF
---
id: $PROJECT_ID
name: $PROJECT_NAME
status: active
origin-idea: idea-$IDEA_ID
sphere: $SPHERE
track: $TRACK
started: $ISO_DATE
---

# Project: $PROJECT_NAME

## Origin
- **Idea ID**: idea-$IDEA_ID
- **Sphere**: $SPHERE
- **Activated**: $ISO_DATE

## Status
- **Current**: ACTIVE
- **Track**: $TRACK

## Structure
- \`plan.md\` - Implementation plan
- \`tasks/\` - Task tracking files
- \`artifacts/\` - Project outputs and deliverables
- \`logs/\` - Execution logs and notes

## Next Steps
1. Review plan.md
2. Break down into tasks (create task files in tasks/)
3. Begin execution

---

*Project activated from idea-$IDEA_ID on $ISO_DATE*
EOF

echo "✅ Created project.md"

# Archive original idea to activated folder
ARCHIVE_FOLDER="../ideas-bank/archive/activated"
mkdir -p "$ARCHIVE_FOLDER"

ARCHIVED_IDEA_FILE="$ARCHIVE_FOLDER/idea-$IDEA_ID-activated-$ISO_DATE.md"

echo "📦 Archiving original idea..."

# Read original idea content
ORIGINAL_CONTENT=$(cat "$IDEA_FILE")

# Check if frontmatter exists
if [[ $ORIGINAL_CONTENT =~ ^---.*---(.*)$ ]]; then
    # Has frontmatter - update it
    # Extract frontmatter block
    FRONTMATTER=$(echo "$ORIGINAL_CONTENT" | sed -n '/^---$/,/^---$/p' | sed '1d;$d')
    BODY=$(echo "$ORIGINAL_CONTENT" | sed '1,/^---$/d' | sed '1,/^---$/d')

    # Update frontmatter
    UPDATED_FRONTMATTER=$(echo "$FRONTMATTER" | sed "s/^status:.*/status: activated/")

    # Check if activated_date already exists
    if ! echo "$UPDATED_FRONTMATTER" | grep -q "^activated_date:"; then
        UPDATED_FRONTMATTER="$UPDATED_FRONTMATTER
activated_date: $ISO_DATE"
    fi

    # Check if became_project already exists
    if ! echo "$UPDATED_FRONTMATTER" | grep -q "^became_project:"; then
        UPDATED_FRONTMATTER="$UPDATED_FRONTMATTER
became_project: $PROJECT_ID"
    fi

    # Write updated file
    cat > "$ARCHIVED_IDEA_FILE" <<ARCHIVEEOF
---
$UPDATED_FRONTMATTER
---
$BODY
ARCHIVEEOF
else
    # No frontmatter - add it
    cat > "$ARCHIVED_IDEA_FILE" <<ARCHIVEEOF
---
status: activated
activated_date: $ISO_DATE
became_project: $PROJECT_ID
sphere: $SPHERE
track: $TRACK
---

$ORIGINAL_CONTENT
ARCHIVEEOF
fi

echo "✅ Archived to: $ARCHIVED_IDEA_FILE"

# Remove original idea from planned folder
rm "$IDEA_FILE"
echo "✅ Removed original idea from planned folder"

# Save to Claude Flow memory
if command -v npx &> /dev/null; then
    echo ""
    echo "💾 Saving to global memory..."

    # Create JSON content for memory
    MEMORY_CONTENT=$(cat <<MEMORYJSON
{
  "id": "$PROJECT_ID",
  "name": "$PROJECT_NAME",
  "status": "active",
  "origin_idea": "idea-$IDEA_ID",
  "sphere": "$SPHERE",
  "track": "$TRACK",
  "started": "$ISO_DATE",
  "project_path": "$PROJECT_FOLDER",
  "archived_idea": "$ARCHIVED_IDEA_FILE"
}
MEMORYJSON
)

    # Store in life-os namespace
    npx claude-flow@v3alpha memory store \
      --namespace "shared-knowledge" \
      --key "life-os:projects:$PROJECT_ID" \
      --content "$MEMORY_CONTENT" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "✅ Saved to global memory: shared-knowledge:life-os:projects:$PROJECT_ID"
    else
        echo "⚠️ Could not save to memory (claude-flow not available)"
    fi
else
    echo "⚠️ Skipping memory save (npx not found)"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 Project Created Successfully!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📁 Project Location: $PROJECT_FOLDER"
echo "📋 Files Created:"
echo "   - project.md (metadata)"
echo "   - plan.md (implementation plan)"
echo "   - tasks/ (for task tracking)"
echo "   - artifacts/ (for deliverables)"
echo "   - logs/ (for execution logs)"
echo ""
echo "📦 Original Idea:"
echo "   - Archived to: $ARCHIVED_IDEA_FILE"
echo "   - Status updated: activated"
echo "   - Linked to: $PROJECT_ID"
echo ""
echo "🚀 Next Steps:"
echo "   1. cd $PROJECT_FOLDER"
echo "   2. Review plan.md"
echo "   3. Create task files in tasks/"
echo "   4. Begin execution!"
echo ""
