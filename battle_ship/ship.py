from . import WINDOW_WIDTH, WINDOW_HEIGHT, SHIP_TYPES


class InvalidShipPositionException(Exception):
    def __init__(self, position):
        self.message = "invalid ship position({position.fore}, {position.aft})"


class Position:
    def __init__(self, **kwargs):
        self.is_vertical = kwargs['is_vertical']
        self.fore = kwargs['fore']
        self.aft = kwargs['aft']


class Ship:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.length = kwargs['length']

        self.position: Position = kwargs['position']

        self.is_placed = False
        self.is_alive = True

    def is_out_of_bounds(self, position):
        return                                                    \
            self.is_vertically_out_of_bounds(position) or \
            self.is_horizontally_out_of_bounds(position)

    def is_vertically_out_of_bounds(self, position):
        fore, aft = position.fore, position.aft

        return not (fore[0] or aft[0]) in range(0, WINDOW_HEIGHT)

    def is_horizontally_out_of_bounds(self, position):
        fore, aft = position.fore, position.aft

        return not (fore[1] or aft[1]) in range(0, WINDOW_WIDTH)

    def set_position(self, new_pos):
        if self.is_out_of_bounds(new_pos):
            raise InvalidShipPositionException(new_pos)

        self.position = new_pos
        self.is_placed = True
        self.set_tiles()

    def set_tiles(self):
        if self.position.is_vertical:
            self.tiles = [
                (self.position.aft[0], x) for x in
                range(min(self.position.aft[1], self.position.fore[1]),
                      max(self.position.aft[1], self.position.fore[1]) + 1)
            ]
        else:
            self.tiles = [
                (x, self.position.aft[1]) for x in
                range(min(self.position.aft[0], self.position.fore[0]),
                      max(self.position.aft[0], self.position.fore[0]) + 1)
            ]

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

        ship = Ship(
            type=k,
            length=v,
            position=dummy_pos)
        ships[k] = ship

    return ships
