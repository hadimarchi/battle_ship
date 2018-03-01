import game_endpoint

import unittest


class TestCreateGame(unittest.TestCase):
    def setUp(self):
        self.session = {}

    def test_games_can_be_made(self):
        game_args = {
            "name": "test-game",
            "active_player": "America",
            "inactive_player": "Russia"
        }

        resp = game_endpoint.create(game_args)

        self.assertEqual(resp['status'], 'success')

    def test_invalid_sends_error(self):
        invalid_args = {
            "name": "test",
            "active_player": "America"
        }

        resp = game_endpoint.create(invalid_args)

        self.assertEqual(resp['status'], 'error')
        self.assertEqual(resp['type'], 'ArgumentException')

    def test_games_with_same_not_is_error(self):
        self.session = {"test": "-- Game Object Goes Here --"}
        invalid_args = {
            "name": "test",
            "active_player": "America",
            "inactive_player": "Russia"
        }

        resp = game_endpoint.create(invalid_args, self.session)

        self.assertEqual(resp['status'], 'error')
        self.assertEqual(resp['type'], 'GameAlreadyExistsException')


if __name__ == '__main__':
    unittest.main()
