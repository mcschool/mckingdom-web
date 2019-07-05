from flask import Blueprint, g, request

app = Blueprint('admin_access', __name__)

@app.route("/api/admin/accesses/game", methods=['GET'])
def get_accesses():
    return "hello"

@app.route("/api/admin/accesses/game/<id>", methods=['GET'])
def post_accesses(id = None):
    return "get id"
