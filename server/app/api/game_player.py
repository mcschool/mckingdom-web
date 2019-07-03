from flask import Blueprint

app = Blueprint('game_player', __name__)


@app.route("/api/game/players", methods=['GET'])
def get_players():
    return "hello"

@app.route("/api/game/players", methods=['PATCH'])
def patch_players():
    return "byebye"

@app.route("/api/game/players", methods=['POST'])
def post_players():
    return "yo"

@app.route("/api/game/players", methods=['PUT'])
def put_players():
    return "no"

@app.route("/api/game/players", methods=['DELETE'])
def delete_players():
    return "yes"
