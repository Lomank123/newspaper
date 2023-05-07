## API

### Description

Here we use FastAPI together with GRPC to communicate with other microservices.


### GRPC

- To generate files from `schema.proto`:

Note that both files must be in the root dir.

```
python -m grpc_tools.protoc --proto_path=./src/articles/grpc schema.proto --python_out=. --grpc_python_out=.
```
