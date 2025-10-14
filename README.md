

## Setup

conda create -n ruff_mypy python=3.12
conda activate ruff_mypy
pip install poetry

poetry init

poetry add --group dev ruff mypy


### Make setup of these tools in pyproject.toml:
#### (Make sure to change the python version in both)

[tool.ruff]
# Linting rules and formatting
line-length = 100
target-version = "py312"
fix = true
extend-select = ["I", "UP", "B", "C90"]  # import sorting, pyupgrade, bugbear, complexity
exclude = ["build", "dist", ".venv"]

[tool.mypy]
python_version = "3.12"
strict = true
# Flip these later to become stricter:
ignore_missing_imports = true       # don’t error on untyped libs
disallow_untyped_defs = false       # allow untyped function defs
disallow_incomplete_defs = false    # allow partially typed defs
warn_return_any = false             # don’t complain about returning Any
warn_unused_ignores = false         # don’t warn about unused # type: ignore
check_untyped_defs = false          # Skips type checking for untyped functions
no_implicit_optional = false        # Allows implicit `Optional[...]` for args with default `None`
warn_unreachable = false           # Disables unreachable code warnings



### Makefile
(set bash alias m for make)
(Just make Makefile in your project and add:)

.PHONY: lint format typecheck check-all

lint:
	poetry run ruff check . --fix

format:
	poetry run ruff format .

typecheck:
	poetry run mypy .

check-all: lint format typecheck




## More just informative:


### Commands:

poetry run ruff check .
poetry run ruff format .    # just formats consistent spacing, indentation, line wrapping
poetry run mypy .

poetry run ruff check . --fix


### If you use VS Code:

Install “Ruff” and “Mypy Type Checker” extensions.

Disable flake8 or pylint to avoid duplicate diagnostics.

Ruff auto-detects pyproject.toml settings.


### Disable mypy in code:

´´´
# my_module.py
# mypy: disallow_untyped_defs=False
'''











### Poetry alias scripts (if not using make):

[tool.poetry.scripts]
lint = "ruff check . --fix"
format = "ruff format ."
typecheck = "mypy ."

Just run:
(set bash alias pp="poetry run")
poetry run lint
poetry run typecheck


