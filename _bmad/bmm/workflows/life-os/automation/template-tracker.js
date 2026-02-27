#!/usr/bin/env node
/**
 * Template Usage Tracker for Life OS
 *
 * Tracks when templates are used and stores usage statistics in global memory.
 * Integrates with claude-flow memory hooks (post-task, post-edit).
 *
 * Usage:
 *   node template-tracker.js --template <template-name> --action <use|fill|complete>
 *   node template-tracker.js --stats
 *   node template-tracker.js --list-unused
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Template categories based on directory structure
const TEMPLATE_CATEGORIES = {
  reviews: ['daily-review', 'weekly-review', 'monthly-review', 'quarterly-review'],
  business: ['lean-canvas', 'okrs', 'swot', 'business-model-canvas', 'value-proposition-canvas', 'porters-five-forces'],
  finance: ['npv', 'dcf', 'monte-carlo', 'real-options', 'capm', 'kelly-criterion'],
  health: ['health-belief-model', 'smart-goals', 'habit-loop', 'progressive-overload', 'macros-tracking', 'recovery-protocols'],
  personal: ['pomodoro', 'atomic-habits', 'eisenhower-matrix', 'gtd', 'growth-mindset', 'deliberate-practice'],
  project: ['project-plan', 'project-journal', 'project-snapshot'],
  triz: ['triz-quick', 'triz-structured', 'ariz-full'],
  workflow: ['workflow-plan', 'project-decisions', 'project-journal']
};

/**
 * Get current timestamp in ISO format
 */
function getTimestamp() {
  return new Date().toISOString();
}

/**
 * Store template usage in global memory
 * @param {string} templateName - Name of the template
 * @param {string} action - Action performed (use|fill|complete)
 * @param {object} metadata - Additional metadata
 */
function trackUsage(templateName, action, metadata = {}) {
  const timestamp = getTimestamp();
  const category = findTemplateCategory(templateName);

  const usageRecord = {
    template: templateName,
    category: category,
    action: action,
    timestamp: timestamp,
    ...metadata
  };

  // Store in global memory using CLI
  const memoryKey = `template-usage:${templateName}:${timestamp}`;
  const memoryValue = JSON.stringify(usageRecord);

  try {
    execSync(
      `npx claude-flow@v3alpha memory store --namespace "shared-knowledge" --key "${memoryKey}" --content "${memoryValue.replace(/"/g, '\\"')}"`,
      { stdio: 'pipe' }
    );
    console.log(`✅ Tracked: ${templateName} - ${action}`);
  } catch (error) {
    console.error(`❌ Failed to track usage: ${error.message}`);
  }

  // Update usage count in summary
  updateUsageSummary(templateName, action);
}

/**
 * Update the usage summary for a template
 * @param {string} templateName - Name of the template
 * @param {string} action - Action performed
 */
function updateUsageSummary(templateName, action) {
  const summaryKey = `template-usage-summary:${templateName}`;

  try {
    // Try to retrieve existing summary
    let summary;
    try {
      const result = execSync(
        `npx claude-flow@v3alpha memory search -q "${summaryKey}" --limit 1`,
        { encoding: 'utf8', stdio: 'pipe' }
      );
      summary = JSON.parse(result);
    } catch {
      // Initialize new summary if not found
      summary = {
        template: templateName,
        total_uses: 0,
        actions: {},
        first_used: getTimestamp(),
        last_used: null
      };
    }

    // Update counters
    summary.total_uses = (summary.total_uses || 0) + 1;
    summary.actions[action] = (summary.actions[action] || 0) + 1;
    summary.last_used = getTimestamp();

    // Store updated summary
    execSync(
      `npx claude-flow@v3alpha memory store --namespace "shared-knowledge" --key "${summaryKey}" --content "${JSON.stringify(summary).replace(/"/g, '\\"')}"`,
      { stdio: 'pipe' }
    );
  } catch (error) {
    console.error(`⚠️ Failed to update summary: ${error.message}`);
  }
}

/**
 * Find which category a template belongs to
 * @param {string} templateName - Name of the template
 * @returns {string} - Category name or 'unknown'
 */
function findTemplateCategory(templateName) {
  for (const [category, templates] of Object.entries(TEMPLATE_CATEGORIES)) {
    if (templates.includes(templateName)) {
      return category;
    }
  }
  return 'unknown';
}

/**
 * Get usage statistics for all templates
 */
function getUsageStats() {
  console.log('\n📊 Template Usage Statistics\n');
  console.log('=' .repeat(80));

  // Search for all template usage summaries
  try {
    const result = execSync(
      'npx claude-flow@v3alpha memory search -q "template-usage-summary:" --limit 100',
      { encoding: 'utf8', stdio: 'pipe' }
    );

    const summaries = JSON.parse(result);

    if (!summaries || summaries.length === 0) {
      console.log('No usage data found.');
      return;
    }

    // Sort by total uses (descending)
    summaries.sort((a, b) => (b.total_uses || 0) - (a.total_uses || 0));

    // Display stats by category
    const byCategory = {};
    summaries.forEach(summary => {
      const category = summary.category || 'unknown';
      if (!byCategory[category]) {
        byCategory[category] = [];
      }
      byCategory[category].push(summary);
    });

    for (const [category, templates] of Object.entries(byCategory)) {
      console.log(`\n${category.toUpperCase()}`);
      console.log('-'.repeat(80));
      templates.forEach(t => {
        const uses = t.total_uses || 0;
        const lastUsed = t.last_used ? new Date(t.last_used).toLocaleDateString() : 'never';
        console.log(`  ${t.template.padEnd(40)} ${uses.toString().padStart(5)} uses  Last: ${lastUsed}`);
      });
    }

    // Summary stats
    console.log('\n' + '='.repeat(80));
    const totalTemplates = summaries.length;
    const totalUses = summaries.reduce((sum, t) => sum + (t.total_uses || 0), 0);
    console.log(`Total templates tracked: ${totalTemplates}`);
    console.log(`Total uses: ${totalUses}`);
    console.log(`Average uses per template: ${(totalUses / totalTemplates).toFixed(2)}`);
  } catch (error) {
    console.error(`❌ Failed to retrieve stats: ${error.message}`);
  }
}

/**
 * List unused templates
 */
function listUnusedTemplates() {
  console.log('\n📋 Unused Templates\n');
  console.log('=' .repeat(80));

  try {
    // Get all tracked templates
    const result = execSync(
      'npx claude-flow@v3alpha memory search -q "template-usage-summary:" --limit 100',
      { encoding: 'utf8', stdio: 'pipe' }
    );
    const trackedTemplates = JSON.parse(result).map(t => t.template);

    // Find all available templates
    const allTemplates = Object.values(TEMPLATE_CATEGORIES).flat();

    // Find unused
    const unused = allTemplates.filter(t => !trackedTemplates.includes(t));

    if (unused.length === 0) {
      console.log('All templates have been used at least once! 🎉');
      return;
    }

    // Group by category
    const unusedByCategory = {};
    unused.forEach(templateName => {
      const category = findTemplateCategory(templateName);
      if (!unusedByCategory[category]) {
        unusedByCategory[category] = [];
      }
      unusedByCategory[category].push(templateName);
    });

    for (const [category, templates] of Object.entries(unusedByCategory)) {
      console.log(`\n${category.toUpperCase()}`);
      console.log('-'.repeat(80));
      templates.forEach(t => console.log(`  - ${t}`));
    }

    console.log('\n' + '='.repeat(80));
    console.log(`Total unused: ${unused.length}/${allTemplates.length} (${((unused.length / allTemplates.length) * 100).toFixed(1)}%)`);
  } catch (error) {
    console.error(`❌ Failed to list unused templates: ${error.message}`);
  }
}

/**
 * Main CLI handler
 */
function main() {
  const args = process.argv.slice(2);

  if (args.length === 0 || args.includes('--help')) {
    console.log(`
Template Usage Tracker

Usage:
  node template-tracker.js --template <name> --action <use|fill|complete>
  node template-tracker.js --stats
  node template-tracker.js --list-unused

Options:
  --template <name>     Template name to track
  --action <action>     Action performed (use, fill, complete)
  --metadata <json>     Additional metadata (optional)
  --stats               Show usage statistics
  --list-unused         List templates that have never been used

Examples:
  node template-tracker.js --template lean-canvas --action fill
  node template-tracker.js --template daily-review --action complete --metadata '{"domain":"health"}'
  node template-tracker.js --stats
    `);
    return;
  }

  if (args.includes('--stats')) {
    getUsageStats();
    return;
  }

  if (args.includes('--list-unused')) {
    listUnusedTemplates();
    return;
  }

  // Parse track usage command
  const templateIndex = args.indexOf('--template');
  const actionIndex = args.indexOf('--action');
  const metadataIndex = args.indexOf('--metadata');

  if (templateIndex === -1 || actionIndex === -1) {
    console.error('❌ Error: --template and --action are required');
    process.exit(1);
  }

  const templateName = args[templateIndex + 1];
  const action = args[actionIndex + 1];
  const metadata = metadataIndex !== -1 ? JSON.parse(args[metadataIndex + 1]) : {};

  if (!['use', 'fill', 'complete'].includes(action)) {
    console.error('❌ Error: action must be one of: use, fill, complete');
    process.exit(1);
  }

  trackUsage(templateName, action, metadata);
}

// Run if called directly
if (require.main === module) {
  main();
}

module.exports = { trackUsage, getUsageStats, listUnusedTemplates };
