from . import SHIP_TYPES
from .position import Position, InvalidPositionException


class Ship:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.length = kwargs['length']

        self.position: Position = kwargs['position']

        self.is_placed = False
        self.is_alive = True

    def set_position(self, new_pos):
        if new_pos.is_out_of_bounds():
            raise InvalidPositionException(new_pos)

        self.position = new_pos
        self.is_placed = True
        self.tiles = self.position.get_tiles()

    def check_shot(self, col, row):
        for tile in self.tiles:
            if tile == (col, row):
                return self.handle_hit()

        return False

    def handle_hit(self, col, row):
        self.tiles.remove((col, row))

        if not self.tiles:
            self.is_alive = False

        return True


def get_init_ships():
    ships = {}
    for k, v in SHIP_TYPES.items():
        dummy_pos = Position(
            aft=(0, 0),
            fore=(k, 0),
            is_vertical=True
        )

        ships[k] = Ship(
            type=k,
            length=v,
            position=dummy_pos
        )

    return ships
