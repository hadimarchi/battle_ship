class Ship:
    def __init__(self, **kwargs):
        self.length = kwargs['length']
        self.position = kwargs['position']


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
