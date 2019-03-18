# -*- coding: utf-8 -*-


class Base(object):
    name = "p1.Base"

    def __init__(self):
        self._base = 'p1.base'

    def print(self):
        print(self._base)