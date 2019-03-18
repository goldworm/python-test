# -*- coding: utf-8 -*-

import sys
from p1.test import Test
import importlib.machinery


def main():
    print('main')
    print(sys.modules)

    loader = importlib.machinery.SourceFileLoader('cx0000001', '../score/cx0000')
    ret = loader.is_package('cx00001')
    loader.exec_module(self, )

if __name__ == '__main__':
    main()
