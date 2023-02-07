"""The datascrape data model."""

from typing import Any, TypedDict


def transform(untyped: dict[str, str],
              typed: dict[str, Any]) -> dict[str, Any]:
    """Convert a dictionary of strings to a dictionary of typed values."""
    fields = typed.__annotations__
    return {name: fields[name](value)
            for name, value in untyped.items()
            if name is not None}


player_fields = {
    "id": int,
    "del": int,
    "team_id": int,
    "Team Name": str,
    "LastName": str,
    "FirstName": str,
    "NickName": str,
    "UniformNumber": int,
    "DayOB": int,
    "MonthOB": int,
    "YearOB": int,
    "NationalityID": int,
    "Nation": str,
    "CityID": int,
    "City": str,
    "facial_type": int,
    "Height (cm)": int,
    "Weight (kg)": int,
    "Bats": int,
    "Throws": int,
    "Position": int,
    "ML Service": int,
    "40 man roster service": int,
    "pro years": int,
    "options used": int,

    "Contact vL": int,
    "Gap vL": int,
    "Power vL": int,
    "Eye vL": int,
    "Avoid K vL": int,
    "BABIP vL": int,

    "Contract Vr": int,
    "Gap Vr": int,
    "Power vR": int,
    "Eye vR": int,
    "Ks vR": int,
    "BABIP vR": int,

    "Contact Pot": int,
    "Gap Pot": int,
    "Power Pot": int,
    "Eye Pot": int,
    "Ks Pot": int,
    "BABIP Pot": int,

    "HBP": int,
    "GB Batter type": int,
    "FB Batter type": int,
    "speed": int,
    "steal": int,
    "running": int,
    "sac bunt": int,
    "bunt hit": int,

    "Move vL": int,
    "Control vL": int,
    "Movement vR": int,
    "Control vR": int,
    "Move Pot": int,
    "Control Pot": int,

    "HBP": int,
    "WP": int,
    "Balk": int,
    "Stamina": int,
    "Hold": int,
    "GB%": int,
    "Velocity": int,
    "ArmSlot": int,

    "Infield Range": int,
    "Infield Error": int,
    "Infield Arm": int,
    "DP": int,
    "CatcherAbil": int,
    "Catcher Arm": int,
    "OF Range": int,
    "OF Error": int,
    "OF Arm": int,

    "PExp": int,
    "CExp": int,
    "1bExp": int,
    "2bExp": int,
    "3bExp": int,
    "ssExp": int,
    "LFExp": int,
    "CFExp": int,
    "RFExp": int,

    "use expected": int,
    "expected level": int,
    "expected ab": int,
    "expected avg": float,
    "expected 2b": int,
    "expected 3b": int,
    "expected hr": int,
    "expected bb": int,
    "expected k": int,
    "expected hbp": int,

    "contract y1": int,
    "contract y2": int,
    "contract y3": int,
    "contract y4": int,
    "contract y5": int,
    "contract y6": int,
    "contract y7": int,
    "contract y8": int,
    "contract y9": int,
    "contract y10": int,
    "contract current year (0 = first year)": int,

    "extension y1": int,
    "extension y2": int,
    "extension y3": int,
    "extension y4": int,
    "extension y5": int,
    "extension y6": int,
    "extension y7": int,
    "extension y8": int,
    "extension y9": int,
    "extension y10": int,

    "greed": int,
    "loyalty": int,
    "play_for_winner": int,
    "work_ethic": int,
    "intelligence": int,
    "leader ability": int,

    "Stuff Overall": int,
    "Stuff R/L split": float,
    "Stuff Pot.": int,

    "Fastball (scale: 0-5)": int,
    "Slider": int,
    "Curveball": int,
    "Changeup": int,
    "Cutter": int,
    "Sinker": int,
    "Splitter": int,
    "Forkball": int,
    "Screwball": int,
    "Circlechange": int,
    "Knucklecurve": int,
    "Knuckleball": int,

    "Fastball Pot.(scale: 0-5)": int,
    "Slider Pot.": int,
    "Curveball Pot.": int,
    "Changeup Pot.": int,
    "Cutter Pot.": int,
    "Sinker Pot.": int,
    "Splitter Pot.": int,
    "Forkball Pot.": int,
    "Screwball Pot.": int,
    "Circlechange Pot.": int,
    "Knucklecurve Pot.": int,
    "Knuckleball Pot.": int,

    "Hitter 3B/2B ratio": float,
    "lahman_id": str,
    "bbref_id": str,
    "bbrefminors_id": str,
    "twitter_handle": str,
}

field_names = {
    "id": "id",
    "del": None,
    "team_id": "team_id",
    "Team Name": None,
    "LastName": "lastname",
    "FirstName": "firstname",
    "NickName": "nickname",
    "UniformNumber": "number",
    "DayOB": "birthDay",
    "MonthOB": "birthMonth",
    "YearOB": "birthYear",
    "NationalityID": None,
    "Nation": "birthCountry",
    "CityID": None,
    "City": "birthCity",
    "facial_type": None,
    "Height (cm)": "height",
    "Weight (kg)": "weight",
    "Bats": "bats",
    "Throws": "throws",
    "Position": "position",
    "ML Service": None,
    "40 man roster service": None,
    "pro years": None,
    "options used": None,

    "Contact vL": None,
    "Gap vL": "gapL",
    "Power vL": "powerL",
    "Eye vL": "eyeL",
    "Avoid K vL": "avoidkL",
    "BABIP vL": "babipL",

    "Contract Vr": None,
    "Gap Vr": "gapR",
    "Power vR": "powerR",
    "Eye vR": "eyeR",
    "Ks vR": "avoidkR",
    "BABIP vR": "babipR",

    "Contact Pot": None,
    "Gap Pot": "gapPot",
    "Power Pot": "powerPot",
    "Eye Pot": "eyePot",
    "Ks Pot": "avoidkPot",
    "BABIP Pot": "babipPot",

    "HBP": None,
    "GB Batter type": "gbType",
    "FB Batter type": "fbType",
    "speed": "speed",
    "steal": "steal",
    "running": "run",
    "sac bunt": "buntSac",
    "bunt hit": "buntHit",

    "Move vL": "movementL",
    "Control vL": "controlL",
    "Movement vR": "movementR",
    "Control vR": "controlR",
    "Move Pot": "movementPot",
    "Control Pot": "controlPot",

    "HBP": None,
    "WP": None,
    "Balk": None,
    "Stamina": "stamina",
    "Hold": "holdRunners",
    "GB%": "gbRate",
    "Velocity": "velocity",
    "ArmSlot": "armSlot",

    "Infield Range": "rangeIf",
    "Infield Error": "errorIf",
    "Infield Arm": "armIf",
    "DP": "doublePlay",
    "CatcherAbil": "abilityC",
    "Catcher Arm": "armC",
    "OF Range": "rangeOf",
    "OF Error": "errorOf",
    "OF Arm": "armOf",

    "PExp": "expP",
    "CExp": "expC",
    "1bExp": "exp1B",
    "2bExp": "exp2B",
    "3bExp": "exp3B",
    "ssExp": "expSS",
    "LFExp": "expLF",
    "CFExp": "expCF",
    "RFExp": "expRF",

    "use expected": None,
    "expected level": None,
    "expected ab": None,
    "expected avg": None,
    "expected 2b": None,
    "expected 3b": None,
    "expected hr": None,
    "expected bb": None,
    "expected k": None,
    "expected hbp": None,

    "contract y1": None,
    "contract y2": None,
    "contract y3": None,
    "contract y4": None,
    "contract y5": None,
    "contract y6": None,
    "contract y7": None,
    "contract y8": None,
    "contract y9": None,
    "contract y10": None,
    "contract current year (0 = first year)": None,

    "extension y1": None,
    "extension y2": None,
    "extension y3": None,
    "extension y4": None,
    "extension y5": None,
    "extension y6": None,
    "extension y7": None,
    "extension y8": None,
    "extension y9": None,
    "extension y10": None,

    "greed": None,
    "loyalty": None,
    "play_for_winner": None,
    "work_ethic": None,
    "intelligence": None,
    "leader ability": None,

    "Stuff Overall": None,
    "Stuff R/L split": "stuffSplit",
    "Stuff Pot.": None,

    "Fastball (scale: 0-5)": "fastball",
    "Slider": "slider",
    "Curveball": "curve",
    "Changeup": "change",
    "Cutter": "cutter",
    "Sinker": "sinker",
    "Splitter": "splitter",
    "Forkball": "fork",
    "Screwball": "screw",
    "Circlechange": "circle",
    "Knucklecurve": "kCurve",
    "Knuckleball": "knuckle",

    "Fastball Pot.(scale: 0-5)": "fastballPot",
    "Slider Pot.": "sliderPot",
    "Curveball Pot.": "curvePot",
    "Changeup Pot.": "changePot",
    "Cutter Pot.": "cutterPot",
    "Sinker Pot.": "sinkerPot",
    "Splitter Pot.": "splitterPot",
    "Forkball Pot.": "forkPot",
    "Screwball Pot.": "screwPot",
    "Circlechange Pot.": "circlePot",
    "Knucklecurve Pot.": "kCurvePot",
    "Knuckleball Pot.": "knucklePot",

    "Hitter 3B/2B ratio": None,
    "lahman_id": None,
    "bbref_id": None,
    "bbrefminors_id": None,
    "twitter_handle": None,
}

fields = {key: value
          for key, value in field_names.items()
          if value is not None}

INSERT_QUERY = """
INSERT OR IGNORE INTO players
    ( id
    , team_id
    , lastname
    , firstname
    , nickname
    , number
    , birthYear
    , birthMonth
    , birthDay
    , birthCountry
    , birthCity
    , height
    , weight
    , position
    , bats
    , throws
    , gbType
    , fbType
    , armSlot
    , babipL
    , babipR
    , babipPot
    , avoidkL
    , avoidkR
    , avoidkPot
    , powerL
    , powerR
    , powerPot
    , gapL
    , gapR
    , gapPot
    , eyeL
    , eyeR
    , eyePot
    , speed
    , run
    , steal
    , buntSac
    , buntHit
    , movementL
    , movementR
    , movementPot
    , controlL
    , controlR
    , controlPot
    , stamina
    , holdRunners
    , gbRate
    , velocity
    , rangeIf
    , rangeOf
    , errorIf
    , errorOf
    , armIf
    , armOf
    , armC
    , doublePlay
    , abilityC
    , expP
    , expC
    , exp1B
    , exp2B
    , exp3B
    , expSS
    , expLF
    , expCF
    , expRF
    , stuffSplit
    , fastball
    , fastballPot
    , slider
    , sliderPot
    , curve
    , curvePot
    , change
    , changePot
    , cutter
    , cutterPot
    , sinker
    , sinkerPot
    , splitter
    , splitterPot
    , fork
    , forkPot
    , screw
    , screwPot
    , circle
    , circlePot
    , kCurve
    , kCurvePot
    , knuckle
    , knucklePot
    )
VALUES
    ( :id
    , :team_id
    , :lastname
    , :firstname
    , :nickname
    , :number
    , :birthYear
    , :birthMonth
    , :birthDay
    , :birthCountry
    , :birthCity
    , :height
    , :weight
    , :position
    , :bats
    , :throws
    , :gbType
    , :fbType
    , :armSlot
    , :babipL
    , :babipR
    , :babipPot
    , :avoidkL
    , :avoidkR
    , :avoidkPot
    , :powerL
    , :powerR
    , :powerPot
    , :gapL
    , :gapR
    , :gapPot
    , :eyeL
    , :eyeR
    , :eyePot
    , :speed
    , :run
    , :steal
    , :buntSac
    , :buntHit
    , :movementL
    , :movementR
    , :movementPot
    , :controlL
    , :controlR
    , :controlPot
    , :stamina
    , :holdRunners
    , :gbRate
    , :velocity
    , :rangeIf
    , :rangeOf
    , :errorIf
    , :errorOf
    , :armIf
    , :armOf
    , :armC
    , :doublePlay
    , :abilityC
    , :expP
    , :expC
    , :exp1B
    , :exp2B
    , :exp3B
    , :expSS
    , :expLF
    , :expCF
    , :expRF
    , :stuffSplit
    , :fastball
    , :fastballPot
    , :slider
    , :sliderPot
    , :curve
    , :curvePot
    , :change
    , :changePot
    , :cutter
    , :cutterPot
    , :sinker
    , :sinkerPot
    , :splitter
    , :splitterPot
    , :fork
    , :forkPot
    , :screw
    , :screwPot
    , :circle
    , :circlePot
    , :kCurve
    , :kCurvePot
    , :knuckle
    , :knucklePot
    )
"""

positions = {
    1: "P",
    2: "C",
    3: "1B",
    4: "2B",
    5: "3B",
    6: "SS",
    7: "LF",
    8: "CF",
    9: "RF",
    10: "DH",
    11: "RP",   # these show up in the roster export, dunno why
    12: "SP",
    13: "CP",
}

handednesses = {
    1: "Right",
    2: "Left",
    3: "Switch",
}

hitting_types = {
    0: "Spray",
    1: "Normal",
    2: "Pull",
    3: "Extreme Pull",
}

arm_slots = {
    1: "Submarine",
    2: "Sidearm",
    3: "Normal",
    4: "Over the top",
}

velocities = {
    0: "80-82",
    1: "81-83",
    2: "82-84",
    3: "83-85",
    4: "84-86",
    5: "85-87",
    6: "86-88",
    7: "87-89",
    8: "88-90",
    9: "89-91",
    10: "90-92",
    11: "91-93",
    12: "92-94",
    13: "93-95",
    14: "94-96",
    15: "95-97",
    16: "96-98",
    17: "97-99",
    18: "98-100",
    19: "99-101",
    20: "100+",
}

Player = TypedDict("Player", player_fields)  # type: ignore
