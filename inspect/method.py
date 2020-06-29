# -*- coding: utf-8 -*-

import inspect


def func():
    pass


class A:
    def nfunc(self):
        pass

    @classmethod
    def cfunc(cls):
        pass

    @staticmethod
    def sfunc():
        pass


def main():
    a = A()
    funcs = [
        func,
        A.nfunc,
        a.nfunc,
        A.cfunc,
        a.cfunc,
        A.sfunc,
        a.sfunc,
    ]

    for f in funcs:
        print(f"{f.__name__} isfunction={inspect.isfunction(f)} ismethod={inspect.ismethod(f)}")
    

if __name__ == "__main__":
    main()

