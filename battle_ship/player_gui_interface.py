import tkinter as tk
import tkinter.ttk as ttk
from . import WINDOW_WIDTH, WINDOW_HEIGHT
from .player import Player
from .gui_helper import GuiHelper


class PlayerGuiInterface:
    def __init__(self, player_1, player_2, window):
        self.window = window
        self.player_1 = player_1
        self.player_2 = player_2

    def get_boards(self):
        self.get_board_for_player(self.player_1)
        self.get_board_for_player(self.player_2)

    def get_board_for_player(self, player):
        player.board = tk.Frame(
                       self.window,
                       width=WINDOW_WIDTH,
                       height=WINDOW_HEIGHT
        )
        player.spaces = [[0 for x in range(WINDOW_WIDTH)]
                         for y in range(WINDOW_HEIGHT)]

    def make_boards(self):
        for x in range(WINDOW_WIDTH):
            for y in range(WINDOW_HEIGHT):
                self.make_board_space(self.player_1, x, y)
                self.make_board_space(self.player_2, x, y)

    def make_board_space(self, player, col, row):
        callback = (lambda: self.place_callback(player, col, row))
        space = tk.Button(player.board,
                          text=' ',
                          command=callback)
        space.grid(column=col, row=row)
        player.spaces[col][row] = space

    def place_callback(self, player, col, row):
        player.buttons.append((col, row))
        if (len(player.buttons)) == 2:
            ship = player.set_ship_location()
            if ship:
                for tile in ship.tiles:
                    player.spaces[tile[0]][tile[1]]["text"] = player.side[0]

            player.buttons = []
