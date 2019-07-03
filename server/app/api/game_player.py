from flask import Blueprint, g, request
from ..models import Player

app = Blueprint('game_player', __name__)


@app.route("/api/game/players", methods=['GET'])
def get_players():
    return "hello"


@app.route("/api/game/players", methods=['PATCH'])
def patch_players():
    data = request.get_json()
    if data['uuid'] is None:
        print("error: no uuid")
    else :
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


@app.route("/api/game/players", methods=['POST'])
def post_players():
    return "yo"


@app.route("/api/game/players", methods=['PUT'])
def put_players():
    return "no"


@app.route("/api/game/players", methods=['DELETE'])
def delete_players():
    return "yes"


@app.route("/api/game/players/<uuid>", methods=['GET'])
def get_player(uuid=None):
    print("=============")
    print(uuid)
    print("=============")
    if(uuid == "1234"):
        print("ok")
    else :
        print("failed")

    return "GET: /api/game/players/<uuid>"


@app.route("/api/game/players/<uuid>/password", methods=['PATCH'])
def patch_password(uuid=None):
    print("=============")
    print(uuid + " change_password")
    print("=============")
    return "GET: /api/game/players/<uuid>/password"


@app.route("/api/game/players/<uuid>/email", methods=['PATCH'])
def patch_email(uuid=None):
    print("=============")
    print(uuid + " change_email")
    print("=============")
    return "GET: /api/game/players/<uuid>/email"


@app.route("/api/game/players/<uuid>", methods=['DELETE'])
def delete_player(uuid=None):
    print("=============")
    print(uuid + " delete_player")
    print("=============")
    return "GET: /api/game/players/<uuid>"
