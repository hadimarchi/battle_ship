import unittest

from battle_ship.ship import get_init_ships, Ship, InvalidShipPositionException
from battle_ship.player import Player
from battle_ship_game import BattleShip


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
        self.ship = Ship(type="carrier", length=5, position=(0, 0))

    def test_ships_have_position(self):
        self.assertEqual(self.ship.aft, (0, 0))

    def test_ships_position_can_be_set(self):
        self.ship.set_position((2, 2), (2, 7))

        self.assertEqual(self.ship.aft, (2, 2))
        self.assertEqual(self.ship.fore, (2, 7))

    def test_error_when_ship_is_out_of_bounds(self):
        with self.assertRaises(InvalidShipPositionException):
            self.ship.set_position((0, 10000000), (0, 0))


class TestBattleShip(unittest.TestCase):
    def setUp(self):
        america = Player(side="America", ships=get_init_ships())
        russia = Player(side="Russia", ships=get_init_ships())

        self.game = BattleShip(player1=russia, player2=america)

    def test_has_players(self):
        self.assertTrue(self.game.player1)
        self.assertTrue(self.game.player2)

    def test_game_starts_by_placing_pieces(self):
        self.assertTrue(self.game.placement_phase)

        self.game.play()
        self.assertFalse(self.game.placement_phase)

    def test_players_place_all_pieces_befor_switching(self):
        active_player = self.game.active_player

        self.game.swap_active_players()

        self.assertNotEqual(active_player, self.game.active_player)

    def test_gui_runs(self):
        self.game.test_run(.5)

    def test_players_can_place_ships(self):
        self.assertTrue(self.game.player1.ship_location("carrier") != (0, 0))


if __name__ == '__main__':
    unittest.main()
