from src.server import serve
import logging


logger = logging.getLogger(__name__)


def main():
    """Entrypoint. Run GRPC server and listen to incoming requests."""
    logger.warning('Starting GRPC server...')
    serve()


if __name__ == '__main__':
    main()
