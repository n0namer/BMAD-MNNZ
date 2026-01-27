---
name: 'step-02-test'
description: 'Step 2: Test — Execute comprehensive testing, validate content functionality, verify integration compatibility'
layer: 'test'
menu:
  next: step-03-audit.md
  back: step-01-validate.md
handler: A
---

# Step 2: Test

**Purpose:** Execute comprehensive testing, validate content functionality, verify integration compatibility, and ensure all components work as expected

## Overview

This step performs comprehensive testing of AGENTS.MD content to ensure functionality, integration compatibility, and overall system reliability.

## Prerequisites

- AGENTS.MD file validated and ready for testing
- Testing environment configured
- Test cases and scenarios defined
- Testing tools and frameworks available

## Input Requirements

### Required Inputs

1. **Validated AGENTS.MD** - File ready for testing
2. **Test Cases** - Comprehensive test cases and scenarios
3. **Testing Environment** - Configured testing environment
4. **Test Data** - Test data and scenarios

### Optional Inputs

1. **Performance Benchmarks** - Performance testing criteria
2. **Integration Test Scenarios** - Integration testing requirements
3. **User Acceptance Criteria** - User acceptance testing requirements

## Process

### 1. Functional Testing

```bash
# Execute functional testing
execute_functional_testing() {
    echo "Executing functional testing..."
    
    local agents_file="$1"
    local test_results_file="$OUTPUT_DIR/functional_test_results.json"
    
    # Test file loading and parsing
    local load_test_passed=true
    local parse_test_passed=true
    
    # Test file loading
    if [ ! -f "$agents_file" ]; then
        load_test_passed=false
        echo "ERROR: AGENTS.MD file not found"
    else
        echo "✓ File loading test passed"
    fi
    
    # Test file parsing
    if ! grep -q "^# " "$agents_file"; then
        parse_test_passed=false
        echo "ERROR: Invalid markdown structure"
    else
        echo "✓ File parsing test passed"
    fi
    
    # Test content structure
    local structure_test_passed=true
    local required_sections=("Overview" "Usage" "Examples")
    
    for section in "${required_sections[@]}"; do
        if ! grep -q "## $section" "$agents_file"; then
            structure_test_passed=false
            echo "ERROR: Missing required section: $section"
        fi
    done
    
    if [ "$structure_test_passed" = true ]; then
        echo "✓ Content structure test passed"
    fi
    
    # Generate functional test results
    cat > "$test_results_file" << EOF
{
  "test_date": "$(date -Iseconds)",
  "file": "$agents_file",
  "tests": {
    "file_loading": {
      "status": "$([ $load_test_passed = true ] && echo "passed" || echo "failed")",
      "details": "File exists and is accessible"
    },
    "file_parsing": {
      "status": "$([ $parse_test_passed = true ] && echo "passed" || echo "failed")",
      "details": "File has valid markdown structure"
    },
    "content_structure": {
      "status": "$([ $structure_test_passed = true ] && echo "passed" || echo "failed")",
      "details": "All required sections present"
    }
  },
  "overall_status": "$([ $load_test_passed = true ] && [ $parse_test_passed = true ] && [ $structure_test_passed = true ] && echo "passed" || echo "failed")"
}
EOF
    
    if [ "$load_test_passed" = true ] && [ "$parse_test_passed" = true ] && [ "$structure_test_passed" = true ]; then
        echo "✓ Functional testing completed successfully"
        return 0
    else
        echo "✗ Functional testing failed"
        return 1
    fi
}
```

### 2. Integration Testing

```bash
# Execute integration testing
execute_integration_testing() {
    echo "Executing integration testing..."
    
    local agents_file="$1"
    local test_results_file="$OUTPUT_DIR/integration_test_results.json"
    
    # Test GitHub Copilot integration
    local copilot_integration_passed=true
    
    # Check for GitHub Copilot compatibility markers
    local copilot_markers=$(grep -c "GitHub Copilot\|copilot" "$agents_file" || echo "0")
    
    if [ "$copilot_markers" -eq 0 ]; then
        copilot_integration_passed=false
        echo "WARNING: No GitHub Copilot integration markers found"
    else
        echo "✓ GitHub Copilot integration markers found"
    fi
    
    # Test BMAD protocol integration
    local bmad_integration_passed=true
    local bmad_markers=$(grep -c "BMAD" "$agents_file" || echo "0")
    
    if [ "$bmad_markers" -lt 5 ]; then
        bmad_integration_passed=false
        echo "WARNING: Insufficient BMAD protocol markers"
    else
        echo "✓ BMAD protocol integration verified"
    fi
    
    # Test phase integration
    local phase_integration_passed=true
    local phase_markers=$(grep -c "Phase [1-4]" "$agents_file" || echo "0")
    
    if [ "$phase_markers" -lt 4 ]; then
        phase_integration_passed=false
        echo "WARNING: Insufficient phase markers"
    else
        echo "✓ Phase integration verified"
    fi
    
    # Generate integration test results
    cat > "$test_results_file" << EOF
{
  "test_date": "$(date -Iseconds)",
  "file": "$agents_file",
  "tests": {
    "github_copilot_integration": {
      "status": "$([ $copilot_integration_passed = true ] && echo "passed" || echo "failed")",
      "markers_found": $copilot_markers,
      "details": "GitHub Copilot integration markers present"
    },
    "bmad_protocol_integration": {
      "status": "$([ $bmad_integration_passed = true ] && echo "passed" || echo "failed")",
      "markers_found": $bmad_markers,
      "details": "BMAD protocol integration verified"
    },
    "phase_integration": {
      "status": "$([ $phase_integration_passed = true ] && echo "passed" || echo "failed")",
      "markers_found": $phase_markers,
      "details": "Phase integration verified"
    }
  },
  "overall_status": "$([ $copilot_integration_passed = true ] && [ $bmad_integration_passed = true ] && [ $phase_integration_passed = true ] && echo "passed" || echo "failed")"
}
EOF
    
    if [ "$copilot_integration_passed" = true ] && [ "$bmad_integration_passed" = true ] && [ "$phase_integration_passed" = true ]; then
        echo "✓ Integration testing completed successfully"
        return 0
    else
        echo "✗ Integration testing failed"
        return 1
    fi
}
```

### 3. Performance Testing

```bash
# Execute performance testing
execute_performance_testing() {
    echo "Executing performance testing..."
    
    local agents_file="$1"
    local test_results_file="$OUTPUT_DIR/performance_test_results.json"
    
    # Test file size performance
    local file_size=$(wc -c < "$agents_file")
    local size_performance_passed=true
    
    if [ "$file_size" -gt 102400 ]; then
        size_performance_passed=false
        echo "WARNING: File size may impact performance: ${file_size} bytes"
    else
        echo "✓ File size performance acceptable: ${file_size} bytes"
    fi
    
    # Test parsing performance
    local parse_time_start=$(date +%s.%N)
    grep -c "^#" "$agents_file" > /dev/null
    local parse_time_end=$(date +%s.%N)
    local parse_time=$(echo "$parse_time_end - $parse_time_start" | bc)
    
    local parse_performance_passed=true
    if (( $(echo "$parse_time > 1.0" | bc -l) )); then
        parse_performance_passed=false
        echo "WARNING: Parsing performance may be slow: ${parse_time} seconds"
    else
        echo "✓ Parsing performance acceptable: ${parse_time} seconds"
    fi
    
    # Test content loading performance
    local load_time_start=$(date +%s.%N)
    cat "$agents_file" > /dev/null
    local load_time_end=$(date +%s.%N)
    local load_time=$(echo "$load_time_end - $load_time_start" | bc)
    
    local load_performance_passed=true
    if (( $(echo "$load_time > 2.0" | bc -l) )); then
        load_performance_passed=false
        echo "WARNING: Loading performance may be slow: ${load_time} seconds"
    else
        echo "✓ Loading performance acceptable: ${load_time} seconds"
    fi
    
    # Generate performance test results
    cat > "$test_results_file" << EOF
{
  "test_date": "$(date -Iseconds)",
  "file": "$agents_file",
  "tests": {
    "file_size_performance": {
      "status": "$([ $size_performance_passed = true ] && echo "passed" || echo "failed")",
      "file_size": $file_size,
      "details": "File size within performance limits"
    },
    "parsing_performance": {
      "status": "$([ $parse_performance_passed = true ] && echo "passed" || echo "failed")",
      "parse_time": $parse_time,
      "details": "Parsing time within acceptable limits"
    },
    "loading_performance": {
      "status": "$([ $load_performance_passed = true ] && echo "passed" || echo "failed")",
      "load_time": $load_time,
      "details": "Loading time within acceptable limits"
    }
  },
  "overall_status": "$([ $size_performance_passed = true ] && [ $parse_performance_passed = true ] && [ $load_performance_passed = true ] && echo "passed" || echo "failed")"
}
EOF
    
    if [ "$size_performance_passed" = true ] && [ "$parse_performance_passed" = true ] && [ "$load_performance_passed" = true ]; then
        echo "✓ Performance testing completed successfully"
        return 0
    else
        echo "✗ Performance testing failed"
        return 1
    fi
}
```

### 4. Compatibility Testing

```bash
# Execute compatibility testing
execute_compatibility_testing() {
    echo "Executing compatibility testing..."
    
    local agents_file="$1"
    local test_results_file="$OUTPUT_DIR/compatibility_test_results.json"
    
    # Test markdown compatibility
    local markdown_compatibility_passed=true
    local markdown_version=$(grep -c "^# " "$agents_file" || echo "0")
    
    if [ "$markdown_version" -eq 0 ]; then
        markdown_compatibility_passed=false
        echo "ERROR: Invalid markdown format"
    else
        echo "✓ Markdown compatibility verified"
    fi
    
    # Test cross-platform compatibility
    local cross_platform_passed=true
    
    # Check for platform-specific content
    local windows_refs=$(grep -c "Windows\|\.exe\|\.bat" "$agents_file" || echo "0")
    local linux_refs=$(grep -c "Linux\|\.sh\|bash" "$agents_file" || echo "0")
    local macos_refs=$(grep -c "macOS\|Mac\|\.app" "$agents_file" || echo "0")
    
    if [ "$windows_refs" -gt 0 ] || [ "$linux_refs" -gt 0 ] || [ "$macos_refs" -gt 0 ]; then
        echo "INFO: Platform-specific references found (Windows: $windows_refs, Linux: $linux_refs, macOS: $macos_refs)"
    else
        echo "✓ Cross-platform compatibility verified"
    fi
    
    # Test tool compatibility
    local tool_compatibility_passed=true
    
    # Check for tool-specific references
    local git_refs=$(grep -c "git\|Git" "$agents_file" || echo "0")
    local github_refs=$(grep -c "GitHub\|github" "$agents_file" || echo "0")
    local copilot_refs=$(grep -c "Copilot\|copilot" "$agents_file" || echo "0")
    
    if [ "$git_refs" -gt 0 ] || [ "$github_refs" -gt 0 ] || [ "$copilot_refs" -gt 0 ]; then
        echo "INFO: Tool-specific references found (Git: $git_refs, GitHub: $github_refs, Copilot: $copilot_refs)"
    else
        echo "✓ Tool compatibility verified"
    fi
    
    # Generate compatibility test results
    cat > "$test_results_file" << EOF
{
  "test_date": "$(date -Iseconds)",
  "file": "$agents_file",
  "tests": {
    "markdown_compatibility": {
      "status": "$([ $markdown_compatibility_passed = true ] && echo "passed" || echo "failed")",
      "details": "Markdown format compatibility verified"
    },
    "cross_platform_compatibility": {
      "status": "$([ $cross_platform_passed = true ] && echo "passed" || echo "failed")",
      "platform_references": {
        "windows": $windows_refs,
        "linux": $linux_refs,
        "macos": $macos_refs
      },
      "details": "Cross-platform compatibility verified"
    },
    "tool_compatibility": {
      "status": "$([ $tool_compatibility_passed = true ] && echo "passed" || echo "failed")",
      "tool_references": {
        "git": $git_refs,
        "github": $github_refs,
        "copilot": $copilot_refs
      },
      "details": "Tool compatibility verified"
    }
  },
  "overall_status": "$([ $markdown_compatibility_passed = true ] && [ $cross_platform_passed = true ] && [ $tool_compatibility_passed = true ] && echo "passed" || echo "failed")"
}
EOF
    
    if [ "$markdown_compatibility_passed" = true ] && [ "$cross_platform_passed" = true ] && [ "$tool_compatibility_passed" = true ]; then
        echo "✓ Compatibility testing completed successfully"
        return 0
    else
        echo "✗ Compatibility testing failed"
        return 1
    fi
}
```

## Output Files

### Functional Test Results
- **File:** `output/functional_test_results.json`
- **Content:** Functional testing results
- **Format:** JSON

### Integration Test Results
- **File:** `output/integration_test_results.json`
- **Content:** Integration testing results
- **Format:** JSON

### Performance Test Results
- **File:** `output/performance_test_results.json`
- **Content:** Performance testing results
- **Format:** JSON

### Compatibility Test Results
- **File:** `output/compatibility_test_results.json`
- **Content:** Compatibility testing results
- **Format:** JSON

## Quality Gates

- [ ] Functional testing passed
- [ ] Integration testing passed
- [ ] Performance testing passed
- [ ] Compatibility testing passed
- [ ] All test results documented
- [ ] No critical failures detected

## Troubleshooting

### Common Issues

1. **Functional testing failed**
   - Check file accessibility
   - Verify markdown structure
   - Ensure required sections present

2. **Integration testing failed**
   - Add missing integration markers
   - Verify BMAD protocol references
   - Check phase markers

3. **Performance testing failed**
   - Optimize file size
   - Improve parsing efficiency
   - Reduce loading time

4. **Compatibility testing failed**
   - Fix markdown format issues
   - Remove platform-specific dependencies
   - Ensure tool compatibility

### Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team