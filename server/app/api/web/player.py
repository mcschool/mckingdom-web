
import json
from datetime import datetime, timedelta
from flask import Blueprint, g, request, jsonify
from app.models import Player

app = Blueprint('web_player', __name__)

# playerの人数を表示する
@app.route("/api/web/players/all", methods=['GET'])
def get_player_all():
    players = g.session.query(Player).count()
    response = []
    data = {"players" : players}
    return jsonify(data)

@app.route("/api/web/players/loginStatus", methods=['GET'])
def get_players_login_all():
    day = datetime.now() - timedelta(days = 1)
    times = datetime.now() - timedelta(seconds = 600)
    players_login_days = g.session.query(Player).filter(
        Player.last_login_at > day,
        Player.updated_at > times
    ).count()
    data = {
        "now": players_login_days
    }
    return jsonify(data)