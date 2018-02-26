from flask import Flask
from flask import Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    test = {"msg": "hello world"}
    return Response(json.dumps(test), mimetype="text/json")


if __name__ == "__main__":
    app.run()
