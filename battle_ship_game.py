import tkinter as tk

from battle_ship.ship import get_init_ships
from battle_ship.player import Player
from battle_ship.game import Game


class BattleShip:
    def __init__(self):
        self.window = tk.Tk()
        self.player_1 = Player(side="America",
                               ships=get_init_ships())

        self.player_2 = Player(side="Russia",
                               ships=get_init_ships())
        self.game = Game(self.player_1, self.player_2)
