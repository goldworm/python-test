from .utils import haha

class Test(object):
    def __init__(self):
        self.value = 0

    def print(self):
        print(self.value)
        haha()

    def run(self):
        self.value += 1
