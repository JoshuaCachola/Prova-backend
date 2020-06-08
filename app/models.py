from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Route(db.Model):
    __tablename__ = 'routes'

    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Float, nullable=False)
    average_time = db.Column(db.Integer)
    best_time = db.Column(db.Integer)
    coordinates = db.Column(db.Text, nullable=False)
    creatorId = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
