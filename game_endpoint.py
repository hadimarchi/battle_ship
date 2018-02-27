from utils import ExceptionWithResponseDict

from battle_ship.game import get_battle_ship_game

import json
import os


class ArgumentException(ExceptionWithResponseDict):
    def __init__(self):
        msg = "Need active_player, inactive_player and name to create game"
        err = {
            "status": "error",
            "type": "ArgumentException",
            "message": msg
        }

        self.resp_dict = err


class GameAlreadyExistsException(ExceptionWithResponseDict):
    def __init__(self, name):
        err = {
            "status": "error",
            "type": "GameAlreadyExistsException",
            "message": "Game {} already exisits".format(name)
        }

        self.resp_dict = err


def create(input_dict, session):
    resp = CreateGameEndpoint(input_dict, session).create()

    return resp


class CreateGameEndpoint:
    def __init__(self, input_dict, session):
        self.input_dict = input_dict
        self.session = session

    def create(self):
        try:
            name, active, inactive = self.get_args()
        except ArgumentException as e:
            return e.get_resp_dict()

        try:
            resp = self.create_game_in_session(name, active, inactive)
        except ExceptionWithResponseDict as e:
            resp = e.get_resp_dict()
        except Exception as e:
            resp = {'status': 'error', 'message': str(e)}

        return resp

    def get_args(self):
        try:
            game_name = self.input_dict['name']
            active = self.input_dict['active_player']
            inactive = self.input_dict['inactive_player']
        except:
            raise ArgumentException()

        return game_name, active, inactive

    def create_game_in_session(self, name, active, inactive):
        game_file_path = 'games/{}.json'.format(name)

        if os.path.exists(game_file_path):
            raise GameAlreadyExistsException(name)

        game_dict = get_battle_ship_game(
            name,
            active,
            inactive
        ).to_dict()

        self.save_to_file(game_file_path, game_dict)

        return {
            "status": "success",
            "message": "game {} has been created, with players {}, {}".format(
                name,
                active,
                inactive
            )
        }

    def save_to_file(self, game_file_path, game_dict):
        if not os.path.exists('games'):
            os.makedirs(game_file_path)

        with open(game_file_path, 'w') as f:
            f.write(json.dumps(game_dict))
