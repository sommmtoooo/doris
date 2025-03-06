import typer
from pathlib import Path
from config import JOURNALS_DIR, NOTES_DIR

def search_files(keyword: str, directory: Path):
    """Search for a keyword in all files within a directory."""
    results = []
    
    if not directory.exists():
        return results
    
    for file in directory.iterdir():
        if file.is_file():
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
                if keyword.lower() in content.lower():
                    results.append(file.name)
    
    return results

def search(keyword: str):
    """Search both journals and notes for a given keyword."""
    journal_results = search_files(keyword, JOURNALS_DIR)
    note_results = search_files(keyword, NOTES_DIR)

    if not journal_results and not note_results:
        typer.echo("No matches found.")
        return

    if journal_results:
        typer.echo("📔 Journals:")
        for entry in journal_results:
            typer.echo(f"  - {entry}")

    if note_results:
        typer.echo("\n📝 Notes:")
        for note in note_results:
            typer.echo(f"  - {note}")
