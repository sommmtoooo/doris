import os
import typer
from .config import NOTES_DIR, load_config


def create_note(title: str):
    """Create a quick note."""
    config = load_config()
    editor = config["editor"]

    note_path = NOTES_DIR / f"{title.replace(' ', '_')}.md"

    if not note_path.exists():
        note_path.touch()
        typer.echo(f"New note created: {note_path}")

    os.system(f"{editor} {note_path}")


def get_notes():
    """List all notes."""
    if not NOTES_DIR.exists():
        typer.echo("No notes found.")
        return

    notes = sorted(NOTES_DIR.iterdir(), reverse=True)
    for note in notes:
        typer.echo(note.name)


def delete_note(title: str):
    """Delete a specific note by title."""
    filename = os.path.join(NOTES_DIR, f"{title}.md")

    if os.path.exists(filename):
        os.remove(filename)
        typer.echo(f"Deleted note: {title}")
    else:
        typer.echo(f"No note found with title '{title}'.")
