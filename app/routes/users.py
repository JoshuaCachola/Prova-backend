from flask import Blueprint, jsonify, request
from sqlalchemy import and_
from ..auth import requires_auth
from flask_cors import cross_origin
from ..models import db, User, Run, Route, PersonalRouteStat


bp = Blueprint('users', __name__, url_prefix="")


@bp.route('/users')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_users():
    users = User.query.all()
    all_users = []
    for user in users:
        all_users.append(user.to_dict())
    return jsonify(all_users)


@bp.route('/users/<user_id>')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_user():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    return jsonify(user)


@bp.route('/users', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
def create_user():
    data = request.json
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        existing_user.nickname = data['username']
        existing_user.email = data['email']
        return jsonify({"userId": existing_user.id, "username": existing_user.nickname, "email": existing_user.email})
    else:
        new_user = User(email=data['email'], username=data['username'])
        db.session.add(new_user)
        db.session.commit()
        new = {"userId": new_user.id, "email": new_user.email,
               "username": new_user.username}
        return new


@bp.route('/users/<int:user_id>/runs')
@cross_origin(headers=['Content-Type', 'Authorization'])
def get_runs(user_id):
    queried_runs = Run.query.filter_by(user_id=user_id).order_by(Run.date)
    runs = [run.to_dict() for run in queried_runs]
    return jsonify(runs)


@bp.route('/users/<int:user_id>/runs', methods=['POST'])
@cross_origin(headers=['Content-Type', 'Authorization'])
def add_run(user_id):
    data = request.json
    time = data['time'].split("'")
    convert_time = (int(time[0]) * 60) + int(time[1]) if len(time) > 1 else int(time[0] * 60)  # noqa
    new_run = Run(date=data['date'],
                  distance=data['distance'],
                  time=convert_time,
                  calories=data['calories'],
                  user_id=user_id,
                  route_id=data['routeId'])
    db.session.add(new_run)
    db.session.commit()

    route_for_run = Route.query.filter(Route.id == new_run.route_id).first()

    if not route_for_run.best_time:
        route_for_run.best_time = new_run.time
    elif new_run.time < route_for_run.best_time:
        route_for_run.best_time = new_run.time
    route_for_run.total_number_of_runs += 1

    if not route_for_run.average_time:
        route_for_run.average_time = new_run.time
    else:
        new_average = (route_for_run.average_time * (route_for_run.total_number_of_runs -
                                                     1) + new_run.time) / route_for_run.total_number_of_runs
        route_for_run.average_time = new_average
    db.session.add(route_for_run)

    personal_route_stats = PersonalRouteStat.query.filter(and_(
        PersonalRouteStat.user_id == user_id, PersonalRouteStat.route_id == new_run.route_id)).first()

    if not personal_route_stats.best_time:
        personal_route_stats.best_time = new_run.time
    elif new_run.time < personal_route_stats.best_time:
        personal_route_stats.best_time = new_run.time
    personal_route_stats.number_of_runs += 1

    if not personal_route_stats.average_time:
        personal_route_stats.average_time = new_run.time
    else:
        new_average = (personal_route_stats.average_time * (personal_route_stats.number_of_runs -
                                                            1) + new_run.time) / personal_route_stats.number_of_runs
        personal_route_stats.average_time = new_average

    db.session.add(personal_route_stats)

    db.session.commit()
    # new_run = new_run.to_dict()
    # return new_run
