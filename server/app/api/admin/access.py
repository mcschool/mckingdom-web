import json
from flask import Blueprint, g, request, jsonify
from sqlalchemy import desc
from ...models.access import Access

app = Blueprint('admin_access', __name__)


@app.route("/api/admin/access/game", methods=['GET'])
def get_accesses_game():
    accesses = g.session.query(Access).all()
    response = []
    for access in accesses:
        response.append(access.as_dict())
    return jsonify(response)


@app.route("/api/admin/access/game/<id>", methods=['GET'])
def post_accesses_game_id(id = None):
    print(id)
    access =g.session.query(Access).filter(
        Access.id == id
    ).first()
    response = access.as_dict()
    return jsonify(response)


@app.route("/api/admin/access", methods = ['GET'])
def get_access():
    accesses = g.session.query(Access).order_by(desc(Access.id)).all()
    response = []
    for access in accesses:
        response.append(access.as_dict())
    return jsonify(response)
