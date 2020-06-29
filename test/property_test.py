# -*- coding: utf-8 -*-

class Test:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


def main():
    t = Test(0)
    t.value = 100


if __name__ == "__main__":
    main()

