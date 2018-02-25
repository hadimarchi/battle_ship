
from battle_ship.player import get_player
from battle_ship.game import Game


def get_battle_ship_game():

    player_2 = get_player("Russia")
    player_1 = get_player("America")

    return Game(
        active=player_1,
        inactive=player_2
    )
