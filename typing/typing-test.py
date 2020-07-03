# -*- coding: utf-8 -*-

from typing import get_origin, get_args, List, Dict, Union, Optional, Tuple
from typing_extensions import TypedDict


class Person(TypedDict):
    name: str
    age: int


def handle_typed_dict():
    print(Person.__annotations__)


def main():
    types = [
        list,
        dict,
        List,
        List[int],
        List["int"],
        Dict,
        Dict[str, str],
        Dict[str, "int"],
        Dict["str", int],
        Dict["str", "int"],
        Tuple[int, ...],
        Optional[int],
        Union[int, str],
    ]

    for _type in types:
        print(get_origin(_type))
        print(get_args(_type))
        print("---------------------------")


    print(getattr(types, "haha", None))

    handle_typed_dict()


if __name__ == "__main__":
    main()

