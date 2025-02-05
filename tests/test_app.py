from pathlib import Path

from typer.testing import CliRunner

from nbcat import __version__
from nbcat.cli import SUPPORTED_FORMATS, app

runner = CliRunner()


def test_app(datadir: Path) -> None:
    filename = datadir / "notebook.ipynb"
    for fmt in SUPPORTED_FORMATS:
        result = runner.invoke(
            app, [filename.as_posix(), "-f", fmt], catch_exceptions=False
        )
        assert result.exit_code == 0
        assert "success = partial" in result.stdout


def test_app_version() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_app_errors(datadir: Path) -> None:
    filename = datadir / "notebook.ipynb"
    result = runner.invoke(app, ["MISSING_FILENAME"])
    assert result.exit_code == 2
    result = runner.invoke(app, [filename.as_posix(), "-f", "MISSING_FORMAT"])
    assert result.exit_code == 11
