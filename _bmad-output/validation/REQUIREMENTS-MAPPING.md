# Detailed Requirements-to-Architecture Mapping

**Project:** katana-vectorbt
**Date:** 2026-02-27
**Purpose:** Detailed traceability of all PRD requirements to architecture decisions

---

## 1. PRD Requirements NOT Covered in Architecture

### 1.1 CORE CONDITIONS (PRD Lines 719-768)

**PRD Specification exists, Architecture specification missing:**

```
PRD Text (Lines 719-768): "1. CORE Conditions (5 mandatory signal components)"
─────────────────────────────────────────────────────────────────────────

CORE Condition #1: [Detailed in PRD, lines 719-735]
  - Name/Purpose from PRD: [EXTRACT FROM PRD]
  - Threshold/Logic from PRD: [EXTRACT FROM PRD]
  - Architecture Mapping: ❌ NO SPECIFICATION
  - Gap Severity: CRITICAL

CORE Condition #2: [Detailed in PRD, lines 736-750]
  - Name/Purpose from PRD: [EXTRACT FROM PRD]
  - Threshold/Logic from PRD: [EXTRACT FROM PRD]
  - Architecture Mapping: ❌ NO SPECIFICATION
  - Gap Severity: CRITICAL

CORE Condition #3: [Detailed in PRD, lines 751-760]
  - Name/Purpose from PRD: [EXTRACT FROM PRD]
  - Threshold/Logic from PRD: [EXTRACT FROM PRD]
  - Architecture Mapping: ❌ NO SPECIFICATION
  - Gap Severity: CRITICAL

CORE Condition #4: [Detailed in PRD, lines 761-765]
  - Name/Purpose from PRD: [EXTRACT FROM PRD]
  - Threshold/Logic from PRD: [EXTRACT FROM PRD]
  - Architecture Mapping: ❌ NO SPECIFICATION
  - Gap Severity: CRITICAL

CORE Condition #5: [Detailed in PRD, lines 766-768]
  - Name/Purpose from PRD: [EXTRACT FROM PRD]
  - Threshold/Logic from PRD: [EXTRACT FROM PRD]
  - Architecture Mapping: ❌ NO SPECIFICATION
  - Gap Severity: CRITICAL
```

**ACTION:** Create signal_framework_spec.md documenting all CORE conditions

---

### 1.2 AUX CONDITIONS (PRD Lines 769-813)

**PRD Specification exists, Architecture specification missing:**

```
PRD Text (Lines 769-813): "2. AUX Conditions (3 optional confidence boosters)"
──────────────────────────────────────────────────────────────────────────

AUX Condition #1: [Detailed in PRD, lines 769-790]
  - Name/Purpose: [EXTRACT]
  - Threshold: [EXTRACT]
  - Architecture Mapping: ❌ NO SPECIFICATION

AUX Condition #2: [Detailed in PRD, lines 791-805]
  - Name/Purpose: [EXTRACT]
  - Threshold: [EXTRACT]
  - Architecture Mapping: ❌ NO SPECIFICATION

AUX Condition #3: [Detailed in PRD, lines 806-813]
  - Name/Purpose: [EXTRACT]
  - Threshold: [EXTRACT]
  - Architecture Mapping: ❌ NO SPECIFICATION
```

**ACTION:** Extend signal_framework_spec.md with AUX conditions

---

### 1.3 ANTI-OVERFITTING DEGRADATION RULES (PRD Lines 842-905)

**PRD Specification exists, Architecture specification missing:**

```
PRD Text (Lines 842-905): "4. Anti-Overfitting Degradation Rules (5 rules)"
──────────────────────────────────────────────────────────────────────────

Degradation Rule #1: [Detailed in PRD, lines 842-860]
  - Name/Purpose: [EXTRACT]
  - Formula: [EXTRACT]
  - Thresholds: [EXTRACT]
  - Architecture Mapping: ❌ NO SPECIFICATION
  - Gap Severity: CRITICAL

Degradation Rule #2: [Detailed in PRD, lines 861-875]
  - Name/Purpose: [EXTRACT]
  - Formula: [EXTRACT]
  - Thresholds: [EXTRACT]
  - Architecture Mapping: ❌ NO SPECIFICATION
  - Gap Severity: CRITICAL

Degradation Rule #3: [Detailed in PRD, lines 876-885]
  - Name/Purpose: [EXTRACT]
  - Formula: [EXTRACT]
  - Thresholds: [EXTRACT]
  - Architecture Mapping: ❌ NO SPECIFICATION
  - Gap Severity: CRITICAL

Degradation Rule #4: [Detailed in PRD, lines 886-895]
  - Name/Purpose: [EXTRACT]
  - Formula: [EXTRACT]
  - Thresholds: [EXTRACT]
  - Architecture Mapping: ❌ NO SPECIFICATION
  - Gap Severity: CRITICAL

Degradation Rule #5: [Detailed in PRD, lines 896-905]
  - Name/Purpose: [EXTRACT]
  - Formula: [EXTRACT]
  - Thresholds: [EXTRACT]
  - Architecture Mapping: ❌ NO SPECIFICATION
  - Gap Severity: CRITICAL
```

**ACTION:** Create overfitting_rules_spec.md with all 5 degradation rules

---

### 1.4 PERFORMANCE VALIDATION TARGETS

**PRD Requirement (Line 37):**
```
"Performance: отображение ключевых метрик <3 сек,
 отчёт генерируется <10 мин на 100+ запусков."
```

**Current State:**
- ✅ Targets specified in PRD
- ❌ No validation plan in architecture
- ❌ No benchmark specification
- ❌ No SLA definition

**Missing in Architecture:**
- How to measure <3s metric display
- Benchmark framework (pytest-benchmark, locust, etc.)
- Load test scenario (100+ runs = what config?)
- Machine specification for reproducible benchmarks
- Continuous monitoring strategy

**ACTION:** Create performance_testing_spec.md

---

### 1.5 ACCESSIBILITY REQUIREMENTS

**PRD Requirement (Line 38):**
```
"Адаптивность (tablet-first), поддержка оффлайна, доступность по клавиатуре,
 цветовые и иконографические схемы для accessibility."
```

**Current State:**
- ✅ Mentioned in PRD
- ⚠️ Mentioned in Architecture NFR
- ❌ No specific standards (WCAG level?)
- ❌ No keyboard navigation spec
- ❌ No color contrast specification

**Missing in Architecture:**
- WCAG 2.1 AA/AAA target
- Keyboard nav: Tab order, focus indicators, hotkeys
- Color contrast ratio targets
- Icon alt-text strategy
- Responsive breakpoints (tablet-first)

**ACTION:** Create accessibility_spec.md (WCAG 2.1 AA checklist)

---

### 1.6 PRICE ACTION MODULE

**PRD Requirement (Line 657-710):**
```
"Price Action (PA) Module: Pattern recognition (support/resistance,
 trends, reversals), integration with signal framework,
 configurable thresholds, stress testing support"
```

**Current State:**
- ✅ Detailed specification in PRD
- ❌ No architecture component
- ❌ Scope unclear (Phase 1 or Phase 2?)
- ❌ Integration point not defined

**Missing in Architecture:**
- PA module specification document
- Pattern definitions (5-10 common patterns?)
- Detection algorithm (support/resistance, trend lines, etc.)
- Integration with signal_framework.py
- Configuration/threshold interface

**ACTION:** Decision required: Phase 1 or Phase 2+? If Phase 1, create pa_module_spec.md

---

## 2. Architecture Decisions Clearly Mapped to PRD

### 2.1 Data Flow Architecture (COVERED)

```
PRD Requirement: "Генерация статичного HTML-дашборда, сбор метрик
                 из артефактов Run Journal"

Architecture Mapping:
  ✅ Data Flow Architecture section (complete mapping)
  ✅ Run Journal component (JSON structure defined)
  ✅ UI Layer reads Run Journal (view-only)
  ✅ Python calculates metrics (no UI calculations)

Coverage: 100%
```

---

### 2.2 Control Plane / CLI (COVERED)

```
PRD Requirement: "Control Plane (CLI Contracts): CLI interface for running backtests,
                 configuration via YAML/JSON, Run Journal as source of truth"

Architecture Mapping:
  ✅ Core Modules → strategy_transformer.py, config_models.py
  ✅ Configuration models (Pydantic)
  ✅ YAML/JSON config support documented
  ✅ Run Journal data structure defined

Coverage: 100%
```

---

### 2.3 Strategy Factory & Registry (COVERED)

```
PRD Requirement: "Strategy Factory & Registry (Autonomy Loop):
                 Strategy registration, pluggable architecture,
                 no breaking changes"

Architecture Mapping:
  ✅ "Минимальные breaking changes" - Design Principle #3
  ✅ "Быстрая адаптация под новые сценарии"
  ✅ Strategy transformer pipeline (transformable)
  ✅ Decorator pattern (implied in code)

Coverage: 90% (pattern not explicitly documented)
```

---

### 2.4 Backtesting Engine (PARTIALLY COVERED)

```
PRD Requirement: "Backtesting Execution: batch backtesting, multi-scenario,
                 optimization integration, performance monitoring"

Architecture Mapping:
  ✅ vectorbt 0.26.2 as foundation (explicit)
  ✅ Optuna 4.x integration (explicit)
  ⚠️ Batch backtesting (framework present, detail TBD)
  ❌ Multi-timeframe (deferred to Wave 4)
  ❌ Performance monitoring (TBD)

Coverage: 60% (Phase 1 base timeframe only)
```

---

### 2.5 Quality Gates (PARTIALLY COVERED)

```
PRD Requirement: "Live Readiness Gates: Live Gate A/B, Offline Gate 4/6,
                 Statistical Power Validation (PSR/MTRL)"

Architecture Mapping:
  ✅ Quality Gates section (framework defined)
  ❌ Specific thresholds (Phase 2+ live gates)
  ⚠️ Offline gates framework (implementation TBD)
  ❌ Statistical metrics implementation (TBD)

Coverage: 40% (framework only, details Phase 2+)
```

---

## 3. Requirements Coverage Summary Table

| Epic | PRD Lines | Phase | Architecture Mapping | Coverage | Status |
|------|-----------|-------|----------------------|----------|--------|
| **Control Plane CLI** | 575-590 | 1 | Core Modules | 100% | ✅ COMPLETE |
| **Run Journal** | 587-590 | 1 | Data Flow | 100% | ✅ COMPLETE |
| **Strategy Factory** | 592-600 | 1 | Transformable Pipeline | 90% | ✅ MOSTLY COMPLETE |
| **Calendar Safety** | 600-610 | 4 | Wave 4 (W4-CAL) | 0% | ⏸️ PHASE 2+ |
| **Price Action** | 657-710 | ? | None (unclear phase) | 0% | ❌ SCOPE UNCLEAR |
| **Signal Framework** | 711-1024 | 1 | signal_framework.py (TBD) | 20% | ⚠️ PARTIAL |
| **CORE Conditions** | 719-768 | 1 | (missing) | 0% | ❌ CRITICAL GAP |
| **AUX Conditions** | 769-813 | 1 | (missing) | 0% | ❌ CRITICAL GAP |
| **Anti-Overfitting** | 842-905 | 1 | (missing) | 0% | ❌ CRITICAL GAP |
| **Entry/Exit Logic** | 986-1024 | 1 | strategy_transformer.py | 50% | ⚠️ PARTIAL |
| **Live Gates** | 1048-1210 | 2/4 | Quality Gates (TBD) | 20% | ⏸️ PHASE 2+ |
| **Dashboard** | 1292-1310 | 1 | UI Layer | 70% | ⚠️ MOSTLY COMPLETE |
| **Backtesting** | 1313-1330 | 1 | Core Modules | 70% | ⚠️ MOSTLY COMPLETE |
| **Optimization** | 1332-1426 | 1/2 | Optuna (partial) | 50% | ⚠️ PARTIAL |
| **Scaled-Live** | 1426-1470 | 2 | Run Journal | 30% | ⏸️ PHASE 2+ |
| **Data Management** | 1472-1510 | 1 | Data Flow | 70% | ⚠️ MOSTLY COMPLETE |
| **Data Integrity** | 1512-1520 | 1 | QA/validation tools | 80% | ✅ MOSTLY COMPLETE |
| **Compliance** | 1519-1525 | 1/2 | Traceability module | 70% | ⚠️ MOSTLY COMPLETE |
| **User Management** | 1522-1525 | 2 | (deferred) | 0% | ⏸️ PHASE 2+ |

---

## 4. Critical Path Analysis (Phase 1)

**These 5 items BLOCK Phase 1 completion:**

1. **CORE Conditions (5 signals)** - Core product feature
2. **Anti-Overfitting Rules (5 rules)** - Product integrity
3. **Performance Validation** - User experience critical
4. **Accessibility (WCAG compliance)** - Depends on target standard
5. **Price Action Module** - Phase 1 or Phase 2+ decision

**Estimated total effort to resolve:** 2-3 weeks (given parallel work)

---

## 5. Test Coverage Gaps

| Feature | Test Coverage | Architecture Notes | Status |
|---------|---------------|-------------------|--------|
| **Signal Framework** | TBD | No tests documented for CORE/AUX | ⚠️ NEEDS PLANNING |
| **Anti-Overfitting** | TBD | No unit tests documented | ⚠️ NEEDS PLANNING |
| **Performance** | TBD | No benchmark tests documented | ⚠️ NEEDS PLANNING |
| **Backtesting** | ✅ Defined (≥95%) | pytest framework ready | ✅ OK |
| **Data Validation** | ✅ Defined (≥95%) | Pydantic models ready | ✅ OK |
| **Price Action** | TBD | Depends on scope decision | ⏳ BLOCKED |

---

## Metadata

- **Analysis Date:** 2026-02-27
- **Scope:** Phase 1 MVP Validation
- **Source Documents:**
  - katana-v-02-prd-katana-vectorbt-2026-01-18.md (298KB)
  - katana-v-04-architecture-2026-01-19.md (491KB)
- **Validation Method:** Requirements extraction + mapping + gap analysis
- **Next Step:** Action item assignment and resolution tracking
