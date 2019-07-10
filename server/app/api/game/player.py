from flask import Blueprint, g, request
from app.models import Player
from datetime import datetime

app = Blueprint('game_player', __name__)


@app.route("/api/game/players", methods=['GET'])
def get_players():
    return "hello"


@app.route("/api/game/players", methods=['PATCH'])
def patch_players():
    data = request.get_json()
    if data['uuid'] is None:
        print("error: no uuid")
    else:
        #データをGET
        p = g.session.query(Player).filter(
            Player.uuid == data['uuid']
        ).first()
        if p is None:
            print("いないから登録")#INSERT
            player = Player()
            player.uuid = data['uuid']
            player.name = data['name']
            g.session.add(player)
            g.session.commit()
        else:
            p.login_count = p.login_count + 1
            p.last_login_at = datetime.now()
            g.session.commit()
            if p.name == data['name']:
                pass
            else:
                p.name = p.name = data['name']
                g.session.commit()

    return "success"


"""
@app.route("/api/game/players/last_login", methods=['PATCH'])
def patch_player_last_login():
    data = request.get_json()
    print(data['uuid'])
    if data['uuid']is None:
        return "error: no uuid"
    player = g.session.query(Player).filter(
        Player.uuid == data['uuid']
    ).first()
    print(player)
    if player is None:
        p = Player()
        p.uuid = data['uuid']
        p.name = data['name']
        p.created_at = datetime.now()
        p.update_at = datetime.now()
        p.last_login_at = datetime.now()
        g.session.add(p)
        g.session.commit()
    else:
        player.last_login_at = datetime.now()
        g.session.commit()
    return "success"
"""


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
    else:
        print("failed")

    return "GET: /api/game/players/<uuid>"


@app.route("/api/game/players/<uuid>/password", methods=['PATCH'])
def patch_password(uuid=None):
    data = request.get_json()
    if data['uuid'] is None:
        print("error: no uuid")
    else:
        p = g.session.query(Player).filter(
            Player.uuid == data['uuid']
        ).first()
        if p is None:
            pass
        else:
            if p.password == data['password']:
                pass
            else:
                print("isalnum")
                if (len(data['password'])) <= 4 and data['password'].encode('utf-8').isalnum():
                    print("パスワードは4文字以上でお願いします.")
                    print("パスワードは英語のみでお願いします.")
                else:
                    p.password = data['password']
                    g.session.commit()

    return "GET: /api/game/players/<uuid>/password"

# EMAIL変更
@app.route("/api/game/players/<uuid>/email", methods=['PATCH'])
def patch_email(uuid=None):
    data = request.get_json()
    if data['uuid'] is None:
        print("error: no uuid")
    else:
        p = g.session.query(Player).filter(
            Player.uuid == data['uuid']
        ).first()
        if p is None:
            pass
        else:
            #データをUPDATE
            if p.email == data['email']:
                pass
            else:
                p.email= data['email']
                g.session.commit()
    return "GET: /api/game/players/<uuid>/email"


@app.route("/api/game/players/<uuid>", methods=['DELETE'])
def delete_player(uuid=None):
    print("=============")
    print(uuid + " delete_player")
    print("=============")
    return "GET: /api/game/players/<uuid>"
