from config.db import db
from config.flask_app import app
from flask_migrate import Migrate
from flask import Flask
from models.Order import Order

migrate = Migrate(app, db)







