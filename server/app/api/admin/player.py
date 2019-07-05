import json
from flask import Blueprint, g, request
from app.models import Player

app = Blueprint('admin_player', __name__)


@app.route("/api/admin/players", methods=['GET'])
def get_players():
    test = [1, 2]
    return json.dumps(test)


@app.route("/api/admin/players/test", methods=['GET'])
def get_players_test():
    p = g.session.query(Player).filter(
        Player.id == 1
    ).first()
    print(p.as_dict())
    return json.dumps(p.as_dict())


@app.route("/api/admin/players", methods=['PATCH'])
def patch_players():
    data = request.get_json()
    if data['uuid'] is None:
        print("error: no uuid")
    else:
        p = g.session.query(Player).filter(
            Player.uuid == data['uuid']
        ).first()
        if p is None:
            print("いないから登録")
            player = Player()
            player.uuid = data['uuid']
            player.name = data['name']
            g.session.add(player)
            g.session.commit()
        else:
            p.login_count = p.login_count + 1
            g.session.commit()
            if p.name == data['name']:
                pass
            else:
                p.name = p.name = data['name']
                g.session.commit()

    return "bye bye"


@app.route("/api/admin/players", methods=['POST'])
def post_players():
    return "yo"
