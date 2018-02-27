
from flask import Response

import json
import os


def make_into_response(dic):
    return Response(json.dumps(dic), mimetype="text/json")


def get_game_dict_from_file(game_name):
    game_file_path = 'games/{}.json'.format(game_name)
    with open(game_file_path, 'r') as f:
        game_dict = json.load(f)
    return game_dict


def check_game_exists(game_path):
    return os.path.exists('games') and os.path.exists(game_path)


def save_game(game_dict):
    game_path = 'games/{}.json'.format(game_dict['name'])

    if not check_game_exists(game_path):
        raise GameDoesntExistException(game_dict['name'])

    with open(game_path, 'w') as f:
        f.write(json.dumps(game_dict))


class ExceptionWithResponseDict(Exception):
    def get_resp_dict(self):
        assert (self.resp_dict is not None)

        return self.resp_dict


class GameAlreadyExistsException(ExceptionWithResponseDict):
    def __init__(self, name):
        err = {
            "status": "error",
            "type": "GameAlreadyExistsException",
            "message": "Game {} already exisits".format(name)
        }

        self.resp_dict = err


class GameDoesntExistException(ExceptionWithResponseDict):
    def __init__(self, name):
        err = {
            "status": "error",
            "type": "GameDoesntExistException",
            "message": "Game {} does not exist".format(name)
        }
        self.resp_dict = err
