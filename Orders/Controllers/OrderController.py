from config.flask_app import app
from flask import Blueprint
from flask import request
from models.Order import Order
from config.db import db
from GRPC.Requests import getUser , getProduct
from messages.publish import publish
from Commands.OrderCreated impoaddrt OrderCreated

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
    publish(
        'events.order.created' ,
        OrderCreated(
            order.id,
            order.userId,
            order.productId,
            order.totalPrice,
            order.totalQuantity
            ).to_string()
        )

    return {
        "success": True,
        "data":order.toDict()
    }


