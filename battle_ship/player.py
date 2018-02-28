from . import WINDOW_WIDTH, WINDOW_HEIGHT
from battle_ship.ship import get_init_ships, Ship
from battle_ship.position import Position
import json


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
        try:
            ships = {
                k: Ship.from_dict(v) for k, v in input_dict['ships'].items()
            }
        except:
            ships = {
                k: Ship.from_dict(v) for k, v in json.loads(input_dict['ships']).items()
            }

        print(input_dict['ships'])
        side = input_dict['player']

        return Player(side, ships)

    def set_ship_location_from_buttons(self):
        if self.buttons[0] == self.buttons[1]:
            return

        if not (self.buttons[0][0] in self.buttons[1]
                or self.buttons[0][1] in self.buttons[1]):
            print("diagonal")
            return

        length, vertical = ((abs(self.buttons[0][0] - self.buttons[1][0]),
                             False),
                            (abs(self.buttons[0][1] - self.buttons[1][1]),
                             True))[self.buttons[0][0] in self.buttons[1]]

        print("length is {}".format(length + 1))

        for k in self.ships.keys():
            if self.is_ship_length(k, length) and not self.is_ship_placed(k):
                print("ship placed is {}".format(k))

                self.ships[k].set_position(
                    Position(
                        fore=self.buttons[0],
                        aft=self.buttons[1],
                        is_vertical=vertical
                    )
                )

                return self.ships[k]

    def set_ship_location(self, ship_dict):
        keys = ['col', 'row', 'length', 'is_vertical']
        col, row, length, is_vertical = [ship_dict[k] for k in keys]

        position = Position(
            aft=[col, row],
            fore=(col, row + length) if is_vertical else (col + length, row),
            is_vertical=is_vertical
        )

        if not position.is_valid():
            raise Exception("position:{} {} {} was invalid".format(
                            position.aft, position.fore, position.is_vertical))

        ship_type = ship_dict['type']
        ship_dict = {
            'type': ship_type,
            'length': int(length),
            'position': position
        }

        self.ships[ship_type] = Ship(**ship_dict)

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
