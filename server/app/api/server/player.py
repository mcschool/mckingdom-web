
import json
from datetime import datetime
from flask import Blueprint, g, request, jsonify
from app.models import Player

app = Blueprint('server_player', __name__)

# playerの人数を表示する
@app.route("/api/server/players/all", methods=['GET'])
def get_player_all():
    players = g.session.query(Player).all()
    player_count = len(players)
    response = []
    data = {"players" : player_count}
    return jsonify(data)