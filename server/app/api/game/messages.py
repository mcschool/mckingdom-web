from flask import Blueprint, g, request, jsonify
from datetime import datetime
from ...models.message import Message

app = Blueprint('game_message', __name__)


@app.route("/api/game/messages", methods=['GET'])
def get_messages():
    messages = g.session.query(Message).all()
    message_data = []
    for message in messages:
        message_data.append(message.as_dict())
    data ={
        "message": message_data
    }
    return jsonify(data)
