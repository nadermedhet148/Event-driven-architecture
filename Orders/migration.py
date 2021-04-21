from Config.db import db
from Config.flask_app import app
from flask_migrate import Migrate
from flask import Flask
from Models.Order import Order

migrate = Migrate(app, db)







