# -*- coding: utf-8 -*-

from .base import Base


class Test(Base):
    name = 'p1.Test'

    def __init__(self):
        super().__init__()
        self.value = 'p1.Test'
