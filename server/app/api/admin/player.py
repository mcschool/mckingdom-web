import json
from datetime import datetime, timedelta
from flask import Blueprint, g, request, jsonify
from app.models import Player
from sqlalchemy import desc

app = Blueprint('admin_player', __name__)


@app.route("/api/admin/players", methods=['GET'])
def get_players():
    test = {"a": 1}
    return jsonify(test)


@app.route("/api/admin/players/test", methods=['GET'])
def get_players_test():
    p = g.session.query(Player).filter(
        Player.id == 1
    ).first()
    response = json.dumps(p.as_dict())
    return jsonify(response)


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


@app.route("/api/admin/players/<id>/role", methods=['PUT'])
def put_player_role(id=None):
    data = request. get_json()
    p = g.session.query(Player).filter(Player.id == id).first()
    if p is None:
        return "not found"
    else:
       p.role = data.get("role")
       p.updated_at = datetime.now()
       g.session.commit()
    return "success"


@app.route("/api/admin/players/admin", methods=['GET'])
def get_player_admin():
    players = g.session.query(Player).filter(Player.role == "admin").all()
    response = []
    for player in players:
        response.append(player.as_dict())
    return jsonify(response)


@app.route("/api/admin/players/loginInfo", methods=['GET'])
def get_player_loginInfo():
    week = datetime.now() - timedelta(days = 7)
    month = datetime.now() - timedelta(days = 30)
    thisWeek = g.session.query(Player).filter(
        Player.last_login_at > week
    ).count()
    thisMonth = g.session.query(Player).filter(
        Player.last_login_at > month
    ).count()
    thisAll = g.session.query(Player).filter().count()
    thisBounceBack = g.session.query(Player).filter(
        Player.login_count == 1
    ).count()
    data = {
        "thisWeek": thisWeek,
        "thisMonth": thisMonth,
        "all": thisAll,
        "bounceBack": thisBounceBack
    }
    return jsonify(data)


@app.route("/api/admin/pvp/kill/total/rank", methods=['GET'])
def get_player_pvp_kill_rank():
    order_kills = g.session.query(Player).order_by(
        desc(Player.pvp_total_kills)
    ).all()
    print("=====")
    for player in order_kills:
        print(player.name, player.pvp_total_kills)
    print("=====")
    return "success"
