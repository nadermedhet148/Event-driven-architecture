from config.db import db
from models.User import User



db.session.add(User(username="Flask", email="example@example.com"))
db.session.commit()

users = User.query.all()