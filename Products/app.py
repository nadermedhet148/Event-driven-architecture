from Config.db import db
from Config.flask_app import app
from Controllers.ProductController import ProductController 
import threading
from GRPCServer import startServer

app.register_blueprint(ProductController)

def runApp():
    app.run(port=5100)

if __name__ == '__main__':

    t2 = threading.Thread(target=runApp)
    t2.start()
    startServer()
    
