"""The homepage view."""

import flask
from website.app import app


@app.route("/")
def view_homepage() -> str:
    """View the homepage."""
    return flask.render_template("homepage.html.jinja")
