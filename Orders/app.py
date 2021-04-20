from config.db import db
from config.flask_app import app
from Controllers.OrderController import OrderController 
import threading


app.register_blueprint(OrderController)



def runApp():
    app.run(port=5300,host="0.0.0.0")

if __name__ == '__main__':

    t2 = threading.Thread(target=runApp)
    t2.start()
    
