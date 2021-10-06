from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config.from_object('config')

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

def minimal_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    return app


def create_app(config_class=None):
    app = minimal_app(config.DevConfig if config_class is None else config_class)
    database.init_app(app)
    migrate.init_app(app)
    controller.init_app(app)
    auth.init_app(app)
    cors.init_app(app)
    schemas.init_app(app)
    seed.init_app(app)
    email.init_app(app)
    swagger.init_app(app)
    return app

from .views import usuario_view, sala_view, pergunta_view