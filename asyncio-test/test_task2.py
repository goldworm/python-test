import asyncio
import time


async def nested():
    print('nested')
    return 42


async def recv(n):
    await asyncio.sleep(2)
    return n


async def _pow():
    task = asyncio.create_task(recv(20))
    value = await task
    return value ** 2


async def main():
    task = asyncio.create_task(_pow())
    await asyncio.sleep(3)
    result = await task
    print(result)


start_time: float = time.time()
asyncio.run(main(), debug=True)
print(time.time() - start_time)
