# -*- coding: utf-8 -*-

import logging


def main():
    logging.basicConfig(filename="error.log", level=logging.DEBUG)
    logging.info("hello")

    a = {}

    try:
        print(a["key"])
    except KeyError as e:
        logging.exception("haha")
        raise
    


if __name__ == "__main__":
    main()

