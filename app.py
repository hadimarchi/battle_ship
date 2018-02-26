from battle_ship import SHIPS

from flask import Flask
from flask import Response
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


@app.route('/api/ships')
def hello_world():
    return Response(json.dumps(SHIPS), mimetype="text/json")


if __name__ == "__main__":
    app.run()
