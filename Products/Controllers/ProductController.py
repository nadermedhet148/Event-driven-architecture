from config.flask_app import app
from flask import Blueprint
from flask import request
from models.Product import Product
from config.db import db
from messages.publish import publish


ProductController = Blueprint('ProductController', __name__,
                        template_folder='templates')

@ProductController.route('/',methods=['POST'])
def createUser():
    body = request.get_json()
    product = Product(name=body.get('name'),price=body.get('price'))
    db.session.add(product)
    db.session.commit()
    return {
        "success": True,
    }

