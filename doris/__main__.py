import typer
import doris.config as config
from .journal import open_journal, get_journals
from .notes import create_note, get_notes
from .search import search
import os
import platform

app = typer.Typer()


# Initialization and configuration functions
@app.command()
def init():
    """Initialize Doris by setting up the necessary directories."""
    config.ensure_setup()
    typer.echo("Doris has been initialized!")


@app.command()
def set_editor(editor: str):
    """Set the preferred text editor for Doris."""
    user_config = config.load_config()
    user_config["editor"] = editor
    config.save_config(user_config)
    typer.echo(f"Editor set to: {editor}")


@app.command()
def edit_config():
    """Open the Doris configuration file in the preferred editor."""
    from .config import edit_config

    edit_config()


# Journal-related functions
@app.command()
def journal(date: str):
    """Create or open a journal entry for today or a specific date."""
    open_journal(date)


@app.command()
def list_journals():
    """List all journal entries."""
    get_journals()


@app.command()
def delete_journal(date: str):
    """Delete a specific journal entry by date (YYYY-MM-DD)."""
    from .journal import delete_journal

    delete_journal(date)


# Note-related functions
@app.command()
def note(title: str):
    """Create a quick note."""
    create_note(title)


@app.command()
def list_notes():
    """List all notes."""
    get_notes()


@app.command()
def delete_note(title: str):
    """Delete a specific note by title."""
    from .notes import delete_note

    delete_note(title)


@app.command()
def search_notes(keyword: str):
    """Search for a keyword in notes and journals."""
    search(keyword)


@app.command()
def open():
    """Open the Doris directory."""
    from .config import CONFIG_DIR, load_config

    config = load_config()
    editor = config["editor"]

    if editor.lower() == "nano":
        if platform.system() == "Darwin":
            os.system(f"open {CONFIG_DIR}")
        elif platform.system() == "Windows":
            os.system(f"explorer {CONFIG_DIR}")
        else:
            os.system(f"xdg-open {CONFIG_DIR}")
    else:
        os.system(f"{editor} {CONFIG_DIR}")


if __name__ == "__main__":
    app()
