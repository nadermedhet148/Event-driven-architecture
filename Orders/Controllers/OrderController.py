from Config.flask_app import app
from flask import Blueprint
from flask import request
from Models.Order import Order
from Config.db import db
from GRPC.Requests import getUser , getProduct
from Messages.publish import publish
from Events.income.OrderCreated import OrderCreated
from flask.json import jsonify

OrderController = Blueprint('OrderController', __name__,
                        template_folder='templates')

@OrderController.route('/',methods=['POST'])
def createOrder():
    body = request.get_json()
    product = getProduct(body.get('productId'))
    user = getUser(body.get('userId'))

    order = Order(
        userId= user.id,
        productId= product.id,
        totalPrice= body.get('quantity') * product.price,
        totalQuantity= body.get('quantity') ,
    )
    db.session.add(order)
    db.session.commit()
    event = OrderCreated(
            order.id,
            order.userId,
            order.productId,
            order.totalPrice,
            order.totalQuantity
            )
    publish(
        'order_created' ,
        event.to_string()
        )

    return jsonify({
        "success": True,
        "data": order.toDict()
    })