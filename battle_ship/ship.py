from . import WINDOW_WIDTH, WINDOW_HEIGHT, SHIP_TYPES


class InvalidShipPositionException(Exception):
    def __init__(self, start, end):
        self.message = "invalid ship position({start}, {end})"


class Ship:
    def __init__(self, **kwargs):
        self.type = kwargs['type']
        self.length = kwargs['length']
        self.aft = kwargs.get('aft', (0, 0))
        self.fore = kwargs.get('fore', (0, self.length))
        self.position = (self.aft, self.fore)
        self.is_placed = False

    def is_out_of_bounds(self, start, end):
        if not (start[0] or end[0]) in range(0, WINDOW_HEIGHT):
            return True
        if not (start[1] or end[1]) in range(0, WINDOW_WIDTH):
            return True
        return False

    def set_position(self, start, end, vertical):
        if self.is_out_of_bounds(start, end):
            raise InvalidShipPositionException(start, end)

        self.aft = start
        self.fore = end
        self.vertical = vertical
        self.is_placed = True
        self.get_tiles()

    def get_tiles(self):
        if self.vertical:
            self.tiles = [(self.aft[0], x)
                          for x in range(min(self.aft[1], self.fore[1]),
                                         max(self.aft[1], self.fore[1])+1)]
        else:
            self.tiles = [(x, self.aft[1])
                          for x in range(min(self.aft[0], self.fore[0]),
                                         max(self.aft[0], self.fore[0])+1)]


def get_init_ships():
    ships = {}
    for k, v in SHIP_TYPES.items():
        ship = Ship(type=k, length=v,
                    aft=(0, 0), fore=(k, 0))
        ships[k] = ship

    return ships
