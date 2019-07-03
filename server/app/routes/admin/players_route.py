from flask_restful import Resource


class AdminPlayerRoute(Resource):

    def get(self):
        return {'aa': 1}
