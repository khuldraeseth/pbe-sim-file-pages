"""The player view."""

from sqlite3 import Connection, Row
from typing import Any
import flask
from website.meanings import (
    ATTRIBUTE_NAMES,
    HITTER_DOUBLED_ATTRIBUTES,
    HITTER_LINKED_ATTRIBUTES,
    HITTER_LRP_ATTRIBUTES,
    PITCH_NAMES,
    PITCHER_DOUBLED_ATTRIBUTES,
    PITCHER_LINKED_ATTRIBUTES,
    PITCHER_LRP_ATTRIBUTES
)
from website.app import app
from website.framework import access_db


def attribute_notes(player: Row, attribute: str) -> list[str]:
    """Create a list of notes for an attribute."""
    vsL = player[f"{attribute}L"]
    vsR = player[f"{attribute}R"]
    pot = player[f"{attribute}Pot"]

    if pot != min(vsL, vsR):
        name = ATTRIBUTE_NAMES[attribute]
        return [
            f"{name} potential is {pot}, expected {min(vsL, vsR)}"
        ]

    return []


def linked_attribute_notes(player: Row, attributes: list[str]) -> list[str]:
    """Create a list of notes for a set of linked attributes."""
    values = {player[attr] for attr in attributes}
    if len(values) > 1:
        return [f"One or more of {attributes} does not match the others"]

    return []


def odd(n: int) -> bool:
    """Tell whether a number is odd."""
    return n & 1 != 0


def doubled_attribute_notes(player: Row, attribute: str) -> list[str]:
    """Create a list of notes for a doubled attribute."""
    if odd(player[attribute]):
        return [f"{ATTRIBUTE_NAMES[attribute]} is odd, expected even"]

    return []


def pitcher_notes(player: Row, pitches: list[tuple[str, Any]]) -> list[str]:
    """Create a list of notes for a pitcher."""
    notes: list[str] = []

    stuffSplit = player["stuffSplit"]
    if stuffSplit != 1.0:
        notes.append(f"Stuff R/L split is {stuffSplit:.3f}, expected 1.000")

    numPitches = len(pitches)
    if numPitches == 1:
        notes.append(f"Found {numPitches} pitch, expected at least 3")
    if 1 < numPitches < 3:
        notes.append(f"Found {numPitches} pitches, expected at least 3")
    if 5 < numPitches:
        notes.append(f"Found {numPitches} pitches, expected no more than 5")

    for attribute in PITCHER_LRP_ATTRIBUTES:
        notes.extend(attribute_notes(player, attribute))

    for attributes in PITCHER_LINKED_ATTRIBUTES:
        notes.extend(linked_attribute_notes(player, attributes))

    for attribute in PITCHER_DOUBLED_ATTRIBUTES:
        notes.extend(doubled_attribute_notes(player, attribute))

    return notes


def hitter_notes(player: Row) -> list[str]:
    """Create a list of notes for a hitter."""
    notes: list[str] = []

    for attribute in HITTER_LRP_ATTRIBUTES:
        notes.extend(attribute_notes(player, attribute))

    for attributes in HITTER_LINKED_ATTRIBUTES:
        notes.extend(linked_attribute_notes(player, attributes))

    for attribute in HITTER_DOUBLED_ATTRIBUTES:
        notes.extend(doubled_attribute_notes(player, attribute))

    gb_type = player["gbType"]
    fb_type = player["fbType"]
    if gb_type != fb_type:
        if gb_type != "Extreme Pull" or fb_type != "Pull":
            notes.append(
                f"GB type {gb_type} does not match FB type {fb_type}")

    return notes


def view_pitcher(player: Row) -> str:
    """View a pitcher."""
    pitches = [
        (name, player[pitch])
        for pitch, name in PITCH_NAMES.items()
        if player[pitch] > 0
    ]
    pitches.sort(key=lambda pitch: pitch[1], reverse=True)

    notes = pitcher_notes(player, pitches)

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
        case "P" | "SP" | "RP" | "CP" | "CF":
            return view_pitcher(player)
        case "C" | "1B" | "2B" | "3B" | "SS" | "LF" | "CF" | "RF" | "DH":
            return view_hitter(player)
        case _:
            flask.abort(500, f"Unknown position {player['position']}.")
