#!/usr/bin/env python3
import os
import re
import yaml
from pathlib import Path

def validate_file(filepath):
    issues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    if not content.startswith('---'):
        issues.append(('missing_frontmatter', 'No frontmatter'))
        return issues
    
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        issues.append(('malformed_frontmatter', 'Frontmatter not properly closed'))
        return issues
    
    frontmatter_text = match.group(1)
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        issues.append(('yaml_error', str(e)))
        return issues
    
    # Check required fields
    required_fields = ['name', 'type', 'description']
    for field in required_fields:
        if field not in frontmatter:
            issues.append(('missing_field', f'Missing required field: {field}'))
    
    # Check for unused variables in frontmatter
    if 'name' in frontmatter and not isinstance(frontmatter['name'], str):
        issues.append(('invalid_type', f'name is not string'))
    
    # Check path fields - ensure they don't use undefined variables
    for key, value in frontmatter.items():
        if key.startswith('nextStepFile') and isinstance(value, str):
            # Check if path is valid (should be relative or absolute)
            if '$' in value or '{{' in value or '{' in value:
                issues.append(('undefined_variable', f'{key} contains undefined variable: {value}'))
            # Normalize path and check if it exists
            if value.startswith('./'):
                target_path = os.path.join(os.path.dirname(filepath), value)
            else:
                target_path = value
            
            # For relative paths, check if they exist
            if not target_path.startswith('/') and value.startswith('./'):
                if not os.path.exists(target_path):
                    issues.append(('path_not_found', f'{key} points to non-existent file: {value}'))
    
    return issues

# Get all markdown files
root_dir = "."
all_files = []
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.md'):
            all_files.append(os.path.join(root, file))

# Validate all files
results = {
    'total_files': len(all_files),
    'files_with_issues': 0,
    'issues_by_type': {},
    'critical_issues': [],
    'compliant_files': 0
}

for filepath in sorted(all_files):
    issues = validate_file(filepath)
    if issues:
        results['files_with_issues'] += 1
        for issue_type, message in issues:
            if issue_type not in results['issues_by_type']:
                results['issues_by_type'][issue_type] = 0
            results['issues_by_type'][issue_type] += 1
            if issue_type in ['undefined_variable', 'path_not_found', 'malformed_frontmatter']:
                results['critical_issues'].append(f"{filepath}: {message}")
    else:
        results['compliant_files'] += 1

# Print results
print(f"\n{'='*80}")
print(f"FRONTMATTER VALIDATION REPORT")
print(f"{'='*80}\n")
print(f"Total files analyzed: {results['total_files']}")
print(f"Compliant files: {results['compliant_files']}")
print(f"Files with issues: {results['files_with_issues']}\n")

if results['issues_by_type']:
    print("Issues by type:")
    for issue_type, count in results['issues_by_type'].items():
        print(f"  {issue_type}: {count}")
    print()

if results['critical_issues']:
    print(f"CRITICAL ISSUES ({len(results['critical_issues'])}):")
    for issue in results['critical_issues'][:10]:
        print(f"  - {issue}")
    if len(results['critical_issues']) > 10:
        print(f"  ... and {len(results['critical_issues']) - 10} more")
else:
    print("✅ NO CRITICAL ISSUES FOUND")

compliance_rate = (results['compliant_files'] / results['total_files'] * 100) if results['total_files'] > 0 else 0
print(f"\nCompliance Rate: {compliance_rate:.1f}%")
print(f"{'='*80}")
