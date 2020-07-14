# -*- coding: utf-8 -*-

import msgpack


def default(obj):
    if isinstance(obj, int):
        return msgpack.ExtType(0, obj.to_bytes(32, "big"))

    raise TypeError(f"Unknown type: {obj}")


def ext_hook(code: int, data: bytes):
    if code == 0:
        return int.from_bytes(data, "big")

    return msgpack.ExtType(code, data)


class Person:
    def __init__(self):
        self.name = "hello"
        self.age = 10


def test_int_overflow():
    expected = [
        5 * 10 ** 23,
        100
    ]

    data: bytes = msgpack.packb(expected, default=default, use_bin_type=True)
    print(data.hex())
    ret: list = msgpack.unpackb(data, ext_hook=ext_hook, raw=False)
    assert ret == expected


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

    test_int_overflow()


if __name__ == '__main__':
    main()
