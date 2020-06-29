from typing import List, get_type_hints
import inspect


class A:
    pass


def func(a: List["4+4"]):
    pass


def main():
    # print(get_type_hints(func))
    print(func.__annotations__)


if __name__ == "__main__":
    main()

