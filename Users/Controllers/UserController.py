from config.flask_app import app
from flask import Blueprint
from flask import request
from models.User import User
from config.db import db
from messages.publish import publish
from Commands.UserCreated import UserCreated


UserController = Blueprint('UserController', __name__,
                        template_folder='templates')

@UserController.route('/',methods=['POST'])
def createUser():
    body = request.get_json()
    user = User(name=body.get('name'))
    db.session.add(user)
    db.session.commit()
    publish('events.usrs.created' , UserCreated(user.name, user.id).to_string() )
    return {
        "success": True,
    }

