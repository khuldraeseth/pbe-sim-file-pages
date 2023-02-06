"""The team view."""


from sqlite3 import Connection
import flask
from website.app import app
from website.framework import access_db


@app.route("/teams/<string:abbreviation>/")
@access_db
def view_team(conn: Connection, abbreviation: str) -> str:
    """View a team."""
    team = conn.execute(
        "SELECT id, location, name FROM teams"
        " WHERE abbreviation = ?",
        (abbreviation,),
    ).fetchone()

    if team is None:
        flask.abort(404, f"Team {abbreviation} not found.")

    team_id = team["id"]
    location = team["location"]
    name = team["name"]
    team_name = f"{location} {name}"

    players = conn.execute(
        "SELECT * FROM players"
        " WHERE team_id = ?",
        (team_id,),
    ).fetchall()

    return flask.render_template(
        "team.html.jinja",
        name=team_name,
        players=players
    )
