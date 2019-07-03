from flask import Blueprint

app = Blueprint('game_player', __name__)


@app.route("/")
def index():
    return {"a": 1}
