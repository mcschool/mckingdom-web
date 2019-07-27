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
    topic.image_path = data.get('image_path')
    topic.is_published = data.get('is_published')
    if topic.is_published is True:
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


@app.route("/api/admin/topics/<id>", methods=['GET'])
def get_topics_id(id = None):
    topic = g.session.query(Topic).filter(
        Topic.id == id
    ).first()
    if topic is None:
        return "error: no data"
    res = {
        "topic": topic.as_dict()
    }
    return jsonify(res)


@app.route("/api/admin/topics/<id>", methods=['PUT'])
def put_topics_id(id = None):
    data = request.get_json()
    if data.get('title') is None:
        return "error: no title"
    topic = g.session.query(Topic).filter(
        Topic.id == id
    ).first()
    topic.title = data.get('title')
    topic.body = data.get('body')
    topic.updated_at = datetime.now()
    g.session.add(topic)
    g.session.commit()
    return "success"


@app.route("/api/admin/topics/<id>/published", methods=['PUT'])
def put_topics_id_published(id = None):
    data = request.get_json()
    if data.get('is_published') is None:
        return "error: no data"
    topic = g.session.query(Topic).filter(
        Topic.id == id
    ).first()
    topic.is_published = data.get('is_published')
    g.session.add(topic)
    g.session.commit()
    return "success"
