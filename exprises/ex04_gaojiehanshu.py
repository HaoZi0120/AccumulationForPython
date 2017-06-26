# -*- coding=utf-8 -*-
# 高阶函数
print '11111'


def add(x, y, f):
    return f(x) + f(y)


print add(5, -6, abs)
print
print '22222'


# map
def f(x):
    return x ** 2


print map(f, [1, 2, 3, 4, 5])
print map(str, [1, 2, 3, 4, 5, ])
print
print '33333'


# reduce


def add(x, y):
    return x + y


print reduce(add, [1, 3, 5, 7, 9])
print
print '44444'


# map+reduce
def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print map(char2num, '13579')
print reduce(fn, map(char2num, '13579'))
print
print '55555'


# map+reduce+lambda

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print str2int('24680')
print
print '66666'


# filter
def is_odd(n):
    return n % 2 == 1


print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
print
print '77777'


def not_empty(s):
    print s and s.strip()
    return s and s.strip()


print filter(not_empty, ['A ', '', 'B', None, 'C', '  '])
print
print '88888'


# sorted
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


print sorted([36, 5, 12, 9, 21], reversed_cmp)
print
print '99999'


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


print sorted(['bob', 'about', 'Zoo', 'Credit'])
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
print
