from Config.flask_app import app
from flask import Blueprint
from flask import request
from Models.User import User
from Config.db import db
from Messages.publish import publish
from Events.outcome.UserCreated import UserCreated


UserController = Blueprint('UserController', __name__,
                        template_folder='templates')

@UserController.route('/',methods=['POST'])
def createUser():
    body = request.get_json()
    user = User(name=body.get('name'))
    db.session.add(user)
    db.session.commit()
    publish('events.users.created' , UserCreated(user.name, user.id).to_string() )
    return {
        "success": True,
        "data": user.toDict()
    }


@UserController.route('/<userId>',methods=['GET'])
def getUser(userId):
    user = User.query.get(userId)
    return {
        "success": True,
        "data": user.toDict()
    }

