import unittest
from ship import get_init_ships
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        init_ships = get_init_ships()
        self.player = Player(init_ships)

    def test_players_have_pieces(self):
        num_ships = len(self.player.ships)
        self.assertEqual(num_ships, 15)

    def test_players_have_right_kinds_of_ships(self):
        ship_sizes = set(range(5, 1, -1))

        for ship in self.player.ships:
            self.assertIn(ship.length, ship_sizes)


if __name__ == '__main__':
    unittest.main()
