from config.flask_app import app
from flask import Blueprint
from flask import request
from models.Order import Order
from config.db import db
from GRPC.Requests import getUser


OrderController = Blueprint('OrderController', __name__,
                        template_folder='templates')

@OrderController.route('/',methods=['POST'])
def createUser():
    body = request.get_json()
    user = getUser(100)
    print(user)
    # db.session.add(user)
    # db.session.commit()
    return {
        "success": True,
        "data":""
    }


