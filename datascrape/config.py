"""datascrape configuration."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE = PROJECT_ROOT/"var"/"players.sqlite3"

DATA_DIR = PROJECT_ROOT/"data"
PBE_DATA = DATA_DIR/"pbe_rosters.txt"
MILPBE_DATA = DATA_DIR/"milpbe_rosters.txt"
