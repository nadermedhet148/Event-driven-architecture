from Config.db import db
from Config.flask_app import app
from Controllers.ProductController import ProductController 
import threading
from GRPCServer import startServer
from Messages.listeners.OrderCreatedConsumer import orderCreatedConsumer 
from Messages.listeners.OrderRollBackedConsumer import orderRollBackedConsumer 


app.register_blueprint(ProductController)

def runApp():
    app.run(port=5100)

if __name__ == '__main__':
    t1 = threading.Thread(target=orderCreatedConsumer)
    t1.start()
    t3 = threading.Thread(target=orderRollBackedConsumer)
    t3.start()
    t2 = threading.Thread(target=runApp)
    t2.start()
    startServer()
    
