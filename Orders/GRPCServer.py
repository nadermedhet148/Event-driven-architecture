import asyncio
import time
import math
import logging
from typing import AsyncIterable, Iterable

import grpc

from GRPC.protosImplantation.users_pb2_grpc import add_UsersServicer_to_server
from GRPC.Service.UserService import UserService

async def serve() -> None:
    server = grpc.aio.server()
    add_UsersServicer_to_server(
        UserService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(serve())