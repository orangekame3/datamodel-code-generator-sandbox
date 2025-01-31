SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help

.PHONY: lint generate-oas

lint: ## Lint openapi.yaml
	@docker run --rm -v $(PWD):/spec redocly/cli lint openapi.yaml

generate-oas: ## Generate openapi.yaml
	@docker pull redocly/cli
	@docker run --rm -v $(PWD):/spec redocly/cli bundle /spec/root.yaml -o /spec/openapi.yaml
	@$(MAKE) lint
