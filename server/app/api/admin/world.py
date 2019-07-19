import json
from datetime import datetime
from flask import Blueprint, g, request, jsonify
from ...models.world import World

app = Blueprint('admin_world', __name__)


@app.route("/api/admin/worlds", methods=['POST'])
def post_world():
    data = request.get_json()
    if data.get('name') is None:
        print("error: no world")
    else:
        if data.get('login_count') is None:
            return "error: no login_count"

        world = World()
        world.name = data['name']
        world.login_count = data['login_count']
        g.session.add(world)
        g.session.commit()
    return"hello post world"


@app.route("/api/admin/worlds", methods=['GET'])
def get_world():
    worlds = g.session.query(World).all()
    response = []
    for world in worlds:
        response.append(world.as_dict())
    return jsonify(response)


@app.route("/api/admin/worlds/<id>", methods=['GET'])
def get_world_id(id = None):
    world = g.session.query(World).filter(
        World.id == id
    ).first()
    if world is None:
        return "error: no world_id"
    response = world.as_dict()
    return jsonify(response)


@app.route("/api/admin/worlds/<id>", methods=['PUT'])
def put_world_id(id = None):
    data = request.get_json()
    if data.get('name') is None:
        return "error: no name"
    world = g.session.query(World).filter(
        World.id == id
    ).first()
    world.name = data.get('name')
    world.description = data.get('description')
    world.image_path = data.get('image_path')
    world.updated_at = datetime.now()
    g.session.add(world)
    g.session.commit()
    return "success"

