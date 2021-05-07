all: build

service = transactions-api

ifdef UID
override UID = 1000
endif

build: ## 👷 Build app
	@echo "👷 Building app"
	@docker-compose build --no-cache $(service)

up: ## 🛫 Run app
	@echo "🛫 Serving app"
	docker-compose up $(service)

down: ## 🔌 Shut down app deleting containers
	@echo "🔌 Disconnecting"
	@docker-compose down

kill: ## 🗡️ Kill containers
	@echo "🗡️ Killing"
	@docker-compose kill

restart: ## ️️↩️ Restart a containers
	@echo "↩️ Restarting"
	@docker-compose restart $(service)

clean:	## 🧹 Delete containers and their volumes
	@echo "🧹 Cleaning"
	@docker-compose down -v --remove-orphans

connect: ## 🔞 Connect to a container
	@echo "🔞 Connecting to container"
	@docker-compose run $(service) /bin/bash

logs: ## 📋 show container logs
	@echo "📋 Showing logs"
	@docker-compose logs -f --tail 100 $(service)

update-deps: ## 📥 Update requirements files with last packages versions
	@echo "📥 Updating dependencies"
	@docker-compose run --rm --entrypoint sh transactions-api -c "pip-compile /code/requirements/dev.in && pip-compile /code/requirements/prod.in"

test: ## 🏃 Run tests
	@echo "🏃‍ Running tests"
	@docker-compose run --rm --entrypoint sh transactions-api -c "pytest $(args)"

lint: ## 🔦 Lint code
	@echo "🔦 Linting code"
	@docker-compose run --rm --entrypoint sh transactions-api -c "black /code/ -t py38 --line-length 80 --skip-string-normalization"

shell: ## 📗 Django shell plus console
	@echo "📗 Shell plus console"
	@docker-compose run --rm --entrypoint python transactions-api manage.py shell_plus

dbshell: ## 💾 Database shell console
	@echo "💾 Database shell console"
	@docker-compose run --rm --entrypoint python transactions-api manage.py dbshell

showmigrations: ## 💾 Show migrations state
	@echo "💾 Show migrations"
	@docker-compose run --rm --entrypoint python transactions-api manage.py showmigrations $(args)

makemigrations: ## 💾 New migrations generation
	@echo "💾 Make migrations"
	@docker-compose run --rm --user=${UID} --entrypoint python transactions-api manage.py makemigrations $(args)

migrate: ## 🚛 Migration execution
	@echo "🚛 Migrate"
	@docker-compose run --rm --entrypoint sh transactions-api -c "python manage.py migrate $(args)"

createsuperuser: ## 👤 Create an admin user
	@echo "👤 Create superuser"
	@docker-compose run --rm --entrypoint python transactions-api manage.py createsuperuser

show-urls: ## 🕵️ Show app urls
	@echo "🕵 Show urls"
	@docker-compose run --rm --entrypoint python transactions-api manage.py show_urls

collectstatic: ## 🗿️ Collect statics
	@echo "🗿 Collect statics"
	@docker-compose run --rm --user=${UID} --entrypoint python transactions-api manage.py collectstatic

load-transactions-csv: 	## Load transactions CSV
	@echo "Load transactions CSV"
	@docker-compose run --rm --entrypoint sh transactions-api -c "python manage.py load_transactions_csv $(args)"

help: ## 📖 Show make targets
	@echo "📖 Help"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf " \033[36m%-20s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)
