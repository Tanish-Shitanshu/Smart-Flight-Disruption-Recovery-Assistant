# ── Flight Disruption Recovery Assistant – Developer Makefile ─────────────────
.PHONY: install install-dev run test lint format type-check clean help

## Install production dependencies
install:
	pip install -r requirements.txt

## Install development dependencies
install-dev:
	pip install -r requirements-dev.txt

## Launch the Streamlit app
run:
	streamlit run app.py

## Run the test suite
test:
	pytest tests/ -v --tb=short

## Run tests with coverage report
test-cov:
	pytest tests/ -v --cov=. --cov-report=term-missing

## Lint with ruff
lint:
	ruff check .

## Auto-format with black
format:
	black .

## Static type checking with mypy
type-check:
	mypy . --ignore-missing-imports

## Remove generated artefacts
clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	rm -f flights.db

## Show this help
help:
	@grep -E '^## ' Makefile | sed 's/^## /  /'
