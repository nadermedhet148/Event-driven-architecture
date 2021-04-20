from GRPC.protosImplantation.products_pb2_grpc import ProductsServicer
import GRPC.protosImplantation.products_pb2 as Products_types_pb2

import Models.Product as ProductModel

class ProductService(ProductsServicer):

    def GetProduct(self, request, context):
        product = ProductModel.Product.query.get(request.id)
        return Products_types_pb2.Product(
            name=product.name,
            id=product.id ,
            price=product.price ,
            quantity=product.quantity
            )
        
