define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

docker_start_db:
	docker-compose -f docker-compose.yml up -d

docker_stop_db:
	docker-compose -f docker-compose.yml stop

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

install-docs:
	pip install -r requirements-doc.txt

run:
	cd app; python main.py

black:
	black --check --diff --verbose app

flake:
	flake8 app

clean-test:
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

test-all: downgrade-test migration-test
	export APP_SETTINGS=test; py.test -vvv app/tests

integration-test: downgrade-test migration-test
	py.test -m"IT" -vvv app/tests

unit-test:
	py.test -m "not IT" -vvv app/tests

coverage: downgrade-test migration-test
	export APP_SETTINGS=test; coverage run --source app -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

migration:
	alembic upgrade head

migration-test:
	export DB_NAME=atendimento-agendamento-test-db;  alembic upgrade head

downgrade:
	alembic downgrade base

downgrade-test:
	export DB_NAME=atendimento-agendamento-test-db; alembic downgrade base

generate_docs:
	rm -f docs/app.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ app
	sphinx-build -b html docs html
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

create-local-api-topic:
	awslocal sns create-topic --name local-sns-atendimento-agendamento --region us-east-1

coverage-reports:
	coverage run --timid --source app -m pytest -m 'not IT'
	coverage report -m
	coverage xml