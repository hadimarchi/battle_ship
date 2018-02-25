from . import WINDOW_WIDTH, WINDOW_HEIGHT, SHIP_TYPES


class InvalidShipPositionException(Exception):
    def __init__(self, start, end):
        self.message = "invalid ship position({start}, {end})"


class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Position:
    def __init__(self, **kwargs):
        self.is_vertical: bool = kwargs['is_vertical']
        self.fore: Coordinate = kwargs['fore']
        self.aft: Coordinate = kwargs['aft']


class Ship:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.length = kwargs['length']

        aft = kwargs.get('aft', (0, 0))
        fore = kwargs.get('fore', (0, self.length))
        is_vertical = kwargs.get('is_vertical', True)

        self.position = Position(
            aft=aft,
            fore=fore,
            is_vertical=is_vertical
            )

        self.is_placed = False
        self.is_alive = True

    def is_out_of_bounds(self, start, end):
        return                                                    \
            self.is_vertically_out_of_bounds(start, end) or \
            self.is_horizontally_out_of_bounds(start, end)

    def is_vertically_out_of_bounds(self, start, end):
        return not (start[0] or end[0]) in range(0, WINDOW_HEIGHT)

    def is_horizontally_out_of_bounds(self, start, end):
        return not (start[1] or end[1]) in range(0, WINDOW_WIDTH)

    def set_position(self, start, end, is_vertical):
        if self.is_out_of_bounds(start, end):
            raise InvalidShipPositionException(start, end)

        self.position = Position(aft=start, fore=end, is_vertical=is_vertical)
        self.is_placed = True
        self.get_tiles(is_vertical)

    def get_tiles(self, is_vertical):
        if is_vertical:
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
        ship = Ship(type=k, length=v,
                    aft=(0, 0), fore=(k, 0))
        ships[k] = ship

    return ships
