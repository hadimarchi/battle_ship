import unittest
from ship import get_init_ships, Ship, InvalidShipPositionException
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        init_ships = get_init_ships()
        self.player = Player(ships=init_ships)

    def test_players_have_pieces(self):
        num_ships = len(self.player.ships)
        self.assertEqual(num_ships, 15)

    def test_players_have_right_kinds_of_ships(self):
        ship_sizes = set(range(5, 1, -1))

        for ship in self.player.ships:
            self.assertIn(ship.length, ship_sizes)


class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = Ship(length=5, position=(0, 0))

    def test_ships_have_position(self):
        self.assertEqual(self.ship.position, (0, 0))

    def test_ships_position_can_be_set(self):
        self.ship.set_position(2, 2)

        self.assertEqual(self.ship.position, (2, 2))

    def test_ships_direction_can_be_set(self):
        self.ship.set_direction("DOWN")

        self.assertEqual(self.ship.direction, "DOWN")

    def test_error_when_ship_is_out_of_bounds(self):
        with self.assertRaises(InvalidShipPositionException):
            self.ship.set_position(10000000, 100000000)


if __name__ == '__main__':
    unittest.main()
