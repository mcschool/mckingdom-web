from flask import Blueprint, g, request
from datetime import datetime
from ...models.access import Access

app = Blueprint('game_access', __name__)


@app.route("/api/game/accesses", methods=['GET'])
def get_accesses():
    return "hello"


@app.route("/api/game/accesses", methods=['POST'])
def post_accesses():
    data = request.get_json()
    #print(data['uuid'])
    if data['uuid'] is None:
        print("error: no uuid")
    else:
        print("else")
        access = Access()
        access.uuid = data['uuid']
        access.created_at = datetime.now()
        g.session.add(access)
        g.session.commit()
    return "post"
