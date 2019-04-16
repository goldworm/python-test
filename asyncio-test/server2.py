# -*- coding: utf-8 -*-

import asyncio
import threading
import time
import sys

from iconservice.iiss.ipc.reward_calc_proxy import RewardCalcProxy
from iconservice.base.address import Address, AddressPrefix


def run(proxy: 'RewardCalcProxy', delay_s: int):
    print(f"thread start {delay_s}")

    time.sleep(delay_s)

    address = Address.from_data(AddressPrefix.EOA, b'')
    ret: list = proxy.query_iscore(address)
    print(f"ret: {ret}")

    address = Address.from_bytes_including_prefix(ret[0])
    print(f"address: {address}")

    print("thread end")


def main():
    loop = asyncio.get_event_loop()

    path: str = "/tmp/iiss.sock"
    proxy = RewardCalcProxy()

    def func():
        print("func() start")
        proxy.open(path)
        proxy.start()
        print("func() end")

    delay_s: int = int(sys.argv[1])
    thread = threading.Thread(target=run, args=(proxy, delay_s))
    thread.start()
 
#     delay_s: int = int(sys.argv[1])
#     thread = threading.Thread(target=run, args=(proxy, delay_s))
#     thread.start()

    try:
        loop.call_soon(func)
        loop.run_forever()
        proxy.close()
    finally:
        loop.close()


if __name__ == '__main__':
    main()
