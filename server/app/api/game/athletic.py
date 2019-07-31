from flask import Blueprint, g, request
from datetime import datetime

app = Blueprint('game_athletic_completed_players', __name__)


@app.route("/api/game/athletic/course/change", methods=['POST'])
def a():
    return "aaa"
