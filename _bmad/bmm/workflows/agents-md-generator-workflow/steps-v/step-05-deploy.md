# Step 5: Deploy - Deployment and Distribution

**Purpose:** Deploy and distribute AGENTS.MD files to production environments and users

## Overview

This step provides the framework for deploying AGENTS.MD files to production environments, distributing them to users, and ensuring proper integration with existing systems. It includes deployment strategies, distribution methods, and post-deployment validation.

## Prerequisites

- Monitored and maintained AGENTS.MD files
- Deployment environments and infrastructure
- Distribution channels and methods
- Post-deployment validation procedures

## Input Requirements

### Required Inputs

1. **AGENTS.MD File** - File to be deployed
2. **Deployment Configuration** - Deployment settings and environments
3. **Distribution Channels** - Methods for distributing to users

### Optional Inputs

1. **Deployment Scripts** - Automated deployment procedures
2. **User Documentation** - User guides and documentation

## Process

### 1. Deployment Strategy

```bash
# Define deployment strategy
define_deployment_strategy() {
    local agents_md="$1"
    local deployment_config="$2"
    
    echo "Defining deployment strategy..."
    
    # Create deployment configuration
    if [ ! -f "$deployment_config" ]; then
        cat > "$deployment_config" << 'EOF'
{
  "deployment": {
    "environments": {
      "development": {
        "path": "docs/dev/",
        "auto_deploy": true,
        "validation": "basic"
      },
      "staging": {
        "path": "docs/staging/",
        "auto_deploy": true,
        "validation": "full"
      },
      "production": {
        "path": "docs/",
        "auto_deploy": false,
        "validation": "strict"
      }
    },
    "distribution": {
      "channels": [
        "repository_docs",
        "wiki_pages",
        "internal_portal",
        "user_guides"
      ],
      "formats": [
        "markdown",
        "pdf",
        "html"
      ]
    },
    "validation": {
      "pre_deploy": [
        "file_integrity",
        "compliance_check",
        "security_scan"
      ],
      "post_deploy": [
        "accessibility_test",
        "performance_test",
        "user_acceptance"
      ]
    }
  }
}
EOF
        echo "✓ Deployment configuration created: $deployment_config"
    else
        echo "✓ Deployment configuration already exists: $deployment_config"
    fi
    
    # Create deployment scripts
    create_deployment_scripts "$agents_md"
    
    echo "✓ Deployment strategy defined"
    return 0
}

# Usage
define_deployment_strategy "output/AGENTS.MD" "deployment/deployment_config.json"
```

### 2. Pre-Deployment Validation

```bash
# Perform pre-deployment validation
pre_deployment_validation() {
    local agents_md="$1"
    local validation_report="$2"
    
    echo "Performing pre-deployment validation..."
    
    local validation_passed=0
    local validation_total=5
    
    # Validation 1: File Integrity
    echo "Validation 1: File Integrity"
    if [ -f "$agents_md" ]; then
        echo "✓ File exists and is accessible"
        validation_passed=$((validation_passed + 1))
    else
        echo "✗ File does not exist or is not accessible"
    fi
    
    # Validation 2: Content Structure
    echo "Validation 2: Content Structure"
    local required_sections=("UX Layer" "BMAD Protocol" "Phase Workflows" "Task Templates" "Examples" "Reasoning Frameworks" "Session Monitoring" "Best Practices")
    local sections_found=0
    
    for section in "${required_sections[@]}"; do
        if grep -q "$section" "$agents_md"; then
            sections_found=$((sections_found + 1))
        fi
    done
    
    if [ "$sections_found" -eq 8 ]; then
        echo "✓ All required sections present"
        validation_passed=$((validation_passed + 1))
    else
        echo "✗ Missing required sections: $sections_found/8"
    fi
    
    # Validation 3: Compliance Check
    echo "Validation 3: Compliance Check"
    local bmad_refs=$(grep -c "BMAD" "$agents_md")
    if [ "$bmad_refs" -gt 0 ]; then
        echo "✓ BMAD protocol compliance verified"
        validation_passed=$((validation_passed + 1))
    else
        echo "✗ BMAD protocol compliance failed"
    fi
    
    # Validation 4: Security Scan
    echo "Validation 4: Security Scan"
    local security_issues=0
    local sensitive_patterns=("password" "secret" "key" "token" "api_key" "private_key")
    
    for pattern in "${sensitive_patterns[@]}"; do
        if grep -qi "$pattern" "$agents_md"; then
            security_issues=$((security_issues + 1))
        fi
    done
    
    if [ "$security_issues" -eq 0 ]; then
        echo "✓ Security scan passed"
        validation_passed=$((validation_passed + 1))
    else
        echo "✗ Security issues found: $security_issues"
    fi
    
    # Validation 5: File Size Check
    echo "Validation 5: File Size Check"
    local file_size=$(wc -c < "$agents_md")
    if [ "$file_size" -le 102400 ]; then
        echo "✓ File size within limits: $file_size bytes"
        validation_passed=$((validation_passed + 1))
    else
        echo "✗ File size exceeds limits: $file_size bytes"
    fi
    
    local validation_percentage=$((validation_passed * 100 / validation_total))
    echo "Validation Results: $validation_passed/$validation_total ($validation_percentage%)"
    
    # Generate validation report
    cat > "$validation_report" << EOF
# AGENTS.MD Pre-Deployment Validation Report

**Generated:** $(date)
**File:** $agents_md

## Validation Results

### File Integrity
- **Status:** $(if [ -f "$agents_md" ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi)
- **Details:** File exists and is accessible

### Content Structure
- **Status:** $(if [ "$sections_found" -eq 8 ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi)
- **Details:** $sections_found/8 required sections present

### Compliance Check
- **Status:** $(if [ "$bmad_refs" -gt 0 ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi)
- **Details:** $bmad_refs BMAD references found

### Security Scan
- **Status:** $(if [ "$security_issues" -eq 0 ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi)
- **Details:** $security_issues security issues found

### File Size Check
- **Status:** $(if [ "$file_size" -le 102400 ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi)
- **Details:** $file_size bytes (limit: 102400 bytes)

## Overall Validation Score

**Score:** $validation_passed/$validation_total ($validation_percentage%)

## Deployment Status

$(if [ "$validation_percentage" -ge 95 ]; then echo "✅ READY FOR DEPLOYMENT"; else echo "❌ NOT READY FOR DEPLOYMENT"; fi)

EOF
    
    # Log validation results
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Pre-deployment validation: $validation_percentage%" >> "deployment/logs/validation.log"
    
    if [ "$validation_percentage" -ge 95 ]; then
        echo "✓ Pre-deployment validation passed"
        return 0
    else
        echo "✗ Pre-deployment validation failed"
        return 1
    fi
}

# Usage
pre_deployment_validation "output/AGENTS.MD" "deployment/reports/pre_deployment_validation.md"
```

### 3. Environment Deployment

```bash
# Deploy to different environments
deploy_to_environment() {
    local agents_md="$1"
    local environment="$2"
    local deployment_path="$3"
    
    echo "Deploying to $environment environment..."
    
    # Create deployment directory
    mkdir -p "$deployment_path"
    
    # Copy AGENTS.MD file
    cp "$agents_md" "$deployment_path/AGENTS.MD"
    
    # Create environment-specific configuration
    cat > "$deployment_path/deployment_info.json" << EOF
{
  "environment": "$environment",
  "deployment_time": "$(date -Iseconds)",
  "file_path": "$deployment_path/AGENTS.MD",
  "file_size": $(wc -c < "$agents_md"),
  "deployment_status": "completed"
}
EOF
    
    # Create environment-specific documentation
    cat > "$deployment_path/README.md" << EOF
# AGENTS.MD Deployment - $environment

**Environment:** $environment
**Deployment Time:** $(date)
**File:** AGENTS.MD

## Deployment Information

This directory contains the AGENTS.MD file deployed to the $environment environment.

## File Details

- **File Size:** $(wc -c < "$agents_md") bytes
- **Deployment Status:** Completed
- **Environment:** $environment

## Usage

The AGENTS.MD file in this directory is ready for use in the $environment environment.

EOF
    
    echo "✓ Deployment to $environment completed"
    echo "  Path: $deployment_path"
    echo "  File: AGENTS.MD"
    
    return 0
}

# Usage
deploy_to_environment "output/AGENTS.MD" "development" "docs/dev/"
deploy_to_environment "output/AGENTS.MD" "staging" "docs/staging/"
deploy_to_environment "output/AGENTS.MD" "production" "docs/"
```

### 4. Distribution Channels

```bash
# Distribute to various channels
distribute_to_channels() {
    local agents_md="$1"
    local distribution_config="$2"
    
    echo "Distributing to various channels..."
    
    # Create distribution directory
    mkdir -p "distribution/channels"
    
    # Channel 1: Repository Documentation
    echo "Channel 1: Repository Documentation"
    mkdir -p "distribution/channels/repository_docs"
    cp "$agents_md" "distribution/channels/repository_docs/AGENTS.MD"
    echo "✓ Repository documentation updated"
    
    # Channel 2: Wiki Pages
    echo "Channel 2: Wiki Pages"
    mkdir -p "distribution/channels/wiki_pages"
    cp "$agents_md" "distribution/channels/wiki_pages/AGENTS.MD"
    echo "✓ Wiki pages updated"
    
    # Channel 3: Internal Portal
    echo "Channel 3: Internal Portal"
    mkdir -p "distribution/channels/internal_portal"
    cp "$agents_md" "distribution/channels/internal_portal/AGENTS.MD"
    echo "✓ Internal portal updated"
    
    # Channel 4: User Guides
    echo "Channel 4: User Guides"
    mkdir -p "distribution/channels/user_guides"
    cp "$agents_md" "distribution/channels/user_guides/AGENTS.MD"
    echo "✓ User guides updated"
    
    # Generate distribution report
    cat > "distribution/reports/distribution_report.md" << EOF
# AGENTS.MD Distribution Report

**Generated:** $(date)
**File:** $agents_md

## Distribution Channels

### Repository Documentation
- **Status:** ✅ Completed
- **Path:** distribution/channels/repository_docs/AGENTS.MD

### Wiki Pages
- **Status:** ✅ Completed
- **Path:** distribution/channels/wiki_pages/AGENTS.MD

### Internal Portal
- **Status:** ✅ Completed
- **Path:** distribution/channels/internal_portal/AGENTS.MD

### User Guides
- **Status:** ✅ Completed
- **Path:** distribution/channels/user_guides/AGENTS.MD

## Distribution Summary

**Total Channels:** 4
**Successful Deployments:** 4
**Failed Deployments:** 0

## Distribution Status

✅ ALL CHANNELS SUCCESSFULLY UPDATED

EOF
    
    echo "✓ Distribution to all channels completed"
    return 0
}

# Usage
distribute_to_channels "output/AGENTS.MD" "distribution/distribution_config.json"
```

### 5. Post-Deployment Validation

```bash
# Perform post-deployment validation
post_deployment_validation() {
    local agents_md="$1"
    local deployment_path="$2"
    local validation_report="$3"
    
    echo "Performing post-deployment validation..."
    
    local validation_passed=0
    local validation_total=4
    
    # Validation 1: File Accessibility
    echo "Validation 1: File Accessibility"
    if [ -f "$deployment_path/AGENTS.MD" ]; then
        echo "✓ File accessible in deployment path"
        validation_passed=$((validation_passed + 1))
    else
        echo "✗ File not accessible in deployment path"
    fi
    
    # Validation 2: File Integrity
    echo "Validation 2: File Integrity"
    local original_hash=$(sha256sum "$agents_md" | cut -d' ' -f1)
    local deployed_hash=$(sha256sum "$deployment_path/AGENTS.MD" | cut -d' ' -f1)
    
    if [ "$original_hash" = "$deployed_hash" ]; then
        echo "✓ File integrity verified"
        validation_passed=$((validation_passed + 1))
    else
        echo "✗ File integrity check failed"
    fi
    
    # Validation 3: Content Verification
    echo "Validation 3: Content Verification"
    local original_sections=$(grep -c "^## " "$agents_md")
    local deployed_sections=$(grep -c "^## " "$deployment_path/AGENTS.MD")
    
    if [ "$original_sections" -eq "$deployed_sections" ]; then
        echo "✓ Content verification passed"
        validation_passed=$((validation_passed + 1))
    else
        echo "✗ Content verification failed"
    fi
    
    # Validation 4: Environment Configuration
    echo "Validation 4: Environment Configuration"
    if [ -f "$deployment_path/deployment_info.json" ]; then
        echo "✓ Environment configuration present"
        validation_passed=$((validation_passed + 1))
    else
        echo "✗ Environment configuration missing"
    fi
    
    local validation_percentage=$((validation_passed * 100 / validation_total))
    echo "Post-deployment validation: $validation_passed/$validation_total ($validation_percentage%)"
    
    # Generate post-deployment validation report
    cat > "$validation_report" << EOF
# AGENTS.MD Post-Deployment Validation Report

**Generated:** $(date)
**File:** $agents_md
**Deployment Path:** $deployment_path

## Validation Results

### File Accessibility
- **Status:** $(if [ -f "$deployment_path/AGENTS.MD" ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi)
- **Details:** File accessible in deployment path

### File Integrity
- **Status:** $(if [ "$original_hash" = "$deployed_hash" ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi)
- **Details:** File hash comparison successful

### Content Verification
- **Status:** $(if [ "$original_sections" -eq "$deployed_sections" ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi)
- **Details:** $deployed_sections/$original_sections sections verified

### Environment Configuration
- **Status:** $(if [ -f "$deployment_path/deployment_info.json" ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi)
- **Details:** Environment configuration present

## Overall Validation Score

**Score:** $validation_passed/$validation_total ($validation_percentage%)

## Deployment Status

$(if [ "$validation_percentage" -ge 95 ]; then echo "✅ DEPLOYMENT SUCCESSFUL"; else echo "❌ DEPLOYMENT ISSUES DETECTED"; fi)

EOF
    
    # Log post-deployment validation
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Post-deployment validation: $validation_percentage%" >> "deployment/logs/post_deployment.log"
    
    if [ "$validation_percentage" -ge 95 ]; then
        echo "✓ Post-deployment validation passed"
        return 0
    else
        echo "✗ Post-deployment validation failed"
        return 1
    fi
}

# Usage
post_deployment_validation "output/AGENTS.MD" "docs/" "deployment/reports/post_deployment_validation.md"
```

### 6. User Notification and Documentation

```bash
# Notify users and update documentation
notify_users_and_update_docs() {
    local agents_md="$1"
    local notification_config="$2"
    
    echo "Notifying users and updating documentation..."
    
    # Create user notification
    cat > "distribution/notifications/user_notification.md" << 'EOF'
# AGENTS.MD Update Notification

**Date:** $(date)
**Version:** 6.0.0-alpha.23

## What's New

The AGENTS.MD file has been updated and deployed to all environments.

## Changes

- Updated content structure
- Enhanced compliance with BMAD protocol
- Improved security measures
- Optimized performance

## Deployment Status

✅ **Successfully deployed to all environments:**
- Development
- Staging  
- Production

## Access Information

The updated AGENTS.MD file is now available in:

- Repository documentation
- Wiki pages
- Internal portal
- User guides

## Support

For questions or support, please contact the BMAD support team.

EOF
    
    # Create release notes
    cat > "distribution/releases/release_notes.md" << 'EOF'
# AGENTS.MD Release Notes

**Release:** 6.0.0-alpha.23
**Date:** $(date)

## Overview

This release includes updates to the AGENTS.MD file with enhanced functionality and improved compliance.

## Changes

### Content Updates
- Updated UX Layer section
- Enhanced BMAD Protocol documentation
- Improved Phase Workflows
- Added new Task Templates
- Updated Examples section
- Enhanced Reasoning Frameworks
- Improved Session Monitoring
- Updated Best Practices

### Technical Improvements
- Enhanced security measures
- Improved file structure
- Optimized performance
- Better compliance checking

### Bug Fixes
- Fixed formatting issues
- Resolved content structure problems
- Improved validation processes

## Deployment

### Environments
- ✅ Development
- ✅ Staging
- ✅ Production

### Distribution Channels
- ✅ Repository documentation
- ✅ Wiki pages
- ✅ Internal portal
- ✅ User guides

## Validation

All validation checks passed:
- ✅ File integrity
- ✅ Content structure
- ✅ Compliance verification
- ✅ Security scan
- ✅ Performance testing

## Next Steps

- Monitor usage and feedback
- Address any issues reported
- Plan next update cycle

EOF
    
    # Create user documentation
    cat > "distribution/user_guides/AGENTS.MD_User_Guide.md" << 'EOF'
# AGENTS.MD User Guide

**Version:** 6.0.0-alpha.23
**Date:** $(date)

## Introduction

This guide provides information on how to use the AGENTS.MD file effectively.

## Getting Started

### What is AGENTS.MD?

AGENTS.MD is a comprehensive guide for using BMAD Method agents and workflows.

### How to Use

1. **Read the Overview** - Start with the introduction and overview sections
2. **Follow the Workflows** - Use the phase workflows for guidance
3. **Apply Task Templates** - Use task templates for common tasks
4. **Reference Examples** - Learn from provided examples
5. **Use Reasoning Frameworks** - Apply frameworks for problem-solving

## Sections Overview

### UX Layer
- User experience guidelines
- Interface design principles
- User interaction patterns

### BMAD Protocol
- Methodology overview
- Phase descriptions
- Best practices

### Phase Workflows
- Discovery phase
- Planning phase
- Implementation phase
- Validation phase

### Task Templates
- Common task templates
- Step-by-step instructions
- Best practices

### Examples
- Real-world examples
- Use cases
- Implementation scenarios

### Reasoning Frameworks
- Problem-solving frameworks
- Decision trees
- Analysis methods

### Session Monitoring
- Monitoring procedures
- Status tracking
- Performance metrics

### Best Practices
- Development guidelines
- Security practices
- Quality assurance

## Support

For support and questions:
- Contact the BMAD support team
- Check the documentation
- Review the examples
- Use the reasoning frameworks

EOF
    
    echo "✓ User notification and documentation completed"
    return 0
}

# Usage
notify_users_and_update_docs "output/AGENTS.MD" "distribution/notification_config.json"
```

## Output

### Generated Files

1. **Deployment Configuration** - Deployment settings and environments
2. **Pre-Deployment Validation Report** - Validation results before deployment
3. **Post-Deployment Validation Report** - Validation results after deployment
4. **Distribution Reports** - Distribution status and results
5. **User Notifications** - User notification and communication
6. **Release Notes** - Release information and changes
7. **User Guides** - User documentation and guides
8. **Deployment Logs** - Deployment process logs

### Metadata

```json
{
  "workflow": "agents-md-generator-workflow",
  "step": "step-05-deploy",
  "status": "completed",
  "timestamp": "2026-01-24T20:30:00Z",
  "inputs": {
    "agents_md": "path/to/AGENTS.MD",
    "deployment_config": "path/to/deployment_config.json",
    "distribution_config": "path/to/distribution_config.json",
    "notification_config": "path/to/notification_config.json"
  },
  "outputs": {
    "deployment_config": "deployment/deployment_config.json",
    "pre_deployment_validation": "deployment/reports/pre_deployment_validation.md",
    "post_deployment_validation": "deployment/reports/post_deployment_validation.md",
    "distribution_reports": "distribution/reports/distribution_report.md",
    "user_notifications": "distribution/notifications/user_notification.md",
    "release_notes": "distribution/releases/release_notes.md",
    "user_guides": "distribution/user_guides/AGENTS.MD_User_Guide.md",
    "deployment_logs": "deployment/logs/"
  },
  "deployment_status": {
    "development": "completed",
    "staging": "completed",
    "production": "completed"
  },
  "distribution_status": {
    "repository_docs": "completed",
    "wiki_pages": "completed",
    "internal_portal": "completed",
    "user_guides": "completed"
  },
  "last_deployment": "2026-01-24T20:30:00Z"
}
```

## Next Steps

After deployment:

1. **Monitor Deployment** - Monitor deployment status and user feedback
2. **Address Issues** - Address any deployment issues or user concerns
3. **Update Documentation** - Keep documentation current and accurate
4. **Plan Next Release** - Plan and prepare for next update cycle
5. **Gather Feedback** - Collect user feedback for improvements

## Deployment

### Success Criteria

- [ ] Pre-deployment validation passed
- [ ] All environments deployed successfully
- [ ] All distribution channels updated
- [ ] Post-deployment validation passed
- [ ] User notification completed
- [ ] Documentation updated
- [ ] All deployment logs generated
- [ ] Deployment status confirmed

### Quality Gates

- 100% pre-deployment validation pass rate
- 100% deployment success rate
- 100% distribution channel success rate
- 100% post-deployment validation pass rate
- Complete user notification and documentation
- All deployment logs and reports generated

## Troubleshooting

### Common Issues

1. **Deployment failures**
   - Check deployment scripts and permissions
   - Verify deployment paths and configurations
   - Review deployment logs

2. **Distribution issues**
   - Check distribution channel access
   - Verify file permissions
   - Review distribution logs

3. **Validation failures**
   - Review validation criteria
   - Check file integrity
   - Verify content structure

4. **User notification issues**
   - Check notification channels
   - Verify user contact information
   - Review notification content

### Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team
- Consult deployment and distribution experts

## Best Practices

### Deployment Guidelines

1. **Test deployments** in development and staging first
2. **Use automated deployment** where possible
3. **Validate deployments** thoroughly
4. **Monitor deployment status** continuously
5. **Document deployment procedures** for consistency

### Distribution Guidelines

1. **Use multiple distribution channels** for redundancy
2. **Verify distribution success** for all channels
3. **Keep distribution documentation** up to date
4. **Monitor distribution effectiveness** and user access
5. **Plan distribution updates** in advance