SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help

.PHONY: generate-schema run lint

generate-schema: ## Generate user schema
	@cd oas && $(MAKE) generate-oas
	@$(MAKE) generate \
	INPUT=./oas/openapi.yaml \
	OUTPUT=app/schemas
	@$(MAKE) fmt

generate:
	@uv run datamodel-codegen \
	--use-schema-description \
	--target-python-version 3.12 \
	--field-constraints \
	--use-annotated \
	--use-field-description \
	--input ${INPUT} \
	--input-file-type openapi \
	--collapse-root-models \
	--enum-field-as-literal one \
	--use-union-operator \
	--use-subclass-enum \
	--output-model-type pydantic_v2.BaseModel \
	--disable-timestamp \
	--use-standard-collections \
	--strict-nullable \
	--use-default \
	--output ${OUTPUT}


run: ## Start the User API
	@uv run fastapi dev


lint: ## Run user linters
	@uv run mypy -p src
	@uv run ruff check src

fmt: ## Format the code
	@uv run ruff format src
