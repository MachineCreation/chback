from flask import Flask
from config import config
from app.authentication.routes import auth
from app.api.routes import graf

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder

app = Flask(__name__)
CORS(app, allow_headers= "x-access-token, content-type")

app.register_blueprint(auth)
app.register_blueprint(graf)

app.json_encoder = JSONEncoder
app.config.from_object(config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)
