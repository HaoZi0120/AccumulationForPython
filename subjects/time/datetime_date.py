#!/usr/bin/python
# -*- coding:UTF-8 -*-
import datetime
import time

print 'date.max:', datetime.date.max
print 'date.min:', datetime.date.min
print 'date.today():', datetime.date.today()
print 'date.fromtimestamp():', datetime.date.fromtimestamp(time.time())
print

# # ---- 结果 ----
# date.max: 9999-12-31
# date.min: 0001-01-01
# date.today(): 2010-04-06
# date.fromtimestamp(): 2010-04-06

now = datetime.date(2010, 04, 06)
tomorrow = now.replace(day=07)
print 'now:', now, ', tomorrow:', tomorrow
print 'timetuple():', now.timetuple()
print 'weekday():', now.weekday()
print 'isoweekday():', now.isoweekday()
print 'isocalendar():', now.isocalendar()
print 'isoformat():', now.isoformat()
print

# # ---- 结果 ----
# now: 2010-04-06 , tomorrow: 2010-04-07
# timetuple(): (2010, 4, 6, 0, 0, 0, 1, 96, -1)
# weekday(): 1
# isoweekday(): 2
# isocalendar(): (2010, 14, 2)
# isoformat(): 2010-04-06


now = datetime.date.today()
tomorrow = now.replace(day=7)
delta = tomorrow - now
print 'now:', now, ' tomorrow:', tomorrow
print 'timedelta:', delta
print now + delta
print tomorrow > now
print

# # ---- 结果 ----
# now: 2010-04-06  tomorrow: 2010-04-07
# timedelta: 1 day, 0:00:00
# 2010-04-07
# True
