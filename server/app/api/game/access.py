from flask import Blueprint, g, request

app = Blueprint('game_access', __name__)

@app.route("/api/game/accesses", methods=['GET'])
def get_accesses():
    return "hello"

@app.route("/api/game/accesses", methods=['POST'])
def post_accesses():
    return "post"
