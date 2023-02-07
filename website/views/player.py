"""The player view."""

from sqlite3 import Connection, Row
import flask
from website.app import app
from website.framework import access_db


def view_pitcher(player: Row) -> str:
    """View a pitcher."""
    return flask.render_template("pitcher.html.jinja", player=player)


def view_hitter(player: Row) -> str:
    """View a batter."""
    positions = ("P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF")
    exp = {pos: player[f"exp{pos}"] for pos in positions}

    primaries = [pos for pos, value in exp.items() if value >= 200]
    secondaries = [pos for pos, value in exp.items() if value >= 150]
    tertiaries = [pos for pos, value in exp.items() if value >= 100]
    return flask.render_template(
        "hitter.html.jinja",
        player=player,
        positions={1: primaries, 2: secondaries, 3: tertiaries}
    )


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
            return view_pitcher(player)
        case "C" | "1B" | "2B" | "3B" | "SS" | "LF" | "CF" | "RF" | "DH":
            return view_hitter(player)
        case _:
            flask.abort(500, f"Unknown position {player['position']}.")
