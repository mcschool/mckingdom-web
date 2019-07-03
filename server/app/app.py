from flask import Flask, session, g, request
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from .db import get_database_engine

application = Flask(__name__)
CORS(application, send_wildcard=application.debug)


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
