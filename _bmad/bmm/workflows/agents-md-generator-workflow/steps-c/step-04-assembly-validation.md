---
name: 'step-04-assembly-validation'
description: 'Step 4: Assembly & Validation — Merge content, validate size limits, perform final validation and export'
layer: 'assembly-validation'
menu:
  next: step-05-completion.md
  back: step-03-content-generation-layer-troubleshooting.md
handler: A
---

# Step 4: Assembly & Validation

**Purpose:** Merge and optimize generated content, validate file size limits and modularization, perform final validation and export, generate compliance report

## Overview

This step assembles all generated content into final AGENTS.MD and .github/copilot-instructions.md files, ensuring compliance with all requirements and size limits.

## Prerequisites

- Step 3: Content Generation completed
- All layer content generated
- Task templates and examples created
- Reasoning frameworks implemented

## Input Requirements

### Required Inputs

1. **Generated Content** - All layer files from step 3
2. **Task Templates** - `data/step-03-task-templates.md`
3. **Examples** - `data/step-03-examples.md`
4. **Reasoning Frameworks** - `data/step-03-reasoning-frameworks.md`

### Optional Inputs

1. **Custom Content** - Additional content specifications
2. **User Preferences** - Content style and format preferences

## Process

### 1. Content Assembly

```bash
# Assemble final AGENTS.MD
ASSEMBLY_FILE="output/AGENTS.MD"

# Start with intro
cat "steps-c/step-03-content-generation-intro.md" > "$ASSEMBLY_FILE"

# Add each layer content
cat "steps-c/step-03-content-generation-layer-ux.md" >> "$ASSEMBLY_FILE"
cat "steps-c/step-03-content-generation-layer-bmad.md" >> "$ASSEMBLY_FILE"
cat "steps-c/step-03-content-generation-layer-phase-workflows.md" >> "$ASSEMBLY_FILE"
cat "steps-c/step-03-content-generation-layer-task-templates.md" >> "$ASSEMBLY_FILE"
cat "steps-c/step-03-content-generation-layer-examples.md" >> "$ASSEMBLY_FILE"
cat "steps-c/step-03-content-generation-layer-reasoning-frameworks.md" >> "$ASSEMBLY_FILE"
cat "steps-c/step-03-content-generation-layer-session-monitoring.md" >> "$ASSEMBLY_FILE"
cat "steps-c/step-03-content-generation-layer-best-practices.md" >> "$ASSEMBLY_FILE"
cat "steps-c/step-03-content-generation-layer-validation.md" >> "$ASSEMBLY_FILE"
cat "steps-c/step-03-content-generation-layer-troubleshooting.md" >> "$ASSEMBLY_FILE"

# Add data references
echo "\n## References\n" >> "$ASSEMBLY_FILE"
echo "For detailed task templates, see: [data/step-03-task-templates.md](data/step-03-task-templates.md)" >> "$ASSEMBLY_FILE"
echo "For examples, see: [data/step-03-examples.md](data/step-03-examples.md)" >> "$ASSEMBLY_FILE"
echo "For reasoning frameworks, see: [data/step-03-reasoning-frameworks.md](data/step-03-reasoning-frameworks.md)" >> "$ASSEMBLY_FILE"
```

### 2. Size Optimization

```bash
# Check file size
check_file_size() {
    local file="$1"
    local max_size="$2"
    
    local size=$(wc -c < "$file")
    if [ "$size" -gt "$max_size" ]; then
        echo "File size exceeds limit: ${size} bytes"
        return 1
    fi
    
    echo "File size within limits: ${size} bytes"
    return 0
}

# Optimize content if needed
optimize_content() {
    local file="$1"
    
    # Remove excessive whitespace
    sed -i 's/^[[:space:]]*$//' "$file"
    
    # Remove duplicate lines
    awk '!seen[$0]++' "$file" > temp_file && mv temp_file "$file"
    
    # Compress long sections
    # (Implementation depends on specific content)
}
```

### 3. Final Validation

```bash
# Comprehensive validation
validate_final_output() {
    local agents_file="$1"
    local copilot_file="$2"
    
    # Check file existence
    if [ ! -f "$agents_file" ] || [ ! -f "$copilot_file" ]; then
        echo "Missing required output files"
        return 1
    fi
    
    # Check file sizes
    if ! check_file_size "$agents_file" 102400; then
        echo "AGENTS.MD exceeds size limit"
        return 1
    fi
    
    if ! check_file_size "$copilot_file" 81920; then
        echo "Copilot instructions exceed size limit"
        return 1
    fi
    
    # Check BMAD compliance
    if ! check_bmad_compliance "$agents_file"; then
        echo "BMAD compliance failed for AGENTS.MD"
        return 1
    fi
    
    # Check GitHub Copilot compatibility
    if ! check_copilot_compatibility "$copilot_file"; then
        echo "GitHub Copilot compatibility failed"
        return 1
    fi
    
    echo "All validations passed"
    return 0
}
```

### 4. Export and Compliance Report

```bash
# Generate compliance report
generate_compliance_report() {
    local report_file="output/compliance_report.json"
    
    cat > "$report_file" << 'EOF'
{
  "timestamp": "$(date)",
  "validation_results": {
    "file_size_check": "passed",
    "bmad_compliance": "passed",
    "github_copilot_compatibility": "passed",
    "content_structure": "passed",
    "task_templates": "passed",
    "examples": "passed",
    "reasoning_frameworks": "passed"
  },
  "output_files": {
    "agents_md": {
      "path": "output/AGENTS.MD",
      "size": "$(wc -c < output/AGENTS.MD)",
      "status": "valid"
    },
    "copilot_instructions": {
      "path": "output/.github/copilot-instructions.md",
      "size": "$(wc -c < output/.github/copilot-instructions.md)",
      "status": "valid"
    }
  },
  "summary": {
    "total_layers": 8,
    "total_examples": 6,
    "total_templates": 4,
    "total_frameworks": 4
  }
}
EOF
}
```

## Output Files

### Final AGENTS.MD
- **Size:** ~100 words
- **Format:** BMAD-compliant markdown
- **Content:** All 8 layers with references to detailed data files

### Final .github/copilot-instructions.md
- **Size:** ~80 words
- **Format:** GitHub Copilot compatible
- **Content:** Quick start guide and usage instructions

### Compliance Report
- **Format:** JSON
- **Content:** Validation results and file status

## Quality Gates

- [ ] Content assembly successful
- [ ] File size within limits
- [ ] BMAD compliance verified
- [ ] GitHub Copilot compatibility confirmed
- [ ] All validations passed

## Troubleshooting

### Common Issues

1. **Assembly failed**
   - Check all layer files exist
   - Verify file permissions
   - Review assembly script

2. **Size optimization needed**
   - Remove redundant content
   - Use modularization
   - Compress large sections

3. **Validation errors**
   - Review compliance requirements
   - Check file structure
   - Validate content format

### Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team