import importlib

import nbcat


def test_version() -> None:
    assert importlib.metadata.version("nbcat") == nbcat.__version__
