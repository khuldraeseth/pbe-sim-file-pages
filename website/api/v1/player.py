"""The player API endpoint."""

from sqlite3 import Connection
import flask
from website.app import app
from website.framework import access_db


@app.route("/api/v1/players/<int:player_id>/")
@access_db
def get_player(conn: Connection, player_id: int) -> flask.Response:
    """View a player."""
    player = conn.execute(
        "SELECT * FROM players WHERE id = ?",
        (player_id,),
    ).fetchone()

    if player is None:
        flask.abort(404, f"Player {player_id} not found.")

    return flask.jsonify({key: player[key] for key in player.keys()})
