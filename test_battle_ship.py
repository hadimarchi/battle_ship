import unittest
from player import Player, get_init_player_ships


class TestPlayer(unittest.TestCase):
    def setUp(self):
        init_ships = get_init_player_ships()
        self.player = Player(init_ships)

    def test_players_have_pieces(self):
        num_ships = len(self.player.ships)
        self.assertEqual(num_ships, 15)


if __name__ == '__main__':
    unittest.main()
