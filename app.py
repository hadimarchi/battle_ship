from battle_ship import SHIPS
from battle_ship.game import get_battle_ship_game

from flask import Flask, request, session
from flask import Response
from flask_cors import CORS
import json
import uuid


app = Flask(__name__)
CORS(app)


def get_response(dic):
    return Response(json.dumps(dic), mimetype="text/json")


@app.route('/api/ships/types')
def ship_types():
    return get_response(SHIPS)


def get_name_arg_error():
    msg = "Need active_player, inactive_player and name to create game"
    err = {
        "type": "error",
        "message": msg
    }

    return get_response(err)


def get_already_exists_error(name):
    err = {
        "type": "error",
        "message": "Game {} already exisits".format(name)
    }

    return get_response(err)


@app.route('/api/game/create', methods=['POST'])
def game_create():
    try:
        game_name = request.form['name']
        active = request.form['active_player']
        inactive = request.form['inactive_player']
    except:
        return get_name_arg_error()

    if session.get(game_name, '') != '':
        return get_already_exists_error(game_name)

    session[game_name] = json.dumps(get_battle_ship_game(
        game_name,
        active,
        inactive
    ).to_dict())

    return get_response({
        "type": "success",
        "message": "game {} has been created, with players {}, {}".format(
            game_name,
            active,
            inactive
        )
    })


if __name__ == "__main__":
    app.secret_key = "a;osdihfw983ujfaidhf98wauofij"
    app.run(debug=True)
