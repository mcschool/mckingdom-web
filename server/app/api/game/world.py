import json
from datetime import datetime
from flask import Blueprint, g, request, jsonify
from ...models.world import World

app = Blueprint('game_world', __name__)

@app.route("/api/game/worlds/<id>", methods=['PUT'])
def put_world(id = None):
    world = g.session.query(World).filter(
        World.id == id
    ).first()
    world.login_count = world.login_count + 1
    g.session.add(world)
    g.session.commit()
    return "success"


