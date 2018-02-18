import tkinter as tk
import time

from battle_ship.ship import Ship, get_init_ships
from battle_ship.player import Player
from battle_ship.game import Game
from battle_ship.gui_helper import GuiHelper


class BattleShip:
    def __init__(self):
        self.america = Player(side="America", ships=get_init_ships())
        self.russia = Player(side="Russia", ships=get_init_ships())
        self.game = Game(self.america, self.russia)
        self.window = tk.Tk()
        self.gui = GuiHelper(self.window, self.game)

    def run(self):
        while True:
            self.window.update_idletasks()
            self.window.update()

    def test_run(self, seconds):
        start = time.clock()

        while time.clock()-start <= seconds:
            self.window.update_idletasks()
            self.window.update()
