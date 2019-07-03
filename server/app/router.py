from flask import make_response
from flask_restful import Api
from . import application
from .routes import GamePlayerRoute, AdminPlayerRoute

api = Api(application)

# Game
api.add_resource(GamePlayerRoute,  '/api/game/players')

# Admin
api.add_resource(AdminPlayerRoute, '/api/admin/players')

