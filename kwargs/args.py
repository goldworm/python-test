# -*- coding: utf-8 -*-


def sum(a: int = 1, b: int = 2) -> int:
    return a + b


def main():
    args = (10, 20) 
    print(sum(*args))

    args = ()
    print(sum(*args))

    args = None
    print(sum(*args))

if __name__ == "__main__":
    main()

