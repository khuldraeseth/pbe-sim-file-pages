"""website framework."""

import functools
from pathlib import Path
from sqlite3 import Connection, Row
from typing import Any, Callable

from website.app import app


Handler = Callable[..., Any]


def access_db(handler: Handler) -> Handler:
    """Grant a handler database access."""
    @functools.wraps(handler)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        db_filename: Path = app.config["DATABASE"]
        with Connection(db_filename) as conn:
            conn.row_factory = Row
            return handler(conn, *args, **kwargs)

    return wrapper
