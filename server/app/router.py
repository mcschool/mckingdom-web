from flask import make_response
from flask_restful import Api
from . import application
from .routes import AdminPlayerRoute

api = Api(application)

#  Admin
api.add_resource(AdminPlayerRoute, '/api/admin/players')

