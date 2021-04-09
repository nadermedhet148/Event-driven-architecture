from config.flask_app import app
from flask import Blueprint
from flask import request
from models.Product import Product
from config.db import db
from messages.publish import publish


ProductController = Blueprint('ProductController', __name__,
                        template_folder='templates')

@ProductController.route('/',methods=['POST'])
def createProduct():
    body = request.get_json()
    product = Product(
        name=body.get('name'),
        price=body.get('price'),
        quantity=body.get('quantity')
        )
    db.session.add(product)
    db.session.commit()
    return {
        "success": True,
        'data' : product.toDict()
    }



@ProductController.route('/<productId>',methods=['GET'])
def getProduct(productId):
    product = Product.query.get(productId)
    return {
        "success": True,
        "data": product.toDict()
    }

