from flask import Blueprint, g, request
from datetime import datetime
from app.models import Player, Access

app = Blueprint('game_athletic_completed_players', __name__)


@app.route("/api/game/me", methods=['PUT'])
def me():
    return "success"
