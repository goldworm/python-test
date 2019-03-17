# -*- coding: utf-8 -*-


class Base(object):
    def __init__(self):
        self.home = 'seoul'

    def __setattr__(self, key, value):
        print(f'Called Base.__setattr({key}, {value})')
        super().__setattr__(key, value)


class Test(Base):
    def __init__(self):
        self.value = 0
        self.name = 'hello'

    def run(self):
        self.value = 0
        self.age = 20

    def __getattr__(self, key):
        print(f'Called __getattr__({key})')
        return super().__getattr__(key)


def main():
    test = Test()
    test.run()


if __name__ == '__main__':
    main()
