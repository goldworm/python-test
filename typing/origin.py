# -*- coding: utf-8 -*-

from typing import Dict, List
from typing_extensions import TypedDict


class Person(TypedDict):
    name: str
    age: int


class A(TypedDict):
    pass


def get_origin(type_hint):
    return getattr(type_hint, "__origin__", None)


def get_args(type_hint):
    return getattr(type_hint, "__args__", ())


def main():
    origin = get_origin(Person)
    args = get_args(Person)    
    # print(origin, args)
    # print(Person.__annotations__)
    # print(f"Class: {Person.__class__.__name__}")
    # print(Person.__dict__)
    # print(A.__dict__)
    # print(Dict[str, int].__origin__)

    origin = get_origin(List[int])
    print(origin)
    print(origin is List)


if __name__ == "__main__":
    main()

