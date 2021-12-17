#!/usr/bin/env python3

from setuptools import setup

author = "liweizhao"

setup(
    name="kv.proto",
    version="1.1",
    author=author,
    author_email="{}@antiy.cn".format(author),
    url="https://code.avlyun.org/grpc/kv-storage",
    py_modules=["kv_pb2", "kv_pb2_grpc"],
    install_requires=["grpcio>=1.33", "protobuf>=3.13"],
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3",
    ],
)

# $ ./setup.py sdist bdist_wheel
# $ twine upload dist/fsmhub-xxx
