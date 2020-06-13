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
    name = db.Column(db.String)
    distance = db.Column(db.Float, nullable=False)
    average_time = db.Column(db.Integer)
    best_time = db.Column(db.Integer)
    coordinates = db.Column(db.Text, nullable=False)
    total_number_of_runs = db.Column(db.Integer, nullable=False)
    directions = db.Column(db.Text)
    image = db.Column(db.Text)
    creatorId = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)

    creator = db.relationship('User', back_populates='routes')
    runs = db.relationship('Run', back_populates='routes')
    personal_route_stats = db.relationship(
        'PersonalRouteStat', back_populates='route')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'distance': self.distance,
            'average_time': self.average_time,
            'best_time': self.best_time,
            'coordinates': self.coordinates,
            'total_number_of_runs': self.total_number_of_runs,
            'creatorId': self.creatorId,
            'directions': self.directions,
            'image': self.image
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
    personal_route_stats = db.relationship(
        'PersonalRouteStat', back_populates='user')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'weight': self.weight
        }


class PersonalRouteStat(db.Model):
    __tablename__ = 'personal_route_stats'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    best_time = db.Column(db.Integer)
    average_time = db.Column(db.Integer)
    number_of_runs = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'))

    route = db.relationship('Route', back_populates='personal_route_stats')
    user = db.relationship('User', back_populates='personal_route_stats')

    def to_dict(self):
        return {
            'id': self.id,
            'best_time': self.best_time,
            'average_time': self.average_time,
            'number_of_runs': self.number_of_runs,
            'user_id': self.user_id,
            'route_id': self.route_id
        }
