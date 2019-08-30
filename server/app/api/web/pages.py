from flask import Blueprint, g, request, jsonify
from ...models import Topic

app = Blueprint('web_pages', __name__)


@app.route("/api/web/pages/index", methods=['GET'])
def get_index_page():
    topics = g.session.query(Topic).limit(3).all()
    topics = [topic.as_dict() for topic in topics]
    res = {
        "topics": topics
    }

    return jsonify(res)
