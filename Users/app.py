from config.db import db
from config.flask_app import app
from flask_migrate import Migrate
from Controllers.UserController import UserController 

from models.User import User

migrate = Migrate(app, db)

app.register_blueprint(UserController)
