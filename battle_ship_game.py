import tkinter as tk
import time

from battle_ship.game import Game
from battle_ship.gui_helper import GuiHelper


class BattleShip:
    def __init__(self, **kwargs):
        self.placement_phase = True

        self.active_player = kwargs["active_player"]
        self.inactive_player = kwargs["inactive_player"]

        self.game = Game(self.active_player, self.inactive_player)

        self.window = tk.Tk()
        self.gui = GuiHelper(self.window, self.game)

    def run(self):
        while True:
            self.window.update_idletasks()
            self.window.update()

    def test_run(self, seconds):
        start = time.clock()

        while time.clock() - start <= seconds:
            self.window.update_idletasks()
            self.window.update()

    def swap_active_players(self):
        self.active_player, self.inactive_player = \
            self.inactive_player, self.active_player

    def play(self):
        self.placement_phase = False
