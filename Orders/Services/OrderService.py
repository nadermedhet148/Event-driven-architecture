from Models.Order import Order
from Config.db import db
from Messages.publish import publish
from Commands.CheckProductQuantity import CheckProductQuantity
from Commands.CheckUserBalance import CheckUserBalance


OrderStatus = {
    "AWAIT_PRODUCT_QUANTITY_CHECK" : "AWAIT_PRODUCT_QUANTITY_CHECK", 
    "AWAIT_USER_BALANCE_CHECK" : "AWAIT_USER_BALANCE_CHECK", 
    "REJECTED_PRODUCT_CANNOT_ACCEPT" : "REJECTED_PRODUCT_CANNOT_ACCEPT", 

    
}
    


class OrderService:
    def createOrder(self , productId , userId , quantity ):
        order = Order(
            userId= userId,
            productId= productId,
            totalQuantity= quantity ,
            status= OrderStatus['AWAIT_PRODUCT_QUANTITY_CHECK']
        )
        db.session.add(order)
        db.session.commit()
        command = CheckProductQuantity(order.id,order.productId,order.totalQuantity)
        publish('product/order_created' ,command.to_string())
        return order

    def handleProductRejectOrder(self , payload):
        order = Order.query.get(payload['orderId'])
        order.status = OrderStatus['REJECTED_PRODUCT_CANNOT_ACCEPT']
        db.session.add(order)
        db.session.commit()

    def handleProductAccpetOrder(self, payload):
        order = Order.query.get(payload['orderId'])
        order.status = OrderStatus['AWAIT_USER_BALANCE_CHECK']
        order.totalPrice = payload['price']
        db.session.add(order)
        db.session.commit()        
        command = CheckUserBalance(order.id,order.userId,order.totalPrice)
        publish('user/order_created' ,command.to_string())


