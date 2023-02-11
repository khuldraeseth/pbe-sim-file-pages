# pyright: reportUnusedImport=false

"""website package initializer."""

from website.app import app     # noqa: F401
from website import api         # noqa: F401
from website import meanings    # noqa: F401
from website import views       # noqa: F401
