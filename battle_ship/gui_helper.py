import tkinter as tk
import tkinter.ttk as ttk
from . import WINDOW_WIDTH


class GuiHelper:
    def __init__(self, window, game, player_interface):
        self.window = window
        self.game = game
        self.player_interface = player_interface

        self.get_boards()
        self.make_boards()
        self.pack_boards()

    def get_boards(self):
        self.player_interface.get_boards()
        self.get_boundary()

    def make_boards(self):
        self.player_interface.make_boards()
        self.make_boundary()

    def pack_boards(self):
        self.player_interface.player_1.board.pack()
        self.boundary_board.pack()
        self.player_interface.player_2.board.pack()

    def get_boundary(self):
        self.boundary_board = tk.Frame(
            self.window,
            width=WINDOW_WIDTH,
            height=2
        )

        self.boundary_spaces = [[0 for y in range(2)]
                                for x in range(WINDOW_WIDTH)]
        self.boundary = [self.boundary_board, self.boundary_spaces]

    def make_boundary(self):
        for x in range(WINDOW_WIDTH):
            for y in range(2):
                space = tk.Button(
                                self.boundary[0],
                                text="*"
                            )
                space.grid(column=x, row=y)
                self.insert_boundary_space(col=x, row=y, space=space)

    def insert_boundary_space(self, col, row, space):
        self.boundary_spaces[col][row] = space
