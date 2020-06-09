from flask import Blueprint, jsonify
from ..models import Route
from flask_cors import cross_origin
from flask import Blueprint, jsonify, request
<< << << < HEAD
== == == =
>>>>>> > a46d7a84604d3be3b3eb8c6e72f3eee76ad623cf

bp = Blueprint('main', __name__, url_prefix='')


@bp.route('/')
def main_page():
    return 'Hello World'


@bp.route('/users/<user_id>/routes')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_my_routes(user_id):
    my_routes = Route.query.filter(Route.creatorId == user_id).all()
    return jsonify(my_routes)


@bp.route('/routes', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
def post_route():
    data = request.json
    print(data)
    return jsonify(data)
