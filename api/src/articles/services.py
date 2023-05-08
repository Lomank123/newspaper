import schema_pb2_grpc as pb2_grpc
import schema_pb2 as pb2
from grpc import aio
from google.protobuf.json_format import MessageToDict
from typing import Dict
import logging

logger = logging.getLogger(__name__)


class ArticleService:
    """Fetch article(s) from outer service."""

    def __init__(self):
        # TODO: Move to consts
        self.host = 'localhost'
        self.port = 50051

        self.channel = aio.insecure_channel(f'{self.host}:{self.port}')
        self.stub = pb2_grpc.ArticlesStub(self.channel)

    async def __aexit__(self, *excinfo):
        """Close grpc connection when the job is done or exception raised."""
        # TODO: Test this (for now in api no logs appeared)
        logger.warning('Closing channel...')
        await self.channel.close()

    async def get_list(self, **kwargs) -> Dict:
        """Return list of articles."""
        request = pb2.ArticleListRequest()
        response = await self.stub.ArticleListResponse(request)
        return {'data': MessageToDict(response)}
