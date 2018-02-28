from utils import                   \
    make_into_response,             \
    open_game,                      \
    get_game_dict_from_file

import game_endpoint

from battle_ship import SHIPS

from flask import Flask, request
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


@app.route('/api/ships/types')
def ship_types():
    return make_into_response(SHIPS)


@app.route('/api/game/create', methods=['POST'])
def game_create():
    resp_dict = game_endpoint.create(request.form)

    return make_into_response(resp_dict)


@app.route('/api/game/<string:name>', methods=['GET'])
def game_get_state(name):
    try:
        game_dict = get_game_dict_from_file(name)
        return make_into_response(json.dumps(game_dict))

    except Exception as e:
        return make_into_response({
            'status': 'error',
            'type': 'no game found with name {}'.format(name),
            'message': str(e)
        })


@app.route('/api/place/ship', methods=['POST'])
def game_place_ship():
    try:
        ship, game_name = request.form['ship'], request.form['game']

        with open_game(game_name) as game:
            game.place_ship(ship)

        return make_into_response({
            'status': 'success'
        })

    except Exception as e:
        return make_into_response({
            'status': 'error',
            'type': type(e),
            'message': str(e)
        })


@app.route('/api/fire/shot', methods=['POST'])
def game_fire_shot():
    shot = json.loads(request.form['shot'])
    game_name = request.form['game']

    with open_game(game_name) as game:
        hit, is_alive = game.fire_shot(shot)

    print("IS HIT = ", hit)

    return make_into_response({
        'status': 'success',
        'is_hit': hit,
        'is_alive': is_alive
    })


@app.route('/api/game/swap/players', methods=['POST'])
def game_swap_players():
    game_name = request.form['game']

    with open_game(game_name) as game:
        game.swap_players()

    return make_into_response({
        'status': 'success'
    })


if __name__ == "__main__":
    app.secret_key = "a;osdihfw983ujfaiofzofisajdfojnvzmxcvoiurqhf98wauofij"
    app.run(debug=True)
