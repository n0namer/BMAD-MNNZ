# Frontend - Shared UI Components

**Status**: 🟠 WAITING FOR BACKEND #2 SIGNAL

---

## Overview

Shared UI component library used across the entire project:
- Dashboard (E11)
- Backend integrations (E9+, E12+, E13+, E14+, E15+)
- All frontend features

---

## Architecture

```
src/frontend/
├── components/              # Reusable UI components
│   ├── buttons/
│   ├── inputs/
│   ├── modals/
│   ├── tables/
│   ├── cards/
│   └── layout/
├── hooks/                   # Custom React/utility hooks
│   ├── useApi.ts
│   ├── useFetch.ts
│   └── useLocalStorage.ts
├── styles/                  # CSS/SCSS styling
│   ├── variables.css
│   ├── components.css
│   └── utilities.css
├── utils/                   # Helper functions
│   ├── format.ts
│   ├── validation.ts
│   └── api.ts
├── types/                   # Shared TypeScript types
│   ├── api.ts
│   ├── components.ts
│   └── store.ts
└── index.ts                 # Main export file
```

---

## Components (To Be Implemented)

### Data Display
- `DataTable` - Sortable, filterable table
- `Chart` - Generic chart wrapper
- `MetricCard` - KPI display
- `Timeline` - Event timeline

### Forms & Input
- `TextField` - Text input
- `Select` - Dropdown
- `DatePicker` - Date selection
- `Checkbox` - Toggle/checkbox
- `RadioGroup` - Radio buttons

### Navigation & Layout
- `Header` - App header
- `Sidebar` - Navigation sidebar
- `Breadcrumbs` - Navigation path
- `Tabs` - Tab navigation
- `Pagination` - Page navigation

### Feedback
- `Alert` - Alert/notification
- `Modal` - Dialog/popup
- `Toast` - Toast notification
- `Badge` - Status badge
- `Spinner` - Loading indicator

---

## Usage Example

```typescript
// Import from src/frontend
import { DataTable, Alert, Button } from '../frontend';

// Use in Dashboard or other components
export const MyComponent = () => {
  return (
    <div>
      <Alert type="info">Data loading...</Alert>
      <DataTable columns={cols} data={rows} />
      <Button onClick={handler}>Submit</Button>
    </div>
  );
};
```

---

## Hooks

### useApi
Fetch data from API with caching:
```typescript
const { data, loading, error } = useApi('/api/runs');
```

### useFetch
Generic fetch wrapper:
```typescript
const [data, setData] = useState(null);
useFetch('/endpoint', data => setData(data));
```

### useLocalStorage
Persistent local storage:
```typescript
const [value, setValue] = useLocalStorage('key', defaultValue);
```

---

## Styling

Uses CSS variables for theming:
```css
:root {
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --spacing-unit: 8px;
  --border-radius: 4px;
}
```

---

## Integration Points

### Dashboard (E11)
- Uses all data display components
- Uses forms for mode toggles & filters
- Custom charts via Plotly/D3

### Backend Features (E9+)
- API integration components
- Form inputs for user interaction
- Data display tables & cards

### Responsive Design
- Mobile-first approach
- Breakpoints: sm (640px), md (768px), lg (1024px), xl (1280px)
- Touch-friendly inputs

---

## Dependencies

- **Plotly**: For chart rendering
- **D3.js**: For advanced visualizations
- **TypeScript**: For type safety
- **Testing**: Jest + Testing Library

---

## Development

### Component Template

```typescript
// components/MyComponent/index.ts
export interface MyComponentProps {
  // Props definition
}

export const MyComponent: React.FC<MyComponentProps> = (props) => {
  return <div>{/* Component JSX */}</div>;
};

// Export from index.ts
export { MyComponent } from './components/MyComponent';
```

### Testing

```typescript
// components/MyComponent/__tests__/index.test.ts
describe('MyComponent', () => {
  it('should render', () => {
    render(<MyComponent />);
    // Test assertions
  });
});
```

---

## Current Status

- **Architecture**: ✅ DEFINED
- **Components**: ⏳ PENDING (Blocked by Backend #2)
- **Hooks**: ⏳ PENDING
- **Styles**: ⏳ PENDING
- **Testing**: ⏳ PENDING

---

## Next Action

**🟠 WAITING FOR SIGNAL**: Backend #2 completion of US-F1a-007

Once signal received:
1. ✅ Define API contract
2. ✅ Create hooks for API integration
3. ✅ Build core components
4. ✅ Integrate with Dashboard

---

**Created**: 2026-02-28
**Status**: Ready for component implementation (blocked)
**Used By**: Dashboard (E11) + All Backend Features
