import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def callback(loop):
    print(f'callback(): thread-{threading.get_ident()}')


def query(loop, ret):
    print(f'query() start: thread-{threading.get_ident()}')
    loop.call_soon_threadsafe(callback, loop)

    future = asyncio.run_coroutine_threadsafe(coro_func(ret), loop)
    ret = future.result() * 10

    print(f'query() end: thread-{threading.get_ident()}')

    return ret


def invoke():
    for i in range(10):
        print(f'invoke(): thread-{threading.get_ident()} {i}')
        time.sleep(1)

    return 0


async def coro_func(ret):
    print(f'coro_func(): thread-{threading.get_ident()}')
    return await asyncio.sleep(5, result=ret)


async def main():
    print(f'main(): thread-{threading.get_ident()}')
    loop = asyncio.get_running_loop()

    pool = ThreadPoolExecutor(2)
    future_query1 = loop.run_in_executor(pool, query, loop, 1)
    future_query2 = loop.run_in_executor(pool, query, loop, 2)
    future_invoke = loop.run_in_executor(None, invoke)

    await asyncio.gather(future_query1, future_query2, future_invoke)

    print(future_query1.result())
    print(future_query2.result())


if __name__ == '__main__':
     asyncio.run(main())
