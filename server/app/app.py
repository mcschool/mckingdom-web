from flask import Flask, g
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from .db import get_database_engine

import app.api.health as health
from app.api.game import (
    player as game_player,
    access as game_access,
    world as game_world,
    athletic_completed_players as game_athletic_completed_players,
    command as game_command, messages as game_messages
)
from app.api.admin import (
    player as admin_player,
    access as admin_access,
    message as admin_message,
    world as admin_world,
    athletic_course as admin_athletic_course,
    topic as admin_topic,
)
from app.api.web import (
    player as web_player,
    world as web_world,
    topic as web_topic,
)

application = Flask(__name__)
apps = [
    health.app,

    game_player.app,
    game_access.app,
    game_world.app,
    game_athletic_completed_players.app,
    game_command.app,
    game_messages.app,

    admin_player.app,
    admin_access.app,
    admin_message.app,
    admin_world.app,
    admin_athletic_course.app,
    admin_topic.app,

    web_player.app,
    web_world.app,
    web_topic.app,
]
for app in apps:
    application.register_blueprint(app)

CORS(application)



@application.before_request
def before_request():
    engine = get_database_engine()
    _sessionmaker = sessionmaker(bind=engine)
    g.session = _sessionmaker()


@application.after_request
def after_request(response):
    g.session.commit()
    g.session.close()
    response.headers["Cache-Control"] = "no-cache"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = -1
    return response
