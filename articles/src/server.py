import grpc
import src.grpc.schema_pb2_grpc as pb2_grpc
import src.grpc.schema_pb2 as pb2
from concurrent import futures


class ArticleServer:
    """GRPC Server."""
    # TODO: Implement


def serve():
    """Run the GRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(ArticleServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
