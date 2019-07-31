from flask import Blueprint, g, request, jsonify
from datetime import datetime
from app.models import Player, Access

app = Blueprint('game_me', __name__)


@app.route("/api/game/me", methods=['PUT'])
def me():
    data = request.get_json()
    player = g.session.query(Player).filter(Player.uuid == data.get("json")).first()
    return jsonify(player.as_dict())
