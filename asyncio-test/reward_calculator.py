# -*- coding: utf-8 -*-

import msgpack
import socket
import time


def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = "/tmp/iiss.sock"
    block_height: int = 100
    iscore: int = 5

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
                payload: list = request[2]
                address_bytes: bytes = payload[0]

                print(f"request: {request}")
                print(f"{address_bytes.hex()}")

                time.sleep(1)

                payload = [address_bytes, iscore, block_height]
                response = [request[0], request[1], payload]
                print(f"response: {response}")
                data: bytes = msgpack.dumps(response)
                print(f"C -> S: {data.hex()}")
                sock.send(data)

                block_height += 1
                print(f"block_height: {block_height}")

    except Exception as e:
        print(e)
    finally:
        sock.close()


if __name__ == "__main__":
    print("start")
    main()
