from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app) #Conectando o bando de dados à aplicação Flask
ma = Marshmallow(app) #Criando uma instancia para serialização/desserialização
migrate = Migrate(app, db)
api = Api(app)

from.views import socio_views
from.models import socio_model