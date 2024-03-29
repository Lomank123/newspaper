import logging
from typing import Any, Dict

import schema_pb2 as pb2
import schema_pb2_grpc as pb2_grpc
from fastapi import status
from fastapi.encoders import jsonable_encoder
from google.protobuf.json_format import MessageToDict
from grpc import aio
from grpc.aio import AioRpcError
from src.settings import GRPC_HOST, GRPC_PORT

logger = logging.getLogger(__name__)


class ArticleService:
    """Fetch article(s) from outer service."""

    def __init__(self) -> None:
        self.channel = aio.insecure_channel(f'{GRPC_HOST}:{GRPC_PORT}')
        self.stub = pb2_grpc.ArticlesStub(self.channel)

    def _build_data(
        self, data: Dict, status: int, error: Dict = dict()
    ) -> Dict[str, Any]:
        return {
            'error': error,
            'status': status,
            'data': data,
        }

    def _build_json(self, data: Dict) -> Any:
        """Return json encoded data."""
        return jsonable_encoder(data)

    async def close_channel(self) -> None:
        """Close `self.channel` gracefully."""
        logger.warning('Closing channel...')
        await self.channel.close()

    async def get_list(self) -> Dict:
        """Return list of articles."""
        error = dict()
        status_code = status.HTTP_200_OK
        data = dict()

        try:
            request = pb2.ArticleListRequest()
            response = await self.stub.ArticleListResponse(request)
            data = MessageToDict(response)
        except AioRpcError as e:
            logger.error(
                f'Error occured when trying to reach GRPC server ({e.code()}).'
                f' Details: {e.debug_error_string()}'
            )
            error['code'] = e.code()
            error['details'] = e.details()
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        except Exception as e:
            logger.error(str(e))
            error['details'] = str(e)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        data = self._build_data(data, status_code, error)
        return self._build_json(data)
