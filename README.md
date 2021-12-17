# kv-storage

kv storage  protocol buffer file

Compile:

```
protoc --go_out=plugins=grpc:. kv.proto
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. kv.proto
```

Usage:

Golang

```go
import pb "code.avlyun.org/grpc/kv-storage"
```

Python

```sh
pip install https://code.avlyun.org/grpc/kv-storage/-/archive/master/kv-storage-master.zip
```

```py
import kv_pb2
import kv_pb2_grpc
```
