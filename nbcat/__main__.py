"""Display a Jupyter notebook with syntax highlighting in the terminal."""

import re
from pathlib import Path
from typing import Annotated, Optional

import nbconvert
import nbformat
import pygments
import typer
from pygments import lexers
from pygments.formatters import terminal

from . import __version__

SUPPORTED_FORMATS = {
    # each entry is a tuple of the exporter class and the lexer name
    "md": (nbconvert.exporters.MarkdownExporter, "markdown"),
    "markdown": (nbconvert.exporters.MarkdownExporter, "markdown"),
    "rst": (nbconvert.exporters.RSTExporter, "rst"),
    "adoc": (nbconvert.exporters.ASCIIDocExporter, None),
    "asciidoc": (nbconvert.exporters.ASCIIDocExporter, None),
    "py": (nbconvert.exporters.PythonExporter, "python"),
    "python": (nbconvert.exporters.PythonExporter, "python"),
}

app = typer.Typer()


def version_callback(value: bool) -> None:  # noqa: FBT001, D103
    if value:
        print(f"nbcat {__version__}")  # noqa: T201
        raise typer.Exit()  # noqa: RSE102


@app.command()
def main(
    filename: Annotated[
        Path, typer.Argument(exists=True, help="The notebook file to display")
    ],
    output_format: Annotated[
        str,
        typer.Option(
            "--format",
            "-f",
            help="The format to convert the notebook to. Supported formats: "
            + ", ".join(SUPPORTED_FORMATS.keys()),
        ),
    ] = "markdown",
    remove_tags: Annotated[
        str,
        typer.Option(
            "--remove-tags",
            "-t",
            help="comma-separated list of HTML tags to remove from the output.",
        ),
    ] = "",
    force_color: Annotated[  # noqa: FBT002
        bool,
        typer.Option(
            "--force-color",
            "-R",
            help="Force syntax highlighting even when the output is not a terminal",
        ),
    ] = False,
    version: Annotated[  # noqa: ARG001
        Optional[bool],  # noqa: FA100
        typer.Option("--version", callback=version_callback, is_eager=True),
    ] = None,
) -> None:
    """Display a notebook with syntax highlighting in the terminal."""
    # set the exporter and laxer name based on the format
    try:
        exporter, lexer_name = SUPPORTED_FORMATS[output_format]
    except KeyError as err:
        typer.echo(f"Unsupported format: {output_format}")
        raise typer.Exit(code=11) from err

    # Convert the notebook to the specified format
    try:
        nb: nbformat.NotebookNode = nbformat.read(
            filename, as_version=nbformat.NO_CONVERT
        )  # type: ignore[no-untyped-call]
    except Exception as err:
        typer.echo(f"Error reading notebook: {err}")
        raise typer.Exit(code=12) from err
    content: str
    content, _resources = nbconvert.export(exporter, nb)  # type: ignore[no-untyped-call]

    # Optionally remove specified HTML tags
    for remove_tag in remove_tags.split(","):
        tag_pattern = rf"<{remove_tag}.*>.*</{remove_tag}>"
        content = re.sub(
            tag_pattern, f"<<{remove_tag} omitted>>", content, flags=re.DOTALL
        )

    # Display the text with syntax highlighting
    if lexer_name is None:
        typer.echo(content)
    else:
        lexer = lexers.get_lexer_by_name(lexer_name)
        formatter = terminal.TerminalFormatter()
        highlighted = pygments.highlight(content, lexer, formatter)
        typer.echo(highlighted, color=force_color or None)


if __name__ == "__main__":
    app()
