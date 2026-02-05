#!/usr/bin/env node
/**
 * subprocess-template-loader.js
 *
 * Loads a single template with context pre-filling
 * Reduces context from 16,000 lines (all templates) to 200-600 lines (one template)
 *
 * Usage:
 *   node subprocess-template-loader.js "triz-quick" "triz" --context "{projectTitle: 'My Project'}"
 *   node subprocess-template-loader.js "swot" "business"
 *
 * Returns: { template: string, lines: number, sections: Array, preFilledCount: number }
 */

const fs = require('fs');
const path = require('path');

// Default graceful fallback
function gracefulFallback(templateName, error) {
  console.error(`[FALLBACK] Template loading failed: ${error.message}`);
  console.error(`[FALLBACK] Proceeding without subprocess template loading`);
  return {
    error: true,
    fallback: true,
    message: `Template ${templateName} not available in subprocess. Loading in main context.`,
    templateName,
    lines: 0
  };
}

async function loadTemplate(templateName, domainFolder, contextDataStr) {
  try {
    // Parse context data if provided
    let contextData = {};
    if (contextDataStr) {
      try {
        contextData = JSON.parse(contextDataStr);
      } catch (e) {
        console.warn('[WARN] Invalid context JSON, ignoring');
      }
    }

    // Construct template path
    const templatesDir = path.join(__dirname, '..', 'templates');
    const templatePath = path.join(
      templatesDir,
      domainFolder === 'triz' ? `${templateName}.template.md` : `${domainFolder}/${templateName}.template.md`
    );

    // Verify file exists
    if (!fs.existsSync(templatePath)) {
      throw new Error(`Template file not found: ${templatePath}`);
    }

    // Load template from disk
    let template = fs.readFileSync(templatePath, 'utf-8');
    const originalLines = template.split('\n').length;

    // Pre-fill known variables from context
    let preFilledCount = 0;
    const placeholders = [
      { pattern: /{project_title}/g, value: contextData.projectTitle },
      { pattern: /{project_domain}/g, value: contextData.domain },
      { pattern: /{timeline}/g, value: contextData.timeline },
      { pattern: /{budget}/g, value: contextData.budget },
      { pattern: /{communication_language}/g, value: contextData.language || 'en' }
    ];

    placeholders.forEach(({ pattern, value }) => {
      if (value && template.includes(pattern.source)) {
        template = template.replace(pattern, value);
        preFilledCount++;
      }
    });

    // Extract sections for navigation
    const sections = extractSections(template);

    // Remove YAML frontmatter for cleaner template
    const lines = template.split('\n');
    let cleanTemplate = template;
    if (lines[0] === '---') {
      const endIdx = lines.slice(1).findIndex(l => l === '---');
      if (endIdx >= 0) {
        cleanTemplate = lines.slice(endIdx + 2).join('\n');
      }
    }

    return {
      success: true,
      template: cleanTemplate,
      originalLines,
      lines: cleanTemplate.split('\n').length,
      sections,
      preFilledCount,
      contextApplied: Object.keys(contextData).length > 0,
      templateName,
      domain: domainFolder,
      contextReduction: originalLines - cleanTemplate.split('\n').length
    };

  } catch (error) {
    return gracefulFallback(templateName, error);
  }
}

function extractSections(template) {
  const lines = template.split('\n');
  const sections = [];

  lines.forEach((line, index) => {
    if (line.startsWith('## ')) {
      sections.push({
        title: line.replace(/^#+\s+/, '').trim(),
        level: 2,
        lineNumber: index + 1
      });
    } else if (line.startsWith('### ')) {
      sections.push({
        title: line.replace(/^#+\s+/, '').trim(),
        level: 3,
        lineNumber: index + 1
      });
    }
  });

  return sections;
}

// CLI Usage
async function main() {
  const args = process.argv.slice(2);

  if (args.length < 2) {
    console.error('Usage: node subprocess-template-loader.js <templateName> <domain> [--context "{...}"]');
    console.error('Example: node subprocess-template-loader.js triz-quick triz');
    process.exit(1);
  }

  const templateName = args[0];
  const domain = args[1];
  let contextStr = null;

  // Parse context if provided
  const contextIdx = args.indexOf('--context');
  if (contextIdx >= 0 && contextIdx + 1 < args.length) {
    contextStr = args[contextIdx + 1];
  }

  const result = await loadTemplate(templateName, domain, contextStr);

  if (result.error) {
    // Graceful fallback - exit cleanly
    console.log(JSON.stringify(result));
    process.exit(0);
  }

  // Success output
  console.log(JSON.stringify({
    success: true,
    templateName: result.templateName,
    domain: result.domain,
    lines: result.lines,
    lineSavings: result.contextReduction,
    sections: result.sections.length,
    preFilledFields: result.preFilledCount,
    message: `Template loaded: ${result.lines} lines (${result.contextReduction} lines saved by removing frontmatter)`
  }));

  // If requested, output the template itself on stderr for testing
  if (process.argv.includes('--with-template')) {
    console.error(result.template);
  }
}

if (require.main === module) {
  main().catch(err => {
    console.error('[FATAL]', err.message);
    process.exit(1);
  });
}

module.exports = { loadTemplate, extractSections };
