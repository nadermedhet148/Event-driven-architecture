from Models.Order import Order
from Config.db import db
from Messages.publish import publish
from Commands.CheckProductQuantity import CheckProductQuantity

OrderStatus = {
    "AWAIT_USER_BALANCE_CHECK" : "AWAIT_USER_BALANCE_CHECK"
}
    


class OrderService:
    def createOrder(self , productId , userId , quantity ):
        order = Order(
            userId= userId,
            productId= productId,
            totalQuantity= quantity ,
            status= OrderStatus['AWAIT_USER_BALANCE_CHECK']
        )
        db.session.add(order)
        db.session.commit()
        event = CheckProductQuantity(
                order.id,
                order.productId,
                order.totalQuantity
                )
        publish(
            'product/order_created' ,
            event.to_string()
            )
        return order
