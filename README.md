# nbcat

[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/tsvikas/nbcat"/workflows/CI/badge.svg
[actions-link]:             https://github.com/tsvikas/nbcat"/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/nbcat
[conda-link]:               https://github.com/conda-forge/nbcat-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/tsvikas/nbcat"/discussions
[pypi-link]:                https://pypi.org/project/nbcat/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/nbcat
[pypi-version]:             https://img.shields.io/pypi/v/nbcat
[rtd-badge]:                https://readthedocs.org/projects/nbcat/badge/?version=latest
[rtd-link]:                 https://nbcat.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->

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

- install git, python3.12, poetry, poethepoet.
- git clone this repo
- create a venv using `poetry env use python3.12; poetry install`
- enable pre-commit checks with `poetry run pre-commit install`
- use `poe check` to verify code quality

## Build

- install poetry-dynamic-versioning[plugin]
- use `poe version` to see the current version
- use `poe tag new_version_number` to add a git tag
- use `poetry build` to build
