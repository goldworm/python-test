# -*- coding: utf-8 -*-

import msgpack


class Person:
    def __init__(self):
        self.name = "hello"
        self.age = 10


def main():
    data = [
        10,
        "hello",
        b"world",
        [
            {"name": "goldworm", "age": 30},
            {"name": "watch", "price": 100, "wallet": [0, 1, 2]},
        ]
    ]
    ret = msgpack.packb(data)
    print(ret.hex())

    data2 = msgpack.unpackb(ret)
    assert data == data2


if __name__ == '__main__':
    main()
