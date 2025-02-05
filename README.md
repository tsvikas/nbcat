# nbcat

<!-- prettier-ignore-start -->
[![Tests][tests-badge]][tests-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]


[tests-badge]:              https://github.com/tsvikas/nbcat/actions/workflows/tests.yml/badge.svg
[tests-link]:               https://github.com/tsvikas/nbcat/actions/workflows/tests.yml
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/nbcat
[conda-link]:               https://github.com/conda-forge/nbcat-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/tsvikas/nbcat/discussions
[pypi-link]:                https://pypi.org/project/nbcat/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/nbcat
[pypi-version]:             https://img.shields.io/pypi/v/nbcat
[rtd-badge]:                https://readthedocs.org/projects/nbcat/badge/?version=latest
[rtd-link]:                 https://nbcat.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->
<!-- SPHINX-START -->

display your notebooks, in the terminal ![Demo](assets/DEMO.gif)

## Installation

use pipx to install:

```bash
pipx install git+https://github.com/tsvikas/nbcat.git
```

## Usage

```bash
nbcat FILENAME -R | less -R
```

use `-f FORMAT` to specify the output format, default is `markdown`

## Development

- install [git][install-git], [uv][install-uv].
- git clone this repo
- run `uv run just prepare`

[install-git]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[install-uv]: https://docs.astral.sh/uv/getting-started/installation/

## Code formatting

- use `uv run black .` to format code
- use
  `git ls-files -z -- '*.md' '*.rst' '*.tex' '*.py' | xargs -0 uv run blacken-docs`
  to format docs

## Code quality

- use `uv run ruff check .` to verify code quality
- use `uv run mypy` to verify check typing
- use `uv run pytest` to run tests

## Build

- run formatting, linting, and tests.
- use `uv run dunamai from git` to see the current version
- use `git tag -a vX.Y.Z -m "version vX.Y.Z" -e` to add a git tag
- use `uv build` to build
- push the tag with `git push origin tag vX.Y.Z`
