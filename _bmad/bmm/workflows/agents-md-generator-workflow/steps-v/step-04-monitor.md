# Step 4: Monitor - Continuous Monitoring and Maintenance

**Purpose:** Establish continuous monitoring and maintenance processes for AGENTS.MD files

## Overview

This step provides the framework for ongoing monitoring, maintenance, and improvement of AGENTS.MD files. It includes monitoring tools, maintenance procedures, update processes, and continuous improvement mechanisms.

## Prerequisites

- Audited and approved AGENTS.MD files
- Monitoring tools and scripts
- Maintenance procedures and guidelines
- Update and improvement processes

## Input Requirements

### Required Inputs

1. **AGENTS.MD File** - File to be monitored
2. **Monitoring Configuration** - Monitoring settings and thresholds
3. **Maintenance Schedule** - Maintenance procedures and timing

### Optional Inputs

1. **Monitoring Tools** - Automated monitoring tools and scripts
2. **Update Policies** - Update and change management policies

## Process

### 1. Monitoring Setup

```bash
# Set up monitoring for AGENTS.MD files
setup_monitoring() {
    local agents_md="$1"
    local monitoring_config="$2"
    
    echo "Setting up monitoring for AGENTS.MD files..."
    
    # Create monitoring directory
    mkdir -p "monitoring/logs"
    mkdir -p "monitoring/reports"
    
    # Initialize monitoring configuration
    if [ ! -f "$monitoring_config" ]; then
        cat > "$monitoring_config" << 'EOF'
{
  "monitoring": {
    "file_integrity": {
      "enabled": true,
      "check_interval": "1h",
      "alert_threshold": "modified"
    },
    "compliance": {
      "enabled": true,
      "check_interval": "24h",
      "alert_threshold": "failed"
    },
    "performance": {
      "enabled": true,
      "check_interval": "6h",
      "alert_threshold": "degraded"
    },
    "security": {
      "enabled": true,
      "check_interval": "12h",
      "alert_threshold": "vulnerability"
    }
  },
  "maintenance": {
    "schedule": {
      "daily": "02:00",
      "weekly": "sunday 03:00",
      "monthly": "1st 04:00"
    },
    "tasks": [
      "backup",
      "cleanup",
      "optimization",
      "validation"
    ]
  }
}
EOF
        echo "✓ Monitoring configuration created: $monitoring_config"
    else
        echo "✓ Monitoring configuration already exists: $monitoring_config"
    fi
    
    # Create monitoring scripts
    create_monitoring_scripts "$agents_md"
    
    echo "✓ Monitoring setup completed"
    return 0
}

# Usage
setup_monitoring "output/AGENTS.MD" "monitoring/monitoring_config.json"
```

### 2. File Integrity Monitoring

```bash
# Monitor file integrity
monitor_file_integrity() {
    local agents_md="$1"
    local baseline_hash="$2"
    
    echo "Monitoring file integrity..."
    
    # Calculate current hash
    local current_hash=$(sha256sum "$agents_md" | cut -d' ' -f1)
    
    # Check if baseline hash exists
    if [ ! -f "$baseline_hash" ]; then
        echo "Creating baseline hash..."
        echo "$current_hash" > "$baseline_hash"
        echo "✓ Baseline hash created: $current_hash"
        return 0
    fi
    
    # Compare hashes
    local stored_hash=$(cat "$baseline_hash")
    
    if [ "$current_hash" = "$stored_hash" ]; then
        echo "✓ File integrity verified: No changes detected"
        return 0
    else
        echo "⚠ File integrity alert: Changes detected"
        echo "  Previous hash: $stored_hash"
        echo "  Current hash: $current_hash"
        
        # Log the change
        local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
        echo "$timestamp - File integrity change detected" >> "monitoring/logs/integrity.log"
        echo "  Previous hash: $stored_hash" >> "monitoring/logs/integrity.log"
        echo "  Current hash: $current_hash" >> "monitoring/logs/integrity.log"
        
        # Update baseline hash
        echo "$current_hash" > "$baseline_hash"
        echo "✓ Baseline hash updated: $current_hash"
        
        return 1
    fi
}

# Usage
monitor_file_integrity "output/AGENTS.MD" "monitoring/baseline_hash.txt"
```

### 3. Compliance Monitoring

```bash
# Monitor compliance status
monitor_compliance() {
    local agents_md="$1"
    local compliance_report="$2"
    
    echo "Monitoring compliance status..."
    
    # Check BMAD compliance
    local bmad_refs=$(grep -c "BMAD" "$agents_md")
    local compliance_score=0
    local total_checks=5
    
    if [ "$bmad_refs" -gt 0 ]; then
        compliance_score=$((compliance_score + 1))
        echo "✓ BMAD protocol compliance: $bmad_refs references"
    else
        echo "✗ BMAD protocol compliance: Missing"
    fi
    
    # Check phase compliance
    local phase_count=0
    local phases=("Discovery" "Planning" "Implementation" "Validation")
    for phase in "${phases[@]}"; do
        if grep -q "$phase" "$agents_md"; then
            phase_count=$((phase_count + 1))
        fi
    done
    
    if [ "$phase_count" -eq 4 ]; then
        compliance_score=$((compliance_score + 1))
        echo "✓ Phase compliance: All 4 phases present"
    else
        echo "✗ Phase compliance: $phase_count/4 phases present"
    fi
    
    # Check file size compliance
    local file_size=$(wc -c < "$agents_md")
    if [ "$file_size" -le 102400 ]; then
        compliance_score=$((compliance_score + 1))
        echo "✓ File size compliance: $file_size bytes"
    else
        echo "✗ File size compliance: $file_size bytes (exceeds limit)"
    fi
    
    # Check content structure compliance
    local required_sections=("UX Layer" "BMAD Protocol" "Phase Workflows" "Task Templates" "Examples" "Reasoning Frameworks" "Session Monitoring" "Best Practices")
    local sections_found=0
    
    for section in "${required_sections[@]}"; do
        if grep -q "$section" "$agents_md"; then
            sections_found=$((sections_found + 1))
        fi
    done
    
    if [ "$sections_found" -eq 8 ]; then
        compliance_score=$((compliance_score + 1))
        echo "✓ Content structure compliance: All 8 sections present"
    else
        echo "✗ Content structure compliance: $sections_found/8 sections present"
    fi
    
    # Check format compliance
    if grep -q "^# " "$agents_md" && grep -q "^## " "$agents_md"; then
        compliance_score=$((compliance_score + 1))
        echo "✓ Format compliance: Markdown format correct"
    else
        echo "✗ Format compliance: Markdown format incorrect"
    fi
    
    local compliance_percentage=$((compliance_score * 100 / total_checks))
    echo "Overall compliance: $compliance_score/$total_checks ($compliance_percentage%)"
    
    # Generate compliance report
    cat > "$compliance_report" << EOF
# AGENTS.MD Compliance Monitoring Report

**Generated:** $(date)
**File:** $agents_md

## Compliance Status

- **BMAD Protocol Compliance:** $bmad_refs references
- **Phase Compliance:** $phase_count/4 phases
- **File Size Compliance:** $file_size bytes
- **Content Structure Compliance:** $sections_found/8 sections
- **Format Compliance:** Markdown format $(if grep -q "^# " "$agents_md" && grep -q "^## " "$agents_md"; then echo "correct"; else echo "incorrect"; fi)

## Overall Compliance Score

**Score:** $compliance_score/$total_checks ($compliance_percentage%)

## Status

$(if [ "$compliance_percentage" -ge 95 ]; then echo "✅ COMPLIANT"; else echo "⚠️ NON-COMPLIANT"; fi)

EOF
    
    # Log compliance status
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Compliance check: $compliance_percentage%" >> "monitoring/logs/compliance.log"
    
    if [ "$compliance_percentage" -ge 95 ]; then
        echo "✓ Compliance monitoring passed"
        return 0
    else
        echo "⚠ Compliance monitoring failed"
        return 1
    fi
}

# Usage
monitor_compliance "output/AGENTS.MD" "monitoring/reports/compliance_report.md"
```

### 4. Performance Monitoring

```bash
# Monitor performance metrics
monitor_performance() {
    local agents_md="$1"
    local performance_report="$2"
    
    echo "Monitoring performance metrics..."
    
    # Measure load time
    local start_time=$(date +%s.%N)
    cat "$agents_md" > /dev/null
    local end_time=$(date +%s.%N)
    local load_time=$(echo "$end_time - $start_time" | bc)
    
    # Measure file size
    local file_size=$(wc -c < "$agents_md")
    local file_size_kb=$(echo "scale=2; $file_size / 1024" | bc)
    
    # Measure processing time
    local process_start=$(date +%s.%N)
    grep -c "BMAD" "$agents_md" > /dev/null
    local process_end=$(date +%s.%N)
    local process_time=$(echo "$process_end - $process_start" | bc)
    
    # Check memory usage
    local memory_usage=$(echo "scale=2; $file_size / 1024" | bc)
    
    echo "Performance Metrics:"
    echo "  Load Time: ${load_time}s"
    echo "  File Size: ${file_size_kb}KB"
    echo "  Processing Time: ${process_time}s"
    echo "  Memory Usage: ${memory_usage}KB"
    
    # Generate performance report
    cat > "$performance_report" << EOF
# AGENTS.MD Performance Monitoring Report

**Generated:** $(date)
**File:** $agents_md

## Performance Metrics

### Load Time
- **Time:** ${load_time}s
- **Status:** $(if (( $(echo "$load_time < 1.0" | bc -l) )); then echo "✅ ACCEPTABLE"; else echo "⚠️ SLOW"; fi)

### File Size
- **Size:** ${file_size_kb}KB
- **Status:** $(if [ "$file_size" -le 102400 ]; then echo "✅ ACCEPTABLE"; else echo "⚠️ LARGE"; fi)

### Processing Time
- **Time:** ${process_time}s
- **Status:** $(if (( $(echo "$process_time < 0.5" | bc -l) )); then echo "✅ ACCEPTABLE"; else echo "⚠️ SLOW"; fi)

### Memory Usage
- **Usage:** ${memory_usage}KB
- **Status:** $(if (( $(echo "$memory_usage < 100" | bc -l) )); then echo "✅ ACCEPTABLE"; else echo "⚠️ HIGH"; fi)

## Performance Summary

$(if (( $(echo "$load_time < 1.0 && $process_time < 0.5 && $memory_usage < 100" | bc -l) )); then echo "✅ ALL METRICS ACCEPTABLE"; else echo "⚠️ SOME METRICS NEED ATTENTION"; fi)

EOF
    
    # Log performance metrics
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Performance: Load=${load_time}s, Size=${file_size_kb}KB, Process=${process_time}s" >> "monitoring/logs/performance.log"
    
    echo "✓ Performance monitoring completed"
    return 0
}

# Usage
monitor_performance "output/AGENTS.MD" "monitoring/reports/performance_report.md"
```

### 5. Security Monitoring

```bash
# Monitor security status
monitor_security() {
    local agents_md="$1"
    local security_report="$2"
    
    echo "Monitoring security status..."
    
    local security_issues=0
    local security_score=100
    
    # Check for sensitive information
    local sensitive_patterns=("password" "secret" "key" "token" "api_key" "private_key")
    for pattern in "${sensitive_patterns[@]}"; do
        if grep -qi "$pattern" "$agents_md"; then
            security_issues=$((security_issues + 1))
            security_score=$((security_score - 20))
            echo "⚠ Sensitive information found: $pattern"
        fi
    done
    
    # Check for malicious content
    local malicious_patterns=("eval(" "exec(" "system(" "shell(" "cmd.exe" "powershell")
    for pattern in "${malicious_patterns[@]}"; do
        if grep -qi "$pattern" "$agents_md"; then
            security_issues=$((security_issues + 1))
            security_score=$((security_score - 25))
            echo "⚠ Malicious content found: $pattern"
        fi
    done
    
    # Check for content injection vulnerabilities
    local injection_patterns=("<script>" "<iframe>" "<object>" "<embed>" "javascript:")
    for pattern in "${injection_patterns[@]}"; do
        if grep -qi "$pattern" "$agents_md"; then
            security_issues=$((security_issues + 1))
            security_score=$((security_score - 15))
            echo "⚠ Content injection vulnerability: $pattern"
        fi
    done
    
    # Check external links
    local external_links=$(grep -c "http" "$agents_md")
    if [ "$external_links" -gt 10 ]; then
        security_issues=$((security_issues + 1))
        security_score=$((security_score - 10))
        echo "⚠ Many external links: $external_links"
    fi
    
    # Check file permissions
    local file_perms=$(stat -c "%a" "$agents_md" 2>/dev/null || echo "644")
    if [ "$file_perms" != "644" ] && [ "$file_perms" != "600" ]; then
        security_issues=$((security_issues + 1))
        security_score=$((security_score - 5))
        echo "⚠ File permissions too permissive: $file_perms"
    fi
    
    echo "Security Status:"
    echo "  Issues Found: $security_issues"
    echo "  Security Score: $security_score/100"
    
    # Generate security report
    cat > "$security_report" << EOF
# AGENTS.MD Security Monitoring Report

**Generated:** $(date)
**File:** $agents_md

## Security Status

### Security Issues Found
- **Count:** $security_issues
- **Score:** $security_score/100

### Detailed Analysis

$(if [ "$security_issues" -eq 0 ]; then echo "✅ NO SECURITY ISSUES DETECTED"; else echo "⚠️ SECURITY ISSUES FOUND"; fi)

### Security Score Breakdown

- **Sensitive Information:** $(if [ "$security_issues" -eq 0 ]; then echo "✅ CLEAN"; else echo "⚠️ ISSUES FOUND"; fi)
- **Malicious Content:** $(if [ "$security_issues" -eq 0 ]; then echo "✅ CLEAN"; else echo "⚠️ ISSUES FOUND"; fi)
- **Content Injection:** $(if [ "$security_issues" -eq 0 ]; then echo "✅ CLEAN"; else echo "⚠️ ISSUES FOUND"; fi)
- **External Links:** $(if [ "$external_links" -le 10 ]; then echo "✅ ACCEPTABLE"; else echo "⚠️ TOO MANY"; fi)
- **File Permissions:** $(if [ "$file_perms" = "644" ] || [ "$file_perms" = "600" ]; then echo "✅ SECURE"; else echo "⚠️ PERMISSIVE"; fi)

## Security Status

$(if [ "$security_score" -ge 80 ]; then echo "✅ SECURE"; elif [ "$security_score" -ge 60 ]; then echo "⚠️ MODERATE RISK"; else echo "✗ HIGH RISK"; fi)

EOF
    
    # Log security status
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Security check: Score=$security_score, Issues=$security_issues" >> "monitoring/logs/security.log"
    
    if [ "$security_score" -ge 80 ]; then
        echo "✓ Security monitoring passed"
        return 0
    else
        echo "⚠ Security monitoring failed"
        return 1
    fi
}

# Usage
monitor_security "output/AGENTS.MD" "monitoring/reports/security_report.md"
```

### 6. Maintenance Automation

```bash
# Automate maintenance tasks
automate_maintenance() {
    local agents_md="$1"
    local maintenance_schedule="$2"
    
    echo "Setting up automated maintenance..."
    
    # Create maintenance script
    cat > "monitoring/scripts/maintenance.sh" << 'EOF'
#!/bin/bash

# AGENTS.MD Maintenance Script
# This script performs automated maintenance tasks

AGENTS_MD="$1"
MAINTENANCE_LOG="monitoring/logs/maintenance.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "$TIMESTAMP - Starting maintenance tasks" >> "$MAINTENANCE_LOG"

# Task 1: Backup
echo "$TIMESTAMP - Creating backup..." >> "$MAINTENANCE_LOG"
cp "$AGENTS_MD" "${AGENTS_MD}.backup.$(date +%Y%m%d_%H%M%S)"
echo "$TIMESTAMP - Backup completed" >> "$MAINTENANCE_LOG"

# Task 2: Cleanup
echo "$TIMESTAMP - Performing cleanup..." >> "$MAINTENANCE_LOG"
# Remove old logs (older than 30 days)
find monitoring/logs -name "*.log" -mtime +30 -delete
# Remove old backups (older than 90 days)
find . -name "*.backup.*" -mtime +90 -delete
echo "$TIMESTAMP - Cleanup completed" >> "$MAINTENANCE_LOG"

# Task 3: Optimization
echo "$TIMESTAMP - Optimizing file..." >> "$MAINTENANCE_LOG"
# Remove empty lines at end of file
sed -i '${/^$/d;}' "$AGENTS_MD"
# Ensure proper line endings
dos2unix "$AGENTS_MD" 2>/dev/null || true
echo "$TIMESTAMP - Optimization completed" >> "$MAINTENANCE_LOG"

# Task 4: Validation
echo "$TIMESTAMP - Running validation..." >> "$MAINTENANCE_LOG"
# Run basic validation checks
if [ -f "$AGENTS_MD" ]; then
    echo "$TIMESTAMP - File exists: PASS" >> "$MAINTENANCE_LOG"
else
    echo "$TIMESTAMP - File exists: FAIL" >> "$MAINTENANCE_LOG"
fi

if grep -q "^# " "$AGENTS_MD"; then
    echo "$TIMESTAMP - File format: PASS" >> "$MAINTENANCE_LOG"
else
    echo "$TIMESTAMP - File format: FAIL" >> "$MAINTENANCE_LOG"
fi

echo "$TIMESTAMP - Maintenance tasks completed" >> "$MAINTENANCE_LOG"
EOF

    chmod +x "monitoring/scripts/maintenance.sh"
    
    # Create cron job for automated maintenance
    if command -v crontab >/dev/null 2>&1; then
        echo "Setting up cron jobs..."
        
        # Daily maintenance at 2 AM
        (crontab -l 2>/dev/null; echo "0 2 * * * $PWD/monitoring/scripts/maintenance.sh $AGENTS_MD") | crontab -
        
        echo "✓ Automated maintenance setup completed"
    else
        echo "⚠ Cron not available, manual maintenance required"
    fi
    
    return 0
}

# Usage
automate_maintenance "output/AGENTS.MD" "monitoring/maintenance_schedule.json"
```

## Output

### Generated Files

1. **Monitoring Configuration** - Monitoring settings and thresholds
2. **File Integrity Logs** - File change detection logs
3. **Compliance Reports** - Regular compliance status reports
4. **Performance Reports** - Performance metrics and analysis
5. **Security Reports** - Security status and vulnerability reports
6. **Maintenance Scripts** - Automated maintenance procedures
7. **Monitoring Dashboard** - Summary dashboard for monitoring status

### Metadata

```json
{
  "workflow": "agents-md-generator-workflow",
  "step": "step-04-monitor",
  "status": "completed",
  "timestamp": "2026-01-24T20:00:00Z",
  "inputs": {
    "agents_md": "path/to/AGENTS.MD",
    "monitoring_config": "path/to/monitoring_config.json",
    "maintenance_schedule": "path/to/maintenance_schedule.json"
  },
  "outputs": {
    "monitoring_config": "monitoring/monitoring_config.json",
    "integrity_logs": "monitoring/logs/integrity.log",
    "compliance_reports": "monitoring/reports/compliance_report.md",
    "performance_reports": "monitoring/reports/performance_report.md",
    "security_reports": "monitoring/reports/security_report.md",
    "maintenance_scripts": "monitoring/scripts/maintenance.sh",
    "monitoring_dashboard": "monitoring/dashboard.html"
  },
  "monitoring_status": {
    "file_integrity": "active",
    "compliance": "active",
    "performance": "active",
    "security": "active",
    "maintenance": "automated"
  },
  "last_monitoring_run": "2026-01-24T20:00:00Z"
}
```

## Next Steps

After setting up monitoring:

1. **Monitor Regularly** - Review monitoring reports and logs
2. **Address Issues** - Fix any issues detected by monitoring
3. **Update Monitoring** - Adjust monitoring settings as needed
4. **Perform Maintenance** - Execute maintenance tasks regularly
5. **Improve Processes** - Continuously improve monitoring and maintenance

## Monitoring

### Success Criteria

- [ ] Monitoring setup completed with all components
- [ ] File integrity monitoring active
- [ ] Compliance monitoring active
- [ ] Performance monitoring active
- [ ] Security monitoring active
- [ ] Maintenance automation configured
- [ ] All monitoring reports generated
- [ ] Monitoring alerts configured

### Quality Gates

- 100% monitoring coverage for critical aspects
- Automated monitoring for all key metrics
- Regular maintenance schedule established
- Alert thresholds configured appropriately
- Monitoring logs and reports accessible
- Maintenance tasks automated where possible

## Troubleshooting

### Common Issues

1. **Monitoring failures**
   - Check monitoring script permissions
   - Verify monitoring configuration
   - Review system resources

2. **False alerts**
   - Adjust alert thresholds
   - Review monitoring logic
   - Update monitoring criteria

3. **Maintenance failures**
   - Check script execution permissions
   - Verify file paths and permissions
   - Review maintenance procedures

4. **Performance issues**
   - Optimize monitoring scripts
   - Adjust monitoring frequency
   - Review system resources

### Support

For issues and support:
- Check `docs/KNOWN_ISSUES.md`
- Review `docs/TROUBLESHOOTING.md`
- Contact BMAD support team
- Consult monitoring and maintenance experts

## Best Practices

### Monitoring Guidelines

1. **Monitor continuously** for real-time awareness
2. **Set appropriate thresholds** to avoid false alerts
3. **Review monitoring data** regularly for trends
4. **Automate responses** where possible
5. **Document monitoring procedures** for consistency

### Maintenance Guidelines

1. **Schedule regular maintenance** to prevent issues
2. **Automate routine tasks** to reduce manual effort
3. **Monitor maintenance effectiveness** and adjust as needed
4. **Keep maintenance procedures up to date**
5. **Document maintenance activities** for audit purposes