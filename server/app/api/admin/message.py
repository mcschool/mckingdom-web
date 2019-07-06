import json
from flask import Blueprint, g, request, jsonify
from datetime import datetime
from ...models.message import Message

app = Blueprint('admin_message', __name__)


@app.route("/api/admin/messages", methods=['GET'])
def get_messages():
    messages = g.session.query(Message).all()
    response = []
    for message in messages:
        response.append(message.as_dict())
    return jsonify(response)

@app.route("/api/admin/messages/<id>", methods=['GET'])
def get_messages_id(id = None):
    message = g.session.query(Message).filter(
        Message.id == id
    ).first()
    response = message.as_dict()
    return jsonify(response)


@app.route("/api/admin/messages", methods=['POST'])
def post_messages():
    data = request.get_json()
    messages = g.session.query(Message).all()
    if data['world'] is None:
        print("error: no world")
    else:
        messages = Message()
        messages.created_at = datetime.now()
        messages.updated_at = datetime.now()
        messages.message = data['message']
        messages.world = data['world']
        g.session.add(messages)
        g.session.commit()
    return "hello post messages"


@app.route("/api/admin/messages/:id", methods=['PUT'])
def put_messages_id():
    return "hello put messages id"


@app.route("/api/admin/messages/:id", methods=['DELETE'])
def delete_messages_id():
    return "hello delete messages id"
