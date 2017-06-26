# -*- coding=utf-8 -*-
# 调试

# python -m pdb ***.py
# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace()  # 运行到这里会自动暂停
print 10 / n
