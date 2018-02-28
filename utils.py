
from battle_ship.game import Game

from flask import Response

from contextlib import contextmanager
import json
import os


def make_into_response(dic):
    return Response(json.dumps(dic), mimetype="text/json")


@contextmanager
def open_game(game_name):
    try:
        game = load_game(game_name)
        yield game
    finally:
        save_game(game)


def check_game_exists(game_path):
    return os.path.exists('games') and os.path.exists(game_path)


def load_game(game_name):
    game_dict = get_game_dict_from_file(game_name)
    return Game.from_dict(game_dict)


def get_game_dict_from_file(game_name):
    game_file_path = 'games/{}.json'.format(game_name)

    print('loading game: ', game_file_path)
    with open(game_file_path, 'r') as f:
        game_dict = json.load(f)
    print('loaded game: ', game_dict)
    return game_dict


def save_game(game):
    if isinstance(game, dict):
        game_dict = game
    else:
        game_dict = game.to_dict()

    game_path = 'games/{}.json'.format(game_dict['name'])

    with open(game_path, 'w') as f:
        f.write(json.dumps(game_dict, indent=2))


class ExceptionWithResponseDict(Exception):
    def get_resp_dict(self):
        assert (self.resp_dict is not None)

        return self.resp_dict


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


class GameDoesntExistException(ExceptionWithResponseDict):
    def __init__(self, name):
        err = {
            "status": "error",
            "type": "GameDoesntExistException",
            "message": "Game {} does not exist".format(name)
        }
        self.resp_dict = err
