# -*- coding: utf-8 -*-

import inspect


def func(a: int):
    pass


class A:
    def nfunc(self, a: int):
        pass

    @classmethod
    def cfunc(cls, a: int):
        pass

    @staticmethod
    def sfunc(a: int):
        pass


class B(A):
    pass


def do_parameters():
    a = A()
    funcs = [
        func,
        A.nfunc,
        getattr(a, "nfunc"),
        a.nfunc,
        a.nfunc,
        A.cfunc,
        a.cfunc,
        A.sfunc,
        a.sfunc,
    ]

    for f in funcs:
        sig = inspect.signature(f)
        print(f"{f.__qualname__}", sig.parameters)


def main():
    a = A()
    funcs = [
        func,
        A.nfunc,
        getattr(a, "nfunc"),
        a.nfunc,
        A.cfunc,
        a.cfunc,
        A.sfunc,
        a.sfunc,
    ]

    for f in funcs:
        print(f"{f.__qualname__} isfunction={inspect.isfunction(f)} ismethod={inspect.ismethod(f)}")
    
    do_parameters()

    print(A.cfunc.__annotations__)


if __name__ == "__main__":
    main()

