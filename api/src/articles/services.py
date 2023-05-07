import grpc
import schema_pb2_grpc as pb2_grpc
import schema_pb2 as pb2


class ArticleService:
    """Fetch article(s) from outer service."""

    def __init__(self):
        # TODO: Move to consts
        self.host = 'localhost'
        self.port = 50051

        self.channel = grpc.insecure_channel(f'{self.host}:{self.port}')
        self.stub = pb2_grpc.ArticlesStub(self.channel)

    def get_list(self, **kwargs):
        """Return list of articles."""

        request = pb2.GetArticleRequest(id=4)

        response = self.stub.GetServerResponse(request)
        return {'data': response.title}
