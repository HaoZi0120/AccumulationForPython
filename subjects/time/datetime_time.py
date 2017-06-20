#!/usr/bin/python
# -*- coding:UTF-8 -*-
import datetime
import time

tm = datetime.time(23, 46, 10, 270)
print 'tm:', tm
print 'hour: %d, minute: %d, second: %d, microsecond: %d' \
        % (tm.hour, tm.minute, tm.second, tm.microsecond)
tm1 = tm.replace(hour=20)
print 'tm1:', tm1
print 'isoformat():', tm.isoformat()
print

# # ---- 结果 ----
# tm: 23:46:10.000270
# hour: 23, minute: 46, second: 10, microsecond: 0
# tm1: 20:46:10
# isoformat(): 23:46:10
