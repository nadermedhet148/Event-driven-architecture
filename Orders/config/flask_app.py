from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/Orders"