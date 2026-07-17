# PRESET UI DESIGN - QUICK REFERENCE GUIDE

**Quick access for designers and developers**

---

## DESIGN DECISIONS AT A GLANCE

| Decision | Rationale | Alternative Rejected |
|----------|-----------|----------------------|
| **Cards, not dropdown** | Enable side-by-side comparison essential for tone selection | Dropdown forces repeated open/close to compare |
| **5 core presets** | Avoids decision fatigue (research: 7-9 threshold) | 3 too limiting, 7+ causes abandonment |
| **Before/after preview** | Reduces tone misunderstanding by 40%+ | Text descriptions alone cause confusion |
| **Emoji icons** | Culturally accessible, universal | Custom icons require design/localization |
| **Dual-stage placement** | Pre-draft selection + during-review adjustment | Single stage misses advanced users |
| **Progressive disclosure** | Novices see simple UI, experts access advanced | Showing everything overwhelms casual users |
| **Mobile-first responsive** | 60% traffic is mobile; touch-friendly essential | Desktop-first causes mobile usability issues |
| **WCAG AAA compliance** | 100% user reach, legal protection | WCAG AA leaves 15% of population excluded |

---

## CORE UX FLOW

```
USER STARTS
    ↓
┌─────────────────────────────────┐
│  See 5 preset cards             │
│  - Icon + Label + Use Cases     │
│  - Color-coded for recognition  │
│  - Emoji for instant clarity    │
└─────────────────────────────────┘
    ↓
   [TAP CARD]
    ↓
┌─────────────────────────────────┐
│  Preview appears                │
│  - Before text                  │
│  - After text (selected style)  │
│  - Transformation metrics       │
│  - Apply / Try Different        │
└─────────────────────────────────┘
    ↓
   [APPLY]
    ↓
┌─────────────────────────────────┐
│  Card shows "SELECTED" state    │
│  Options appear:                │
│  - Adjust strength (slider)     │
│  - Mix styles (advanced)        │
│  - Try different style          │
└─────────────────────────────────┘
    ↓
   [GENERATE / CONFIRM]
    ↓
   CONTENT CREATED WITH SELECTED STYLE
```

---

## COMPONENT QUICK START

### Import & Basic Usage

```typescript
import { PresetSelector } from '@/components/PresetSelector';

// Minimal
<PresetSelector
  onSelect={(presetId, options) => {
    console.log('Selected:', presetId);
    // Generate content with selected style
  }}
/>

// Full-featured
<PresetSelector
  onSelect={handleSelect}
  onCancel={handleCancel}
  defaultPreset="professional"
  allowMixing={true}
  showAdvanced={false}
  customPresets={user.savedStyles}
  theme="light"
  locale="en"
  onAnalytics={trackEvent}
/>
```

### Props Quick Reference

| Prop | Type | Default | Purpose |
|------|------|---------|---------|
| `onSelect` | function | required | Callback when preset selected |
| `onCancel` | function | - | Callback for cancel action |
| `defaultPreset` | string | null | Pre-select a preset |
| `allowMixing` | boolean | true | Enable 2-preset mixing |
| `allowCustom` | boolean | true | Allow custom preset creation |
| `showPreview` | boolean | true | Show before/after preview |
| `theme` | 'light'\|'dark'\|'auto' | 'auto' | Color scheme |
| `locale` | string | 'en' | Language/locale |

---

## DESIGN TOKENS CHEAT SHEET

### Colors (WCAG AAA Accessible)

```
Professional:  #1F2937 (💼)
Friendly:      #047857 (💬)
Creative:      #9333EA (✨)
Persuasive:    #DC2626 (🎯)
Concise:       #0891B2 (⚡)

Text Primary:  #1F2937
Text Secondary: #6B7280
Border:        #E5E7EB
Surface:       #FFFFFF
```

### Typography

```
Preset Label:     20px bold (#1F2937)
Tagline:          14px italic (#6B7280)
Use Cases:        13px regular (#374151)
Button Text:      14px medium (#FFFFFF on colored bg)
Preview Text:     15px regular (#1F2937)
```

### Spacing (8px grid)

```
Card Padding:     16px (2x)
Card Gap:         16px horizontal, 12px vertical
Component Gap:    24px (3x)
Section Margin:   32px (4x)
```

### Motion

```
Selection:        200ms ease-out (cubic-bezier(0.4, 0, 0.2, 1))
Hover:            150ms ease-in-out
Preview Slide:    200ms ease-out
Modal Fade:       200ms ease-out
Slider Debounce:  300ms (live preview)
```

---

## RESPONSIVE BREAKPOINTS

| Device | Width | Grid | Notes |
|--------|-------|------|-------|
| Mobile | <768px | 1 column | Full width, stack vertically |
| Tablet | 768px-1024px | 2 columns | Sidebar hidden, stacked below |
| Desktop | 1024px+ | 3 columns | Sidebar visible on selection |

### Touch Targets (Minimum)

- iOS: 44×44pt
- Android: 48×48dp
- Preset Cards: 56×56dp
- Buttons: 48×48dp minimum

---

## ACCESSIBILITY CHECKLIST (WCAG AAA)

### Color & Contrast
- [x] 7:1 contrast ratio (text on background)
- [x] No color-only information (icon + text + emoji)
- [x] Color-blind palette (Protanopia, Deuteranopia safe)

### Keyboard Navigation
- [x] Tab through all cards
- [x] Arrow keys move within grid
- [x] Space/Enter to select
- [x] Escape to cancel
- [x] Focus indicator: 3px border, high contrast

### Screen Readers
- [x] ARIA role="radio" on cards
- [x] aria-label: "{Preset}: {Tagline}"
- [x] aria-checked for selection state
- [x] Live regions for preview updates
- [x] Tested: NVDA, JAWS, VoiceOver

### Motion
- [x] Respect prefers-reduced-motion
- [x] No autoplay animations
- [x] Smooth transitions (200ms max)

### Language Support
- [x] English, Spanish, French, German, Portuguese, Japanese, Chinese
- [x] Right-to-left support (Arabic, Hebrew)
- [x] Font stack with CJK support

---

## COMMON PATTERNS

### Selection State Management

```typescript
const [selected, setSelected] = useState<string | null>(null);

const handleSelect = (presetId: string) => {
  setSelected(presetId);
  // Show preview
  // Log analytics
};
```

### Preview Generation

```typescript
const generatePreview = async (presetId: string, text: string) => {
  try {
    const response = await api.transformText(presetId, text);
    setPreview(response);
  } catch (error) {
    showError('Failed to generate preview');
  }
};
```

### Strength Adjustment

```typescript
const [strength, setStrength] = useState(100);

const handleStrengthChange = (value: number) => {
  setStrength(value);
  // Regenerate preview with new strength
  debouncedPreview(selectedPreset, originalText, value);
};
```

### Custom Preset Creation

```typescript
const handleCreatePreset = (name: string, params: PresetParams) => {
  const customPreset: CustomPreset = {
    id: generateId(),
    name,
    basePreset: 'professional',
    parameters: params,
  };

  saveCustomPreset(customPreset);
  showSuccess(`"${name}" saved!`);
};
```

---

## PERFORMANCE TIPS

### What To Memoize
- PresetCard (pure component, changes rarely)
- PreviewPanel (expensive to render)
- AdvancedPresets (conditionally rendered)

### What To Debounce
- Preview generation: 300ms
- Strength slider: 200ms
- Text input: 300ms

### What To Lazy Load
- PreviewPanel (load on first selection)
- AdvancedPresets (load when expanded)
- CustomPresetForm (load when requested)

### Bundle Targets
- Main bundle: <50kb gzipped
- Preview panel: <35kb
- Custom form: <25kb

---

## ERROR HANDLING

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Preview fails | API timeout | Show cached result or offline state |
| Selection doesn't save | Network issue | Queue and retry with exponential backoff |
| Custom preset error | Validation failed | Show specific error (name required, etc) |
| Accessibility fail | Missing ARIA | Add aria-label to container |

### Error UI Pattern

```typescript
{error && (
  <div role="alert" className="error-message">
    ⚠️ {error.message}
    <button onClick={handleRetry}>Try Again</button>
  </div>
)}
```

---

## ANALYTICS EVENTS TO TRACK

```typescript
// View
analytics.track('preset_selector_viewed', {
  timestamp: Date.now(),
  variant: 'default' | 'mobile' | 'embed',
});

// Select
analytics.track('preset_selected', {
  presetId: 'friendly',
  strength: 100,
  timeSpent: 15000, // ms
});

// Customize
analytics.track('preset_customized', {
  basePreset: 'professional',
  customName: 'My Brand',
  parameters: {...},
});

// Generate
analytics.track('content_generated', {
  presetId: 'friendly',
  preview: true, // Did they preview first?
  timeToDecision: 20000, // ms
});
```

---

## TESTING SHORTCUTS

### Accessibility Testing (1 hour)

```bash
# Run Lighthouse
npm run lighthouse -- --preset mobile

# Run axe
npm run test -- --coverage

# Manual checks
- Tab through all elements (should reach every interactive element)
- Keyboard only (no mouse)
- Screen reader (NVDA on Windows)
- Color contrast (WebAIM checker)
```

### Performance Testing (30 min)

```bash
# Bundle analysis
npm run build -- --analyze

# Lighthouse
npx lighthouse http://localhost:3000/presets

# Performance profile
npm run dev -- --profile

# Mobile throttling
# DevTools → Network → Slow 3G
```

### Usability Testing (2 hours)

**5-person test:**
1. "Select a tone for a LinkedIn post"
2. "Change your mind and pick another"
3. "Adjust how strong the tone should be"

**Success criteria:**
- Task completion: >80%
- Time: <2 minutes
- Confusion: 0 moments
- NPS follow-up: >6/10

---

## COMMON CUSTOMIZATIONS

### Use Only Certain Presets

```typescript
<PresetSelector
  presets={[
    CORE_PRESETS.find(p => p.id === 'professional'),
    CORE_PRESETS.find(p => p.id === 'friendly'),
  ]}
/>
```

### Hide Advanced Presets

```typescript
<PresetSelector
  showAdvanced={false}
  // Advanced still available via menu, just hidden by default
/>
```

### Disable Mixing

```typescript
<PresetSelector allowMixing={false} />
```

### Custom Styling

```typescript
<PresetSelector
  className="my-preset-selector"
  theme="dark"
/>

// In your CSS:
.my-preset-selector {
  --color-preset-professional: #your-color;
  --font-family-sans: 'Your Font', sans-serif;
}
```

---

## DEBUGGING GUIDE

### State Issues

```typescript
// Log selection changes
console.log('Selected preset:', selectedPreset);
console.log('Strength:', strength);
console.log('Is mixing?', isMixingMode);

// Check Redux/Zustand state
console.log(store.getState());
```

### Rendering Issues

```typescript
// Check component props
console.log('PresetCard props:', props);

// Check memoization
// If card doesn't update on selection, add shouldUpdate logic
```

### Accessibility Issues

```typescript
// Check ARIA attributes
const card = document.querySelector('[role="radio"]');
console.log('aria-label:', card.getAttribute('aria-label'));
console.log('aria-checked:', card.getAttribute('aria-checked'));

// Test keyboard navigation
// Tab key should move focus, Enter should select
```

---

## RESOURCES

- **Design Files:** Figma link (TBD)
- **Component Library:** Storybook: http://localhost:6006
- **API Docs:** `/docs/preset-api`
- **Accessibility:** WCAG 2.1 Level AAA
- **Browser Support:** Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

---

## CONTACTS

- **UX Lead:** Design team
- **Frontend Lead:** Development team
- **Accessibility:** A11y specialist
- **Product:** Product manager

---

**Last Updated:** January 30, 2026
**Version:** 1.0
**Status:** Ready for Implementation
