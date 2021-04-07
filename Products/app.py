from config.db import db
from config.flask_app import app
from flask_migrate import Migrate
from Controllers.ProductController import ProductController 

migrate = Migrate(app, db)

app.register_blueprint(ProductController)
