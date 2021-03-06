from battle_ship.ship import Ship
from battle_ship.player import get_player, Player


class Game:
    def __init__(
            self,
            name=None,
            active=None,
            inactive=None
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

    @staticmethod
    def from_dict(input_dict):
        active_player = Player.from_dict(input_dict['active'])
        inactive_player = Player.from_dict(input_dict['inactive'])

        return Game(
            name=input_dict['name'],
            active=active_player,
            inactive=inactive_player
        )

    def fire_shot(self, shot):
        return self.inactive.receive_shot(*shot)

    def place_ship(self, ship_dict):
        self.active.set_ship_location(ship_dict)

    def swap_players(self):
        self.active, self.inactive = self.inactive, self.active

    def is_player(self, player_name):
        return player_name == self.active.side or \
            player_name == self.inactive.side

    def is_active_player(self, player_name):
        return player_name == self.active.side


def get_battle_ship_game(name, active, inactive):

    player_2 = get_player(active)
    player_1 = get_player(inactive)

    return Game(
        name=name,
        active=player_1,
        inactive=player_2
    )
