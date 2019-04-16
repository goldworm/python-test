# -*- coding: utf-8 -*-

import socket
import time
from enum import IntEnum

import msgpack


class MessageType(IntEnum):
    NONE = -1
    VERSION = 0
    CLAIM = 1
    QUERY = 2
    CALCULATE = 3
    COMMIT_BLOCK = 4


def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = "/tmp/iiss.sock"
    block_height: int = 100

    try:
        sock.connect(server_address)

        unpacker = msgpack.Unpacker(raw=True)

        while True:
            print("Reading...")
            data: bytes = sock.recv(1024)
            print(f"S -> C: {data.hex()}")
            if len(data) == 0:
                break

            unpacker.feed(data)

            for request in unpacker:
                print(f"request: {request}")

                msg_type: int = request[0]

                payload = request[2]
                if isinstance(payload, list):
                    print(f"payload: {payload}")
                else:
                    print(f"payload: {payload.hex()}")

                time.sleep(1)

                if msg_type == MessageType.QUERY:
                    data: bytes = handle_query(request, block_height)

                sock.send(data)
                print(f"C -> S: {data.hex()}")

                block_height += 1
                print(f"block_height: {block_height}")

    except Exception as e:
        print(e)
    finally:
        sock.close()


def handle_query(request, block_height: int) -> bytes:
    msg_type: int = request[0]
    msg_id: int = request[1]
    address_bytes = request[2]
    iscore: int = 100
    payload = [address_bytes, iscore.to_bytes(1, 'big'), block_height]

    response = [msg_type, msg_id, payload]
    data: bytes = msgpack.dumps(response)

    return data


if __name__ == "__main__":
    print("start")
    main()
