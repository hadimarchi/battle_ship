import options


class InvalidShipPositionException(Exception):
    pass


class Ship:
    def __init__(self, **kwargs):
        self.length = kwargs['length']
        self.position = kwargs.get('position', (0, 0))
        self.direction = kwargs.get('direction', 'DOWN')

    def is_out_of_bounds(self, pos):
        x, y = pos

        return x < 0 or x > options.width or \
            y < 0 or y > options.height

    def set_position(self, x, y):
        new_pos = (x, y)

        if self.is_out_of_bounds(new_pos):
            msg = "invalid ship position ({}, {})".format(x, y)
            raise InvalidShipPositionException(msg)

        self.position = new_pos

    def set_direction(self, direction):
        self.direction = direction


def get_init_ships():
    ship_types = [
        [5, 1],
        [4, 2],
        [3, 3],
        [3, 4],
        [2, 5]
    ]

    ships = []
    for length, amount in ship_types:
        len_sized_ships = [
            Ship(length=length, position=(0, 0)) for _ in range(amount)
        ]

        ships += len_sized_ships

    return ships
