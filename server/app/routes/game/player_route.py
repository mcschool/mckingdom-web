from flask_restful import Resource


class GamePlayerRoute(Resource):

    def get(self):
        return {'t': 'GET: /api/game/players'}

    def post(self):
        return {'t': 'POST: /api/game/players'}
