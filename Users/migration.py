from Config.db import db
from Config.flask_app import app
from flask_migrate import Migrate
from flask import Flask
from Models.User import User

migrate = Migrate(app, db)







