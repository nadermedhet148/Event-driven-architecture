from config.db import db
from config.flask_app import app
from flask_migrate import Migrate
from Controllers.OrderController import OrderController 


migrate = Migrate(app, db)

app.register_blueprint(OrderController)
