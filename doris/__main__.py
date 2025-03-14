import typer
import doris.config as config
from .journal import open_journal, get_journals
from .notes import create_note, get_notes
from .search import search

app = typer.Typer()


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
def journal():
    """Create or open today's journal entry."""
    open_journal()


@app.command()
def note(title: str):
    """Create a quick note."""
    create_note(title)


@app.command()
def list_journals():
    """List all journal entries."""
    get_journals()


@app.command()
def delete_journal(date: str):
    """Delete a specific journal entry by date (YYYY-MM-DD)."""
    delete_journal(date)


@app.command()
def list_notes():
    """List all notes."""
    get_notes()


@app.command()
def search_notes(keyword: str):
    """Search for a keyword in notes and journals."""
    search(keyword)


if __name__ == "__main__":
    app()
