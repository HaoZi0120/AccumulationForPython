# -*- coding=utf-8 -*-
#序列化

import json
d = dict(name='Bob', age=20, score=88)
dj=json.dumps(d)
print dj

c=json.loads(dj)
print c

