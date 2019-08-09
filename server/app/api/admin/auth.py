import json
from flask import Blueprint, g, request, jsonify

app = Blueprint('admin_auth', __name__)


@app.route("/api/admin/auth/login", methods=['POST'])
def post_auth_login():
    data = request.get_json()
    if data.get("loginId") == 'mckingdom' and data.get('password') == 'u56i79ns':
        return jsonify({"token": "LRCknUPLswvd"}), 200
    return jsonify({"success": False}), 401


@app.route("/api/admin/auth/auth", methods=['POST'])
def post_auth_auth():
    headers = request.headers
    if headers.get("X-Admin-Token") == 'LRCknUPLswvd':
        return jsonify({'success': True})
    return jsonify({'success': False})
