"""website configuration."""

from pathlib import Path


APPLICATION_ROOT = "/"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE = PROJECT_ROOT/"var"/"players.sqlite3"
