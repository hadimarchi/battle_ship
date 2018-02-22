from . import WINDOW_WIDTH, WINDOW_HEIGHT


class Player(object):
    def __init__(self, side="America", ships={}):
        self.side = side
        self.ships = ships
        self.buttons = []

    def set_ship_location(self):
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

        print("length is {}".format(length+1))
        for k in self.ships.keys():
            if self.ships[k].length == length + 1 and not self.ships[k].is_placed:
                print("ship placed is {}".format(k))
                self.ships[k].set_position(self.buttons[0], self.buttons[1], vertical)
                return self.ships[k]

    def ship_location(self, ship):
        return self.ships[ship].position
