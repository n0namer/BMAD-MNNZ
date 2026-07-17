.PHONY: help install install-dev lint format-check format type-check test coverage ci clean

help:
	@echo "BMAD Development Commands"
	@echo ""
	@echo "Installation:"
	@echo "  make install          - Install dependencies with Poetry"
	@echo "  make install-dev      - Install dependencies + dev tools"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint             - Run ruff linter"
	@echo "  make format-check     - Check code formatting with black"
	@echo "  make format           - Auto-format code with black"
	@echo "  make type-check       - Run mypy type checking"
	@echo ""
	@echo "Testing:"
	@echo "  make test             - Run pytest tests"
	@echo "  make coverage         - Run tests with coverage report (HTML)"
	@echo ""
	@echo "CI/CD:"
	@echo "  make ci               - Run all checks locally (lint, format-check, type-check, test)"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean            - Remove build artifacts and caches"

install:
	poetry install --no-root

install-dev: install
	poetry install

lint:
	poetry run ruff check src/

format-check:
	poetry run black --check src/

format:
	poetry run black src/

type-check:
	poetry run mypy src/bmad

test:
	poetry run pytest src/tests/ -v

coverage:
	poetry run pytest src/tests/ -v --cov=src/bmad --cov-report=html --cov-report=term-missing
	@echo "Coverage report generated in coverage_html/index.html"

ci: lint format-check type-check test
	@echo "All CI checks passed!"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
	find . -type d -name .coverage -exec rm -rf {} +
	find . -type d -name coverage_html -exec rm -rf {} +
	find . -type d -name dist -exec rm -rf {} +
	find . -type d -name build -exec rm -rf {} +
	find . -type d -name *.egg-info -exec rm -rf {} +
	rm -f .coverage
