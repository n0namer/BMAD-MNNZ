#!/bin/bash
# Complete a project (move ACTIVE → COMPLETED)

# Usage: ./complete-project.sh {project-folder-path}
# Example: ./complete-project.sh ../projects-bank/active/project-001-katana

PROJECT_PATH=$1

# Validate inputs
if [ -z "$PROJECT_PATH" ]; then
    echo "❌ Usage: ./complete-project.sh {project-folder-path}"
    echo "Example: ./complete-project.sh ../projects-bank/active/project-001-katana"
    exit 1
fi

# Check if project exists
if [ ! -d "$PROJECT_PATH" ]; then
    echo "❌ Error: Project folder not found: $PROJECT_PATH"
    exit 1
fi

# Extract project name from path
PROJECT_NAME=$(basename "$PROJECT_PATH")

# Extract project ID (assumes format: project-NNN-name)
if [[ $PROJECT_NAME =~ project-([0-9]+)-.+ ]]; then
    PROJECT_ID="${BASH_REMATCH[1]}"
else
    echo "❌ Error: Invalid project name format. Expected: project-NNN-name"
    exit 1
fi

# Check if retrospective exists (REQUIRED)
RETROSPECTIVE_FILE="$PROJECT_PATH/logs/retrospective.md"
if [ ! -f "$RETROSPECTIVE_FILE" ]; then
    echo "❌ Error: Retrospective not found: $RETROSPECTIVE_FILE"
    echo "❌ Cannot complete project without retrospective."
    echo ""
    echo "Create retrospective first:"
    echo "  1. Create file: $RETROSPECTIVE_FILE"
    echo "  2. Answer: What worked? What didn't? What would you do differently?"
    echo "  3. Run this script again"
    exit 1
fi

# Check if project.md exists
PROJECT_FILE="$PROJECT_PATH/project.md"
if [ ! -f "$PROJECT_FILE" ]; then
    echo "❌ Error: project.md not found: $PROJECT_FILE"
    exit 1
fi

# Get current date
COMPLETED_DATE=$(date +%Y-%m-%d)
COMPLETED_ISO=$(date -Iseconds)

echo "📦 Completing project: $PROJECT_NAME"
echo "📁 Source: $PROJECT_PATH"
echo ""

# Determine destination path
ACTIVE_BASE=$(dirname "$PROJECT_PATH")
PARENT_DIR=$(dirname "$ACTIVE_BASE")
COMPLETED_PATH="$PARENT_DIR/completed/$PROJECT_NAME"

# Check if already exists in completed
if [ -d "$COMPLETED_PATH" ]; then
    echo "⚠️ Warning: Project already exists in completed folder"
    echo "❌ Path: $COMPLETED_PATH"
    exit 1
fi

# Create completed directory if needed
mkdir -p "$PARENT_DIR/completed"

echo "🔄 Updating project.md frontmatter..."

# Update frontmatter (status, completed date)
# Use sed to update YAML frontmatter
sed -i "s/^status: .*/status: completed/" "$PROJECT_FILE"
sed -i "s/^completed: .*/completed: $COMPLETED_DATE/" "$PROJECT_FILE"
sed -i "s/^progress: .*/progress: 100/" "$PROJECT_FILE"

echo "✅ Updated frontmatter:"
echo "   - status: completed"
echo "   - completed: $COMPLETED_DATE"
echo "   - progress: 100"
echo ""

echo "📦 Moving project to completed folder..."

# Move project folder
mv "$PROJECT_PATH" "$COMPLETED_PATH"

if [ $? -eq 0 ]; then
    echo "✅ Project moved successfully!"
    echo "📁 New location: $COMPLETED_PATH"
else
    echo "❌ Error: Failed to move project"
    exit 1
fi

echo ""
echo "💾 Saving to global memory..."

# Create JSON content for memory
MEMORY_CONTENT=$(cat <<MEMORYJSON
{
  "project_id": "$PROJECT_ID",
  "project_name": "$PROJECT_NAME",
  "status": "completed",
  "completed_date": "$COMPLETED_DATE",
  "completed_iso": "$COMPLETED_ISO",
  "project_path": "$COMPLETED_PATH",
  "retrospective_exists": true
}
MEMORYJSON
)

# Store in life-os namespace
if command -v npx &> /dev/null; then
    npx claude-flow@v3alpha memory store \
      --namespace "life-os" \
      --key "completed:project-$PROJECT_ID" \
      --content "$MEMORY_CONTENT" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "✅ Saved to global memory: life-os:completed:project-$PROJECT_ID"
    else
        echo "⚠️ Could not save to memory (claude-flow not available)"
    fi
else
    echo "⚠️ Skipping memory save (npx not found)"
fi

echo ""
echo "🎉 PROJECT COMPLETED!"
echo ""
echo "📊 Summary:"
echo "   Project: $PROJECT_NAME"
echo "   Completed: $COMPLETED_DATE"
echo "   Location: $COMPLETED_PATH"
echo ""
echo "📋 Next Steps:"
echo "   1. Review retrospective for learnings"
echo "   2. Extract patterns for future projects"
echo "   3. Update portfolio dashboard"
echo ""
