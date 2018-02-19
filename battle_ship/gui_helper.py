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
        self.american_board = tk.Frame(
            self.window,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT
        )

        self.american_spaces = [[0 for x in range(WINDOW_WIDTH)]
                                for y in range(WINDOW_HEIGHT)]

        self.boundary_board = tk.Frame(
            self.window,
            width=WINDOW_WIDTH,
            height=2
        )

        self.boundary_spaces = [[0 for x in range(WINDOW_WIDTH)]
                                for y in range(2)]

        self.russian_board = tk.Frame(
            self.window,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT
        )

        self.russian_spaces = [[0 for x in range(WINDOW_WIDTH)]
                               for y in range(WINDOW_HEIGHT)]

        self.boards = {
            "america": {
                "spaces": self.american_spaces,
                "board": self.american_board
            },
            "russian": {
                "spaces": self.russian_spaces,
                "board": self.russian_board
            }
        }

        self.boundary = [self.boundary_board, self.boundary_spaces]

    def make_boards(self):
        for x in range(WINDOW_WIDTH):
            for y in range(2):
                self.make_boundary(x, y)
            for z in range(WINDOW_HEIGHT):
                self.make_boards_space(x, z)

        self.american_board.pack()
        self.boundary_board.pack()
        self.russian_board.pack()

    def make_boundary(self, x, y):
        space = tk.Button(
            self.boundary[0],
            text="*"
        )
        space.grid(row=y, column=x)
        self.boundary[1][y][x] = space

    def make_boards_space(self, col, row):
        # [[self.american_board, self.american_spaces, "american"],
        # [self.russian_board, self.russian_spaces, "russian"]

        for side, player in self.boards.items():
            callback = self.make_place_callback(row, col, side)
            space = tk.Button(
                player["board"],
                text=' ',
                command=callback
            )

            space.grid(row=row, column=col)
            player["spaces"][col][row] = space

    def make_place_callback(self, row, col, player):
        game_player = self.game.player_1
        board_spaces = self.american_spaces

        if player == "russian":
            game_player = self.game.player_2
            board_spaces = self.russian_spaces

        return lambda: self.place_callback(
            board_spaces,
            game_player,
            player,
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
