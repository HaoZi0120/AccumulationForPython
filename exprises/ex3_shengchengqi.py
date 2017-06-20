# -*- coding=utf-8 -*-
# 生成器

L = [x * x for x in range(0, 10)]
print 'L', L
print

g = (x * x for x in range(0, 10))
print 'g', g
print

print '11111'


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


fib(6)
print

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
print '22222'


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


for f in fib2(6):
    print f
print
