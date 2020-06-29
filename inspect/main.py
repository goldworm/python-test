# -*- coding: utf-8 -*-

import inspect


def func(a, b: int, c: str) -> int:
    pass


def main():
    sig = inspect.signature(func)
    print(func.__qualname__)
    print(dir(sig))
    


if __name__ == "__main__":
    main()

