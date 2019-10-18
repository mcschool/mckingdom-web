import json
from flask import Blueprint, g, request, jsonify
from app.models import Player, Access
from datetime import datetime, timedelta
from sqlalchemy import desc

app = Blueprint('game_player', __name__)


@app.route("/api/game/players/my_ranking", methods=['POST'])
def post_players_myranking():
    data = request.get_json()
    p = g.session.query(Player).filter(
        Player.uuid == data['uuid']
    ).first()
    more_logincount = g.session.query(Player).filter(
        Player.login_count > p.login_count
    ).count()
    all_playercount = g.session.query(Player).count()
    ranking = more_logincount + 1
    response = {
        "total_players": all_playercount,
        "my_ranking": ranking,
        "login_count": p.login_count
    }
    return jsonify(response)


@app.route("/api/game/players", methods=['POST'])
def post_players():
    data = request.get_json()
    day = datetime.now() - timedelta(days = 1)
    if data['uuid'] is None:
        return("error: no uuid")
    #データをGET
    p = g.session.query(Player).filter(
        Player.uuid == data['uuid'],
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
    access = Access()
    access.uuid = data['uuid']
    access.created_at = datetime.now()
    g.session.add(access)
    g.session.commit()

    p = g.session.query(Player).filter(
        Player.uuid == data['uuid'],
    ).first()

    if p.last_login_at < day:
        p.money = p.money + 1
        g.session.commit()
    else:
        pass

    return jsonify(p.as_dict())


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


@app.route("/api/game/pvp/kill", methods=['PUT'])
def put_player_kill():
    data = request.get_json()
    if data.get('uuid') is None:
        return "error: no uuid"
    player = g.session.query(Player).filter(
        data.get('uuid') == Player.uuid
    ).first()
    player.pvp_total_kills = player.pvp_total_kills + 1
    if player.pvp_max_kill_streaks < data.get('kill_streak'):
        player.pvp_max_kill_streaks = data.get('kill_streak')
    g.session.add(player)
    g.session.commit()
    return "success"


@app.route("/api/admin/pvp/kill/total/rank", methods=['GET'])
def get_player_pvp_kill_rank():
    order_kills = g.session.query(Player).order_by(
        desc(Player.pvp_total_kills)
    ).all()
    data = []
    for player in order_kills:
        data.append(player.as_dict())
    return jsonify(data)
