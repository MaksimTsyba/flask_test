from flask import Flask
from flask_migrate import Migrate
from models import db
import config
import flask_sqlalchemy

migrate = Migrate()

def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    # db.create_all()
    migrate.init_app(flask_app, db)
    return flask_app