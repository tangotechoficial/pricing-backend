

run-dev:
	docker-compose up --build web

run-staging:
	docker-compose -p pricing_staging -f docker-compose-staging.yml up --build web 


