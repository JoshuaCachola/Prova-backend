from flask import Blueprint, jsonify
from sqlalchemy import and_
from ..models import db, Route, PersonalRouteStat
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


@bp.route('/users/<user_id>/latest_route')
@cross_origin(headers=["Content-Type", "Authorization"])
def latest_route(user_id):
    latest = Route.query.order_by(Route.id.desc()).first()
    return jsonify(latest.to_dict())


@bp.route('/routes', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
def post_route():
    data = request.json
    new_route = Route(
        distance=data['distance'],
        average_time=None,
        best_time=None,
        total_number_of_runs=0,
        coordinates=data['coordinates'],
        creatorId=data['creatorId']
    )
    db.session.add(new_route)
    db.session.commit()
    return jsonify(data)


@bp.route('/routes/<route_id>', methods=['PUT'])
@cross_origin(headers=["Content-Type", "Authorization"])
def get_a_route(route_id):
    data = request.json
    user_id = data['userId']
    route = Route.query.get(route_id)
    personal_stats_entry = PersonalRouteStat.query.filter(
        and_(PersonalRouteStat.route_id == route_id, PersonalRouteStat.user_id == user_id)).first()
    if personal_stats_entry:
        return jsonify(route.to_dict(), personal_stats_entry.to_dict())
    else:
        new_personal_stats_entry = PersonalRouteStat(
            route_id=route_id,
            user_id=user_id,
            best_time=0,
            average_time=0,
            number_of_runs=0
        )
        db.session.add(new_personal_stats_entry)
        db.session.commit()
        return jsonify(route.to_dict(), new_personal_stats_entry.to_dict())
