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