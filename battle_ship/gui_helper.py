import tkinter as tk
from . import WINDOW_WIDTH, WINDOW_HEIGHT


class GuiHelper:
    def __init__(self, window, game):
        self.placement_phase = True

        self.window = window
        self.game = game
        self.get_boards()
        self.make_boards()

    def get_boards(self):
        self.game.active_player.make_board(self.window)

        self.boundary_board, self.boundary_spaces = self.get_boundary(2)

        self.game.inactive_player.make_board(self.window)

    def get_boundary(self, num_rows):
        board = self.get_boundary_board(num_rows)
        spaces = self.get_boundary_spaces(num_rows)

        return [board, spaces]

    def get_boundary_board(self, num_rows):
        return tk.Frame(
            self.window,
            width=WINDOW_WIDTH,
            height=num_rows
        )

    def get_boundary_spaces(self, num_boundary_rows):
        row = [0 for x in range(WINDOW_WIDTH)]

        return [row for y in range(num_boundary_rows)]

    def make_boards(self):
        for x in range(WINDOW_WIDTH):
            for y in range(2):
                self.make_boundary(x, y)
            for z in range(WINDOW_HEIGHT):
                self.make_boards_space(x, z)

        self.game.active_player.board.pack()
        self.boundary_board.pack()
        self.game.inactive_playe.board.pack()

    def make_boundary(self, x, y):
        space = tk.Button(
            self.boundary[0],
            text="*"
        )

        space.grid(row=y, column=x)
        self.boundary_space[y][x] = space

    def make_boards_space(self, player, col, row):
        callback = self.make_place_callback(row, col, player)

        player.add_button(row, col, callback)

    def make_place_callback(self, row, col, player):
        return lambda: self.place_callback(
            player.spaces,
            player,
            player.side,
            col,
            row
        )

    def place_callback(self, board_spaces, game_player, player, col, row):
        print("x is {}".format(col))
        print("y is {}".format(row))

        game_player.buttons.append((col, row))

        if len(game_player.buttons) == 2:
            placement = game_player.set_ship_location(game_player.buttons[0],
                                                      game_player.buttons[1])
            if placement[0]:
                board_spaces[col][row]["text"] = player[0]

                x, y = game_player.buttons[0][0], game_player.buttons[0][1]

                board_spaces[x][y]["text"] = player[0]

                if placement[1]:
                    print("vertical")

                    for i in range(min(game_player.buttons[0][1], row),
                                   max(game_player.buttons[0][1], row)):
                        board_spaces[col][i]["text"] = player[0]
                else:
                    for i in range(min(game_player.buttons[0][0], col),
                                   max(game_player.buttons[0][0], col)):
                        board_spaces[i][row]["text"] = player[0]

            game_player.buttons = []
