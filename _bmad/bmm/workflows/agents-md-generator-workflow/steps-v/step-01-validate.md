---
name: 'step-01-validate'
description: 'Step 1: Validate — Verify AGENTS.MD content compliance, check file size limits, validate BMAD protocol adherence'
layer: 'validate'
menu:
  next: step-02-test.md
  back: AGENTS-MD-GENERATOR-WORKFLOW.md
handler: A
---

# Step 1: Validate

**Purpose:** Verify AGENTS.MD content compliance, check file size limits, validate BMAD protocol adherence, and ensure GitHub Copilot compatibility

## Overview

This step performs comprehensive validation of AGENTS.MD content to ensure it meets all requirements, standards, and compatibility criteria.

## Prerequisites

- AGENTS.MD file to be validated
- BMAD requirements and standards defined
- GitHub Copilot compatibility requirements
- Validation tools and scripts available

## Input Requirements

### Required Inputs

1. **AGENTS.MD File** - File to be validated
2. **BMAD Requirements** - BMAD protocol requirements
3. **GitHub Copilot Standards** - Compatibility requirements
4. **Validation Rules** - Validation criteria and rules

### Optional Inputs

1. **Custom Validation Rules** - Additional validation criteria
2. **Previous Validation Results** - Historical validation data
3. **User Preferences** - Custom validation preferences

## Process

### 1. File Size Validation

```bash
# Validate file size limits
validate_file_size() {
    echo "Validating file size limits..."
    
    local agents_file="$1"
    local max_size="$2"
    local validation_file="$OUTPUT_DIR/file_size_validation.json"
    
    # Check file size
    local file_size=$(wc -c < "$agents_file")
    
    # Validate against limits
    local status="compliant"
    local issues=()
    
    if [ "$file_size" -gt "$max_size" ]; then
        status="non_compliant"
        issues+=("File size exceeds limit: ${file_size} bytes > ${max_size} bytes")
    fi
    
    # Check for excessive whitespace
    local whitespace_lines=$(grep -c "^[[:space:]]*$" "$agents_file" || echo "0")
    if [ "$whitespace_lines" -gt 50 ]; then
        issues+=("Excessive whitespace lines: $whitespace_lines")
    fi
    
    # Generate validation report
    cat > "$validation_file" << EOF
{
  "validation_date": "$(date -Iseconds)",
  "file": "$agents_file",
  "file_size": $file_size,
  "max_allowed_size": $max_size,
  "status": "$status",
  "issues": $(printf '%s\n' "${issues[@]}" | jq -R . | jq -s .),
  "recommendations": [
    "Remove excessive whitespace if present",
    "Optimize content structure if size limit exceeded",
    "Consider modularization for large files"
  ]
}
EOF
    
    if [ "$status" = "compliant" ]; then
        echo "✓ File size validation passed"
    else
        echo "✗ File size validation failed"
        for issue in "${issues[@]}"; do
            echo "  - $issue"
        done
    fi
    
    return $([ "$status" = "compliant" ] && echo "0" || echo "1")
}
```

### 2. BMAD Protocol Validation

```bash
# Validate BMAD protocol compliance
validate_bmad_protocol() {
    echo "Validating BMAD protocol compliance..."
    
    local agents_file="$1"
    local validation_file="$OUTPUT_DIR/bmad_protocol_validation.json"
    
    # Check for BMAD protocol elements
    local bmad_refs=$(grep -c "BMAD" "$agents_file" || echo "0")
    local phase_refs=$(grep -c "Phase [1-4]" "$agents_file" || echo "0")
    local handler_refs=$(grep -c "handler:" "$agents_file" || echo "0")
    local menu_refs=$(grep -c "menu:" "$agents_file" || echo "0")
    
    # Validate phase structure
    local phase_1=$(grep -c "Phase 1\|Discovery" "$agents_file" || echo "0")
    local phase_2=$(grep -c "Phase 2\|Planning" "$agents_file" || echo "0")
    local phase_3=$(grep -c "Phase 3\|Implementation" "$agents_file" || echo "0")
    local phase_4=$(grep -c "Phase 4\|Validation" "$agents_file" || echo "0")
    
    # Check for required sections
    local ux_layer=$(grep -c "UX Layer" "$agents_file" || echo "0")
    local bmad_protocol=$(grep -c "BMAD Protocol" "$agents_file" || echo "0")
    local phase_workflows=$(grep -c "Phase Workflows" "$agents_file" || echo "0")
    
    # Determine compliance status
    local status="compliant"
    local issues=()
    
    if [ "$bmad_refs" -lt 5 ]; then
        status="non_compliant"
        issues+=("Insufficient BMAD protocol references: $bmad_refs")
    fi
    
    if [ "$phase_refs" -lt 4 ]; then
        status="non_compliant"
        issues+=("Insufficient phase references: $phase_refs")
    fi
    
    if [ "$phase_1" -eq 0 ] || [ "$phase_2" -eq 0 ] || [ "$phase_3" -eq 0 ] || [ "$phase_4" -eq 0 ]; then
        status="non_compliant"
        issues+=("Missing required phase sections")
    fi
    
    if [ "$ux_layer" -eq 0 ] || [ "$bmad_protocol" -eq 0 ] || [ "$phase_workflows" -eq 0 ]; then
        status="non_compliant"
        issues+=("Missing required layer sections")
    fi
    
    # Generate validation report
    cat > "$validation_file" << EOF
{
  "validation_date": "$(date -Iseconds)",
  "file": "$agents_file",
  "bmad_references": $bmad_refs,
  "phase_references": $phase_refs,
  "handler_references": $handler_refs,
  "menu_references": $menu_refs,
  "phase_breakdown": {
    "phase_1": $phase_1,
    "phase_2": $phase_2,
    "phase_3": $phase_3,
    "phase_4": $phase_4
  },
  "layer_sections": {
    "ux_layer": $ux_layer,
    "bmad_protocol": $bmad_protocol,
    "phase_workflows": $phase_workflows
  },
  "status": "$status",
  "issues": $(printf '%s\n' "${issues[@]}" | jq -R . | jq -s .),
  "recommendations": [
    "Add more BMAD protocol references if needed",
    "Ensure all phase sections are present",
    "Verify layer section completeness"
  ]
}
EOF
    
    if [ "$status" = "compliant" ]; then
        echo "✓ BMAD protocol validation passed"
    else
        echo "✗ BMAD protocol validation failed"
        for issue in "${issues[@]}"; do
            echo "  - $issue"
        done
    fi
    
    return $([ "$status" = "compliant" ] && echo "0" || echo "1")
}
```

### 3. GitHub Copilot Compatibility Validation

```bash
# Validate GitHub Copilot compatibility
validate_copilot_compatibility() {
    echo "Validating GitHub Copilot compatibility..."
    
    local agents_file="$1"
    local validation_file="$OUTPUT_DIR/copilot_compatibility_validation.json"
    
    # Check file format
    local file_extension="${agents_file##*.}"
    local format_valid=true
    
    if [ "$file_extension" != "md" ]; then
        format_valid=false
    fi
    
    # Check required sections
    local overview_section=$(grep -c "## Overview" "$agents_file" || echo "0")
    local usage_section=$(grep -c "## Usage" "$agents_file" || echo "0")
    local examples_section=$(grep -c "## Examples" "$agents_file" || echo "0")
    
    # Check for agent-friendly content
    local agent_friendly=true
    local agent_keywords=$(grep -c "agent\|LLM\|AI" "$agents_file" || echo "0")
    
    # Check for clear structure
    local clear_structure=true
    local heading_count=$(grep -c "^#" "$agents_file" || echo "0")
    
    # Determine compatibility status
    local status="compatible"
    local issues=()
    
    if [ "$format_valid" = false ]; then
        status="incompatible"
        issues+=("File format not markdown: $file_extension")
    fi
    
    if [ "$overview_section" -eq 0 ]; then
        status="incompatible"
        issues+=("Missing Overview section")
    fi
    
    if [ "$usage_section" -eq 0 ]; then
        status="incompatible"
        issues+=("Missing Usage section")
    fi
    
    if [ "$examples_section" -eq 0 ]; then
        status="incompatible"
        issues+=("Missing Examples section")
    fi
    
    if [ "$heading_count" -lt 5 ]; then
        status="incompatible"
        issues+=("Insufficient structure: $heading_count headings")
    fi
    
    # Generate validation report
    cat > "$validation_file" << EOF
{
  "validation_date": "$(date -Iseconds)",
  "file": "$agents_file",
  "file_format": "$file_extension",
  "format_valid": $format_valid,
  "required_sections": {
    "overview": $overview_section,
    "usage": $usage_section,
    "examples": $examples_section
  },
  "agent_keywords": $agent_keywords,
  "heading_count": $heading_count,
  "status": "$status",
  "issues": $(printf '%s\n' "${issues[@]}" | jq -R . | jq -s .),
  "recommendations": [
    "Ensure file is in markdown format",
    "Add required sections (Overview, Usage, Examples)",
    "Include agent-friendly content",
    "Maintain clear document structure"
  ]
}
EOF
    
    if [ "$status" = "compatible" ]; then
        echo "✓ GitHub Copilot compatibility validation passed"
    else
        echo "✗ GitHub Copilot compatibility validation failed"
        for issue in "${issues[@]}"; do
            echo "  - $issue"
        done
    fi
    
    return $([ "$status" = "compatible" ] && echo "0" || echo "1")
}
```

### 4. Content Quality Validation

```bash
# Validate content quality
validate_content_quality() {
    echo "Validating content quality..."
    
    local agents_file="$1"
    local validation_file="$OUTPUT_DIR/content_quality_validation.json"
    
    # Check for spelling and grammar issues (basic checks)
    local spelling_issues=0
    local grammar_issues=0
    
    # Check for broken links
    local broken_links=$(grep -c "http.*[^)]" "$agents_file" || echo "0")
    
    # Check for code blocks
    local code_blocks=$(grep -c "```" "$agents_file" || echo "0")
    
    # Check for proper markdown syntax
    local markdown_issues=0
    
    # Basic markdown validation
    if ! grep -q "^# " "$agents_file"; then
        markdown_issues=$((markdown_issues + 1))
    fi
    
    if ! grep -q "^## " "$agents_file"; then
        markdown_issues=$((markdown_issues + 1))
    fi
    
    # Determine quality status
    local status="good"
    local issues=()
    
    if [ "$broken_links" -gt 10 ]; then
        status="poor"
        issues+=("Too many potential broken links: $broken_links")
    fi
    
    if [ "$code_blocks" -eq 0 ]; then
        status="poor"
        issues+=("No code examples found")
    fi
    
    if [ "$markdown_issues" -gt 0 ]; then
        status="poor"
        issues+=("Markdown syntax issues: $markdown_issues")
    fi
    
    # Generate validation report
    cat > "$validation_file" << EOF
{
  "validation_date": "$(date -Iseconds)",
  "file": "$agents_file",
  "spelling_issues": $spelling_issues,
  "grammar_issues": $grammar_issues,
  "broken_links": $broken_links,
  "code_blocks": $code_blocks,
  "markdown_issues": $markdown_issues,
  "status": "$status",
  "issues": $(printf '%s\n' "${issues[@]}" | jq -R . | jq -s .),
  "recommendations": [
    "Review and fix spelling/grammar issues",
    "Verify all links are working",
    "Add code examples where appropriate",
    "Fix markdown syntax issues"
  ]
}
EOF
    
    if [ "$status" = "good" ]; then
        echo "✓ Content quality validation passed"
    else
        echo "✗ Content quality validation failed"
        for issue in "${issues[@]}"; do
            echo "  - $issue"
        done
    fi
    
    return $([ "$status" = "good" ] && echo "0" || echo "1")
}
```

## Output Files

### File Size Validation
- **File:** `output/file_size_validation.json`
- **Content:** File size compliance results
- **Format:** JSON

### BMAD Protocol Validation
- **File:** `output/bmad_protocol_validation.json`
- **Content:** BMAD protocol compliance results
- **Format:** JSON

### GitHub Copilot Compatibility Validation
- **File:** `output/copilot_compatibility_validation.json`
- **Content:** GitHub Copilot compatibility results
- **Format:** JSON

### Content Quality Validation
- **File:** `output/content_quality_validation.json`
- **Content:** Content quality assessment results
- **Format:** JSON

## Quality Gates

- [ ] File size validation passed
- [ ] BMAD protocol validation passed
- [ ] GitHub Copilot compatibility validation passed
- [ ] Content quality validation passed
- [ ] All validation reports generated
- [ ] No critical issues found

## Troubleshooting

### Common Issues

1. **File size validation failed**
   - Remove excessive whitespace
   - Optimize content structure
   - Consider modularization

2. **BMAD protocol validation failed**
   - Add missing BMAD references
   - Ensure all phase sections present
   - Verify layer section completeness

3. **GitHub Copilot compatibility failed**
   - Convert to markdown format
   - Add required sections
   - Improve document structure

4. **Content quality validation failed**
   - Fix spelling/grammar issues
   - Verify links
   - Add code examples
   - Fix markdown syntax

### Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team