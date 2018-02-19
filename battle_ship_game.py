import tkinter as tk
import time

from battle_ship.game import Game
from battle_ship.gui_helper import GuiHelper


class BattleShip:
    def __init__(self, **kwargs):
        self.placement_phase = True

        self.player1 = kwargs["player1"]
        self.player2 = kwargs["player2"]

        self.game = Game(self.player1, self.player2)

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

    def play(self):
        self.placement_phase = False
