

run-dev: export DJANGO_PORT = 8000
run-dev: export DB_PORT = 5432
run-dev:
	docker-compose up --build web

run-staging: export DJANGO_PORT = 8001
run-staging: export DB_PORT = 5433
run-staging:
	docker-compose -p pricing_staging -f docker-compose-staging.yml up --build web 


