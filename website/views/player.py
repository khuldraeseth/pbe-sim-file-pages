"""The player view."""

from sqlite3 import Connection
import flask
from website.app import app
from website.framework import access_db


@app.route("/players/<int:player_id>/")
@access_db
def view_player(conn: Connection, player_id: int) -> str:
    """View a player."""
    player = conn.execute(
        "SELECT * FROM players WHERE id = ?",
        (player_id,),
    ).fetchone()

    if player is None:
        flask.abort(404, f"Player {player_id} not found.")

    match player["position"]:
        case "P" | "SP" | "RP" | "CP":
            return flask.render_template("pitcher.html.jinja", player=player)
        case "C" | "1B" | "2B" | "3B" | "SS" | "LF" | "CF" | "RF" | "DH":
            return flask.render_template("hitter.html.jinja", player=player)
        case _:
            flask.abort(500, f"Unknown position {player['position']}.")
