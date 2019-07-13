import json
from flask import Blueprint, g, request, jsonify
from ...models.player import Player

app = Blueprint('game_command', __name__)


@app.route("/api/game/command/password", methods=['PUT'])
def put_command_password():
    data = request.get_json()
    if data.get('uuid') is None:
        return "error: no uuid"
    if data.get('password') is None:
        return "error: no password"
    if len(data.get('password')) > 4:
        if len(data.get('password')) < 32:
            player = g.session.query(Player).filter(
                Player.uuid == data.get('uuid')
            ).first()
            player.password = data.get('password')
            g.session.commit()
    return "success"


@app.route("/api/game/command/email", methods=['PUT'])
def put_command_email():
    data = request.get_json()
    if data.get('uuid') is None:
        return "error: no uuid"
    if data.get('email') is None:
        return "error: no email"
    if len(data.get('email')) >= 10:
        if len(data.get('email')) <= 240:
            if '@' in data.get('email'):
                player = g.session.query(Player).filter(
                    Player.uuid == data.get('uuid')
                ).first()
                player.email = data.get('email')
            else:
                return "error: no @ mark"
    return "success"
