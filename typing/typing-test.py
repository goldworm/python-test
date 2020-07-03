# -*- coding: utf-8 -*-

import inspect
from typing import List, Dict, Union, Optional, Tuple
from typing import get_origin, get_args, get_type_hints
from typing_extensions import TypedDict

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
    Union[bool, Union[int, str]],
]


class Person(TypedDict):
    name: str
    age: int


def test_types():

    for _type in types:
        print(get_origin(_type))
        print(get_args(_type))
        print("---------------------------")


def test_types2():
    print("### test_types2()")

    for _type in types:
        try:
            print(_type.__origin__)
            print(_type.__args__)
            print("---------------------------")
        except:
            pass


def test_get_type_hints():
    def f(a: int = None):
        pass

    type_hints = get_type_hints(f)
    print(f"get_type_hints(): {type_hints}")

    sig = inspect.signature(f)
    parameter = sig.parameters["a"]
    print(f"inspect: {parameter.annotation}")


def handle_typed_dict():
    print(Person.__annotations__)


def test_optional():
    def func(a: int = None):
        pass

    sig = inspect.signature(func)
    print(sig.parameters)


def main():

    # test_types()
    test_types2()
    # handle_typed_dict()
    # test_optional()
    test_get_type_hints()


if __name__ == "__main__":
    main()

