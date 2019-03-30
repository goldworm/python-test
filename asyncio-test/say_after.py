import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def sleep():
    print('sleep start')
    for i in range(100):
        print(f'{i}')
        time.sleep(0.1)
    print('sleep end')


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task0 = asyncio.create_task(sleep())

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task0
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
