### GRPC

- To generate files from `schema.proto`:

Note that both files must be in the root dir.

```
python -m grpc_tools.protoc --proto_path=./src/grpc schema.proto --python_out=. --grpc_python_out=.
```