from . import WINDOW_WIDTH, WINDOW_HEIGHT

from battle_ship.ship import Ship
from battle_ship.position import Position


class Player(object):
    def __init__(self, side="", ships={}):
        self.side = side
        self.ships = ships
        self.buttons = []
        self.board = [
            [y for y in range(WINDOW_HEIGHT)]
            for x in range(WINDOW_WIDTH)
        ]

    def to_dict(self):
        player = {
            "player": self.side,
            "ships": {k: v.to_dict() for k, v in self.ships.items()}
        }

        return player

    @staticmethod
    def from_dict(input_dict):
        ships = {
            k: Ship.from_dict(v) for k, v in input_dict['ships'].items()
        }

        side = input_dict['player']

        return Player(side, ships)

    def set_ship_location(self, ship_dict):
        position = self.get_position_from_dict(ship_dict)

        if not position.is_valid():
            raise Exception("position:{} {} {} was invalid".format(
                            position.aft, position.fore, position.is_vertical))

        ship_type = ship_dict['type']
        ship_dict = {
            'type': ship_type,
            'length': ship_dict['length'],
            'position': position
        }

        self.ships[ship_type] = Ship(**ship_dict)

    def get_position_from_dict(self, ship_dict):
        keys = ['col', 'row', 'length', 'is_vertical']
        col, row, length, is_vertical = [ship_dict[k] for k in keys]

        return Position(
            aft=(col, row + length - 1) if is_vertical else (col + length - 1, row),
            fore=[col, row],
            is_vertical=is_vertical
        )

    def receive_shot(self, col, row):
        for ship_name, ship in self.ships.items():
            if ship.check_shot(col, row):
                return True, ship

        return False, None

    def ship_location(self, ship):
        return self.ships[ship].position

    def has_live_ships(self):
        return len(self.ships.size())

    def check_ship_health(self, ship):
        return len(self.ships[ship].tiles)


def get_player(side):
    return Player(
        side=side,
        ships={}
    )
