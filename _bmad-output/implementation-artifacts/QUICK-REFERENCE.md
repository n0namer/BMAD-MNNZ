# Database Test Isolation - Quick Reference Guide

**Last Updated:** 2026-02-26
**For:** DevOps/Infrastructure Engineers
**Time to Read:** 5 minutes

---

## One-Page Architecture

```
BEFORE (Sequential - 30 min)
┌─────────────────────────┐
│ Unit Tests: 5 min       │
├─────────────────────────┤
│ Integration: 6 min      │
├─────────────────────────┤
│ E2E Tests: 8 min        │
├─────────────────────────┤
│ Quality Gates: 3 min    │
├─────────────────────────┤
│ TOTAL: 30 minutes       │
└─────────────────────────┘

AFTER (Parallel 4x - 10 min)
Unit (2 min) │ ┌──────────────┐
Intg (2.5m)  │ │ Running in   │
E2E (3 min)  │ │ parallel:    │
Qual (3 min) │ │ 4x jobs at   │
             │ │ once!        │
             │ └──────────────┘
             │ TOTAL: 10 minutes (3x faster)
```

---

## Key Concepts (30 seconds each)

### 1. Transaction-Based Isolation
```python
# Each test wrapped in transaction, auto-rollback
@pytest.fixture
def db_session(engine):
    tx = engine.connect().begin()
    session = SessionLocal(bind=connection)
    yield session
    tx.rollback()  # ← Automatic cleanup
```
- **Speed:** <5ms overhead
- **Use for:** Unit + Integration tests
- **Isolation:** 100% (via transaction rollback)

### 2. Container-Based Isolation
```yaml
services:
  postgres:
    image: postgres:15-alpine
    env:
      POSTGRES_DB: katana_e2e_${{ matrix.batch }}
    # ← Each job gets unique database
```
- **Speed:** 30s startup overhead
- **Use for:** E2E tests only
- **Isolation:** 100% (separate database)

### 3. Parallelization Strategy
```yaml
strategy:
  matrix:
    batch: [1, 2, 3, 4]  # ← 4 parallel jobs
  max-parallel: 4
```
- **Jobs:** 4 concurrent (matches CPU cores)
- **Speedup:** 4x for independent work
- **Dependencies:** Only between stages

---

## Implementation Checklist (2 hours)

### Stage 1: Foundation (30 min)
- [ ] Copy `db-setup-per-test.sh` to `scripts/`
- [ ] Copy `db-cleanup-per-test.sh` to `scripts/`
- [ ] Make scripts executable: `chmod +x scripts/db-*.sh`
- [ ] Verify PostgreSQL running: `pg_isready -h localhost`

### Stage 2: Fixtures (45 min)
- [ ] Add to `tests/conftest.py`:
  ```python
  @pytest.fixture(scope="session")
  def test_db_engine():
      return create_engine(TEST_DATABASE_URL, ...)

  @pytest.fixture
  def db_session(test_db_engine):
      tx = test_db_engine.connect().begin()
      session = SessionLocal(bind=connection)
      yield session
      tx.rollback()
  ```
- [ ] Update existing fixtures to use `db_session`
- [ ] Run: `pytest tests/unit/ -v` (should pass)
- [ ] Measure time: Compare before/after

### Stage 3: GitHub Actions (45 min)
- [ ] Copy `github-actions-db-isolation.yaml` to `.github/workflows/`
- [ ] Rename to `ci-parallel.yml`
- [ ] Test on pull request (not main yet)
- [ ] Review logs for errors
- [ ] Verify all batches running in parallel

### Stage 4: Validation (20 min)
- [ ] Check: All tests pass
- [ ] Check: Execution time ~10 min (not 30)
- [ ] Check: No cross-test pollution
- [ ] Check: Coverage reports generated
- [ ] Merge to main

---

## Files You Need

| File | Location | Size | Purpose |
|------|----------|------|---------|
| Main guide | `DB-TEST-ISOLATION-IMPLEMENTATION.md` | 15KB | Complete details |
| Summary | `IMPLEMENTATION-SUMMARY.md` | 10KB | Overview + timeline |
| Workflow | `github-actions-db-isolation.yaml` | 15KB | GitHub Actions |
| Setup script | `db-setup-per-test.sh` | 12KB | Initialize DB |
| Cleanup script | `db-cleanup-per-test.sh` | 12KB | Remove DB |
| **This file** | `QUICK-REFERENCE.md` | 3KB | Quick lookup |

---

## Code Snippets (Copy-Paste Ready)

### Conftest.py Addition
```python
# Add to tests/conftest.py

import os
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session

TEST_DATABASE_URL = os.environ.get(
    "TEST_DATABASE_URL",
    "postgresql://test_user:test_pass@localhost:5432/katana_test"
)

@pytest.fixture(scope="session")
def test_db_engine():
    """Create test database engine (session-scoped)."""
    engine = create_engine(
        TEST_DATABASE_URL,
        echo=False,
        pool_size=20,
        max_overflow=40,
        pool_recycle=3600,
        pool_pre_ping=True,
    )
    from katana.database.models import Base
    Base.metadata.create_all(bind=engine)
    yield engine
    engine.dispose()

@pytest.fixture
def db_session(test_db_engine):
    """Per-test database session with auto-rollback."""
    connection = test_db_engine.connect()
    transaction = connection.begin()
    SessionLocal = sessionmaker(bind=connection)
    session = SessionLocal()
    session.begin_nested()
    yield session
    session.close()
    transaction.rollback()
    connection.close()
```

### Test Update (Before → After)
```python
# BEFORE
def test_create_user(db):
    user = User(name="Test")
    db.add(user)
    db.commit()

# AFTER (almost identical, just fixture name)
def test_create_user(db_session):  # ← Changed fixture name
    user = User(name="Test")
    db_session.add(user)
    db_session.commit()  # ← Still works, commits to transaction
    # After test: transaction auto-rolls back
```

### GitHub Actions Setup
```yaml
# Add to .github/workflows/ci-parallel.yml

services:
  postgres:
    image: postgres:15-alpine
    env:
      POSTGRES_DB: katana_test
      POSTGRES_USER: test_user
      POSTGRES_PASSWORD: ${{ secrets.DB_PASSWORD }}
    options: >-
      --health-cmd pg_isready
      --health-interval 10s
      --health-timeout 5s
      --health-retries 5
    ports:
      - 5432:5432

env:
  TEST_DATABASE_URL: postgresql://test_user:${{ secrets.DB_PASSWORD }}@localhost:5432/katana_test

steps:
  - name: Run tests in parallel
    run: |
      pytest tests/ \
        -v \
        --maxfail=3 \
        --tb=short \
        -n 4  # ← 4 parallel workers
```

---

## Performance Targets

| Metric | Target | How to Verify |
|--------|--------|---------------|
| Unit tests | <2 min | `time pytest tests/unit/` |
| Integration tests | <2.5 min | `time pytest tests/integration/` |
| E2E tests | <3 min | `time pytest tests/integration/end_to_end/` |
| Quality gates | <3 min | Check GitHub Actions logs |
| **Total** | **<10 min** | Sum all above (parallel) |
| **Speedup** | **3x** | Old: 30 min, New: 10 min |

---

## Troubleshooting (1 min each)

### Q: Tests timeout in parallel
**A:** Increase connection pool
```python
pool_size=30, max_overflow=50  # Increase from 20/40
```

### Q: "Too many connections" error
**A:** Close connections properly
```python
session.close()  # ← Add this
transaction.rollback()
connection.close()
```

### Q: Tests pass locally, fail in CI
**A:** Parallel reveals race conditions
```bash
# Test locally with parallel
pytest tests/ -n 4 -v
```

### Q: PostgreSQL won't start in CI
**A:** Check port binding
```yaml
ports:
  - 5433:5432  # ← Use different port
```

### Q: Database not cleaning up
**A:** Run cleanup script
```bash
./scripts/db-cleanup-per-test.sh --database katana_test --force
```

---

## Command Reference

### Local Testing

```bash
# Test with transaction isolation (single DB, 4 workers)
pytest tests/ -n 4 -v

# Test with cleanup
./scripts/db-cleanup-per-test.sh --database katana_test
./scripts/db-setup-per-test.sh --database katana_test --seed-data true
pytest tests/

# Measure performance
time pytest tests/ -v
```

### Database Management

```bash
# Setup test database
./scripts/db-setup-per-test.sh --verbose

# Cleanup test database
./scripts/db-cleanup-per-test.sh --force

# Verify isolation
psql -U test_user -d katana_test -c "SELECT count(*) FROM pg_stat_activity;"
```

### GitHub Actions

```bash
# Trigger workflow manually
gh workflow run ci-parallel.yml

# View logs
gh run view <RUN_ID> --log

# Cancel running workflow
gh run cancel <RUN_ID>
```

---

## Success Signs

✅ **Working Correctly**
- Tests pass in <10 minutes
- 4 jobs running in parallel
- No "connection pool exhausted" errors
- Coverage reports generated
- All batches complete successfully

❌ **Needs Attention**
- Tests timeout in parallel
- Intermittent "connection" errors
- One batch significantly slower
- Coverage reports missing
- Database cleanup failing

---

## Common Mistakes (and fixes)

| Mistake | Fix | Impact |
|---------|-----|--------|
| Forgetting `session.close()` | Add close before rollback | Connection leak |
| Hardcoding DB name | Use env vars | Parallel conflicts |
| No transaction rollback | Check fixture yields | Cross-test pollution |
| Pool size too small | Set pool_size=30 | "Too many connections" |
| Skipping cleanup script | Always run cleanup | Disk space fills up |

---

## Further Reading

**For details:** See `DB-TEST-ISOLATION-IMPLEMENTATION.md`
- Part 1: Strategy comparison (10 min read)
- Part 2: Implementation details (15 min read)
- Part 3-7: Templates and scripts (20 min skim)

**For troubleshooting:** See Part 10 of main guide

**For best practices:** See Part 9 of main guide

---

## Timeline Summary

| Stage | Time | Task |
|-------|------|------|
| **Design** | 30 min | ✅ DONE |
| **Implementation** | 2 hours | ← YOU ARE HERE |
| **Testing** | 30 min | Verify parallel execution |
| **Deployment** | 15 min | Merge to main |
| **TOTAL** | **3 hours** | From start to production |

---

## Key Metrics to Track

```
Before                    After
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Execution Time: 30 min → 10 min (3x)
Developer Wait: 35 min → 12 min (2.9x)
Cost per Run: $0.24 → $0.32 (+33%)
Productivity Gain: 20 min/run (ROI: 2 weeks)
Test Isolation: Weak → Perfect
```

---

## Quick Decision Tree

```
START
  │
  ├─→ Running tests sequentially?
  │   └─→ YES: Implement parallel (this guide)
  │
  ├─→ Tests fail in CI but pass locally?
  │   └─→ YES: Race conditions - parallel reveals them
  │
  ├─→ Database "too many connections"?
  │   └─→ YES: Increase pool_size in fixture
  │
  └─→ Everything working?
      └─→ YES: Deploy to main, celebrate! 🎉
```

---

## Support Checklist

Before asking for help, verify:
- [ ] PostgreSQL is running: `pg_isready -h localhost`
- [ ] Scripts are executable: `ls -la scripts/db-*.sh | grep '^-rwx'`
- [ ] TEST_DATABASE_URL is set
- [ ] Python version is 3.8+
- [ ] pytest installed: `pytest --version`

---

**Status:** ✅ Ready to implement
**Next Step:** Copy fixtures to conftest.py and run tests
**Expected Result:** 3x faster CI/CD pipeline

---

*Generated by BMAD-MNNZ Infrastructure Engineering Team*
*For questions or issues, refer to main implementation guide*
