from typing import List, get_type_hints, Dict
import inspect


class A:
    pass


def func(a: List["open('hello', 'w')"], b: "A", c: Dict[str, "A"]):
    pass


def main():
    print("get_type_hints(): ", get_type_hints(func))
    print(func.__annotations__)


if __name__ == "__main__":
    main()

