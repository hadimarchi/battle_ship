from utils import make_into_response
import game_endpoint

from battle_ship import SHIPS

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
    resp_dict = game_endpoint.create(request.form, session)

    return make_into_response(resp_dict)


@app.route('/api/game/<name>', methods=['GET'])
def game_get_state(name):
    try:
        game_file_path = 'games/{}.json'.format(name)
        with open(game_file_path, 'r') as f:
            game_json = json.load(f)

            return make_into_response(game_json)

    except Exception as e:
        return make_into_response({
            'status': 'error',
            'type': 'no game found with name {}'.format(name),
            'message': str(e)
        })


@app.route('/api/game/place/ship', methods=['POST'])
def game_place_ship():
    ship, game = request.form['ship'], request.form['game']
    return make_into_response({
        'test_msg': 'adding ship: ' + ship + ', to game: ' + game
    })


@app.route('/api/game/fire/shot', methods=['POST'])
def game_fire_shot():
    return make_into_response({
        'test_msg': 'firing shot at position: ' + request.form['position']
    })


@app.route('/api/game/swap/players', methods=['POST'])
def game_swap_players():
    return make_into_response({
        'test_msg': 'swapping players'
    })


if __name__ == "__main__":
    app.secret_key = "a;osdihfw983ujfaiofzofisajdfojnvzmxcvoiurqhf98wauofij"
    app.run(debug=True)
