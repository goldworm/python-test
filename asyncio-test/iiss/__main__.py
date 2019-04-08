# -*- coding: utf-8 -*-

import asyncio

from .reward_calc_proxy import RewardCalcProxy


def main():
    loop = asyncio.get_event_loop()

    path: str = "/tmp/iiss.sock"
    proxy = RewardCalcProxy()

    def func():
        print("func() start")
        proxy.open(path)
        proxy.start()
        print("func() end")

    try:
        loop.call_soon(func)
        loop.run_forever()
        proxy.close()
    finally:
        loop.close()


if __name__ == '__main__':
    main()
