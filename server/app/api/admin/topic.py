from flask import Blueprint, g, request, jsonify
from datetime import datetime
from ...models.topic import Topic

app = Blueprint('admin_topic', __name__)


@app.route("/api/admin/topics", methods=['POST'])
def post_topics():
    data = request.get_json()
    if data.get('title') is None:
        return"error: no title"
    topic = Topic()
    topic.title = data.get('title')
    topic.body = data.get('body')
    topic.is_published = data.get('is_published')
    if topic.is_published == "true":
        topic.published_at = datetime.now()
    else:
        topic.published_at = None
    g.session.add(topic)
    g.session.commit()
    return "success"


@app.route("/api/admin/topics", methods=['GET'])
def get_topics():
    topics = g.session.query(Topic).all()
    topics_data = []
    for topic in topics:
        topics_data.append(topic.as_dict())
    data = {
        "topics": topics_data
    }
    return jsonify(data)
