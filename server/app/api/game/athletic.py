from flask import Blueprint, g, request
from datetime import datetime

app = Blueprint('game_athletic', __name__)


@app.route("/api/game/athletic/course/change", methods=['POST'])
def a():
    return "aaa"
