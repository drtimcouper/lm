
# positional:

def f1(a,b):
    return a+b

res = f1(2,3)
assert res == 5

res = f1('hello ', 'world')
assert res == 'hello world'

'
def f2(a,b=4):
    return a+b

res = f2(2,3)
assert res == 5

res = f2(2)
assert res ==6


def f3(*args):
    #return a tuple with the arguments in reverse order
    return args[::-1]

res = f3(1,2,'a')
assert res == ('a',2,1)

res = f3(*(1,2,'a'))
assert res == ('a',2,1)

res = f3(1, *(2,'a'))
assert res == ('a',2,1)


def f4(**kwargs):
    return list(sorted(zip(kwargs.keys(), kwargs.values())))

res = f4(**{'a': "letter a", '1': 'number 1'})
assert res == [('1', 'number 1'), ('a', 'letter a')], res

res = f4(b='letter b', **{'2': 'number 2'})
assert res ==  [('2', 'number 2'), ('b', 'letter b')], res

def f5(*a, **k):
    return list(a[::-1]) + sorted(list(k.keys()))

tup = (14, "5a")
d = {'2': 'number 2'}
res = f5(1,2, *tup, y='not', z='snooze', **d)
assert res == ['5a', 14, 2, 1, '2', 'y', 'z']

def f1plus(a,b):
    return a+b, a-b

res = f1plus(5,2)
assert res == (7,3)
mysum, mydiff = f1plus(5,2)
assert mysum == 7
assert mydiff == 3
