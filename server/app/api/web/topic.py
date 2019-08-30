import json
from datetime import datetime, timedelta
from flask import Blueprint, g, request, jsonify
from app.models import Player
from ...models.topic import Topic

app = Blueprint('web_topic', __name__)


@app.route("/api/web/topics", methods=['GET'])
def get_topics_all():
    topics = g.session.query(Topic).all()
    topics_data = []
    for topic in topics:
        topics_data.append(topic.as_dict())
    data = {
        "topics": topics_data
    }
    return jsonify(data) 


@app.route("/api/web/topics/<id>", methods=['GET'])
def get_topic_id(id=None):
    topic = g.session.query(Topic).filter(
        Topic.id == id
    ).first()
    if topic is None:
        return "topic : null"
    if topic.is_published is False:
        return "topic : null"
    data = {
        "topic": topic.as_dict()
    }
    return jsonify(data)
