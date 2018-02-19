# __init__.py
# Authors: Hal DiMarchi, William Horn
# battleship helper functions

from collections import namedtuple

Space = namedtuple("row", "col")

WINDOW_HEIGHT = 10
WINDOW_WIDTH = 10
CARRIER_LENGTH = 5
BATTLESHIP_LENGTH = 4
SUBMARINE_LENGTH = 3
DESTROYER_LENGTH = 3
PATROL_BOAT_LENGTH = 2
SHIP_TYPES = {
    "carrier": CARRIER_LENGTH,
    "battleship": BATTLESHIP_LENGTH,
    "submarine": SUBMARINE_LENGTH,
    "destroyer": DESTROYER_LENGTH,
    "patrol boat": PATROL_BOAT_LENGTH
}
