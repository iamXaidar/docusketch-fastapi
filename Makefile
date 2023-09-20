up:
	docker compose -f docker-compose-local.yaml up -d
down:
	docker compose -f docker-compose-local.yaml down
init_db:
	cd ./source && poetry run alembic revision --autogenerate -m "Initial" && poetry run alembic upgrade heads
import:
	cd ./source && poetry run python import.py
startapp:
	cd ./source && poetry run uvicorn main:app --reload
create_dotenv:
	cd ./source && cat config/.env.template > config/.env
