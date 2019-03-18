# -*- coding: utf-8 -*-


def main():
    try:
        raise TypeError
    except:
        raise
    finally:
        print('finally')


if __name__ == '__main__':
    main()