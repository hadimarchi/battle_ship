from .player_helper import PlayerHelper


class Player(object):
    def __init__(self, side="America", ships={}):
        self.side = side
        self.ships = ships
        self.buttons = []
        self.helper = PlayerHelper(self)

    def set_ship_location(self):
        if self.helper.position_is_bad():
            return

        length, vertical = self.helper.get_length_and_alignment()

        print("length is {}".format(length+1))
        for k in self.ships.keys():
            if self.is_ship_length(k, length) and not self.is_ship_placed(k):
                print("ship placed is {}".format(k))
                self.ships[k].set_position(self.buttons[0],
                                           self.buttons[1],
                                           vertical)
                return self.ships[k]

    def is_ship_placed(self, ship):
        return self.ships[ship].is_placed

    def is_ship_length(self, ship, length):
        return self.ships[ship].length == length + 1

    def ship_location(self, ship):
        return self.ships[ship].position
