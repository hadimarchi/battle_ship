from utils import ExceptionWithResponseDict

from battle_ship.game import get_battle_ship_game

import json


class ArgumentException(ExceptionWithResponseDict):
    def __init__(self):
        msg = "Need active_player, inactive_player and name to create game"
        err = {
            "type": "error",
            "message": msg
        }

        self.resp_dict = err


class GameAlreadyExistsException(ExceptionWithResponseDict):
    def __init__(self, name):
        err = {
            "type": "error",
            "message": "Game {} already exisits".format(name)
        }

        self.resp_dict = err


def create_game(session, name, active, inactive):

    if session.get(name, '') != '':
        raise GameAlreadyExistsException(name)

    session[name] = json.dumps(get_battle_ship_game(
        name,
        active,
        inactive
    ).to_dict())

    return {
        "type": "success",
        "message": "game {} has been created, with players {}, {}".format(
            name,
            active,
            inactive
        )
    }


def get_create_game_args(input_dict):
    try:
        game_name = input_dict['name']
        active = input_dict['active_player']
        inactive = input_dict['inactive_player']
    except:
        raise ArgumentException()

    return game_name, active, inactive


def create(input_dict, session):
    try:
        name, active, inactive = get_create_game_args(input_dict)
    except ArgumentException as e:
        return e.get_resp_dict()

    try:
        resp = create_game(session, name, active, inactive)
    except ExceptionWithResponseDict as e:
        resp = e.get_resp_dict()
    except Exception as e:
        resp = {'type': 'error', 'message': str(e)}

    return resp
