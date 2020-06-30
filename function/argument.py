# -*- coding: utf-8 -*-

def func(a, b):
    print(a, b)


class A:
    def func(a, b):
        print(a, b)


def main():
    args = (1, 2)
    kwargs = {"a":3}
    func(*args, **kwargs)
    

if __name__ == "__main__":
    main()

