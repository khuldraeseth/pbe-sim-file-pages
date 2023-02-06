"""The entry point for the datascrape application."""

from csv import QUOTE_MINIMAL, Dialect, DictReader
import functools
from pathlib import Path
from sqlite3 import Connection, Row
from typing import Any, Callable
import click
from datascrape import config
from datascrape import model


class OotpDialect(Dialect):
    """A dialect for OOTP roster files."""

    delimiter = ","
    doublequote = True
    escapechar = None
    lineterminator = "\r\n"
    quotechar = '"'
    quoting = QUOTE_MINIMAL
    skipinitialspace = True
    strict = False


def access_db(fun: Callable[..., Any]) -> Callable[..., Any]:
    """Grant a function database access."""
    @functools.wraps(fun)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        db_filename: Path = config.DATABASE
        with Connection(db_filename) as conn:
            conn.row_factory = Row
            return fun(conn, *args, **kwargs)

    return wrapper


def cull_if_meaningless(line: str) -> str | None:
    """Make a line of a roster file meaningful, or transform it to None."""
    if not line.startswith("//"):
        return line

    if line.startswith("//id,"):
        return line.lstrip("/")

    return None


def make_csv(roster_file: Path) -> str:
    """Make CSV data from a roster file."""
    lines = roster_file.read_text().splitlines()
    culled_lines = (cull_if_meaningless(line) for line in lines)
    return "\n".join(line for line in culled_lines if line is not None)


@access_db
def add_from_csv(conn: Connection, csv: str) -> None:
    """Add data from a CSV file to the database."""
    reader = DictReader(csv.splitlines(), dialect=OotpDialect())
    for row in reader:
        row = model.transform(row, model.Player)  # type: ignore
        player = {
            model.fields[key]: value
            for key, value in row.items()
            if key in model.fields
        }
        player["position"] = model.positions[player["position"]]
        player["bats"] = model.handednesses[player["bats"]]
        player["throws"] = model.handednesses[player["throws"]]
        player["gbType"] = model.hitting_types[player["gbType"]]
        player["fbType"] = model.hitting_types[player["fbType"]]
        player["armSlot"] = model.arm_slots[player["armSlot"]]
        player["velocity"] = model.velocities[player["velocity"]]

        if player["id"] == 1700:
            player["firstname"] = "Robert');"
            player["lastname"] = "DROP TABLE players; --"

        conn.execute(model.INSERT_QUERY, player)

        if player["firstname"] is None or player["firstname"] == "":
            print(player["lastname"])
        else:
            print(f"{player['firstname']} {player['lastname']}")


@click.command()
@click.option(
    "-f", "--roster-file", "roster_files",
    type=click.Path(exists=True, dir_okay=False),
    multiple=True,
    default=[config.PBE_DATA, config.MILPBE_DATA],
    help="The roster files to process.")
def main(roster_files: list[Path]) -> None:
    """Run the datascrape application."""
    for file in roster_files:
        csv = make_csv(Path(file))
        add_from_csv(csv)


if __name__ == "__main__":
    main()
