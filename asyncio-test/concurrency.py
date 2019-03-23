import asyncio
import threading
import time

[]


def callback(loop):
    print(f'callback(): thread-{threading.get_ident()}')


def query(loop):
    print(f'query(): thread-{threading.get_ident()}')
    loop.call_soon_threadsafe(callback, loop)
    future = asyncio.run_coroutine_threadsafe(coro_func(), loop)
    return future.result() * 10


def invoke():
    for i in range(10):
        print(f'invoke(): thread-{threading.get_ident()} {i}')
        time.sleep(1)

    return 0


async def coro_func():
    print(f'coro_func(): thread-{threading.get_ident()}')
    return await asyncio.sleep(3, result=42)


async def main():
    print(f'main(): thread-{threading.get_ident()}')
    loop = asyncio.get_running_loop()

    future_query = loop.run_in_executor(None, query, loop)
    future_invoke = loop.run_in_executor(None, invoke)

    await asyncio.gather(future_query, future_invoke)

    print(future_query.result())


if __name__ == '__main__':
     asyncio.run(main())
