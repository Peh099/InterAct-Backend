from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow

def minimal_app(config_class):
app = Flask(__name__)
app.config.from_object('config')
return app

def create_app(config_class=None):
app = minimal_app(config.DevConfig if config_class is None else config_class)
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
return app

from .views import usuario_view, sala_view, pergunta_view