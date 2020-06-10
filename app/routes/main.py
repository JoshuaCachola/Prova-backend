from flask import Blueprint, jsonify
from ..models import db, Route
from flask_cors import cross_origin
from flask import Blueprint, jsonify, request

bp = Blueprint('main', __name__, url_prefix='')


@bp.route('/')
def main_page():
    return 'Hello World'


@bp.route('/users/<user_id>/routes')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_my_routes(user_id):
    my_routes = Route.query.filter(Route.creatorId == user_id).all()
    dict_routes = [route.to_dict() for route in my_routes]
    return jsonify(dict_routes)


@bp.route('/routes', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
def post_route():
    data = request.json
    new_route = Route(
        distance=data['distance'],
        average_time=data['averageTime'],
        best_time=data['bestTime'],
        coordinates=data['coordinates'],
        creatorId=data['creatorId']
    )
    db.session.add(new_route)
    db.session.commit()
    return jsonify(data)


@bp.route('/routes/<route_id>')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_a_route(route_id):
    route = Route.query.get(route_id)
    return jsonify(route.to_dict())
