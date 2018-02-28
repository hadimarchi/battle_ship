from utils import make_into_response, get_game_dict_from_file, save_game
import game_endpoint

from battle_ship import SHIPS
from battle_ship.game import Game

from flask import Flask, request, session
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


@app.route('/api/game/place/ship', methods=['POST'])
def game_place_ship():
    ship, game_name = request.form['ship'], request.form['game']
    game_dict = get_game_dict_from_file(game_name)
    game = Game.from_dict(game_dict)
    game.place_ship(ship)
    game_dict = game.to_dict()
    save_game(game_dict)
    return make_into_response({
        'status': 'success'
    })


@app.route('/api/game/fire/shot', methods=['POST'])
def game_fire_shot():
    shot, game_name = request.form['shot'], request.form['game']
    game_dict = get_game_dict_from_file(game_name)
    game = Game.from_dict(game_dict)
    hit, is_alive = game.fire_shot(shot)
    game_dict = game.to_dict()
    save_game(game_dict)
    return make_into_response({
        'status': 'success',
        'is_hit': hit,
        'is_alive': is_alive
    })


@app.route('/api/game/swap/players', methods=['POST'])
def game_swap_players():
    game = request.form['game']
    return make_into_response({
        'test_msg': 'swapping players'
    })


if __name__ == "__main__":
    app.secret_key = "a;osdihfw983ujfaiofzofisajdfojnvzmxcvoiurqhf98wauofij"
    app.run(debug=True)
