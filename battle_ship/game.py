from battle_ship.ship import Ship
from battle_ship.player import get_player, Player


class Game:
    def __init__(
            self,
            name: str=None,
            active: Player=None,
            inactive: Player=None
    ):
        self.name = name
        self.active = active
        self.inactive = inactive

    def to_dict(self):
        return {
            "name": self.name,
            "active": self.active.to_dict(),
            "inactive": self.inactive.to_dict()
        }

    def setup(self):
        pass

    def turn(self):
        pass


def get_battle_ship_game(name, active, inactive):

    player_2 = get_player(active)
    player_1 = get_player(inactive)

    return Game(
        name=name,
        active=player_1,
        inactive=player_2
    )
