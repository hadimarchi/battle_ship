
class Player(object):
    def __init__(self, ships):
        self.ships = ships


def get_init_player_ships():
    ship_lengths = list(range(5, 1, -1))
    ship_amounts = list(range(6))

    print(ship_lengths)
    print(ship_amounts)

    return list(range(15))
