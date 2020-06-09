from flask import Blueprint, jsonify, request
from ..auth import requires_auth
from flask_cors import cross_origin
from ..models import db, User

bp = Blueprint('users', __name__, url_prefix="")


@bp.route('/users')
@cross_origin(headers=["Content-Type", "Authorization"])
def user():
    users = User.query.all()
    for user in users:
        print(f"{user}")
    return jsonify("hello")


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
        new = {"userId": new_user.id, "email": new_user.email, "username": new_user.username}
        return new
