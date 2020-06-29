# -*- coding: utf-8 -*-


class Base(object):
    def __new__(cls):
        print(f"{cls.__name__}.__new__")
        return super().__new__(cls)

    def __init__(self):
        print(f"Base.__init__")


class Test(Base):
    def __init__(self):
        print(f"Test.__init__")


def main():
    test1 = Test()
    test2 = Test()


if __name__ == "__main__":
    main()

