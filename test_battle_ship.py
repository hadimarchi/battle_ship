import unittest

from battle_ship.ship import get_init_ships, Ship
from battle_ship.position import InvalidPositionException, Position
from battle_ship.player import Player
from battle_ship.game import get_battle_ship_game


class TestPlayer(unittest.TestCase):
    def setUp(self):
        init_ships = get_init_ships()
        self.player = Player(ships=init_ships)

    def test_players_have_pieces(self):
        num_ships = len(self.player.ships)
        self.assertEqual(num_ships, 5)

    def test_players_have_right_kinds_of_ships(self):
        ship_sizes = set(range(5, 1, -1))

        for k, v in self.player.ships.items():
            self.assertIn(v.length, ship_sizes)


class TestShip(unittest.TestCase):
    def setUp(self):
        pos = Position(
            fore=(0, 0),
            aft=(0, 1),
            is_vertical=True
        )

        self.ship = Ship(
            type="carrier",
            length=5,
            position=pos
        )

    def test_ships_have_position(self):
        self.assertEqual(self.ship.position.aft, (0, 1))

    def test_ships_position_can_be_set(self):
        new_pos = Position(
            aft=(2, 2),
            fore=(2, 7),
            is_vertical=True
        )

        self.ship.set_position(new_pos)

        self.assertEqual(self.ship.position.aft, (2, 2))
        self.assertEqual(self.ship.position.fore, (2, 7))

    def test_error_when_ship_is_out_of_bounds(self):
        with self.assertRaises(InvalidPositionException):
            self.ship.set_position(
                Position(
                    fore=(0, 10000000),
                    aft=(0, 0),
                    is_vertical=True
                )
            )


class TestBattleShip(unittest.TestCase):
    def setUp(self):
        self.game = get_battle_ship_game("test", "America", "Russia")

    def test_has_players(self):
        self.assertTrue(self.game.active)
        self.assertTrue(self.game.inactive)

    def test_players_can_place_ships(self):
        self.assertTrue(self.game.active.ship_location("carrier") != (0, 0))


if __name__ == '__main__':
    unittest.main()
