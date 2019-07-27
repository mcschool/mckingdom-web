from flask import Blueprint, g, request, jsonify
from datetime import datetime

app = Blueprint('health', __name__)


@app.route("/api/health", methods=['GET'])
def get_health():
    data = {
        "status": "health GET",
    }
    return jsonify(data)


@app.route("/api/health", methods=['POST'])
def post_health():
    data = {
        "status": "health POST",
    }
    return jsonify(data)


@app.route("/api/health", methods=['PUT'])
def put_health():
    data = {
        "status": "health PUT",
    }
    return jsonify(data)


@app.route("/api/health", methods=['PATCH'])
def patch_health():
    data = {
        "status": "health PATCH",
    }
    return jsonify(data)


@app.route("/api/health", methods=['DELETE'])
def delete_health():
    data = {
        "status": "health DELETE",
    }
    return jsonify(data)
