class Ship:
    def __init__(self, length):
        self.length = length


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
        len_sized_ships = [Ship(length) for _ in range(amount)]
        ships += len_sized_ships

    return ships
