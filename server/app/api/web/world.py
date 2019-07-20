from flask import Blueprint, g, request, jsonify
from app.models import World

app = Blueprint('web_world', __name__)

