import GRPC.protosImplantation.users_pb2_grpc as users_service
import GRPC.protosImplantation.users_types_pb2 as users_messages
import grpc
from functools import partial


def getUser(userId):
    channel = grpc.insecure_channel('localhost:50051')
    stub = users_service.UsersStub(channel)
    user = stub.GetUser(users_messages.User(id=userId))
    return user
