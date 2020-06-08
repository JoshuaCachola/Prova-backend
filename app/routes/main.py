from flask import Blueprint, jsonify
from flask_cors import cross_origin, CORS
from .auth import AuthError, requires_auth

bp = Blueprint('main', __name__, '')


# @bp.route('/')
# @cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
# def main_page():
#     response = "Hello from a private endpoint! You need to be authenticated to see this."
#     return jsonify(message=response)

@bp.route('/')
def main():
    return "hello world"
