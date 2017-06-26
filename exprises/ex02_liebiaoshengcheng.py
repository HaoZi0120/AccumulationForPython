# -*- coding=utf-8 -*-
# 列表生成

print 'list(range(1, 10))'
print list(range(1, 10))
print


print '[x * x for x in range(1, 10)]'
print [x * x for x in range(1, 10)]
print

print '[x * x for x in range(1, 11) if x - 4 == 3]'
print [x * x for x in range(1, 11) if x - 4 == 3]
print

print "[m + n for m in 'ABC' for n in 'XYZ']"
print [m + n for m in 'ABC' for n in 'XYZ']
print