from flask_restful import Resource
from flask import g, request
from ...models import Player


class GamePlayerRoute(Resource):

    def get(self):
        return {'t': 'GET: /api/game/players'}

    def post(self):
        data = request.get_json()
        session = g.session
        player = Player()
        player.name = "aaaa"
        player.uuid = "xxxx"
        session.add(player)
        session.commit()

        print(data)

        return {'t': 'POST: /api/game/players'}

    def patch(self):
        data = request.get_json()
        print(data)
        return {'t': 'PATCH: /api/game/players'}
