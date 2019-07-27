from flask import Blueprint, g, request, jsonify
from datetime import datetime
from ...models.message import Message

app = Blueprint('game_message', __name__)


@app.route("/api/game/messages", methods=['GET'])
def get_messages():
    messages = g.session.query(Message).all()
    response = []
    for message in messages:
        response.append(message.as_dict())
    return jsonify(response)
