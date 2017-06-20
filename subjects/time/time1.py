# !/usr/bin/python
# -*- coding: UTF-8 -*-
import time

ticks = time.time()
print 'ticks:', ticks

local_time = time.localtime(ticks)
print 'local_time:', local_time

asc_time = time.asctime(local_time)
print 'asc_time:', asc_time

str_f_time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print 'str_f_time1:', str_f_time1
str_f_time2 = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
print 'str_f_time2:', str_f_time2

a = '2017-03-13 16:12:16'
str_p_time1 = time.strptime(a, '%Y-%m-%d %H:%M:%S')
print 'str_p_time1:', str_p_time1
b = 'Mon Mar 28 22:24:24 2016'
str_p_time2 = time.strptime(b, '%a %b %d %H:%M:%S %Y')
print 'str_p_time2:', str_p_time2

mk_time = time.mktime(str_p_time1)
print 'mk_time:', mk_time

# % y
# 两位数的年份表示（00 - 99）
# % Y
# 四位数的年份表示（000 - 9999）
# % m
# 月份（01 - 12）
# % d
# 月内中的一天（0 - 31）
# % H
# 24
# 小时制小时数（0 - 23）
# % I
# 12
# 小时制小时数（01 - 12）
# % M
# 分钟数（00 = 59）
# % S
# 秒（00 - 59）
# % a
# 本地简化星期名称
# % A
# 本地完整星期名称
# % b
# 本地简化的月份名称
# % B
# 本地完整的月份名称
# % c
# 本地相应的日期表示和时间表示
# % j
# 年内的一天（001 - 366）
# % p
# 本地A.M.或P.M.的等价符
# % U
# 一年中的星期数（00 - 53）星期天为星期的开始
# % w
# 星期（0 - 6），星期天为星期的开始
# % W
# 一年中的星期数（00 - 53）星期一为星期的开始
# % x
# 本地相应的日期表示
# % X
# 本地相应的时间表示
# % Z
# 当前时区的名称
# % % % 号本身


