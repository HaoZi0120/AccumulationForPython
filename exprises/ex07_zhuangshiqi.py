# -*- coding=utf-8 -*-
# 装饰器

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now(s):
    print '2013-12-25',s

#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
now('123')

#把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)