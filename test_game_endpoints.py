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

        resp = game_endpoint.create(game_args, self.session)

        self.assertEqual(resp['type'], 'success')


if __name__ == '__main__':
    unittest.main()
