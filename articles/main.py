from src.server import serve


def main():
    """Entrypoint. Run GRPC server and listen to incoming requests."""
    # TODO: Add logging here
    serve()


if __name__ == '__main__':
    main()
