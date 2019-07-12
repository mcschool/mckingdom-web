from flask import Blueprint, g, request
from datetime import datetime

app = Blueprint('health', __name__)


@app.route("/api/health", methods=['GET'])
def get_health():
    return "health: GET"


@app.route("/api/health", methods=['POST'])
def post_health():
    return "health: POST"


@app.route("/api/health", methods=['PUT'])
def put_health():
    return "health: PUT"


@app.route("/api/health", methods=['PATCH'])
def patch_health():
    return "health: PATCH"


@app.route("/api/health", methods=['DELETE'])
def delete_health():
    return "health: DELETE"
