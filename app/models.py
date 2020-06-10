from flask_sqlalchemy import SQLAlchemy  # noqa

db = SQLAlchemy()


class Run(db.Model):
    __tablename__ = "runs"

    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    calories = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'))

    users = db.relationship('User', back_populates='runs')
    routes = db.relationship('Route', back_populates='runs')

    def to_dict(self):
        return {
            'id': self.id,
            'distance': self.distance,
            'time': self.time,
            'date': self.date,
            'calories': self.calories,
            'user_id': self.user_id,
            'route_id': self.route_id
        }


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

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'email': self.email,
            'weight': self.weight
        }
