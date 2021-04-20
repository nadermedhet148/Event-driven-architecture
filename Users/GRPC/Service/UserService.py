from GRPC.protosImplantation.users_pb2_grpc import UsersServicer
import GRPC.protosImplantation.users_types_pb2 as users_types_pb2

import Models.User as UserModel

class UserService(UsersServicer):

    def GetUser(self, request, context):
        user = UserModel.User.query.get(request.id)
        return users_types_pb2.User(name=user.name, id=user.id)
        
