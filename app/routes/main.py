from flask import Blueprint

bp = Blueprint('main', __name__, '')


@bp.route('/')
def main_page():
    return 'Hello World'
