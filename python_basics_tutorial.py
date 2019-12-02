# int
a = 1031
print(a, type(a))  # 1031 <class 'int'>
dir(int)
help(int)
a.bit_length()

# float
print(1., type(1.))  # 1.0 <class 'float'>

import decimal
from decimal import Decimal
decimal.getcontext()
d = Decimal(1) / Decimal(3)
print(d)  # 0.3333333333333333333333333333
decimal.getcontext().prec = 4
e = Decimal(1) / Decimal(3)
print(e)  # 0.3333
print(d + e)  # 0.6666

# bool
T = True
F = False
print(T + 2)  # T is 1 -> 3
print(F - 8)  # F is 0 -> -8

# if X if not 0 or 0.0 then bool(X) is True, else bool(X) is False
print(type(0), bool(0), bool(1))  # <class 'int'> False True
print(type(10.31), bool(0.00), bool(10.31))  # <class 'float'> False True
print(type(True), bool(False), bool(True))  # <class 'bool'> False True

# if X is not null then bool(X) is True, else bool bool(X) if False
print(type(''), bool(''), bool('python'))  # <class 'str'> False True
print(type(()), bool(()), bool((10,)))  # <class 'tuple'> False True
print(type([]), bool([]), bool([1, 2]))  # <class 'list'> False True
print(type({}), bool({}), bool({'a': 1, 'b': 2}))  # <class 'dict'> False True
print(type(set()), bool(set()), bool({1, 2}))  # <class 'set'> False True

# dir(str)
t1 = 'i love Python!'
print(t1, type(t1))
t2 = "I love Python!"
print(t2, type(t2))  # I love Python! <class 'str'>

print(t1.capitalize())  # I love python!
print(t2.split())  # ['I', 'love', 'Python!']
print(t1.find('love'))  # 2
print(t1.find('like'))  # -1
print(t2.replace('love Python', 'hate R'))  # I hate R!
print('http://wwww/python.org'.strip('htp:/'))  # wwww/python.org
print('http://www.python.org'.strip('.org'))  # http://www.python

s = 'Python'
print(s)
print(s[2:4])  # th
print(s[-5:-2])  # yth
print(s[2])   # t
print(s[-1])  # n

# tuple
t1 = (1, 10.31, 'python')
t2 = 1, 10.31, 'python'
print(t1, type(t1))
print(t2, type(t2))  # (1, 10.31, 'python') <class 'tuple'>

print(type(('OK')))  # <class 'str'>
print(type(('OK',)))  # <class 'tuple'>

nested = (1, 10.31, 'python'), ('data', 11)
print(nested[0])  # (1, 10.31, 'python')
print(nested[0][0], nested[0][1], nested[0][2])  # 1 10.31 python
print(nested[0][0:2])  # (1, 10.31)

# tuple is immutable
t = ('OK', [1, 2], True)
# TypeError: 'tuple' object does not support item assigment
# t[2] = False

t[1].append(3)
print(t)  # ('OK', [1, 2, 3], True)
