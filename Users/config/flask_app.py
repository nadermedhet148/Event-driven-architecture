from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@127.0.0.1:5432/Users"