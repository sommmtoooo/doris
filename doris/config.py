import os
import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".doris"
CONFIG_FILE = CONFIG_DIR / "config.json"
NOTES_DIR = CONFIG_DIR / "notes"
JOURNALS_DIR = CONFIG_DIR / "journals"

DEFAULT_CONFIG = {"editor": os.getenv("EDITOR", "vim")}


def ensure_setup():
    """Ensure Doris directories and config file exist."""
    CONFIG_DIR.mkdir(exist_ok=True)
    NOTES_DIR.mkdir(exist_ok=True)
    JOURNALS_DIR.mkdir(exist_ok=True)

    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)


def load_config():
    """Load the user configuration."""
    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(config):
    """Save the user configuration."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
