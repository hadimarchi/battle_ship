import unittest

from battle_ship.ship import get_init_ships, Ship
from battle_ship.position import InvalidPositionException, Position
from battle_ship.player import Player
from battle_ship.game import get_battle_ship_game, Game


class TestPlayer(unittest.TestCase):
    def setUp(self):
        init_ships = get_init_ships()
        self.player = Player(side="america", ships=init_ships)

    def test_players_have_pieces(self):
        num_ships = len(self.player.ships)
        self.assertEqual(num_ships, 5)

    def test_players_have_right_kinds_of_ships(self):
        ship_sizes = set(range(5, 1, -1))

        for k, v in self.player.ships.items():
            self.assertIn(v.length, ship_sizes)

    def test_to_dict(self):
        player_dict = self.player.to_dict()
        self.assertIn('player', player_dict)
        self.assertEqual('america', player_dict['player'])
        self.assertIn('ships', player_dict)

    def test_from_dict(self):
        player_dict = self.player.to_dict()
        new_player = Player.from_dict(player_dict)
        self.assertEqual(self.player.side, new_player.side)


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
            position=pos,
            is_alive=True
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

    def test_to_dict(self):
        ship_dict = self.ship.to_dict()
        self.assertEqual(self.ship.type, ship_dict['type'])

    def test_from_dict(self):
        ship_dict = self.ship.to_dict()
        new_ship = Ship.from_dict(ship_dict)
        self.assertEqual(self.ship.type, new_ship.type)
        self.assertEqual(self.ship.length, new_ship.length)
        self.assertEqual(self.ship.position.fore, new_ship.position.fore)


class TestPosition(unittest.TestCase):
    def setUp(self):
        self.position = Position(aft=(0, 0), fore=(0, 5), is_vertical=False)

    def test_to_dict(self):
        pos_dict = self.position.to_dict()
        self.assertEqual(pos_dict['aft'], self.position.aft)
        self.assertEqual(pos_dict['fore'], self.position.fore)
        self.assertEqual(pos_dict['is_vertical'], self.position.is_vertical)

    def test_from_dict(self):
        pos_dict = self.position.to_dict()
        new_pos = Position.from_dict(pos_dict)
        self.assertEqual(new_pos.aft, self.position.aft)
        self.assertEqual(new_pos.fore, self.position.fore)
        self.assertEqual(new_pos.is_vertical, self.position.is_vertical)


class TestBattleShip(unittest.TestCase):
    def setUp(self):
        self.game = get_battle_ship_game("test", "America", "Russia")

    def test_has_players(self):
        self.assertTrue(self.game.active)
        self.assertTrue(self.game.inactive)

    def test_players_can_place_ships(self):
        self.assertTrue(self.game.active.ship_location("carrier") != (0, 0))

    def test_to_dict(self):
        game_dict = self.game.to_dict()
        self.assertEqual(game_dict['name'], self.game.name)
        self.assertEqual(game_dict['active']['player'], self.game.active.side)
        self.assertEqual(game_dict['inactive']['player'], self.game.inactive.side)

    def test_from_dict(self):
        game_dict = self.game.to_dict()
        new_game = Game.from_dict(game_dict)
        self.assertEqual(new_game.name, self.game.name)


if __name__ == '__main__':
    unittest.main()
