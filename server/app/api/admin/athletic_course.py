import json
from flask import Blueprint, g, request, jsonify
from datetime import datetime
from ...models.athletic_course import AthleticCourse

app = Blueprint('admin_athletic_course', __name__)


@app.route("/api/admin/athletic_courses", methods=['POST'])
def post_athletic_courses():
    data = request.get_json()
    if data['name'] is None:
        return "error: no world"
    athletic = AthleticCourse()
    athletic.course_no = data['course_no']
    athletic.name = data['name']
    athletic.description = data['description']
    athletic.difficulty = data['difficulty']
    g.session.add(athletic)
    g.session.commit()
    print("=====")
    print(data['difficulty'])
    print("=====")
    return "success"


@app.route("/api/admin/athletic_courses/<id>", methods=['GET'])
def get_athletic_courses(id = None):
    data = request.get_json()
    athletic = g.session.query(AthleticCourse).filter(
        AthleticCourse.id == id
    ).first()
    response = athletic.as_dict()
    return jsonify(response)


@app.route("/api/admin/athletic_courses/<id>", methods=['PUT'])
def put_athletic_courses(id = None):
    data = request.get_json()
    if data['course_no'] is None:
        return "error: no course_no"
    if data['name'] is None:
        return "error: no world"
    athletic = g.session.query(AthleticCourse).filter(
        AthleticCourse.id == id
    ).first()
    athletic.course_no = data['course_no']
    athletic.name = data['name']
    athletic.description = data['description']
    athletic.difficulty = data['difficulty']
    g.session.add(athletic)
    g.session.commit()
    return"success"


@app.route("/api/admin/athletic_courses/<id>", methods=['DELETE'])
def delete_athletic_courses(id = None):
    if id.isdecimal():
        athletic = g.session.query(AthleticCourse).filter(
            AthleticCourse.id == id
        ).delete()
        g.session.commit()
    else:
        return "error: no id"
    return"successfully deleted"
