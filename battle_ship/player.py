from . import WINDOW_WIDTH, WINDOW_HEIGHT
from battle_ship.ship import get_init_ships


class Player(object):
    def __init__(self, side="America", ships={}):
        self.side = side
        self.ships = ships
        self.buttons = []
        self.board = [[y for y in range(WINDOW_HEIGHT)]
                      for x in range(WINDOW_WIDTH)]

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
            if self.ships[k].length == length + 1 and not self.ships[k].is_placed:
                print("ship placed is {}".format(k))
                self.ships[k].set_position(
                    self.buttons[0], self.buttons[1], vertical)
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
