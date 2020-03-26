.PHONY: all help start stop build bash clean logs
.DEFAULT_GOAL := help


ifeq ($(ALT_COMPOSE),)
        CONFIG:=-f docker-compose.yml
else
        CONFIG:=-f $(ALT_COMPOSE)
endif

COMPOSE=docker-compose $(CONFIG)

# help: Makefile targets description
# #
# target: help -> Displays this help message.
help:
	@egrep "^#" [Mm]akefile | cut -d' ' -f3,4,5- | sed 's/^Usage:/\tUsage:/'

# target: build-dev -> build web app container for development
build-dev:
	$(COMPOSE) up --no-start --build web

# target: build-staging -> build web app staging container
build-staging:
	docker-compose -p pricing_staging -f docker-compose-staging.yml up --no-start --build web 

# target: start -> start containers
start: 
	$(COMPOSE) start web db

# target: stop -> Stop running containers
stop: 
	$(COMPOSE) stop

# target: restart -> restart containers
restart: stop start

# target: shell -> Give a shell into container
shell:
	$(COMPOSE) exec web /bin/bash

# target: logs -> Use to display containers logs 
logs:
	$(COMPOSE) logs --follow

# target: migrate -> Run application migrations
migrate:
	$(COMPOSE) run web python manage.py migrate



