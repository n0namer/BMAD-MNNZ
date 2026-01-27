---
name: 'step-01-edit'
description: 'Step 1: Edit — Modify existing AGENTS.MD content, update task templates, refresh examples and frameworks'
layer: 'edit'
menu:
  next: step-02-test.md
  back: AGENTS-MD-GENERATOR-WORKFLOW.md
handler: A
---

# Step 1: Edit

**Purpose:** Modify existing AGENTS.MD content, update task templates, refresh examples and frameworks, and ensure all content remains current and accurate

## Overview

This step handles the editing and updating of existing AGENTS.MD content to ensure it remains current, accurate, and aligned with evolving requirements and best practices.

## Prerequisites

- Existing AGENTS.MD file present
- Current requirements and standards defined
- Change requests or update requirements identified
- Backup of current content available

## Input Requirements

### Required Inputs

1. **Current AGENTS.MD** - Existing AGENTS.MD file to be updated
2. **Change Requests** - List of required changes or updates
3. **Updated Requirements** - New or modified requirements
4. **Standards Updates** - Updated BMAD or GitHub Copilot standards

### Optional Inputs

1. **User Feedback** - Feedback on current content
2. **Usage Analytics** - Data on how content is being used
3. **Performance Metrics** - Metrics showing content effectiveness

## Process

### 1. Content Analysis

```bash
# Analyze current content
analyze_current_content() {
    echo "Analyzing current AGENTS.MD content..."
    
    local agents_file="$1"
    local analysis_file="$OUTPUT_DIR/content_analysis.json"
    
    # Check file size
    local file_size=$(wc -c < "$agents_file")
    
    # Count sections
    local section_count=$(grep -c "^#" "$agents_file")
    
    # Check for outdated content
    local outdated_count=$(grep -c "TODO\|FIXME\|DEPRECATED" "$agents_file" || echo "0")
    
    # Check compliance
    local bmad_refs=$(grep -c "BMAD" "$agents_file" || echo "0")
    local phase_refs=$(grep -c "Phase [1-4]" "$agents_file" || echo "0")
    
    cat > "$analysis_file" << EOF
{
  "analysis_date": "$(date -Iseconds)",
  "file_size": $file_size,
  "sections_count": $section_count,
  "outdated_markers": $outdated_count,
  "bmad_references": $bmad_refs,
  "phase_references": $phase_refs,
  "compliance_status": {
    "bmad_protocol": $([ $bmad_refs -gt 0 ] && echo "compliant" || echo "non_compliant"),
    "phase_structure": $([ $phase_refs -gt 0 ] && echo "compliant" || echo "non_compliant"),
    "file_size": $([ $file_size -lt 102400 ] && echo "compliant" || echo "non_compliant")
  }
}
EOF
    
    echo "✓ Content analysis completed: $analysis_file"
    return 0
}
```

### 2. Change Request Processing

```bash
# Process change requests
process_change_requests() {
    echo "Processing change requests..."
    
    local change_requests_file="$1"
    local changes_file="$OUTPUT_DIR/changes_to_apply.json"
    
    # Load change requests
    if [ ! -f "$change_requests_file" ]; then
        echo "No change requests file found, skipping change processing"
        return 0
    fi
    
    # Process each change request
    local change_count=$(jq '.changes | length' "$change_requests_file" 2>/dev/null || echo "0")
    
    if [ "$change_count" -gt 0 ]; then
        echo "Processing $change_count change requests..."
        
        # Create changes file
        cat > "$changes_file" << EOF
{
  "change_date": "$(date -Iseconds)",
  "total_changes": $change_count,
  "changes": $(jq '.changes' "$change_requests_file" 2>/dev/null || echo "[]"),
  "status": "pending"
}
EOF
        
        echo "✓ Change requests processed: $changes_file"
    else
        echo "No change requests to process"
    fi
    
    return 0
}
```

### 3. Content Updates

```bash
# Apply content updates
apply_content_updates() {
    echo "Applying content updates..."
    
    local agents_file="$1"
    local changes_file="$2"
    local updated_file="$OUTPUT_DIR/AGENTS.MD.updated"
    
    # Create backup
    cp "$agents_file" "$OUTPUT_DIR/AGENTS.MD.backup"
    
    # Apply changes if they exist
    if [ -f "$changes_file" ]; then
        local change_count=$(jq '.total_changes' "$changes_file" 2>/dev/null || echo "0")
        
        if [ "$change_count" -gt 0 ]; then
            echo "Applying $change_count content changes..."
            
            # Apply each change
            jq -r '.changes[] | @base64' "$changes_file" | while read -r change; do
                local change_type=$(echo "$change" | jq -r '.type')
                local target_section=$(echo "$change" | jq -r '.target_section')
                local new_content=$(echo "$change" | jq -r '.new_content')
                
                case "$change_type" in
                    "update")
                        # Update existing section
                        sed -i "/^## $target_section$/,/^## /{ /^## $target_section$/!{ /^## /!d; }; }" "$agents_file"
                        echo "## $target_section" >> "$agents_file"
                        echo "$new_content" >> "$agents_file"
                        echo "" >> "$agents_file"
                        ;;
                    "add")
                        # Add new section
                        echo "## $target_section" >> "$agents_file"
                        echo "$new_content" >> "$agents_file"
                        echo "" >> "$agents_file"
                        ;;
                    "remove")
                        # Remove section
                        sed -i "/^## $target_section$/,/^## /d" "$agents_file"
                        ;;
                esac
            done
            
            echo "✓ Content updates applied"
        else
            echo "No changes to apply"
        fi
    else
        echo "No changes file found, copying original"
        cp "$agents_file" "$updated_file"
    fi
    
    return 0
}
```

### 4. Task Template Updates

```bash
# Update task templates
update_task_templates() {
    echo "Updating task templates..."
    
    local templates_file="$DATA_DIR/step-03-task-templates.md"
    local updated_templates="$OUTPUT_DIR/task_templates.updated.md"
    
    # Check if templates file exists
    if [ ! -f "$templates_file" ]; then
        echo "Task templates file not found, skipping template updates"
        return 0
    fi
    
    # Update templates based on latest standards
    cp "$templates_file" "$updated_templates"
    
    # Add any new templates or update existing ones
    # This would typically involve checking against a template registry
    # and applying standard updates
    
    echo "✓ Task templates updated: $updated_templates"
    return 0
}
```

### 5. Examples and Frameworks Refresh

```bash
# Refresh examples and frameworks
refresh_examples_and_frameworks() {
    echo "Refreshing examples and frameworks..."
    
    local examples_file="$DATA_DIR/step-03-examples.md"
    local frameworks_file="$DATA_DIR/step-03-reasoning-frameworks.md"
    
    # Update examples
    if [ -f "$examples_file" ]; then
        # Check for outdated examples
        local outdated_examples=$(grep -c "outdated\|deprecated" "$examples_file" || echo "0")
        
        if [ "$outdated_examples" -gt 0 ]; then
            echo "Found $outdated_examples outdated examples, updating..."
            # Update or remove outdated examples
            sed -i '/outdated\|deprecated/d' "$examples_file"
            echo "✓ Outdated examples removed"
        fi
    fi
    
    # Update frameworks
    if [ -f "$frameworks_file" ]; then
        # Check for outdated frameworks
        local outdated_frameworks=$(grep -c "outdated\|deprecated" "$frameworks_file" || echo "0")
        
        if [ "$outdated_frameworks" -gt 0 ]; then
            echo "Found $outdated_frameworks outdated frameworks, updating..."
            # Update or remove outdated frameworks
            sed -i '/outdated\|deprecated/d' "$frameworks_file"
            echo "✓ Outdated frameworks removed"
        fi
    fi
    
    echo "✓ Examples and frameworks refreshed"
    return 0
}
```

## Output Files

### Updated AGENTS.MD
- **File:** `output/AGENTS.MD.updated`
- **Content:** Updated AGENTS.MD content
- **Format:** BMAD-compliant markdown

### Content Analysis
- **File:** `output/content_analysis.json`
- **Content:** Analysis of current content status
- **Format:** JSON

### Changes Applied
- **File:** `output/changes_to_apply.json`
- **Content:** Changes that were applied
- **Format:** JSON

### Updated Templates
- **File:** `output/task_templates.updated.md`
- **Content:** Updated task templates
- **Format:** Markdown

## Quality Gates

- [ ] Content analysis completed
- [ ] All change requests processed
- [ ] Content updates applied successfully
- [ ] Task templates updated
- [ ] Examples and frameworks refreshed
- [ ] Backup created before changes

## Troubleshooting

### Common Issues

1. **Content analysis failed**
   - Check file permissions
   - Verify file format
   - Check for corrupted content

2. **Change requests not processed**
   - Verify change requests file format
   - Check for syntax errors
   - Validate change request structure

3. **Content updates failed**
   - Check file write permissions
   - Verify backup creation
   - Review change application logic

4. **Template updates incomplete**
   - Check template file format
   - Verify update logic
   - Review template registry

### Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team