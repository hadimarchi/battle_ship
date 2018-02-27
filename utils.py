
from flask import Response

import json


def make_into_response(dic):
    return Response(json.dumps(dic), mimetype="text/json")


def get_game_dict_from_file(game_name):
    game_file_path = 'games/{}.json'.format(game_name)
    with open(game_file_path, 'r') as f:
        game_dict = json.load(f)
    return game_dict


class ExceptionWithResponseDict(Exception):
    def get_resp_dict(self):
        assert (self.resp_dict is not None)

        return self.resp_dict
