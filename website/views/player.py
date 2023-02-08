"""The player view."""

from sqlite3 import Connection, Row
import flask
from website.app import app
from website.framework import access_db


def pitcher_notes(player: Row) -> list[str]:
    """Create a list of notes for a pitcher."""
    return []


def hitter_notes(player: Row) -> list[str]:
    """Create a list of notes for a hitter."""
    return []


def view_pitcher(player: Row) -> str:
    """View a pitcher."""
    PITCH_NAMES = {
        "fastball": "Fastball",
        "slider": "Slider",
        "curve": "Curveball",
        "change": "Changeup",
        "cutter": "Cutter",
        "sinker": "Sinker",
        "splitter": "Splitter",
        "fork": "Forkball",
        "screw": "Screwball",
        "circle": "Circle Change",
        "kCurve": "Knuckle Curve",
        "knuckle": "Knuckleball",
    }

    pitches = [
        (name, player[pitch])
        for pitch, name in PITCH_NAMES.items()
        if player[pitch] > 0
    ]
    pitches.sort(key=lambda pitch: pitch[1], reverse=True)

    notes = pitcher_notes(player)

    return flask.render_template(
        "pitcher.html.jinja",
        player=player,
        pitches=pitches,
        notes=notes,
    )


def view_hitter(player: Row) -> str:
    """View a batter."""
    POSITIONS = ("P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF")
    exp = {pos: player[f"exp{pos}"] for pos in POSITIONS}

    primaries = [pos for pos, value in exp.items() if value >= 200]
    secondaries = [pos for pos, value in exp.items() if value >= 150]
    tertiaries = [pos for pos, value in exp.items() if value >= 100]

    notes = hitter_notes(player)

    return flask.render_template(
        "hitter.html.jinja",
        player=player,
        positions={1: primaries, 2: secondaries, 3: tertiaries},
        notes=notes,
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
