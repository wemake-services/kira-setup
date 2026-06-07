set shell := ["bash", "-eu", "-o", "pipefail", "-c"]
set dotenv-load := false

# List all available recipes
_default:
    @just --list --unsorted

# Run Python linting
[group('dev')]
lint:
    poetry run flake8 kira_setup

# Run static type checks
[group('dev')]
type-check:
    poetry run mypy kira_setup

# Validate package metadata and dependencies
[group('dev')]
package:
    poetry check
    poetry run pip check
    poetry run safety check --full-report

# Run all local quality checks
[group('dev')]
test: lint type-check package
