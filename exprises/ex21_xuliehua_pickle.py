# -*- coding=utf-8 -*-
#序列化

try:
    import cPickle as pickle
except ImportError:
    import pickle

#首先，我们尝试把一个对象序列化并写入文件：

d = dict(name='Bob', age=20, score=88)
print 'd=',d
#pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

f = open('ex21_dump.txt', 'wb')
pickle.dump(d, f)
f.close()


f = open('ex21_dump.txt', 'rb')
d = pickle.load(f)
f.close()
print 'd=',d