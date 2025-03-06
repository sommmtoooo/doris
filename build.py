import os
import shutil
import sys
import subprocess
from pathlib import Path

BUILD_DIR = Path("dist")
EXECUTABLE_NAME = "doris"

def clean():
    """Remove previous build files."""
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    typer.echo("Cleaned old build files.")

def build():
    """Build Doris as an executable using PyInstaller."""
    typer.echo("Building Doris...")
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--name", EXECUTABLE_NAME,
        "app/doris.py"
    ], check=True)
    typer.echo(f"Build complete! Executable available at: {BUILD_DIR / EXECUTABLE_NAME}")

if __name__ == "__main__":
    import typer
    app = typer.Typer()
    app.command()(clean)
    app.command()(build)
    app()
