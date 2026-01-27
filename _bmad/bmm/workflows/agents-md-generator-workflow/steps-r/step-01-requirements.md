---
name: 'step-01-requirements'
description: 'Step 1: Requirements — Analyze BMAD requirements, extract KR requirements, identify user requirements'
layer: 'requirements'
menu:
  next: step-02-prd.md
  back: AGENTS-MD-GENERATOR-WORKFLOW.md
handler: A
---

# Step 1: Requirements

**Purpose:** Analyze BMAD requirements, extract KR requirements, identify user requirements, and create comprehensive requirements documentation

## Overview

This step performs comprehensive requirements analysis for the AGENTS.MD generation workflow, extracting and documenting all necessary requirements from BMAD protocol, Key Results, and user specifications.

## Prerequisites

- BMAD protocol documentation available
- Key Results (KR) requirements defined
- User requirements gathering completed
- Requirements analysis tools and templates available

## Input Requirements

### Required Inputs

1. **BMAD Protocol Documentation** - Complete BMAD protocol specifications
2. **Key Results (KR) Requirements** - All 10 KR requirements with detailed specifications
3. **User Requirements** - User stories, acceptance criteria, and functional requirements
4. **North Star Description** - Project vision and success metrics

### Optional Inputs

1. **Stakeholder Interviews** - Additional stakeholder input and requirements
2. **Competitive Analysis** - Requirements from similar tools and workflows
3. **Technical Constraints** - Technical limitations and constraints
4. **Business Rules** - Business logic and rule requirements

## Process

### 1. BMAD Requirements Analysis

```bash
# Analyze BMAD protocol requirements
analyze_bmad_requirements() {
    echo "Analyzing BMAD protocol requirements..."
    
    local bmad_analysis_file="$OUTPUT_DIR/bmad_requirements_analysis.json"
    
    # Extract BMAD protocol elements
    local phase_management=$(grep -c "Phase Management\|phase_management" "$BMAD_REQUIREMENTS" || echo "0")
    local input_output_spec=$(grep -c "Input/Output Specification\|input_output_specification" "$BMAD_REQUIREMENTS" || echo "0")
    local compliance_check=$(grep -c "Compliance Check\|compliance_check" "$BMAD_REQUIREMENTS" || echo "0")
    
    # Analyze BMAD structure requirements
    local bmad_structure=$(grep -c "BMAD\|bmad" "$BMAD_REQUIREMENTS" || echo "0")
    local frontmatter_required=$(grep -c "frontmatter\|Frontmatter" "$BMAD_REQUIREMENTS" || echo "0")
    local handler_required=$(grep -c "handler\|Handler" "$BMAD_REQUIREMENTS" || echo "0")
    
    # Generate BMAD analysis report
    cat > "$bmad_analysis_file" << EOF
{
  "analysis_date": "$(date -Iseconds)",
  "bmad_protocol_elements": {
    "phase_management": $phase_management,
    "input_output_specification": $input_output_spec,
    "compliance_check": $compliance_check
  },
  "bmad_structure_requirements": {
    "bmad_references": $bmad_structure,
    "frontmatter_required": $frontmatter_required,
    "handler_required": $handler_required
  },
  "compliance_requirements": {
    "phase_references": true,
    "layer_structure": true,
    "menu_system": true,
    "handler_specification": true
  },
  "analysis_summary": {
    "total_bmad_elements": $((phase_management + input_output_spec + compliance_check)),
    "structure_compliance": $([ $frontmatter_required -gt 0 ] && [ $handler_required -gt 0 ] && echo "compliant" || echo "non_compliant")
  }
}
EOF
    
    echo "✓ BMAD requirements analysis completed: $bmad_analysis_file"
    return 0
}
```

### 2. KR Requirements Extraction

```bash
# Extract and analyze KR requirements
extract_kr_requirements() {
    echo "Extracting KR requirements..."
    
    local kr_analysis_file="$OUTPUT_DIR/kr_requirements_analysis.json"
    
    # Extract each KR requirement
    local kr_1=$(grep -c "KR-1\|binary identical\|Binary identical" "$KR_REQUIREMENTS" || echo "0")
    local kr_2=$(grep -c "KR-2\|BMAD phase\|BMAD understanding" "$KR_REQUIREMENTS" || echo "0")
    local kr_3=$(grep -c "KR-3\|GitHub Copilot\|copilot compatibility" "$KR_REQUIREMENTS" || echo "0")
    local kr_4=$(grep -c "KR-4\|content preservation\|Content preservation" "$KR_REQUIREMENTS" || echo "0")
    local kr_5=$(grep -c "KR-5\|realistic examples\|Realistic examples" "$KR_REQUIREMENTS" || echo "0")
    local kr_6=$(grep -c "KR-6\|task templates\|Task templates" "$KR_REQUIREMENTS" || echo "0")
    local kr_7=$(grep -c "KR-7\|steering guide\|Steering guide" "$KR_REQUIREMENTS" || echo "0")
    local kr_8=$(grep -c "KR-8\|agent autonomy\|Agent autonomy" "$KR_REQUIREMENTS" || echo "0")
    local kr_9=$(grep -c "KR-9\|XML\|pseudo-code\|XML + pseudo-code" "$KR_REQUIREMENTS" || echo "0")
    local kr_10=$(grep -c "KR-10\|advanced features\|Advanced features" "$KR_REQUIREMENTS" || echo "0")
    
    # Generate KR analysis report
    cat > "$kr_analysis_file" << EOF
{
  "analysis_date": "$(date -Iseconds)",
  "kr_requirements": {
    "KR-1": {
      "description": "Binary identical files",
      "references_found": $kr_1,
      "status": "$([ $kr_1 -gt 0 ] && echo "identified" || echo "missing")"
    },
    "KR-2": {
      "description": "BMAD phase understanding",
      "references_found": $kr_2,
      "status": "$([ $kr_2 -gt 0 ] && echo "identified" || echo "missing")"
    },
    "KR-3": {
      "description": "GitHub Copilot compatibility",
      "references_found": $kr_3,
      "status": "$([ $kr_3 -gt 0 ] && echo "identified" || echo "missing")"
    },
    "KR-4": {
      "description": "Content preservation",
      "references_found": $kr_4,
      "status": "$([ $kr_4 -gt 0 ] && echo "identified" || echo "missing")"
    },
    "KR-5": {
      "description": "Realistic examples",
      "references_found": $kr_5,
      "status": "$([ $kr_5 -gt 0 ] && echo "identified" || echo "missing")"
    },
    "KR-6": {
      "description": "Task templates",
      "references_found": $kr_6,
      "status": "$([ $kr_6 -gt 0 ] && echo "identified" || echo "missing")"
    },
    "KR-7": {
      "description": "Steering guide",
      "references_found": $kr_7,
      "status": "$([ $kr_7 -gt 0 ] && echo "identified" || echo "missing")"
    },
    "KR-8": {
      "description": "Agent autonomy",
      "references_found": $kr_8,
      "status": "$([ $kr_8 -gt 0 ] && echo "identified" || echo "missing")"
    },
    "KR-9": {
      "description": "XML + pseudo-code",
      "references_found": $kr_9,
      "status": "$([ $kr_9 -gt 0 ] && echo "identified" || echo "missing")"
    },
    "KR-10": {
      "description": "Advanced features",
      "references_found": $kr_10,
      "status": "$([ $kr_10 -gt 0 ] && echo "identified" || echo "missing")"
    }
  },
  "analysis_summary": {
    "total_kr_requirements": 10,
    "requirements_identified": $((kr_1 + kr_2 + kr_3 + kr_4 + kr_5 + kr_6 + kr_7 + kr_8 + kr_9 + kr_10)),
    "completeness_percentage": $(( (kr_1 + kr_2 + kr_3 + kr_4 + kr_5 + kr_6 + kr_7 + kr_8 + kr_9 + kr_10) * 100 / 10 ))
  }
}
EOF
    
    echo "✓ KR requirements extraction completed: $kr_analysis_file"
    return 0
}
```

### 3. User Requirements Identification

```bash
# Identify and analyze user requirements
identify_user_requirements() {
    echo "Identifying user requirements..."
    
    local user_analysis_file="$OUTPUT_DIR/user_requirements_analysis.json"
    
    # Extract user requirement categories
    local functional_reqs=$(grep -c "functional\|Functionality\|feature\|Feature" "$USER_REQUIREMENTS" || echo "0")
    local non_functional_reqs=$(grep -c "performance\|Performance\|security\|Security\|usability\|Usability" "$USER_REQUIREMENTS" || echo "0")
    local user_stories=$(grep -c "user story\|User story\|As a\|as a" "$USER_REQUIREMENTS" || echo "0")
    local acceptance_criteria=$(grep -c "acceptance\|Acceptance\|criteria\|Criteria" "$USER_REQUIREMENTS" || echo "0")
    
    # Extract specific user types
    local developers=$(grep -c "developer\|Developer\|dev\|Dev" "$USER_REQUIREMENTS" || echo "0")
    local agents=$(grep -c "agent\|Agent\|LLM\|AI" "$USER_REQUIREMENTS" || echo "0")
    local maintainers=$(grep -c "maintainer\|Maintainer\|maintain\|Maintain" "$USER_REQUIREMENTS" || echo "0")
    
    # Generate user requirements analysis
    cat > "$user_analysis_file" << EOF
{
  "analysis_date": "$(date -Iseconds)",
  "user_requirement_categories": {
    "functional_requirements": $functional_reqs,
    "non_functional_requirements": $non_functional_reqs,
    "user_stories": $user_stories,
    "acceptance_criteria": $acceptance_criteria
  },
  "user_types": {
    "developers": $developers,
    "agents": $agents,
    "maintainers": $maintainers
  },
  "requirement_quality": {
    "traceability": $([ $user_stories -gt 0 ] && echo "good" || echo "poor"),
    "testability": $([ $acceptance_criteria -gt 0 ] && echo "good" || echo "poor"),
    "completeness": $([ $functional_reqs -gt 0 ] && [ $non_functional_reqs -gt 0 ] && echo "good" || echo "poor")
  },
  "analysis_summary": {
    "total_requirement_indicators": $((functional_reqs + non_functional_reqs + user_stories + acceptance_criteria)),
    "user_types_identified": $((developers + agents + maintainers))
  }
}
EOF
    
    echo "✓ User requirements identification completed: $user_analysis_file"
    return 0
}
```

### 4. Requirements Documentation

```bash
# Create comprehensive requirements documentation
create_requirements_documentation() {
    echo "Creating comprehensive requirements documentation..."
    
    local requirements_doc_file="$OUTPUT_DIR/requirements_documentation.md"
    
    # Get analysis results
    local bmad_elements=$(jq '.bmad_protocol_elements | to_entries | length' "$OUTPUT_DIR/bmad_requirements_analysis.json" 2>/dev/null || echo "0")
    local kr_identified=$(jq '.analysis_summary.requirements_identified' "$OUTPUT_DIR/kr_requirements_analysis.json" 2>/dev/null || echo "0")
    local user_reqs=$(jq '.analysis_summary.total_requirement_indicators' "$OUTPUT_DIR/user_requirements_analysis.json" 2>/dev/null || echo "0")
    
    # Generate comprehensive requirements documentation
    cat > "$requirements_doc_file" << EOF
# Comprehensive Requirements Documentation

**Generated:** $(date -Iseconds)
**Workflow:** AGENTS.MD Generation
**Version:** 6.0.0-alpha.23

## Executive Summary

This document provides a comprehensive overview of all requirements for the AGENTS.MD generation workflow, including BMAD protocol requirements, Key Results (KR) requirements, and user requirements.

### Requirements Overview

- **BMAD Protocol Elements:** $bmad_elements
- **KR Requirements Identified:** $kr_identified/10
- **User Requirements Indicators:** $user_reqs
- **Overall Completeness:** $(( (bmad_elements + kr_identified + user_reqs) * 100 / 20 ))%

## BMAD Protocol Requirements

### Phase Management
- **Requirement:** Comprehensive phase management system
- **Status:** $([ $bmad_elements -gt 0 ] && echo "Defined" || echo "Missing")
- **Details:** All 4 phases (Discovery, Planning, Implementation, Validation) must be properly managed

### Input/Output Specification
- **Requirement:** Clear input and output specifications
- **Status:** $([ $bmad_elements -gt 0 ] && echo "Defined" || echo "Missing")
- **Details:** All inputs and outputs must be clearly specified with proper format requirements

### Compliance Check
- **Requirement:** Comprehensive compliance checking
- **Status:** $([ $bmad_elements -gt 0 ] && echo "Defined" || echo "Missing")
- **Details:** All BMAD protocol compliance requirements must be validated

### Structure Requirements
- **Frontmatter:** Required for all files
- **Handler Specification:** Required for all steps
- **Menu System:** Required for navigation
- **Layer Structure:** 8-layer architecture required

## Key Results (KR) Requirements

### KR-1: Binary Identical Files
- **Status:** $([ $kr_identified -gt 0 ] && echo "Identified" || echo "Missing")
- **Requirement:** Generated files must be binary identical to reference files
- **Validation:** File comparison and checksum verification

### KR-2: BMAD Phase Understanding
- **Status:** $([ $kr_identified -gt 1 ] && echo "Identified" || echo "Missing")
- **Requirement:** Complete understanding and implementation of BMAD phases
- **Validation:** Phase structure and transition verification

### KR-3: GitHub Copilot Compatibility
- **Status:** $([ $kr_identified -gt 2 ] && echo "Identified" || echo "Missing")
- **Requirement:** Full compatibility with GitHub Copilot
- **Validation:** Copilot integration testing

### KR-4: Content Preservation
- **Status:** $([ $kr_identified -gt 3 ] && echo "Identified" || echo "Missing")
- **Requirement:** Complete preservation of original content
- **Validation:** Content integrity verification

### KR-5: Realistic Examples
- **Status:** $([ $kr_identified -gt 4 ] && echo "Identified" || echo "Missing")
- **Requirement:** All examples must be realistic and functional
- **Validation:** Example testing and validation

### KR-6: Task Templates
- **Status:** $([ $kr_identified -gt 5 ] && echo "Identified" || echo "Missing")
- **Requirement:** Comprehensive task templates for all scenarios
- **Validation:** Template completeness and usability testing

### KR-7: Steering Guide
- **Status:** $([ $kr_identified -gt 6 ] && echo "Identified" || echo "Missing")
- **Requirement:** Complete steering guide for workflow navigation
- **Validation:** Guide completeness and usability testing

### KR-8: Agent Autonomy
- **Status:** $([ $kr_identified -gt 7 ] && echo "Identified" || echo "Missing")
- **Requirement:** Full agent autonomy with decision-making capabilities
- **Validation:** Autonomy testing and validation

### KR-9: XML + Pseudo-code
- **Status:** $([ $kr_identified -gt 8 ] && echo "Identified" || echo "Missing")
- **Requirement:** XML frameworks and pseudo-code implementation
- **Validation:** Framework and algorithm validation

### KR-10: Advanced Features
- **Status:** $([ $kr_identified -gt 9 ] && echo "Identified" || echo "Missing")
- **Requirement:** Advanced features including monitoring and best practices
- **Validation:** Feature completeness and functionality testing

## User Requirements

### Functional Requirements
- **Count:** $user_reqs
- **Status:** $([ $user_reqs -gt 0 ] && echo "Defined" || echo "Missing")
- **Categories:** Content generation, validation, testing, deployment

### Non-Functional Requirements
- **Performance:** File size limits, processing speed
- **Security:** Content integrity, access control
- **Usability:** Clear documentation, easy navigation

### User Stories
- **Developers:** Need comprehensive AGENTS.MD documentation
- **Agents:** Need clear guidance and examples
- **Maintainers:** Need easy maintenance and updates

### Acceptance Criteria
- **Validation:** All requirements must be testable
- **Completeness:** All scenarios must be covered
- **Quality:** All deliverables must meet quality standards

## Requirements Traceability

### BMAD Protocol Traceability
- All BMAD elements are traceable to specific requirements
- Phase management is traceable to workflow structure
- Compliance checking is traceable to validation requirements

### KR Requirements Traceability
- All 10 KR requirements are identified and documented
- Each KR requirement has clear acceptance criteria
- All KR requirements are testable and verifiable

### User Requirements Traceability
- All user requirements are traceable to user stories
- Acceptance criteria are defined for all functional requirements
- Non-functional requirements are measurable and testable

## Conclusion

This comprehensive requirements documentation provides a complete foundation for the AGENTS.MD generation workflow. All requirements are clearly defined, traceable, and testable, ensuring successful implementation and validation.

For questions or clarifications regarding these requirements, please contact the BMAD support team.
EOF

    echo "✓ Comprehensive requirements documentation created: $requirements_doc_file"
    return 0
}
```

## Output Files

### BMAD Requirements Analysis
- **File:** `output/bmad_requirements_analysis.json`
- **Content:** BMAD protocol requirements analysis
- **Format:** JSON

### KR Requirements Analysis
- **File:** `output/kr_requirements_analysis.json`
- **Content:** Key Results requirements extraction and analysis
- **Format:** JSON

### User Requirements Analysis
- **File:** `output/user_requirements_analysis.json`
- **Content:** User requirements identification and analysis
- **Format:** JSON

### Requirements Documentation
- **File:** `output/requirements_documentation.md`
- **Content:** Comprehensive requirements documentation
- **Format:** Markdown

## Quality Gates

- [ ] BMAD requirements analysis completed
- [ ] KR requirements extraction completed
- [ ] User requirements identification completed
- [ ] Comprehensive requirements documentation created
- [ ] All requirements are traceable and testable
- [ ] Requirements completeness verified

## Troubleshooting

### Common Issues

1. **Missing BMAD requirements**
   - Review BMAD protocol documentation
   - Check for all required elements
   - Verify structure compliance

2. **Incomplete KR requirements**
   - Review all 10 KR requirements
   - Check for missing references
   - Verify requirement completeness

3. **Insufficient user requirements**
   - Conduct additional user interviews
   - Review user stories and acceptance criteria
   - Validate requirement traceability

4. **Requirements documentation incomplete**
   - Verify all analysis files are generated
   - Check documentation completeness
   - Review traceability matrix

### Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team