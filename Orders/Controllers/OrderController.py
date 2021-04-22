from Config.flask_app import app
from flask import Blueprint
from flask import request
from Models.Order import Order
from Config.db import db
from GRPC.Requests import getUser , getProduct
from flask.json import jsonify
from Services.OrderService import OrderService

OrderController = Blueprint('OrderController', __name__,
                        template_folder='templates')

@OrderController.route('/',methods=['POST'])
def createOrder():
    body = request.get_json()
    
    service = OrderService()

    order = service.createOrder(body.get('productId'), body.get('userId') ,  body.get('quantity'))

    return jsonify({
        "success": True,
        "data": order.toDict()
    })