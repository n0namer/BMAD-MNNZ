# PRESET UI IMPLEMENTATION GUIDE

**Version:** 1.0
**Status:** Ready for Development
**Target:** React/Vue + CSS/Tailwind Implementation
**Accessibility:** WCAG AAA Compliance

---

## TABLE OF CONTENTS

1. [Architecture Overview](#architecture-overview)
2. [Component Hierarchy](#component-hierarchy)
3. [State Management](#state-management)
4. [Props & Data Structures](#props--data-structures)
5. [CSS Classes & Tokens](#css-classes--tokens)
6. [Implementation Checklist](#implementation-checklist)
7. [Testing Guide](#testing-guide)
8. [Performance Optimization](#performance-optimization)

---

## ARCHITECTURE OVERVIEW

### System Design Philosophy

**Key Principles:**
1. **Component-First:** Reusable, composable building blocks
2. **State-Driven:** Single source of truth for preset selection
3. **Accessibility-Built-In:** ARIA, keyboard nav, screen readers from day 1
4. **Performance-Optimized:** Lazy loading, memoization, code splitting
5. **Mobile-First:** Desktop features as progressive enhancements

### High-Level Flow

```
┌──────────────────────────────────────────┐
│   <PresetSelector />                    │
│   (Main container)                      │
├──────────────────────────────────────────┤
│                                          │
│  Header: Title, instructions             │
│  ├─ <PresetCard /> × 5 (core presets)   │
│  │   ├─ Icon                           │
│  │   ├─ Label                          │
│  │   └─ Use Cases                      │
│  │                                     │
│  ├─ <PreviewPanel /> (conditional)     │
│  │   ├─ Before/After Toggle            │
│  │   ├─ Strength Slider (if applicable)│
│  │   └─ Apply Button                   │
│  │                                     │
│  ├─ <AdvancedPresets /> (collapsible)  │
│  │   └─ <PresetCard /> × 5             │
│  │                                     │
│  ├─ <CustomPresets /> (if any)         │
│  │   └─ <CustomPresetCard /> × N       │
│  │                                     │
│  └─ Action Buttons (Back, Next, etc.)  │
│                                          │
└──────────────────────────────────────────┘
```

---

## COMPONENT HIERARCHY

### Level 1: Main Container

```tsx
<PresetSelector
  onSelect={(presetId, options) => {}}
  onCancel={() => {}}
  defaultPreset="professional"
  allowMixing={true}
  showAdvanced={false}
  onAdvancedToggle={() => {}}
  customPresets={[]}
/>
```

**Responsibilities:**
- Manage overall selection state
- Coordinate child components
- Handle form submission
- Track user interactions (analytics)

### Level 2: Card Components

```tsx
<PresetCard
  id="professional"
  emoji="💼"
  label="Professional"
  tagline="Formal, authoritative"
  useCases={["Reports", "Emails", "Proposals"]}
  color="#1F2937"
  isSelected={false}
  onSelect={() => {}}
  onHover={() => {}}
  showExample={true}
  exampleText="..."
/>
```

**Responsibilities:**
- Display preset information
- Handle selection click
- Show/hide preview
- Manage hover state

### Level 3: Preview Components

```tsx
<PreviewPanel
  originalText="Original text..."
  transformedText="Transformed text..."
  presetName="Friendly"
  metrics={{
    formality: 40,
    warmth: 75,
    expression: "high"
  }}
  onApply={() => {}}
  onCancel={() => {}}
/>
```

**Responsibilities:**
- Display before/after comparison
- Show transformation metrics
- Handle apply/cancel
- Manage preview state

### Level 4: Utilities

```tsx
<StrengthSlider
  value={100}
  onChange={(value) => {}}
  label="Strength"
  min={10}
  max={100}
  step={10}
/>

<PresetMixer
  presets={[...]}
  onMix={(primary, secondary, ratio) => {}}
/>

<CustomPresetForm
  onSave={(name, params) => {}}
  basePreset="professional"
/>
```

---

## STATE MANAGEMENT

### Global State Structure

```typescript
interface PresetState {
  // Selection
  selectedPreset: string | null;           // "professional", "friendly", etc.
  selectedStrength: number;                // 0-100 (default: 100)

  // Mixing
  isMixingMode: boolean;
  mixedWith: string | null;
  mixRatio: number;                        // 0-100 (left-right blend)

  // UI
  isAdvancedOpen: boolean;
  showPreview: boolean;
  previewMode: 'before' | 'after';         // For toggle

  // History
  previousSelection: string | null;
  previousStrength: number;

  // Custom
  customPresets: CustomPreset[];
  favorites: string[];
}

interface CustomPreset {
  id: string;
  name: string;
  basePreset: string;
  parameters: {
    formality: number;      // 0-100
    tone: number;           // 0-100 (serious-playful)
    length: number;         // 0-100 (concise-verbose)
    vocabulary: number;     // 0-100 (simple-complex)
  };
  components?: string[];    // e.g., ["professional", "friendly"]
  ratio?: number;           // For mixed presets
}

interface PresetDefinition {
  id: string;
  emoji: string;
  label: string;
  tagline: string;
  useCases: string[];
  color: string;
  description: string;
  advanced?: boolean;       // Hidden by default if true
}
```

### State Management Pattern (Redux / Zustand Example)

**Redux:**
```typescript
// actions.ts
export const selectPreset = (presetId: string) => ({
  type: 'SELECT_PRESET',
  payload: presetId
});

export const setStrength = (value: number) => ({
  type: 'SET_STRENGTH',
  payload: value
});

export const toggleAdvanced = () => ({
  type: 'TOGGLE_ADVANCED'
});

// reducer.ts
const initialState: PresetState = {
  selectedPreset: null,
  selectedStrength: 100,
  isMixingMode: false,
  mixedWith: null,
  mixRatio: 50,
  isAdvancedOpen: false,
  showPreview: false,
  previewMode: 'after',
  previousSelection: null,
  previousStrength: 100,
  customPresets: [],
  favorites: []
};

export const presetReducer = (
  state = initialState,
  action: PresetAction
): PresetState => {
  switch (action.type) {
    case 'SELECT_PRESET':
      return {
        ...state,
        previousSelection: state.selectedPreset,
        selectedPreset: action.payload,
        showPreview: true,
      };

    case 'SET_STRENGTH':
      return {
        ...state,
        previousStrength: state.selectedStrength,
        selectedStrength: action.payload,
      };

    case 'TOGGLE_ADVANCED':
      return {
        ...state,
        isAdvancedOpen: !state.isAdvancedOpen,
      };

    default:
      return state;
  }
};
```

**Zustand (Alternative - Simpler):**
```typescript
import create from 'zustand';

interface PresetStore {
  state: PresetState;
  selectPreset: (id: string) => void;
  setStrength: (value: number) => void;
  toggleAdvanced: () => void;
  reset: () => void;
}

export const usePresetStore = create<PresetStore>((set) => ({
  state: initialState,

  selectPreset: (id: string) => set((prev) => ({
    state: {
      ...prev.state,
      previousSelection: prev.state.selectedPreset,
      selectedPreset: id,
      showPreview: true,
    }
  })),

  setStrength: (value: number) => set((prev) => ({
    state: {
      ...prev.state,
      selectedStrength: Math.min(100, Math.max(0, value)),
    }
  })),

  toggleAdvanced: () => set((prev) => ({
    state: {
      ...prev.state,
      isAdvancedOpen: !prev.state.isAdvancedOpen,
    }
  })),

  reset: () => set({ state: initialState }),
}));
```

---

## PROPS & DATA STRUCTURES

### PresetSelector Props

```typescript
interface PresetSelectorProps {
  // Callbacks
  onSelect: (presetId: string, options: SelectionOptions) => void;
  onCancel: () => void;
  onAdvancedToggle?: (isOpen: boolean) => void;

  // Initial State
  defaultPreset?: string;
  initialStrength?: number;
  initialText?: string;

  // Features
  allowMixing?: boolean;              // default: true
  allowCustom?: boolean;              // default: true
  showAdvanced?: boolean;             // default: false
  showPreview?: boolean;              // default: true

  // Data
  presets?: PresetDefinition[];        // Override core presets
  advancedPresets?: PresetDefinition[];
  customPresets?: CustomPreset[];

  // Localization
  locale?: 'en' | 'es' | 'fr' | 'de' | 'pt' | 'ja' | 'zh';
  translations?: LocalizationStrings;

  // Analytics
  onAnalytics?: (event: AnalyticsEvent) => void;

  // Style
  theme?: 'light' | 'dark' | 'auto';
  className?: string;
  style?: CSSProperties;
}

interface SelectionOptions {
  presetId: string;
  strength: number;
  mixedWith?: string;
  mixRatio?: number;
  customId?: string;
  transformedText?: string;
}

interface AnalyticsEvent {
  type: 'view' | 'select' | 'mix' | 'customize' | 'apply';
  presetId: string;
  timestamp: number;
  timeSpent: number;
}
```

### PresetCard Props

```typescript
interface PresetCardProps {
  // Data
  id: string;
  emoji: string;
  label: string;
  tagline: string;
  useCases: string[];
  color: string;

  // State
  isSelected: boolean;
  isHovered: boolean;

  // Callbacks
  onSelect: (id: string) => void;
  onHover: (id: string | null) => void;
  onPreview?: (id: string) => void;

  // Options
  showExample?: boolean;
  exampleText?: string;
  disabled?: boolean;

  // Style
  size?: 'small' | 'medium' | 'large';
  className?: string;
}
```

### Core Presets Data

```typescript
const CORE_PRESETS: PresetDefinition[] = [
  {
    id: 'professional',
    emoji: '💼',
    label: 'Professional',
    tagline: 'Formal, authoritative',
    useCases: ['Reports', 'Formal emails', 'Proposals'],
    color: '#1F2937',
    description: 'Corporate tone suitable for business communication',
  },
  {
    id: 'friendly',
    emoji: '💬',
    label: 'Friendly',
    tagline: 'Casual, conversational',
    useCases: ['Social posts', 'Comments', 'Chat messages'],
    color: '#047857',
    description: 'Warm, approachable tone for personal connection',
  },
  {
    id: 'creative',
    emoji: '✨',
    label: 'Creative',
    tagline: 'Imaginative, expressive',
    useCases: ['Stories', 'Marketing', 'Creative content'],
    color: '#9333EA',
    description: 'Artistic, unique voice for distinctive content',
  },
  {
    id: 'persuasive',
    emoji: '🎯',
    label: 'Persuasive',
    tagline: 'Compelling, action-driven',
    useCases: ['Sales copy', 'CTAs', 'Pitches'],
    color: '#DC2626',
    description: 'Motivating tone designed to inspire action',
  },
  {
    id: 'concise',
    emoji: '⚡',
    label: 'Concise',
    tagline: 'Direct, efficient',
    useCases: ['Headlines', 'Bios', 'Captions'],
    color: '#0891B2',
    description: 'Efficient, focused tone for scannable content',
  },
];

const ADVANCED_PRESETS: PresetDefinition[] = [
  {
    id: 'formal',
    emoji: '📋',
    label: 'Formal',
    tagline: 'Legal, academic',
    useCases: ['Legal documents', 'Formal papers', 'Academic writing'],
    color: '#1F2937',
    description: 'Structured, precise language for formal contexts',
    advanced: true,
  },
  // ... 4 more advanced presets
];
```

---

## CSS CLASSES & TOKENS

### Tailwind Configuration (if using Tailwind CSS)

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        preset: {
          professional: '#1F2937',
          friendly: '#047857',
          creative: '#9333EA',
          persuasive: '#DC2626',
          concise: '#0891B2',
        },
        surface: {
          primary: '#FFFFFF',
          secondary: '#F9FAFB',
          tertiary: '#F3F4F6',
        },
        text: {
          primary: '#1F2937',
          secondary: '#6B7280',
          tertiary: '#9CA3AF',
        },
        border: {
          light: '#E5E7EB',
          medium: '#D1D5DB',
          dark: '#9CA3AF',
        }
      },
      spacing: {
        'card-gap': '16px',
        'card-padding': '16px',
      },
      borderRadius: {
        'card': '8px',
        'input': '6px',
      },
      boxShadow: {
        'card-sm': '0 1px 2px rgba(0,0,0,0.05)',
        'card-md': '0 4px 6px rgba(0,0,0,0.1)',
        'card-lg': '0 8px 16px rgba(0,0,0,0.15)',
        'focus': '0 0 0 3px rgba(8,145,178,0.1)',
      },
      animation: {
        'select': 'selectFade 0.2s ease-out',
        'hover': 'hoverGlow 0.15s ease-in-out',
      },
      keyframes: {
        selectFade: {
          '0%': { opacity: '0', transform: 'scale(0.95)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
        hoverGlow: {
          '0%': { boxShadow: '0 0 0 0 rgba(31,41,55,0)' },
          '100%': { boxShadow: '0 4px 12px rgba(0,0,0,0.1)' },
        },
      },
    },
  },
};
```

### BEM Naming Convention (for CSS Modules / BEM)

```css
/* PresetSelector Container */
.preset-selector { }
.preset-selector--mobile { }
.preset-selector--dark { }

/* Preset Cards */
.preset-card { }
.preset-card--selected { }
.preset-card--hover { }
.preset-card--disabled { }
.preset-card__emoji { }
.preset-card__label { }
.preset-card__tagline { }
.preset-card__use-cases { }
.preset-card__button { }

/* Preview Panel */
.preview-panel { }
.preview-panel--visible { }
.preview-panel__header { }
.preview-panel__content { }
.preview-panel__toggle { }
.preview-panel__before { }
.preview-panel__after { }
.preview-panel__metrics { }

/* Strength Slider */
.strength-slider { }
.strength-slider__label { }
.strength-slider__track { }
.strength-slider__thumb { }
.strength-slider__value { }

/* Buttons */
.btn { }
.btn--primary { }
.btn--secondary { }
.btn--tertiary { }
.btn--disabled { }
.btn--loading { }

/* Accessibility */
.focus-visible { }
.sr-only { }
```

### CSS Variables (CSS Custom Properties)

```css
:root {
  /* Colors */
  --color-preset-professional: #1F2937;
  --color-preset-friendly: #047857;
  --color-preset-creative: #9333EA;
  --color-preset-persuasive: #DC2626;
  --color-preset-concise: #0891B2;

  --color-surface-primary: #FFFFFF;
  --color-surface-secondary: #F9FAFB;
  --color-text-primary: #1F2937;
  --color-text-secondary: #6B7280;
  --color-border: #E5E7EB;

  /* Typography */
  --font-family-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Hiragino Sans', 'Noto Sans CJK JP', sans-serif;
  --font-size-sm: 14px;
  --font-size-base: 16px;
  --font-size-lg: 18px;
  --font-size-xl: 20px;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.6;
  --line-height-loose: 1.7;

  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 12px;
  --spacing-lg: 16px;
  --spacing-xl: 24px;

  /* Transitions */
  --duration-fast: 150ms;
  --duration-base: 200ms;
  --duration-slow: 300ms;
  --easing-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --easing-out: cubic-bezier(0, 0, 0.2, 1);
}

/* Dark Mode */
@media (prefers-color-scheme: dark) {
  :root {
    --color-surface-primary: #1F2937;
    --color-text-primary: #F9FAFB;
    --color-border: #374151;
  }
}
```

---

## IMPLEMENTATION CHECKLIST

### Phase 1: Core Components (Week 1-2)

- [ ] **PresetCard Component**
  - [ ] Render emoji, label, tagline
  - [ ] Display use cases list
  - [ ] Handle click/selection
  - [ ] Apply selected styles
  - [ ] Keyboard navigation
  - [ ] Screen reader labels

- [ ] **PresetSelector Container**
  - [ ] Layout 5 core cards (3-col desktop, 2-col tablet, 1-col mobile)
  - [ ] Manage selection state
  - [ ] Show/hide preview panel
  - [ ] Action buttons (Back, Next)

- [ ] **PreviewPanel Component**
  - [ ] Before/after text display
  - [ ] Toggle between before/after
  - [ ] Show transformation metrics
  - [ ] Apply/Cancel buttons

- [ ] **Responsive Design**
  - [ ] Desktop (1200px+): 3-column grid
  - [ ] Tablet (768px): 2-column grid
  - [ ] Mobile (375px): 1-column stack
  - [ ] Touch targets: 48x48dp minimum

### Phase 2: Advanced Features (Week 3)

- [ ] **Advanced Presets**
  - [ ] Toggle to show 5 additional presets
  - [ ] Collapsible section with smooth animation
  - [ ] Same card styling as core

- [ ] **Strength Slider**
  - [ ] Range input from 10-100%
  - [ ] Real-time preview update (300ms debounce)
  - [ ] Shows different text transformations
  - [ ] Keyboard support (arrow keys)

- [ ] **Preset Mixing**
  - [ ] Select 2 presets to blend
  - [ ] Slider for ratio adjustment
  - [ ] Live preview of mixed result
  - [ ] Save as custom preset option

### Phase 3: Customization (Week 4)

- [ ] **Create Custom Preset Modal**
  - [ ] Input field for preset name
  - [ ] Base preset selection
  - [ ] Parameter sliders (formality, tone, etc.)
  - [ ] Live preview updates
  - [ ] Save/Cancel buttons

- [ ] **Saved Presets Display**
  - [ ] Show list of user's custom presets
  - [ ] Edit/delete options
  - [ ] Star/favorite functionality
  - [ ] Drag-to-reorder

- [ ] **Favorite Management**
  - [ ] Heart icon on cards
  - [ ] Save combinations
  - [ ] Quick access panel
  - [ ] Max 6 favorites visible

### Phase 4: Accessibility & Refinement (Week 5)

- [ ] **Keyboard Navigation**
  - [ ] Tab through all cards
  - [ ] Arrow keys to navigate grid
  - [ ] Space/Enter to select
  - [ ] Escape to cancel/close
  - [ ] Tab order correct

- [ ] **Screen Reader Testing**
  - [ ] ARIA labels on all elements
  - [ ] Role attributes correct
  - [ ] Live regions for updates
  - [ ] Test with NVDA, JAWS, VoiceOver

- [ ] **Color & Contrast**
  - [ ] WCAG AAA (7:1) contrast ratio
  - [ ] Color-blind simulator pass
  - [ ] High contrast mode support
  - [ ] Dark mode support

- [ ] **Motion & Animation**
  - [ ] Smooth transitions (200ms)
  - [ ] Respect prefers-reduced-motion
  - [ ] No jarring effects
  - [ ] GPU-accelerated where possible

- [ ] **Performance**
  - [ ] Lazy load advanced presets
  - [ ] Memoize card components
  - [ ] Debounce preview updates
  - [ ] Code split preview panel

- [ ] **Documentation**
  - [ ] Component prop documentation
  - [ ] Usage examples
  - [ ] Accessibility features
  - [ ] Configuration guide

### Phase 5: Testing (Week 6)

- [ ] **Unit Tests**
  - [ ] State management logic
  - [ ] Component rendering
  - [ ] Event handlers
  - [ ] Conditional rendering

- [ ] **Integration Tests**
  - [ ] Selection workflow
  - [ ] Preview updates
  - [ ] Form submission
  - [ ] Custom preset creation

- [ ] **E2E Tests (Playwright/Cypress)**
  - [ ] Full user workflow
  - [ ] Mobile interactions
  - [ ] Keyboard navigation
  - [ ] Form validation

- [ ] **Usability Testing**
  - [ ] 5-8 users
  - [ ] Task completion rate >85%
  - [ ] Time on task <90 seconds
  - [ ] SUS score >75

---

## TESTING GUIDE

### Unit Tests (Jest + React Testing Library)

```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import PresetCard from './PresetCard';

describe('PresetCard', () => {
  const mockProps = {
    id: 'professional',
    emoji: '💼',
    label: 'Professional',
    tagline: 'Formal, authoritative',
    useCases: ['Reports', 'Emails'],
    color: '#1F2937',
    isSelected: false,
    onSelect: jest.fn(),
  };

  it('renders card with preset information', () => {
    render(<PresetCard {...mockProps} />);

    expect(screen.getByText('Professional')).toBeInTheDocument();
    expect(screen.getByText('Formal, authoritative')).toBeInTheDocument();
    expect(screen.getByText('Reports')).toBeInTheDocument();
  });

  it('calls onSelect when clicked', async () => {
    const user = userEvent.setup();
    render(<PresetCard {...mockProps} />);

    await user.click(screen.getByRole('button'));

    expect(mockProps.onSelect).toHaveBeenCalledWith('professional');
  });

  it('applies selected styles when isSelected=true', () => {
    const { container } = render(
      <PresetCard {...mockProps} isSelected={true} />
    );

    expect(container.querySelector('.preset-card--selected')).toBeInTheDocument();
  });

  it('is keyboard accessible', async () => {
    const user = userEvent.setup();
    render(<PresetCard {...mockProps} />);

    const button = screen.getByRole('button');
    button.focus();

    expect(button).toHaveFocus();

    await user.keyboard('{Enter}');
    expect(mockProps.onSelect).toHaveBeenCalled();
  });

  it('has proper ARIA labels', () => {
    render(<PresetCard {...mockProps} />);

    const button = screen.getByRole('button', {
      name: /professional/i
    });

    expect(button).toHaveAccessibleName();
  });
});
```

### Integration Tests

```typescript
describe('PresetSelector Integration', () => {
  it('completes full preset selection workflow', async () => {
    const user = userEvent.setup();
    const mockOnSelect = jest.fn();

    render(
      <PresetSelector
        onSelect={mockOnSelect}
        showPreview={true}
      />
    );

    // Click Professional card
    await user.click(screen.getByRole('button', {
      name: /professional/i
    }));

    // Preview should show
    expect(screen.getByText(/how your text transforms/i)).toBeInTheDocument();

    // Click Apply
    await user.click(screen.getByRole('button', {
      name: /apply/i
    }));

    // Verify callback
    expect(mockOnSelect).toHaveBeenCalledWith('professional', expect.any(Object));
  });

  it('handles preset switching', async () => {
    const user = userEvent.setup();
    render(<PresetSelector />);

    // Select Professional
    await user.click(screen.getByRole('button', {
      name: /professional/i
    }));

    // Verify Professional preview shows
    expect(screen.getByText(/professional/i)).toBeInTheDocument();

    // Switch to Friendly
    await user.click(screen.getByRole('button', {
      name: /friendly/i
    }));

    // Verify Friendly preview shows
    expect(screen.getByText(/friendly/i)).toBeInTheDocument();
  });
});
```

### E2E Tests (Playwright)

```typescript
import { test, expect } from '@playwright/test';

test.describe('Preset Selector E2E', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000/presets');
  });

  test('user selects preset and generates content', async ({ page }) => {
    // Click Professional card
    await page.click('[data-testid="preset-card-professional"]');

    // Verify selection
    await expect(page.locator('[data-testid="preview-panel"]')).toBeVisible();

    // Verify preview text
    const preview = await page.textContent('[data-testid="preview-text"]');
    expect(preview).toBeTruthy();

    // Click Apply
    await page.click('button:has-text("Apply")');

    // Should navigate or close
    await expect(page.locator('[data-testid="preset-selector"]')).not.toBeVisible();
  });

  test('mobile keyboard navigation works', async ({ page }) => {
    // Tab to first card
    await page.keyboard.press('Tab');

    // Verify focus
    const focused = await page.locator(':focus');
    expect(focused).toHaveAttribute('data-testid', 'preset-card-professional');

    // Arrow to next
    await page.keyboard.press('ArrowRight');

    // Verify focus moved
    const newFocus = await page.locator(':focus');
    expect(newFocus).toHaveAttribute('data-testid', 'preset-card-friendly');

    // Select with Enter
    await page.keyboard.press('Enter');

    // Verify selection
    expect(newFocus).toHaveClass('preset-card--selected');
  });

  test('accessibility audit passes', async ({ page }) => {
    // Run accessibility scan
    const results = await page.accessibilitySnapshot();

    expect(results.violations).toHaveLength(0);
    expect(results).toMatchObject({
      violations: [],
      passes: expect.any(Array),
    });
  });
});
```

### Accessibility Audit

```typescript
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

describe('PresetSelector Accessibility', () => {
  it('should not have any accessibility violations', async () => {
    const { container } = render(
      <PresetSelector
        presets={CORE_PRESETS}
        onSelect={() => {}}
      />
    );

    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('should meet WCAG AAA color contrast', async () => {
    const { container } = render(<PresetSelector />);

    // Test specific color combinations
    const cards = container.querySelectorAll('.preset-card');

    cards.forEach(card => {
      const bgColor = getComputedStyle(card).backgroundColor;
      const textColor = getComputedStyle(card).color;

      const contrast = getContrastRatio(bgColor, textColor);
      expect(contrast).toBeGreaterThanOrEqual(7); // WCAG AAA
    });
  });
});
```

---

## PERFORMANCE OPTIMIZATION

### Code Splitting

```typescript
// Split preview panel (lazy load)
const PreviewPanel = lazy(() => import('./PreviewPanel'));
const AdvancedPresets = lazy(() => import('./AdvancedPresets'));
const CustomPresetForm = lazy(() => import('./CustomPresetForm'));

export function PresetSelector(props: PresetSelectorProps) {
  return (
    <Suspense fallback={<PresetCardSkeleton />}>
      {/* Core presets always visible */}
      {CORE_PRESETS.map(preset => (
        <PresetCard key={preset.id} {...preset} />
      ))}

      {/* Lazy load preview on selection */}
      {selectedPreset && (
        <Suspense fallback={<div>Loading preview...</div>}>
          <PreviewPanel presetId={selectedPreset} />
        </Suspense>
      )}
    </Suspense>
  );
}
```

### Memoization

```typescript
// Memoize expensive components
export const PresetCard = memo(function PresetCard({
  id,
  emoji,
  label,
  // ...props
}: PresetCardProps) {
  return (
    <div className="preset-card" role="radio">
      {/* ... */}
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison for specific props
  return (
    prevProps.id === nextProps.id &&
    prevProps.isSelected === nextProps.isSelected &&
    prevProps.isHovered === nextProps.isHovered
  );
});

// Memoize callback
const handleSelect = useCallback((presetId: string) => {
  onSelect(presetId);
}, [onSelect]);
```

### Debouncing & Throttling

```typescript
// Debounce preview updates
const debouncedPreview = useMemo(
  () => debounce((text: string) => {
    generatePreview(selectedPreset, text);
  }, 300),
  [selectedPreset]
);

// Throttle hover events
const throttledHover = useCallback(
  throttle((id: string | null) => {
    setHoveredCard(id);
  }, 50),
  []
);
```

### Bundle Analysis

```bash
# Analyze bundle size
npm run build -- --analyze

# Tree-shake unused code
npm run build -- --minify terser

# Monitor performance
npm run lighthouse
```

### Performance Budget

```json
{
  "bundles": [
    {
      "name": "preset-selector",
      "path": "dist/preset-selector.js",
      "maxSize": "45kb"
    },
    {
      "name": "preview-panel",
      "path": "dist/preview-panel.js",
      "maxSize": "35kb"
    }
  ],
  "metrics": [
    {
      "name": "First Contentful Paint",
      "threshold": "1500ms"
    },
    {
      "name": "Time to Interactive",
      "threshold": "2500ms"
    },
    {
      "name": "Cumulative Layout Shift",
      "threshold": "0.1"
    }
  ]
}
```

---

## DEPLOYMENT CHECKLIST

### Pre-Launch

- [ ] All tests passing (>90% coverage)
- [ ] Lighthouse score >90 (performance, accessibility, best practices)
- [ ] Bundle size <50kb gzipped
- [ ] No console errors or warnings
- [ ] Accessibility audit (axe) passes
- [ ] Mobile viewport tested
- [ ] Dark mode tested
- [ ] Keyboard navigation tested
- [ ] Screen reader tested (3 readers minimum)
- [ ] Analytics events logging
- [ ] Error boundary in place
- [ ] Loading states defined
- [ ] Error states defined

### Rollout Strategy

1. **Stage 1: Internal Testing** (1 week)
   - Team testing
   - Feedback collection
   - Bug fixes

2. **Stage 2: Beta Release** (1 week)
   - 10% of users
   - Monitor error rates
   - Gather feedback

3. **Stage 3: Gradual Rollout** (2 weeks)
   - 25% → 50% → 100%
   - Performance monitoring
   - Issue response

4. **Stage 4: Full Release** (ongoing)
   - Monitor analytics
   - Collect user feedback
   - Plan improvements

---

**Implementation Guide Complete**

Ready for development team handoff.

Questions? Create an issue or contact UX team.
