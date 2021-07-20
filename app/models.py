import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class User(db.Model):
    """ Model for cars """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    login = db.Column(db.String(100))
    password = db.Column(db.String(100))
    type = db.Column(db.Integer)
    requests = db.relationship('Request', backref='user', lazy=True)


class Request(db.Model):
    """ Model for requests """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)