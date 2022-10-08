include .env
export

migrate:
	cd migrator && poetry run alembic upgrade head

downgrade:
	cd migrator && poetry run alembic downgrade -1

revision:
	cd migrator && poetry run alembic revision --autogenerate

prepare:
	poetry install

shell:
	poetry shell 

db:
	docker compose up -d postgresql 

run:
	docker compose up -d postgresql 

down:
	docker compose down

logs:
	docker compose logs

open_db:
	psql -h ${POSTGRES_HOST} -U ${POSTGRES_USERNAME} -d ${POSTGRES_DATABASE}

