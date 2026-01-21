install:
	uv sync

run:
	uv run gendiff -h

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

quick-reinstall: build package-reinstall