import json
from flask import Blueprint, g, request, jsonify
from datetime import datetime
from ...models.player import Player

app = Blueprint('game_command', __name__)


@app.route("/api/game/command/password", methods=['PUT'])
def put_command_password():
    data = request.get_json()
    if data.get('uuid') is None:
        return "error: no uuid"
    if data.get('password') is None:
        return "error: no password"
    if len(data.get('password')) < 4:
        return "error: pass too short"
    if len(data.get('password')) > 32:
        return "error: pass too long"
    player = g.session.query(Player).filter(
        Player.uuid == data.get('uuid')
    ).first()
    player.password = data.get('password')
    g.session.commit()
    return "success"


@app.route("/api/game/command/email", methods=['POST'])
def post_command_email():
    data = request.get_json()
    if data.get('uuid') is None:
        result = {
            "success": False
        }
        return jsonify(result)
    if data.get('email') is None:
        result = {
            "success": False
        }
        return jsonify(result)
    if len(data.get('email')) <= 10:
        result = {
            "success": False
        }
        return jsonify(result)
    if len(data.get('email')) >= 240:
        result = {
            "success": False
        }
        return jsonify(result)
    if '@' in data.get('email'):
            player = g.session.query(Player).filter(
                Player.uuid == data.get('uuid')
            ).first()
            player.email = data.get('email')
            g.session.add(player)
            g.session.commit()
    else:
        result = {
            "success": False
        }
        return jsonify(result)
    result ={
        "success": True
    }
    return jsonify(result)
