import asyncio
import time
import math
import logging
from typing import AsyncIterable, Iterable

import grpc

from GRPC.protosImplantation.products_pb2_grpc import add_ProductsServicer_to_server
from GRPC.Service.ProductService import ProductService

async def serve() -> None:
    server = grpc.aio.server()
    add_ProductsServicer_to_server(
        ProductService(), server)
    server.add_insecure_port('[::]:50052')
    await server.start()
    await server.wait_for_termination()


def startServer():
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(serve())