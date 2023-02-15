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
    #!/usr/bin/env bash
    set -euxo pipefail
    args=(
        dist
        build
    )
    rm -rf "${args[@]}"
