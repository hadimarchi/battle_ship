import tkinter as tk
import time

from battle_ship.ship import Ship, get_init_ships
from battle_ship.player import Player
from battle_ship.player_gui_interface import PlayerGuiInterface
from battle_ship.game import Game
from battle_ship.gui_helper import GuiHelper


class BattleShip:
    def __init__(self):
        self.window = tk.Tk()
        self.player_1 = Player(side="America",
                               ships=get_init_ships())

        self.player_2 = Player(side="Russia",
                               ships=get_init_ships())
        self.player_gui_interface = PlayerGuiInterface(
                                    self.player_1,
                                    self.player_2,
                                    self.window)
        self.game = Game(self.player_1, self.player_2)
        self.gui = GuiHelper(self.window,
                             self.game,
                             self.player_gui_interface)

    def run(self):
        while True:
            self.window.update_idletasks()
            self.window.update()

    def test_run(self, seconds):
        start = time.clock()

        while time.clock()-start <= seconds:
            self.window.update_idletasks()
            self.window.update()
