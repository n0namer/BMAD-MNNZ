# Accessibility Remediation - Quick Start Guide
## Katana-VectorBT WCAG 2.1 AA Implementation

**Status:** Critical Blockers Identified
**Priority:** Must Fix Before MVP Release
**Effort:** 40-50 hours (2-3 weeks)
**Owner:** Development Team + Accessibility Champion

---

## Critical Blockers (DO FIRST)

### 🔴 BLOCKER 1: Chart Alt Text & Table Alternatives
**What's Missing:** Charts lack accessible alternatives for blind/low-vision users
**Impact:** Automatic WCAG failure - charts are core product feature
**Effort:** 12-16 hours
**Status:** Not Started

**Checklist:**
- [ ] Create alt text template for equity curve chart
- [ ] Create alt text template for drawdown chart
- [ ] Create HTML table fallback for equity curve
- [ ] Create HTML table fallback for drawdown
- [ ] Create alt text template for other chart types (distribution, trades, etc.)
- [ ] Implement in all 6 screens
- [ ] Test with NVDA screen reader
- [ ] Verify with Lighthouse audit

**Example Alt Text:**
```html
<!-- ❌ TOO VAGUE -->
<img src="equity.png" alt="Equity curve" />

<!-- ✅ GOOD -->
<img src="equity.png" alt="Equity curve starting at $100,000 on 2026-01-01,
peaking at $127,500 on 2026-02-15, with maximum drawdown of $98,400 (1.6%),
ending at $123,650 on 2026-02-26, net profit of 23.65%" />
```

**Table Fallback:**
```html
<table role="table" aria-label="Equity curve data">
  <caption>Strategy Equity Curve (2026-01-01 to 2026-02-26)</caption>
  <thead>
    <tr>
      <th scope="col">Date</th>
      <th scope="col">Equity ($)</th>
      <th scope="col">Change (%)</th>
      <th scope="col">Drawdown (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2026-01-01</td>
      <td>100,000</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <!-- ... more rows ... -->
  </tbody>
</table>
```

---

### 🔴 BLOCKER 2: SVG State Machine Diagram Accessibility
**What's Missing:** Interactive state diagram not keyboard/screen reader accessible
**Impact:** Users cannot navigate strategy lifecycle without vision
**Effort:** 8-12 hours
**Status:** Not Started

**Checklist:**
- [ ] Create HTML/list-based state transition view (backup)
- [ ] Add ARIA labels to SVG elements (`<title>`, `<desc>`)
- [ ] Implement keyboard navigation (Arrow keys to move between states)
- [ ] Add focus indicators to state boxes
- [ ] Test with JAWS screen reader
- [ ] Verify Escape key closes details
- [ ] Test Enter key opens state details

**Example Implementation:**
```html
<!-- Accessible alternative: HTML list -->
<div role="main">
  <h2>Strategy State Machine</h2>
  <ol class="state-timeline">
    <li>
      <strong>State 1: GENERATE</strong>
      <button aria-expanded="false" aria-controls="generate-details">
        View Details
      </button>
      <div id="generate-details" hidden>
        Started: 2026-01-01
        Duration: 3 days
        Next: OPTIMIZE
      </div>
    </li>
    <li>
      <strong>State 2: OPTIMIZE</strong>
      <!-- ... -->
    </li>
  </ol>
</div>
```

---

### 🔴 BLOCKER 3: Disabled Form Field Contrast
**What's Missing:** Disabled controls likely fail 3:1 contrast (common issue)
**Impact:** Low-vision users cannot distinguish disabled vs. enabled controls
**Effort:** 4-6 hours
**Status:** Not Started

**Checklist:**
- [ ] Define disabled state background color
- [ ] Define disabled state text color
- [ ] Verify contrast ratio ≥ 3:1 with WebAIM Checker
- [ ] Apply to all form fields (input, select, checkbox, button, etc.)
- [ ] Add `aria-disabled="true"` to all disabled controls
- [ ] Test with Chrome DevTools contrast inspector
- [ ] Verify visually distinct from enabled state

**Recommended Disabled Palette:**
```css
/* Disabled state */
.form-control:disabled {
  background-color: #F5F5F5;  /* Light gray */
  color: #999999;             /* Medium gray, 3.1:1 contrast */
  border-color: #CCCCCC;      /* Light border */
  opacity: 0.6;               /* Additional visual indicator */
  cursor: not-allowed;        /* Show cannot interact */
}

/* Ensure 3:1 contrast */
/* #999999 on #F5F5F5 = 3.1:1 ✅ */
```

---

### 🔴 BLOCKER 4: Toast Notification Colors
**What's Missing:** Toast severity levels (INFO/WARNING/ERROR) not color-defined
**Impact:** Color-blind users cannot distinguish notification severity
**Effort:** 2-3 hours
**Status:** Not Started

**Checklist:**
- [ ] Define INFO toast colors (background, text, border)
- [ ] Define WARNING toast colors
- [ ] Define ERROR toast colors
- [ ] Add status icons (ℹ️, ⚠️, ❌) - not color-only
- [ ] Add `role="status"` or `role="alert"` to toast
- [ ] Add `aria-live="polite"` or `aria-live="assertive"`
- [ ] Test with Coblis color blindness simulator
- [ ] Verify all 3 severity levels distinguishable

**Color Definitions:**
```css
/* INFO Toast */
.toast.info {
  background-color: #D1ECF1;     /* Light cyan */
  color: #0C5460;                 /* Dark cyan */
  border: 2px solid #0C5460;
}
.toast.info::before {
  content: "ℹ️";                   /* Info icon */
}

/* WARNING Toast */
.toast.warning {
  background-color: #FFF3CD;      /* Light yellow */
  color: #856404;                 /* Dark yellow */
  border: 2px solid #FFC107;
}
.toast.warning::before {
  content: "⚠️";                   /* Warning icon */
}

/* ERROR Toast */
.toast.error {
  background-color: #F8D7DA;      /* Light red */
  color: #721C24;                 /* Dark red */
  border: 2px solid #DC3545;
}
.toast.error::before {
  content: "❌";                   /* Error icon */
}
```

---

### 🔴 BLOCKER 5: Form Error Messages
**What's Missing:** Error identification strategy not fully specified
**Impact:** Users don't understand validation failures
**Effort:** 6-8 hours
**Status:** Not Started

**Checklist:**
- [ ] Create error message for every validation rule
- [ ] Make error messages specific and actionable
- [ ] Add form-level error summary (list all errors)
- [ ] Link errors to form fields with `aria-describedby`
- [ ] Announce errors immediately with `role="alert"`
- [ ] Focus first error field when form submitted
- [ ] Test with NVDA screen reader
- [ ] Verify all 15+ form fields covered

**Error Message Examples:**
```
❌ WRONG:
"Invalid input"

✅ CORRECT:
"Start date must be in YYYY-MM-DD format (example: 2026-02-26).
You entered: 2026-2-26"

---

❌ WRONG:
"Number too large"

✅ CORRECT:
"Confidence threshold must be between 0.50 and 0.90.
You entered: 0.95 (too high by 0.05)"
```

**Form Structure:**
```html
<!-- Error summary at top -->
<div role="alert" aria-live="assertive">
  <h2>Please fix the following errors:</h2>
  <ul>
    <li>
      <a href="#start-date">Start date: Invalid format (expected YYYY-MM-DD)</a>
    </li>
    <li>
      <a href="#confidence">Confidence threshold: Value too high (max 0.90)</a>
    </li>
  </ul>
</div>

<!-- Individual field errors -->
<label for="start-date">Start Date</label>
<input
  id="start-date"
  type="text"
  aria-invalid="true"
  aria-describedby="start-date-error">
<span id="start-date-error" role="alert">
  Invalid date format. Use YYYY-MM-DD (example: 2026-02-26)
</span>
```

---

### 🔴 BLOCKER 6: Interactive Component ARIA
**What's Missing:** Not all 40+ components have documented ARIA roles
**Impact:** Screen reader users cannot interact with dropdowns, tabs, sliders, modals
**Effort:** 10-14 hours
**Status:** Not Started

**Checklist:**
- [ ] Create ARIA documentation for dropdowns (`role="combobox"`)
- [ ] Create ARIA documentation for tabs (`role="tab"`, `aria-selected`)
- [ ] Create ARIA documentation for sliders (`aria-valuemin/max/now`)
- [ ] Create ARIA documentation for modals (`role="dialog"`, `aria-modal`)
- [ ] Create ARIA documentation for data tables (`<caption>`, `<th scope>`)
- [ ] Implement ARIA for all 6 screens
- [ ] Test with JAWS screen reader
- [ ] Create ARIA implementation checklist

**Component Count by Screen:**
| Screen | Dropdowns | Tabs | Sliders | Modals | Tables | Total |
|--------|-----------|------|---------|--------|--------|-------|
| Dashboard | 2 | 3 | 0 | 1 | 2 | 8 |
| State Machine | 1 | 0 | 0 | 1 | 1 | 3 |
| Quality Gates | 2 | 1 | 0 | 2 | 1 | 6 |
| Promotion Tracker | 1 | 2 | 0 | 1 | 1 | 5 |
| Degradation Monitor | 2 | 1 | 3 | 2 | 2 | 10 |
| Audit Trail | 3 | 0 | 0 | 1 | 1 | 5 |
| **TOTAL** | **11** | **7** | **3** | **8** | **8** | **37** |

**ARIA Implementation Template - Dropdown:**
```html
<!-- ✅ ACCESSIBLE DROPDOWN -->
<div class="dropdown-wrapper">
  <label for="filter-state">Filter by State:</label>
  <button
    id="filter-state"
    role="combobox"
    aria-expanded="false"
    aria-owns="state-options"
    aria-haspopup="listbox">
    Select state...
  </button>

  <ul id="state-options" role="listbox" hidden>
    <li role="option" aria-selected="false">GENERATE</li>
    <li role="option" aria-selected="false">OPTIMIZE</li>
    <li role="option" aria-selected="false">VALIDATE</li>
  </ul>
</div>
```

---

## High Priority Gaps (Fix Next)

### 🟡 Focus Management in Modals
**Effort:** 4-6 hours | **Status:** Not Started

**Checklist:**
- [ ] Implement focus trap (Tab loops within modal)
- [ ] Document focus return (where to return after modal closes)
- [ ] Test with keyboard Tab key
- [ ] Verify Escape key closes modal and returns focus
- [ ] Test with NVDA screen reader

**Code Example:**
```javascript
// Focus trap
modal.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    const focusableElements = modal.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];

    if (e.shiftKey && document.activeElement === firstElement) {
      e.preventDefault();
      lastElement.focus();
    } else if (!e.shiftKey && document.activeElement === lastElement) {
      e.preventDefault();
      firstElement.focus();
    }
  }
});

// Return focus when modal closes
const triggerButton = document.querySelector('[data-toggle="modal"]');
modal.addEventListener('close', () => {
  triggerButton.focus(); // Return focus to button that opened modal
});
```

---

### 🟡 Data Table Keyboard Navigation
**Effort:** 4-6 hours | **Status:** Not Started

**Checklist:**
- [ ] Add Ctrl+Home/End shortcuts for large tables
- [ ] Add column sort via keyboard (Shift+Click, then arrows)
- [ ] Implement row selection with Shift+Up/Down
- [ ] Test with keyboard only (no mouse)

---

### 🟡 Link vs. Button Distinction
**Effort:** 2-3 hours | **Status:** Not Started

**Checklist:**
- [ ] Semantic distinction: Links navigate, buttons trigger actions
- [ ] Document when to use `<a>` vs. `<button>`
- [ ] Add to component library
- [ ] Audit existing components for correct semantic use

---

### 🟡 Language Markup
**Effort:** 2-3 hours | **Status:** Not Started

**Checklist:**
- [ ] Add `lang="en"` to English sections
- [ ] Add `lang="ru"` to Russian sections
- [ ] Screen reader tests pronunciation

**Example:**
```html
<html lang="en">
  <body>
    <h1>Strategy Dashboard</h1>
    <p lang="ru">Стратегия активна</p>  <!-- Russian section -->
  </body>
</html>
```

---

## Testing Roadmap

### Week 1: Critical Blockers
**Tuesday-Wednesday:**
- [ ] Chart alt text + table fallbacks implemented
- [ ] SVG diagram accessible alternative created
- [ ] Disabled field contrast colors defined

**Thursday-Friday:**
- [ ] Toast colors specified
- [ ] Form error messages complete
- [ ] ARIA for dropdowns/tabs/tables documented

### Week 2: Validation
**Monday:**
- [ ] Lighthouse accessibility audit (target: 100/100)
- [ ] NVDA screen reader testing
- [ ] Keyboard-only navigation testing

**Tuesday-Wednesday:**
- [ ] JAWS testing (complex interactions)
- [ ] Color contrast verification
- [ ] Focus management testing

**Thursday:**
- [ ] Final remediation fixes
- [ ] Re-test all blockers
- [ ] Documentation complete

**Friday:**
- [ ] Sign-off and release gate

---

## Automated Testing Setup

### Add to CI/CD Pipeline
```bash
# 1. Lighthouse CI
npm install -g @lhci/cli
lhci autorun --config=lighthouse-config.json

# Expected score: 100/100 accessibility
```

**lighthouse-config.json:**
```json
{
  "ci": {
    "collect": {
      "url": ["http://localhost:8888/dashboard"],
      "numberOfRuns": 3
    },
    "assert": {
      "assertions": {
        "categories:accessibility": ["error", {"minScore": 1.0}],
        "color-contrast": "error",
        "aria-valid-attr": "error",
        "button-name": "error",
        "image-alt": "error"
      }
    }
  }
}
```

---

## Accessibility Champion Responsibilities

**Assign one person to:**
1. ✅ Maintain accessibility standards (WCAG 2.1 AA)
2. ✅ Code review for accessibility issues
3. ✅ Screen reader testing (NVDA minimum)
4. ✅ Lighthouse monitoring
5. ✅ Documentation updates
6. ✅ Team training

---

## Tools & Resources

### Free Testing Tools
- **Lighthouse:** Chrome DevTools > Lighthouse
- **NVDA:** https://www.nvaccess.org/ (Windows)
- **WebAIM Contrast Checker:** https://webaim.org/resources/contrastchecker/
- **Coblis Color Blindness Simulator:** https://www.color-blindness.com/coblis-color-blindness-simulator/
- **Color Oracle:** https://colororacle.org/

### Paid Tools
- **JAWS Screen Reader:** https://www.freedomscientific.com/ (Industry standard)
- **axe DevTools:** https://www.deque.com/axe/devtools/ (Enhanced version)

---

## Success Criteria for MVP Release

**MUST PASS:**
1. ✅ Lighthouse accessibility score = 100/100
2. ✅ All 6 critical blockers fixed
3. ✅ NVDA screen reader: All major features usable
4. ✅ Keyboard-only: All navigation possible without mouse
5. ✅ Color contrast: All text ≥ 4.5:1 verified
6. ✅ No accessibility violations in axe scan

**NICE TO HAVE:**
- JAWS testing completed
- High contrast mode tested
- Zoom (200%) tested
- Documentation complete

---

## Questions?

**Accessibility is not optional - it's required by law (ADA, WCAG) and good UX.**

Every blocker fixed = 15-20% improvement in overall accessibility score.
After all blockers fixed, compliance will reach 95%+ and meet MVP requirements.

---

**Document Version:** 1.0
**Last Updated:** 2026-02-26
**Status:** READY FOR IMPLEMENTATION
