import os
from datetime import datetime
from pathlib import Path
import typer
from .config import JOURNALS_DIR, load_config


def get_journal_path(date: str = None) -> Path:
    """Get the path for a journal entry on a specific date."""
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    return JOURNALS_DIR / f"{date}.md"


def get_today_journal():
    """Get the path for today's journal entry."""
    today = datetime.today().strftime("%Y-%m-%d") + ".md"
    return JOURNALS_DIR / today


def open_journal(date: str = None):
    """Open a specific journal entry, defaulting to today's date if not provided."""

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    config = load_config()
    editor = config["editor"]

    journal_path = get_journal_path(date)

    if not journal_path.exists():
        journal_path.touch()
        typer.echo(f"New journal entry created: {journal_path}")

    os.system(f"{editor} {journal_path}")


def get_journals():
    """List all journal entries."""
    if not JOURNALS_DIR.exists():
        typer.echo("No journal entries found.")
        return

    journals = sorted(JOURNALS_DIR.iterdir(), reverse=True)
    for journal in journals:
        typer.echo(journal.name)


def delete_journal(date: str):
    """Delete a specific journal entry by date."""

    journal_path = get_journal_path(date)

    if journal_path.exists():
        journal_path.unlink()
        typer.echo(f"Deleted journal entry for {date}.")
    else:
        typer.echo(f"No journal entry found for {date}.")
