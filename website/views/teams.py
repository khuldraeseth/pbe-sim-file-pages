"""The teams view."""

from sqlite3 import Connection
import flask
from website.app import app
from website.framework import access_db


@app.route("/teams/")
@access_db
def view_teams(conn: Connection) -> str:
    """View the list of teams."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()
    return flask.render_template("teams.html.jinja", teams=teams)
