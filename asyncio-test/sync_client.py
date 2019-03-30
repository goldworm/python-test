import socket
import sys
import os


def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = "/tmp/is.sock"

    try:
        sock.connect(server_address)

        while True:
            text: str = input('> ')
            sock.send(text.encode())
            print(f"C -> S: {text}")

            data: bytes = sock.recv(1024)
            if len(data) == 0:
                break

            text: str = data.decode()
            print(f"S -> C: {text}")

            if text in ("stop", "loopstop"):
                break

    except Exception as e:
        print(e)
    finally:
        sock.close()


if __name__ == "__main__":
    main()
