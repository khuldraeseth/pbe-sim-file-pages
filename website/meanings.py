"""Meanings of various things in the context of the website."""

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


ATTRIBUTE_NAMES = {
    "control": "Control",
    "controlL": "Control vs LHB",
    "controlR": "Control vs RHB",
    "controlPot": "Control Potential",
    "movement": "Movement",
    "movementL": "Movement vs LHB",
    "movementR": "Movement vs RHB",
    "movementPot": "Movement Potential",
    "stamina": "Stamina",
    "holdRunners": "Hold Runners",
    "stuffSplit": "Stuff R/L Split",
    "babip": "BABIP",
    "babipL": "BABIP vs LHP",
    "babipR": "BABIP vs RHP",
    "babipPot": "BABIP Potential",
    "avoidK": "Avoid K's",
    "avoidKL": "Avoid K's vs LHP",
    "avoidKR": "Avoid K's vs RHP",
    "avoidKPot": "Avoid K's Potential",
    "gap": "Gap",
    "gapL": "Gap vs LHP",
    "gapR": "Gap vs RHP",
    "gapPot": "Gap Potential",
    "power": "Power",
    "powerL": "Power vs LHP",
    "powerR": "Power vs RHP",
    "powerPot": "Power Potential",
    "eye": "Eye/Patience",
    "eyeL": "Eye/Patience vs LHP",
    "eyeR": "Eye/Patience vs RHP",
    "eyePot": "Eye/Patience Potential",
    "bunt": "Bunting",
    "buntSac": "Sacrifice Bunt",
    "buntHit": "Bunt for Hit",
    "speed": "Speed",
    "run": "Baserunning",
    "steal": "Stealing",
    "range": "Range",
    "rangeIf": "Infield Range",
    "rangeOf": "Outfield Range",
    "arm": "Arm",
    "armIf": "Infield Arm",
    "armOf": "Outfield Arm",
    "armC": "Catcher Arm",
    "error": "Error",
    "errorIf": "Infield Error",
    "errorOf": "Outfield Error",
    "doublePlay": "Turn Double Play",
    "abilityC": "Catcher Ability",
}


HITTER_LRP_ATTRIBUTES = [
    "babip",
    "avoidK",
    "gap",
    "power",
    "eye",
]


PITCHER_LRP_ATTRIBUTES = [
    "control",
    "movement",
]


HITTER_LINKED_ATTRIBUTES = [
    ["speed", "run"],
    ["buntSac", "buntHit"],
    ["rangeIf", "rangeOf"],
    ["armIf", "armOf", "armC"],
    ["errorIf", "errorOf"],
]


PITCHER_LINKED_ATTRIBUTES = [
    [name, f"{name}Pot"] for name in PITCH_NAMES.keys()
]


HITTER_DOUBLED_ATTRIBUTES = [
    "babipL",
    "babipR",
    "babipPot",
    "avoidKL",
    "avoidKR",
    "avoidKPot",
    "gapL",
    "gapR",
    "gapPot",
    "powerL",
    "powerR",
    "powerPot",
    "eyeL",
    "eyeR",
    "eyePot",
    "speed",
    "run",
    "steal",
    "buntSac",
    "buntHit",
    "rangeIf",
    "rangeOf",
    "armIf",
    "armOf",
    "armC",
    "errorIf",
    "errorOf",
    "doublePlay",
    "abilityC",
]


PITCHER_DOUBLED_ATTRIBUTES = [
    "controlL",
    "controlR",
    "controlPot",
    "movementL",
    "movementR",
    "movementPot",
    "stamina",
    "holdRunners",
]
