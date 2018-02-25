from battle_ship.ship import Ship
from battle_ship.player import Player


class Game:
    def __init__(self, active: Player=None, inactive: Player=None):
        self.active = active
        self.inactive = inactive

    def setup(self):
        pass

    def turn(self):
        pass
