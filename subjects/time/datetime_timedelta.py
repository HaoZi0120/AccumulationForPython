#!/usr/bin/python
# -*- coding:UTF-8 -*-
import datetime
import time

now = datetime.datetime.now()
print 'now():', now
some_time = (
    now - datetime.timedelta(days=10, seconds=5, microseconds=10, milliseconds=6, minutes=8,
                             hours=9,
                             weeks=10)).strftime("%Y-%m-%d %H:%M:%S")
print 'some_time:', some_time
