#!/usr/bin/env python3


import time
import grpc
from kv_pb2_grpc import KVStub
from kv_pb2 import *


def main():
    channel = grpc.insecure_channel('k8smiddlewan.avlyun.org:30051')
    stub = KVStub(channel)
    response = stub.Get(GetRequest(key='00', space="t_hash"))
    # print(response.value)
    t = time.time()
    for i in range(1000):
        rule = [
            RuleUnit(space="t_hash", index=0),
            RuleUnit(space="t_hash_2", index=1),
        ]
        queries = [
            Query(keys=['00', '00', ]),
        ]
        response = stub.Search(SearchRequest(rule=rule, queries=queries))
    print(response, time.time() - t)


if __name__ == '__main__':
    main()
