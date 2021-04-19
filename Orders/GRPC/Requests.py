import GRPC.protosImplantation.users_pb2_grpc as users_service
import GRPC.protosImplantation.users_types_pb2 as users_messages
import GRPC.protosImplantation.products_pb2_grpc as products_service
import GRPC.protosImplantation.products_pb2 as products_messages
import grpc
from functools import partial


def getUser(userId):
    channel = grpc.insecure_channel('users-service:50051')
    stub = users_service.UsersStub(channel)
    user = stub.GetUser(users_messages.User(id=userId))
    return user

def getProduct(userId):
    channel = grpc.insecure_channel('product-service:50052')
    stub = products_service.ProductsStub(channel)
    product = stub.GetProduct(products_messages.Product(id=userId))
    return product
