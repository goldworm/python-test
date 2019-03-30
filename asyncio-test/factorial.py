# -*- coding: utf-8 -*-

import asyncio


async def factorial(name: str, number: int):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i

    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    result = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

    print(result)


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
