
from . import WINDOW_WIDTH, WINDOW_HEIGHT


class InvalidPositionException(Exception):
    def __init__(self, position):
        self.message = "invalid ship position({position.fore}, {position.aft})"


class Position:
    def __init__(self, **kwargs):
        self.is_vertical = kwargs['is_vertical']
        self.fore = kwargs['fore']
        self.aft = kwargs['aft']

    def to_dict(self):
        position = {'fore': self.fore,
                    'aft': self.aft,
                    'is_vertical': self.is_vertical}
        return position

    @staticmethod
    def from_dict(input_dict):
        return Position(**input_dict)

    def get_tiles(self):
        if self.is_vertical:
            tiles = [
                (self.aft[0], x) for x in
                range(min(self.aft[1], self.fore[1]),
                      max(self.aft[1], self.fore[1]) + 1)
            ]
        else:
            tiles = [
                (x, self.aft[1]) for x in
                range(min(self.aft[0], self.fore[0]),
                      max(self.aft[0], self.fore[0]) + 1)
            ]

        return tiles

    def is_out_of_bounds(self):
        return                                      \
            self.is_vertically_out_of_bounds() or   \
            self.is_horizontally_out_of_bounds()

    def is_vertically_out_of_bounds(self):
        return not (self.fore[0] or self.aft[0]) in range(0, WINDOW_HEIGHT)

    def is_horizontally_out_of_bounds(self):
        return not (self.fore[1] or self.aft[1]) in range(0, WINDOW_WIDTH)
