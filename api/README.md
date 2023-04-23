## API

### Description

Here we use FastAPI together with GRPC to communicate with other microservices.


### GRPC

- To generate files from `schema.proto`:

```
python -m grpc_tools.protoc --proto_path=./src/articles/grpc schema.proto --python_out=./src/articles/grpc --grpc_python_out=./src/articles/grpc
```
