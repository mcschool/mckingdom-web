import json
from flask import Blueprint, g, request, jsonify
from ...models.message import Message

app = Blueprint('admin_message', __name__)

@app.route("/api/admin/messages", methods=['GET'])
def get_messages():
    return "hello messages"

@app.route("/api/admin/messages/:id", methods=['GET'])
def get_messages_id():
    return "hello messages id"

@app.route("/api/admin/messages", methods=['POST'])
def post_messages():
    return "hello post messages"

@app.route("/api/admin/messages/:id", methods=['PUT'])
def put_messages_id():
    return "hello put messages id"

@app.route("/api/admin/messages/:id", methods=['DELETE'])
def delete_messages_id():
    return "hello delete messages id"
