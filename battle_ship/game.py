from battle_ship.ship import Ship
from battle_ship.player import get_player, Player


class Game:
    def __init__(self, active: Player=None, inactive: Player=None):
        self.active = active
        self.inactive = inactive

    def setup(self):
        pass

    def turn(self):
        pass


def get_battle_ship_game():

    player_2 = get_player("Russia")
    player_1 = get_player("America")

    return Game(
        active=player_1,
        inactive=player_2
    )
