
import tkinter as tk
from . import WINDOW_WIDTH, WINDOW_HEIGHT


class Player(object):
    def __init__(self, side="America", ships={}):
        self.side = side
        self.ships = ships
        self.buttons = []

        self.spaces = None
        self.board = None

    def set_ship_location(self, start, end):
        if start == end:
            print("same")
            return (False, False)

        if not (start[0] in end or start[1] in end):
            print("diagonal")
            return (False, False)

        length = abs(start[0] - end[0])
        vertical = False

        if start[0] in end:
            length = abs(start[1] - end[1])
            vertical = True

        length = max(abs(start[0] - end[0]), abs(start[1] - end[1]))
        print("length is {}".format(length))

        for k in self.ships.keys():
            if self.ships[k].length == length + 1 and not self.ships[k].is_placed:
                print("ship placed is {}".format(k))
                self.ships[k].set_position(start, end)
                return (True, vertical)

        return (False, False)

    def make_board(self, window):
        self.board = tk.Frame(
            window,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT
        )

        self.spaces = [[0 for x in range(WINDOW_WIDTH)]
                       for y in range(WINDOW_HEIGHT)]

    def add_button(self, row, col, callback):
        space = tk.Button(
            self.board,
            text=' ',
            command=callback
        )

        space.grid(row=row, column=col)
        self.spaces[col][row] = space

    def ship_location(self, ship):
        return self.ships[ship].position
