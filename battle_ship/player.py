from . import WINDOW_WIDTH, WINDOW_HEIGHT
from battle_ship.ship import get_init_ships
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
        player = {"player": self.side,
                  "ships": {k: v.to_dict() for k, v in self.ships.items()}}
        return player

    @staticmethod
    def from_dict(input_dict):
        ships = input_dict['ships']
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

    def make_shot(self):
        col = input(" enter a column between 1 and 10 ")
        row = input(" enter a row between 1 and 10 ")

        return (col, row)

    def receive_shot(self, col, row):
        for ship in self.ships:
            if ship.check_shot(col, row):
                if not ship.is_alive:
                    del ship
            return True
        return False

    def ship_location(self, ship):
        return self.ships[ship].position

    def has_live_ships(self):
        return len(self.ships.size())

    def check_ship_health(self, ship):
        return len(self.ships[ship].tiles)


def get_player(side):
    return Player(
        side=side,
        ships=get_init_ships()
    )
