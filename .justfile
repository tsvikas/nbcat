default:
  @just --list

init:
  # git init & initial commit
  git init
  git add --all
  git commit -m "initial commit" -q

  # install venv
  uv python pin python3.9
  uv sync
  git add uv.lock .python-version
  git commit -m "chore: uv sync" -q

  # pre-commit update
  uv run pre-commit autoupdate -j "$(nproc)"
  git add .pre-commit-config.yaml
  git commit -m "chore: pre-commit update" --allow-empty -q

  # pre-commit install
  uv run pre-commit install

  @just test

prepare:
  uv sync
  uv run pre-commit install

test:
  uv run pre-commit run --all-files
  uv run pytest
