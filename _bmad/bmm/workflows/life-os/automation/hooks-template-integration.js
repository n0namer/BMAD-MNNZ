#!/usr/bin/env node
/**
 * Hook Integration for Template Usage Tracking
 *
 * This script provides integration points for claude-flow hooks
 * to automatically track template usage when files are created/edited.
 *
 * Triggered by:
 * - post-edit hook: Detects when a template file is created/modified
 * - post-task hook: Records template completion when task involves template
 *
 * Installation:
 *   Add to ~/.claude-flow/hooks/post-edit.js
 *   Add to ~/.claude-flow/hooks/post-task.js
 */

const fs = require('fs');
const path = require('path');
const { trackUsage } = require('./template-tracker.js');

/**
 * Template file patterns to detect
 */
const TEMPLATE_PATTERNS = [
  /daily-review.*\.md$/,
  /weekly-review.*\.md$/,
  /monthly-review.*\.md$/,
  /quarterly-review.*\.md$/,
  /lean-canvas.*\.md$/,
  /okrs.*\.md$/,
  /swot.*\.md$/,
  /business-model-canvas.*\.md$/,
  /value-proposition-canvas.*\.md$/,
  /porters-five-forces.*\.md$/,
  /npv.*\.md$/,
  /dcf.*\.md$/,
  /monte-carlo.*\.md$/,
  /real-options.*\.md$/,
  /capm.*\.md$/,
  /kelly-criterion.*\.md$/,
  /health-belief-model.*\.md$/,
  /smart-goals.*\.md$/,
  /habit-loop.*\.md$/,
  /progressive-overload.*\.md$/,
  /macros-tracking.*\.md$/,
  /recovery-protocols.*\.md$/,
  /pomodoro.*\.md$/,
  /atomic-habits.*\.md$/,
  /eisenhower-matrix.*\.md$/,
  /gtd.*\.md$/,
  /growth-mindset.*\.md$/,
  /deliberate-practice.*\.md$/,
  /project-plan.*\.md$/,
  /project-journal.*\.md$/,
  /project-snapshot.*\.md$/,
  /triz-quick.*\.md$/,
  /triz-structured.*\.md$/,
  /ariz-full.*\.md$/,
  /workflow-plan.*\.md$/
];

/**
 * Extract template name from filename
 * @param {string} filename - The file name
 * @returns {string|null} - Template name or null if not a template
 */
function extractTemplateName(filename) {
  for (const pattern of TEMPLATE_PATTERNS) {
    if (pattern.test(filename)) {
      // Extract template type from pattern
      const match = filename.match(/^([a-z-]+)/);
      return match ? match[1] : null;
    }
  }
  return null;
}

/**
 * Detect if file content indicates template completion
 * @param {string} filePath - Path to the file
 * @returns {boolean} - True if template appears completed
 */
function isTemplateCompleted(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');

    // Heuristics for completion:
    // 1. Fewer than 5% placeholder patterns ({{...}})
    const placeholderCount = (content.match(/\{\{[^}]+\}\}/g) || []).length;
    const totalLines = content.split('\n').length;
    const placeholderRatio = placeholderCount / totalLines;

    // 2. Has filled sections (more than template minimum)
    const contentLength = content.replace(/\s/g, '').length;
    const minCompletedLength = 500; // Arbitrary threshold

    return placeholderRatio < 0.05 && contentLength > minCompletedLength;
  } catch (error) {
    return false;
  }
}

/**
 * Check if file has frontmatter with template metadata
 * @param {string} filePath - Path to the file
 * @returns {object|null} - Frontmatter object or null
 */
function extractFrontmatter(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    const frontmatterMatch = content.match(/^---\n([\s\S]+?)\n---/);

    if (!frontmatterMatch) return null;

    const frontmatter = {};
    const lines = frontmatterMatch[1].split('\n');

    for (const line of lines) {
      const [key, ...valueParts] = line.split(':');
      if (key && valueParts.length > 0) {
        const value = valueParts.join(':').trim();
        frontmatter[key.trim()] = value;
      }
    }

    return frontmatter;
  } catch (error) {
    return null;
  }
}

/**
 * Post-edit hook handler
 * Tracks when template files are created or significantly modified
 *
 * @param {object} hookData - Data from claude-flow post-edit hook
 * @param {string} hookData.filePath - Path to edited file
 * @param {string} hookData.action - Type of edit (create|modify|delete)
 */
function handlePostEdit(hookData) {
  const { filePath, action } = hookData;
  const filename = path.basename(filePath);
  const templateName = extractTemplateName(filename);

  if (!templateName) {
    // Not a template file, skip
    return;
  }

  const frontmatter = extractFrontmatter(filePath);
  const metadata = {
    domain: frontmatter?.domain || 'unknown',
    action_type: action
  };

  if (action === 'create') {
    // New template file created
    trackUsage(templateName, 'use', metadata);
  } else if (action === 'modify') {
    // Check if template is now completed
    if (isTemplateCompleted(filePath)) {
      trackUsage(templateName, 'complete', metadata);
    } else {
      trackUsage(templateName, 'fill', metadata);
    }
  }
}

/**
 * Post-task hook handler
 * Tracks template usage when task descriptions mention template work
 *
 * @param {object} hookData - Data from claude-flow post-task hook
 * @param {string} hookData.taskDescription - Description of completed task
 * @param {boolean} hookData.success - Whether task succeeded
 * @param {string[]} hookData.filesModified - List of modified files
 */
function handlePostTask(hookData) {
  const { taskDescription, success, filesModified } = hookData;

  if (!success) {
    // Only track successful completions
    return;
  }

  // Check if task involves template work
  const templateMentions = [];

  TEMPLATE_PATTERNS.forEach(pattern => {
    const templateMatch = taskDescription.match(pattern);
    if (templateMatch) {
      templateMentions.push(templateMatch[1]);
    }
  });

  // Check modified files for templates
  if (filesModified && Array.isArray(filesModified)) {
    filesModified.forEach(filePath => {
      const templateName = extractTemplateName(path.basename(filePath));
      if (templateName && !templateMentions.includes(templateName)) {
        templateMentions.push(templateName);
      }
    });
  }

  // Track each template mentioned
  templateMentions.forEach(templateName => {
    trackUsage(templateName, 'use', {
      source: 'post-task-hook',
      task: taskDescription
    });
  });
}

/**
 * Auto-detection wrapper
 * Called by claude-flow hooks with generic hook data
 */
function autoDetectAndTrack(hookType, hookData) {
  try {
    if (hookType === 'post-edit') {
      handlePostEdit(hookData);
    } else if (hookType === 'post-task') {
      handlePostTask(hookData);
    }
  } catch (error) {
    // Silent fail - don't break the hook chain
    console.error(`⚠️ Template tracking error: ${error.message}`);
  }
}

module.exports = {
  handlePostEdit,
  handlePostTask,
  autoDetectAndTrack
};
