#!/bin/bash
# Archive an idea to quarterly folder

# Usage: ./archive-idea.sh {idea-id} {status} [reason]
# Example: ./archive-idea.sh 001 completed
# Example: ./archive-idea.sh 006 killed "Market validation failure"

IDEA_ID=$1
STATUS=$2  # completed or killed
REASON=$3  # optional, for killed ideas

# Validate inputs
if [ -z "$IDEA_ID" ] || [ -z "$STATUS" ]; then
    echo "❌ Usage: ./archive-idea.sh {idea-id} {completed|killed} [reason]"
    exit 1
fi

if [ "$STATUS" != "completed" ] && [ "$STATUS" != "killed" ]; then
    echo "❌ Status must be 'completed' or 'killed'"
    exit 1
fi

# Get current quarter
YEAR=$(date +%Y)
MONTH=$(date +%m)
if [ $MONTH -le 3 ]; then
    QUARTER="q1"
elif [ $MONTH -le 6 ]; then
    QUARTER="q2"
elif [ $MONTH -le 9 ]; then
    QUARTER="q3"
else
    QUARTER="q4"
fi

# Paths
ARCHIVE_BASE="../output/archive"
QUARTER_FOLDER="$YEAR-$QUARTER"
ARCHIVE_PATH="$ARCHIVE_BASE/$STATUS/$QUARTER_FOLDER"
OUTPUT_FOLDER="../output"

# Create quarter folder if needed
mkdir -p "$ARCHIVE_PATH"

# Find idea files
RETROSPECTIVE_FILE="$OUTPUT_FOLDER/idea-$IDEA_ID-retrospective.md"
EXECUTION_TRACKER="$OUTPUT_FOLDER/idea-$IDEA_ID-execution-tracker.md"
PIVOT_KILL_FILE="$OUTPUT_FOLDER/step-x-04-decision-$IDEA_ID.md"

# Check if retrospective exists
if [ ! -f "$RETROSPECTIVE_FILE" ]; then
    echo "⚠️ Warning: Retrospective not found: $RETROSPECTIVE_FILE"
    echo "Archive will be created without full retrospective data."
fi

# Create archive entry
ARCHIVE_FILE="$ARCHIVE_PATH/idea-$IDEA_ID-archive.md"

echo "📦 Archiving idea $IDEA_ID as $STATUS..."

# Generate archive entry header
cat > "$ARCHIVE_FILE" <<EOF
# Idea $IDEA_ID Archive

**Status:** $(if [ "$STATUS" = "completed" ]; then echo "✅ COMPLETED"; else echo "❌ KILLED"; fi)
**Archived:** $(date +%Y-%m-%d)
**Quarter:** $QUARTER_FOLDER

EOF

# Add kill reason if provided
if [ "$STATUS" = "killed" ] && [ -n "$REASON" ]; then
    echo "**Kill Reason:** $REASON" >> "$ARCHIVE_FILE"
    echo "" >> "$ARCHIVE_FILE"
fi

# Copy retrospective content if exists
if [ -f "$RETROSPECTIVE_FILE" ]; then
    echo "---" >> "$ARCHIVE_FILE"
    echo "" >> "$ARCHIVE_FILE"
    echo "## Retrospective" >> "$ARCHIVE_FILE"
    echo "" >> "$ARCHIVE_FILE"
    cat "$RETROSPECTIVE_FILE" >> "$ARCHIVE_FILE"
fi

# Add execution tracker summary if exists
if [ -f "$EXECUTION_TRACKER" ]; then
    echo "" >> "$ARCHIVE_FILE"
    echo "---" >> "$ARCHIVE_FILE"
    echo "" >> "$ARCHIVE_FILE"
    echo "## Execution Timeline" >> "$ARCHIVE_FILE"
    echo "" >> "$ARCHIVE_FILE"
    grep -A 50 "## Timeline" "$EXECUTION_TRACKER" >> "$ARCHIVE_FILE" 2>/dev/null || echo "*Execution tracker found but no timeline section*" >> "$ARCHIVE_FILE"
fi

# Add pivot-or-kill analysis if exists (for killed ideas)
if [ "$STATUS" = "killed" ] && [ -f "$PIVOT_KILL_FILE" ]; then
    echo "" >> "$ARCHIVE_FILE"
    echo "---" >> "$ARCHIVE_FILE"
    echo "" >> "$ARCHIVE_FILE"
    echo "## Pivot-or-Kill Analysis" >> "$ARCHIVE_FILE"
    echo "" >> "$ARCHIVE_FILE"
    cat "$PIVOT_KILL_FILE" >> "$ARCHIVE_FILE"
fi

# Add archive footer
cat >> "$ARCHIVE_FILE" <<EOF

---

**Archived by:** Archive Script
**Archive Date:** $(date +%Y-%m-%d)
**Archive Location:** $ARCHIVE_PATH/idea-$IDEA_ID-archive.md
EOF

echo "✅ Idea $IDEA_ID archived successfully!"
echo "📁 Location: $ARCHIVE_FILE"

# Store in memory (if claude-flow is available)
if command -v npx &> /dev/null; then
    echo "💾 Saving to global memory..."

    # Create JSON content for memory
    MEMORY_CONTENT=$(cat <<MEMORYJSON
{
  "idea_id": "$IDEA_ID",
  "status": "$STATUS",
  "quarter": "$QUARTER_FOLDER",
  "archive_date": "$(date +%Y-%m-%d)",
  "archive_path": "$ARCHIVE_FILE",
  "reason": "$REASON"
}
MEMORYJSON
)

    # Store in archive namespace
    npx claude-flow@v3alpha memory store \
      --namespace "archive" \
      --key "$STATUS:idea-$IDEA_ID:$QUARTER_FOLDER" \
      --content "$MEMORY_CONTENT" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "✅ Saved to global memory: archive:$STATUS:idea-$IDEA_ID:$QUARTER_FOLDER"
    else
        echo "⚠️ Could not save to memory (claude-flow not available)"
    fi
else
    echo "⚠️ Skipping memory save (npx not found)"
fi

echo ""
echo "🎉 Archive complete!"
echo "Next: Run pattern mining during quarterly review to learn from this idea"
