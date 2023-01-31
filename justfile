default: init install-dev

init:
	python -m pip install --upgrade pip wheel setuptools build

install:
	python -m pip install --upgrade .

install-dev:
	python -m pip install --upgrade --editable .[dev,tests,docs]

lint:
	python -m isort src/
	python -m black src/

pylint:
	python -m pylint src/

test:
	python -m pytest

build-dist:
	python -m pip install --upgrade build
	python -m build

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.mypy_cache' -exec rm -rf {} +
	rm -rf .tox
	rm -f coverage.xml
	rm -f coverage.json
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .coverage.*
	find . -name '.pytest_cache' -exec rm -rf {} +
	rm -rf dist
	rm -rf build
