# -*- coding: utf-8 -*-

import socket
import time

from iiss.utils.msgpack_for_ipc import MsgPackForIpc


def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = "/tmp/iiss.sock"
    block_height: int = 100
    iscore: int = 5

    try:
        sock.connect(server_address)

        while True:
            data: bytes = sock.recv(1024)
            print(f"S -> C: {data.hex()}")
            if len(data) == 0:
                break

            request: list = MsgPackForIpc.loads(data)
            address_bytes: bytes = request[2]

            print(request)
            print(f"{request[2].hex()}")

            time.sleep(5)

            response = [
                request[0], request[1], address_bytes, iscore, block_height
            ]
            data: bytes = MsgPackForIpc.dumps(response)
            print(f"C -> S: {data.hex()}")
            sock.send(data)

            block_height += 1

    except Exception as e:
        print(e)
    finally:
        sock.close()


if __name__ == "__main__":
    print("start")
    main()
