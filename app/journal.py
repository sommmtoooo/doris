import os
from datetime import datetime
from pathlib import Path
import typer
from config import JOURNALS_DIR, load_config

def get_today_journal():
    """Get the path for today's journal entry."""
    today = datetime.today().strftime("%Y-%m-%d") + ".md"
    return JOURNALS_DIR / today

def open_journal():
    """Create or open today's journal entry."""
    config = load_config()
    editor = config["editor"]

    journal_path = get_today_journal()
    
    if not journal_path.exists():
        journal_path.touch()
        typer.echo(f"New journal entry created: {journal_path}")

    os.system(f"{editor} {journal_path}")

def list_journals():
    """List all journal entries."""
    if not JOURNALS_DIR.exists():
        typer.echo("No journal entries found.")
        return

    journals = sorted(JOURNALS_DIR.iterdir(), reverse=True)
    for journal in journals:
        typer.echo(journal.name)
