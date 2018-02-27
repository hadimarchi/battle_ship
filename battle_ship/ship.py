from . import SHIPS
from .position import Position, InvalidPositionException


class Ship:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.length = kwargs['length']
        self.is_alive = kwargs.get('is_alive', True)
        self.position = kwargs['position']

        self.is_placed = False

    def to_dict(self):
        ship = {'type': self.type, 'length': self.length,
                'is_alive': self.is_alive, 'position': self.position.to_dict()}
        return ship

    @staticmethod
    def from_dict(input_dict):
        input_dict['position'] = Position.from_dict(input_dict['position'])

        return Ship(**input_dict)

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
    for ship_type in SHIPS:
        dummy_pos = Position(
            aft=(0, 0),
            fore=(ship_type["length"], 0),
            is_vertical=False
        )

        ships[ship_type["name"]] = Ship(
            type=ship_type["name"],
            length=ship_type["length"],
            position=dummy_pos
        )

    return ships
