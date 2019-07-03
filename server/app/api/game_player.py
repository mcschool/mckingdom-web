from flask import Blueprint

app = Blueprint('game_player', __name__)


@app.route("/", methods=['GET'])
def index():
    return "hello"
