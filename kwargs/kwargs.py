# -*- coding: utf-8 -*-


def sum(a: int, b: int = 0) -> int:
    return a + b


def main():
    kwargs = {"a": 10, "b": 0}

    assert sum(**kwargs) == 10


if __name__ == "__main__":
    main()

