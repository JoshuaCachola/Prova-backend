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
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'))

    users = db.relationship('User', back_populates='runs')
    routes = db.relationship('Route', back_populates='runs')


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
    runs = db.relationship('Run', back_populates='routes')

    def to_dict(self):
        return {
            'id': self.id,
            'distance': self.distance,
            'average_time': self.average_time,
            'best_time': self.best_time,
            'coordinates': self.coordinates,
            'creatorId': self.creatorId
        }


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    weight = db.Column(db.Integer)

    routes = db.relationship('Route', back_populates='creator')
    runs = db.relationship('Run', back_populates='users')
