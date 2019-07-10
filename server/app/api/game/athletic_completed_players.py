import json
from flask import Blueprint, g, request, jsonify
from datetime import datetime
from ...models.athletic_completed_players import AthleticCompletedPlayers

app = Blueprint('game_athletic_completed_players', __name__)


@app.route("/api/game/athletic_completed_players", methods=['POST'])
def post_athletic_completed_players():
    data = request.get_json()
    if data['athletic_course_id'] is None:
        return "error: no course id"
    if data['athletic_player_id'] is None:
        return "error: no player id"
    if data['athletic_player_uuid'] is None:
        return "error: no player uuid"
    if data['athletic_total_time'] is None:
        return "error: no total time"
    athletic = AthleticCompletedPlayers()
    athletic.athletic_course_id = data['athletic_course_id']
    athletic.player_id = data['athletic_player_id']
    athletic.player_uuid = data['athletic_player_uuid']
    athletic.total_time = data['athletic_total_time']
    g.session.add(athletic)
    g.session.commit()
    return "success"


@app.route("/api/game/athletic_completed_players", methods=['GET'])
def get_athletic_completed_players():
    data = request.get_json()
    athletic = g.session.query(AthleticCompletedPlayers).all()
    response = []
    for athletic in athletic:
        response.append(athletic.as_dict())
        return jsonify(response)


@app.route("/api/game/athletic_completed_players/<int:id>", methods=['GET'])
def get_athletic_completed_players_id(id = None):
    data = request.get_json()
    athletic = g.session.query(AthleticCompletedPlayers).filter(
        AthleticCompletedPlayers.id == id
    ).first()
    response = athletic.as_dict()
    return jsonify(response)


@app.route("/api/game/athletic_completed_players/course", methods=['GET'])
def get_athletic_completed_players_course():
    data = request.get_json()
    course = data['athletic_course_id']
    athletics = g.session.query(AthleticCompletedPlayers).filter(
        AthleticCompletedPlayers.athletic_course_id == course
    ).all()
    response = []
    for athletic in athletics:
        response.append(athletic.as_dict())
    return jsonify(response)


@app.route("/api/game/athletic_completed_players/player", methods=['GET'])
def get_athletic_completed_players_players():
    data = request.get_json()
    player = data['player_uuid']
    athletics = g.session.query(AthleticCompletedPlayers).filter(
        AthleticCompletedPlayers.player_uuid == player
    ).all()
    response = []
    for athletic in athletics:
        response.append(athletic.as_dict())
    return jsonify(response)


@app.route("/api/game/athletic_completed_players/total_time", methods=['GET'])
def get_athletic_completed_players_total_time():
    data = request.get_json()
    time = data['total_time']
    if time.isdecimal():
        if time < 0:
            return "error: time under 0"
        athletics = g.session.query(AthleticCompletedPlayers).filter(
            AthleticCompletedPlayers.total_time <= time
        ).all()
        response = []
        for athletic in athletics:
            response.append(athletic.as_dict())
    else:
        return "error: not number"
    return jsonify(response)


@app.route("/api/game/athletic_completed_players/player/<uuid>/course/<course_id>", methods=['GET'])
def get_athletic_completed_players_uuid_course_id(uuid = None, course_id = None):
    data = request.get_json()
    athletics = g.session.query(AthleticCompletedPlayers).filter(
        AthleticCompletedPlayers.athletic_course_id == course_id,
        AthleticCompletedPlayers.player_uuid == uuid
    ).all()
    response = []
    for athletic in athletics:
        response.append(athletic.as_dict())
    return jsonify(response)
