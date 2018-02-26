from utils import make_into_response
import game_endpoint

from battle_ship import SHIPS

from flask import Flask, request, session
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api/ships/types')
def ship_types():
    return make_into_response(SHIPS)


@app.route('/api/game/create', methods=['POST'])
def game_create():
    resp_dict = game_endpoint.create(request.form, session)

    return make_into_response(resp_dict)


if __name__ == "__main__":
    app.secret_key = "a;osdihfw983ujfaidhf98wauofij"
    app.run(debug=True)
