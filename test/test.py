class Test(object):
    def __str__(self):
        raise KeyError


class TestException(BaseException):
    def __str__(self):
        raise ValueError


class String(str):
    def __str__(self):
        print('call String.__str__')
        return String('hehe')


def haha():
    print('haha')
    return 'haha'

b = 'world'
a = String('hello')

str_a = str(a)
print(f'type of str_a: {type(str_a)}')

print(type(a))
print(type(b))
print(a)
setattr(a, '__str__', haha)
print(a)

print(type(a) == str)

try:
    print('a')
except TestException as e:
    print('haha')
    print(e)

#t = Test()
#text: string = f'text: {t}'
#print(t)
