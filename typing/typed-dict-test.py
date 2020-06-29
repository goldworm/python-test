# -*- coding: utf-8 -*-

from typing import Dict, List, get_type_hints, Union, get_origin
from typing_extensions import TypedDict, _TypedDictMeta
import inspect


class Address(object):
    def __init__(self):
        self.value = 0


class Delegation(TypedDict):
    address: str
    value: int


def func(a: Delegation, b: Dict[str, int], c: List[int], delegations: List[Delegation], d: str, e: bytes, f: bool, g: Address, h: List, i: Dict, j: List[int]) -> int:
    print("func")


print(get_origin(Delegation))


def main():
    type_hints = get_type_hints(func)

    for i, k in enumerate(type_hints):
        v = type_hints[k]
        print(f"{i:02d}-{k}: {v}")

        if v is List:
            print(dir(v))
            print(v.__parameters__)

        attr = "__origin__"
        if hasattr(v, attr):
            print(f"origin: {getattr(v, attr)}")

        attr = "__annotations__"
        if hasattr(v, attr):
            print(f"annotations: {getattr(v, attr)}")

        if hasattr(v, "__args__"):
            args = getattr(v, "__args__")
            print(f"args: {args}")
            for k in args:
                print(f"{k}")

        if isinstance(v, Dict):
            print("dict")
        elif isinstance(v, List):
            print("list")

        print("----------------------")


if __name__ == "__main__":
    main()

