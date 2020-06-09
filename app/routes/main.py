from flask import Blueprint, jsonify

bp = Blueprint('main', __name__, '')


@bp.route('/')
def main_page():
    response = "Hello World"
    return jsonify(message=response)
