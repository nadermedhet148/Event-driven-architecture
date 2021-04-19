from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@db:5432/Products"