SHELL := /usr/bin/env bash

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show the help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_.-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: lint
lint: ## Run Python linting.
	poetry run flake8 kira_setup

.PHONY: type-check
type-check: ## Run static type checks.
	poetry run mypy kira_setup

.PHONY: package
package: ## Validate package metadata and dependencies.
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: lint type-check package ## Run all local quality checks.
