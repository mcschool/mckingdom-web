import json
from flask import Blueprint, g, request, jsonify
from datetime import datetime
from ...models.player import Player

app = Blueprint('game_pvp', __name__)


@app.route("/api/game/pvp/kill", methods=['PUT'])
def put_player_kill():
    data = request.get_json()
    if data.get('uuid') is None:
        result ={
            "success": False
        }
        return jsonify(result)
    player = g.session.query(Player).filter(
        data.get('uuid') == Player.uuid
    ).first()
    player.pvp_total_kills = player.pvp_total_kills + 1
    g.session.add(player)
    g.session.commit()
    data ={
        "success":True
    }
    return jsonify(data)
