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

from .views import usuario_view, sala_view, pergunta_view