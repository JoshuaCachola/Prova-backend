from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Run(db.Model):
    __tablename__ = "runs"

    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float)
    time = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    calories = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    route_id = db.Column(db.Integer, db.ForeignKey('routes'))

    users = db.relationship('User', back_populates='runs')
    routes = db.relationship('Route', back_populates='runs')
