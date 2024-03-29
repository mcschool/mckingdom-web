from flask import Blueprint, g, request
from datetime import datetime
from ...models.athletic_completed_players import AthleticCompletedPlayers
from ...models.player import Player
from ...models.athletic_course import AthleticCourse

app = Blueprint('game_athletic', __name__)


@app.route("/api/game/athletic/course/change", methods=['PUT'])
def athletic_course_change():
    data = request.get_json()
    if data.get('course_no') is None:
        return "error: course_no is none"
    athletic_course = g.session.query(AthleticCourse).filter(
        data.get('course_no') == AthleticCourse.course_no
    ).first()
    athletic_course.play_count = athletic_course.play_count + 1
    g.session.add(athletic_course)
    g.session.commit()
    return jsonify(data)
