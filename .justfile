default:
  @just --list

init:
  git init
  @just update
  @just prepare
  @just test

update:
  uv sync --upgrade
  uv run pre-commit autoupdate -j "$(nproc)"

prepare:
  uv run pre-commit install

test:
  uv run pre-commit run --all-files
  uv run pytest
