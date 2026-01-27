---
name: 'step-03-content-generation-layer-troubleshooting'
description: 'Troubleshooting — Common Issues, Error Handling, Support Resources'
layer: 'troubleshooting'
menu:
  next: step-04-assembly-validation.md
  back: step-03-content-generation-layer-validation.md
handler: C
---

# Step 3: Content Generation — Troubleshooting

## Common Issues

### 1. Content Generation Failed
**Symptoms:**
- Empty or incomplete output files
- Script errors during generation
- Missing required sections

**Solutions:**
- Check requirements loading: `cat output/requirements_metadata.json`
- Verify architecture structure: `cat output/architecture_structure.json`
- Review template implementation: Check syntax in task templates

### 2. File Size Exceeded
**Symptoms:**
- Files larger than 100KB
- GitHub Copilot compatibility issues
- Performance problems

**Solutions:**
- Optimize content structure: Remove redundant information
- Use modularization: Split large files into smaller modules
- Remove unnecessary content: Focus on essential information

### 3. Validation Errors
**Symptoms:**
- Compliance check failures
- Missing required sections
- Format validation errors

**Solutions:**
- Review compliance requirements: Check KR requirements
- Check content structure: Ensure all required sections present
- Validate file format: Verify markdown syntax

## Error Handling

### File Not Found
```bash
# Check if file exists
if [ ! -f "$file" ]; then
    echo "Error: File not found: $file" >&2
    return 1
fi
```

### Permission Denied
```bash
# Check file permissions
if [ ! -r "$file" ]; then
    echo "Error: Cannot read file: $file" >&2
    return 1
fi
```

### Content Validation Failed
```bash
# Validate content structure
if ! grep -q "^# " "$file"; then
    echo "Error: Missing title in file: $file" >&2
    return 1
fi
```

## Support Resources

### Documentation
- `docs/KNOWN_ISSUES.md` - Known issues and workarounds
- `docs/TROUBLESHOOTING.md` - Detailed troubleshooting guide
- `docs/ARCHITECTURE.md` - Architecture documentation

### Contact
- BMAD support team: [support@bmad.example.com](mailto:support@bmad.example.com)
- GitHub issues: [github.com/bmad/bmad/issues](https://github.com/bmad/bmad/issues)
- Community forum: [community.bmad.example.com](https://community.bmad.example.com)