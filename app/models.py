from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Route(db.Model):
    __tablename__ = 'routes'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    average_time = db.Column(db.Integer)
    best_time = db.Column(db.Integer)
    coordinates = db.Column(db.Text, nullable=False)
    creatorId = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)

    creator = db.relationship('User', back_populates='routes')


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    weight = db.Column(db.Integer)

    routes = db.relationship('Route', back_populates='creator')
