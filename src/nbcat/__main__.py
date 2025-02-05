"""nbcat: display jupyter notebooks in the terminal.

use `python -m nbcat` to run the cli
"""

from .cli import app

if __name__ == "__main__":
    app(prog_name="nbcat")
