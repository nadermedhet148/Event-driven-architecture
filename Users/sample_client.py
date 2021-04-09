import GRPC.protosImplantation.users_pb2_grpc as users_service
import  GRPC.protosImplantation.users_types_pb2 as users_messages
import GRPC.Service.UserService as UserService
import grpc
from functools import partial


def getUser(stub):
    user = stub.GetUser(users_messages.User(id=2))
    print(user.id , user.name)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_service.UsersStub(channel)
        print("-------------- GetFeature --------------")
        getUser(stub)



if __name__ == '__main__':
    run()