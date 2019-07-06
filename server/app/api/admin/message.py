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


@app.route("/api/admin/messages/<id>", methods=['PUT'])
def put_messages_id(id = None):
    data = request.get_json()
    if data['message'] is None:
        print("error: no message")
    elif data['world'] is None:
            print("error: no world")
    else:
        message = g.session.query(Message).filter(
            Message.id == id
        ).first()
        message.message = data['message']
        message.world = data['world']
        g.session.add(message)
        g.session.commit()
    return "hello put messages id"


@app.route("/api/admin/messages/<id>", methods=['DELETE'])
def delete_messages_id(id = None):
    message = g.session.query(Message).filter(
        Message.id == id
    ).delete()
    g.session.commit()
    return "hello delete messages id"
