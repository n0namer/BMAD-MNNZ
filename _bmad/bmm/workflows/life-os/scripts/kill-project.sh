#!/bin/bash
# Kill a project (move ACTIVE → KILLED)

# Usage: ./kill-project.sh {project-folder-path} {kill-reason}
# Example: ./kill-project.sh ../projects-bank/active/project-001-katana "Market pivot - no longer viable"

PROJECT_PATH=$1
KILL_REASON=$2

# Validate inputs
if [ -z "$PROJECT_PATH" ]; then
    echo "❌ Usage: ./kill-project.sh {project-folder-path} {kill-reason}"
    echo "Example: ./kill-project.sh ../projects-bank/active/project-001-katana \"Market pivot - no longer viable\""
    exit 1
fi

if [ -z "$KILL_REASON" ]; then
    echo "❌ Error: Kill reason is required"
    echo "Usage: ./kill-project.sh {project-folder-path} {kill-reason}"
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

# Check if project.md exists
PROJECT_FILE="$PROJECT_PATH/project.md"
if [ ! -f "$PROJECT_FILE" ]; then
    echo "❌ Error: project.md not found: $PROJECT_FILE"
    exit 1
fi

# Get current date
KILLED_DATE=$(date +%Y-%m-%d)
KILLED_ISO=$(date -Iseconds)

echo "⚠️ KILLING PROJECT: $PROJECT_NAME"
echo "📁 Source: $PROJECT_PATH"
echo "💀 Reason: $KILL_REASON"
echo ""

# Determine destination path
ACTIVE_BASE=$(dirname "$PROJECT_PATH")
PARENT_DIR=$(dirname "$ACTIVE_BASE")
KILLED_PATH="$PARENT_DIR/killed/$PROJECT_NAME"

# Check if already exists in killed
if [ -d "$KILLED_PATH" ]; then
    echo "⚠️ Warning: Project already exists in killed folder"
    echo "❌ Path: $KILLED_PATH"
    exit 1
fi

# Create killed directory if needed
mkdir -p "$PARENT_DIR/killed"

# Create logs directory if it doesn't exist
mkdir -p "$PROJECT_PATH/logs"

echo "📝 Creating kill-analysis.md..."

# Create kill analysis document
KILL_ANALYSIS_FILE="$PROJECT_PATH/logs/kill-analysis.md"

cat > "$KILL_ANALYSIS_FILE" <<EOF
# Project Kill Analysis

**Project**: $PROJECT_NAME
**Killed**: $KILLED_DATE
**Decision By**: [Your Name]

---

## Kill Decision

### Primary Reason
$KILL_REASON

### Contributing Factors
- [Factor 1]
- [Factor 2]
- [Factor 3]

### Timeline of Concerns
- **[Date]**: [First warning sign]
- **[Date]**: [Escalating issue]
- **[Date]**: [Final decision point]

---

## What We Learned

### What Went Wrong
1. **[Issue Area 1]**
   - What happened: ___
   - Root cause: ___
   - Warning signs: ___

2. **[Issue Area 2]**
   - What happened: ___
   - Root cause: ___
   - Warning signs: ___

3. **[Issue Area 3]**
   - What happened: ___
   - Root cause: ___
   - Warning signs: ___

### What We Could Have Done Differently
- [ ] Earlier validation of [assumption]
- [ ] More focus on [area]
- [ ] Different approach to [strategy]
- [ ] Better resource allocation
- [ ] More frequent checkpoints

### Early Warning Signals We Missed
1. ___
2. ___
3. ___

---

## Salvageable Outputs

### What We Preserved
- [ ] Code/artifacts in: artifacts/
- [ ] Documentation in: [location]
- [ ] Learnings captured in: [location]
- [ ] Data/research in: [location]

### Potential Reuse
- **Component X**: Could be used for [future project]
- **Learning Y**: Applicable to [similar situation]
- **Asset Z**: Reusable in [context]

---

## Decision Analysis

### Would We Do This Again?
**[ ] Yes, with changes** | **[ ] No, not viable** | **[ ] Maybe, under different conditions**

**Reasoning**: ___

### Under What Conditions Would This Work?
- Condition 1: ___
- Condition 2: ___
- Condition 3: ___

### Related Ideas Worth Exploring
- [ ] Idea 1: [description]
- [ ] Idea 2: [description]
- [ ] Idea 3: [description]

---

## Future Prevention

### Red Flags to Watch For
1. ___
2. ___
3. ___

### Questions to Ask Next Time
- Before starting: ___
- During execution: ___
- At checkpoints: ___

### Patterns to Avoid
- Pattern 1: ___
- Pattern 2: ___
- Pattern 3: ___

---

## Emotional Reflection

### How Do We Feel About This Decision?
[Honest reflection on the emotional aspect of killing the project]

### What Are We Grateful For?
- Learning 1: ___
- Learning 2: ___
- Learning 3: ___

### How Will This Make Us Better?
[Forward-looking perspective on growth from this experience]

---

**Analysis Completed**: $KILLED_DATE
**Status**: Project killed and archived
**Next Action**: Extract patterns during quarterly review
EOF

echo "✅ Created kill-analysis.md"
echo ""

echo "🔄 Updating project.md frontmatter..."

# Update frontmatter (status, killed date, reason)
sed -i "s/^status: .*/status: killed/" "$PROJECT_FILE"
sed -i "s/^completed: .*/killed: $KILLED_DATE/" "$PROJECT_FILE"

# Add kill_reason field if not exists (append after killed field)
if ! grep -q "^kill_reason:" "$PROJECT_FILE"; then
    sed -i "/^killed:/a kill_reason: \"$KILL_REASON\"" "$PROJECT_FILE"
else
    sed -i "s/^kill_reason:.*/kill_reason: \"$KILL_REASON\"/" "$PROJECT_FILE"
fi

echo "✅ Updated frontmatter:"
echo "   - status: killed"
echo "   - killed: $KILLED_DATE"
echo "   - kill_reason: $KILL_REASON"
echo ""

echo "📦 Moving project to killed folder..."

# Move project folder
mv "$PROJECT_PATH" "$KILLED_PATH"

if [ $? -eq 0 ]; then
    echo "✅ Project moved successfully!"
    echo "📁 New location: $KILLED_PATH"
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
  "status": "killed",
  "killed_date": "$KILLED_DATE",
  "killed_iso": "$KILLED_ISO",
  "kill_reason": "$KILL_REASON",
  "project_path": "$KILLED_PATH",
  "kill_analysis_exists": true
}
MEMORYJSON
)

# Store in life-os namespace
if command -v npx &> /dev/null; then
    npx claude-flow@v3alpha memory store \
      --namespace "life-os" \
      --key "killed:project-$PROJECT_ID" \
      --content "$MEMORY_CONTENT" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "✅ Saved to global memory: life-os:killed:project-$PROJECT_ID"
    else
        echo "⚠️ Could not save to memory (claude-flow not available)"
    fi
else
    echo "⚠️ Skipping memory save (npx not found)"
fi

echo ""
echo "💀 PROJECT KILLED"
echo ""
echo "📊 Summary:"
echo "   Project: $PROJECT_NAME"
echo "   Killed: $KILLED_DATE"
echo "   Reason: $KILL_REASON"
echo "   Location: $KILLED_PATH"
echo ""
echo "📋 Next Steps:"
echo "   1. Review kill-analysis.md and complete all sections"
echo "   2. Extract learnings for future projects"
echo "   3. Update portfolio dashboard"
echo "   4. Consider if salvageable components can be reused"
echo ""
echo "💡 Remember: Killing projects is a sign of good judgment, not failure."
echo ""
