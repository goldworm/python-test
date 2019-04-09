# -*- coding: utf-8 -*-

import msgpack
from io import BytesIO

# Copyright 2018 ICON Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import socket
from typing import Any
from typing import Tuple
import msgpack


class Client:
    def __init__(self) -> None:
        self.conn = None
        self.req_sn: int = 0
        self.unpacker = None

    def _send(self, msg: int, data: Any):
        msg_to_send = [msg, data]
        msgpack.dump(msg_to_send, self)

    def _recv(self) -> Tuple[int, Any]:
        msg = self.unpacker.unpack()
        return msg[0], msg[1]

    def connect(self, address: str) -> None:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(address)
        self.conn = sock
        self.unpacker = msgpack.Unpacker(self)

    def write(self, b: bytes) -> None:
        self.conn.sendall(b)

    def read(self, n=None) -> bytes:
        if n is None:
            n = 1024
        return self.conn.recv(n)

    def send(self, msg: int, data: Any):
        self._send(msg, data)

    def send_and_receive(self, msg: int, data: Any) -> Tuple[int, Any]:
        self._send(msg, data)
        return self._recv()

    def receive(self) -> Tuple[int, Any]:
        return self._recv()


def main():
    test_packb()
    test_stream()

def test_packb():
    data = [1, 2 ,3]
    result: bytes = msgpack.packb(data, use_bin_type=True)
    print(result)


def test_stream():
    buf = BytesIO()
    for i in range(100):
       buf.write(msgpack.packb(i, use_bin_type=True))

    buf.seek(0)

    unpacker = msgpack.Unpacker(buf, raw=False)
    for unpacked in unpacker:
        print(unpacked)


if __name__ == '__main__':
    main()
