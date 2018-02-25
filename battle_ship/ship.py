from . import WINDOW_WIDTH, WINDOW_HEIGHT, SHIP_TYPES


class InvalidShipPositionException(Exception):
    def __init__(self, position):
        self.message = "invalid ship position({position.fore}, {position.aft})"


class Position:
    def __init__(self, **kwargs):
        self.is_vertical = kwargs['is_vertical']
        self.fore = kwargs['fore']
        self.aft = kwargs['aft']

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


class Ship:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.length = kwargs['length']

        self.position: Position = kwargs['position']

        self.is_placed = False
        self.is_alive = True

    def set_position(self, new_pos):
        if new_pos.is_out_of_bounds():
            raise InvalidShipPositionException(new_pos)

        self.position = new_pos
        self.is_placed = True
        self.set_tiles()

    def set_tiles(self):
        self.tiles = self.position.get_tiles()

    def check_shot(self, col, row):
        for tile in self.tiles:
            if tile == (col, row):
                return self.handle_hit()

        return False

    def handle_hit(self, col, row):
        self.tiles.remove((col, row))

        if not self.tiles:
            self.is_alive = False

        return True


def get_init_ships():
    ships = {}
    for k, v in SHIP_TYPES.items():
        dummy_pos = Position(
            aft=(0, 0),
            fore=(k, 0),
            is_vertical=True
        )

        ships[k] = Ship(
            type=k,
            length=v,
            position=dummy_pos
        )

    return ships
