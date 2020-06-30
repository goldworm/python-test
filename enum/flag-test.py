# -*- coding: utf-8 -*-

from enum import Flag, auto


class Test(Flag):
    NONE = 0
    A = auto()
    B = auto()
    C = auto()
    D = auto()


def main():
    for flag in Test:
        print(f"{flag}: {flag.value}")


main()
