PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python3 -m repetitor.manage migrate

.PHONY: migrations
migrations:
	poetry run python3 -m repetitor.manage makemigrations

.PHONY: run-dependencies
run-dependencies:
	test -f .env || touch .env
	docker compose -f docker-compose.dev.yaml down; \
	docker compose -f docker-compose.dev.yaml up --force-recreate db --force-recreate redis

.PHONY: stop-dependencies
stop-dependencies:
	docker compose -f docker-compose.dev.yaml down

.PHONY: runserver
runserver:
	poetry run python -m repetitor.manage runserver

.PHONY: shell
shell:
	poetry run python -m repetitor.manage shell_plus

.PHONY: superuser
superuser:
	poetry run python -m repetitor.manage createsuperuser

.PHONY: run-production
run-production:
	test -f .env || touch .env
	docker compose down; docker compose build; docker compose up -d --force-recreate
