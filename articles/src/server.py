import grpc
import schema_pb2_grpc as pb2_grpc
import schema_pb2 as pb2
from concurrent import futures


class ArticleServer(pb2_grpc.ArticlesServicer):
    """GRPC Server."""

    def GetServerResponse(self, request, context):
        # TODO: Think of an async grpc if possible
        # TODO: Use asyncpg to connect to dbs
        article_id = request.id
        result = {'title': f'Article id: {article_id}!'}
        return pb2.GetArticleResponse(**result)


def serve():
    """Run the GRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ArticlesServicer_to_server(ArticleServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
