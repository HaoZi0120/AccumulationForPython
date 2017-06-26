# -*-coding=utf-8 -*-
# itertools

import itertools

print '11111'
natuals = itertools.count(1)
t = 0
for n in natuals:
    t += 1
    print n
    if t > 5:
        break
print
print '22222'

t = 0
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
for c in cs:
    print c
    if t > 5:
        break
print
print '33333'

ns = itertools.repeat('A', 5)
for n in ns:
    print n
print
print '44444'

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n
print
print '55555'
t = 0
for c in itertools.chain('ABC', 'XYZ'):
    print c
    if t > 5:
        break