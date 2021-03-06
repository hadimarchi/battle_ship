from utils import ExceptionWithResponseDict, ArgumentException, save_game

from battle_ship.game import get_battle_ship_game


def create(input_dict):
    resp = CreateGameEndpoint(input_dict).create()

    return resp


class CreateGameEndpoint:
    def __init__(self, input_dict):
        self.input_dict = input_dict

    def create(self):
        try:
            name, active, inactive = self.get_args()
            resp = self.create_game(name, active, inactive)
        except ExceptionWithResponseDict as e:
            resp = e.get_resp_dict()

        return resp

    def get_args(self):
        try:
            game_name = self.input_dict['name']
            active = self.input_dict['active_player']
            inactive = self.input_dict['inactive_player']
        except:
            raise ArgumentException()

        return game_name, active, inactive

    def create_game(self, name, active, inactive):
        game_dict = get_battle_ship_game(
            name,
            active,
            inactive
        ).to_dict()

        save_game(game_dict)

        return {
            "status": "success",
            "message": "game {} has been created, with players {}, {}".format(
                name,
                active,
                inactive
            )
        }
